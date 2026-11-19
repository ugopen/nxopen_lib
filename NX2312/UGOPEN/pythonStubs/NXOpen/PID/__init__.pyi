from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Assemblies
import NXOpen.Diagramming.Tables
##   @brief  Represents a AutomaticTableBuilder.  
## 
##    <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateAutomaticTableBuilder  NXOpen::PID::PidManager::CreateAutomaticTableBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ScopeType </term> <description> 
##  
## CurrentSheet </description> </item> 
## 
## <item><term> 
##  
## StockType </term> <description> 
##  
## Pipe </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1847.0.0  <br> 

class AutomaticTableBuilder(NXOpen.Builder): 
    """ <summary> Represents a AutomaticTableBuilder. </summary> """


    ##  Represents the object type. 
    ##  Equipment 
    class ObjectTypeOption(Enum):
        """
        Members Include: <Equipment> <InlineEquipment> <Run> <PipeStock>
        """
        Equipment: int
        InlineEquipment: int
        Run: int
        PipeStock: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AutomaticTableBuilder.ObjectTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the scope type.  
    ##  Lists objects in current sheet 
    class ScopeTypeOption(Enum):
        """
        Members Include: <CurrentSheet> <OtherSheet> <System>
        """
        CurrentSheet: int
        OtherSheet: int
        System: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AutomaticTableBuilder.ScopeTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the stock type. 
    ##  Pipe Stock 
    class StockOption(Enum):
        """
        Members Include: <Pipe> <Instrumentation> <Hvac>
        """
        Pipe: int
        Instrumentation: int
        Hvac: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AutomaticTableBuilder.StockOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) ManualUpdate
    ##   the manual update flag.  
    ##    If true, the automatic update will be disabled, the table could be updated manually.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def ManualUpdate(self) -> bool:
        """
        Getter for property: (bool) ManualUpdate
          the manual update flag.  
           If true, the automatic update will be disabled, the table could be updated manually.   
         
        """
        pass
    
    ## Setter for property: (bool) ManualUpdate

    ##   the manual update flag.  
    ##    If true, the automatic update will be disabled, the table could be updated manually.   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ManualUpdate.setter
    def ManualUpdate(self, manualUpdate: bool):
        """
        Setter for property: (bool) ManualUpdate
          the manual update flag.  
           If true, the automatic update will be disabled, the table could be updated manually.   
         
        """
        pass
    
    ## Getter for property: (@link AutomaticTableBuilder.ObjectTypeOption NXOpen.PID.AutomaticTableBuilder.ObjectTypeOption@endlink) ObjectType
    ##   the object type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return AutomaticTableBuilder.ObjectTypeOption
    @property
    def ObjectType(self) -> AutomaticTableBuilder.ObjectTypeOption:
        """
        Getter for property: (@link AutomaticTableBuilder.ObjectTypeOption NXOpen.PID.AutomaticTableBuilder.ObjectTypeOption@endlink) ObjectType
          the object type.  
             
         
        """
        pass
    
    ## Setter for property: (@link AutomaticTableBuilder.ObjectTypeOption NXOpen.PID.AutomaticTableBuilder.ObjectTypeOption@endlink) ObjectType

    ##   the object type.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ObjectType.setter
    def ObjectType(self, objectType: AutomaticTableBuilder.ObjectTypeOption):
        """
        Setter for property: (@link AutomaticTableBuilder.ObjectTypeOption NXOpen.PID.AutomaticTableBuilder.ObjectTypeOption@endlink) ObjectType
          the object type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) OutputControlLoop
    ##   the option to output the control loop list.  
    ##    Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def OutputControlLoop(self) -> bool:
        """
        Getter for property: (bool) OutputControlLoop
          the option to output the control loop list.  
           Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun@endlink .   
         
        """
        pass
    
    ## Setter for property: (bool) OutputControlLoop

    ##   the option to output the control loop list.  
    ##    Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun@endlink .   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @OutputControlLoop.setter
    def OutputControlLoop(self, controlLoop: bool):
        """
        Setter for property: (bool) OutputControlLoop
          the option to output the control loop list.  
           Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun@endlink .   
         
        """
        pass
    
    ## Getter for property: (bool) OutputEquipment
    ##   the option to output the equipment list.  
    ##    Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def OutputEquipment(self) -> bool:
        """
        Getter for property: (bool) OutputEquipment
          the option to output the equipment list.  
           Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment@endlink .   
         
        """
        pass
    
    ## Setter for property: (bool) OutputEquipment

    ##   the option to output the equipment list.  
    ##    Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment@endlink .   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @OutputEquipment.setter
    def OutputEquipment(self, equipment: bool):
        """
        Setter for property: (bool) OutputEquipment
          the option to output the equipment list.  
           Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment@endlink .   
         
        """
        pass
    
    ## Getter for property: (bool) OutputInlineEquipmentValve
    ##   the option to output the inline equipment/valve list.  
    ##    Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def OutputInlineEquipmentValve(self) -> bool:
        """
        Getter for property: (bool) OutputInlineEquipmentValve
          the option to output the inline equipment/valve list.  
           Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment@endlink .   
         
        """
        pass
    
    ## Setter for property: (bool) OutputInlineEquipmentValve

    ##   the option to output the inline equipment/valve list.  
    ##    Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment@endlink .   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @OutputInlineEquipmentValve.setter
    def OutputInlineEquipmentValve(self, inlineEquipmentValve: bool):
        """
        Setter for property: (bool) OutputInlineEquipmentValve
          the option to output the inline equipment/valve list.  
           Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment@endlink .   
         
        """
        pass
    
    ## Getter for property: (bool) OutputInstrumentation
    ##   the option to output the instrumentation list.  
    ##    Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def OutputInstrumentation(self) -> bool:
        """
        Getter for property: (bool) OutputInstrumentation
          the option to output the instrumentation list.  
           Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment@endlink .   
         
        """
        pass
    
    ## Setter for property: (bool) OutputInstrumentation

    ##   the option to output the instrumentation list.  
    ##    Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment@endlink .   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @OutputInstrumentation.setter
    def OutputInstrumentation(self, instrumentation: bool):
        """
        Setter for property: (bool) OutputInstrumentation
          the option to output the instrumentation list.  
           Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionEquipment@endlink .   
         
        """
        pass
    
    ## Getter for property: (bool) OutputRun
    ##   the option to output the run list.  
    ##    Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def OutputRun(self) -> bool:
        """
        Getter for property: (bool) OutputRun
          the option to output the run list.  
           Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun@endlink .   
         
        """
        pass
    
    ## Setter for property: (bool) OutputRun

    ##   the option to output the run list.  
    ##    Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun@endlink .   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @OutputRun.setter
    def OutputRun(self, run: bool):
        """
        Setter for property: (bool) OutputRun
          the option to output the run list.  
           Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionRun@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link AutomaticTableBuilder.ScopeTypeOption NXOpen.PID.AutomaticTableBuilder.ScopeTypeOption@endlink) ScopeType
    ##   the scope type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return AutomaticTableBuilder.ScopeTypeOption
    @property
    def ScopeType(self) -> AutomaticTableBuilder.ScopeTypeOption:
        """
        Getter for property: (@link AutomaticTableBuilder.ScopeTypeOption NXOpen.PID.AutomaticTableBuilder.ScopeTypeOption@endlink) ScopeType
          the scope type.  
             
         
        """
        pass
    
    ## Setter for property: (@link AutomaticTableBuilder.ScopeTypeOption NXOpen.PID.AutomaticTableBuilder.ScopeTypeOption@endlink) ScopeType

    ##   the scope type.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ScopeType.setter
    def ScopeType(self, scopeType: AutomaticTableBuilder.ScopeTypeOption):
        """
        Setter for property: (@link AutomaticTableBuilder.ScopeTypeOption NXOpen.PID.AutomaticTableBuilder.ScopeTypeOption@endlink) ScopeType
          the scope type.  
             
         
        """
        pass
    
    ## Getter for property: (@link Sheet NXOpen.PID.Sheet@endlink) Sheet
    ##   the sheet, only available if the ScopeType is OtherSheet.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return Sheet
    @property
    def Sheet(self) -> Sheet:
        """
        Getter for property: (@link Sheet NXOpen.PID.Sheet@endlink) Sheet
          the sheet, only available if the ScopeType is OtherSheet.  
             
         
        """
        pass
    
    ## Setter for property: (@link Sheet NXOpen.PID.Sheet@endlink) Sheet

    ##   the sheet, only available if the ScopeType is OtherSheet.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Sheet.setter
    def Sheet(self, sheet: Sheet):
        """
        Setter for property: (@link Sheet NXOpen.PID.Sheet@endlink) Sheet
          the sheet, only available if the ScopeType is OtherSheet.  
             
         
        """
        pass
    
    ## Getter for property: (@link AutomaticTableBuilder.StockOption NXOpen.PID.AutomaticTableBuilder.StockOption@endlink) StockType
    ##   the stock type to output.  
    ##    Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionPipeStock NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionPipeStock@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return AutomaticTableBuilder.StockOption
    @property
    def StockType(self) -> AutomaticTableBuilder.StockOption:
        """
        Getter for property: (@link AutomaticTableBuilder.StockOption NXOpen.PID.AutomaticTableBuilder.StockOption@endlink) StockType
          the stock type to output.  
           Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionPipeStock NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionPipeStock@endlink .   
         
        """
        pass
    
    ## Setter for property: (@link AutomaticTableBuilder.StockOption NXOpen.PID.AutomaticTableBuilder.StockOption@endlink) StockType

    ##   the stock type to output.  
    ##    Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionPipeStock NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionPipeStock@endlink .   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @StockType.setter
    def StockType(self, stockType: AutomaticTableBuilder.StockOption):
        """
        Setter for property: (@link AutomaticTableBuilder.StockOption NXOpen.PID.AutomaticTableBuilder.StockOption@endlink) StockType
          the stock type to output.  
           Only applicable when @link NXOpen::PID::AutomaticTableBuilder::ScopeType NXOpen::PID::AutomaticTableBuilder::ScopeType@endlink  is @link NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionPipeStock NXOpen::PID::AutomaticTableBuilder::ObjectTypeOptionPipeStock@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Assemblies.Partition NXOpen.Assemblies.Partition@endlink) System
    ##   the system, only available if the ScopeType is System.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Assemblies.Partition
    @property
    def System(self) -> NXOpen.Assemblies.Partition:
        """
        Getter for property: (@link NXOpen.Assemblies.Partition NXOpen.Assemblies.Partition@endlink) System
          the system, only available if the ScopeType is System.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Assemblies.Partition NXOpen.Assemblies.Partition@endlink) System

    ##   the system, only available if the ScopeType is System.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @System.setter
    def System(self, system: NXOpen.Assemblies.Partition):
        """
        Setter for property: (@link NXOpen.Assemblies.Partition NXOpen.Assemblies.Partition@endlink) System
          the system, only available if the ScopeType is System.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.Tables.TableBuilder NXOpen.Diagramming.Tables.TableBuilder@endlink) Table
    ##   the @link NXOpen::Diagramming::Tables::TableBuilder NXOpen::Diagramming::Tables::TableBuilder@endlink  of the @link NXOpen::Diagramming::Tables::Table NXOpen::Diagramming::Tables::Table@endlink .  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Diagramming.Tables.TableBuilder
    @property
    def Table(self) -> NXOpen.Diagramming.Tables.TableBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.Tables.TableBuilder NXOpen.Diagramming.Tables.TableBuilder@endlink) Table
          the @link NXOpen::Diagramming::Tables::TableBuilder NXOpen::Diagramming::Tables::TableBuilder@endlink  of the @link NXOpen::Diagramming::Tables::Table NXOpen::Diagramming::Tables::Table@endlink .  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.Tables.TableBuilder NXOpen.Diagramming.Tables.TableBuilder@endlink) Table

    ##   the @link NXOpen::Diagramming::Tables::TableBuilder NXOpen::Diagramming::Tables::TableBuilder@endlink  of the @link NXOpen::Diagramming::Tables::Table NXOpen::Diagramming::Tables::Table@endlink .  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @Table.setter
    def Table(self, diagrammingTable: NXOpen.Diagramming.Tables.TableBuilder):
        """
        Setter for property: (@link NXOpen.Diagramming.Tables.TableBuilder NXOpen.Diagramming.Tables.TableBuilder@endlink) Table
          the @link NXOpen::Diagramming::Tables::TableBuilder NXOpen::Diagramming::Tables::TableBuilder@endlink  of the @link NXOpen::Diagramming::Tables::Table NXOpen::Diagramming::Tables::Table@endlink .  
             
         
        """
        pass
    
    ##  Gets the number of property cell ranges. 
    ##  @return number (int):  the number of property cell ranges .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNumberOfPropertyCellRanges(builder: AutomaticTableBuilder) -> int:
        """
         Gets the number of property cell ranges. 
         @return number (int):  the number of property cell ranges .
        """
        pass
    
    ##  Gets the property cell range at the given index. 
    ##             The index must be greater than or equal to 0, and less than the number of property cell ranges. 
    ##         
    ##  @return propertyCellRange (@link PropertyCellRangeBuilder NXOpen.PID.PropertyCellRangeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  the index of property cell range 
    def GetPropertyCellRange(builder: AutomaticTableBuilder, index: int) -> PropertyCellRangeBuilder:
        """
         Gets the property cell range at the given index. 
                    The index must be greater than or equal to 0, and less than the number of property cell ranges. 
                
         @return propertyCellRange (@link PropertyCellRangeBuilder NXOpen.PID.PropertyCellRangeBuilder@endlink): .
        """
        pass
    
    ##  Inserts the given number of property cell ranges at the given index. 
    ##             The index must be greater than or equal to 0, and less than or equal to the number of property cell ranges.
    ##             The number of property types and the number of property keys must be same, and must be greater than 0.
    ##         
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the index of the first inserted property cell range 
    def InsertPropertyCellRanges(builder: AutomaticTableBuilder, index: int, propertyTypes: List[PropertyType], propertyKeys: List[str]) -> None:
        """
         Inserts the given number of property cell ranges at the given index. 
                    The index must be greater than or equal to 0, and less than or equal to the number of property cell ranges.
                    The number of property types and the number of property keys must be same, and must be greater than 0.
                
        """
        pass
    
    ##  Removes the given number of property cell ranges starting with the given index. 
    ##             The index must be greater than or equal to 0, and less than the number of property cell ranges.
    ##             The number must be greater than 0, and "index + number" must be less than or equal to the number of property cell ranges.
    ##         
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the index of the first removed property cell range 
    def RemovePropertyCellRanges(builder: AutomaticTableBuilder, index: int, number: int) -> None:
        """
         Removes the given number of property cell ranges starting with the given index. 
                    The index must be greater than or equal to 0, and less than the number of property cell ranges.
                    The number must be greater than 0, and "index + number" must be less than or equal to the number of property cell ranges.
                
        """
        pass
    
import NXOpen
##  Represents a collection of AutomaticTable.  <br> To obtain an instance of this class, refer to @link NXOpen::PID::Sheet  NXOpen::PID::Sheet @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AutomaticTableCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of AutomaticTable. """


    ##  Finds the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  with the given identifier as recorded in a journal.
    ##            An exception will be thrown if no object can be found with given name. 
    ##  @return automaticTable (@link AutomaticTable NXOpen.PID.AutomaticTable@endlink):  @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  with this name. .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  Identifier to be found 
    def FindObject(sheet: AutomaticTableCollection, journalIdentifier: str) -> AutomaticTable:
        """
         Finds the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  with the given identifier as recorded in a journal.
                   An exception will be thrown if no object can be found with given name. 
         @return automaticTable (@link AutomaticTable NXOpen.PID.AutomaticTable@endlink):  @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  with this name. .
        """
        pass
    
    ##  Reads the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  from template part. 
    ##             Opens the template part with specified part name, and copies the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  from template part to this sheet.
    ##         
    ##  @return automaticTable (@link AutomaticTable NXOpen.PID.AutomaticTable@endlink):  the new @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  name of the template part 
    def ReadFromTemplate(sheet: AutomaticTableCollection, templatePartName: str) -> AutomaticTable:
        """
         Reads the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  from template part. 
                    Opens the template part with specified part name, and copies the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  from template part to this sheet.
                
         @return automaticTable (@link AutomaticTable NXOpen.PID.AutomaticTable@endlink):  the new @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  .
        """
        pass
    
    ##  Saves the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  as template part. 
    ##             Creates a template part with specified part name, and copies the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  to the template part.
    ##         
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  
    @overload
    def SaveAsTemplate(self, sheet: AutomaticTableCollection, automaticTable: AutomaticTable, templatePartName: str) -> None:
        """
         Saves the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  as template part. 
                    Creates a template part with specified part name, and copies the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  to the template part.
                
        """
        pass
    
    ##  Saves the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  as template part. 
    ##             Creates a template part with specified part name on PartOperationCreateBuilder, and copies the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  to the template part.
    ##         
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  
    @overload
    def SaveAsTemplate(self, sheet: AutomaticTableCollection, automaticTable: AutomaticTable, builder: PartOperationCreateBuilder) -> None:
        """
         Saves the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  as template part. 
                    Creates a template part with specified part name on PartOperationCreateBuilder, and copies the @link NXOpen::PID::AutomaticTable NXOpen::PID::AutomaticTable@endlink  to the template part.
                
        """
        pass
    
import NXOpen
import NXOpen.Diagramming.Tables
##   @brief  the automatic table for PID objects  
## 
##    <br> To create or edit an instance of this class, use @link NXOpen::PID::AutomaticTableBuilder  NXOpen::PID::AutomaticTableBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AutomaticTable(NXOpen.NXObject): 
    """ <summary> the automatic table for PID objects </summary> """


    ## Getter for property: (@link NXOpen.Diagramming.Tables.Table NXOpen.Diagramming.Tables.Table@endlink) Table
    ##   the @link NXOpen::Diagramming::Tables::Table NXOpen::Diagramming::Tables::Table@endlink  which displays in sheet.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Diagramming.Tables.Table
    @property
    def Table(self) -> NXOpen.Diagramming.Tables.Table:
        """
        Getter for property: (@link NXOpen.Diagramming.Tables.Table NXOpen.Diagramming.Tables.Table@endlink) Table
          the @link NXOpen::Diagramming::Tables::Table NXOpen::Diagramming::Tables::Table@endlink  which displays in sheet.  
             
         
        """
        pass
    
    ##  Refreshes the table contents. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def Refresh(automaticTable: AutomaticTable) -> None:
        """
         Refreshes the table contents. 
        """
        pass
    
import NXOpen
import NXOpen.Diagramming
## 
##     Represents a BulkEditBuilder to edit bulk of objects.
##      <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateBulkEditBuilder  NXOpen::PID::PidManager::CreateBulkEditBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class BulkEditBuilder(NXOpen.Builder): 
    """
    Represents a BulkEditBuilder to edit bulk of objects.
    """


    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) RenderingProperties
    ##   the line rendering properties.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Diagramming.RenderingPropertiesBuilder
    @property
    def RenderingProperties(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) RenderingProperties
          the line rendering properties.  
             
         
        """
        pass
    
    ##  Sets the delta value of X coordinate for bulk moving. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="deltaXCoordinate"> (float) </param>
    def SetDeltaXCoordinate(builder: BulkEditBuilder, deltaXCoordinate: float) -> None:
        """
         Sets the delta value of X coordinate for bulk moving. 
        """
        pass
    
    ##  Sets the delta value of Y coordinate for bulk moving. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="deltaYCoordinate"> (float) </param>
    def SetDeltaYCoordinate(builder: BulkEditBuilder, deltaYCoordinate: float) -> None:
        """
         Sets the delta value of Y coordinate for bulk moving. 
        """
        pass
    
    ##  Sets the visibility of sheet elements. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="hide"> (bool) </param>
    def SetHide(builder: BulkEditBuilder, hide: bool) -> None:
        """
         Sets the visibility of sheet elements. 
        """
        pass
    
    ##  Sets the visibility of labels. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="hideLabel"> (bool) </param>
    def SetHideLabel(builder: BulkEditBuilder, hideLabel: bool) -> None:
        """
         Sets the visibility of labels. 
        """
        pass
    
    ##  Sets the sheet elements for bulk editing. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="sheetElements"> (@link NXOpen.Diagramming.SheetElement List[NXOpen.Diagramming.SheetElement]@endlink) </param>
    def SetSheetElements(builder: BulkEditBuilder, sheetElements: List[NXOpen.Diagramming.SheetElement]) -> None:
        """
         Sets the sheet elements for bulk editing. 
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


import NXOpen
##  Represents a builder class that performs PID Design Context operations.
##          <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateDesignContextBuilder  NXOpen::PID::PidManager::CreateDesignContextBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class DesignContextBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs PID Design Context operations.
        """


    ## Getter for property: (@link ConfigurationContextBuilder NXOpen.PDM.ConfigurationContextBuilder@endlink) ConfigurationContext
    ##   the configuration context builder.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return ConfigurationContextBuilder
    @property
    def ConfigurationContext(self) -> ConfigurationContextBuilder:
        """
        Getter for property: (@link ConfigurationContextBuilder NXOpen.PDM.ConfigurationContextBuilder@endlink) ConfigurationContext
          the configuration context builder.  
             
         
        """
        pass
    
import NXOpen
##   @brief  Represents a DesignValidationBuilder.  
## 
##    <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateDesignValidationBuilder  NXOpen::PID::PidManager::CreateDesignValidationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class DesignValidationBuilder(NXOpen.Builder): 
    """ <summary> Represents a DesignValidationBuilder. </summary> """


    ## Getter for property: (bool) SaveResult
    ##   the option to save validation result   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

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
    ##   <br>  Created in NX1980.0.0  <br> 

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
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  A list of checker ids 
    def SetSelectedCheckerIds(builder: DesignValidationBuilder, selectedCheckerIds: List[str]) -> None:
        """
         Specifies the selected checker ids 
        """
        pass
    
import NXOpen
import NXOpen.Diagramming
##   @brief 
##     Builder used to model a piece of Equipment.  
## 
##  
##      <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateEquipmentBuilder  NXOpen::PID::PidManager::CreateEquipmentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
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
##   <br>  Created in NX11.0.1  <br> 

class EquipmentBuilder(NXOpen.Builder): 
    """ <summary>
    Builder used to model a piece of Equipment. </summary>
    """


    ## Getter for property: (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink) ExistingSymbol
    ##   the symbol from foundation window.  
    ##    It is only applicable when @link PID::EquipmentBuilder::SymbolSourceType PID::EquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionExistingSymbol PID::SymbolSourceOptionExistingSymbol@endlink .  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Diagramming.Node
    @property
    def ExistingSymbol(self) -> NXOpen.Diagramming.Node:
        """
        Getter for property: (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink) ExistingSymbol
          the symbol from foundation window.  
           It is only applicable when @link PID::EquipmentBuilder::SymbolSourceType PID::EquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionExistingSymbol PID::SymbolSourceOptionExistingSymbol@endlink .  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink) ExistingSymbol

    ##   the symbol from foundation window.  
    ##    It is only applicable when @link PID::EquipmentBuilder::SymbolSourceType PID::EquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionExistingSymbol PID::SymbolSourceOptionExistingSymbol@endlink .  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ExistingSymbol.setter
    def ExistingSymbol(self, existingSymbol: NXOpen.Diagramming.Node):
        """
        Setter for property: (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink) ExistingSymbol
          the symbol from foundation window.  
           It is only applicable when @link PID::EquipmentBuilder::SymbolSourceType PID::EquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionExistingSymbol PID::SymbolSourceOptionExistingSymbol@endlink .  
         
        """
        pass
    
    ## Getter for property: (@link Equipment NXOpen.PID.Equipment@endlink) ExistingSymbolLogicalElementRevision
    ##   the Logical Element Revision for the symbol.  
    ##    It is only applicable when @link PID::EquipmentBuilder::SymbolSourceType PID::EquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionLogicalElementRevision PID::SymbolSourceOptionLogicalElementRevision@endlink .  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return Equipment
    @property
    def ExistingSymbolLogicalElementRevision(self) -> Equipment:
        """
        Getter for property: (@link Equipment NXOpen.PID.Equipment@endlink) ExistingSymbolLogicalElementRevision
          the Logical Element Revision for the symbol.  
           It is only applicable when @link PID::EquipmentBuilder::SymbolSourceType PID::EquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionLogicalElementRevision PID::SymbolSourceOptionLogicalElementRevision@endlink .  
         
        """
        pass
    
    ## Setter for property: (@link Equipment NXOpen.PID.Equipment@endlink) ExistingSymbolLogicalElementRevision

    ##   the Logical Element Revision for the symbol.  
    ##    It is only applicable when @link PID::EquipmentBuilder::SymbolSourceType PID::EquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionLogicalElementRevision PID::SymbolSourceOptionLogicalElementRevision@endlink .  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ExistingSymbolLogicalElementRevision.setter
    def ExistingSymbolLogicalElementRevision(self, existingSymbolLogicalElementRevision: Equipment):
        """
        Setter for property: (@link Equipment NXOpen.PID.Equipment@endlink) ExistingSymbolLogicalElementRevision
          the Logical Element Revision for the symbol.  
           It is only applicable when @link PID::EquipmentBuilder::SymbolSourceType PID::EquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionLogicalElementRevision PID::SymbolSourceOptionLogicalElementRevision@endlink .  
         
        """
        pass
    
    ## Getter for property: (bool) FlipHorizontal
    ##   the option to flip the symbol horizontally.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @FlipVertical.setter
    def FlipVertical(self, flipVertical: bool):
        """
        Setter for property: (bool) FlipVertical
          the option to flip the symbol vertically.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FulfillmentAttributeOwner
    ##   the owner of fulfillment attributes group.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1988.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def FulfillmentAttributeOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FulfillmentAttributeOwner
          the owner of fulfillment attributes group.  
            
         
        """
        pass
    
    ## Getter for property: (str) Label
    ##   the tag of this equipment.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
          the tag of this equipment.  
             
         
        """
        pass
    
    ## Getter for property: (bool) LockAspectRatio
    ##   the option to lock the aspect ratio.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LockAspectRatio.setter
    def LockAspectRatio(self, lockAspectRatio: bool):
        """
        Setter for property: (bool) LockAspectRatio
          the option to lock the aspect ratio.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) NeedAttrOwner
    ##   the owner of need attributes group.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1988.0.0.  Use @link NXOpen::PID::EquipmentBuilder::NeedAttributeOwner NXOpen::PID::EquipmentBuilder::NeedAttributeOwner@endlink instead.  <br> 

    ## @return NXOpen.NXObject
    @property
    def NeedAttrOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) NeedAttrOwner
          the owner of need attributes group.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) NeedAttributeOwner
    ##   the owner of need attributes group.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1988.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def NeedAttributeOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) NeedAttributeOwner
          the owner of need attributes group.  
            
         
        """
        pass
    
    ## Getter for property: (str) NodeId
    ##   the current node ID of this equipment.  
    ##    It works only in edit mode, it's optional and the first node ID stored in the equipment will be used as default.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def NodeId(self) -> str:
        """
        Getter for property: (str) NodeId
          the current node ID of this equipment.  
           It works only in edit mode, it's optional and the first node ID stored in the equipment will be used as default.  
         
        """
        pass
    
    ## Setter for property: (str) NodeId

    ##   the current node ID of this equipment.  
    ##    It works only in edit mode, it's optional and the first node ID stored in the equipment will be used as default.  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @NodeId.setter
    def NodeId(self, nodeId: str):
        """
        Setter for property: (str) NodeId
          the current node ID of this equipment.  
           It works only in edit mode, it's optional and the first node ID stored in the equipment will be used as default.  
         
        """
        pass
    
    ## Getter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet
    ##   the owning sheet of this sheet element.  
    ##    Its setting method works only in creation mode.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return Sheet
    @property
    def OwningSheet(self) -> Sheet:
        """
        Getter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet
          the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    
    ## Setter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet

    ##   the owning sheet of this sheet element.  
    ##    Its setting method works only in creation mode.   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @OwningSheet.setter
    def OwningSheet(self, owningSheet: Sheet):
        """
        Setter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet
          the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    
    ## Getter for property: (@link RotateAngleOption NXOpen.PID.RotateAngleOption@endlink) Rotate
    ##   the symbol rotation angle.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return RotateAngleOption
    @property
    def Rotate(self) -> RotateAngleOption:
        """
        Getter for property: (@link RotateAngleOption NXOpen.PID.RotateAngleOption@endlink) Rotate
          the symbol rotation angle.  
             
         
        """
        pass
    
    ## Setter for property: (@link RotateAngleOption NXOpen.PID.RotateAngleOption@endlink) Rotate

    ##   the symbol rotation angle.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @Rotate.setter
    def Rotate(self, rotate: RotateAngleOption):
        """
        Setter for property: (@link RotateAngleOption NXOpen.PID.RotateAngleOption@endlink) Rotate
          the symbol rotation angle.  
             
         
        """
        pass
    
    ## Getter for property: (float) Scale
    ##   the scale value.  
    ##    It is only applicable when @link PID::EquipmentBuilder::LockAspectRatio PID::EquipmentBuilder::LockAspectRatio@endlink  is true.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
          the scale value.  
           It is only applicable when @link PID::EquipmentBuilder::LockAspectRatio PID::EquipmentBuilder::LockAspectRatio@endlink  is true.  
         
        """
        pass
    
    ## Setter for property: (float) Scale

    ##   the scale value.  
    ##    It is only applicable when @link PID::EquipmentBuilder::LockAspectRatio PID::EquipmentBuilder::LockAspectRatio@endlink  is true.  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
          the scale value.  
           It is only applicable when @link PID::EquipmentBuilder::LockAspectRatio PID::EquipmentBuilder::LockAspectRatio@endlink  is true.  
         
        """
        pass
    
    ## Getter for property: (float) ScaleX
    ##   the x scale value.  
    ##    It is only applicable when @link PID::EquipmentBuilder::LockAspectRatio PID::EquipmentBuilder::LockAspectRatio@endlink  is false.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def ScaleX(self) -> float:
        """
        Getter for property: (float) ScaleX
          the x scale value.  
           It is only applicable when @link PID::EquipmentBuilder::LockAspectRatio PID::EquipmentBuilder::LockAspectRatio@endlink  is false.  
         
        """
        pass
    
    ## Setter for property: (float) ScaleX

    ##   the x scale value.  
    ##    It is only applicable when @link PID::EquipmentBuilder::LockAspectRatio PID::EquipmentBuilder::LockAspectRatio@endlink  is false.  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ScaleX.setter
    def ScaleX(self, scaleX: float):
        """
        Setter for property: (float) ScaleX
          the x scale value.  
           It is only applicable when @link PID::EquipmentBuilder::LockAspectRatio PID::EquipmentBuilder::LockAspectRatio@endlink  is false.  
         
        """
        pass
    
    ## Getter for property: (float) ScaleY
    ##   the y scale value.  
    ##    It is only applicable when @link PID::EquipmentBuilder::LockAspectRatio PID::EquipmentBuilder::LockAspectRatio@endlink  is false.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def ScaleY(self) -> float:
        """
        Getter for property: (float) ScaleY
          the y scale value.  
           It is only applicable when @link PID::EquipmentBuilder::LockAspectRatio PID::EquipmentBuilder::LockAspectRatio@endlink  is false.  
         
        """
        pass
    
    ## Setter for property: (float) ScaleY

    ##   the y scale value.  
    ##    It is only applicable when @link PID::EquipmentBuilder::LockAspectRatio PID::EquipmentBuilder::LockAspectRatio@endlink  is false.  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ScaleY.setter
    def ScaleY(self, scaleY: float):
        """
        Setter for property: (float) ScaleY
          the y scale value.  
           It is only applicable when @link PID::EquipmentBuilder::LockAspectRatio PID::EquipmentBuilder::LockAspectRatio@endlink  is false.  
         
        """
        pass
    
    ## Getter for property: (str) SymbolId
    ##   the symbol ID of this equipment.  
    ##    It is only applicable when @link NXOpen::PID::EquipmentBuilder::SymbolSourceType NXOpen::PID::EquipmentBuilder::SymbolSourceType@endlink  is @link NXOpen::PID::SymbolSourceOptionReuseLibrary NXOpen::PID::SymbolSourceOptionReuseLibrary@endlink .  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def SymbolId(self) -> str:
        """
        Getter for property: (str) SymbolId
          the symbol ID of this equipment.  
           It is only applicable when @link NXOpen::PID::EquipmentBuilder::SymbolSourceType NXOpen::PID::EquipmentBuilder::SymbolSourceType@endlink  is @link NXOpen::PID::SymbolSourceOptionReuseLibrary NXOpen::PID::SymbolSourceOptionReuseLibrary@endlink .  
         
        """
        pass
    
    ## Setter for property: (str) SymbolId

    ##   the symbol ID of this equipment.  
    ##    It is only applicable when @link NXOpen::PID::EquipmentBuilder::SymbolSourceType NXOpen::PID::EquipmentBuilder::SymbolSourceType@endlink  is @link NXOpen::PID::SymbolSourceOptionReuseLibrary NXOpen::PID::SymbolSourceOptionReuseLibrary@endlink .  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @SymbolId.setter
    def SymbolId(self, symbolId: str):
        """
        Setter for property: (str) SymbolId
          the symbol ID of this equipment.  
           It is only applicable when @link NXOpen::PID::EquipmentBuilder::SymbolSourceType NXOpen::PID::EquipmentBuilder::SymbolSourceType@endlink  is @link NXOpen::PID::SymbolSourceOptionReuseLibrary NXOpen::PID::SymbolSourceOptionReuseLibrary@endlink .  
         
        """
        pass
    
    ## Getter for property: (@link SymbolSourceOption NXOpen.PID.SymbolSourceOption@endlink) SymbolSourceType
    ##   the symbol source type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return SymbolSourceOption
    @property
    def SymbolSourceType(self) -> SymbolSourceOption:
        """
        Getter for property: (@link SymbolSourceOption NXOpen.PID.SymbolSourceOption@endlink) SymbolSourceType
          the symbol source type   
            
         
        """
        pass
    
    ## Setter for property: (@link SymbolSourceOption NXOpen.PID.SymbolSourceOption@endlink) SymbolSourceType

    ##   the symbol source type   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @SymbolSourceType.setter
    def SymbolSourceType(self, symbolSourceType: SymbolSourceOption):
        """
        Setter for property: (@link SymbolSourceOption NXOpen.PID.SymbolSourceOption@endlink) SymbolSourceType
          the symbol source type   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseExistingID
    ##   the option to place a duplicate symbol.  
    ##    It is only applicable when @link NXOpen::PID::EquipmentBuilder::SymbolSourceType NXOpen::PID::EquipmentBuilder::SymbolSourceType@endlink  is @link NXOpen::PID::SymbolSourceOptionExistingSymbol NXOpen::PID::SymbolSourceOptionExistingSymbol@endlink .  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def UseExistingID(self) -> bool:
        """
        Getter for property: (bool) UseExistingID
          the option to place a duplicate symbol.  
           It is only applicable when @link NXOpen::PID::EquipmentBuilder::SymbolSourceType NXOpen::PID::EquipmentBuilder::SymbolSourceType@endlink  is @link NXOpen::PID::SymbolSourceOptionExistingSymbol NXOpen::PID::SymbolSourceOptionExistingSymbol@endlink .  
         
        """
        pass
    
    ## Setter for property: (bool) UseExistingID

    ##   the option to place a duplicate symbol.  
    ##    It is only applicable when @link NXOpen::PID::EquipmentBuilder::SymbolSourceType NXOpen::PID::EquipmentBuilder::SymbolSourceType@endlink  is @link NXOpen::PID::SymbolSourceOptionExistingSymbol NXOpen::PID::SymbolSourceOptionExistingSymbol@endlink .  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @UseExistingID.setter
    def UseExistingID(self, useExistingID: bool):
        """
        Setter for property: (bool) UseExistingID
          the option to place a duplicate symbol.  
           It is only applicable when @link NXOpen::PID::EquipmentBuilder::SymbolSourceType NXOpen::PID::EquipmentBuilder::SymbolSourceType@endlink  is @link NXOpen::PID::SymbolSourceOptionExistingSymbol NXOpen::PID::SymbolSourceOptionExistingSymbol@endlink .  
         
        """
        pass
    
    ##  Detaches the equipment from all attached connections. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def DetachAllConnections(builder: EquipmentBuilder) -> None:
        """
         Detaches the equipment from all attached connections. 
        """
        pass
    
    ##  Gets connection location for the inline symbol. 
    ##  @return A tuple consisting of (pipe, connectionId, segementId, percent). 
    ##  - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
    ##  - connectionId is: str.
    ##  - segementId is: int.
    ##  - percent is: float.

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInlineSymbolLocation(builder: EquipmentBuilder) -> Tuple[Pipe, str, int, float]:
        """
         Gets connection location for the inline symbol. 
         @return A tuple consisting of (pipe, connectionId, segementId, percent). 
         - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
         - connectionId is: str.
         - segementId is: int.
         - percent is: float.

        """
        pass
    
    ##  Gets the symbol location. 
    ##  @return location (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the symbol location. .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLocation(builder: EquipmentBuilder) -> NXOpen.Point2d:
        """
         Gets the symbol location. 
         @return location (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the symbol location. .
        """
        pass
    
    ##  Gets new connection after inserting an inline symbol. 
    ##  @return A tuple consisting of (pipe, connectionId). 
    ##  - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
    ##  - connectionId is: str.

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNewInlineConnection(builder: EquipmentBuilder) -> Tuple[Pipe, str]:
        """
         Gets new connection after inserting an inline symbol. 
         @return A tuple consisting of (pipe, connectionId). 
         - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
         - connectionId is: str.

        """
        pass
    
    ##  Get the node object of the equipment builder. 
    ##  @return node (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNode(builder: EquipmentBuilder) -> NXOpen.Diagramming.Node:
        """
         Get the node object of the equipment builder. 
         @return node (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink): .
        """
        pass
    
    ##  Sets the attached symbol. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the port id of this equipment symbol for the attachment. 
    def SetAttachedSymbol(builder: EquipmentBuilder, fromPortId: str, toSymbol: NXOpen.NXObject, toSymbolNodeSidId: str, toSymbolPortId: str) -> None:
        """
         Sets the attached symbol. 
        """
        pass
    
    ##  Sets the fulfillment data of the symbol. The input symbol should be a 3D one and in the same category with the entity of the builder
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="symbolID"> (str) </param>
    def SetFulfillment(builder: EquipmentBuilder, symbolID: str) -> None:
        """
         Sets the fulfillment data of the symbol. The input symbol should be a 3D one and in the same category with the entity of the builder
        """
        pass
    
    ##  Sets connection location for the inline symbol. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="pipe"> (@link Pipe NXOpen.PID.Pipe@endlink) </param>
    ## <param name="connectionId"> (str) </param>
    ## <param name="segementId"> (int) </param>
    ## <param name="percent"> (float) </param>
    def SetInlineSymbolLocation(builder: EquipmentBuilder, pipe: Pipe, connectionId: str, segementId: int, percent: float) -> None:
        """
         Sets connection location for the inline symbol. 
        """
        pass
    
    ##  Sets the symbol location. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the symbol location. 
    def SetLocation(builder: EquipmentBuilder, location: NXOpen.Point2d) -> None:
        """
         Sets the symbol location. 
        """
        pass
    
##  Represents the equipment class.  <br> To create or edit an instance of this class, use @link NXOpen::PID::EquipmentBuilder  NXOpen::PID::EquipmentBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Equipment(LogicalElementRevision): 
    """ Represents the equipment class. """


    ##  Get one port of the equipment by port ID.
    ##  @return port (@link Port NXOpen.PID.Port@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="portId"> (str) </param>
    def GetPort(equipment: Equipment, portId: str) -> Port:
        """
         Get one port of the equipment by port ID.
         @return port (@link Port NXOpen.PID.Port@endlink): .
        """
        pass
    
    ##  Get ports of the equipment.
    ##  @return ports (@link Port List[NXOpen.PID.Port]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPorts(equipment: Equipment) -> List[Port]:
        """
         Get ports of the equipment.
         @return ports (@link Port List[NXOpen.PID.Port]@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
import NXOpen.Gateway
##  Represents a builder class that performs Generic File New operations.
##          <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateFilenewapplicationBuilder  NXOpen::PID::PidManager::CreateFilenewapplicationBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class FileNewApplicationBuilder(NXOpen.Gateway.IGenericFileNewApplicationBuilder): 
    """ Represents a builder class that performs Generic File New operations.
        """


    ## Getter for property: (@link NXOpen.DisplayPartOption NXOpen.DisplayPartOption@endlink) DisplayPartOption
    ##   the display part option for the new file being created   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.DisplayPartOption
    @property
    def DisplayPartOption(self) -> NXOpen.DisplayPartOption:
        """
        Getter for property: (@link NXOpen.DisplayPartOption NXOpen.DisplayPartOption@endlink) DisplayPartOption
          the display part option for the new file being created   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayPartOption NXOpen.DisplayPartOption@endlink) DisplayPartOption

    ##   the display part option for the new file being created   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DisplayPartOption.setter
    def DisplayPartOption(self, displayPartOption: NXOpen.DisplayPartOption):
        """
        Setter for property: (@link NXOpen.DisplayPartOption NXOpen.DisplayPartOption@endlink) DisplayPartOption
          the display part option for the new file being created   
            
         
        """
        pass
    
    ## Getter for property: (str) TemplateBaseTcType
    ##   the BaseTCType of the template part from which to create the new file   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def TemplateBaseTcType(self) -> str:
        """
        Getter for property: (str) TemplateBaseTcType
          the BaseTCType of the template part from which to create the new file   
            
         
        """
        pass
    
    ## Setter for property: (str) TemplateBaseTcType

    ##   the BaseTCType of the template part from which to create the new file   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TemplateBaseTcType.setter
    def TemplateBaseTcType(self, baseTCType: str):
        """
        Setter for property: (str) TemplateBaseTcType
          the BaseTCType of the template part from which to create the new file   
            
         
        """
        pass
    
    ## Getter for property: (str) TemplateFileName
    ##   the name of the template part from which to create the new file   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def TemplateFileName(self) -> str:
        """
        Getter for property: (str) TemplateFileName
          the name of the template part from which to create the new file   
            
         
        """
        pass
    
    ## Setter for property: (str) TemplateFileName

    ##   the name of the template part from which to create the new file   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TemplateFileName.setter
    def TemplateFileName(self, templateFileName: str):
        """
        Setter for property: (str) TemplateFileName
          the name of the template part from which to create the new file   
            
         
        """
        pass
    
    ## Getter for property: (str) TemplatePresentationName
    ##   the presentation name of the underlying template which is used for creating new file    
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def TemplatePresentationName(self) -> str:
        """
        Getter for property: (str) TemplatePresentationName
          the presentation name of the underlying template which is used for creating new file    
            
         
        """
        pass
    
    ## Setter for property: (str) TemplatePresentationName

    ##   the presentation name of the underlying template which is used for creating new file    
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TemplatePresentationName.setter
    def TemplatePresentationName(self, presentationName: str):
        """
        Setter for property: (str) TemplatePresentationName
          the presentation name of the underlying template which is used for creating new file    
            
         
        """
        pass
    
    ## Getter for property: (str) TemplateTcType
    ##   the TCType of the template part from which to create the new file   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def TemplateTcType(self) -> str:
        """
        Getter for property: (str) TemplateTcType
          the TCType of the template part from which to create the new file   
            
         
        """
        pass
    
    ## Setter for property: (str) TemplateTcType

    ##   the TCType of the template part from which to create the new file   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TemplateTcType.setter
    def TemplateTcType(self, tcType: str):
        """
        Setter for property: (str) TemplateTcType
          the TCType of the template part from which to create the new file   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FileNewTemplateType NXOpen.FileNewTemplateType@endlink) TemplateType
    ##   the template type for the new file being created   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.FileNewTemplateType
    @property
    def TemplateType(self) -> NXOpen.FileNewTemplateType:
        """
        Getter for property: (@link NXOpen.FileNewTemplateType NXOpen.FileNewTemplateType@endlink) TemplateType
          the template type for the new file being created   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.FileNewTemplateType NXOpen.FileNewTemplateType@endlink) TemplateType

    ##   the template type for the new file being created   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TemplateType.setter
    def TemplateType(self, templateType: NXOpen.FileNewTemplateType):
        """
        Setter for property: (@link NXOpen.FileNewTemplateType NXOpen.FileNewTemplateType@endlink) TemplateType
          the template type for the new file being created   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Part.Units NXOpen.Part.Units@endlink) TemplateUnits
    ##   the units for the new file being created   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Part.Units
    @property
    def TemplateUnits(self) -> NXOpen.Part.Units:
        """
        Getter for property: (@link NXOpen.Part.Units NXOpen.Part.Units@endlink) TemplateUnits
          the units for the new file being created   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Part.Units NXOpen.Part.Units@endlink) TemplateUnits

    ##   the units for the new file being created   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TemplateUnits.setter
    def TemplateUnits(self, units: NXOpen.Part.Units):
        """
        Setter for property: (@link NXOpen.Part.Units NXOpen.Part.Units@endlink) TemplateUnits
          the units for the new file being created   
            
         
        """
        pass
    
    ##  The @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink  of the subset.
    ##         
    ##  @return collaborativeDesign (@link NXOpen.CollaborativeDesign NXOpen.CollaborativeDesign@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def GetCollaborativeDesign(builder: FileNewApplicationBuilder) -> NXOpen.CollaborativeDesign:
        """
         The @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink  of the subset.
                
         @return collaborativeDesign (@link NXOpen.CollaborativeDesign NXOpen.CollaborativeDesign@endlink): .
        """
        pass
    
    ##  The @link NXOpen::Assemblies::Partition NXOpen::Assemblies::Partition@endlink  of the subset.
    ##         
    ##  @return partitions (@link NXOpen.Assemblies.Partition List[NXOpen.Assemblies.Partition]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def GetTargetPartitions(builder: FileNewApplicationBuilder) -> List[NXOpen.Assemblies.Partition]:
        """
         The @link NXOpen::Assemblies::Partition NXOpen::Assemblies::Partition@endlink  of the subset.
                
         @return partitions (@link NXOpen.Assemblies.Partition List[NXOpen.Assemblies.Partition]@endlink): .
        """
        pass
    
    ##  The @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink  of the subset.
    ##         
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="collaborativeDesign"> (@link NXOpen.CollaborativeDesign NXOpen.CollaborativeDesign@endlink) </param>
    def SetCollaborativeDesign(builder: FileNewApplicationBuilder, collaborativeDesign: NXOpen.CollaborativeDesign) -> None:
        """
         The @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink  of the subset.
                
        """
        pass
    
    ##  The @link Assemblies::Partition Assemblies::Partition@endlink  of the subset.
    ##         
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="partitions"> (@link NXOpen.Assemblies.Partition List[NXOpen.Assemblies.Partition]@endlink) </param>
    def SetTargetPartitions(builder: FileNewApplicationBuilder, partitions: List[NXOpen.Assemblies.Partition]) -> None:
        """
         The @link Assemblies::Partition Assemblies::Partition@endlink  of the subset.
                
        """
        pass
    
import NXOpen
##   @brief 
##     Represents FlowDirectionArrowBuilder  
## 
##  
##       <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateFlowDirectionArrowBuilder  NXOpen::PID::PidManager::CreateFlowDirectionArrowBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class FlowDirectionArrowBuilder(NXOpen.Builder): 
    """ <summary>
    Represents FlowDirectionArrowBuilder </summary>
     """


    ## Getter for property: (float) LocationPercent
    ##   the percent along the segment for this Flow Direction Arrow.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LocationSegment.setter
    def LocationSegment(self, locationPercent: int):
        """
        Setter for property: (int) LocationSegment
          the segment this Flow Direction Arrow is located on.  
             
         
        """
        pass
    
    ##  Gets the connection for this Flow Direction Arrow. 
    ##  @return A tuple consisting of (pipe, connectionId). 
    ##  - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
    ##  - connectionId is: str.

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def GetConnection(builder: FlowDirectionArrowBuilder) -> Tuple[Pipe, str]:
        """
         Gets the connection for this Flow Direction Arrow. 
         @return A tuple consisting of (pipe, connectionId). 
         - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
         - connectionId is: str.

        """
        pass
    
    ##  Change the direction of FDA. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def ReverseDirection(builder: FlowDirectionArrowBuilder) -> None:
        """
         Change the direction of FDA. 
        """
        pass
    
    ##  Sets the connection for this Flow Direction Arrow. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="equipment"> (@link Pipe NXOpen.PID.Pipe@endlink) </param>
    ## <param name="connectionId"> (str) </param>
    def SetConnection(builder: FlowDirectionArrowBuilder, equipment: Pipe, connectionId: str) -> None:
        """
         Sets the connection for this Flow Direction Arrow. 
        """
        pass
    
import NXOpen
##  Represents a collection of FlowDirectionArrow.  <br> To obtain an instance of this class, refer to @link NXOpen::PID::Sheet  NXOpen::PID::Sheet @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class FlowDirectionArrowCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of FlowDirectionArrow. """


    ##  Finds the @link PID::FlowDirectionArrow PID::FlowDirectionArrow@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return flowdirectionarrow (@link FlowDirectionArrow NXOpen.PID.FlowDirectionArrow@endlink):  @link PID::FlowDirectionArrow PID::FlowDirectionArrow@endlink  with this name. .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_reader ("NX P and ID Design Reader") OR nx_pid_design_author ("NX P and ID Design Author")
    ##  Identifier to be found 
    def FindObject(sheet: FlowDirectionArrowCollection, journalIdentifier: str) -> FlowDirectionArrow:
        """
         Finds the @link PID::FlowDirectionArrow PID::FlowDirectionArrow@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return flowdirectionarrow (@link FlowDirectionArrow NXOpen.PID.FlowDirectionArrow@endlink):  @link PID::FlowDirectionArrow PID::FlowDirectionArrow@endlink  with this name. .
        """
        pass
    
import NXOpen
##   @brief  A symbol that indicates the direction the of the flow 
## 
##    <br> To create or edit an instance of this class, use @link NXOpen::PID::FlowDirectionArrowBuilder  NXOpen::PID::FlowDirectionArrowBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class FlowDirectionArrow(NXOpen.NXObject): 
    """ <summary> A symbol that indicates the direction the of the flow</summary> """
    pass


import NXOpen
import NXOpen.Diagramming
import NXOpen.PLAS
##  Represents a @link PID::InstrumentationSymbol PID::InstrumentationSymbol@endlink  and @link PID::Instrumentation PID::Instrumentation@endlink builder  <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateInstrumentationBuilder  NXOpen::PID::PidManager::CreateInstrumentationBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## SymbolSize </term> <description> 
##  
## 15 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1847.0.0  <br> 

class InstrumentationBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>PID.InstrumentationSymbol</ja_class> and <ja_class>PID.Instrumentation</ja_class>builder """


    ## Getter for property: (str) ControlLoopName
    ##   the control loop name.  
    ##    Used under native mode or instrumentation lightweight mode.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def ControlLoopName(self) -> str:
        """
        Getter for property: (str) ControlLoopName
          the control loop name.  
           Used under native mode or instrumentation lightweight mode.   
         
        """
        pass
    
    ## Setter for property: (str) ControlLoopName

    ##   the control loop name.  
    ##    Used under native mode or instrumentation lightweight mode.   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ControlLoopName.setter
    def ControlLoopName(self, controlLoopName: str):
        """
        Setter for property: (str) ControlLoopName
          the control loop name.  
           Used under native mode or instrumentation lightweight mode.   
         
        """
        pass
    
    ## Getter for property: (str) FunctionId
    ##   the function   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def FunctionId(self) -> str:
        """
        Getter for property: (str) FunctionId
          the function   
            
         
        """
        pass
    
    ## Setter for property: (str) FunctionId

    ##   the function   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @FunctionId.setter
    def FunctionId(self, functionId: str):
        """
        Setter for property: (str) FunctionId
          the function   
            
         
        """
        pass
    
    ## Getter for property: (@link InstrumentationType NXOpen.PID.InstrumentationType@endlink) InstrumentationType
    ##   the instrumentation type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return InstrumentationType
    @property
    def InstrumentationType(self) -> InstrumentationType:
        """
        Getter for property: (@link InstrumentationType NXOpen.PID.InstrumentationType@endlink) InstrumentationType
          the instrumentation type   
            
         
        """
        pass
    
    ## Setter for property: (@link InstrumentationType NXOpen.PID.InstrumentationType@endlink) InstrumentationType

    ##   the instrumentation type   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @InstrumentationType.setter
    def InstrumentationType(self, type: InstrumentationType):
        """
        Setter for property: (@link InstrumentationType NXOpen.PID.InstrumentationType@endlink) InstrumentationType
          the instrumentation type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.DiagrammingArrowtype NXOpen.Diagramming.DiagrammingArrowtype@endlink) LeaderArrowhead
    ##   the arrow type of the end arrow.  
    ##    Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Diagramming.DiagrammingArrowtype
    @property
    def LeaderArrowhead(self) -> NXOpen.Diagramming.DiagrammingArrowtype:
        """
        Getter for property: (@link NXOpen.Diagramming.DiagrammingArrowtype NXOpen.Diagramming.DiagrammingArrowtype@endlink) LeaderArrowhead
          the arrow type of the end arrow.  
           Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.DiagrammingArrowtype NXOpen.Diagramming.DiagrammingArrowtype@endlink) LeaderArrowhead

    ##   the arrow type of the end arrow.  
    ##    Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LeaderArrowhead.setter
    def LeaderArrowhead(self, arrowTypeOption: NXOpen.Diagramming.DiagrammingArrowtype):
        """
        Setter for property: (@link NXOpen.Diagramming.DiagrammingArrowtype NXOpen.Diagramming.DiagrammingArrowtype@endlink) LeaderArrowhead
          the arrow type of the end arrow.  
           Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
         
        """
        pass
    
    ## Getter for property: (float) LeaderStubLength
    ##   the stub length of this leader line.  
    ##    The negative value is not expected, and only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def LeaderStubLength(self) -> float:
        """
        Getter for property: (float) LeaderStubLength
          the stub length of this leader line.  
           The negative value is not expected, and only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
         
        """
        pass
    
    ## Setter for property: (float) LeaderStubLength

    ##   the stub length of this leader line.  
    ##    The negative value is not expected, and only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LeaderStubLength.setter
    def LeaderStubLength(self, stubLength: float):
        """
        Setter for property: (float) LeaderStubLength
          the stub length of this leader line.  
           The negative value is not expected, and only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.DiagrammingStubsides NXOpen.Diagramming.DiagrammingStubsides@endlink) LeaderStubSide
    ##   the stub sides of this leader line.  
    ##    Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Diagramming.DiagrammingStubsides
    @property
    def LeaderStubSide(self) -> NXOpen.Diagramming.DiagrammingStubsides:
        """
        Getter for property: (@link NXOpen.Diagramming.DiagrammingStubsides NXOpen.Diagramming.DiagrammingStubsides@endlink) LeaderStubSide
          the stub sides of this leader line.  
           Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.DiagrammingStubsides NXOpen.Diagramming.DiagrammingStubsides@endlink) LeaderStubSide

    ##   the stub sides of this leader line.  
    ##    Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LeaderStubSide.setter
    def LeaderStubSide(self, stubSides: NXOpen.Diagramming.DiagrammingStubsides):
        """
        Setter for property: (@link NXOpen.Diagramming.DiagrammingStubsides NXOpen.Diagramming.DiagrammingStubsides@endlink) LeaderStubSide
          the stub sides of this leader line.  
           Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
         
        """
        pass
    
    ## Getter for property: (bool) LeaderUsed
    ##   the option to use leader.  
    ##    Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def LeaderUsed(self) -> bool:
        """
        Getter for property: (bool) LeaderUsed
          the option to use leader.  
           Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
         
        """
        pass
    
    ## Setter for property: (bool) LeaderUsed

    ##   the option to use leader.  
    ##    Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LeaderUsed.setter
    def LeaderUsed(self, isLeaderUsed: bool):
        """
        Setter for property: (bool) LeaderUsed
          the option to use leader.  
           Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink   
         
        """
        pass
    
    ## Getter for property: (str) MeasurementVariable
    ##   the measured variable   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def MeasurementVariable(self) -> str:
        """
        Getter for property: (str) MeasurementVariable
          the measured variable   
            
         
        """
        pass
    
    ## Setter for property: (str) MeasurementVariable

    ##   the measured variable   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MeasurementVariable.setter
    def MeasurementVariable(self, measurementVariable: str):
        """
        Setter for property: (str) MeasurementVariable
          the measured variable   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PLAS.Run NXOpen.PLAS.Run@endlink) OwningControlLoop
    ##   the control loop.  
    ##     Used under manager mode or instrumentation non-lightweight mode.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.PLAS.Run
    @property
    def OwningControlLoop(self) -> NXOpen.PLAS.Run:
        """
        Getter for property: (@link NXOpen.PLAS.Run NXOpen.PLAS.Run@endlink) OwningControlLoop
          the control loop.  
            Used under manager mode or instrumentation non-lightweight mode.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PLAS.Run NXOpen.PLAS.Run@endlink) OwningControlLoop

    ##   the control loop.  
    ##     Used under manager mode or instrumentation non-lightweight mode.   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @OwningControlLoop.setter
    def OwningControlLoop(self, controlLoop: NXOpen.PLAS.Run):
        """
        Setter for property: (@link NXOpen.PLAS.Run NXOpen.PLAS.Run@endlink) OwningControlLoop
          the control loop.  
            Used under manager mode or instrumentation non-lightweight mode.   
         
        """
        pass
    
    ## Getter for property: (@link InstrumentationControlLoopType NXOpen.PID.InstrumentationControlLoopType@endlink) OwningControlLoopType
    ##   the owning control loop option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return InstrumentationControlLoopType
    @property
    def OwningControlLoopType(self) -> InstrumentationControlLoopType:
        """
        Getter for property: (@link InstrumentationControlLoopType NXOpen.PID.InstrumentationControlLoopType@endlink) OwningControlLoopType
          the owning control loop option   
            
         
        """
        pass
    
    ## Setter for property: (@link InstrumentationControlLoopType NXOpen.PID.InstrumentationControlLoopType@endlink) OwningControlLoopType

    ##   the owning control loop option   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @OwningControlLoopType.setter
    def OwningControlLoopType(self, type: InstrumentationControlLoopType):
        """
        Setter for property: (@link InstrumentationControlLoopType NXOpen.PID.InstrumentationControlLoopType@endlink) OwningControlLoopType
          the owning control loop option   
            
         
        """
        pass
    
    ## Getter for property: (float) SymbolSize
    ##   the symbol size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def SymbolSize(self) -> float:
        """
        Getter for property: (float) SymbolSize
          the symbol size   
            
         
        """
        pass
    
    ## Setter for property: (float) SymbolSize

    ##   the symbol size   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SymbolSize.setter
    def SymbolSize(self, symbolSize: float):
        """
        Setter for property: (float) SymbolSize
          the symbol size   
            
         
        """
        pass
    
    ## Getter for property: (@link InstrumentationSymbolType NXOpen.PID.InstrumentationSymbolType@endlink) SymbolType
    ##   the symbol type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return InstrumentationSymbolType
    @property
    def SymbolType(self) -> InstrumentationSymbolType:
        """
        Getter for property: (@link InstrumentationSymbolType NXOpen.PID.InstrumentationSymbolType@endlink) SymbolType
          the symbol type   
            
         
        """
        pass
    
    ## Setter for property: (@link InstrumentationSymbolType NXOpen.PID.InstrumentationSymbolType@endlink) SymbolType

    ##   the symbol type   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SymbolType.setter
    def SymbolType(self, symbolType: InstrumentationSymbolType):
        """
        Setter for property: (@link InstrumentationSymbolType NXOpen.PID.InstrumentationSymbolType@endlink) SymbolType
          the symbol type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyle
    ##   the text style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Diagramming.TextStyleBuilder
    @property
    def TextStyle(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyle
          the text style   
            
         
        """
        pass
    
    ##  Detaches the instrumentation from its attachments. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeSymbol NXOpen::PID::InstrumentationTypeSymbol@endlink 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def Detach(builder: InstrumentationBuilder) -> None:
        """
         Detaches the instrumentation from its attachments. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeSymbol NXOpen::PID::InstrumentationTypeSymbol@endlink 
        """
        pass
    
    ##  Gets connection location for the inline symbol. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeSymbol NXOpen::PID::InstrumentationTypeSymbol@endlink  and the instrument is inserted into one pipe.
    ##  @return A tuple consisting of (pipe, connectionId, segementId, percent). 
    ##  - pipe is: @link NXOpen.NXObject NXOpen.NXObject@endlink. @link NXOpen::PID::NativePipe NXOpen::PID::NativePipe@endlink  or @link NXOpen::PID::Pipe NXOpen::PID::Pipe@endlink .
    ##  - connectionId is: str.
    ##  - segementId is: int.
    ##  - percent is: float.

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInlineSymbolLocation(builder: InstrumentationBuilder) -> Tuple[NXOpen.NXObject, str, int, float]:
        """
         Gets connection location for the inline symbol. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeSymbol NXOpen::PID::InstrumentationTypeSymbol@endlink  and the instrument is inserted into one pipe.
         @return A tuple consisting of (pipe, connectionId, segementId, percent). 
         - pipe is: @link NXOpen.NXObject NXOpen.NXObject@endlink. @link NXOpen::PID::NativePipe NXOpen::PID::NativePipe@endlink  or @link NXOpen::PID::Pipe NXOpen::PID::Pipe@endlink .
         - connectionId is: str.
         - segementId is: int.
         - percent is: float.

        """
        pass
    
    ##  Gets the reference object and point of the instrumentation annotation. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink 
    ##  @return A tuple consisting of (reference, point, connectionSegementId). 
    ##  - reference is: @link NXOpen.Diagramming.SheetElement NXOpen.Diagramming.SheetElement@endlink.
    ##  - point is: @link NXOpen.Point2d NXOpen.Point2d@endlink. the instrumentation annotation's leader point. .
    ##  - connectionSegementId is: int.

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLeaderTerminator(builder: InstrumentationBuilder) -> Tuple[NXOpen.Diagramming.SheetElement, NXOpen.Point2d, int]:
        """
         Gets the reference object and point of the instrumentation annotation. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink 
         @return A tuple consisting of (reference, point, connectionSegementId). 
         - reference is: @link NXOpen.Diagramming.SheetElement NXOpen.Diagramming.SheetElement@endlink.
         - point is: @link NXOpen.Point2d NXOpen.Point2d@endlink. the instrumentation annotation's leader point. .
         - connectionSegementId is: int.

        """
        pass
    
    ##  Gets the instrumentation location. 
    ##  @return location (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the instrumentation location. .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLocation(builder: InstrumentationBuilder) -> NXOpen.Point2d:
        """
         Gets the instrumentation location. 
         @return location (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the instrumentation location. .
        """
        pass
    
    ##  Gets new pipe after inserting an inline symbol. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeSymbol NXOpen::PID::InstrumentationTypeSymbol@endlink  and the instrument is inserted into one pipe.
    ##  @return A tuple consisting of (pipe, connectionId). 
    ##  - pipe is: @link NXOpen.NXObject NXOpen.NXObject@endlink. @link NXOpen::PID::NativePipe NXOpen::PID::NativePipe@endlink  or @link NXOpen::PID::Pipe NXOpen::PID::Pipe@endlink .
    ##  - connectionId is: str.

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNewInlineConnection(builder: InstrumentationBuilder) -> Tuple[NXOpen.NXObject, str]:
        """
         Gets new pipe after inserting an inline symbol. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeSymbol NXOpen::PID::InstrumentationTypeSymbol@endlink  and the instrument is inserted into one pipe.
         @return A tuple consisting of (pipe, connectionId). 
         - pipe is: @link NXOpen.NXObject NXOpen.NXObject@endlink. @link NXOpen::PID::NativePipe NXOpen::PID::NativePipe@endlink  or @link NXOpen::PID::Pipe NXOpen::PID::Pipe@endlink .
         - connectionId is: str.

        """
        pass
    
    ##  Get the node object of the instrumentation. 
    ##  @return node (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNode(builder: InstrumentationBuilder) -> NXOpen.Diagramming.Node:
        """
         Get the node object of the instrumentation. 
         @return node (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink): .
        """
        pass
    
    ##  Set the attached instrument symbol. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeSymbol NXOpen::PID::InstrumentationTypeSymbol@endlink 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  @link NXOpen::PID::InstrumentationSymbol NXOpen::PID::InstrumentationSymbol@endlink  or @link NXOpen::PID::Instrumentation NXOpen::PID::Instrumentation@endlink 
    def SetAttachedInstrumentSymbol(builder: InstrumentationBuilder, fromPortId: str, toInstrumentSymbol: NXOpen.NXObject, toPortId: str) -> None:
        """
         Set the attached instrument symbol. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeSymbol NXOpen::PID::InstrumentationTypeSymbol@endlink 
        """
        pass
    
    ##  Sets connection location for the inline symbol. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeSymbol NXOpen::PID::InstrumentationTypeSymbol@endlink  and the instrument is inserted into one pipe.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  @link NXOpen::PID::NativePipe NXOpen::PID::NativePipe@endlink  or @link NXOpen::PID::Pipe NXOpen::PID::Pipe@endlink 
    def SetInlineSymbolLocation(builder: InstrumentationBuilder, pipe: NXOpen.NXObject, connectionId: str, segementId: int, percent: float) -> None:
        """
         Sets connection location for the inline symbol. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeSymbol NXOpen::PID::InstrumentationTypeSymbol@endlink  and the instrument is inserted into one pipe.
        """
        pass
    
    ##  Sets the reference object and point of the instrumentation annotation. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the instrumentation annotation's leader point. 
    def SetLeaderTerminator(builder: InstrumentationBuilder, reference: NXOpen.Diagramming.SheetElement, point: NXOpen.Point2d, connectionSegementId: int) -> None:
        """
         Sets the reference object and point of the instrumentation annotation. Only used when the instrumentation type is @link NXOpen::PID::InstrumentationTypeAnnotation NXOpen::PID::InstrumentationTypeAnnotation@endlink 
        """
        pass
    
    ##  Sets the instrumentation location. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the instrumentation location. 
    def SetLocation(builder: InstrumentationBuilder, location: NXOpen.Point2d) -> None:
        """
         Sets the instrumentation location. 
        """
        pass
    
## Represents the identification display for the control loop of the instrumentation symbols. 
##  control loop Id. 
class InstrumentationControlLoopDisplay(Enum):
    """
    Members Include: <Id> <Name> <Blank>
    """
    Id: int
    Name: int
    Blank: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> InstrumentationControlLoopDisplay:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## Represents the pipe instrumentation control loop type. 
##  unassigned control loop. 
class InstrumentationControlLoopType(Enum):
    """
    Members Include: <Unassigned> <Active> <Inferred> <Specified>
    """
    Unassigned: int
    Active: int
    Inferred: int
    Specified: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> InstrumentationControlLoopType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
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


##  Represents the InstrumentationSymbol class.  <br> To create or edit an instance of this class, use @link NXOpen::PID::InstrumentationBuilder  NXOpen::PID::InstrumentationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class InstrumentationSymbol(Equipment): 
    """ Represents the InstrumentationSymbol class. """
    pass


## Represents the instrumentation type. 
##  instrumentation symbol. 
class InstrumentationType(Enum):
    """
    Members Include: <Symbol> <Annotation>
    """
    Symbol: int
    Annotation: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> InstrumentationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.DiagrammingLibraryAuthor
##   @brief  Represents a LibraryAuthoringBuilder.  
## 
##   
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.  <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateLibraryAuthoringBuilder  NXOpen::PID::PidManager::CreateLibraryAuthoringBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Symbol2D.Image.CaptureMethod </term> <description> 
##  
## GraphicsArea </description> </item> 
## 
## <item><term> 
##  
## Symbol2D.Image.Format </term> <description> 
##  
## Bmp </description> </item> 
## 
## <item><term> 
##  
## Symbol2D.Image.Size </term> <description> 
##  
## Pixels64 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.1  <br> 

class LibraryAuthoringBuilder(NXOpen.Builder): 
    """ <summary> Represents a LibraryAuthoringBuilder. </summary> 
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>. """


    ## Getter for property: (@link NXOpen.DiagrammingLibraryAuthor.LineTypeBuilderList NXOpen.DiagrammingLibraryAuthor.LineTypeBuilderList@endlink) LineTypes
    ##   the list of line types.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.DiagrammingLibraryAuthor.LineTypeBuilderList
    @property
    def LineTypes(self) -> NXOpen.DiagrammingLibraryAuthor.LineTypeBuilderList:
        """
        Getter for property: (@link NXOpen.DiagrammingLibraryAuthor.LineTypeBuilderList NXOpen.DiagrammingLibraryAuthor.LineTypeBuilderList@endlink) LineTypes
          the list of line types.  
             
         
        """
        pass
    
    ## Getter for property: (str) OutputFolder
    ##   the output folder for generated files.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return str
    @property
    def OutputFolder(self) -> str:
        """
        Getter for property: (str) OutputFolder
          the output folder for generated files.  
             
         
        """
        pass
    
    ## Setter for property: (str) OutputFolder

    ##   the output folder for generated files.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @OutputFolder.setter
    def OutputFolder(self, outputFolder: str):
        """
        Setter for property: (str) OutputFolder
          the output folder for generated files.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DiagrammingLibraryAuthor.PipeStockBuilder NXOpen.DiagrammingLibraryAuthor.PipeStockBuilder@endlink) PipeStock
    ##   the pipe stock sub-builder.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.DiagrammingLibraryAuthor.PipeStockBuilder
    @property
    def PipeStock(self) -> NXOpen.DiagrammingLibraryAuthor.PipeStockBuilder:
        """
        Getter for property: (@link NXOpen.DiagrammingLibraryAuthor.PipeStockBuilder NXOpen.DiagrammingLibraryAuthor.PipeStockBuilder@endlink) PipeStock
          the pipe stock sub-builder.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DiagrammingLibraryAuthor.Symbol2DBuilder NXOpen.DiagrammingLibraryAuthor.Symbol2DBuilder@endlink) Symbol2D
    ##   the symbol 2D sub-builder.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.DiagrammingLibraryAuthor.Symbol2DBuilder
    @property
    def Symbol2D(self) -> NXOpen.DiagrammingLibraryAuthor.Symbol2DBuilder:
        """
        Getter for property: (@link NXOpen.DiagrammingLibraryAuthor.Symbol2DBuilder NXOpen.DiagrammingLibraryAuthor.Symbol2DBuilder@endlink) Symbol2D
          the symbol 2D sub-builder.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DiagrammingLibraryAuthor.Symbol3DBuilder NXOpen.DiagrammingLibraryAuthor.Symbol3DBuilder@endlink) Symbol3D
    ##   the symbol 3D sub-builder.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.DiagrammingLibraryAuthor.Symbol3DBuilder
    @property
    def Symbol3D(self) -> NXOpen.DiagrammingLibraryAuthor.Symbol3DBuilder:
        """
        Getter for property: (@link NXOpen.DiagrammingLibraryAuthor.Symbol3DBuilder NXOpen.DiagrammingLibraryAuthor.Symbol3DBuilder@endlink) Symbol3D
          the symbol 3D sub-builder.  
             
         
        """
        pass
    
    ##  Creates a new 3D symbol 
    ##  @return symbolObject (@link NXOpen.DiagrammingLibraryAuthor.AttributeHolder NXOpen.DiagrammingLibraryAuthor.AttributeHolder@endlink):  the symbol object .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="instanceId"> (str) </param>
    ## <param name="partId"> (str) </param>
    ## <param name="partName"> (str) </param>
    ## <param name="numberName"> (str) </param>
    def Create3DSymbol(builder: LibraryAuthoringBuilder, instanceId: str, partId: str, partName: str, numberName: str) -> NXOpen.DiagrammingLibraryAuthor.AttributeHolder:
        """
         Creates a new 3D symbol 
         @return symbolObject (@link NXOpen.DiagrammingLibraryAuthor.AttributeHolder NXOpen.DiagrammingLibraryAuthor.AttributeHolder@endlink):  the symbol object .
        """
        pass
    
    ##  Creates a new line type 
    ##  @return lineType (@link NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    def CreateLineType(builder: LibraryAuthoringBuilder) -> NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder:
        """
         Creates a new line type 
         @return lineType (@link NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder@endlink): .
        """
        pass
    
    ##  Deletes the 3D symbol which is new created 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the symbol object,
    ##                 only accept the object which is got by @link NXOpen::PID::LibraryAuthoringBuilder::Create3DSymbol NXOpen::PID::LibraryAuthoringBuilder::Create3DSymbol@endlink  
    def Delete3DSymbol(builder: LibraryAuthoringBuilder, symbolObject: NXOpen.DiagrammingLibraryAuthor.AttributeHolder) -> None:
        """
         Deletes the 3D symbol which is new created 
        """
        pass
    
    ##  Gets the symbol objects which have user attributes of the symbol. 
    ##  @return symbolObjects (@link NXOpen.DiagrammingLibraryAuthor.AttributeHolder List[NXOpen.DiagrammingLibraryAuthor.AttributeHolder]@endlink):  the symbol objects .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def GetSymbolObjects(builder: LibraryAuthoringBuilder) -> List[NXOpen.DiagrammingLibraryAuthor.AttributeHolder]:
        """
         Gets the symbol objects which have user attributes of the symbol. 
         @return symbolObjects (@link NXOpen.DiagrammingLibraryAuthor.AttributeHolder List[NXOpen.DiagrammingLibraryAuthor.AttributeHolder]@endlink):  the symbol objects .
        """
        pass
    
    ##  Selects the all symbols in the folder by the 2D symbol ID 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="classId"> (str) </param>
    ## <param name="symbolId"> (str) </param>
    def SelectFolder(builder: LibraryAuthoringBuilder, classId: str, symbolId: str) -> None:
        """
         Selects the all symbols in the folder by the 2D symbol ID 
        """
        pass
    
    ##  Selects one 2D symbol or 3D symbol by the symbol ID 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="symbolId"> (str) </param>
    def SelectSymbol(builder: LibraryAuthoringBuilder, symbolId: str) -> None:
        """
         Selects one 2D symbol or 3D symbol by the symbol ID 
        """
        pass
    
import NXOpen
import NXOpen.Diagramming
##   @brief 
##     Builder used to model a piece of Off Sheet Connector.  
## 
##  
##      <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateOffSheetConnectorBuilder  NXOpen::PID::PidManager::CreateOffSheetConnectorBuilder @endlink  <br> 
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
##   <br>  Created in NX11.0.1  <br> 

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
    ## </description> </item></list>
    class StyleOption(Enum):
        """
        Members Include: <SmallFilledArrowOut> <SmallFilledArrowIn> <Box> <ChevronOut> <ChevronIn>
        """
        SmallFilledArrowOut: int
        SmallFilledArrowIn: int
        Box: int
        ChevronOut: int
        ChevronIn: int
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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def Horizontal(self) -> bool:
        """
        Getter for property: (bool) Horizontal
          the option to flip the symbol horizontally.  
             
         
        """
        pass
    
    ## Getter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet
    ##   the owning sheet of this sheet element.  
    ##    Its setting method works only in creation mode.   
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return Sheet
    @property
    def OwningSheet(self) -> Sheet:
        """
        Getter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet
          the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    
    ## Setter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet

    ##   the owning sheet of this sheet element.  
    ##    Its setting method works only in creation mode.   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @OwningSheet.setter
    def OwningSheet(self, owningSheet: Sheet):
        """
        Setter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet
          the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    
    ## Getter for property: (@link RotateAngleOption NXOpen.PID.RotateAngleOption@endlink) RotateOption
    ##   the symbol rotation angle.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return RotateAngleOption
    @property
    def RotateOption(self) -> RotateAngleOption:
        """
        Getter for property: (@link RotateAngleOption NXOpen.PID.RotateAngleOption@endlink) RotateOption
          the symbol rotation angle.  
             
         
        """
        pass
    
    ## Setter for property: (@link RotateAngleOption NXOpen.PID.RotateAngleOption@endlink) RotateOption

    ##   the symbol rotation angle.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @RotateOption.setter
    def RotateOption(self, rotate: RotateAngleOption):
        """
        Setter for property: (@link RotateAngleOption NXOpen.PID.RotateAngleOption@endlink) RotateOption
          the symbol rotation angle.  
             
         
        """
        pass
    
    ## Getter for property: (@link OffSheetConnectorBuilder.StyleOption NXOpen.PID.OffSheetConnectorBuilder.StyleOption@endlink) Style
    ##   the style of OSC   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return OffSheetConnectorBuilder.StyleOption
    @property
    def Style(self) -> OffSheetConnectorBuilder.StyleOption:
        """
        Getter for property: (@link OffSheetConnectorBuilder.StyleOption NXOpen.PID.OffSheetConnectorBuilder.StyleOption@endlink) Style
          the style of OSC   
            
         
        """
        pass
    
    ## Setter for property: (@link OffSheetConnectorBuilder.StyleOption NXOpen.PID.OffSheetConnectorBuilder.StyleOption@endlink) Style

    ##   the style of OSC   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @Style.setter
    def Style(self, style: OffSheetConnectorBuilder.StyleOption):
        """
        Setter for property: (@link OffSheetConnectorBuilder.StyleOption NXOpen.PID.OffSheetConnectorBuilder.StyleOption@endlink) Style
          the style of OSC   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyleBuilder
    ##   the text style of the OSC.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def FlipHorizontally(builder: OffSheetConnectorBuilder) -> None:
        """
         To flip a off sheet connector horizonally
        """
        pass
    
    ##  To flip a off sheet connector vertically
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def FlipVertically(builder: OffSheetConnectorBuilder) -> None:
        """
         To flip a off sheet connector vertically
        """
        pass
    
    ##  To get the connection connecting to the OSC sheet element.
    ##  @return A tuple consisting of (type, connection, connectionId). 
    ##  - type is: @link ConnectionEndType NXOpen.PID.ConnectionEndType@endlink.
    ##  - connection is: @link Pipe NXOpen.PID.Pipe@endlink.
    ##  - connectionId is: str.

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def GetConnection(builder: OffSheetConnectorBuilder) -> Tuple[ConnectionEndType, Pipe, str]:
        """
         To get the connection connecting to the OSC sheet element.
         @return A tuple consisting of (type, connection, connectionId). 
         - type is: @link ConnectionEndType NXOpen.PID.ConnectionEndType@endlink.
         - connection is: @link Pipe NXOpen.PID.Pipe@endlink.
         - connectionId is: str.

        """
        pass
    
    ##  Gets the symbol location. 
    ##  @return location (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the symbol location. .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def GetLocation(builder: OffSheetConnectorBuilder) -> NXOpen.Point2d:
        """
         Gets the symbol location. 
         @return location (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the symbol location. .
        """
        pass
    
    ##  Get the node object of the off sheet connector builder. 
    ##  @return node (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def GetNode(builder: OffSheetConnectorBuilder) -> NXOpen.Diagramming.Node:
        """
         Get the node object of the off sheet connector builder. 
         @return node (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink): .
        """
        pass
    
    ##  Links to the destination OSC. If the input OffSheetConnector is NULL, it means break the existing link.  
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="desObject"> (@link OffSheetConnector NXOpen.PID.OffSheetConnector@endlink) </param>
    def LinkOSC(builder: OffSheetConnectorBuilder, desObject: OffSheetConnector) -> None:
        """
         Links to the destination OSC. If the input OffSheetConnector is NULL, it means break the existing link.  
        """
        pass
    
    ##  To rotate a off sheet connector
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def Rotate(builder: OffSheetConnectorBuilder) -> None:
        """
         To rotate a off sheet connector
        """
        pass
    
    ##  To set the connection connecting to the OSC sheet element.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="type"> (@link ConnectionEndType NXOpen.PID.ConnectionEndType@endlink) </param>
    ## <param name="connection"> (@link Pipe NXOpen.PID.Pipe@endlink) </param>
    ## <param name="connectionId"> (str) </param>
    def SetConnection(builder: OffSheetConnectorBuilder, type: ConnectionEndType, connection: Pipe, connectionId: str) -> None:
        """
         To set the connection connecting to the OSC sheet element.
        """
        pass
    
    ##  Sets the symbol location. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the osc location. 
    def SetLocation(builder: OffSheetConnectorBuilder, location: NXOpen.Point2d) -> None:
        """
         Sets the symbol location. 
        """
        pass
    
import NXOpen.Diagramming
##  Represents the off sheet connector class.  <br> To create or edit an instance of this class, use @link NXOpen::PID::OffSheetConnectorBuilder  NXOpen::PID::OffSheetConnectorBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class OffSheetConnector(CrossSheetReference): 
    """ Represents the off sheet connector class. """


    ##  Get connections of this off sheet connector object.
    ##  @return connections (@link NXOpen.Diagramming.Connection List[NXOpen.Diagramming.Connection]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def GetConnections(oscObject: OffSheetConnector) -> List[NXOpen.Diagramming.Connection]:
        """
         Get connections of this off sheet connector object.
         @return connections (@link NXOpen.Diagramming.Connection List[NXOpen.Diagramming.Connection]@endlink): .
        """
        pass
    
    ##  Get referenced diagramming sheets.
    ##  @return sheets (@link Sheet List[NXOpen.PID.Sheet]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def GetReferencedSheets(oscObject: OffSheetConnector) -> List[Sheet]:
        """
         Get referenced diagramming sheets.
         @return sheets (@link Sheet List[NXOpen.PID.Sheet]@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
import NXOpen.Diagramming
import NXOpen.PLAS
##  A manager to deal with all objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class PidManager(NXOpen.Object): 
    """ A manager to deal with all objects. """


    ##  Convert an unassigned run to normal one
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## <param name="run"> (@link NXOpen.PLAS.Run NXOpen.PLAS.Run@endlink) </param>
    @staticmethod
    def ConvertUnassignedRunToNormalRun(run: NXOpen.PLAS.Run) -> None:
        """
         Convert an unassigned run to normal one
        """
        pass
    
    ##  Creates a @link NXOpen::PID::AutomaticTableBuilder NXOpen::PID::AutomaticTableBuilder@endlink . 
    ##  @return builder (@link AutomaticTableBuilder NXOpen.PID.AutomaticTableBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the part that will own the object 
    def CreateAutomaticTableBuilder(part: NXOpen.Part, table: AutomaticTable) -> AutomaticTableBuilder:
        """
         Creates a @link NXOpen::PID::AutomaticTableBuilder NXOpen::PID::AutomaticTableBuilder@endlink . 
         @return builder (@link AutomaticTableBuilder NXOpen.PID.AutomaticTableBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::BulkEditBuilder NXOpen::PID::BulkEditBuilder@endlink  
    ##  @return builder (@link BulkEditBuilder NXOpen.PID.BulkEditBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateBulkEditBuilder(part: NXOpen.Part) -> BulkEditBuilder:
        """
         Creates a @link NXOpen::PID::BulkEditBuilder NXOpen::PID::BulkEditBuilder@endlink  
         @return builder (@link BulkEditBuilder NXOpen.PID.BulkEditBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::DesignContextBuilder NXOpen::PID::DesignContextBuilder@endlink  
    ##  @return builder (@link DesignContextBuilder NXOpen.PID.DesignContextBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    def CreateDesignContextBuilder() -> DesignContextBuilder:
        """
         Creates a @link NXOpen::PID::DesignContextBuilder NXOpen::PID::DesignContextBuilder@endlink  
         @return builder (@link DesignContextBuilder NXOpen.PID.DesignContextBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::DesignValidationBuilder NXOpen::PID::DesignValidationBuilder@endlink . 
    ##  @return builder (@link DesignValidationBuilder NXOpen.PID.DesignValidationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the part that will own the object 
    def CreateDesignValidationBuilder(part: NXOpen.Part) -> DesignValidationBuilder:
        """
         Creates a @link NXOpen::PID::DesignValidationBuilder NXOpen::PID::DesignValidationBuilder@endlink . 
         @return builder (@link DesignValidationBuilder NXOpen.PID.DesignValidationBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::EquipmentBuilder NXOpen::PID::EquipmentBuilder@endlink . 
    ##  @return builder (@link EquipmentBuilder NXOpen.PID.EquipmentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the part that will own the object 
    def CreateEquipmentBuilder(part: NXOpen.Part, equipment: Equipment) -> EquipmentBuilder:
        """
         Creates a @link NXOpen::PID::EquipmentBuilder NXOpen::PID::EquipmentBuilder@endlink . 
         @return builder (@link EquipmentBuilder NXOpen.PID.EquipmentBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::FileNewApplicationBuilder NXOpen::PID::FileNewApplicationBuilder@endlink  
    ##  @return builder (@link FileNewApplicationBuilder NXOpen.PID.FileNewApplicationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    def CreateFilenewapplicationBuilder() -> FileNewApplicationBuilder:
        """
         Creates a @link NXOpen::PID::FileNewApplicationBuilder NXOpen::PID::FileNewApplicationBuilder@endlink  
         @return builder (@link FileNewApplicationBuilder NXOpen.PID.FileNewApplicationBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::FlowDirectionArrowBuilder NXOpen::PID::FlowDirectionArrowBuilder@endlink . 
    ##  @return builder (@link FlowDirectionArrowBuilder NXOpen.PID.FlowDirectionArrowBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  @link NXOpen::PID::FlowDirectionArrow NXOpen::PID::FlowDirectionArrow@endlink  to be edited, if NULL then create a new one 
    def CreateFlowDirectionArrowBuilder(part: NXOpen.Part, flowDirectionArrow: FlowDirectionArrow) -> FlowDirectionArrowBuilder:
        """
         Creates a @link NXOpen::PID::FlowDirectionArrowBuilder NXOpen::PID::FlowDirectionArrowBuilder@endlink . 
         @return builder (@link FlowDirectionArrowBuilder NXOpen.PID.FlowDirectionArrowBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::InstrumentationBuilder NXOpen::PID::InstrumentationBuilder@endlink . 
    ##  @return builder (@link InstrumentationBuilder NXOpen.PID.InstrumentationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the part that will own the object 
    def CreateInstrumentationBuilder(part: NXOpen.Part, instrumentation: NXOpen.NXObject) -> InstrumentationBuilder:
        """
         Creates a @link NXOpen::PID::InstrumentationBuilder NXOpen::PID::InstrumentationBuilder@endlink . 
         @return builder (@link InstrumentationBuilder NXOpen.PID.InstrumentationBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::LibraryAuthoringBuilder NXOpen::PID::LibraryAuthoringBuilder@endlink . 
    ##  @return builder (@link LibraryAuthoringBuilder NXOpen.PID.LibraryAuthoringBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the part that will own the object 
    def CreateLibraryAuthoringBuilder(part: NXOpen.Part) -> LibraryAuthoringBuilder:
        """
         Creates a @link NXOpen::PID::LibraryAuthoringBuilder NXOpen::PID::LibraryAuthoringBuilder@endlink . 
         @return builder (@link LibraryAuthoringBuilder NXOpen.PID.LibraryAuthoringBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::OffSheetConnectorBuilder NXOpen::PID::OffSheetConnectorBuilder@endlink . 
    ##  @return builder (@link OffSheetConnectorBuilder NXOpen.PID.OffSheetConnectorBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the part that will own the object 
    def CreateOffSheetConnectorBuilder(part: NXOpen.Part, oscObject: OffSheetConnector) -> OffSheetConnectorBuilder:
        """
         Creates a @link NXOpen::PID::OffSheetConnectorBuilder NXOpen::PID::OffSheetConnectorBuilder@endlink . 
         @return builder (@link OffSheetConnectorBuilder NXOpen.PID.OffSheetConnectorBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::PipeBuilder NXOpen::PID::PipeBuilder@endlink . 
    ##  @return builder (@link PipeBuilder NXOpen.PID.PipeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the part that will own the object 
    def CreatePipeBuilder(part: NXOpen.Part, pipe: Pipe) -> PipeBuilder:
        """
         Creates a @link NXOpen::PID::PipeBuilder NXOpen::PID::PipeBuilder@endlink . 
         @return builder (@link PipeBuilder NXOpen.PID.PipeBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::PortEquipmentBuilder NXOpen::PID::PortEquipmentBuilder@endlink . 
    ##  @return builder (@link PortEquipmentBuilder NXOpen.PID.PortEquipmentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the part that will own the object 
    def CreatePortEquipmentBuilder(part: NXOpen.Part, portEquipment: PortEquipment) -> PortEquipmentBuilder:
        """
         Creates a @link NXOpen::PID::PortEquipmentBuilder NXOpen::PID::PortEquipmentBuilder@endlink . 
         @return builder (@link PortEquipmentBuilder NXOpen.PID.PortEquipmentBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::PreferencesBuilder NXOpen::PID::PreferencesBuilder@endlink . 
    ##  @return builder (@link PreferencesBuilder NXOpen.PID.PreferencesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the part that will own the object 
    def CreatePreferencesBuilder(part: NXOpen.Part, sheet: Sheet) -> PreferencesBuilder:
        """
         Creates a @link NXOpen::PID::PreferencesBuilder NXOpen::PID::PreferencesBuilder@endlink . 
         @return builder (@link PreferencesBuilder NXOpen.PID.PreferencesBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::PID::SheetTemplateBuilder NXOpen::PID::SheetTemplateBuilder@endlink  
    ##  @return builder (@link SheetTemplateBuilder NXOpen.PID.SheetTemplateBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the part that will own the object 
    def CreateSheetTemplateBuilder(part: NXOpen.Part, sheet: NXOpen.Diagramming.Sheet) -> SheetTemplateBuilder:
        """
         Creates a @link NXOpen::PID::SheetTemplateBuilder NXOpen::PID::SheetTemplateBuilder@endlink  
         @return builder (@link SheetTemplateBuilder NXOpen.PID.SheetTemplateBuilder@endlink): .
        """
        pass
    
    ##  Delete Sheet Elements. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  Sheet Elements to be checked
    @staticmethod
    def DeleteSheetElements(sheetElementsDel: List[NXOpen.Diagramming.SheetElement]) -> None:
        """
         Delete Sheet Elements. 
        """
        pass
    
    ##  Enter Library Authoring Tool. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def EnterLibraryAuthoring() -> None:
        """
         Enter Library Authoring Tool. 
        """
        pass
    
    ##  Exit Library Authoring Tool. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def ExitLibraryAuthoring() -> None:
        """
         Exit Library Authoring Tool. 
        """
        pass
    
    ##  Exports @link NXOpen::PDM::ElementGroup NXOpen::PDM::ElementGroup@endlink  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  The runs to be exported 
    def ExportRunManaged(runTags: List[NXOpen.NXObject], destination: str) -> None:
        """
         Exports @link NXOpen::PDM::ElementGroup NXOpen::PDM::ElementGroup@endlink  
        """
        pass
    
    ##  Exports @link NXOpen::PDM::ElementGroup NXOpen::PDM::ElementGroup@endlink  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  The runs to be exported 
    def ExportRunManagedWithSpecificName(runTags: List[NXOpen.NXObject], fileNames: List[str], destination: str) -> None:
        """
         Exports @link NXOpen::PDM::ElementGroup NXOpen::PDM::ElementGroup@endlink  
        """
        pass
    
    ##  Exports @link NXOpen::PDM::ElementGroup NXOpen::PDM::ElementGroup@endlink  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  The runs to be exported 
    def ExportRunNative(runTags: List[NXOpen.NXObject], destination: str) -> None:
        """
         Exports @link NXOpen::PDM::ElementGroup NXOpen::PDM::ElementGroup@endlink  
        """
        pass
    
    ##  Exports @link NXOpen::PDM::ElementGroup NXOpen::PDM::ElementGroup@endlink  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  The runs to be exported 
    def ExportRunNativeWithSpecificName(runTags: List[NXOpen.NXObject], fileNames: List[str], destination: str) -> None:
        """
         Exports @link NXOpen::PDM::ElementGroup NXOpen::PDM::ElementGroup@endlink  
        """
        pass
    
    ##  Gets the @link NXOpen::PLAS::Run NXOpen::PLAS::Run@endlink  objects in the @link NXOpen::Assemblies::Partition NXOpen::Assemblies::Partition@endlink  
    ##  @return runs (@link NXOpen.PLAS.Run List[NXOpen.PLAS.Run]@endlink):  the run objects .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="system"> (@link NXOpen.Assemblies.Partition NXOpen.Assemblies.Partition@endlink) </param>
    @staticmethod
    def GetRunsInSystem(system: NXOpen.Assemblies.Partition) -> List[NXOpen.PLAS.Run]:
        """
         Gets the @link NXOpen::PLAS::Run NXOpen::PLAS::Run@endlink  objects in the @link NXOpen::Assemblies::Partition NXOpen::Assemblies::Partition@endlink  
         @return runs (@link NXOpen.PLAS.Run List[NXOpen.PLAS.Run]@endlink):  the run objects .
        """
        pass
    
    ##  Gets the @link NXOpen::PID::Sheet NXOpen::PID::Sheet@endlink  from part. 
    ##  @return sheet (@link Sheet NXOpen.PID.Sheet@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ##  the sheet part 
    @staticmethod
    def GetSheet(part: NXOpen.Part) -> Sheet:
        """
         Gets the @link NXOpen::PID::Sheet NXOpen::PID::Sheet@endlink  from part. 
         @return sheet (@link Sheet NXOpen.PID.Sheet@endlink): .
        """
        pass
    
    ##  Gets the @link NXOpen::PID::Sheet NXOpen::PID::Sheet@endlink  objects in the @link NXOpen::Assemblies::Partition NXOpen::Assemblies::Partition@endlink  
    ##  @return sheets (@link Sheet List[NXOpen.PID.Sheet]@endlink):  the sheet objects .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="system"> (@link NXOpen.Assemblies.Partition NXOpen.Assemblies.Partition@endlink) </param>
    @staticmethod
    def GetSheetsInSystem(system: NXOpen.Assemblies.Partition) -> List[Sheet]:
        """
         Gets the @link NXOpen::PID::Sheet NXOpen::PID::Sheet@endlink  objects in the @link NXOpen::Assemblies::Partition NXOpen::Assemblies::Partition@endlink  
         @return sheets (@link Sheet List[NXOpen.PID.Sheet]@endlink):  the sheet objects .
        """
        pass
    
    ##  Loads a @link NXOpen::Assemblies::Partition NXOpen::Assemblies::Partition@endlink  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## <param name="system"> (@link NXOpen.Assemblies.Partition NXOpen.Assemblies.Partition@endlink) </param>
    @staticmethod
    def LoadSystem(system: NXOpen.Assemblies.Partition) -> None:
        """
         Loads a @link NXOpen::Assemblies::Partition NXOpen::Assemblies::Partition@endlink  
        """
        pass
    
    ##  Opens a @link NXOpen::PID::Sheet NXOpen::PID::Sheet@endlink  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## <param name="sheet"> (@link Sheet NXOpen.PID.Sheet@endlink) </param>
    @staticmethod
    def OpenSheet(sheet: Sheet) -> None:
        """
         Opens a @link NXOpen::PID::Sheet NXOpen::PID::Sheet@endlink  
        """
        pass
    
    ##  Opens a @link NXOpen::PID::Sheet NXOpen::PID::Sheet@endlink  without displaying the sheet. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## <param name="sheet"> (@link Sheet NXOpen.PID.Sheet@endlink) </param>
    @staticmethod
    def OpenSheetQuietly(sheet: Sheet) -> None:
        """
         Opens a @link NXOpen::PID::Sheet NXOpen::PID::Sheet@endlink  without displaying the sheet. 
        """
        pass
    
    ##  Moves branch from one run to another. the original branch will be destroyed 
    ##  @return newbranch (@link OrderedElementGroup NXOpen.PDM.OrderedElementGroup@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## <param name="sourceRun"> (@link NXOpen.PLAS.Run NXOpen.PLAS.Run@endlink) </param>
    ## <param name="destinationRun"> (@link NXOpen.PLAS.Run NXOpen.PLAS.Run@endlink) </param>
    ## <param name="oldbranch"> (@link OrderedElementGroup NXOpen.PDM.OrderedElementGroup@endlink) </param>
    def ReparentBranch(sourceRun: NXOpen.PLAS.Run, destinationRun: NXOpen.PLAS.Run, oldbranch: OrderedElementGroup) -> OrderedElementGroup:
        """
         Moves branch from one run to another. the original branch will be destroyed 
         @return newbranch (@link OrderedElementGroup NXOpen.PDM.OrderedElementGroup@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.Diagramming
import NXOpen.PLAS
##   @brief  Represents a PipeBuilder.  
## 
##    <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreatePipeBuilder  NXOpen::PID::PidManager::CreatePipeBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class PipeBuilder(NXOpen.Builder): 
    """ <summary> Represents a PipeBuilder. </summary> """


    ## Getter for property: (@link PipeDisciplineType NXOpen.PID.PipeDisciplineType@endlink) Discipline
    ##   the pipe discipline type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PipeDisciplineType
    @property
    def Discipline(self) -> PipeDisciplineType:
        """
        Getter for property: (@link PipeDisciplineType NXOpen.PID.PipeDisciplineType@endlink) Discipline
          the pipe discipline type   
            
         
        """
        pass
    
    ## Setter for property: (@link PipeDisciplineType NXOpen.PID.PipeDisciplineType@endlink) Discipline

    ##   the pipe discipline type   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Discipline.setter
    def Discipline(self, disciplineType: PipeDisciplineType):
        """
        Setter for property: (@link PipeDisciplineType NXOpen.PID.PipeDisciplineType@endlink) Discipline
          the pipe discipline type   
            
         
        """
        pass
    
    ## Getter for property: (str) ElementId
    ##   the current element ID of this pipe.  
    ##    It works only in edit mode, it's optional and the first element ID stored in the pipe will be used as default.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def ElementId(self) -> str:
        """
        Getter for property: (str) ElementId
          the current element ID of this pipe.  
           It works only in edit mode, it's optional and the first element ID stored in the pipe will be used as default.  
         
        """
        pass
    
    ## Setter for property: (str) ElementId

    ##   the current element ID of this pipe.  
    ##    It works only in edit mode, it's optional and the first element ID stored in the pipe will be used as default.  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ElementId.setter
    def ElementId(self, elementId: str):
        """
        Setter for property: (str) ElementId
          the current element ID of this pipe.  
           It works only in edit mode, it's optional and the first element ID stored in the pipe will be used as default.  
         
        """
        pass
    
    ## Getter for property: (str) Id
    ##   the id of the pipe.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
          the id of the pipe.  
             
         
        """
        pass
    
    ## Getter for property: (str) LineTypePathId
    ##   the line type path ID of the Pipe.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def LineTypePathId(self) -> str:
        """
        Getter for property: (str) LineTypePathId
          the line type path ID of the Pipe.  
             
         
        """
        pass
    
    ## Setter for property: (str) LineTypePathId

    ##   the line type path ID of the Pipe.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LineTypePathId.setter
    def LineTypePathId(self, lineTypePathId: str):
        """
        Setter for property: (str) LineTypePathId
          the line type path ID of the Pipe.  
             
         
        """
        pass
    
    ## Getter for property: (str) OverStockPathId
    ##   the over stock path ID of the pipe.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def OverStockPathId(self) -> str:
        """
        Getter for property: (str) OverStockPathId
          the over stock path ID of the pipe.  
             
         
        """
        pass
    
    ## Setter for property: (str) OverStockPathId

    ##   the over stock path ID of the pipe.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @OverStockPathId.setter
    def OverStockPathId(self, overStockPathId: str):
        """
        Setter for property: (str) OverStockPathId
          the over stock path ID of the pipe.  
             
         
        """
        pass
    
    ## Getter for property: (bool) OverrideLineType
    ##   the option to override line type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def OverrideLineType(self) -> bool:
        """
        Getter for property: (bool) OverrideLineType
          the option to override line type   
            
         
        """
        pass
    
    ## Setter for property: (bool) OverrideLineType

    ##   the option to override line type   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @OverrideLineType.setter
    def OverrideLineType(self, overrideLineType: bool):
        """
        Setter for property: (bool) OverrideLineType
          the option to override line type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) OverstockAttributeOwner
    ##   the owner of overstock attributes group.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1988.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def OverstockAttributeOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) OverstockAttributeOwner
          the owner of overstock attributes group.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PLAS.Run NXOpen.PLAS.Run@endlink) OwningRun
    ##   the owning run of the pipe.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.PLAS.Run
    @property
    def OwningRun(self) -> NXOpen.PLAS.Run:
        """
        Getter for property: (@link NXOpen.PLAS.Run NXOpen.PLAS.Run@endlink) OwningRun
          the owning run of the pipe.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PLAS.Run NXOpen.PLAS.Run@endlink) OwningRun

    ##   the owning run of the pipe.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @OwningRun.setter
    def OwningRun(self, owningRun: NXOpen.PLAS.Run):
        """
        Setter for property: (@link NXOpen.PLAS.Run NXOpen.PLAS.Run@endlink) OwningRun
          the owning run of the pipe.  
             
         
        """
        pass
    
    ## Getter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet
    ##   the owning sheet of this pipe.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return Sheet
    @property
    def OwningSheet(self) -> Sheet:
        """
        Getter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet
          the owning sheet of this pipe.  
             
         
        """
        pass
    
    ## Setter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet

    ##   the owning sheet of this pipe.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @OwningSheet.setter
    def OwningSheet(self, owningSheet: Sheet):
        """
        Setter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet
          the owning sheet of this pipe.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) PipeAttributeOwner
    ##   the owner of pipe attributes.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def PipeAttributeOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) PipeAttributeOwner
          the owner of pipe attributes.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) PipeStockAttributeOwner
    ##   the owner of pipe stock attributes group.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1988.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def PipeStockAttributeOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) PipeStockAttributeOwner
          the owner of pipe stock attributes group.  
            
         
        """
        pass
    
    ## Getter for property: (bool) ReverseEnd
    ##   the reversed flag of this connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def ReverseEnd(self) -> bool:
        """
        Getter for property: (bool) ReverseEnd
          the reversed flag of this connection.  
             
         
        """
        pass
    
    ## Getter for property: (str) StockPathId
    ##   the stock path ID of the pipe.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def StockPathId(self) -> str:
        """
        Getter for property: (str) StockPathId
          the stock path ID of the pipe.  
             
         
        """
        pass
    
    ## Setter for property: (str) StockPathId

    ##   the stock path ID of the pipe.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @StockPathId.setter
    def StockPathId(self, stockPathId: str):
        """
        Setter for property: (str) StockPathId
          the stock path ID of the pipe.  
             
         
        """
        pass
    
    ##  Get bending points for polyline to render the connection. 
    ##  @return points (@link NXOpen.Point2d List[NXOpen.Point2d]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBendPoints(builder: PipeBuilder) -> List[NXOpen.Point2d]:
        """
         Get bending points for polyline to render the connection. 
         @return points (@link NXOpen.Point2d List[NXOpen.Point2d]@endlink): .
        """
        pass
    
    ##  Get the connection object of the connection builder. 
    ##  @return connection (@link NXOpen.Diagramming.Connection NXOpen.Diagramming.Connection@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetConnection(builder: PipeBuilder) -> NXOpen.Diagramming.Connection:
        """
         Get the connection object of the connection builder. 
         @return connection (@link NXOpen.Diagramming.Connection NXOpen.Diagramming.Connection@endlink): .
        """
        pass
    
    ##  Gets the end port of this pipe.
    ##  @return A tuple consisting of (equipment, nodeSidId, portId). 
    ##  - equipment is: @link Equipment NXOpen.PID.Equipment@endlink.
    ##  - nodeSidId is: str.
    ##  - portId is: str.

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEnd(builder: PipeBuilder) -> Tuple[Equipment, str, str]:
        """
         Gets the end port of this pipe.
         @return A tuple consisting of (equipment, nodeSidId, portId). 
         - equipment is: @link Equipment NXOpen.PID.Equipment@endlink.
         - nodeSidId is: str.
         - portId is: str.

        """
        pass
    
    ##  Get the end location of this connection.
    ##             This end location is applicable only when the @link Diagramming::ConnectionBuilder::End Diagramming::ConnectionBuilder::End@endlink  port is NULL. 
    ##  @return endLocation (@link NXOpen.Point2d NXOpen.Point2d@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEndLocation(builder: PipeBuilder) -> NXOpen.Point2d:
        """
         Get the end location of this connection.
                    This end location is applicable only when the @link Diagramming::ConnectionBuilder::End Diagramming::ConnectionBuilder::End@endlink  port is NULL. 
         @return endLocation (@link NXOpen.Point2d NXOpen.Point2d@endlink): .
        """
        pass
    
    ##  Gets the end Tee. 
    ##  @return A tuple consisting of (tee, nodeSidId). 
    ##  - tee is: @link Equipment NXOpen.PID.Equipment@endlink.
    ##  - nodeSidId is: str.

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEndTee(builder: PipeBuilder) -> Tuple[Equipment, str]:
        """
         Gets the end Tee. 
         @return A tuple consisting of (tee, nodeSidId). 
         - tee is: @link Equipment NXOpen.PID.Equipment@endlink.
         - nodeSidId is: str.

        """
        pass
    
    ##  Get the connection location for tee object at the end of the connection. 
    ##  @return A tuple consisting of (pipe, connectionId, segementId, percent). 
    ##  - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
    ##  - connectionId is: str.
    ##  - segementId is: int.
    ##  - percent is: float.

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEndTeeLocation(builder: PipeBuilder) -> Tuple[Pipe, str, int, float]:
        """
         Get the connection location for tee object at the end of the connection. 
         @return A tuple consisting of (pipe, connectionId, segementId, percent). 
         - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
         - connectionId is: str.
         - segementId is: int.
         - percent is: float.

        """
        pass
    
    ##  Gets new connection after inserting the end Tee. 
    ##  @return A tuple consisting of (pipe, connectionId). 
    ##  - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
    ##  - connectionId is: str.

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNewEndTeeConnection(builder: PipeBuilder) -> Tuple[Pipe, str]:
        """
         Gets new connection after inserting the end Tee. 
         @return A tuple consisting of (pipe, connectionId). 
         - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
         - connectionId is: str.

        """
        pass
    
    ##  Gets new connection after inserting the start Tee. 
    ##  @return A tuple consisting of (pipe, connectionId). 
    ##  - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
    ##  - connectionId is: str.

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNewStartTeeConnection(builder: PipeBuilder) -> Tuple[Pipe, str]:
        """
         Gets new connection after inserting the start Tee. 
         @return A tuple consisting of (pipe, connectionId). 
         - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
         - connectionId is: str.

        """
        pass
    
    ##  Gets the start port of this connection. 
    ##  @return A tuple consisting of (equipment, nodeSidId, portId). 
    ##  - equipment is: @link Equipment NXOpen.PID.Equipment@endlink.
    ##  - nodeSidId is: str.
    ##  - portId is: str.

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStart(builder: PipeBuilder) -> Tuple[Equipment, str, str]:
        """
         Gets the start port of this connection. 
         @return A tuple consisting of (equipment, nodeSidId, portId). 
         - equipment is: @link Equipment NXOpen.PID.Equipment@endlink.
         - nodeSidId is: str.
         - portId is: str.

        """
        pass
    
    ##  Get the start location of this connection.
    ##             This start location is applicable only when the @link Diagramming::ConnectionBuilder::Start Diagramming::ConnectionBuilder::Start@endlink  is NULL.
    ##  @return startLocation (@link NXOpen.Point2d NXOpen.Point2d@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStartLocation(builder: PipeBuilder) -> NXOpen.Point2d:
        """
         Get the start location of this connection.
                    This start location is applicable only when the @link Diagramming::ConnectionBuilder::Start Diagramming::ConnectionBuilder::Start@endlink  is NULL.
         @return startLocation (@link NXOpen.Point2d NXOpen.Point2d@endlink): .
        """
        pass
    
    ##  Gets the start Tee. 
    ##  @return A tuple consisting of (tee, nodeSidId). 
    ##  - tee is: @link Equipment NXOpen.PID.Equipment@endlink.
    ##  - nodeSidId is: str.

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStartTee(builder: PipeBuilder) -> Tuple[Equipment, str]:
        """
         Gets the start Tee. 
         @return A tuple consisting of (tee, nodeSidId). 
         - tee is: @link Equipment NXOpen.PID.Equipment@endlink.
         - nodeSidId is: str.

        """
        pass
    
    ##  Get the connection location for tee object at the start of the connection. 
    ##  @return A tuple consisting of (pipe, connectionId, segementId, percent). 
    ##  - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
    ##  - connectionId is: str.
    ##  - segementId is: int.
    ##  - percent is: float.

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStartTeeLocation(builder: PipeBuilder) -> Tuple[Pipe, str, int, float]:
        """
         Get the connection location for tee object at the start of the connection. 
         @return A tuple consisting of (pipe, connectionId, segementId, percent). 
         - pipe is: @link Pipe NXOpen.PID.Pipe@endlink.
         - connectionId is: str.
         - segementId is: int.
         - percent is: float.

        """
        pass
    
    ##  Set bending points for polyline to render the connection. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="points"> (@link NXOpen.Point2d List[NXOpen.Point2d]@endlink) </param>
    def SetBendPoints(builder: PipeBuilder, points: List[NXOpen.Point2d]) -> None:
        """
         Set bending points for polyline to render the connection. 
        """
        pass
    
    ##  Sets the end port of this pipe.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="equipment"> (@link Equipment NXOpen.PID.Equipment@endlink) </param>
    ## <param name="nodeSidId"> (str) </param>
    ## <param name="portId"> (str) </param>
    def SetEnd(builder: PipeBuilder, equipment: Equipment, nodeSidId: str, portId: str) -> None:
        """
         Sets the end port of this pipe.
        """
        pass
    
    ##  Set the end location of this connection.
    ##             This end location is applicable only when the @link Diagramming::ConnectionBuilder::End Diagramming::ConnectionBuilder::End@endlink  port is NULL. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="endLocation"> (@link NXOpen.Point2d NXOpen.Point2d@endlink) </param>
    def SetEndLocation(builder: PipeBuilder, endLocation: NXOpen.Point2d) -> None:
        """
         Set the end location of this connection.
                    This end location is applicable only when the @link Diagramming::ConnectionBuilder::End Diagramming::ConnectionBuilder::End@endlink  port is NULL. 
        """
        pass
    
    ##  Set the connection location for tee object at the end of the connection. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="pipe"> (@link Pipe NXOpen.PID.Pipe@endlink) </param>
    ## <param name="connectionId"> (str) </param>
    ## <param name="segementId"> (int) </param>
    ## <param name="percent"> (float) </param>
    def SetEndTeeLocation(builder: PipeBuilder, pipe: Pipe, connectionId: str, segementId: int, percent: float) -> None:
        """
         Set the connection location for tee object at the end of the connection. 
        """
        pass
    
    ##  Sets the start port of this connection. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="equipment"> (@link Equipment NXOpen.PID.Equipment@endlink) </param>
    ## <param name="nodeSidId"> (str) </param>
    ## <param name="portId"> (str) </param>
    def SetStart(builder: PipeBuilder, equipment: Equipment, nodeSidId: str, portId: str) -> None:
        """
         Sets the start port of this connection. 
        """
        pass
    
    ##  Set the start location of this connection.
    ##             This start location is applicable only when the @link Diagramming::ConnectionBuilder::Start Diagramming::ConnectionBuilder::Start@endlink  is NULL.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="startLocation"> (@link NXOpen.Point2d NXOpen.Point2d@endlink) </param>
    def SetStartLocation(builder: PipeBuilder, startLocation: NXOpen.Point2d) -> None:
        """
         Set the start location of this connection.
                    This start location is applicable only when the @link Diagramming::ConnectionBuilder::Start Diagramming::ConnectionBuilder::Start@endlink  is NULL.
        """
        pass
    
    ##  Set the connection location for tee object at the start of the connection. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="pipe"> (@link Pipe NXOpen.PID.Pipe@endlink) </param>
    ## <param name="connectionId"> (str) </param>
    ## <param name="segementId"> (int) </param>
    ## <param name="percent"> (float) </param>
    def SetStartTeeLocation(builder: PipeBuilder, pipe: Pipe, connectionId: str, segementId: int, percent: float) -> None:
        """
         Set the connection location for tee object at the start of the connection. 
        """
        pass
    
## Represents the pipe discipline type. 
##  piping discipline. 
class PipeDisciplineType(Enum):
    """
    Members Include: <Piping> <Instrumentation> <Hvac>
    """
    Piping: int
    Instrumentation: int
    Hvac: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> PipeDisciplineType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the Pipe class.  <br> To create or edit an instance of this class, use @link NXOpen::PID::PipeBuilder  NXOpen::PID::PipeBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Pipe(ConnectionElementRevision): 
    """ Represents the Pipe class. """
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
import NXOpen.Diagramming
##   @brief 
##     Builder used to model a piece of PortEquipment.  
## 
##  
##      <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreatePortEquipmentBuilder  NXOpen::PID::PidManager::CreatePortEquipmentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## SymbolSourceType </term> <description> 
##  
## ReuseLibrary </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.1  <br> 

class PortEquipmentBuilder(NXOpen.Builder): 
    """ <summary>
    Builder used to model a piece of PortEquipment. </summary>
    """


    ## Getter for property: (@link NXOpen.Diagramming.Port NXOpen.Diagramming.Port@endlink) ExistingSymbol
    ##   the symbol from foundation window.  
    ##    It is only applicable when @link PID::PortEquipmentBuilder::SymbolSourceType PID::PortEquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionExistingSymbol PID::SymbolSourceOptionExistingSymbol@endlink .  
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Diagramming.Port
    @property
    def ExistingSymbol(self) -> NXOpen.Diagramming.Port:
        """
        Getter for property: (@link NXOpen.Diagramming.Port NXOpen.Diagramming.Port@endlink) ExistingSymbol
          the symbol from foundation window.  
           It is only applicable when @link PID::PortEquipmentBuilder::SymbolSourceType PID::PortEquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionExistingSymbol PID::SymbolSourceOptionExistingSymbol@endlink .  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.Port NXOpen.Diagramming.Port@endlink) ExistingSymbol

    ##   the symbol from foundation window.  
    ##    It is only applicable when @link PID::PortEquipmentBuilder::SymbolSourceType PID::PortEquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionExistingSymbol PID::SymbolSourceOptionExistingSymbol@endlink .  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ExistingSymbol.setter
    def ExistingSymbol(self, existingSymbol: NXOpen.Diagramming.Port):
        """
        Setter for property: (@link NXOpen.Diagramming.Port NXOpen.Diagramming.Port@endlink) ExistingSymbol
          the symbol from foundation window.  
           It is only applicable when @link PID::PortEquipmentBuilder::SymbolSourceType PID::PortEquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionExistingSymbol PID::SymbolSourceOptionExistingSymbol@endlink .  
         
        """
        pass
    
    ## Getter for property: (str) Label
    ##   the tag of this port equipment.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
          the tag of this port equipment.  
             
         
        """
        pass
    
    ## Getter for property: (bool) LockAspectRatio
    ##   the option to lock the aspect ratio.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LockAspectRatio.setter
    def LockAspectRatio(self, lockAspectRatio: bool):
        """
        Setter for property: (bool) LockAspectRatio
          the option to lock the aspect ratio.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) NeedAttrOwner
    ##   the owner of need attributes group.  
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.NXObject
    @property
    def NeedAttrOwner(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) NeedAttrOwner
          the owner of need attributes group.  
            
         
        """
        pass
    
    ## Getter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet
    ##   the owning sheet of this sheet element.  
    ##    Its setting method works only in creation mode.   
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return Sheet
    @property
    def OwningSheet(self) -> Sheet:
        """
        Getter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet
          the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    
    ## Setter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet

    ##   the owning sheet of this sheet element.  
    ##    Its setting method works only in creation mode.   
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @OwningSheet.setter
    def OwningSheet(self, owningSheet: Sheet):
        """
        Setter for property: (@link Sheet NXOpen.PID.Sheet@endlink) OwningSheet
          the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    
    ## Getter for property: (str) PortId
    ##   the current port ID of this port equipment.  
    ##    It works only in edit mode, it's optional and the first port ID stored in the port equipment will be used as default.  
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def PortId(self) -> str:
        """
        Getter for property: (str) PortId
          the current port ID of this port equipment.  
           It works only in edit mode, it's optional and the first port ID stored in the port equipment will be used as default.  
         
        """
        pass
    
    ## Setter for property: (str) PortId

    ##   the current port ID of this port equipment.  
    ##    It works only in edit mode, it's optional and the first port ID stored in the port equipment will be used as default.  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @PortId.setter
    def PortId(self, portId: str):
        """
        Setter for property: (str) PortId
          the current port ID of this port equipment.  
           It works only in edit mode, it's optional and the first port ID stored in the port equipment will be used as default.  
         
        """
        pass
    
    ## Getter for property: (float) RelativePercentX
    ##   the X percentage of location relative to the node.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def RelativePercentX(self) -> float:
        """
        Getter for property: (float) RelativePercentX
          the X percentage of location relative to the node.  
             
         
        """
        pass
    
    ## Setter for property: (float) RelativePercentX

    ##   the X percentage of location relative to the node.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @RelativePercentX.setter
    def RelativePercentX(self, percentX: float):
        """
        Setter for property: (float) RelativePercentX
          the X percentage of location relative to the node.  
             
         
        """
        pass
    
    ## Getter for property: (float) RelativePercentY
    ##   the Y percentage of location relative to the node.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def RelativePercentY(self) -> float:
        """
        Getter for property: (float) RelativePercentY
          the Y percentage of location relative to the node.  
             
         
        """
        pass
    
    ## Setter for property: (float) RelativePercentY

    ##   the Y percentage of location relative to the node.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @RelativePercentY.setter
    def RelativePercentY(self, percentY: float):
        """
        Setter for property: (float) RelativePercentY
          the Y percentage of location relative to the node.  
             
         
        """
        pass
    
    ## Getter for property: (float) RelativeValueX
    ##   the X offset value of location relative to the node.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def RelativeValueX(self) -> float:
        """
        Getter for property: (float) RelativeValueX
          the X offset value of location relative to the node.  
             
         
        """
        pass
    
    ## Setter for property: (float) RelativeValueX

    ##   the X offset value of location relative to the node.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @RelativeValueX.setter
    def RelativeValueX(self, valueX: float):
        """
        Setter for property: (float) RelativeValueX
          the X offset value of location relative to the node.  
             
         
        """
        pass
    
    ## Getter for property: (float) RelativeValueY
    ##   the Y offset value of location relative to the node.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def RelativeValueY(self) -> float:
        """
        Getter for property: (float) RelativeValueY
          the Y offset value of location relative to the node.  
             
         
        """
        pass
    
    ## Setter for property: (float) RelativeValueY

    ##   the Y offset value of location relative to the node.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @RelativeValueY.setter
    def RelativeValueY(self, valueY: float):
        """
        Setter for property: (float) RelativeValueY
          the Y offset value of location relative to the node.  
             
         
        """
        pass
    
    ## Getter for property: (float) Scale
    ##   the scale value.  
    ##    It is only applicable when @link PID::PortEquipmentBuilder::LockAspectRatio PID::PortEquipmentBuilder::LockAspectRatio@endlink  is true.  
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
          the scale value.  
           It is only applicable when @link PID::PortEquipmentBuilder::LockAspectRatio PID::PortEquipmentBuilder::LockAspectRatio@endlink  is true.  
         
        """
        pass
    
    ## Setter for property: (float) Scale

    ##   the scale value.  
    ##    It is only applicable when @link PID::PortEquipmentBuilder::LockAspectRatio PID::PortEquipmentBuilder::LockAspectRatio@endlink  is true.  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
          the scale value.  
           It is only applicable when @link PID::PortEquipmentBuilder::LockAspectRatio PID::PortEquipmentBuilder::LockAspectRatio@endlink  is true.  
         
        """
        pass
    
    ## Getter for property: (float) ScaleX
    ##   the x scale value.  
    ##    It is only applicable when @link PID::PortEquipmentBuilder::LockAspectRatio PID::PortEquipmentBuilder::LockAspectRatio@endlink  is false.  
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def ScaleX(self) -> float:
        """
        Getter for property: (float) ScaleX
          the x scale value.  
           It is only applicable when @link PID::PortEquipmentBuilder::LockAspectRatio PID::PortEquipmentBuilder::LockAspectRatio@endlink  is false.  
         
        """
        pass
    
    ## Setter for property: (float) ScaleX

    ##   the x scale value.  
    ##    It is only applicable when @link PID::PortEquipmentBuilder::LockAspectRatio PID::PortEquipmentBuilder::LockAspectRatio@endlink  is false.  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ScaleX.setter
    def ScaleX(self, scaleX: float):
        """
        Setter for property: (float) ScaleX
          the x scale value.  
           It is only applicable when @link PID::PortEquipmentBuilder::LockAspectRatio PID::PortEquipmentBuilder::LockAspectRatio@endlink  is false.  
         
        """
        pass
    
    ## Getter for property: (float) ScaleY
    ##   the y scale value.  
    ##    It is only applicable when @link PID::PortEquipmentBuilder::LockAspectRatio PID::PortEquipmentBuilder::LockAspectRatio@endlink  is false.  
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def ScaleY(self) -> float:
        """
        Getter for property: (float) ScaleY
          the y scale value.  
           It is only applicable when @link PID::PortEquipmentBuilder::LockAspectRatio PID::PortEquipmentBuilder::LockAspectRatio@endlink  is false.  
         
        """
        pass
    
    ## Setter for property: (float) ScaleY

    ##   the y scale value.  
    ##    It is only applicable when @link PID::PortEquipmentBuilder::LockAspectRatio PID::PortEquipmentBuilder::LockAspectRatio@endlink  is false.  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ScaleY.setter
    def ScaleY(self, scaleY: float):
        """
        Setter for property: (float) ScaleY
          the y scale value.  
           It is only applicable when @link PID::PortEquipmentBuilder::LockAspectRatio PID::PortEquipmentBuilder::LockAspectRatio@endlink  is false.  
         
        """
        pass
    
    ## Getter for property: (str) SymbolId
    ##   the symbol ID of this port equipment.  
    ##    It is only applicable when @link PID::PortEquipmentBuilder::SymbolSourceType PID::PortEquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionReuseLibrary PID::SymbolSourceOptionReuseLibrary@endlink .  
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def SymbolId(self) -> str:
        """
        Getter for property: (str) SymbolId
          the symbol ID of this port equipment.  
           It is only applicable when @link PID::PortEquipmentBuilder::SymbolSourceType PID::PortEquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionReuseLibrary PID::SymbolSourceOptionReuseLibrary@endlink .  
         
        """
        pass
    
    ## Setter for property: (str) SymbolId

    ##   the symbol ID of this port equipment.  
    ##    It is only applicable when @link PID::PortEquipmentBuilder::SymbolSourceType PID::PortEquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionReuseLibrary PID::SymbolSourceOptionReuseLibrary@endlink .  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @SymbolId.setter
    def SymbolId(self, symbolId: str):
        """
        Setter for property: (str) SymbolId
          the symbol ID of this port equipment.  
           It is only applicable when @link PID::PortEquipmentBuilder::SymbolSourceType PID::PortEquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionReuseLibrary PID::SymbolSourceOptionReuseLibrary@endlink .  
         
        """
        pass
    
    ## Getter for property: (@link SymbolSourceOption NXOpen.PID.SymbolSourceOption@endlink) SymbolSourceType
    ##   the symbol source type   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return SymbolSourceOption
    @property
    def SymbolSourceType(self) -> SymbolSourceOption:
        """
        Getter for property: (@link SymbolSourceOption NXOpen.PID.SymbolSourceOption@endlink) SymbolSourceType
          the symbol source type   
            
         
        """
        pass
    
    ## Setter for property: (@link SymbolSourceOption NXOpen.PID.SymbolSourceOption@endlink) SymbolSourceType

    ##   the symbol source type   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @SymbolSourceType.setter
    def SymbolSourceType(self, symbolSourceType: SymbolSourceOption):
        """
        Setter for property: (@link SymbolSourceOption NXOpen.PID.SymbolSourceOption@endlink) SymbolSourceType
          the symbol source type   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseExistingID
    ##   the option to place a duplicate symbol.  
    ##    It is only applicable when @link PID::PortEquipmentBuilder::SymbolSourceType PID::PortEquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionExistingSymbol PID::SymbolSourceOptionExistingSymbol@endlink .  
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def UseExistingID(self) -> bool:
        """
        Getter for property: (bool) UseExistingID
          the option to place a duplicate symbol.  
           It is only applicable when @link PID::PortEquipmentBuilder::SymbolSourceType PID::PortEquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionExistingSymbol PID::SymbolSourceOptionExistingSymbol@endlink .  
         
        """
        pass
    
    ## Setter for property: (bool) UseExistingID

    ##   the option to place a duplicate symbol.  
    ##    It is only applicable when @link PID::PortEquipmentBuilder::SymbolSourceType PID::PortEquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionExistingSymbol PID::SymbolSourceOptionExistingSymbol@endlink .  
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @UseExistingID.setter
    def UseExistingID(self, useExistingID: bool):
        """
        Setter for property: (bool) UseExistingID
          the option to place a duplicate symbol.  
           It is only applicable when @link PID::PortEquipmentBuilder::SymbolSourceType PID::PortEquipmentBuilder::SymbolSourceType@endlink  is @link PID::SymbolSourceOptionExistingSymbol PID::SymbolSourceOptionExistingSymbol@endlink .  
         
        """
        pass
    
    ##  Get the node. 
    ##  @return A tuple consisting of (equipment, nodeId). 
    ##  - equipment is: @link Equipment NXOpen.PID.Equipment@endlink.
    ##  - nodeId is: str.

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def GetNode(builder: PortEquipmentBuilder) -> Tuple[Equipment, str]:
        """
         Get the node. 
         @return A tuple consisting of (equipment, nodeId). 
         - equipment is: @link Equipment NXOpen.PID.Equipment@endlink.
         - nodeId is: str.

        """
        pass
    
    ##  Get the port object of the PortEquipment builder. 
    ##  @return port (@link NXOpen.Diagramming.Port NXOpen.Diagramming.Port@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    @staticmethod
    def GetPort(builder: PortEquipmentBuilder) -> NXOpen.Diagramming.Port:
        """
         Get the port object of the PortEquipment builder. 
         @return port (@link NXOpen.Diagramming.Port NXOpen.Diagramming.Port@endlink): .
        """
        pass
    
    ##  Sets the fulfillment data of the symbol. The input symbol should be a 3D one and in the same category with the entity of the builder
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="symbolID"> (str) </param>
    def SetFulfillment(builder: PortEquipmentBuilder, symbolID: str) -> None:
        """
         Sets the fulfillment data of the symbol. The input symbol should be a 3D one and in the same category with the entity of the builder
        """
        pass
    
    ##  Set the node. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ## <param name="equipment"> (@link Equipment NXOpen.PID.Equipment@endlink) </param>
    ## <param name="nodeId"> (str) </param>
    def SetNode(builder: PortEquipmentBuilder, equipment: Equipment, nodeId: str) -> None:
        """
         Set the node. 
        """
        pass
    
##  Represents the PortEquipment class.  <br> To create or edit an instance of this class, use @link NXOpen::PID::PortEquipmentBuilder  NXOpen::PID::PortEquipmentBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class PortEquipment(Equipment): 
    """ Represents the PortEquipment class. """
    pass


##  Represents the port class.  <br> This class is not created directly by the user.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Port(PortArtifact): 
    """ Represents the port class. """


    ## Getter for property: (str) ConnectionType
    ##   the connection type of the port.  
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def ConnectionType(self) -> str:
        """
        Getter for property: (str) ConnectionType
          the connection type of the port.  
            
         
        """
        pass
    
    ## Getter for property: (@link PortDirectionOption NXOpen.PID.PortDirectionOption@endlink) Direction
    ##   the Id of the port.  
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return PortDirectionOption
    @property
    def Direction(self) -> PortDirectionOption:
        """
        Getter for property: (@link PortDirectionOption NXOpen.PID.PortDirectionOption@endlink) Direction
          the Id of the port.  
            
         
        """
        pass
    
    ## Getter for property: (str) Discipline
    ##   the Id of the port.  
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
          the Id of the port.  
            
         
        """
        pass
    
    ## Getter for property: (str) Id
    ##   the Id of the port.  
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
          the Id of the port.  
            
         
        """
        pass
    
    ## Getter for property: (bool) Inline
    ##   the indicator of the port's inline.  
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def Inline(self) -> bool:
        """
        Getter for property: (bool) Inline
          the indicator of the port's inline.  
            
         
        """
        pass
    
    ## Getter for property: (str) Material
    ##   the material of the port.  
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def Material(self) -> str:
        """
        Getter for property: (str) Material
          the material of the port.  
            
         
        """
        pass
    
    ## Getter for property: (float) Nps
    ##   the nps of the port.  
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def Nps(self) -> float:
        """
        Getter for property: (float) Nps
          the nps of the port.  
            
         
        """
        pass
    
    ## Getter for property: (str) PortAlias
    ##   the Id of the port.  
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def PortAlias(self) -> str:
        """
        Getter for property: (str) PortAlias
          the Id of the port.  
            
         
        """
        pass
    
    ## Getter for property: (bool) Terminating
    ##   the indicator of the port's terminating.  
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def Terminating(self) -> bool:
        """
        Getter for property: (bool) Terminating
          the indicator of the port's terminating.  
            
         
        """
        pass
    
import NXOpen
import NXOpen.Diagramming
import NXOpen.Diagramming.Tables
import NXOpen.GeometricUtilities
## 
##     Represents a PreferencesAnnotationBuilder
##     
## 
##   <br>  Created in NX11.0.1  <br> 

class PreferencesAnnotationBuilder(NXOpen.TaggedObject): 
    """
    Represents a PreferencesAnnotationBuilder
    """


    ## Getter for property: (@link NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition@endlink) ConnectionLabelHorizontalOffsetPosition
    ##   the horizontal position of the connection tag.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ConnectionLabelVerticalOffsetPosition.setter
    def ConnectionLabelVerticalOffsetPosition(self, position: NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition):
        """
        Setter for property: (@link NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition@endlink) ConnectionLabelVerticalOffsetPosition
          the vertical position of the connection tag.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) TablesBorderCellSettings
    ##      the preferences tabular note border cell settings builder   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
##      <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreatePreferencesBuilder  NXOpen::PID::PidManager::CreatePreferencesBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class PreferencesBuilder(NXOpen.Builder): 
    """
    Represents a PreferencesBuilder
    """


    ## Getter for property: (@link PreferencesAnnotationBuilder NXOpen.PID.PreferencesAnnotationBuilder@endlink) Annotation
    ##      the preferences annotation builder   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return PreferencesAnnotationBuilder
    @property
    def Annotation(self) -> PreferencesAnnotationBuilder:
        """
        Getter for property: (@link PreferencesAnnotationBuilder NXOpen.PID.PreferencesAnnotationBuilder@endlink) Annotation
             the preferences annotation builder   
            
         
        """
        pass
    
    ## Getter for property: (@link PreferencesConnectionBuilder NXOpen.PID.PreferencesConnectionBuilder@endlink) Connection
    ##      the preferences connection builder   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return PreferencesConnectionBuilder
    @property
    def Connection(self) -> PreferencesConnectionBuilder:
        """
        Getter for property: (@link PreferencesConnectionBuilder NXOpen.PID.PreferencesConnectionBuilder@endlink) Connection
             the preferences connection builder   
            
         
        """
        pass
    
    ## Getter for property: (@link PreferencesGeneralBuilder NXOpen.PID.PreferencesGeneralBuilder@endlink) General
    ##      the preferences general builder   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return PreferencesGeneralBuilder
    @property
    def General(self) -> PreferencesGeneralBuilder:
        """
        Getter for property: (@link PreferencesGeneralBuilder NXOpen.PID.PreferencesGeneralBuilder@endlink) General
             the preferences general builder   
            
         
        """
        pass
    
    ## Getter for property: (@link PreferencesInstrumentationBuilder NXOpen.PID.PreferencesInstrumentationBuilder@endlink) Instrumentation
    ##  the preferences instrumentation builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PreferencesInstrumentationBuilder
    @property
    def Instrumentation(self) -> PreferencesInstrumentationBuilder:
        """
        Getter for property: (@link PreferencesInstrumentationBuilder NXOpen.PID.PreferencesInstrumentationBuilder@endlink) Instrumentation
         the preferences instrumentation builder   
            
         
        """
        pass
    
    ## Getter for property: (@link PreferencesOffSheetConnectorBuilder NXOpen.PID.PreferencesOffSheetConnectorBuilder@endlink) OffSheetConnector
    ##      the preferences offsheetconnector builder   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return PreferencesOffSheetConnectorBuilder
    @property
    def OffSheetConnector(self) -> PreferencesOffSheetConnectorBuilder:
        """
        Getter for property: (@link PreferencesOffSheetConnectorBuilder NXOpen.PID.PreferencesOffSheetConnectorBuilder@endlink) OffSheetConnector
             the preferences offsheetconnector builder   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Diagramming
import NXOpen.GeometricUtilities
## 
##     Represents a PreferencesConnectionBuilder
##     
## 
##   <br>  Created in NX11.0.1  <br> 

class PreferencesConnectionBuilder(NXOpen.TaggedObject): 
    """
    Represents a PreferencesConnectionBuilder
    """


    ## Getter for property: (bool) AllowNonOrthogonalConnections
    ##   the allow non-orthogonal connections.  
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ArrowStyle.setter
    def ArrowStyle(self, style: NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle):
        """
        Setter for property: (@link NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle@endlink) ArrowStyle
          the arrow style.  
            
         
        """
        pass
    
    ## Getter for property: (float) JumperGap
    ##   the jumper gap.  
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @TeeSize.setter
    def TeeSize(self, size: float):
        """
        Setter for property: (float) TeeSize
          the tee size.  
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a PreferencesGeneralBuilder
##     
## 
##   <br>  Created in NX11.0.1  <br> 

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
    ##   <br>  Created in NX1847.0.0  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @HidePorts.setter
    def HidePorts(self, hidePorts: bool):
        """
        Setter for property: (bool) HidePorts
           the flag to hide the ports.  
             
         
        """
        pass
    
    ## Getter for property: (str) TagMask
    ##    the name of the file containing the tag mask configurations.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

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
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @TagMask.setter
    def TagMask(self, tagMaskFile: str):
        """
        Setter for property: (str) TagMask
           the name of the file containing the tag mask configurations.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a PreferencesInstrumentationBuilder
##     
## 
##   <br>  Created in NX1847.0.0  <br> 

class PreferencesInstrumentationBuilder(NXOpen.TaggedObject): 
    """
    Represents a PreferencesInstrumentationBuilder
    """


    ## Getter for property: (@link InstrumentationControlLoopDisplay NXOpen.PID.InstrumentationControlLoopDisplay@endlink) ControlLoopDisplay
    ##    the identification display for the control loop of the instrumentation symbols.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return InstrumentationControlLoopDisplay
    @property
    def ControlLoopDisplay(self) -> InstrumentationControlLoopDisplay:
        """
        Getter for property: (@link InstrumentationControlLoopDisplay NXOpen.PID.InstrumentationControlLoopDisplay@endlink) ControlLoopDisplay
           the identification display for the control loop of the instrumentation symbols.  
             
         
        """
        pass
    
    ## Setter for property: (@link InstrumentationControlLoopDisplay NXOpen.PID.InstrumentationControlLoopDisplay@endlink) ControlLoopDisplay

    ##    the identification display for the control loop of the instrumentation symbols.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ControlLoopDisplay.setter
    def ControlLoopDisplay(self, display: InstrumentationControlLoopDisplay):
        """
        Setter for property: (@link InstrumentationControlLoopDisplay NXOpen.PID.InstrumentationControlLoopDisplay@endlink) ControlLoopDisplay
           the identification display for the control loop of the instrumentation symbols.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Diagramming
import NXOpen.GeometricUtilities
## 
##     Represents a PreferencesOffSheetConnectorBuilder
##     
## 
##   <br>  Created in NX11.0.1  <br> 

class PreferencesOffSheetConnectorBuilder(NXOpen.TaggedObject): 
    """
    Represents a PreferencesOffSheetConnectorBuilder
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
    ## </description> </item></list>
    class StyleOption(Enum):
        """
        Members Include: <SmallFilledArrowOut> <SmallFilledArrowIn> <Box> <ChevronOut> <ChevronIn>
        """
        SmallFilledArrowOut: int
        SmallFilledArrowIn: int
        Box: int
        ChevronOut: int
        ChevronIn: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesOffSheetConnectorBuilder.StyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link PreferencesOffSheetConnectorBuilder.StyleOption NXOpen.PID.PreferencesOffSheetConnectorBuilder.StyleOption@endlink) Style
    ##   the style of OSC   
    ##     
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return PreferencesOffSheetConnectorBuilder.StyleOption
    @property
    def Style(self) -> PreferencesOffSheetConnectorBuilder.StyleOption:
        """
        Getter for property: (@link PreferencesOffSheetConnectorBuilder.StyleOption NXOpen.PID.PreferencesOffSheetConnectorBuilder.StyleOption@endlink) Style
          the style of OSC   
            
         
        """
        pass
    
    ## Setter for property: (@link PreferencesOffSheetConnectorBuilder.StyleOption NXOpen.PID.PreferencesOffSheetConnectorBuilder.StyleOption@endlink) Style

    ##   the style of OSC   
    ##     
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @Style.setter
    def Style(self, style: PreferencesOffSheetConnectorBuilder.StyleOption):
        """
        Setter for property: (@link PreferencesOffSheetConnectorBuilder.StyleOption NXOpen.PID.PreferencesOffSheetConnectorBuilder.StyleOption@endlink) Style
          the style of OSC   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyleBuilder
    ##   the text style of the OSC.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Diagramming.TextStyleBuilder
    @property
    def TextStyleBuilder(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyleBuilder
          the text style of the OSC.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Diagramming.Tables
import NXOpen.GeometricUtilities
##   @brief  Represents a PropertyCellRangeBuilder.  
## 
##    <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class PropertyCellRangeBuilder(NXOpen.TaggedObject): 
    """ <summary> Represents a PropertyCellRangeBuilder. </summary> """


    ## Getter for property: (str) PropertyKey
    ##   the property key.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def PropertyKey(self) -> str:
        """
        Getter for property: (str) PropertyKey
          the property key.  
             
         
        """
        pass
    
    ## Setter for property: (str) PropertyKey

    ##   the property key.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PropertyKey.setter
    def PropertyKey(self, propertyKey: str):
        """
        Setter for property: (str) PropertyKey
          the property key.  
             
         
        """
        pass
    
    ## Getter for property: (@link PropertyType NXOpen.PID.PropertyType@endlink) PropertyType
    ##   the property type.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PropertyType
    @property
    def PropertyType(self) -> PropertyType:
        """
        Getter for property: (@link PropertyType NXOpen.PID.PropertyType@endlink) PropertyType
          the property type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PropertyType NXOpen.PID.PropertyType@endlink) PropertyType

    ##   the property type.  
    ##      
    ##  
    ## Setter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PropertyType.setter
    def PropertyType(self, propertyType: PropertyType):
        """
        Setter for property: (@link PropertyType NXOpen.PID.PropertyType@endlink) PropertyType
          the property type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.Tables.CellRangeBuilder NXOpen.Diagramming.Tables.CellRangeBuilder@endlink) TableCellRange
    ##   the cell range.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Diagramming.Tables.CellRangeBuilder
    @property
    def TableCellRange(self) -> NXOpen.Diagramming.Tables.CellRangeBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.Tables.CellRangeBuilder NXOpen.Diagramming.Tables.CellRangeBuilder@endlink) TableCellRange
          the cell range.  
             
         
        """
        pass
    
##  Represents the property type. 
##  Null type 
class PropertyType(Enum):
    """
    Members Include: <Null> <Index> <UserAttribute> <NeedAttribute> <FulfillmentAttribute> <PipeStockAttribute> <PidTag> <ParentRun> <Quantity> <System> <RunAttribute> <EquipmentAttribute>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> PropertyType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
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
##  Represents a @link NXOpen::PID::SheetTemplateBuilder NXOpen::PID::SheetTemplateBuilder@endlink  builder, and the builder is used to model a sheet template.  <br> To create a new instance of this class, use @link NXOpen::PID::PidManager::CreateSheetTemplateBuilder  NXOpen::PID::PidManager::CreateSheetTemplateBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class SheetTemplateBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.PID.SheetTemplateBuilder</ja_class> builder, and the builder is used to model a sheet template. """


    ## Getter for property: (@link NXOpen.Diagramming.SheetBuilder NXOpen.Diagramming.SheetBuilder@endlink) Sheet
    ##   the diagramming sheet builder.  
    ##      
    ##  
    ## Getter License requirements: nx_pid_design_author ("NX P and ID Design Author")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Diagramming.SheetBuilder
    @property
    def Sheet(self) -> NXOpen.Diagramming.SheetBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.SheetBuilder NXOpen.Diagramming.SheetBuilder@endlink) Sheet
          the diagramming sheet builder.  
             
         
        """
        pass
    
import NXOpen.PLAS
##  
##         Represents a base class that provides common methods for various model elements in a @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .
##      <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class Sheet(SheetRevision): 
    """ 
        Represents a base class that provides common methods for various model elements in a <ja_class>NXOpen.CollaborativeDesign</ja_class>.
    """


    ##  Returns the @link NXOpen::PID::FlowDirectionArrowCollection  NXOpen::PID::FlowDirectionArrowCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @link FlowDirectionArrowCollection NXOpen.PID.FlowDirectionArrowCollection@endlink
    @property
    def FlowDirectionArrows() -> FlowDirectionArrowCollection:
        """
         Returns the @link NXOpen::PID::FlowDirectionArrowCollection  NXOpen::PID::FlowDirectionArrowCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::PID::AutomaticTableCollection  NXOpen::PID::AutomaticTableCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @link AutomaticTableCollection NXOpen.PID.AutomaticTableCollection@endlink
    @property
    def AutomaticTables() -> AutomaticTableCollection:
        """
         Returns the @link NXOpen::PID::AutomaticTableCollection  NXOpen::PID::AutomaticTableCollection @endlink  belonging to this part 
        """
        pass
    
    ##  This is an internal API and can be changed at any time 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @link InstrumentationCollection NXOpen.PID.InstrumentationCollection@endlink
    @property
    def Instrumentations() -> InstrumentationCollection:
        """
         This is an internal API and can be changed at any time 
        """
        pass
    
    ##  Gets the @link NXOpen::PID::Equipment NXOpen::PID::Equipment@endlink  objects in the sheet 
    ##  @return equipment (@link Equipment List[NXOpen.PID.Equipment]@endlink):  the equipment objects .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEquipment(sheet: Sheet) -> List[Equipment]:
        """
         Gets the @link NXOpen::PID::Equipment NXOpen::PID::Equipment@endlink  objects in the sheet 
         @return equipment (@link Equipment List[NXOpen.PID.Equipment]@endlink):  the equipment objects .
        """
        pass
    
    ##  Gets the @link NXOpen::PID::Pipe NXOpen::PID::Pipe@endlink  objects in the sheet 
    ##  @return pipes (@link Pipe List[NXOpen.PID.Pipe]@endlink):  the pipe objects .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPipes(sheet: Sheet) -> List[Pipe]:
        """
         Gets the @link NXOpen::PID::Pipe NXOpen::PID::Pipe@endlink  objects in the sheet 
         @return pipes (@link Pipe List[NXOpen.PID.Pipe]@endlink):  the pipe objects .
        """
        pass
    
    ##  Gets the @link NXOpen::PLAS::Run NXOpen::PLAS::Run@endlink  objects in the sheet 
    ##  @return runs (@link NXOpen.PLAS.Run List[NXOpen.PLAS.Run]@endlink):  the run objects .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRuns(sheet: Sheet) -> List[NXOpen.PLAS.Run]:
        """
         Gets the @link NXOpen::PLAS::Run NXOpen::PLAS::Run@endlink  objects in the sheet 
         @return runs (@link NXOpen.PLAS.Run List[NXOpen.PLAS.Run]@endlink):  the run objects .
        """
        pass
    
##  Represents the symbol source options. 
##  from the reuse library. 
class SymbolSourceOption(Enum):
    """
    Members Include: <ReuseLibrary> <ExistingSymbol> <LogicalElementRevision>
    """
    ReuseLibrary: int
    ExistingSymbol: int
    LogicalElementRevision: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SymbolSourceOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## @package NXOpen.PID
## Classes, Enums and Structs under NXOpen.PID namespace

##  @link AutomaticTableBuilderObjectTypeOption NXOpen.PID.AutomaticTableBuilderObjectTypeOption @endlink is an alias for @link AutomaticTableBuilder.ObjectTypeOption NXOpen.PID.AutomaticTableBuilder.ObjectTypeOption@endlink
AutomaticTableBuilderObjectTypeOption = AutomaticTableBuilder.ObjectTypeOption


##  @link AutomaticTableBuilderScopeTypeOption NXOpen.PID.AutomaticTableBuilderScopeTypeOption @endlink is an alias for @link AutomaticTableBuilder.ScopeTypeOption NXOpen.PID.AutomaticTableBuilder.ScopeTypeOption@endlink
AutomaticTableBuilderScopeTypeOption = AutomaticTableBuilder.ScopeTypeOption


##  @link AutomaticTableBuilderStockOption NXOpen.PID.AutomaticTableBuilderStockOption @endlink is an alias for @link AutomaticTableBuilder.StockOption NXOpen.PID.AutomaticTableBuilder.StockOption@endlink
AutomaticTableBuilderStockOption = AutomaticTableBuilder.StockOption


##  @link OffSheetConnectorBuilderStyleOption NXOpen.PID.OffSheetConnectorBuilderStyleOption @endlink is an alias for @link OffSheetConnectorBuilder.StyleOption NXOpen.PID.OffSheetConnectorBuilder.StyleOption@endlink
OffSheetConnectorBuilderStyleOption = OffSheetConnectorBuilder.StyleOption


##  @link PreferencesOffSheetConnectorBuilderStyleOption NXOpen.PID.PreferencesOffSheetConnectorBuilderStyleOption @endlink is an alias for @link PreferencesOffSheetConnectorBuilder.StyleOption NXOpen.PID.PreferencesOffSheetConnectorBuilder.StyleOption@endlink
PreferencesOffSheetConnectorBuilderStyleOption = PreferencesOffSheetConnectorBuilder.StyleOption


