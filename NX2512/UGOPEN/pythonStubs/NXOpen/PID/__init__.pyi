from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Assemblies
import NXOpen.Diagramming.Tables
class AutomaticTableBuilder(NXOpen.Builder): 
    """  Represents a AutomaticTableBuilder.  """
    class ObjectTypeOption(Enum):
        """
        Members Include: 
         |Equipment|  Equipment 
         |InlineEquipment|  Inline quipment, deprecated from nx1872 and combined with NXOpen.PID.AutomaticTableBuilder.ObjectTypeOption.Equipment.
         |Run|  Run 
         |PipeStock|  Pipe Stock 

        """
        Equipment: int
        InlineEquipment: int
        Run: int
        PipeStock: int
        @staticmethod
        def ValueOf(value: int) -> AutomaticTableBuilder.ObjectTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScopeTypeOption(Enum):
        """
        Members Include: 
         |CurrentSheet|  Lists objects in current sheet 
         |OtherSheet|  Lists objects in other sheet 
         |System|  Lists objects in specific system 

        """
        CurrentSheet: int
        OtherSheet: int
        System: int
        @staticmethod
        def ValueOf(value: int) -> AutomaticTableBuilder.ScopeTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StockOption(Enum):
        """
        Members Include: 
         |Pipe|  Pipe Stock 
         |Instrumentation|  Instrumentation Line Stock
         |Hvac|  HVAC Stock 

        """
        Pipe: int
        Instrumentation: int
        Hvac: int
        @staticmethod
        def ValueOf(value: int) -> AutomaticTableBuilder.StockOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ManualUpdate(self) -> bool:
        """
        Getter for property: (bool) ManualUpdate
         Returns the manual update flag.  
           If true, the automatic update will be disabled, the table could be updated manually.   
         
        """
        pass
    @ManualUpdate.setter
    def ManualUpdate(self, manualUpdate: bool):
        """
        Setter for property: (bool) ManualUpdate
         Returns the manual update flag.  
           If true, the automatic update will be disabled, the table could be updated manually.   
         
        """
        pass
    @property
    def ObjectType(self) -> AutomaticTableBuilder.ObjectTypeOption:
        """
        Getter for property: ( AutomaticTableBuilder.ObjectTypeOption NXOp) ObjectType
         Returns the object type.  
             
         
        """
        pass
    @ObjectType.setter
    def ObjectType(self, objectType: AutomaticTableBuilder.ObjectTypeOption):
        """
        Setter for property: ( AutomaticTableBuilder.ObjectTypeOption NXOp) ObjectType
         Returns the object type.  
             
         
        """
        pass
    @property
    def OutputControlLoop(self) -> bool:
        """
        Getter for property: (bool) OutputControlLoop
         Returns the option to output the control loop list.  
           Only applicable when  NXOpen::PID::AutomaticTableBuilder::ScopeType  is  NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun .   
         
        """
        pass
    @OutputControlLoop.setter
    def OutputControlLoop(self, controlLoop: bool):
        """
        Setter for property: (bool) OutputControlLoop
         Returns the option to output the control loop list.  
           Only applicable when  NXOpen::PID::AutomaticTableBuilder::ScopeType  is  NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun .   
         
        """
        pass
    @property
    def OutputEquipment(self) -> bool:
        """
        Getter for property: (bool) OutputEquipment
         Returns the option to output the equipment list.  
           Only applicable when  NXOpen::PID::AutomaticTableBuilder::ScopeType  is  NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment .   
         
        """
        pass
    @OutputEquipment.setter
    def OutputEquipment(self, equipment: bool):
        """
        Setter for property: (bool) OutputEquipment
         Returns the option to output the equipment list.  
           Only applicable when  NXOpen::PID::AutomaticTableBuilder::ScopeType  is  NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment .   
         
        """
        pass
    @property
    def OutputInlineEquipmentValve(self) -> bool:
        """
        Getter for property: (bool) OutputInlineEquipmentValve
         Returns the option to output the inline equipmentvalve list.  
           Only applicable when  NXOpen::PID::AutomaticTableBuilder::ScopeType  is  NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment .   
         
        """
        pass
    @OutputInlineEquipmentValve.setter
    def OutputInlineEquipmentValve(self, inlineEquipmentValve: bool):
        """
        Setter for property: (bool) OutputInlineEquipmentValve
         Returns the option to output the inline equipmentvalve list.  
           Only applicable when  NXOpen::PID::AutomaticTableBuilder::ScopeType  is  NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment .   
         
        """
        pass
    @property
    def OutputInstrumentation(self) -> bool:
        """
        Getter for property: (bool) OutputInstrumentation
         Returns the option to output the instrumentation list.  
           Only applicable when  NXOpen::PID::AutomaticTableBuilder::ScopeType  is  NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment .   
         
        """
        pass
    @OutputInstrumentation.setter
    def OutputInstrumentation(self, instrumentation: bool):
        """
        Setter for property: (bool) OutputInstrumentation
         Returns the option to output the instrumentation list.  
           Only applicable when  NXOpen::PID::AutomaticTableBuilder::ScopeType  is  NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment .   
         
        """
        pass
    @property
    def OutputRun(self) -> bool:
        """
        Getter for property: (bool) OutputRun
         Returns the option to output the run list.  
           Only applicable when  NXOpen::PID::AutomaticTableBuilder::ScopeType  is  NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun .   
         
        """
        pass
    @OutputRun.setter
    def OutputRun(self, run: bool):
        """
        Setter for property: (bool) OutputRun
         Returns the option to output the run list.  
           Only applicable when  NXOpen::PID::AutomaticTableBuilder::ScopeType  is  NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun .   
         
        """
        pass
    @property
    def ScopeType(self) -> AutomaticTableBuilder.ScopeTypeOption:
        """
        Getter for property: ( AutomaticTableBuilder.ScopeTypeOption NXOp) ScopeType
         Returns the scope type.  
             
         
        """
        pass
    @ScopeType.setter
    def ScopeType(self, scopeType: AutomaticTableBuilder.ScopeTypeOption):
        """
        Setter for property: ( AutomaticTableBuilder.ScopeTypeOption NXOp) ScopeType
         Returns the scope type.  
             
         
        """
        pass
    @property
    def Sheet(self) -> Sheet:
        """
        Getter for property: ( Sheet NXOp) Sheet
         Returns the sheet, only available if the ScopeType is OtherSheet.  
             
         
        """
        pass
    @Sheet.setter
    def Sheet(self, sheet: Sheet):
        """
        Setter for property: ( Sheet NXOp) Sheet
         Returns the sheet, only available if the ScopeType is OtherSheet.  
             
         
        """
        pass
    @property
    def StockType(self) -> AutomaticTableBuilder.StockOption:
        """
        Getter for property: ( AutomaticTableBuilder.StockOption NXOp) StockType
         Returns the stock type to output.  
           Only applicable when  NXOpen::PID::AutomaticTableBuilder::ScopeType  is  NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionPipeStock .   
         
        """
        pass
    @StockType.setter
    def StockType(self, stockType: AutomaticTableBuilder.StockOption):
        """
        Setter for property: ( AutomaticTableBuilder.StockOption NXOp) StockType
         Returns the stock type to output.  
           Only applicable when  NXOpen::PID::AutomaticTableBuilder::ScopeType  is  NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionPipeStock .   
         
        """
        pass
    @property
    def System(self) -> NXOpen.Assemblies.Partition:
        """
        Getter for property: ( NXOpen.Assemblies.Partition) System
         Returns the system, only available if the ScopeType is System.  
             
         
        """
        pass
    @System.setter
    def System(self, system: NXOpen.Assemblies.Partition):
        """
        Setter for property: ( NXOpen.Assemblies.Partition) System
         Returns the system, only available if the ScopeType is System.  
             
         
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
    def GetNumberOfPropertyCellRanges(self) -> int:
        """
         Gets the number of property cell ranges. 
         Returns number (int):  the number of property cell ranges .
        """
        pass
    def GetPropertyCellRange(self, index: int) -> PropertyCellRangeBuilder:
        """
         Gets the property cell range at the given index. 
                    The index must be greater than or equal to 0, and less than the number of property cell ranges. 
                
         Returns propertyCellRange ( PropertyCellRangeBuilder NXOp): .
        """
        pass
    def InsertPropertyCellRanges(self, index: int, propertyTypes: List[PropertyType], propertyKeys: List[str]) -> None:
        """
         Inserts the given number of property cell ranges at the given index. 
                    The index must be greater than or equal to 0, and less than or equal to the number of property cell ranges.
                    The number of property types and the number of property keys must be same, and must be greater than 0.
                
        """
        pass
    def RemovePropertyCellRanges(self, index: int, number: int) -> None:
        """
         Removes the given number of property cell ranges starting with the given index. 
                    The index must be greater than or equal to 0, and less than the number of property cell ranges.
                    The number must be greater than 0, and "index + number" must be less than or equal to the number of property cell ranges.
                
        """
        pass
import NXOpen
class AutomaticTableCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of AutomaticTable. """
    def FindObject(self, journalIdentifier: str) -> AutomaticTable:
        """
         Finds the NXOpen.PID.AutomaticTable with the given identifier as recorded in a journal.
                   An exception will be thrown if no object can be found with given name. 
         Returns automaticTable ( AutomaticTable NXOp):  NXOpen.PID.AutomaticTable with this name. .
        """
        pass
    def ReadFromTemplate(self, templatePartName: str) -> AutomaticTable:
        """
         Reads the NXOpen.PID.AutomaticTable from template part. 
                    Opens the template part with specified part name, and copies the NXOpen.PID.AutomaticTable from template part to this sheet.
                
         Returns automaticTable ( AutomaticTable NXOp):  the new NXOpen.PID.AutomaticTable .
        """
        pass
    @overload
    def SaveAsTemplate(self, automaticTable: AutomaticTable, templatePartName: str) -> None:
        """
         Saves the NXOpen.PID.AutomaticTable as template part. 
                    Creates a template part with specified part name, and copies the NXOpen.PID.AutomaticTable to the template part.
                
        """
        pass
    @overload
    def SaveAsTemplate(self, automaticTable: AutomaticTable, builder: PartOperationCreateBuilder) -> None:
        """
         Saves the NXOpen.PID.AutomaticTable as template part. 
                    Creates a template part with specified part name on PartOperationCreateBuilder, and copies the NXOpen.PID.AutomaticTable to the template part.
                
        """
        pass
import NXOpen
import NXOpen.Diagramming.Tables
class AutomaticTable(NXOpen.NXObject): 
    """  the automatic table for PID objects  """
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
class BulkEditBuilder(NXOpen.Builder): 
    """
    Represents a BulkEditBuilder to edit bulk of objects.
    """
    @property
    def RenderingProperties(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) RenderingProperties
         Returns the line rendering properties.  
             
         
        """
        pass
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
import NXOpen
class DesignContextBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs PID Design Context operations.
        """
    @property
    def ConfigurationContext(self) -> ConfigurationContextBuilder:
        """
        Getter for property: ( ConfigurationContextBuilder NXOp) ConfigurationContext
         Returns the configuration context builder.  
             
         
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
import NXOpen
import NXOpen.Diagramming
class EquipmentBuilder(NXOpen.Builder): 
    """ 
    Builder used to model a piece of Equipment. 
    """
    @property
    def ExistingSymbol(self) -> NXOpen.Diagramming.Node:
        """
        Getter for property: ( NXOpen.Diagramming.Node) ExistingSymbol
         Returns the symbol from foundation window.  
           It is only applicable when  PID::EquipmentBuilder::SymbolSourceType  is  PID::SymbolSourceOptionExistingSymbol .  
         
        """
        pass
    @ExistingSymbol.setter
    def ExistingSymbol(self, existingSymbol: NXOpen.Diagramming.Node):
        """
        Setter for property: ( NXOpen.Diagramming.Node) ExistingSymbol
         Returns the symbol from foundation window.  
           It is only applicable when  PID::EquipmentBuilder::SymbolSourceType  is  PID::SymbolSourceOptionExistingSymbol .  
         
        """
        pass
    @property
    def ExistingSymbolLogicalElementRevision(self) -> Equipment:
        """
        Getter for property: ( Equipment NXOp) ExistingSymbolLogicalElementRevision
         Returns the Logical Element Revision for the symbol.  
           It is only applicable when  PID::EquipmentBuilder::SymbolSourceType  is  PID::SymbolSourceOptionLogicalElementRevision .  
         
        """
        pass
    @ExistingSymbolLogicalElementRevision.setter
    def ExistingSymbolLogicalElementRevision(self, existingSymbolLogicalElementRevision: Equipment):
        """
        Setter for property: ( Equipment NXOp) ExistingSymbolLogicalElementRevision
         Returns the Logical Element Revision for the symbol.  
           It is only applicable when  PID::EquipmentBuilder::SymbolSourceType  is  PID::SymbolSourceOptionLogicalElementRevision .  
         
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
    def FulfillmentAttributeOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) FulfillmentAttributeOwner
         Returns the owner of fulfillment attributes group.  
            
         
        """
        pass
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the tag of this equipment.  
             
         
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
    def NeedAttrOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) NeedAttrOwner
         Returns the owner of need attributes group.  
            
         
        """
        pass
    @property
    def NeedAttributeOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) NeedAttributeOwner
         Returns the owner of need attributes group.  
            
         
        """
        pass
    @property
    def NodeId(self) -> str:
        """
        Getter for property: (str) NodeId
         Returns the current node ID of this equipment.  
           It works only in edit mode, it's optional and the first node ID stored in the equipment will be used as default.  
         
        """
        pass
    @NodeId.setter
    def NodeId(self, nodeId: str):
        """
        Setter for property: (str) NodeId
         Returns the current node ID of this equipment.  
           It works only in edit mode, it's optional and the first node ID stored in the equipment will be used as default.  
         
        """
        pass
    @property
    def OwningSheet(self) -> Sheet:
        """
        Getter for property: ( Sheet NXOp) OwningSheet
         Returns the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    @OwningSheet.setter
    def OwningSheet(self, owningSheet: Sheet):
        """
        Setter for property: ( Sheet NXOp) OwningSheet
         Returns the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    @property
    def Rotate(self) -> RotateAngleOption:
        """
        Getter for property: ( RotateAngleOption NXOp) Rotate
         Returns the symbol rotation angle.  
             
         
        """
        pass
    @Rotate.setter
    def Rotate(self, rotate: RotateAngleOption):
        """
        Setter for property: ( RotateAngleOption NXOp) Rotate
         Returns the symbol rotation angle.  
             
         
        """
        pass
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the scale value.  
           It is only applicable when  PID::EquipmentBuilder::LockAspectRatio  is true.  
         
        """
        pass
    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the scale value.  
           It is only applicable when  PID::EquipmentBuilder::LockAspectRatio  is true.  
         
        """
        pass
    @property
    def ScaleX(self) -> float:
        """
        Getter for property: (float) ScaleX
         Returns the x scale value.  
           It is only applicable when  PID::EquipmentBuilder::LockAspectRatio  is false.  
         
        """
        pass
    @ScaleX.setter
    def ScaleX(self, scaleX: float):
        """
        Setter for property: (float) ScaleX
         Returns the x scale value.  
           It is only applicable when  PID::EquipmentBuilder::LockAspectRatio  is false.  
         
        """
        pass
    @property
    def ScaleY(self) -> float:
        """
        Getter for property: (float) ScaleY
         Returns the y scale value.  
           It is only applicable when  PID::EquipmentBuilder::LockAspectRatio  is false.  
         
        """
        pass
    @ScaleY.setter
    def ScaleY(self, scaleY: float):
        """
        Setter for property: (float) ScaleY
         Returns the y scale value.  
           It is only applicable when  PID::EquipmentBuilder::LockAspectRatio  is false.  
         
        """
        pass
    @property
    def SymbolId(self) -> str:
        """
        Getter for property: (str) SymbolId
         Returns the symbol ID of this equipment.  
           It is only applicable when  NXOpen::PID::EquipmentBuilder::SymbolSourceType  is  NXOpen::PID::SymbolSourceOptionReuseLibrary .  
         
        """
        pass
    @SymbolId.setter
    def SymbolId(self, symbolId: str):
        """
        Setter for property: (str) SymbolId
         Returns the symbol ID of this equipment.  
           It is only applicable when  NXOpen::PID::EquipmentBuilder::SymbolSourceType  is  NXOpen::PID::SymbolSourceOptionReuseLibrary .  
         
        """
        pass
    @property
    def SymbolSourceType(self) -> SymbolSourceOption:
        """
        Getter for property: ( SymbolSourceOption NXOp) SymbolSourceType
         Returns the symbol source type   
            
         
        """
        pass
    @SymbolSourceType.setter
    def SymbolSourceType(self, symbolSourceType: SymbolSourceOption):
        """
        Setter for property: ( SymbolSourceOption NXOp) SymbolSourceType
         Returns the symbol source type   
            
         
        """
        pass
    @property
    def UseExistingID(self) -> bool:
        """
        Getter for property: (bool) UseExistingID
         Returns the option to place a duplicate symbol.  
           It is only applicable when  NXOpen::PID::EquipmentBuilder::SymbolSourceType  is  NXOpen::PID::SymbolSourceOptionExistingSymbol .  
         
        """
        pass
    @UseExistingID.setter
    def UseExistingID(self, useExistingID: bool):
        """
        Setter for property: (bool) UseExistingID
         Returns the option to place a duplicate symbol.  
           It is only applicable when  NXOpen::PID::EquipmentBuilder::SymbolSourceType  is  NXOpen::PID::SymbolSourceOptionExistingSymbol .  
         
        """
        pass
    def DetachAllConnections(self) -> None:
        """
         Detaches the equipment from all attached connections. 
        """
        pass
    def GetInlineSymbolLocation(self) -> Tuple[Pipe, str, int, float]:
        """
         Gets connection location for the inline symbol. 
         Returns A tuple consisting of (pipe, connectionId, segementId, percent). 
         - pipe is:  Pipe NXOp.
         - connectionId is: str.
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
    def GetNewInlineConnection(self) -> Tuple[Pipe, str]:
        """
         Gets new connection after inserting an inline symbol. 
         Returns A tuple consisting of (pipe, connectionId). 
         - pipe is:  Pipe NXOp.
         - connectionId is: str.

        """
        pass
    def GetNode(self) -> NXOpen.Diagramming.Node:
        """
         Get the node object of the equipment builder. 
         Returns node ( NXOpen.Diagramming.Node): .
        """
        pass
    def SetAttachedSymbol(self, fromPortId: str, toSymbol: NXOpen.NXObject, toSymbolNodeSidId: str, toSymbolPortId: str) -> None:
        """
         Sets the attached symbol. 
        """
        pass
    def SetFulfillment(self, symbolID: str) -> None:
        """
         Sets the fulfillment data of the symbol. The input symbol should be a 3D one and in the same category with the entity of the builder
        """
        pass
    def SetInlineSymbolLocation(self, pipe: Pipe, connectionId: str, segementId: int, percent: float) -> None:
        """
         Sets connection location for the inline symbol. 
        """
        pass
    def SetLocation(self, location: NXOpen.Point2d) -> None:
        """
         Sets the symbol location. 
        """
        pass
class Equipment(LogicalElementRevision): 
    """ Represents the equipment class. """
    def GetPort(self, portId: str) -> Port:
        """
         Get one port of the equipment by port ID.
         Returns port ( Port NXOp): .
        """
        pass
    def GetPorts(self) -> List[Port]:
        """
         Get ports of the equipment.
         Returns ports ( Port List[NX): .
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Gateway
class FileNewApplicationBuilder(NXOpen.Gateway.IGenericFileNewApplicationBuilder): 
    """ Represents a builder class that performs Generic File New operations.
        """
    @property
    def DisplayPartOption(self) -> NXOpen.DisplayPartOption:
        """
        Getter for property: ( NXOpen.DisplayPartOption) DisplayPartOption
         Returns the display part option for the new file being created   
            
         
        """
        pass
    @DisplayPartOption.setter
    def DisplayPartOption(self, displayPartOption: NXOpen.DisplayPartOption):
        """
        Setter for property: ( NXOpen.DisplayPartOption) DisplayPartOption
         Returns the display part option for the new file being created   
            
         
        """
        pass
    @property
    def TemplateBaseTcType(self) -> str:
        """
        Getter for property: (str) TemplateBaseTcType
         Returns the BaseTCType of the template part from which to create the new file   
            
         
        """
        pass
    @TemplateBaseTcType.setter
    def TemplateBaseTcType(self, baseTCType: str):
        """
        Setter for property: (str) TemplateBaseTcType
         Returns the BaseTCType of the template part from which to create the new file   
            
         
        """
        pass
    @property
    def TemplateFileName(self) -> str:
        """
        Getter for property: (str) TemplateFileName
         Returns the name of the template part from which to create the new file   
            
         
        """
        pass
    @TemplateFileName.setter
    def TemplateFileName(self, templateFileName: str):
        """
        Setter for property: (str) TemplateFileName
         Returns the name of the template part from which to create the new file   
            
         
        """
        pass
    @property
    def TemplatePresentationName(self) -> str:
        """
        Getter for property: (str) TemplatePresentationName
         Returns the presentation name of the underlying template which is used for creating new file    
            
         
        """
        pass
    @TemplatePresentationName.setter
    def TemplatePresentationName(self, presentationName: str):
        """
        Setter for property: (str) TemplatePresentationName
         Returns the presentation name of the underlying template which is used for creating new file    
            
         
        """
        pass
    @property
    def TemplateTcType(self) -> str:
        """
        Getter for property: (str) TemplateTcType
         Returns the TCType of the template part from which to create the new file   
            
         
        """
        pass
    @TemplateTcType.setter
    def TemplateTcType(self, tcType: str):
        """
        Setter for property: (str) TemplateTcType
         Returns the TCType of the template part from which to create the new file   
            
         
        """
        pass
    @property
    def TemplateType(self) -> NXOpen.FileNewTemplateType:
        """
        Getter for property: ( NXOpen.FileNewTemplateType) TemplateType
         Returns the template type for the new file being created   
            
         
        """
        pass
    @TemplateType.setter
    def TemplateType(self, templateType: NXOpen.FileNewTemplateType):
        """
        Setter for property: ( NXOpen.FileNewTemplateType) TemplateType
         Returns the template type for the new file being created   
            
         
        """
        pass
    @property
    def TemplateUnits(self) -> NXOpen.Part.Units:
        """
        Getter for property: ( NXOpen.Part.Units) TemplateUnits
         Returns the units for the new file being created   
            
         
        """
        pass
    @TemplateUnits.setter
    def TemplateUnits(self, units: NXOpen.Part.Units):
        """
        Setter for property: ( NXOpen.Part.Units) TemplateUnits
         Returns the units for the new file being created   
            
         
        """
        pass
    def GetCollaborativeDesign(self) -> NXOpen.CollaborativeDesign:
        """
         The NXOpen.CollaborativeDesign of the subset.
                
         Returns collaborativeDesign ( NXOpen.CollaborativeDesign): .
        """
        pass
    def GetTargetPartitions(self) -> List[NXOpen.Assemblies.Partition]:
        """
         The NXOpen.Assemblies.Partition of the subset.
                
         Returns partitions ( NXOpen.Assemblies.Partition Li): .
        """
        pass
    def SetCollaborativeDesign(self, collaborativeDesign: NXOpen.CollaborativeDesign) -> None:
        """
         The NXOpen.CollaborativeDesign of the subset.
                
        """
        pass
    def SetTargetPartitions(self, partitions: List[NXOpen.Assemblies.Partition]) -> None:
        """
         The Assemblies.Partition of the subset.
                
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
    def GetConnection(self) -> Tuple[Pipe, str]:
        """
         Gets the connection for this Flow Direction Arrow. 
         Returns A tuple consisting of (pipe, connectionId). 
         - pipe is:  Pipe NXOp.
         - connectionId is: str.

        """
        pass
    def ReverseDirection(self) -> None:
        """
         Change the direction of FDA. 
        """
        pass
    def SetConnection(self, equipment: Pipe, connectionId: str) -> None:
        """
         Sets the connection for this Flow Direction Arrow. 
        """
        pass
import NXOpen
class FlowDirectionArrowCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of FlowDirectionArrow. """
    def FindObject(self, journalIdentifier: str) -> FlowDirectionArrow:
        """
         Finds the PID.FlowDirectionArrow with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns flowdirectionarrow ( FlowDirectionArrow NXOp):  PID.FlowDirectionArrow with this name. .
        """
        pass
import NXOpen
class FlowDirectionArrow(NXOpen.NXObject): 
    """  A symbol that indicates the direction the of the flow """
    pass
import NXOpen
import NXOpen.Diagramming
import NXOpen.PLAS
class InstrumentationBuilder(NXOpen.Builder): 
    """ Represents a PID.InstrumentationSymbol and PID.Instrumentationbuilder """
    @property
    def ControlLoopName(self) -> str:
        """
        Getter for property: (str) ControlLoopName
         Returns the control loop name.  
           Used under native mode or instrumentation lightweight mode.   
         
        """
        pass
    @ControlLoopName.setter
    def ControlLoopName(self, controlLoopName: str):
        """
        Setter for property: (str) ControlLoopName
         Returns the control loop name.  
           Used under native mode or instrumentation lightweight mode.   
         
        """
        pass
    @property
    def FunctionId(self) -> str:
        """
        Getter for property: (str) FunctionId
         Returns the function   
            
         
        """
        pass
    @FunctionId.setter
    def FunctionId(self, functionId: str):
        """
        Setter for property: (str) FunctionId
         Returns the function   
            
         
        """
        pass
    @property
    def InstrumentationType(self) -> InstrumentationType:
        """
        Getter for property: ( InstrumentationType NXOp) InstrumentationType
         Returns the instrumentation type   
            
         
        """
        pass
    @InstrumentationType.setter
    def InstrumentationType(self, type: InstrumentationType):
        """
        Setter for property: ( InstrumentationType NXOp) InstrumentationType
         Returns the instrumentation type   
            
         
        """
        pass
    @property
    def LeaderArrowhead(self) -> NXOpen.Diagramming.DiagrammingArrowtype:
        """
        Getter for property: ( NXOpen.Diagramming.DiagrammingArrowtype) LeaderArrowhead
         Returns the arrow type of the end arrow.  
           Only used when the instrumentation type is  NXOpen::PID::InstrumentationTypeAnnotation   
         
        """
        pass
    @LeaderArrowhead.setter
    def LeaderArrowhead(self, arrowTypeOption: NXOpen.Diagramming.DiagrammingArrowtype):
        """
        Setter for property: ( NXOpen.Diagramming.DiagrammingArrowtype) LeaderArrowhead
         Returns the arrow type of the end arrow.  
           Only used when the instrumentation type is  NXOpen::PID::InstrumentationTypeAnnotation   
         
        """
        pass
    @property
    def LeaderStubLength(self) -> float:
        """
        Getter for property: (float) LeaderStubLength
         Returns the stub length of this leader line.  
           The negative value is not expected, and only used when the instrumentation type is  NXOpen::PID::InstrumentationTypeAnnotation   
         
        """
        pass
    @LeaderStubLength.setter
    def LeaderStubLength(self, stubLength: float):
        """
        Setter for property: (float) LeaderStubLength
         Returns the stub length of this leader line.  
           The negative value is not expected, and only used when the instrumentation type is  NXOpen::PID::InstrumentationTypeAnnotation   
         
        """
        pass
    @property
    def LeaderStubSide(self) -> NXOpen.Diagramming.DiagrammingStubsides:
        """
        Getter for property: ( NXOpen.Diagramming.DiagrammingStubsides) LeaderStubSide
         Returns the stub sides of this leader line.  
           Only used when the instrumentation type is  NXOpen::PID::InstrumentationTypeAnnotation   
         
        """
        pass
    @LeaderStubSide.setter
    def LeaderStubSide(self, stubSides: NXOpen.Diagramming.DiagrammingStubsides):
        """
        Setter for property: ( NXOpen.Diagramming.DiagrammingStubsides) LeaderStubSide
         Returns the stub sides of this leader line.  
           Only used when the instrumentation type is  NXOpen::PID::InstrumentationTypeAnnotation   
         
        """
        pass
    @property
    def LeaderUsed(self) -> bool:
        """
        Getter for property: (bool) LeaderUsed
         Returns the option to use leader.  
           Only used when the instrumentation type is  NXOpen::PID::InstrumentationTypeAnnotation   
         
        """
        pass
    @LeaderUsed.setter
    def LeaderUsed(self, isLeaderUsed: bool):
        """
        Setter for property: (bool) LeaderUsed
         Returns the option to use leader.  
           Only used when the instrumentation type is  NXOpen::PID::InstrumentationTypeAnnotation   
         
        """
        pass
    @property
    def MeasurementVariable(self) -> str:
        """
        Getter for property: (str) MeasurementVariable
         Returns the measured variable   
            
         
        """
        pass
    @MeasurementVariable.setter
    def MeasurementVariable(self, measurementVariable: str):
        """
        Setter for property: (str) MeasurementVariable
         Returns the measured variable   
            
         
        """
        pass
    @property
    def OwningControlLoop(self) -> NXOpen.PLAS.Run:
        """
        Getter for property: ( NXOpen.PLAS.Run) OwningControlLoop
         Returns the control loop.  
            Used under manager mode or instrumentation non-lightweight mode.   
         
        """
        pass
    @OwningControlLoop.setter
    def OwningControlLoop(self, controlLoop: NXOpen.PLAS.Run):
        """
        Setter for property: ( NXOpen.PLAS.Run) OwningControlLoop
         Returns the control loop.  
            Used under manager mode or instrumentation non-lightweight mode.   
         
        """
        pass
    @property
    def OwningControlLoopType(self) -> InstrumentationControlLoopType:
        """
        Getter for property: ( InstrumentationControlLoopType NXOp) OwningControlLoopType
         Returns the owning control loop option   
            
         
        """
        pass
    @OwningControlLoopType.setter
    def OwningControlLoopType(self, type: InstrumentationControlLoopType):
        """
        Setter for property: ( InstrumentationControlLoopType NXOp) OwningControlLoopType
         Returns the owning control loop option   
            
         
        """
        pass
    @property
    def SymbolSize(self) -> float:
        """
        Getter for property: (float) SymbolSize
         Returns the symbol size   
            
         
        """
        pass
    @SymbolSize.setter
    def SymbolSize(self, symbolSize: float):
        """
        Setter for property: (float) SymbolSize
         Returns the symbol size   
            
         
        """
        pass
    @property
    def SymbolType(self) -> InstrumentationSymbolType:
        """
        Getter for property: ( InstrumentationSymbolType NXOp) SymbolType
         Returns the symbol type   
            
         
        """
        pass
    @SymbolType.setter
    def SymbolType(self, symbolType: InstrumentationSymbolType):
        """
        Setter for property: ( InstrumentationSymbolType NXOp) SymbolType
         Returns the symbol type   
            
         
        """
        pass
    @property
    def TextStyle(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.TextStyleBuilder) TextStyle
         Returns the text style   
            
         
        """
        pass
    def Detach(self) -> None:
        """
         Detaches the instrumentation from its attachments. Only used when the instrumentation type is NXOpen.PID.InstrumentationType.Symbol
        """
        pass
    def GetInlineSymbolLocation(self) -> Tuple[NXOpen.NXObject, str, int, float]:
        """
         Gets connection location for the inline symbol. Only used when the instrumentation type is NXOpen.PID.InstrumentationType.Symbol and the instrument is inserted into one pipe.
         Returns A tuple consisting of (pipe, connectionId, segementId, percent). 
         - pipe is:  NXOpen.NXObject. NXOpen.PID.NativePipe or NXOpen.PID.Pipe.
         - connectionId is: str.
         - segementId is: int.
         - percent is: float.

        """
        pass
    def GetLeaderTerminator(self) -> Tuple[NXOpen.Diagramming.SheetElement, NXOpen.Point2d, int]:
        """
         Gets the reference object and point of the instrumentation annotation. Only used when the instrumentation type is NXOpen.PID.InstrumentationType.Annotation
         Returns A tuple consisting of (reference, point, connectionSegementId). 
         - reference is:  NXOpen.Diagramming.SheetElement.
         - point is:  NXOpen.Point2d. the instrumentation annotation's leader point. .
         - connectionSegementId is: int.

        """
        pass
    def GetLocation(self) -> NXOpen.Point2d:
        """
         Gets the instrumentation location. 
         Returns location ( NXOpen.Point2d):  the instrumentation location. .
        """
        pass
    def GetNewInlineConnection(self) -> Tuple[NXOpen.NXObject, str]:
        """
         Gets new pipe after inserting an inline symbol. Only used when the instrumentation type is NXOpen.PID.InstrumentationType.Symbol and the instrument is inserted into one pipe.
         Returns A tuple consisting of (pipe, connectionId). 
         - pipe is:  NXOpen.NXObject. NXOpen.PID.NativePipe or NXOpen.PID.Pipe.
         - connectionId is: str.

        """
        pass
    def GetNode(self) -> NXOpen.Diagramming.Node:
        """
         Get the node object of the instrumentation. 
         Returns node ( NXOpen.Diagramming.Node): .
        """
        pass
    def SetAttachedInstrumentSymbol(self, fromPortId: str, toInstrumentSymbol: NXOpen.NXObject, toPortId: str) -> None:
        """
         Set the attached instrument symbol. Only used when the instrumentation type is NXOpen.PID.InstrumentationType.Symbol
        """
        pass
    def SetInlineSymbolLocation(self, pipe: NXOpen.NXObject, connectionId: str, segementId: int, percent: float) -> None:
        """
         Sets connection location for the inline symbol. Only used when the instrumentation type is NXOpen.PID.InstrumentationType.Symbol and the instrument is inserted into one pipe.
        """
        pass
    def SetLeaderTerminator(self, reference: NXOpen.Diagramming.SheetElement, point: NXOpen.Point2d, connectionSegementId: int) -> None:
        """
         Sets the reference object and point of the instrumentation annotation. Only used when the instrumentation type is NXOpen.PID.InstrumentationType.Annotation
        """
        pass
    def SetLocation(self, location: NXOpen.Point2d) -> None:
        """
         Sets the instrumentation location. 
        """
        pass
class InstrumentationControlLoopDisplay(Enum):
    """
    Members Include: 
     |Id|  control loop Id. 
     |Name|  control loop name. 
     |Blank|  no display. 

    """
    Id: int
    Name: int
    Blank: int
    @staticmethod
    def ValueOf(value: int) -> InstrumentationControlLoopDisplay:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class InstrumentationControlLoopType(Enum):
    """
    Members Include: 
     |Unassigned|  unassigned control loop. 
     |Active|  active control loop. 
     |Inferred|  inferred control loop. 
     |Specified|  specified control loop. 

    """
    Unassigned: int
    Active: int
    Inferred: int
    Specified: int
    @staticmethod
    def ValueOf(value: int) -> InstrumentationControlLoopType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
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
class InstrumentationSymbol(Equipment): 
    """ Represents the InstrumentationSymbol class. """
    pass
class InstrumentationType(Enum):
    """
    Members Include: 
     |Symbol|  instrumentation symbol. 
     |Annotation|  instrumentation annotation. 

    """
    Symbol: int
    Annotation: int
    @staticmethod
    def ValueOf(value: int) -> InstrumentationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.DiagrammingLibraryAuthor
class LibraryAuthoringBuilder(NXOpen.Builder): 
    """  Represents a LibraryAuthoringBuilder.  
        Calling Builder.Commit on this builder will only return . """
    @property
    def LineTypes(self) -> NXOpen.DiagrammingLibraryAuthor.LineTypeBuilderList:
        """
        Getter for property: ( NXOpen.DiagrammingLibraryAuthor.LineTypeBuilderList) LineTypes
         Returns the list of line types.  
             
         
        """
        pass
    @property
    def OutputFolder(self) -> str:
        """
        Getter for property: (str) OutputFolder
         Returns the output folder for generated files.  
             
         
        """
        pass
    @OutputFolder.setter
    def OutputFolder(self, outputFolder: str):
        """
        Setter for property: (str) OutputFolder
         Returns the output folder for generated files.  
             
         
        """
        pass
    @property
    def PipeStock(self) -> NXOpen.DiagrammingLibraryAuthor.PipeStockBuilder:
        """
        Getter for property: ( NXOpen.DiagrammingLibraryAuthor.PipeStockBuilder) PipeStock
         Returns the pipe stock sub-builder.  
             
         
        """
        pass
    @property
    def Symbol2D(self) -> NXOpen.DiagrammingLibraryAuthor.Symbol2DBuilder:
        """
        Getter for property: ( NXOpen.DiagrammingLibraryAuthor.Symbol2DBuilder) Symbol2D
         Returns the symbol 2D sub-builder.  
             
         
        """
        pass
    @property
    def Symbol3D(self) -> NXOpen.DiagrammingLibraryAuthor.Symbol3DBuilder:
        """
        Getter for property: ( NXOpen.DiagrammingLibraryAuthor.Symbol3DBuilder) Symbol3D
         Returns the symbol 3D sub-builder.  
             
         
        """
        pass
    def Create3DSymbol(self, instanceId: str, partId: str, partName: str, numberName: str) -> NXOpen.DiagrammingLibraryAuthor.AttributeHolder:
        """
         Creates a new 3D symbol 
         Returns symbolObject ( NXOpen.DiagrammingLibraryAuthor.AttributeHolder):  the symbol object .
        """
        pass
    def CreateLineType(self) -> NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder:
        """
         Creates a new line type 
         Returns lineType ( NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder): .
        """
        pass
    def Delete3DSymbol(self, symbolObject: NXOpen.DiagrammingLibraryAuthor.AttributeHolder) -> None:
        """
         Deletes the 3D symbol which is new created 
        """
        pass
    def GetSymbolObjects(self) -> List[NXOpen.DiagrammingLibraryAuthor.AttributeHolder]:
        """
         Gets the symbol objects which have user attributes of the symbol. 
         Returns symbolObjects ( NXOpen.DiagrammingLibraryAuthor.AttributeHolder Li):  the symbol objects .
        """
        pass
    def SelectFolder(self, classId: str, symbolId: str) -> None:
        """
         Selects the all symbols in the folder by the 2D symbol ID 
        """
        pass
    def SelectSymbol(self, symbolId: str) -> None:
        """
         Selects one 2D symbol or 3D symbol by the symbol ID 
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

        """
        SmallFilledArrowOut: int
        SmallFilledArrowIn: int
        Box: int
        ChevronOut: int
        ChevronIn: int
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
        Getter for property: ( Sheet NXOp) OwningSheet
         Returns the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    @OwningSheet.setter
    def OwningSheet(self, owningSheet: Sheet):
        """
        Setter for property: ( Sheet NXOp) OwningSheet
         Returns the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    @property
    def RotateOption(self) -> RotateAngleOption:
        """
        Getter for property: ( RotateAngleOption NXOp) RotateOption
         Returns the symbol rotation angle.  
             
         
        """
        pass
    @RotateOption.setter
    def RotateOption(self, rotate: RotateAngleOption):
        """
        Setter for property: ( RotateAngleOption NXOp) RotateOption
         Returns the symbol rotation angle.  
             
         
        """
        pass
    @property
    def Style(self) -> OffSheetConnectorBuilder.StyleOption:
        """
        Getter for property: ( OffSheetConnectorBuilder.StyleOption NXOp) Style
         Returns the style of OSC   
            
         
        """
        pass
    @Style.setter
    def Style(self, style: OffSheetConnectorBuilder.StyleOption):
        """
        Setter for property: ( OffSheetConnectorBuilder.StyleOption NXOp) Style
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
    def GetConnection(self) -> Tuple[ConnectionEndType, Pipe, str]:
        """
         To get the connection connecting to the OSC sheet element.
         Returns A tuple consisting of (type, connection, connectionId). 
         - type is:  ConnectionEndType NXOp.
         - connection is:  Pipe NXOp.
         - connectionId is: str.

        """
        pass
    def GetLocation(self) -> NXOpen.Point2d:
        """
         Gets the symbol location. 
         Returns location ( NXOpen.Point2d):  the symbol location. .
        """
        pass
    def GetNode(self) -> NXOpen.Diagramming.Node:
        """
         Get the node object of the off sheet connector builder. 
         Returns node ( NXOpen.Diagramming.Node): .
        """
        pass
    def LinkOSC(self, desObject: OffSheetConnector) -> None:
        """
         Links to the destination OSC. If the input OffSheetConnector is NULL, it means break the existing link.  
        """
        pass
    def Rotate(self) -> None:
        """
         To rotate a off sheet connector
        """
        pass
    def SetConnection(self, type: ConnectionEndType, connection: Pipe, connectionId: str) -> None:
        """
         To set the connection connecting to the OSC sheet element.
        """
        pass
    def SetLocation(self, location: NXOpen.Point2d) -> None:
        """
         Sets the symbol location. 
        """
        pass
import NXOpen.Diagramming
class OffSheetConnector(CrossSheetReference): 
    """ Represents the off sheet connector class. """
    def GetConnections(self) -> List[NXOpen.Diagramming.Connection]:
        """
         Get connections of this off sheet connector object.
         Returns connections ( NXOpen.Diagramming.Connection Li): .
        """
        pass
    def GetReferencedSheets(self) -> List[Sheet]:
        """
         Get referenced diagramming sheets.
         Returns sheets ( Sheet List[NX): .
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Diagramming
import NXOpen.PLAS
class PidManager(NXOpen.Object): 
    """ A manager to deal with all objects. """
    def ConvertUnassignedRunToNormalRun(run: NXOpen.PLAS.Run) -> None:
        """
         Convert an unassigned run to normal one
        """
        pass
    def CreateAutomaticTableBuilder(part: NXOpen.Part, table: AutomaticTable) -> AutomaticTableBuilder:
        """
         Creates a NXOpen.PID.AutomaticTableBuilder. 
         Returns builder ( AutomaticTableBuilder NXOp): .
        """
        pass
    def CreateBulkEditBuilder(part: NXOpen.Part) -> BulkEditBuilder:
        """
         Creates a NXOpen.PID.BulkEditBuilder 
         Returns builder ( BulkEditBuilder NXOp): .
        """
        pass
    def CreateDesignContextBuilder() -> DesignContextBuilder:
        """
         Creates a NXOpen.PID.DesignContextBuilder 
         Returns builder ( DesignContextBuilder NXOp): .
        """
        pass
    def CreateDesignValidationBuilder(part: NXOpen.Part) -> DesignValidationBuilder:
        """
         Creates a NXOpen.PID.DesignValidationBuilder. 
         Returns builder ( DesignValidationBuilder NXOp): .
        """
        pass
    def CreateEquipmentBuilder(part: NXOpen.Part, equipment: Equipment) -> EquipmentBuilder:
        """
         Creates a NXOpen.PID.EquipmentBuilder. 
         Returns builder ( EquipmentBuilder NXOp): .
        """
        pass
    def CreateFilenewapplicationBuilder() -> FileNewApplicationBuilder:
        """
         Creates a NXOpen.PID.FileNewApplicationBuilder 
         Returns builder ( FileNewApplicationBuilder NXOp): .
        """
        pass
    def CreateFlowDirectionArrowBuilder(part: NXOpen.Part, flowDirectionArrow: FlowDirectionArrow) -> FlowDirectionArrowBuilder:
        """
         Creates a NXOpen.PID.FlowDirectionArrowBuilder. 
         Returns builder ( FlowDirectionArrowBuilder NXOp): .
        """
        pass
    def CreateInstrumentationBuilder(part: NXOpen.Part, instrumentation: NXOpen.NXObject) -> InstrumentationBuilder:
        """
         Creates a NXOpen.PID.InstrumentationBuilder. 
         Returns builder ( InstrumentationBuilder NXOp): .
        """
        pass
    def CreateLibraryAuthoringBuilder(part: NXOpen.Part) -> LibraryAuthoringBuilder:
        """
         Creates a NXOpen.PID.LibraryAuthoringBuilder. 
         Returns builder ( LibraryAuthoringBuilder NXOp): .
        """
        pass
    def CreateOffSheetConnectorBuilder(part: NXOpen.Part, oscObject: OffSheetConnector) -> OffSheetConnectorBuilder:
        """
         Creates a NXOpen.PID.OffSheetConnectorBuilder. 
         Returns builder ( OffSheetConnectorBuilder NXOp): .
        """
        pass
    def CreatePipeBuilder(part: NXOpen.Part, pipe: Pipe) -> PipeBuilder:
        """
         Creates a NXOpen.PID.PipeBuilder. 
         Returns builder ( PipeBuilder NXOp): .
        """
        pass
    def CreatePortEquipmentBuilder(part: NXOpen.Part, portEquipment: PortEquipment) -> PortEquipmentBuilder:
        """
         Creates a NXOpen.PID.PortEquipmentBuilder. 
         Returns builder ( PortEquipmentBuilder NXOp): .
        """
        pass
    def CreatePreferencesBuilder(part: NXOpen.Part, sheet: Sheet) -> PreferencesBuilder:
        """
         Creates a NXOpen.PID.PreferencesBuilder. 
         Returns builder ( PreferencesBuilder NXOp): .
        """
        pass
    def CreateSheetTemplateBuilder(part: NXOpen.Part, sheet: NXOpen.Diagramming.Sheet) -> SheetTemplateBuilder:
        """
         Creates a NXOpen.PID.SheetTemplateBuilder 
         Returns builder ( SheetTemplateBuilder NXOp): .
        """
        pass
    def DeleteSheetElements(sheetElementsDel: List[NXOpen.Diagramming.SheetElement]) -> None:
        """
         Delete Sheet Elements. 
        """
        pass
    def EnterLibraryAuthoring() -> None:
        """
         Enter Library Authoring Tool. 
        """
        pass
    def ExitLibraryAuthoring() -> None:
        """
         Exit Library Authoring Tool. 
        """
        pass
    def ExportRunManaged(runTags: List[NXOpen.NXObject], destination: str) -> None:
        """
         Exports NXOpen.PDM.ElementGroup 
        """
        pass
    def ExportRunManagedWithSpecificName(runTags: List[NXOpen.NXObject], fileNames: List[str], destination: str) -> None:
        """
         Exports NXOpen.PDM.ElementGroup 
        """
        pass
    def ExportRunNative(runTags: List[NXOpen.NXObject], destination: str) -> None:
        """
         Exports NXOpen.PDM.ElementGroup 
        """
        pass
    def ExportRunNativeWithSpecificName(runTags: List[NXOpen.NXObject], fileNames: List[str], destination: str) -> None:
        """
         Exports NXOpen.PDM.ElementGroup 
        """
        pass
    def GetRunsInSystem(system: NXOpen.Assemblies.Partition) -> List[NXOpen.PLAS.Run]:
        """
         Gets the NXOpen.PLAS.Run objects in the NXOpen.Assemblies.Partition 
         Returns runs ( NXOpen.PLAS.Run Li):  the run objects .
        """
        pass
    def GetSheet(part: NXOpen.Part) -> Sheet:
        """
         Gets the NXOpen.PID.Sheet from part. 
         Returns sheet ( Sheet NXOp): .
        """
        pass
    def GetSheetsInSystem(system: NXOpen.Assemblies.Partition) -> List[Sheet]:
        """
         Gets the NXOpen.PID.Sheet objects in the NXOpen.Assemblies.Partition 
         Returns sheets ( Sheet List[NX):  the sheet objects .
        """
        pass
    def LoadSystem(system: NXOpen.Assemblies.Partition) -> None:
        """
         Loads a NXOpen.Assemblies.Partition 
        """
        pass
    def OpenSheet(sheet: Sheet) -> None:
        """
         Opens a NXOpen.PID.Sheet 
        """
        pass
    def OpenSheetQuietly(sheet: Sheet) -> None:
        """
         Opens a NXOpen.PID.Sheet without displaying the sheet. 
        """
        pass
    def ReparentBranch(sourceRun: NXOpen.PLAS.Run, destinationRun: NXOpen.PLAS.Run, oldbranch: OrderedElementGroup) -> OrderedElementGroup:
        """
         Moves branch from one run to another. the original branch will be destroyed 
         Returns newbranch ( OrderedElementGroup NXOp): .
        """
        pass
import NXOpen
import NXOpen.Diagramming
import NXOpen.PLAS
class PipeBuilder(NXOpen.Builder): 
    """  Represents a PipeBuilder.  """
    @property
    def Discipline(self) -> PipeDisciplineType:
        """
        Getter for property: ( PipeDisciplineType NXOp) Discipline
         Returns the pipe discipline type   
            
         
        """
        pass
    @Discipline.setter
    def Discipline(self, disciplineType: PipeDisciplineType):
        """
        Setter for property: ( PipeDisciplineType NXOp) Discipline
         Returns the pipe discipline type   
            
         
        """
        pass
    @property
    def ElementId(self) -> str:
        """
        Getter for property: (str) ElementId
         Returns the current element ID of this pipe.  
           It works only in edit mode, it's optional and the first element ID stored in the pipe will be used as default.  
         
        """
        pass
    @ElementId.setter
    def ElementId(self, elementId: str):
        """
        Setter for property: (str) ElementId
         Returns the current element ID of this pipe.  
           It works only in edit mode, it's optional and the first element ID stored in the pipe will be used as default.  
         
        """
        pass
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the id of the pipe.  
             
         
        """
        pass
    @property
    def LineTypePathId(self) -> str:
        """
        Getter for property: (str) LineTypePathId
         Returns the line type path ID of the Pipe.  
             
         
        """
        pass
    @LineTypePathId.setter
    def LineTypePathId(self, lineTypePathId: str):
        """
        Setter for property: (str) LineTypePathId
         Returns the line type path ID of the Pipe.  
             
         
        """
        pass
    @property
    def OverStockPathId(self) -> str:
        """
        Getter for property: (str) OverStockPathId
         Returns the over stock path ID of the pipe.  
             
         
        """
        pass
    @OverStockPathId.setter
    def OverStockPathId(self, overStockPathId: str):
        """
        Setter for property: (str) OverStockPathId
         Returns the over stock path ID of the pipe.  
             
         
        """
        pass
    @property
    def OverrideLineType(self) -> bool:
        """
        Getter for property: (bool) OverrideLineType
         Returns the option to override line type   
            
         
        """
        pass
    @OverrideLineType.setter
    def OverrideLineType(self, overrideLineType: bool):
        """
        Setter for property: (bool) OverrideLineType
         Returns the option to override line type   
            
         
        """
        pass
    @property
    def OverstockAttributeOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) OverstockAttributeOwner
         Returns the owner of overstock attributes group.  
            
         
        """
        pass
    @property
    def OwningRun(self) -> NXOpen.PLAS.Run:
        """
        Getter for property: ( NXOpen.PLAS.Run) OwningRun
         Returns the owning run of the pipe.  
             
         
        """
        pass
    @OwningRun.setter
    def OwningRun(self, owningRun: NXOpen.PLAS.Run):
        """
        Setter for property: ( NXOpen.PLAS.Run) OwningRun
         Returns the owning run of the pipe.  
             
         
        """
        pass
    @property
    def OwningSheet(self) -> Sheet:
        """
        Getter for property: ( Sheet NXOp) OwningSheet
         Returns the owning sheet of this pipe.  
             
         
        """
        pass
    @OwningSheet.setter
    def OwningSheet(self, owningSheet: Sheet):
        """
        Setter for property: ( Sheet NXOp) OwningSheet
         Returns the owning sheet of this pipe.  
             
         
        """
        pass
    @property
    def PipeAttributeOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) PipeAttributeOwner
         Returns the owner of pipe attributes.  
            
         
        """
        pass
    @property
    def PipeStockAttributeOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) PipeStockAttributeOwner
         Returns the owner of pipe stock attributes group.  
            
         
        """
        pass
    @property
    def ReverseEnd(self) -> bool:
        """
        Getter for property: (bool) ReverseEnd
         Returns the reversed flag of this connection.  
             
         
        """
        pass
    @property
    def StockPathId(self) -> str:
        """
        Getter for property: (str) StockPathId
         Returns the stock path ID of the pipe.  
             
         
        """
        pass
    @StockPathId.setter
    def StockPathId(self, stockPathId: str):
        """
        Setter for property: (str) StockPathId
         Returns the stock path ID of the pipe.  
             
         
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
    def GetEnd(self) -> Tuple[Equipment, str, str]:
        """
         Gets the end port of this pipe.
         Returns A tuple consisting of (equipment, nodeSidId, portId). 
         - equipment is:  Equipment NXOp.
         - nodeSidId is: str.
         - portId is: str.

        """
        pass
    def GetEndLocation(self) -> NXOpen.Point2d:
        """
         Get the end location of this connection.
                    This end location is applicable only when the Diagramming.ConnectionBuilder.End port is . 
         Returns endLocation ( NXOpen.Point2d): .
        """
        pass
    def GetEndTee(self) -> Tuple[Equipment, str]:
        """
         Gets the end Tee. 
         Returns A tuple consisting of (tee, nodeSidId). 
         - tee is:  Equipment NXOp.
         - nodeSidId is: str.

        """
        pass
    def GetEndTeeLocation(self) -> Tuple[Pipe, str, int, float]:
        """
         Get the connection location for tee object at the end of the connection. 
         Returns A tuple consisting of (pipe, connectionId, segementId, percent). 
         - pipe is:  Pipe NXOp.
         - connectionId is: str.
         - segementId is: int.
         - percent is: float.

        """
        pass
    def GetNewEndTeeConnection(self) -> Tuple[Pipe, str]:
        """
         Gets new connection after inserting the end Tee. 
         Returns A tuple consisting of (pipe, connectionId). 
         - pipe is:  Pipe NXOp.
         - connectionId is: str.

        """
        pass
    def GetNewStartTeeConnection(self) -> Tuple[Pipe, str]:
        """
         Gets new connection after inserting the start Tee. 
         Returns A tuple consisting of (pipe, connectionId). 
         - pipe is:  Pipe NXOp.
         - connectionId is: str.

        """
        pass
    def GetStart(self) -> Tuple[Equipment, str, str]:
        """
         Gets the start port of this connection. 
         Returns A tuple consisting of (equipment, nodeSidId, portId). 
         - equipment is:  Equipment NXOp.
         - nodeSidId is: str.
         - portId is: str.

        """
        pass
    def GetStartLocation(self) -> NXOpen.Point2d:
        """
         Get the start location of this connection.
                    This start location is applicable only when the Diagramming.ConnectionBuilder.Start is .
         Returns startLocation ( NXOpen.Point2d): .
        """
        pass
    def GetStartTee(self) -> Tuple[Equipment, str]:
        """
         Gets the start Tee. 
         Returns A tuple consisting of (tee, nodeSidId). 
         - tee is:  Equipment NXOp.
         - nodeSidId is: str.

        """
        pass
    def GetStartTeeLocation(self) -> Tuple[Pipe, str, int, float]:
        """
         Get the connection location for tee object at the start of the connection. 
         Returns A tuple consisting of (pipe, connectionId, segementId, percent). 
         - pipe is:  Pipe NXOp.
         - connectionId is: str.
         - segementId is: int.
         - percent is: float.

        """
        pass
    def SetBendPoints(self, points: List[NXOpen.Point2d]) -> None:
        """
         Set bending points for polyline to render the connection. 
        """
        pass
    def SetEnd(self, equipment: Equipment, nodeSidId: str, portId: str) -> None:
        """
         Sets the end port of this pipe.
        """
        pass
    def SetEndLocation(self, endLocation: NXOpen.Point2d) -> None:
        """
         Set the end location of this connection.
                    This end location is applicable only when the Diagramming.ConnectionBuilder.End port is . 
        """
        pass
    def SetEndTeeLocation(self, pipe: Pipe, connectionId: str, segementId: int, percent: float) -> None:
        """
         Set the connection location for tee object at the end of the connection. 
        """
        pass
    def SetStart(self, equipment: Equipment, nodeSidId: str, portId: str) -> None:
        """
         Sets the start port of this connection. 
        """
        pass
    def SetStartLocation(self, startLocation: NXOpen.Point2d) -> None:
        """
         Set the start location of this connection.
                    This start location is applicable only when the Diagramming.ConnectionBuilder.Start is .
        """
        pass
    def SetStartTeeLocation(self, pipe: Pipe, connectionId: str, segementId: int, percent: float) -> None:
        """
         Set the connection location for tee object at the start of the connection. 
        """
        pass
class PipeDisciplineType(Enum):
    """
    Members Include: 
     |Piping|  piping discipline. 
     |Instrumentation|  instrumentation discipline. 
     |Hvac|  HVAC discipline. 

    """
    Piping: int
    Instrumentation: int
    Hvac: int
    @staticmethod
    def ValueOf(value: int) -> PipeDisciplineType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Pipe(ConnectionElementRevision): 
    """ Represents the Pipe class. """
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
import NXOpen.Diagramming
class PortEquipmentBuilder(NXOpen.Builder): 
    """ 
    Builder used to model a piece of PortEquipment. 
    """
    @property
    def ExistingSymbol(self) -> NXOpen.Diagramming.Port:
        """
        Getter for property: ( NXOpen.Diagramming.Port) ExistingSymbol
         Returns the symbol from foundation window.  
           It is only applicable when  PID::PortEquipmentBuilder::SymbolSourceType  is  PID::SymbolSourceOptionExistingSymbol .  
         
        """
        pass
    @ExistingSymbol.setter
    def ExistingSymbol(self, existingSymbol: NXOpen.Diagramming.Port):
        """
        Setter for property: ( NXOpen.Diagramming.Port) ExistingSymbol
         Returns the symbol from foundation window.  
           It is only applicable when  PID::PortEquipmentBuilder::SymbolSourceType  is  PID::SymbolSourceOptionExistingSymbol .  
         
        """
        pass
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the tag of this port equipment.  
             
         
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
    def NeedAttrOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) NeedAttrOwner
         Returns the owner of need attributes group.  
            
         
        """
        pass
    @property
    def OwningSheet(self) -> Sheet:
        """
        Getter for property: ( Sheet NXOp) OwningSheet
         Returns the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    @OwningSheet.setter
    def OwningSheet(self, owningSheet: Sheet):
        """
        Setter for property: ( Sheet NXOp) OwningSheet
         Returns the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    @property
    def PortId(self) -> str:
        """
        Getter for property: (str) PortId
         Returns the current port ID of this port equipment.  
           It works only in edit mode, it's optional and the first port ID stored in the port equipment will be used as default.  
         
        """
        pass
    @PortId.setter
    def PortId(self, portId: str):
        """
        Setter for property: (str) PortId
         Returns the current port ID of this port equipment.  
           It works only in edit mode, it's optional and the first port ID stored in the port equipment will be used as default.  
         
        """
        pass
    @property
    def RelativePercentX(self) -> float:
        """
        Getter for property: (float) RelativePercentX
         Returns the X percentage of location relative to the node.  
             
         
        """
        pass
    @RelativePercentX.setter
    def RelativePercentX(self, percentX: float):
        """
        Setter for property: (float) RelativePercentX
         Returns the X percentage of location relative to the node.  
             
         
        """
        pass
    @property
    def RelativePercentY(self) -> float:
        """
        Getter for property: (float) RelativePercentY
         Returns the Y percentage of location relative to the node.  
             
         
        """
        pass
    @RelativePercentY.setter
    def RelativePercentY(self, percentY: float):
        """
        Setter for property: (float) RelativePercentY
         Returns the Y percentage of location relative to the node.  
             
         
        """
        pass
    @property
    def RelativeValueX(self) -> float:
        """
        Getter for property: (float) RelativeValueX
         Returns the X offset value of location relative to the node.  
             
         
        """
        pass
    @RelativeValueX.setter
    def RelativeValueX(self, valueX: float):
        """
        Setter for property: (float) RelativeValueX
         Returns the X offset value of location relative to the node.  
             
         
        """
        pass
    @property
    def RelativeValueY(self) -> float:
        """
        Getter for property: (float) RelativeValueY
         Returns the Y offset value of location relative to the node.  
             
         
        """
        pass
    @RelativeValueY.setter
    def RelativeValueY(self, valueY: float):
        """
        Setter for property: (float) RelativeValueY
         Returns the Y offset value of location relative to the node.  
             
         
        """
        pass
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the scale value.  
           It is only applicable when  PID::PortEquipmentBuilder::LockAspectRatio  is true.  
         
        """
        pass
    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the scale value.  
           It is only applicable when  PID::PortEquipmentBuilder::LockAspectRatio  is true.  
         
        """
        pass
    @property
    def ScaleX(self) -> float:
        """
        Getter for property: (float) ScaleX
         Returns the x scale value.  
           It is only applicable when  PID::PortEquipmentBuilder::LockAspectRatio  is false.  
         
        """
        pass
    @ScaleX.setter
    def ScaleX(self, scaleX: float):
        """
        Setter for property: (float) ScaleX
         Returns the x scale value.  
           It is only applicable when  PID::PortEquipmentBuilder::LockAspectRatio  is false.  
         
        """
        pass
    @property
    def ScaleY(self) -> float:
        """
        Getter for property: (float) ScaleY
         Returns the y scale value.  
           It is only applicable when  PID::PortEquipmentBuilder::LockAspectRatio  is false.  
         
        """
        pass
    @ScaleY.setter
    def ScaleY(self, scaleY: float):
        """
        Setter for property: (float) ScaleY
         Returns the y scale value.  
           It is only applicable when  PID::PortEquipmentBuilder::LockAspectRatio  is false.  
         
        """
        pass
    @property
    def SymbolId(self) -> str:
        """
        Getter for property: (str) SymbolId
         Returns the symbol ID of this port equipment.  
           It is only applicable when  PID::PortEquipmentBuilder::SymbolSourceType  is  PID::SymbolSourceOptionReuseLibrary .  
         
        """
        pass
    @SymbolId.setter
    def SymbolId(self, symbolId: str):
        """
        Setter for property: (str) SymbolId
         Returns the symbol ID of this port equipment.  
           It is only applicable when  PID::PortEquipmentBuilder::SymbolSourceType  is  PID::SymbolSourceOptionReuseLibrary .  
         
        """
        pass
    @property
    def SymbolSourceType(self) -> SymbolSourceOption:
        """
        Getter for property: ( SymbolSourceOption NXOp) SymbolSourceType
         Returns the symbol source type   
            
         
        """
        pass
    @SymbolSourceType.setter
    def SymbolSourceType(self, symbolSourceType: SymbolSourceOption):
        """
        Setter for property: ( SymbolSourceOption NXOp) SymbolSourceType
         Returns the symbol source type   
            
         
        """
        pass
    @property
    def UseExistingID(self) -> bool:
        """
        Getter for property: (bool) UseExistingID
         Returns the option to place a duplicate symbol.  
           It is only applicable when  PID::PortEquipmentBuilder::SymbolSourceType  is  PID::SymbolSourceOptionExistingSymbol .  
         
        """
        pass
    @UseExistingID.setter
    def UseExistingID(self, useExistingID: bool):
        """
        Setter for property: (bool) UseExistingID
         Returns the option to place a duplicate symbol.  
           It is only applicable when  PID::PortEquipmentBuilder::SymbolSourceType  is  PID::SymbolSourceOptionExistingSymbol .  
         
        """
        pass
    def GetNode(self) -> Tuple[Equipment, str]:
        """
         Get the node. 
         Returns A tuple consisting of (equipment, nodeId). 
         - equipment is:  Equipment NXOp.
         - nodeId is: str.

        """
        pass
    def GetPort(self) -> NXOpen.Diagramming.Port:
        """
         Get the port object of the PortEquipment builder. 
         Returns port ( NXOpen.Diagramming.Port): .
        """
        pass
    def SetFulfillment(self, symbolID: str) -> None:
        """
         Sets the fulfillment data of the symbol. The input symbol should be a 3D one and in the same category with the entity of the builder
        """
        pass
    def SetNode(self, equipment: Equipment, nodeId: str) -> None:
        """
         Set the node. 
        """
        pass
class PortEquipment(Equipment): 
    """ Represents the PortEquipment class. """
    pass
class Port(PortArtifact): 
    """ Represents the port class. """
    @property
    def ConnectionType(self) -> str:
        """
        Getter for property: (str) ConnectionType
         Returns the connection type of the port.  
            
         
        """
        pass
    @property
    def Direction(self) -> PortDirectionOption:
        """
        Getter for property: ( PortDirectionOption NXOp) Direction
         Returns the Id of the port.  
            
         
        """
        pass
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
         Returns the Id of the port.  
            
         
        """
        pass
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the Id of the port.  
            
         
        """
        pass
    @property
    def Inline(self) -> bool:
        """
        Getter for property: (bool) Inline
         Returns the indicator of the port's inline.  
            
         
        """
        pass
    @property
    def Material(self) -> str:
        """
        Getter for property: (str) Material
         Returns the material of the port.  
            
         
        """
        pass
    @property
    def Nps(self) -> float:
        """
        Getter for property: (float) Nps
         Returns the nps of the port.  
            
         
        """
        pass
    @property
    def PortAlias(self) -> str:
        """
        Getter for property: (str) PortAlias
         Returns the Id of the port.  
            
         
        """
        pass
    @property
    def Terminating(self) -> bool:
        """
        Getter for property: (bool) Terminating
         Returns the indicator of the port's terminating.  
            
         
        """
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
        Getter for property: ( PreferencesAnnotationBuilder NXOp) Annotation
         Returns    the preferences annotation builder   
            
         
        """
        pass
    @property
    def Connection(self) -> PreferencesConnectionBuilder:
        """
        Getter for property: ( PreferencesConnectionBuilder NXOp) Connection
         Returns    the preferences connection builder   
            
         
        """
        pass
    @property
    def General(self) -> PreferencesGeneralBuilder:
        """
        Getter for property: ( PreferencesGeneralBuilder NXOp) General
         Returns    the preferences general builder   
            
         
        """
        pass
    @property
    def Instrumentation(self) -> PreferencesInstrumentationBuilder:
        """
        Getter for property: ( PreferencesInstrumentationBuilder NXOp) Instrumentation
         Returnsthe preferences instrumentation builder   
            
         
        """
        pass
    @property
    def OffSheetConnector(self) -> PreferencesOffSheetConnectorBuilder:
        """
        Getter for property: ( PreferencesOffSheetConnectorBuilder NXOp) OffSheetConnector
         Returns    the preferences offsheetconnector builder   
            
         
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
import NXOpen.GeometricUtilities
class PreferencesInstrumentationBuilder(NXOpen.TaggedObject): 
    """
    Represents a PreferencesInstrumentationBuilder
    """
    @property
    def ControlLoopDisplay(self) -> InstrumentationControlLoopDisplay:
        """
        Getter for property: ( InstrumentationControlLoopDisplay NXOp) ControlLoopDisplay
         Returns  the identification display for the control loop of the instrumentation symbols.  
             
         
        """
        pass
    @ControlLoopDisplay.setter
    def ControlLoopDisplay(self, display: InstrumentationControlLoopDisplay):
        """
        Setter for property: ( InstrumentationControlLoopDisplay NXOp) ControlLoopDisplay
         Returns  the identification display for the control loop of the instrumentation symbols.  
             
         
        """
        pass
import NXOpen
import NXOpen.Diagramming
import NXOpen.GeometricUtilities
class PreferencesOffSheetConnectorBuilder(NXOpen.TaggedObject): 
    """
    Represents a PreferencesOffSheetConnectorBuilder
    """
    class StyleOption(Enum):
        """
        Members Include: 
         |SmallFilledArrowOut| 
         |SmallFilledArrowIn| 
         |Box| 
         |ChevronOut| 
         |ChevronIn| 

        """
        SmallFilledArrowOut: int
        SmallFilledArrowIn: int
        Box: int
        ChevronOut: int
        ChevronIn: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesOffSheetConnectorBuilder.StyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Style(self) -> PreferencesOffSheetConnectorBuilder.StyleOption:
        """
        Getter for property: ( PreferencesOffSheetConnectorBuilder.StyleOption NXOp) Style
         Returns the style of OSC   
            
         
        """
        pass
    @Style.setter
    def Style(self, style: PreferencesOffSheetConnectorBuilder.StyleOption):
        """
        Setter for property: ( PreferencesOffSheetConnectorBuilder.StyleOption NXOp) Style
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
    def PropertyType(self) -> PropertyType:
        """
        Getter for property: ( PropertyType NXOp) PropertyType
         Returns the property type.  
             
         
        """
        pass
    @PropertyType.setter
    def PropertyType(self, propertyType: PropertyType):
        """
        Setter for property: ( PropertyType NXOp) PropertyType
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
class PropertyType(Enum):
    """
    Members Include: 
     |Null|  Null type 
     |Index|  Index of object 
     |UserAttribute|  User attribute 
     |NeedAttribute|  Need attribute 
     |FulfillmentAttribute|  Fulfillment attribute 
     |PipeStockAttribute|  Pipe stock attribute 
     |PidTag|  The tag of PID object 
     |ParentRun|  The parent run of pipe stock 
     |Quantity|  The quantity of same object 
     |System|  The system of object 
     |RunAttribute|  The attibute of run object 
     |EquipmentAttribute|  The attibute of equipment object 

    """
    Null: int
    Index: int
    UserAttribute: int
    NeedAttribute: int
    FulfillmentAttribute: int
    PipeStockAttribute: int
    PidTag: int
    ParentRun: int
    Quantity: int
    System: int
    RunAttribute: int
    EquipmentAttribute: int
    @staticmethod
    def ValueOf(value: int) -> PropertyType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
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
class SheetTemplateBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.PID.SheetTemplateBuilder builder, and the builder is used to model a sheet template. """
    @property
    def Sheet(self) -> NXOpen.Diagramming.SheetBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.SheetBuilder) Sheet
         Returns the diagramming sheet builder.  
             
         
        """
        pass
import NXOpen.PLAS
class Sheet(SheetRevision): 
    """ 
        Represents a base class that provides common methods for various model elements in a NXOpen.CollaborativeDesign.
    """
    @property
    def FlowDirectionArrows() -> FlowDirectionArrowCollection:
        """
         Returns the  NXOpen::PID::FlowDirectionArrowCollection   belonging to this part 
        """
        pass
    @property
    def AutomaticTables() -> AutomaticTableCollection:
        """
         Returns the  NXOpen::PID::AutomaticTableCollection   belonging to this part 
        """
        pass
    @property
    def Instrumentations() -> InstrumentationCollection:
        """
         This is an internal API and can be changed at any time 
        """
        pass
    def GetEquipment(self) -> List[Equipment]:
        """
         Gets the NXOpen.PID.Equipment objects in the sheet 
         Returns equipment ( Equipment List[NX):  the equipment objects .
        """
        pass
    def GetPipes(self) -> List[Pipe]:
        """
         Gets the NXOpen.PID.Pipe objects in the sheet 
         Returns pipes ( Pipe List[NX):  the pipe objects .
        """
        pass
    def GetRuns(self) -> List[NXOpen.PLAS.Run]:
        """
         Gets the NXOpen.PLAS.Run objects in the sheet 
         Returns runs ( NXOpen.PLAS.Run Li):  the run objects .
        """
        pass
class SymbolSourceOption(Enum):
    """
    Members Include: 
     |ReuseLibrary|  from the reuse library. 
     |ExistingSymbol|  from the symbol in document window. 
     |LogicalElementRevision|  from an existing Logical Element Revision. 

    """
    ReuseLibrary: int
    ExistingSymbol: int
    LogicalElementRevision: int
    @staticmethod
    def ValueOf(value: int) -> SymbolSourceOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
