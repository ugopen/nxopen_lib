from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a @link NXOpen::PcbExchange::AdvancedConductivityBuilder NXOpen::PcbExchange::AdvancedConductivityBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateAdvancedConductivityBuilder  NXOpen::PcbExchange::Manager::CreateAdvancedConductivityBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class AdvancedConductivityBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.PcbExchange.AdvancedConductivityBuilder</ja_class> """


    ##  Method to get diameters 
    ##  @return diameters (List[float]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDiameters(builder: AdvancedConductivityBuilder) -> List[float]:
        """
         Method to get diameters 
         @return diameters (List[float]): .
        """
        pass
    
    ##  Method to get endLayers 
    ##  @return endLayers (List[int]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEndLayers(builder: AdvancedConductivityBuilder) -> List[int]:
        """
         Method to get endLayers 
         @return endLayers (List[int]): .
        """
        pass
    
    ##  Method to get fillMaterials 
    ##  @return fillMaterials (List[int]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFillMaterials(builder: AdvancedConductivityBuilder) -> List[int]:
        """
         Method to get fillMaterials 
         @return fillMaterials (List[int]): .
        """
        pass
    
    ##  Method to get bFilleds 
    ##  @return bFilleds (List[bool]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFilled(builder: AdvancedConductivityBuilder) -> List[bool]:
        """
         Method to get bFilleds 
         @return bFilleds (List[bool]): .
        """
        pass
    
    ##  Method to get holes counts 
    ##  @return holesCounts (List[int]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetHolesCounts(builder: AdvancedConductivityBuilder) -> List[int]:
        """
         Method to get holes counts 
         @return holesCounts (List[int]): .
        """
        pass
    
    ##  Method to get netsList 
    ##  @return nets (List[str]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNetsList(builder: AdvancedConductivityBuilder) -> List[str]:
        """
         Method to get netsList 
         @return nets (List[str]): .
        """
        pass
    
    ##  Method to get netsToFilterString 
    ##  @return nets (str): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNetsToFilterString(builder: AdvancedConductivityBuilder) -> str:
        """
         Method to get netsToFilterString 
         @return nets (str): .
        """
        pass
    
    ##  Method to get padstacks 
    ##  @return padstacks (List[str]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPadstacks(builder: AdvancedConductivityBuilder) -> List[str]:
        """
         Method to get padstacks 
         @return padstacks (List[str]): .
        """
        pass
    
    ##  Method to get platingMaterials 
    ##  @return platingMaterials (List[int]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPlatingMaterials(builder: AdvancedConductivityBuilder) -> List[int]:
        """
         Method to get platingMaterials 
         @return platingMaterials (List[int]): .
        """
        pass
    
    ##  Method to get platingThicknesses 
    ##  @return platingThicknesses (List[float]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPlatingThicknesses(builder: AdvancedConductivityBuilder) -> List[float]:
        """
         Method to get platingThicknesses 
         @return platingThicknesses (List[float]): .
        """
        pass
    
    ##  Method to get startLayers 
    ##  @return startLayers (List[int]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStartLayers(builder: AdvancedConductivityBuilder) -> List[int]:
        """
         Method to get startLayers 
         @return startLayers (List[int]): .
        """
        pass
    
    ##  Method to get tags 
    ##  @return t (List[int]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetT(builder: AdvancedConductivityBuilder) -> List[int]:
        """
         Method to get tags 
         @return t (List[int]): .
        """
        pass
    
    ##  Method to get textualFilter 
    ##  @return filter (bool): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTextualFilter(builder: AdvancedConductivityBuilder) -> bool:
        """
         Method to get textualFilter 
         @return filter (bool): .
        """
        pass
    
    ##  Method to get types 
    ##  @return types (List[int]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTypes(builder: AdvancedConductivityBuilder) -> List[int]:
        """
         Method to get types 
         @return types (List[int]): .
        """
        pass
    
    ##  Method to set diameters 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="diameters"> (List[float]) </param>
    def SetDiameters(builder: AdvancedConductivityBuilder, diameters: List[float]) -> None:
        """
         Method to set diameters 
        """
        pass
    
    ##  Method to set endLayers 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="endLayers"> (List[int]) </param>
    def SetEndLayers(builder: AdvancedConductivityBuilder, endLayers: List[int]) -> None:
        """
         Method to set endLayers 
        """
        pass
    
    ##  Method to set fillMaterials 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="fillMaterials"> (List[int]) </param>
    def SetFillMaterials(builder: AdvancedConductivityBuilder, fillMaterials: List[int]) -> None:
        """
         Method to set fillMaterials 
        """
        pass
    
    ##  Method to set fillMaterials 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="bFilleds"> (List[int]) </param>
    def SetFilled(builder: AdvancedConductivityBuilder, bFilleds: List[int]) -> None:
        """
         Method to set fillMaterials 
        """
        pass
    
    ##  Method to set holes counts 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="holesCounts"> (List[int]) </param>
    def SetHolesCounts(builder: AdvancedConductivityBuilder, holesCounts: List[int]) -> None:
        """
         Method to set holes counts 
        """
        pass
    
    ##  Method to set netsList 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="nets"> (List[str]) </param>
    def SetNetsList(builder: AdvancedConductivityBuilder, nets: List[str]) -> None:
        """
         Method to set netsList 
        """
        pass
    
    ##  Method to set netsToFilterString 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="nets"> (str) </param>
    def SetNetsToFilterString(builder: AdvancedConductivityBuilder, nets: str) -> None:
        """
         Method to set netsToFilterString 
        """
        pass
    
    ##  Method to set padstacks 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="nets"> (List[str]) </param>
    def SetPadstacks(builder: AdvancedConductivityBuilder, nets: List[str]) -> None:
        """
         Method to set padstacks 
        """
        pass
    
    ##  Method to set platingMaterials 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="platingMaterials"> (List[int]) </param>
    def SetPlatingMaterials(builder: AdvancedConductivityBuilder, platingMaterials: List[int]) -> None:
        """
         Method to set platingMaterials 
        """
        pass
    
    ##  Method to set platingThicknesses 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="platingThicknesses"> (List[float]) </param>
    def SetPlatingThicknesses(builder: AdvancedConductivityBuilder, platingThicknesses: List[float]) -> None:
        """
         Method to set platingThicknesses 
        """
        pass
    
    ##  Method to set startLayers 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="startLayers"> (List[int]) </param>
    def SetStartLayers(builder: AdvancedConductivityBuilder, startLayers: List[int]) -> None:
        """
         Method to set startLayers 
        """
        pass
    
    ##  Method to set tags 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="t"> (List[int]) </param>
    def SetT(builder: AdvancedConductivityBuilder, t: List[int]) -> None:
        """
         Method to set tags 
        """
        pass
    
    ##  Method to set textualFilter 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="filter"> (bool) </param>
    def SetTextualFilter(builder: AdvancedConductivityBuilder, filter: bool) -> None:
        """
         Method to set textualFilter 
        """
        pass
    
    ##  Method to set types 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="types"> (List[int]) </param>
    def SetTypes(builder: AdvancedConductivityBuilder, types: List[int]) -> None:
        """
         Method to set types 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::PcbExchange::AlternateComponentManager NXOpen::PcbExchange::AlternateComponentManager@endlink .  <br> To obtain an instance of this class, refer to @link NXOpen::PcbExchange::Manager  NXOpen::PcbExchange::Manager @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class AlternateComponentManager(NXOpen.Object): 
    """ Represents a <ja_class>NXOpen.PcbExchange.AlternateComponentManager</ja_class>. """


    ##  Replaces the component with alternate one. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition")
    ##  UGMaster dataset name or UGAltrep dataset name. 
    def Replace(component: NXOpen.NXObject, datasetName: str) -> None:
        """
         Replaces the component with alternate one. 
        """
        pass
    
import NXOpen
##  Represents a builder to create or edit area attributes.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateAreaAttributesBuilder  NXOpen::PcbExchange::Manager::CreateAreaAttributesBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class AreaAttributesBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit area attributes. """


    ##  The layer options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Current</term><description> 
    ## </description> </item><item><term> 
    ## Both</term><description> 
    ## </description> </item><item><term> 
    ## Inner</term><description> 
    ## </description> </item><item><term> 
    ## All</term><description> 
    ## </description> </item></list>
    class LayerEnum(Enum):
        """
        Members Include: <Current> <Both> <Inner> <All>
        """
        Current: int
        Both: int
        Inner: int
        All: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AreaAttributesBuilder.LayerEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The owner options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unowned</term><description> 
    ## </description> </item><item><term> 
    ## Mcad</term><description> 
    ## </description> </item><item><term> 
    ## Ecad</term><description> 
    ## </description> </item></list>
    class OwnerEnum(Enum):
        """
        Members Include: <Unowned> <Mcad> <Ecad>
        """
        Unowned: int
        Mcad: int
        Ecad: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AreaAttributesBuilder.OwnerEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The area type options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Keepout</term><description> 
    ## </description> </item><item><term> 
    ## Keepin</term><description> 
    ## </description> </item><item><term> 
    ## Other</term><description> 
    ## </description> </item><item><term> 
    ## Copper</term><description> 
    ## </description> </item></list>
    class TypeEnum(Enum):
        """
        Members Include: <Keepout> <Keepin> <Other> <Copper>
        """
        Keepout: int
        Keepin: int
        Other: int
        Copper: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AreaAttributesBuilder.TypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link AreaAttributesBuilder.TypeEnum NXOpen.PcbExchange.AreaAttributesBuilder.TypeEnum@endlink) AreaType
    ##   the area type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return AreaAttributesBuilder.TypeEnum
    @property
    def AreaType(self) -> AreaAttributesBuilder.TypeEnum:
        """
        Getter for property: (@link AreaAttributesBuilder.TypeEnum NXOpen.PcbExchange.AreaAttributesBuilder.TypeEnum@endlink) AreaType
          the area type.  
             
         
        """
        pass
    
    ## Setter for property: (@link AreaAttributesBuilder.TypeEnum NXOpen.PcbExchange.AreaAttributesBuilder.TypeEnum@endlink) AreaType

    ##   the area type.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AreaType.setter
    def AreaType(self, type: AreaAttributesBuilder.TypeEnum):
        """
        Setter for property: (@link AreaAttributesBuilder.TypeEnum NXOpen.PcbExchange.AreaAttributesBuilder.TypeEnum@endlink) AreaType
          the area type.  
             
         
        """
        pass
    
    ## Getter for property: (int) Color
    ##   the area color.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def Color(self) -> int:
        """
        Getter for property: (int) Color
          the area color.  
             
         
        """
        pass
    
    ## Setter for property: (int) Color

    ##   the area color.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Color.setter
    def Color(self, color: int):
        """
        Setter for property: (int) Color
          the area color.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the area height.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the area height.  
             
         
        """
        pass
    
    ## Getter for property: (bool) InvertedVolume
    ##   the flag indicating whether an area has an inverted volume.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def InvertedVolume(self) -> bool:
        """
        Getter for property: (bool) InvertedVolume
          the flag indicating whether an area has an inverted volume.  
             
         
        """
        pass
    
    ## Setter for property: (bool) InvertedVolume

    ##   the flag indicating whether an area has an inverted volume.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @InvertedVolume.setter
    def InvertedVolume(self, invertedVolume: bool):
        """
        Setter for property: (bool) InvertedVolume
          the flag indicating whether an area has an inverted volume.  
             
         
        """
        pass
    
    ## Getter for property: (@link AreaAttributesBuilder.LayerEnum NXOpen.PcbExchange.AreaAttributesBuilder.LayerEnum@endlink) Layer
    ##   the area layer.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return AreaAttributesBuilder.LayerEnum
    @property
    def Layer(self) -> AreaAttributesBuilder.LayerEnum:
        """
        Getter for property: (@link AreaAttributesBuilder.LayerEnum NXOpen.PcbExchange.AreaAttributesBuilder.LayerEnum@endlink) Layer
          the area layer.  
             
         
        """
        pass
    
    ## Setter for property: (@link AreaAttributesBuilder.LayerEnum NXOpen.PcbExchange.AreaAttributesBuilder.LayerEnum@endlink) Layer

    ##   the area layer.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Layer.setter
    def Layer(self, type: AreaAttributesBuilder.LayerEnum):
        """
        Setter for property: (@link AreaAttributesBuilder.LayerEnum NXOpen.PcbExchange.AreaAttributesBuilder.LayerEnum@endlink) Layer
          the area layer.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the area name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the area name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the area name.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the area name.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Objects
    ##   the selected objects.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Objects
          the selected objects.  
             
         
        """
        pass
    
    ## Getter for property: (@link AreaAttributesBuilder.OwnerEnum NXOpen.PcbExchange.AreaAttributesBuilder.OwnerEnum@endlink) Owner
    ##   the area owner.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return AreaAttributesBuilder.OwnerEnum
    @property
    def Owner(self) -> AreaAttributesBuilder.OwnerEnum:
        """
        Getter for property: (@link AreaAttributesBuilder.OwnerEnum NXOpen.PcbExchange.AreaAttributesBuilder.OwnerEnum@endlink) Owner
          the area owner.  
             
         
        """
        pass
    
    ## Setter for property: (@link AreaAttributesBuilder.OwnerEnum NXOpen.PcbExchange.AreaAttributesBuilder.OwnerEnum@endlink) Owner

    ##   the area owner.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Owner.setter
    def Owner(self, type: AreaAttributesBuilder.OwnerEnum):
        """
        Setter for property: (@link AreaAttributesBuilder.OwnerEnum NXOpen.PcbExchange.AreaAttributesBuilder.OwnerEnum@endlink) Owner
          the area owner.  
             
         
        """
        pass
    
    ## Getter for property: (str) Subtype
    ##   the area subtype.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def Subtype(self) -> str:
        """
        Getter for property: (str) Subtype
          the area subtype.  
             
         
        """
        pass
    
    ## Setter for property: (str) Subtype

    ##   the area subtype.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Subtype.setter
    def Subtype(self, subtype: str):
        """
        Setter for property: (str) Subtype
          the area subtype.  
             
         
        """
        pass
    
import NXOpen
##  Represents a builder to create or edit area mapping.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateAreaMappingBuilder  NXOpen::PcbExchange::Manager::CreateAreaMappingBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class AreaMappingBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit area mapping. """


    ##  Prints area mapping areas. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def PrintMapping(builder: AreaMappingBuilder) -> None:
        """
         Prints area mapping areas. 
        """
        pass
    
    ##  Sets copper areas. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="copperAreaList"> (List[str]) </param>
    def SetCopperAreas(builder: AreaMappingBuilder, copperAreaList: List[str]) -> None:
        """
         Sets copper areas. 
        """
        pass
    
    ##  Sets keepin areas. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="keepinAreaList"> (List[str]) </param>
    def SetKeepinAreas(builder: AreaMappingBuilder, keepinAreaList: List[str]) -> None:
        """
         Sets keepin areas. 
        """
        pass
    
    ##  Sets keepout areas. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="keepoutAreaList"> (List[str]) </param>
    def SetKeepoutAreas(builder: AreaMappingBuilder, keepoutAreaList: List[str]) -> None:
        """
         Sets keepout areas. 
        """
        pass
    
    ##  Sets other areas. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="otherAreaList"> (List[str]) </param>
    def SetOtherAreas(builder: AreaMappingBuilder, otherAreaList: List[str]) -> None:
        """
         Sets other areas. 
        """
        pass
    
import NXOpen
##  Represents a Area Mapping for Pcb Exchange.  <br> To create or edit an instance of this class, use @link NXOpen::PcbExchange::AreaMappingBuilder  NXOpen::PcbExchange::AreaMappingBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class AreaMapping(NXOpen.NXObject): 
    """ Represents a Area Mapping for Pcb Exchange. """
    pass


import NXOpen
##  Represents  a @link NXOpen::PcbExchange::AttributeRemover NXOpen::PcbExchange::AttributeRemover@endlink .  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class AttributeRemover(NXOpen.Object): 
    """ Represents  a <ja_class>NXOpen.PcbExchange.AttributeRemover</ja_class>. """


    ##  The remove attributes options. 
    ##  Remove board attributes 
    class Option(Enum):
        """
        Members Include: <Board> <Components> <Areas> <Holes> <Traces> <Pads> <All>
        """
        Board: int
        Components: int
        Areas: int
        Holes: int
        Traces: int
        Pads: int
        All: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AttributeRemover.Option:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Removes the attributes. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="action"> (@link AttributeRemover.Option NXOpen.PcbExchange.AttributeRemover.Option@endlink) </param>
    ## <param name="objTags"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    def RemoveAttributes(action: AttributeRemover.Option, objTags: List[NXOpen.TaggedObject]) -> None:
        """
         Removes the attributes. 
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a builder to create or edit board attributes.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateBoardAttributesBuilder  NXOpen::PcbExchange::Manager::CreateBoardAttributesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Owner </term> <description> 
##  
## Unowned </description> </item> 
## 
## <item><term> 
##  
## Revision </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class BoardAttributesBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit board attributes. """


    ##  The owner type options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unowned</term><description> 
    ## </description> </item><item><term> 
    ## Mcad</term><description> 
    ## </description> </item><item><term> 
    ## Ecad</term><description> 
    ## </description> </item></list>
    class OwnerEnum(Enum):
        """
        Members Include: <Unowned> <Mcad> <Ecad>
        """
        Unowned: int
        Mcad: int
        Ecad: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BoardAttributesBuilder.OwnerEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectBody NXOpen.SelectBody@endlink) BoardFeature
    ##   the board feature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.SelectBody
    @property
    def BoardFeature(self) -> NXOpen.SelectBody:
        """
        Getter for property: (@link NXOpen.SelectBody NXOpen.SelectBody@endlink) BoardFeature
          the board feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.SelectDatumCsys NXOpen.Features.SelectDatumCsys@endlink) CsysSelection
    ##   the coordinate system for selection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Features.SelectDatumCsys
    @property
    def CsysSelection(self) -> NXOpen.Features.SelectDatumCsys:
        """
        Getter for property: (@link NXOpen.Features.SelectDatumCsys NXOpen.Features.SelectDatumCsys@endlink) CsysSelection
          the coordinate system for selection.  
             
         
        """
        pass
    
    ## Getter for property: (@link BoardAttributesBuilder.OwnerEnum NXOpen.PcbExchange.BoardAttributesBuilder.OwnerEnum@endlink) Owner
    ##   the board owner.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return BoardAttributesBuilder.OwnerEnum
    @property
    def Owner(self) -> BoardAttributesBuilder.OwnerEnum:
        """
        Getter for property: (@link BoardAttributesBuilder.OwnerEnum NXOpen.PcbExchange.BoardAttributesBuilder.OwnerEnum@endlink) Owner
          the board owner.  
             
         
        """
        pass
    
    ## Setter for property: (@link BoardAttributesBuilder.OwnerEnum NXOpen.PcbExchange.BoardAttributesBuilder.OwnerEnum@endlink) Owner

    ##   the board owner.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Owner.setter
    def Owner(self, owner: BoardAttributesBuilder.OwnerEnum):
        """
        Setter for property: (@link BoardAttributesBuilder.OwnerEnum NXOpen.PcbExchange.BoardAttributesBuilder.OwnerEnum@endlink) Owner
          the board owner.  
             
         
        """
        pass
    
    ## Getter for property: (str) Part
    ##   the board part name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def Part(self) -> str:
        """
        Getter for property: (str) Part
          the board part name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Part

    ##   the board part name.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Part.setter
    def Part(self, part: str):
        """
        Setter for property: (str) Part
          the board part name.  
             
         
        """
        pass
    
    ## Getter for property: (int) Revision
    ##   the board revision.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def Revision(self) -> int:
        """
        Getter for property: (int) Revision
          the board revision.  
             
         
        """
        pass
    
    ## Setter for property: (int) Revision

    ##   the board revision.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Revision.setter
    def Revision(self, revision: int):
        """
        Setter for property: (int) Revision
          the board revision.  
             
         
        """
        pass
    
import NXOpen
##  Represents a builder to create or edit board properties.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateBoardPropertiesBuilder  NXOpen::PcbExchange::Manager::CreateBoardPropertiesBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BoardPropertiesBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit board properties. """


    ##  Defines the board stackup options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FromPart</term><description> 
    ## </description> </item><item><term> 
    ## FromFile</term><description> 
    ## </description> </item><item><term> 
    ## FromODB</term><description> 
    ## </description> </item></list>
    class BoardStackupOption(Enum):
        """
        Members Include: <FromPart> <FromFile> <FromODB>
        """
        FromPart: int
        FromFile: int
        FromODB: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BoardPropertiesBuilder.BoardStackupOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines if materials come from PCB or NX. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## PCBMaterialLibrary</term><description> 
    ## </description> </item><item><term> 
    ## NXMaterialLibrary</term><description> 
    ## </description> </item></list>
    class MaterialsFromOption(Enum):
        """
        Members Include: <PCBMaterialLibrary> <NXMaterialLibrary>
        """
        PCBMaterialLibrary: int
        NXMaterialLibrary: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BoardPropertiesBuilder.MaterialsFromOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the Structural algorithm option. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Equivalent</term><description> 
    ## </description> </item></list>
    class StructuralAlgorithmOption(Enum):
        """
        Members Include: <Equivalent>
        """
        Equivalent: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BoardPropertiesBuilder.StructuralAlgorithmOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the thermal algorithm options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Discretized</term><description> 
    ## </description> </item><item><term> 
    ## Equivalent</term><description> 
    ## </description> </item></list>
    class ThermalAlgorithmOption(Enum):
        """
        Members Include: <Discretized> <Equivalent>
        """
        Discretized: int
        Equivalent: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BoardPropertiesBuilder.ThermalAlgorithmOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AdvancedOptionsFromFile
    ##   the flag indicating whether the advanced options are from the file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def AdvancedOptionsFromFile(self) -> bool:
        """
        Getter for property: (bool) AdvancedOptionsFromFile
          the flag indicating whether the advanced options are from the file.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AdvancedOptionsFromFile

    ##   the flag indicating whether the advanced options are from the file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AdvancedOptionsFromFile.setter
    def AdvancedOptionsFromFile(self, advancedOptionsFromFile: bool):
        """
        Setter for property: (bool) AdvancedOptionsFromFile
          the flag indicating whether the advanced options are from the file.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AdvancedOptionsFromPart
    ##   the flag indicating whether the advanced options are from the part.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def AdvancedOptionsFromPart(self) -> bool:
        """
        Getter for property: (bool) AdvancedOptionsFromPart
          the flag indicating whether the advanced options are from the part.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AdvancedOptionsFromPart

    ##   the flag indicating whether the advanced options are from the part.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AdvancedOptionsFromPart.setter
    def AdvancedOptionsFromPart(self, advancedOptionsFromPart: bool):
        """
        Setter for property: (bool) AdvancedOptionsFromPart
          the flag indicating whether the advanced options are from the part.  
             
         
        """
        pass
    
    ## Getter for property: (str) BoardPropertyFile
    ##   the board property file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def BoardPropertyFile(self) -> str:
        """
        Getter for property: (str) BoardPropertyFile
          the board property file.  
             
         
        """
        pass
    
    ## Setter for property: (str) BoardPropertyFile

    ##   the board property file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BoardPropertyFile.setter
    def BoardPropertyFile(self, boardPropertyFile: str):
        """
        Setter for property: (str) BoardPropertyFile
          the board property file.  
             
         
        """
        pass
    
    ## Getter for property: (@link BoardPropertiesBuilder.BoardStackupOption NXOpen.PcbExchange.BoardPropertiesBuilder.BoardStackupOption@endlink) BoardStackup
    ##   the board stackup.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return BoardPropertiesBuilder.BoardStackupOption
    @property
    def BoardStackup(self) -> BoardPropertiesBuilder.BoardStackupOption:
        """
        Getter for property: (@link BoardPropertiesBuilder.BoardStackupOption NXOpen.PcbExchange.BoardPropertiesBuilder.BoardStackupOption@endlink) BoardStackup
          the board stackup.  
             
         
        """
        pass
    
    ## Setter for property: (@link BoardPropertiesBuilder.BoardStackupOption NXOpen.PcbExchange.BoardPropertiesBuilder.BoardStackupOption@endlink) BoardStackup

    ##   the board stackup.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BoardStackup.setter
    def BoardStackup(self, boardStackup: BoardPropertiesBuilder.BoardStackupOption):
        """
        Setter for property: (@link BoardPropertiesBuilder.BoardStackupOption NXOpen.PcbExchange.BoardPropertiesBuilder.BoardStackupOption@endlink) BoardStackup
          the board stackup.  
             
         
        """
        pass
    
    ## Getter for property: (str) BoardStackupFile
    ##   the board stackup file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def BoardStackupFile(self) -> str:
        """
        Getter for property: (str) BoardStackupFile
          the board stackup file.  
             
         
        """
        pass
    
    ## Setter for property: (str) BoardStackupFile

    ##   the board stackup file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BoardStackupFile.setter
    def BoardStackupFile(self, boardStackupFile: str):
        """
        Setter for property: (str) BoardStackupFile
          the board stackup file.  
             
         
        """
        pass
    
    ## Getter for property: (str) BoardStackupODBFolder
    ##   the board stackup ODB folder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def BoardStackupODBFolder(self) -> str:
        """
        Getter for property: (str) BoardStackupODBFolder
          the board stackup ODB folder.  
             
         
        """
        pass
    
    ## Setter for property: (str) BoardStackupODBFolder

    ##   the board stackup ODB folder.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BoardStackupODBFolder.setter
    def BoardStackupODBFolder(self, boardStackupODBFolder: str):
        """
        Setter for property: (str) BoardStackupODBFolder
          the board stackup ODB folder.  
             
         
        """
        pass
    
    ## Getter for property: (int) CalculationPointsPrecision
    ##   the calculation points precision.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def CalculationPointsPrecision(self) -> int:
        """
        Getter for property: (int) CalculationPointsPrecision
          the calculation points precision.  
             
         
        """
        pass
    
    ## Setter for property: (int) CalculationPointsPrecision

    ##   the calculation points precision.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CalculationPointsPrecision.setter
    def CalculationPointsPrecision(self, calculationPointsPrecision: int):
        """
        Setter for property: (int) CalculationPointsPrecision
          the calculation points precision.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DefaultHolePlatingThickness
    ##   the default hole plating thickness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DefaultHolePlatingThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DefaultHolePlatingThickness
          the default hole plating thickness.  
             
         
        """
        pass
    
    ## Getter for property: (int) DielectricNxMaterial
    ##   the dielectric material when materials are from the NX material library.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def DielectricNxMaterial(self) -> int:
        """
        Getter for property: (int) DielectricNxMaterial
          the dielectric material when materials are from the NX material library.  
             
         
        """
        pass
    
    ## Setter for property: (int) DielectricNxMaterial

    ##   the dielectric material when materials are from the NX material library.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DielectricNxMaterial.setter
    def DielectricNxMaterial(self, dielectricNxMaterial: int):
        """
        Setter for property: (int) DielectricNxMaterial
          the dielectric material when materials are from the NX material library.  
             
         
        """
        pass
    
    ## Getter for property: (int) DielectricPcbMaterial
    ##   the dielectric material when materials are from the PCB material library.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def DielectricPcbMaterial(self) -> int:
        """
        Getter for property: (int) DielectricPcbMaterial
          the dielectric material when materials are from the PCB material library.  
             
         
        """
        pass
    
    ## Setter for property: (int) DielectricPcbMaterial

    ##   the dielectric material when materials are from the PCB material library.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DielectricPcbMaterial.setter
    def DielectricPcbMaterial(self, dielectricPcbMaterial: int):
        """
        Setter for property: (int) DielectricPcbMaterial
          the dielectric material when materials are from the PCB material library.  
             
         
        """
        pass
    
    ## Getter for property: (@link BoardPropertiesBuilder.MaterialsFromOption NXOpen.PcbExchange.BoardPropertiesBuilder.MaterialsFromOption@endlink) MaterialsFrom
    ##   the materials source.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return BoardPropertiesBuilder.MaterialsFromOption
    @property
    def MaterialsFrom(self) -> BoardPropertiesBuilder.MaterialsFromOption:
        """
        Getter for property: (@link BoardPropertiesBuilder.MaterialsFromOption NXOpen.PcbExchange.BoardPropertiesBuilder.MaterialsFromOption@endlink) MaterialsFrom
          the materials source.  
             
         
        """
        pass
    
    ## Setter for property: (@link BoardPropertiesBuilder.MaterialsFromOption NXOpen.PcbExchange.BoardPropertiesBuilder.MaterialsFromOption@endlink) MaterialsFrom

    ##   the materials source.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @MaterialsFrom.setter
    def MaterialsFrom(self, materialsFrom: BoardPropertiesBuilder.MaterialsFromOption):
        """
        Setter for property: (@link BoardPropertiesBuilder.MaterialsFromOption NXOpen.PcbExchange.BoardPropertiesBuilder.MaterialsFromOption@endlink) MaterialsFrom
          the materials source.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfCalculationPoints
    ##   the number of calculation points.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def NumberOfCalculationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfCalculationPoints
          the number of calculation points.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfCalculationPoints

    ##   the number of calculation points.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @NumberOfCalculationPoints.setter
    def NumberOfCalculationPoints(self, numberOfCalculationPoints: int):
        """
        Setter for property: (int) NumberOfCalculationPoints
          the number of calculation points.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReadViasFromFile
    ##   the flag indicating whether to read vias from file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def ReadViasFromFile(self) -> bool:
        """
        Getter for property: (bool) ReadViasFromFile
          the flag indicating whether to read vias from file.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReadViasFromFile

    ##   the flag indicating whether to read vias from file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ReadViasFromFile.setter
    def ReadViasFromFile(self, readViasFromFile: bool):
        """
        Setter for property: (bool) ReadViasFromFile
          the flag indicating whether to read vias from file.  
             
         
        """
        pass
    
    ## Getter for property: (@link BoardPropertiesBuilder.StructuralAlgorithmOption NXOpen.PcbExchange.BoardPropertiesBuilder.StructuralAlgorithmOption@endlink) StructuralAlgorithm
    ##   the structural algorithm.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return BoardPropertiesBuilder.StructuralAlgorithmOption
    @property
    def StructuralAlgorithm(self) -> BoardPropertiesBuilder.StructuralAlgorithmOption:
        """
        Getter for property: (@link BoardPropertiesBuilder.StructuralAlgorithmOption NXOpen.PcbExchange.BoardPropertiesBuilder.StructuralAlgorithmOption@endlink) StructuralAlgorithm
          the structural algorithm.  
             
         
        """
        pass
    
    ## Setter for property: (@link BoardPropertiesBuilder.StructuralAlgorithmOption NXOpen.PcbExchange.BoardPropertiesBuilder.StructuralAlgorithmOption@endlink) StructuralAlgorithm

    ##   the structural algorithm.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @StructuralAlgorithm.setter
    def StructuralAlgorithm(self, algorithm: BoardPropertiesBuilder.StructuralAlgorithmOption):
        """
        Setter for property: (@link BoardPropertiesBuilder.StructuralAlgorithmOption NXOpen.PcbExchange.BoardPropertiesBuilder.StructuralAlgorithmOption@endlink) StructuralAlgorithm
          the structural algorithm.  
             
         
        """
        pass
    
    ## Getter for property: (@link BoardPropertiesBuilder.ThermalAlgorithmOption NXOpen.PcbExchange.BoardPropertiesBuilder.ThermalAlgorithmOption@endlink) ThermalAlgorithm
    ##   the thermal algorithm.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return BoardPropertiesBuilder.ThermalAlgorithmOption
    @property
    def ThermalAlgorithm(self) -> BoardPropertiesBuilder.ThermalAlgorithmOption:
        """
        Getter for property: (@link BoardPropertiesBuilder.ThermalAlgorithmOption NXOpen.PcbExchange.BoardPropertiesBuilder.ThermalAlgorithmOption@endlink) ThermalAlgorithm
          the thermal algorithm.  
             
         
        """
        pass
    
    ## Setter for property: (@link BoardPropertiesBuilder.ThermalAlgorithmOption NXOpen.PcbExchange.BoardPropertiesBuilder.ThermalAlgorithmOption@endlink) ThermalAlgorithm

    ##   the thermal algorithm.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ThermalAlgorithm.setter
    def ThermalAlgorithm(self, algorithm: BoardPropertiesBuilder.ThermalAlgorithmOption):
        """
        Setter for property: (@link BoardPropertiesBuilder.ThermalAlgorithmOption NXOpen.PcbExchange.BoardPropertiesBuilder.ThermalAlgorithmOption@endlink) ThermalAlgorithm
          the thermal algorithm.  
             
         
        """
        pass
    
    ## Getter for property: (int) TraceNxMaterial
    ##   the trace material when materials are from theNX material library.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def TraceNxMaterial(self) -> int:
        """
        Getter for property: (int) TraceNxMaterial
          the trace material when materials are from theNX material library.  
             
         
        """
        pass
    
    ## Setter for property: (int) TraceNxMaterial

    ##   the trace material when materials are from theNX material library.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TraceNxMaterial.setter
    def TraceNxMaterial(self, traceNxMaterial: int):
        """
        Setter for property: (int) TraceNxMaterial
          the trace material when materials are from theNX material library.  
             
         
        """
        pass
    
    ## Getter for property: (int) TracePcbMaterial
    ##   the trace material when materials are from the PCB material library.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def TracePcbMaterial(self) -> int:
        """
        Getter for property: (int) TracePcbMaterial
          the trace material when materials are from the PCB material library.  
             
         
        """
        pass
    
    ## Setter for property: (int) TracePcbMaterial

    ##   the trace material when materials are from the PCB material library.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TracePcbMaterial.setter
    def TracePcbMaterial(self, tracePcbMaterial: int):
        """
        Setter for property: (int) TracePcbMaterial
          the trace material when materials are from the PCB material library.  
             
         
        """
        pass
    
    ## Getter for property: (int) ViaNxMaterial
    ##   the via material when materials are from the NX material library.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def ViaNxMaterial(self) -> int:
        """
        Getter for property: (int) ViaNxMaterial
          the via material when materials are from the NX material library.  
             
         
        """
        pass
    
    ## Setter for property: (int) ViaNxMaterial

    ##   the via material when materials are from the NX material library.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ViaNxMaterial.setter
    def ViaNxMaterial(self, viaNxMaterial: int):
        """
        Setter for property: (int) ViaNxMaterial
          the via material when materials are from the NX material library.  
             
         
        """
        pass
    
    ## Getter for property: (int) ViaPcbMaterial
    ##   the via material when materials are from the PCB material library.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def ViaPcbMaterial(self) -> int:
        """
        Getter for property: (int) ViaPcbMaterial
          the via material when materials are from the PCB material library.  
             
         
        """
        pass
    
    ## Setter for property: (int) ViaPcbMaterial

    ##   the via material when materials are from the PCB material library.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ViaPcbMaterial.setter
    def ViaPcbMaterial(self, viaPcbMaterial: int):
        """
        Setter for property: (int) ViaPcbMaterial
          the via material when materials are from the PCB material library.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ViewCalculationReport
    ##   the flag indicating whether to show the calculation report after the calculation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def ViewCalculationReport(self) -> bool:
        """
        Getter for property: (bool) ViewCalculationReport
          the flag indicating whether to show the calculation report after the calculation.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ViewCalculationReport

    ##   the flag indicating whether to show the calculation report after the calculation.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ViewCalculationReport.setter
    def ViewCalculationReport(self, viewCalculationReport: bool):
        """
        Setter for property: (bool) ViewCalculationReport
          the flag indicating whether to show the calculation report after the calculation.  
             
         
        """
        pass
    
##  Defines the side of a Board. 
##  Either side. 
class BoardSide(Enum):
    """
    Members Include: <Both> <Top> <Bottom>
    """
    Both: int
    Top: int
    Bottom: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> BoardSide:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents a builder to compare MCAD and ECAD files and update.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateCompareAndUpdateBuilder  NXOpen::PcbExchange::Manager::CreateCompareAndUpdateBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class CompareAndUpdateBuilder(NXOpen.Builder): 
    """ Represents a builder to compare MCAD and ECAD files and update. """


    ##  The assembly update options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Specify</term><description> 
    ## </description> </item></list>
    class AssemblyUpdateEnum(Enum):
        """
        Members Include: <All> <NotSet> <Specify>
        """
        All: int
        NotSet: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CompareAndUpdateBuilder.AssemblyUpdateEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The board update options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item></list>
    class BoardUpdateEnum(Enum):
        """
        Members Include: <All> <NotSet>
        """
        All: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CompareAndUpdateBuilder.BoardUpdateEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The compare options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## BoardOnly</term><description> 
    ## </description> </item></list>
    class CompareEnum(Enum):
        """
        Members Include: <All> <BoardOnly>
        """
        All: int
        BoardOnly: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CompareAndUpdateBuilder.CompareEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CompareAndUpdateBuilder.AssemblyUpdateEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.AssemblyUpdateEnum@endlink) AssemblyUpdateOptions
    ##   the assembly update options.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return CompareAndUpdateBuilder.AssemblyUpdateEnum
    @property
    def AssemblyUpdateOptions(self) -> CompareAndUpdateBuilder.AssemblyUpdateEnum:
        """
        Getter for property: (@link CompareAndUpdateBuilder.AssemblyUpdateEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.AssemblyUpdateEnum@endlink) AssemblyUpdateOptions
          the assembly update options.  
             
         
        """
        pass
    
    ## Setter for property: (@link CompareAndUpdateBuilder.AssemblyUpdateEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.AssemblyUpdateEnum@endlink) AssemblyUpdateOptions

    ##   the assembly update options.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AssemblyUpdateOptions.setter
    def AssemblyUpdateOptions(self, assemblyUpdateOptions: CompareAndUpdateBuilder.AssemblyUpdateEnum):
        """
        Setter for property: (@link CompareAndUpdateBuilder.AssemblyUpdateEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.AssemblyUpdateEnum@endlink) AssemblyUpdateOptions
          the assembly update options.  
             
         
        """
        pass
    
    ## Getter for property: (str) BoardFile
    ##   the board file when the board does not come from ODB.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def BoardFile(self) -> str:
        """
        Getter for property: (str) BoardFile
          the board file when the board does not come from ODB.  
             
         
        """
        pass
    
    ## Setter for property: (str) BoardFile

    ##   the board file when the board does not come from ODB.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BoardFile.setter
    def BoardFile(self, boardFile: str):
        """
        Setter for property: (str) BoardFile
          the board file when the board does not come from ODB.  
             
         
        """
        pass
    
    ## Getter for property: (str) BoardFolder
    ##   the folder when the board comes from ODB.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def BoardFolder(self) -> str:
        """
        Getter for property: (str) BoardFolder
          the folder when the board comes from ODB.  
             
         
        """
        pass
    
    ## Setter for property: (str) BoardFolder

    ##   the folder when the board comes from ODB.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BoardFolder.setter
    def BoardFolder(self, boardFolder: str):
        """
        Setter for property: (str) BoardFolder
          the folder when the board comes from ODB.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardThickness
    ##   the board thickness when the thickness is overriden.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BoardThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardThickness
          the board thickness when the thickness is overriden.  
             
         
        """
        pass
    
    ## Getter for property: (@link CompareAndUpdateBuilder.BoardUpdateEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.BoardUpdateEnum@endlink) BoardUpdateOptions
    ##   the board update options.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return CompareAndUpdateBuilder.BoardUpdateEnum
    @property
    def BoardUpdateOptions(self) -> CompareAndUpdateBuilder.BoardUpdateEnum:
        """
        Getter for property: (@link CompareAndUpdateBuilder.BoardUpdateEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.BoardUpdateEnum@endlink) BoardUpdateOptions
          the board update options.  
             
         
        """
        pass
    
    ## Setter for property: (@link CompareAndUpdateBuilder.BoardUpdateEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.BoardUpdateEnum@endlink) BoardUpdateOptions

    ##   the board update options.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BoardUpdateOptions.setter
    def BoardUpdateOptions(self, boardUpdateOptions: CompareAndUpdateBuilder.BoardUpdateEnum):
        """
        Setter for property: (@link CompareAndUpdateBuilder.BoardUpdateEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.BoardUpdateEnum@endlink) BoardUpdateOptions
          the board update options.  
             
         
        """
        pass
    
    ## Getter for property: (@link CompareAndUpdateBuilder.CompareEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.CompareEnum@endlink) CompareOptions
    ##   the compare options.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return CompareAndUpdateBuilder.CompareEnum
    @property
    def CompareOptions(self) -> CompareAndUpdateBuilder.CompareEnum:
        """
        Getter for property: (@link CompareAndUpdateBuilder.CompareEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.CompareEnum@endlink) CompareOptions
          the compare options.  
             
         
        """
        pass
    
    ## Setter for property: (@link CompareAndUpdateBuilder.CompareEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.CompareEnum@endlink) CompareOptions

    ##   the compare options.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CompareOptions.setter
    def CompareOptions(self, compareOptions: CompareAndUpdateBuilder.CompareEnum):
        """
        Setter for property: (@link CompareAndUpdateBuilder.CompareEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.CompareEnum@endlink) CompareOptions
          the compare options.  
             
         
        """
        pass
    
    ## Getter for property: (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) ECADEntityFilter
    ##   the ECAD filters.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return EntityFilter
    @property
    def ECADEntityFilter(self) -> EntityFilter:
        """
        Getter for property: (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) ECADEntityFilter
          the ECAD filters.  
             
         
        """
        pass
    
    ## Setter for property: (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) ECADEntityFilter

    ##   the ECAD filters.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ECADEntityFilter.setter
    def ECADEntityFilter(self, filter: EntityFilter):
        """
        Setter for property: (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) ECADEntityFilter
          the ECAD filters.  
             
         
        """
        pass
    
    ## Getter for property: (bool) FilterEcadModel
    ##   the flag indicating whether to filter the ECAD model.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def FilterEcadModel(self) -> bool:
        """
        Getter for property: (bool) FilterEcadModel
          the flag indicating whether to filter the ECAD model.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FilterEcadModel

    ##   the flag indicating whether to filter the ECAD model.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FilterEcadModel.setter
    def FilterEcadModel(self, filterEcadModel: bool):
        """
        Setter for property: (bool) FilterEcadModel
          the flag indicating whether to filter the ECAD model.  
             
         
        """
        pass
    
    ## Getter for property: (bool) FilterNxModel
    ##   the flag indicating whether to filter the NX model.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def FilterNxModel(self) -> bool:
        """
        Getter for property: (bool) FilterNxModel
          the flag indicating whether to filter the NX model.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FilterNxModel

    ##   the flag indicating whether to filter the NX model.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FilterNxModel.setter
    def FilterNxModel(self, filterNxModel: bool):
        """
        Setter for property: (bool) FilterNxModel
          the flag indicating whether to filter the NX model.  
             
         
        """
        pass
    
    ## Getter for property: (bool) FromOdbFolder
    ##   the flag indicating whether the board comes from ODB.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def FromOdbFolder(self) -> bool:
        """
        Getter for property: (bool) FromOdbFolder
          the flag indicating whether the board comes from ODB.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FromOdbFolder

    ##   the flag indicating whether the board comes from ODB.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FromOdbFolder.setter
    def FromOdbFolder(self, fromOdbFolder: bool):
        """
        Setter for property: (bool) FromOdbFolder
          the flag indicating whether the board comes from ODB.  
             
         
        """
        pass
    
    ## Getter for property: (str) LibraryFile
    ##   the library file when the board does not come from ODB.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def LibraryFile(self) -> str:
        """
        Getter for property: (str) LibraryFile
          the library file when the board does not come from ODB.  
             
         
        """
        pass
    
    ## Setter for property: (str) LibraryFile

    ##   the library file when the board does not come from ODB.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @LibraryFile.setter
    def LibraryFile(self, libraryFile: str):
        """
        Setter for property: (str) LibraryFile
          the library file when the board does not come from ODB.  
             
         
        """
        pass
    
    ## Getter for property: (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) NXEntityFilter
    ##   the NX model filters.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return EntityFilter
    @property
    def NXEntityFilter(self) -> EntityFilter:
        """
        Getter for property: (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) NXEntityFilter
          the NX model filters.  
             
         
        """
        pass
    
    ## Setter for property: (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) NXEntityFilter

    ##   the NX model filters.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @NXEntityFilter.setter
    def NXEntityFilter(self, filter: EntityFilter):
        """
        Setter for property: (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) NXEntityFilter
          the NX model filters.  
             
         
        """
        pass
    
    ## Getter for property: (bool) OnlyUseExistingComponents
    ##   the flag indicating whether to only use existing components.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def OnlyUseExistingComponents(self) -> bool:
        """
        Getter for property: (bool) OnlyUseExistingComponents
          the flag indicating whether to only use existing components.  
             
         
        """
        pass
    
    ## Setter for property: (bool) OnlyUseExistingComponents

    ##   the flag indicating whether to only use existing components.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @OnlyUseExistingComponents.setter
    def OnlyUseExistingComponents(self, onlyUseExistingComponents: bool):
        """
        Setter for property: (bool) OnlyUseExistingComponents
          the flag indicating whether to only use existing components.  
             
         
        """
        pass
    
    ## Getter for property: (bool) OverrideBoardThickness
    ##   the flag indicating whether to override the board thickness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def OverrideBoardThickness(self) -> bool:
        """
        Getter for property: (bool) OverrideBoardThickness
          the flag indicating whether to override the board thickness.  
             
         
        """
        pass
    
    ## Setter for property: (bool) OverrideBoardThickness

    ##   the flag indicating whether to override the board thickness.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @OverrideBoardThickness.setter
    def OverrideBoardThickness(self, overrideBoardThickness: bool):
        """
        Setter for property: (bool) OverrideBoardThickness
          the flag indicating whether to override the board thickness.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowLog
    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowLog

    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ##  Compares the assemblies. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def Compare(builder: CompareAndUpdateBuilder) -> None:
        """
         Compares the assemblies. 
        """
        pass
    
    ##  Previews all changes. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def PreviewChanges(builder: CompareAndUpdateBuilder) -> None:
        """
         Previews all changes. 
        """
        pass
    
    ##  Sets the update option flag. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="resDef"> (str) </param>
    ## <param name="status"> (bool) </param>
    def SetUpdateOption(builder: CompareAndUpdateBuilder, resDef: str, status: bool) -> None:
        """
         Sets the update option flag. 
        """
        pass
    
    ##  Un-highlights all. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def UnhighlightAll(builder: CompareAndUpdateBuilder) -> None:
        """
         Un-highlights all. 
        """
        pass
    
import NXOpen
##  Represents a builder to create or edit component attributes.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateBoardAttributesBuilder  NXOpen::PcbExchange::Manager::CreateBoardAttributesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## PlacementOwner </term> <description> 
##  
## Placed </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class ComponentAttributesBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit component attributes. """


    ##  The placement/owner options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Mcad</term><description> 
    ## </description> </item><item><term> 
    ## Ecad</term><description> 
    ## </description> </item><item><term> 
    ## Placed</term><description> 
    ## </description> </item><item><term> 
    ## Unplaced</term><description> 
    ## </description> </item></list>
    class PlacementOwnerEnum(Enum):
        """
        Members Include: <Mcad> <Ecad> <Placed> <Unplaced>
        """
        Mcad: int
        Ecad: int
        Placed: int
        Unplaced: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ComponentAttributesBuilder.PlacementOwnerEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Components
    ##   the components.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Components(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Components
          the components.  
             
         
        """
        pass
    
    ## Getter for property: (bool) PackageClearanceTypesModification
    ##   the flag indicating whether a component package clearance types change is allowed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def PackageClearanceTypesModification(self) -> bool:
        """
        Getter for property: (bool) PackageClearanceTypesModification
          the flag indicating whether a component package clearance types change is allowed.  
             
         
        """
        pass
    
    ## Setter for property: (bool) PackageClearanceTypesModification

    ##   the flag indicating whether a component package clearance types change is allowed.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @PackageClearanceTypesModification.setter
    def PackageClearanceTypesModification(self, canModification: bool):
        """
        Setter for property: (bool) PackageClearanceTypesModification
          the flag indicating whether a component package clearance types change is allowed.  
             
         
        """
        pass
    
    ## Getter for property: (str) PackageName
    ##   the component package name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def PackageName(self) -> str:
        """
        Getter for property: (str) PackageName
          the component package name.  
             
         
        """
        pass
    
    ## Setter for property: (str) PackageName

    ##   the component package name.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PackageName.setter
    def PackageName(self, packageName: str):
        """
        Setter for property: (str) PackageName
          the component package name.  
             
         
        """
        pass
    
    ## Getter for property: (bool) PackageNameModification
    ##   the flag indicating whether a component package name change is allowed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def PackageNameModification(self) -> bool:
        """
        Getter for property: (bool) PackageNameModification
          the flag indicating whether a component package name change is allowed.  
             
         
        """
        pass
    
    ## Setter for property: (bool) PackageNameModification

    ##   the flag indicating whether a component package name change is allowed.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PackageNameModification.setter
    def PackageNameModification(self, canModification: bool):
        """
        Setter for property: (bool) PackageNameModification
          the flag indicating whether a component package name change is allowed.  
             
         
        """
        pass
    
    ## Getter for property: (str) PartNumber
    ##   the component part number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def PartNumber(self) -> str:
        """
        Getter for property: (str) PartNumber
          the component part number.  
             
         
        """
        pass
    
    ## Setter for property: (str) PartNumber

    ##   the component part number.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PartNumber.setter
    def PartNumber(self, partNumber: str):
        """
        Setter for property: (str) PartNumber
          the component part number.  
             
         
        """
        pass
    
    ## Getter for property: (bool) PartNumberModification
    ##   the flag indicating whether a component part number change is allowed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def PartNumberModification(self) -> bool:
        """
        Getter for property: (bool) PartNumberModification
          the flag indicating whether a component part number change is allowed.  
             
         
        """
        pass
    
    ## Setter for property: (bool) PartNumberModification

    ##   the flag indicating whether a component part number change is allowed.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PartNumberModification.setter
    def PartNumberModification(self, canModification: bool):
        """
        Setter for property: (bool) PartNumberModification
          the flag indicating whether a component part number change is allowed.  
             
         
        """
        pass
    
    ## Getter for property: (@link ComponentAttributesBuilder.PlacementOwnerEnum NXOpen.PcbExchange.ComponentAttributesBuilder.PlacementOwnerEnum@endlink) PlacementOwner
    ##   the component placement/owner.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return ComponentAttributesBuilder.PlacementOwnerEnum
    @property
    def PlacementOwner(self) -> ComponentAttributesBuilder.PlacementOwnerEnum:
        """
        Getter for property: (@link ComponentAttributesBuilder.PlacementOwnerEnum NXOpen.PcbExchange.ComponentAttributesBuilder.PlacementOwnerEnum@endlink) PlacementOwner
          the component placement/owner.  
             
         
        """
        pass
    
    ## Setter for property: (@link ComponentAttributesBuilder.PlacementOwnerEnum NXOpen.PcbExchange.ComponentAttributesBuilder.PlacementOwnerEnum@endlink) PlacementOwner

    ##   the component placement/owner.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PlacementOwner.setter
    def PlacementOwner(self, placementOwner: ComponentAttributesBuilder.PlacementOwnerEnum):
        """
        Setter for property: (@link ComponentAttributesBuilder.PlacementOwnerEnum NXOpen.PcbExchange.ComponentAttributesBuilder.PlacementOwnerEnum@endlink) PlacementOwner
          the component placement/owner.  
             
         
        """
        pass
    
    ## Getter for property: (str) ReferenceDesignator
    ##   the component reference designator.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def ReferenceDesignator(self) -> str:
        """
        Getter for property: (str) ReferenceDesignator
          the component reference designator.  
             
         
        """
        pass
    
    ## Setter for property: (str) ReferenceDesignator

    ##   the component reference designator.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ReferenceDesignator.setter
    def ReferenceDesignator(self, referenceDesignator: str):
        """
        Setter for property: (str) ReferenceDesignator
          the component reference designator.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReferenceDesignatorModification
    ##   the flag indicating whether a component reference designator change is allowed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ReferenceDesignatorModification(self) -> bool:
        """
        Getter for property: (bool) ReferenceDesignatorModification
          the flag indicating whether a component reference designator change is allowed.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReferenceDesignatorModification

    ##   the flag indicating whether a component reference designator change is allowed.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ReferenceDesignatorModification.setter
    def ReferenceDesignatorModification(self, canModification: bool):
        """
        Setter for property: (bool) ReferenceDesignatorModification
          the flag indicating whether a component reference designator change is allowed.  
             
         
        """
        pass
    
    ##  Gets the package clearance types. 
    ##  @return data (List[str]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPackageClearanceTypes(builder: ComponentAttributesBuilder) -> List[str]:
        """
         Gets the package clearance types. 
         @return data (List[str]): .
        """
        pass
    
    ##  Sets the package clearance types. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="data"> (List[str]) </param>
    def SetPackageClearanceTypes(builder: ComponentAttributesBuilder, data: List[str]) -> None:
        """
         Sets the package clearance types. 
        """
        pass
    
import NXOpen
##  Represents a builder to create, edit, or remove automatic component-board constraints.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateComponentConstraintsBuilder  NXOpen::PcbExchange::Manager::CreateComponentConstraintsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ComponentConstraintsBuilder(NXOpen.Builder): 
    """ Represents a builder to create, edit, or remove automatic component-board constraints. """


    ##  the action options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Add</term><description> 
    ## </description> </item><item><term> 
    ## Remove</term><description> 
    ## </description> </item></list>
    class ActionEnum(Enum):
        """
        Members Include: <Add> <Remove>
        """
        Add: int
        Remove: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ComponentConstraintsBuilder.ActionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ComponentConstraintsBuilder.ActionEnum NXOpen.PcbExchange.ComponentConstraintsBuilder.ActionEnum@endlink) Action
    ##   the action to be performed on the component-board constraints by the builder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return ComponentConstraintsBuilder.ActionEnum
    @property
    def Action(self) -> ComponentConstraintsBuilder.ActionEnum:
        """
        Getter for property: (@link ComponentConstraintsBuilder.ActionEnum NXOpen.PcbExchange.ComponentConstraintsBuilder.ActionEnum@endlink) Action
          the action to be performed on the component-board constraints by the builder.  
             
         
        """
        pass
    
    ## Setter for property: (@link ComponentConstraintsBuilder.ActionEnum NXOpen.PcbExchange.ComponentConstraintsBuilder.ActionEnum@endlink) Action

    ##   the action to be performed on the component-board constraints by the builder.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Action.setter
    def Action(self, action: ComponentConstraintsBuilder.ActionEnum):
        """
        Setter for property: (@link ComponentConstraintsBuilder.ActionEnum NXOpen.PcbExchange.ComponentConstraintsBuilder.ActionEnum@endlink) Action
          the action to be performed on the component-board constraints by the builder.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BoardFaces
    ##   the selected board faces.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BoardFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BoardFaces
          the selected board faces.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a builder to create a component csys attribute.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateComponentCsysBuilder  NXOpen::PcbExchange::Manager::CreateComponentCsysBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ComponentCsysBuilder(NXOpen.Builder): 
    """ Represents a builder to create a component csys attribute. """


    ## Getter for property: (@link NXOpen.Features.SelectDatumCsys NXOpen.Features.SelectDatumCsys@endlink) Selection
    ##   the csys selection.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Features.SelectDatumCsys
    @property
    def Selection(self) -> NXOpen.Features.SelectDatumCsys:
        """
        Getter for property: (@link NXOpen.Features.SelectDatumCsys NXOpen.Features.SelectDatumCsys@endlink) Selection
          the csys selection.  
            
         
        """
        pass
    
import NXOpen
##  Represents a builder to create a component placement outline attribute.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateComponentPlacementOutlineBuilder  NXOpen::PcbExchange::Manager::CreateComponentPlacementOutlineBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class ComponentPlacementOutlineBuilder(NXOpen.Builder): 
    """ Represents a builder to create a component placement outline attribute. """


    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Sketch
    ##   the sketch.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def Sketch(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Sketch
          the sketch.  
            
         
        """
        pass
    
##  Defines the position of a conductive layer. 
##  Any layer. 
class ConductiveLayerSide(Enum):
    """
    Members Include: <All> <Top> <Bottom> <Outer> <Inner>
    """
    All: int
    Top: int
    Bottom: int
    Outer: int
    Inner: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ConductiveLayerSide:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents a Design Interference for Pcb Exchange Design Validation.  <br> There is no kf creator for this.  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class DesignInterference(NXOpen.TaggedObject): 
    """ Represents a Design Interference for Pcb Exchange Design Validation. """


    ## Getter for property: (float) Distance
    ##   the distance.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
          the distance.  
             
         
        """
        pass
    
    ## Getter for property: (str) PrimaryEntity
    ##   the primary entity.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def PrimaryEntity(self) -> str:
        """
        Getter for property: (str) PrimaryEntity
          the primary entity.  
             
         
        """
        pass
    
    ## Getter for property: (str) ResultType
    ##   the result type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def ResultType(self) -> str:
        """
        Getter for property: (str) ResultType
          the result type.  
             
         
        """
        pass
    
    ## Getter for property: (@link DesignRule NXOpen.PcbExchange.DesignRule@endlink) Rule
    ##   the rule.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return DesignRule
    @property
    def Rule(self) -> DesignRule:
        """
        Getter for property: (@link DesignRule NXOpen.PcbExchange.DesignRule@endlink) Rule
          the rule.  
             
         
        """
        pass
    
    ## Getter for property: (str) RuleMeasurement
    ##   the rule measurement.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def RuleMeasurement(self) -> str:
        """
        Getter for property: (str) RuleMeasurement
          the rule measurement.  
             
         
        """
        pass
    
    ## Getter for property: (str) RuleName
    ##   the rule name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def RuleName(self) -> str:
        """
        Getter for property: (str) RuleName
          the rule name.  
             
         
        """
        pass
    
    ## Getter for property: (str) RuleSeverity
    ##   the rule severity.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def RuleSeverity(self) -> str:
        """
        Getter for property: (str) RuleSeverity
          the rule severity.  
             
         
        """
        pass
    
    ## Getter for property: (str) RuleType
    ##   the rule type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def RuleType(self) -> str:
        """
        Getter for property: (str) RuleType
          the rule type.  
             
         
        """
        pass
    
    ## Getter for property: (str) SecondaryEntity
    ##   the secondary entity.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def SecondaryEntity(self) -> str:
        """
        Getter for property: (str) SecondaryEntity
          the secondary entity.  
             
         
        """
        pass
    
import NXOpen
##  Creates or edits @link NXOpen::PcbExchange::DesignRule NXOpen::PcbExchange::DesignRule@endlink .
##         A call to @link NXOpen::Builder::Commit NXOpen::Builder::Commit@endlink  on this builder will only return NULL.
##      <br> Use @link NXOpen::PcbExchange::Manager NXOpen::PcbExchange::Manager@endlink  to get an instance of this class.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class DesignRuleBuilder(NXOpen.Builder): 
    """ Creates or edits <ja_class>NXOpen.PcbExchange.DesignRule</ja_class>.
        A call to <ja_method>NXOpen.Builder.Commit</ja_method> on this builder will only return <ja_NULL>.
    """


    ##  Criteria for filtering entities of Component class. 
    ##  Accept any Pcb Components. 
    class ComponentFilter(Enum):
        """
        Members Include: <Any> <ByPackage> <ByOwner> <ByRefDes> <ByPartNumber> <ByCompType> <ByPartName> <ByAreaName> <ByAreaSubtype> <ByAreaOwner> <ByAreaLayer> <Specify> <ByNetName> <ByPackageClearanceType> <ByWireBondNetName>
        """
        Any: int
        ByPackage: int
        ByOwner: int
        ByRefDes: int
        ByPartNumber: int
        ByCompType: int
        ByPartName: int
        ByAreaName: int
        ByAreaSubtype: int
        ByAreaOwner: int
        ByAreaLayer: int
        Specify: int
        ByNetName: int
        ByPackageClearanceType: int
        ByWireBondNetName: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DesignRuleBuilder.ComponentFilter:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link DesignRuleType NXOpen.PcbExchange.DesignRuleType@endlink) ConstraintType
    ##   the constraint type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return DesignRuleType
    @property
    def ConstraintType(self) -> DesignRuleType:
        """
        Getter for property: (@link DesignRuleType NXOpen.PcbExchange.DesignRuleType@endlink) ConstraintType
          the constraint type.  
             
         
        """
        pass
    
    ## Setter for property: (@link DesignRuleType NXOpen.PcbExchange.DesignRuleType@endlink) ConstraintType

    ##   the constraint type.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ConstraintType.setter
    def ConstraintType(self, constraintType: DesignRuleType):
        """
        Setter for property: (@link DesignRuleType NXOpen.PcbExchange.DesignRuleType@endlink) ConstraintType
          the constraint type.  
             
         
        """
        pass
    
    ## Getter for property: (@link DesignRuleMeasurement NXOpen.PcbExchange.DesignRuleMeasurement@endlink) MeasurementType
    ##   the measurement type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return DesignRuleMeasurement
    @property
    def MeasurementType(self) -> DesignRuleMeasurement:
        """
        Getter for property: (@link DesignRuleMeasurement NXOpen.PcbExchange.DesignRuleMeasurement@endlink) MeasurementType
          the measurement type.  
             
         
        """
        pass
    
    ## Setter for property: (@link DesignRuleMeasurement NXOpen.PcbExchange.DesignRuleMeasurement@endlink) MeasurementType

    ##   the measurement type.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MeasurementType.setter
    def MeasurementType(self, measurementType: DesignRuleMeasurement):
        """
        Setter for property: (@link DesignRuleMeasurement NXOpen.PcbExchange.DesignRuleMeasurement@endlink) MeasurementType
          the measurement type.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the rule name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the rule name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the rule name.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the rule name.  
             
         
        """
        pass
    
    ## Getter for property: (@link DesignRuleSeverity NXOpen.PcbExchange.DesignRuleSeverity@endlink) Severity
    ##   the design rule severity.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return DesignRuleSeverity
    @property
    def Severity(self) -> DesignRuleSeverity:
        """
        Getter for property: (@link DesignRuleSeverity NXOpen.PcbExchange.DesignRuleSeverity@endlink) Severity
          the design rule severity.  
             
         
        """
        pass
    
    ## Setter for property: (@link DesignRuleSeverity NXOpen.PcbExchange.DesignRuleSeverity@endlink) Severity

    ##   the design rule severity.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Severity.setter
    def Severity(self, severity: DesignRuleSeverity):
        """
        Setter for property: (@link DesignRuleSeverity NXOpen.PcbExchange.DesignRuleSeverity@endlink) Severity
          the design rule severity.  
             
         
        """
        pass
    
    ##  Gets an optional board side parameter for the component filter for a given side of the constraint. 
    ##  @return side (@link BoardSide NXOpen.PcbExchange.BoardSide@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  Index of the filter. 
    def GetBoardSide(builder: DesignRuleBuilder, filterIndex: int) -> BoardSide:
        """
         Gets an optional board side parameter for the component filter for a given side of the constraint. 
         @return side (@link BoardSide NXOpen.PcbExchange.BoardSide@endlink): .
        """
        pass
    
    ##  Gets the clearance requirement in a given direction. The value is expressed in Part Units. 
    ##  @return clearance (float):  The clearance value in Part Units. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The direction. 
    def GetClearance(builder: DesignRuleBuilder, direction: DesignRuleMargin) -> float:
        """
         Gets the clearance requirement in a given direction. The value is expressed in Part Units. 
         @return clearance (float):  The clearance value in Part Units. .
        """
        pass
    
    ##  Gets the component filter criteria for a given side of the constraint. Only applicable when @link NXOpen::PcbExchange::EntityCategory NXOpen::PcbExchange::EntityCategory@endlink  is @link NXOpen::PcbExchange::EntityCategoryComponent NXOpen::PcbExchange::EntityCategoryComponent@endlink . 
    ##  @return componentFilter (@link DesignRuleBuilder.ComponentFilter NXOpen.PcbExchange.DesignRuleBuilder.ComponentFilter@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  Index of the filter. 
    def GetComponentFilter(builder: DesignRuleBuilder, filterIndex: int) -> DesignRuleBuilder.ComponentFilter:
        """
         Gets the component filter criteria for a given side of the constraint. Only applicable when @link NXOpen::PcbExchange::EntityCategory NXOpen::PcbExchange::EntityCategory@endlink  is @link NXOpen::PcbExchange::EntityCategoryComponent NXOpen::PcbExchange::EntityCategoryComponent@endlink . 
         @return componentFilter (@link DesignRuleBuilder.ComponentFilter NXOpen.PcbExchange.DesignRuleBuilder.ComponentFilter@endlink): .
        """
        pass
    
    ##  Gets an optional conductive layer side parameter for the copper filter for a given side of the constraint. 
    ##  @return side (@link ConductiveLayerSide NXOpen.PcbExchange.ConductiveLayerSide@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  Index of the filter. 
    def GetConductiveLayerSide(builder: DesignRuleBuilder, filterIndex: int) -> ConductiveLayerSide:
        """
         Gets an optional conductive layer side parameter for the copper filter for a given side of the constraint. 
         @return side (@link ConductiveLayerSide NXOpen.PcbExchange.ConductiveLayerSide@endlink): .
        """
        pass
    
    ##  Gets the entity category for a given side of the constraint. 
    ##  @return entityType (@link EntityCategory NXOpen.PcbExchange.EntityCategory@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  Index of the filter. 
    def GetEntityType(builder: DesignRuleBuilder, filterIndex: int) -> EntityCategory:
        """
         Gets the entity category for a given side of the constraint. 
         @return entityType (@link EntityCategory NXOpen.PcbExchange.EntityCategory@endlink): .
        """
        pass
    
    ##  Gets an optional string parameters for the component filter for a given side of the constraint. 
    ##  @return data (List[str]): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  Index of the filter. 
    def GetFilterData(builder: DesignRuleBuilder, filterIndex: int) -> List[str]:
        """
         Gets an optional string parameters for the component filter for a given side of the constraint. 
         @return data (List[str]): .
        """
        pass
    
    ##  Gets an optional wire bond side parameter for the wire bond filter for a given side of the constraint. 
    ##  @return side (@link WireBondSide NXOpen.PcbExchange.WireBondSide@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  Index of the filter. 
    def GetWireBondSide(builder: DesignRuleBuilder, filterIndex: int) -> WireBondSide:
        """
         Gets an optional wire bond side parameter for the wire bond filter for a given side of the constraint. 
         @return side (@link WireBondSide NXOpen.PcbExchange.WireBondSide@endlink): .
        """
        pass
    
    ##  Sets an optional board side parameter for the component filter for a given side of the constraint. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  Index of the filter. 
    def SetBoardSide(builder: DesignRuleBuilder, filterIndex: int, side: BoardSide) -> None:
        """
         Sets an optional board side parameter for the component filter for a given side of the constraint. 
        """
        pass
    
    ##  Sets the clearance requirement in a given direction. The value is expressed in Part Units. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  The direction. 
    def SetClearance(builder: DesignRuleBuilder, direction: DesignRuleMargin, clearance: float) -> None:
        """
         Sets the clearance requirement in a given direction. The value is expressed in Part Units. 
        """
        pass
    
    ##  Sets the component filter criteria for a given side of the constraint. Only applicable when @link NXOpen::PcbExchange::EntityCategory NXOpen::PcbExchange::EntityCategory@endlink  is @link NXOpen::PcbExchange::EntityCategoryComponent NXOpen::PcbExchange::EntityCategoryComponent@endlink . 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  Index of the filter. 
    def SetComponentFilter(builder: DesignRuleBuilder, filterIndex: int, componentFilter: DesignRuleBuilder.ComponentFilter) -> None:
        """
         Sets the component filter criteria for a given side of the constraint. Only applicable when @link NXOpen::PcbExchange::EntityCategory NXOpen::PcbExchange::EntityCategory@endlink  is @link NXOpen::PcbExchange::EntityCategoryComponent NXOpen::PcbExchange::EntityCategoryComponent@endlink . 
        """
        pass
    
    ##  Sets an optional conductive layer side parameter for the copper filter for a given side of the constraint. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  Index of the filter. 
    def SetConductiveLayerSide(builder: DesignRuleBuilder, filterIndex: int, side: ConductiveLayerSide) -> None:
        """
         Sets an optional conductive layer side parameter for the copper filter for a given side of the constraint. 
        """
        pass
    
    ##  Sets the entity category for a given side of the constraint. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  Index of the filter. 
    def SetEntityType(builder: DesignRuleBuilder, filterIndex: int, entityType: EntityCategory) -> None:
        """
         Sets the entity category for a given side of the constraint. 
        """
        pass
    
    ##  Sets an optional string parameter for the component filter for a given side of the constraint. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  Index of the filter. 
    @overload
    def SetFilterData(self, builder: DesignRuleBuilder, filterIndex: int, data: str) -> None:
        """
         Sets an optional string parameter for the component filter for a given side of the constraint. 
        """
        pass
    
    ##  Sets optional string parameters for the component filter for a given side of the constraint. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  Index of the filter. 
    @overload
    def SetFilterData(self, builder: DesignRuleBuilder, filterIndex: int, data: List[str]) -> None:
        """
         Sets optional string parameters for the component filter for a given side of the constraint. 
        """
        pass
    
    ##  Sets an optional wire bond side parameter for the wire bond filter for a given side of the constraint. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  Index of the filter. 
    def SetWireBondSide(builder: DesignRuleBuilder, filterIndex: int, side: WireBondSide) -> None:
        """
         Sets an optional wire bond side parameter for the wire bond filter for a given side of the constraint. 
        """
        pass
    
##  Defines the directions of a @link NXOpen::PcbExchange::DesignRuleType NXOpen::PcbExchange::DesignRuleType@endlink . 
##  The XY constraint of a @link NXOpen::PcbExchange::DesignRuleTypeOrtho NXOpen::PcbExchange::DesignRuleTypeOrtho@endlink  rule. 
class DesignRuleMargin(Enum):
    """
    Members Include: <OrthoXY> <OrthoZ> <Xyz> <LongToLong> <ShortToShort> <LongToShort> <ShortToLong> <Z>
    """
    OrthoXY: int
    OrthoZ: int
    Xyz: int
    LongToLong: int
    ShortToShort: int
    LongToShort: int
    ShortToLong: int
    Z: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DesignRuleMargin:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Defines the measurement type of a @link NXOpen::PcbExchange::DesignRule NXOpen::PcbExchange::DesignRule@endlink . 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Lightweight</term><description> 
## </description> </item><item><term> 
## Exact</term><description> 
## </description> </item></list>
class DesignRuleMeasurement(Enum):
    """
    Members Include: <Lightweight> <Exact>
    """
    Lightweight: int
    Exact: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DesignRuleMeasurement:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Defines the severity of a @link NXOpen::PcbExchange::DesignRule NXOpen::PcbExchange::DesignRule@endlink . 
##  The constraints specifies the minimum threshold. 
class DesignRuleSeverity(Enum):
    """
    Members Include: <Minimum> <Optimal>
    """
    Minimum: int
    Optimal: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DesignRuleSeverity:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Defines the type of a @link NXOpen::PcbExchange::DesignRule NXOpen::PcbExchange::DesignRule@endlink . 
##  Orthogonal check. The clearance requirement is expressed independently in the XY plane, and along the Z axis. 
class DesignRuleType(Enum):
    """
    Members Include: <Ortho> <Distance> <EdgeToEdge>
    """
    Ortho: int
    Distance: int
    EdgeToEdge: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DesignRuleType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents a Design Rule for Pcb Exchange Design Validation.  <br> To create or edit an instance of this class, use @link NXOpen::PcbExchange::DesignRuleBuilder  NXOpen::PcbExchange::DesignRuleBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class DesignRule(NXOpen.TaggedObject): 
    """ Represents a Design Rule for Pcb Exchange Design Validation. """


    ## Getter for property: (str) Name
    ##   the rule name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the rule name.  
             
         
        """
        pass
    
    ##  Decreases the rule priority. Moves the rule down in the priority ranking. Returns the rule that was immediately below it, or NULL if the rule is already in last place. 
    ##  @return otherRule (@link DesignRule NXOpen.PcbExchange.DesignRule@endlink):  Rule substituted with. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def DecreasePriority(rule: DesignRule) -> DesignRule:
        """
         Decreases the rule priority. Moves the rule down in the priority ranking. Returns the rule that was immediately below it, or NULL if the rule is already in last place. 
         @return otherRule (@link DesignRule NXOpen.PcbExchange.DesignRule@endlink):  Rule substituted with. .
        """
        pass
    
    ##  Deletes the rule. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def Destroy(rule: DesignRule) -> None:
        """
         Deletes the rule. 
        """
        pass
    
    ##  Increases the rule priority. Moves the rule up in the priority ranking. Returns the rule that was immediately above it, or NULL if the rule is already in first place. 
    ##  @return otherRule (@link DesignRule NXOpen.PcbExchange.DesignRule@endlink):  Rule substituted with. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def IncreasePriority(rule: DesignRule) -> DesignRule:
        """
         Increases the rule priority. Moves the rule up in the priority ranking. Returns the rule that was immediately above it, or NULL if the rule is already in first place. 
         @return otherRule (@link DesignRule NXOpen.PcbExchange.DesignRule@endlink):  Rule substituted with. .
        """
        pass
    
import NXOpen
##  Performs validation of Pcb Exchange design.  <br> Use @link NXOpen::PcbExchange::Manager NXOpen::PcbExchange::Manager@endlink  to get an instance of this class.  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class DesignValidator(NXOpen.TransientObject): 
    """ Performs validation of Pcb Exchange design. """


    ## Getter for property: (int) InterferenceCount
    ##   the number of interferences.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return int
    @property
    def InterferenceCount(self) -> int:
        """
        Getter for property: (int) InterferenceCount
          the number of interferences.  
             
         
        """
        pass
    
    ##  Disposes of this instance. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(builder: DesignValidator) -> None:
        """
         Disposes of this instance. 
        """
        pass
    
    ##  Exports the list of interferences to a file. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="filename"> (str) </param>
    def ExportInterferences(builder: DesignValidator, filename: str) -> None:
        """
         Exports the list of interferences to a file. 
        """
        pass
    
    ##  Gets the list of interferences. 
    ##  @return interferences (@link DesignInterference List[NXOpen.PcbExchange.DesignInterference]@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInterferences(builder: DesignValidator) -> List[DesignInterference]:
        """
         Gets the list of interferences. 
         @return interferences (@link DesignInterference List[NXOpen.PcbExchange.DesignInterference]@endlink): .
        """
        pass
    
    ##  Performs design analysis. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition")
    @staticmethod
    def PerformAnalysis(builder: DesignValidator) -> None:
        """
         Performs design analysis. 
        """
        pass
    
    ##  Clears the list of interferences and resets the analysis state. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition")
    @staticmethod
    def ResetAnalysis(builder: DesignValidator) -> None:
        """
         Clears the list of interferences and resets the analysis state. 
        """
        pass
    
import NXOpen
##  Represents a builder to export ECAD model.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateEcadExportBuilder  NXOpen::PcbExchange::Manager::CreateEcadExportBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class EcadExportBuilder(NXOpen.Builder): 
    """ Represents a builder to export ECAD model. """


    ##  The ECAD location options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Os</term><description> 
    ## </description> </item><item><term> 
    ## Tc</term><description> 
    ## </description> </item></list>
    class EcadLocationEnum(Enum):
        """
        Members Include: <Os> <Tc>
        """
        Os: int
        Tc: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EcadExportBuilder.EcadLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The file units options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Mm</term><description> 
    ## </description> </item><item><term> 
    ## Thou</term><description> 
    ## </description> </item></list>
    class ExportUnitsEnum(Enum):
        """
        Members Include: <Mm> <Thou>
        """
        Mm: int
        Thou: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EcadExportBuilder.ExportUnitsEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The file format options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Idf2</term><description> 
    ## </description> </item><item><term> 
    ## Idf3</term><description> 
    ## </description> </item><item><term> 
    ## Idf4</term><description> 
    ## </description> </item><item><term> 
    ## Zbmb</term><description> 
    ## </description> </item><item><term> 
    ## Zpcb</term><description> 
    ## </description> </item><item><term> 
    ## Idx2</term><description> 
    ## </description> </item><item><term> 
    ## Idx3</term><description> 
    ## </description> </item></list>
    class FileFormatEnum(Enum):
        """
        Members Include: <Idf2> <Idf3> <Idf4> <Zbmb> <Zpcb> <Idx2> <Idx3>
        """
        Idf2: int
        Idf3: int
        Idf4: int
        Zbmb: int
        Zpcb: int
        Idx2: int
        Idx3: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EcadExportBuilder.FileFormatEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) BoardFile
    ##   the board file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def BoardFile(self) -> str:
        """
        Getter for property: (str) BoardFile
          the board file.  
             
         
        """
        pass
    
    ## Setter for property: (str) BoardFile

    ##   the board file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BoardFile.setter
    def BoardFile(self, boardFile: str):
        """
        Setter for property: (str) BoardFile
          the board file.  
             
         
        """
        pass
    
    ## Getter for property: (bool) BoardOnly
    ##   the flag indicating whether to export only the board.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def BoardOnly(self) -> bool:
        """
        Getter for property: (bool) BoardOnly
          the flag indicating whether to export only the board.  
             
         
        """
        pass
    
    ## Setter for property: (bool) BoardOnly

    ##   the flag indicating whether to export only the board.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BoardOnly.setter
    def BoardOnly(self, boardOnly: bool):
        """
        Setter for property: (bool) BoardOnly
          the flag indicating whether to export only the board.  
             
         
        """
        pass
    
    ## Getter for property: (@link EcadExportBuilder.EcadLocationEnum NXOpen.PcbExchange.EcadExportBuilder.EcadLocationEnum@endlink) EcadLocation
    ##   the location of the ECAD file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return EcadExportBuilder.EcadLocationEnum
    @property
    def EcadLocation(self) -> EcadExportBuilder.EcadLocationEnum:
        """
        Getter for property: (@link EcadExportBuilder.EcadLocationEnum NXOpen.PcbExchange.EcadExportBuilder.EcadLocationEnum@endlink) EcadLocation
          the location of the ECAD file.  
             
         
        """
        pass
    
    ## Setter for property: (@link EcadExportBuilder.EcadLocationEnum NXOpen.PcbExchange.EcadExportBuilder.EcadLocationEnum@endlink) EcadLocation

    ##   the location of the ECAD file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EcadLocation.setter
    def EcadLocation(self, ecadLocation: EcadExportBuilder.EcadLocationEnum):
        """
        Setter for property: (@link EcadExportBuilder.EcadLocationEnum NXOpen.PcbExchange.EcadExportBuilder.EcadLocationEnum@endlink) EcadLocation
          the location of the ECAD file.  
             
         
        """
        pass
    
    ## Getter for property: (str) EcadNumber
    ##   the ECAD number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def EcadNumber(self) -> str:
        """
        Getter for property: (str) EcadNumber
          the ECAD number.  
             
         
        """
        pass
    
    ## Setter for property: (str) EcadNumber

    ##   the ECAD number.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EcadNumber.setter
    def EcadNumber(self, ecadNumber: str):
        """
        Setter for property: (str) EcadNumber
          the ECAD number.  
             
         
        """
        pass
    
    ## Getter for property: (str) EcadRevision
    ##   the ECAD revision.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def EcadRevision(self) -> str:
        """
        Getter for property: (str) EcadRevision
          the ECAD revision.  
             
         
        """
        pass
    
    ## Setter for property: (str) EcadRevision

    ##   the ECAD revision.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EcadRevision.setter
    def EcadRevision(self, ecadRevision: str):
        """
        Setter for property: (str) EcadRevision
          the ECAD revision.  
             
         
        """
        pass
    
    ## Getter for property: (@link EcadExportBuilder.FileFormatEnum NXOpen.PcbExchange.EcadExportBuilder.FileFormatEnum@endlink) FileFormat
    ##   the file format.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return EcadExportBuilder.FileFormatEnum
    @property
    def FileFormat(self) -> EcadExportBuilder.FileFormatEnum:
        """
        Getter for property: (@link EcadExportBuilder.FileFormatEnum NXOpen.PcbExchange.EcadExportBuilder.FileFormatEnum@endlink) FileFormat
          the file format.  
             
         
        """
        pass
    
    ## Setter for property: (@link EcadExportBuilder.FileFormatEnum NXOpen.PcbExchange.EcadExportBuilder.FileFormatEnum@endlink) FileFormat

    ##   the file format.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FileFormat.setter
    def FileFormat(self, fileFormat: EcadExportBuilder.FileFormatEnum):
        """
        Setter for property: (@link EcadExportBuilder.FileFormatEnum NXOpen.PcbExchange.EcadExportBuilder.FileFormatEnum@endlink) FileFormat
          the file format.  
             
         
        """
        pass
    
    ## Getter for property: (@link EcadExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.EcadExportBuilder.ExportUnitsEnum@endlink) FileUnits
    ##   the file units.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return EcadExportBuilder.ExportUnitsEnum
    @property
    def FileUnits(self) -> EcadExportBuilder.ExportUnitsEnum:
        """
        Getter for property: (@link EcadExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.EcadExportBuilder.ExportUnitsEnum@endlink) FileUnits
          the file units.  
             
         
        """
        pass
    
    ## Setter for property: (@link EcadExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.EcadExportBuilder.ExportUnitsEnum@endlink) FileUnits

    ##   the file units.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FileUnits.setter
    def FileUnits(self, exportUnits: EcadExportBuilder.ExportUnitsEnum):
        """
        Setter for property: (@link EcadExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.EcadExportBuilder.ExportUnitsEnum@endlink) FileUnits
          the file units.  
             
         
        """
        pass
    
    ## Getter for property: (str) LibraryFile
    ##   the library file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def LibraryFile(self) -> str:
        """
        Getter for property: (str) LibraryFile
          the library file.  
             
         
        """
        pass
    
    ## Setter for property: (str) LibraryFile

    ##   the library file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @LibraryFile.setter
    def LibraryFile(self, libraryFile: str):
        """
        Setter for property: (str) LibraryFile
          the library file.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowLog
    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowLog

    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseCurrentWorkPart
    ##   the flag indicating whether to use the current work part.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def UseCurrentWorkPart(self) -> bool:
        """
        Getter for property: (bool) UseCurrentWorkPart
          the flag indicating whether to use the current work part.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseCurrentWorkPart

    ##   the flag indicating whether to use the current work part.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @UseCurrentWorkPart.setter
    def UseCurrentWorkPart(self, useCurrentWorkPart: bool):
        """
        Setter for property: (bool) UseCurrentWorkPart
          the flag indicating whether to use the current work part.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseEntityFilter
    ##   the flag indicating whether to use the entity filter.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def UseEntityFilter(self) -> bool:
        """
        Getter for property: (bool) UseEntityFilter
          the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseEntityFilter

    ##   the flag indicating whether to use the entity filter.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @UseEntityFilter.setter
    def UseEntityFilter(self, useEntityFilter: bool):
        """
        Setter for property: (bool) UseEntityFilter
          the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    
    ##  Gets the area mapping. 
    ##  @return areaMapping (@link AreaMapping NXOpen.PcbExchange.AreaMapping@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAreaMapping(builder: EcadExportBuilder) -> AreaMapping:
        """
         Gets the area mapping. 
         @return areaMapping (@link AreaMapping NXOpen.PcbExchange.AreaMapping@endlink): .
        """
        pass
    
    ##  Gets the entity filter. 
    ##  @return filter (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEntityFilter(builder: EcadExportBuilder) -> EntityFilter:
        """
         Gets the entity filter. 
         @return filter (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink): .
        """
        pass
    
    ##  Runs the pre-export ECAD hook and sets the board file, if defined. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def RunPreExportEcadHook(builder: EcadExportBuilder) -> None:
        """
         Runs the pre-export ECAD hook and sets the board file, if defined. 
        """
        pass
    
    ##  Sets the area mapping. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="areaMapping"> (@link AreaMapping NXOpen.PcbExchange.AreaMapping@endlink) </param>
    def SetAreaMapping(builder: EcadExportBuilder, areaMapping: AreaMapping) -> None:
        """
         Sets the area mapping. 
        """
        pass
    
    ##  Sets the entity filter. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="filter"> (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) </param>
    def SetEntityFilter(builder: EcadExportBuilder, filter: EntityFilter) -> None:
        """
         Sets the entity filter. 
        """
        pass
    
import NXOpen
##  Represents a builder to import ECAD model.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateEcadImportBuilder  NXOpen::PcbExchange::Manager::CreateEcadImportBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class EcadImportBuilder(NXOpen.Builder): 
    """ Represents a builder to import ECAD model. """


    ##  Defines the ECAD file location options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Os</term><description> 
    ## </description> </item><item><term> 
    ## Tc</term><description> 
    ## </description> </item></list>
    class EcadLocationEnum(Enum):
        """
        Members Include: <Os> <Tc>
        """
        Os: int
        Tc: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EcadImportBuilder.EcadLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the import option. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## BoardOnly</term><description> 
    ## </description> </item></list>
    class ImportOptionEnum(Enum):
        """
        Members Include: <All> <BoardOnly>
        """
        All: int
        BoardOnly: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EcadImportBuilder.ImportOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) BoardFile
    ##   the board file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def BoardFile(self) -> str:
        """
        Getter for property: (str) BoardFile
          the board file.  
             
         
        """
        pass
    
    ## Setter for property: (str) BoardFile

    ##   the board file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BoardFile.setter
    def BoardFile(self, boardFile: str):
        """
        Setter for property: (str) BoardFile
          the board file.  
             
         
        """
        pass
    
    ## Getter for property: (str) BoardFolder
    ##   the board folder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def BoardFolder(self) -> str:
        """
        Getter for property: (str) BoardFolder
          the board folder.  
             
         
        """
        pass
    
    ## Setter for property: (str) BoardFolder

    ##   the board folder.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BoardFolder.setter
    def BoardFolder(self, boardFolder: str):
        """
        Setter for property: (str) BoardFolder
          the board folder.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardThickness
    ##   the board thickness when the thickness is overriden.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BoardThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardThickness
          the board thickness when the thickness is overriden.  
             
         
        """
        pass
    
    ## Getter for property: (@link EcadImportBuilder.EcadLocationEnum NXOpen.PcbExchange.EcadImportBuilder.EcadLocationEnum@endlink) EcadLocation
    ##   the ECAD file location option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return EcadImportBuilder.EcadLocationEnum
    @property
    def EcadLocation(self) -> EcadImportBuilder.EcadLocationEnum:
        """
        Getter for property: (@link EcadImportBuilder.EcadLocationEnum NXOpen.PcbExchange.EcadImportBuilder.EcadLocationEnum@endlink) EcadLocation
          the ECAD file location option.  
             
         
        """
        pass
    
    ## Setter for property: (@link EcadImportBuilder.EcadLocationEnum NXOpen.PcbExchange.EcadImportBuilder.EcadLocationEnum@endlink) EcadLocation

    ##   the ECAD file location option.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EcadLocation.setter
    def EcadLocation(self, ecadLocation: EcadImportBuilder.EcadLocationEnum):
        """
        Setter for property: (@link EcadImportBuilder.EcadLocationEnum NXOpen.PcbExchange.EcadImportBuilder.EcadLocationEnum@endlink) EcadLocation
          the ECAD file location option.  
             
         
        """
        pass
    
    ## Getter for property: (str) EcadNumber
    ##   the ECAD number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def EcadNumber(self) -> str:
        """
        Getter for property: (str) EcadNumber
          the ECAD number.  
             
         
        """
        pass
    
    ## Setter for property: (str) EcadNumber

    ##   the ECAD number.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EcadNumber.setter
    def EcadNumber(self, ecadNumber: str):
        """
        Setter for property: (str) EcadNumber
          the ECAD number.  
             
         
        """
        pass
    
    ## Getter for property: (str) EcadRevision
    ##   the ECAD revision.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def EcadRevision(self) -> str:
        """
        Getter for property: (str) EcadRevision
          the ECAD revision.  
             
         
        """
        pass
    
    ## Setter for property: (str) EcadRevision

    ##   the ECAD revision.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EcadRevision.setter
    def EcadRevision(self, ecadRevision: str):
        """
        Setter for property: (str) EcadRevision
          the ECAD revision.  
             
         
        """
        pass
    
    ## Getter for property: (@link EcadImportBuilder.ImportOptionEnum NXOpen.PcbExchange.EcadImportBuilder.ImportOptionEnum@endlink) ImportOption
    ##   the import option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return EcadImportBuilder.ImportOptionEnum
    @property
    def ImportOption(self) -> EcadImportBuilder.ImportOptionEnum:
        """
        Getter for property: (@link EcadImportBuilder.ImportOptionEnum NXOpen.PcbExchange.EcadImportBuilder.ImportOptionEnum@endlink) ImportOption
          the import option.  
             
         
        """
        pass
    
    ## Setter for property: (@link EcadImportBuilder.ImportOptionEnum NXOpen.PcbExchange.EcadImportBuilder.ImportOptionEnum@endlink) ImportOption

    ##   the import option.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ImportOption.setter
    def ImportOption(self, importOption: EcadImportBuilder.ImportOptionEnum):
        """
        Setter for property: (@link EcadImportBuilder.ImportOptionEnum NXOpen.PcbExchange.EcadImportBuilder.ImportOptionEnum@endlink) ImportOption
          the import option.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsOdbFolder
    ##   the flag indicating whether the input is from an ODB folder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def IsOdbFolder(self) -> bool:
        """
        Getter for property: (bool) IsOdbFolder
          the flag indicating whether the input is from an ODB folder.  
             
         
        """
        pass
    
    ## Setter for property: (bool) IsOdbFolder

    ##   the flag indicating whether the input is from an ODB folder.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @IsOdbFolder.setter
    def IsOdbFolder(self, isOdbFolder: bool):
        """
        Setter for property: (bool) IsOdbFolder
          the flag indicating whether the input is from an ODB folder.  
             
         
        """
        pass
    
    ## Getter for property: (str) LibraryFile
    ##   the library file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def LibraryFile(self) -> str:
        """
        Getter for property: (str) LibraryFile
          the library file.  
             
         
        """
        pass
    
    ## Setter for property: (str) LibraryFile

    ##   the library file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @LibraryFile.setter
    def LibraryFile(self, libraryFile: str):
        """
        Setter for property: (str) LibraryFile
          the library file.  
             
         
        """
        pass
    
    ## Getter for property: (bool) OnlyUseExistingComponents
    ##   the flag indicating whether to only use existing components.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def OnlyUseExistingComponents(self) -> bool:
        """
        Getter for property: (bool) OnlyUseExistingComponents
          the flag indicating whether to only use existing components.  
             
         
        """
        pass
    
    ## Setter for property: (bool) OnlyUseExistingComponents

    ##   the flag indicating whether to only use existing components.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @OnlyUseExistingComponents.setter
    def OnlyUseExistingComponents(self, onlyUseExistingComp: bool):
        """
        Setter for property: (bool) OnlyUseExistingComponents
          the flag indicating whether to only use existing components.  
             
         
        """
        pass
    
    ## Getter for property: (str) OutputPart
    ##   the output part.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def OutputPart(self) -> str:
        """
        Getter for property: (str) OutputPart
          the output part.  
             
         
        """
        pass
    
    ## Setter for property: (str) OutputPart

    ##   the output part.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @OutputPart.setter
    def OutputPart(self, outputPart: str):
        """
        Setter for property: (str) OutputPart
          the output part.  
             
         
        """
        pass
    
    ## Getter for property: (bool) OverrideBoardThickness
    ##   the flag indicating whether to override the board thickness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def OverrideBoardThickness(self) -> bool:
        """
        Getter for property: (bool) OverrideBoardThickness
          the flag indicating whether to override the board thickness.  
             
         
        """
        pass
    
    ## Setter for property: (bool) OverrideBoardThickness

    ##   the flag indicating whether to override the board thickness.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @OverrideBoardThickness.setter
    def OverrideBoardThickness(self, overrideBoardThickness: bool):
        """
        Setter for property: (bool) OverrideBoardThickness
          the flag indicating whether to override the board thickness.  
             
         
        """
        pass
    
    ## Getter for property: (str) PartName
    ##   the part name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def PartName(self) -> str:
        """
        Getter for property: (str) PartName
          the part name.  
             
         
        """
        pass
    
    ## Setter for property: (str) PartName

    ##   the part name.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PartName.setter
    def PartName(self, partName: str):
        """
        Setter for property: (str) PartName
          the part name.  
             
         
        """
        pass
    
    ## Getter for property: (str) PartNumber
    ##   the part number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def PartNumber(self) -> str:
        """
        Getter for property: (str) PartNumber
          the part number.  
             
         
        """
        pass
    
    ## Setter for property: (str) PartNumber

    ##   the part number.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PartNumber.setter
    def PartNumber(self, partNumber: str):
        """
        Setter for property: (str) PartNumber
          the part number.  
             
         
        """
        pass
    
    ## Getter for property: (str) PartRevision
    ##   the part revision.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def PartRevision(self) -> str:
        """
        Getter for property: (str) PartRevision
          the part revision.  
             
         
        """
        pass
    
    ## Setter for property: (str) PartRevision

    ##   the part revision.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PartRevision.setter
    def PartRevision(self, partRevision: str):
        """
        Setter for property: (str) PartRevision
          the part revision.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowLog
    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowLog

    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseCurrentWorkPart
    ##   the flag indicating whether to use the current work part.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def UseCurrentWorkPart(self) -> bool:
        """
        Getter for property: (bool) UseCurrentWorkPart
          the flag indicating whether to use the current work part.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseCurrentWorkPart

    ##   the flag indicating whether to use the current work part.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @UseCurrentWorkPart.setter
    def UseCurrentWorkPart(self, useCurrentWorkPart: bool):
        """
        Setter for property: (bool) UseCurrentWorkPart
          the flag indicating whether to use the current work part.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseEntityFilter
    ##   the flag indicating whether to use the entity filter.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def UseEntityFilter(self) -> bool:
        """
        Getter for property: (bool) UseEntityFilter
          the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseEntityFilter

    ##   the flag indicating whether to use the entity filter.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @UseEntityFilter.setter
    def UseEntityFilter(self, useEntityFilter: bool):
        """
        Setter for property: (bool) UseEntityFilter
          the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    
    ##  Gets the entity filter. 
    ##  @return filter (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEntityFilter(builder: EcadImportBuilder) -> EntityFilter:
        """
         Gets the entity filter. 
         @return filter (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink): .
        """
        pass
    
    ##  Sets the entity filter. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="filter"> (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) </param>
    def SetEntityFilter(builder: EcadImportBuilder, filter: EntityFilter) -> None:
        """
         Sets the entity filter. 
        """
        pass
    
import NXOpen
##  Represents a builder to import ECAD panel.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateEcadPanelImportBuilder  NXOpen::PcbExchange::Manager::CreateEcadPanelImportBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class EcadPanelImportBuilder(NXOpen.Builder): 
    """ Represents a builder to import ECAD panel. """


    ##  The optimization method options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Pattern</term><description> 
    ## </description> </item></list>
    class OptimizationMethodOptions(Enum):
        """
        Members Include: <NotSet> <Pattern>
        """
        NotSet: int
        Pattern: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EcadPanelImportBuilder.OptimizationMethodOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the ECAD Panel file location options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Os</term><description> 
    ## </description> </item><item><term> 
    ## Tc</term><description> 
    ## </description> </item></list>
    class PanelLocationEnum(Enum):
        """
        Members Include: <Os> <Tc>
        """
        Os: int
        Tc: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EcadPanelImportBuilder.PanelLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The thieving options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Curve</term><description> 
    ## </description> </item><item><term> 
    ## SolidBody</term><description> 
    ## </description> </item></list>
    class ThievingOptions(Enum):
        """
        Members Include: <NotSet> <Curve> <SolidBody>
        """
        NotSet: int
        Curve: int
        SolidBody: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EcadPanelImportBuilder.ThievingOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) Breakaway
    ##   the flag indicating whether to create breakaway.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def Breakaway(self) -> bool:
        """
        Getter for property: (bool) Breakaway
          the flag indicating whether to create breakaway.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Breakaway

    ##   the flag indicating whether to create breakaway.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Breakaway.setter
    def Breakaway(self, breakaway: bool):
        """
        Setter for property: (bool) Breakaway
          the flag indicating whether to create breakaway.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsPanelFolder
    ##   the flag indicating whether the input is from a panel folder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def IsPanelFolder(self) -> bool:
        """
        Getter for property: (bool) IsPanelFolder
          the flag indicating whether the input is from a panel folder.  
             
         
        """
        pass
    
    ## Setter for property: (bool) IsPanelFolder

    ##   the flag indicating whether the input is from a panel folder.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @IsPanelFolder.setter
    def IsPanelFolder(self, isPanelFolder: bool):
        """
        Setter for property: (bool) IsPanelFolder
          the flag indicating whether the input is from a panel folder.  
             
         
        """
        pass
    
    ## Getter for property: (@link EcadPanelImportBuilder.OptimizationMethodOptions NXOpen.PcbExchange.EcadPanelImportBuilder.OptimizationMethodOptions@endlink) OptimizationMethod
    ##   the optimization method option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return EcadPanelImportBuilder.OptimizationMethodOptions
    @property
    def OptimizationMethod(self) -> EcadPanelImportBuilder.OptimizationMethodOptions:
        """
        Getter for property: (@link EcadPanelImportBuilder.OptimizationMethodOptions NXOpen.PcbExchange.EcadPanelImportBuilder.OptimizationMethodOptions@endlink) OptimizationMethod
          the optimization method option.  
             
         
        """
        pass
    
    ## Setter for property: (@link EcadPanelImportBuilder.OptimizationMethodOptions NXOpen.PcbExchange.EcadPanelImportBuilder.OptimizationMethodOptions@endlink) OptimizationMethod

    ##   the optimization method option.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OptimizationMethod.setter
    def OptimizationMethod(self, optimizationMethod: EcadPanelImportBuilder.OptimizationMethodOptions):
        """
        Setter for property: (@link EcadPanelImportBuilder.OptimizationMethodOptions NXOpen.PcbExchange.EcadPanelImportBuilder.OptimizationMethodOptions@endlink) OptimizationMethod
          the optimization method option.  
             
         
        """
        pass
    
    ## Getter for property: (str) PanelFile
    ##   the panel file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def PanelFile(self) -> str:
        """
        Getter for property: (str) PanelFile
          the panel file.  
             
         
        """
        pass
    
    ## Setter for property: (str) PanelFile

    ##   the panel file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @PanelFile.setter
    def PanelFile(self, panelFile: str):
        """
        Setter for property: (str) PanelFile
          the panel file.  
             
         
        """
        pass
    
    ## Getter for property: (str) PanelFolder
    ##   the panel folder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def PanelFolder(self) -> str:
        """
        Getter for property: (str) PanelFolder
          the panel folder.  
             
         
        """
        pass
    
    ## Setter for property: (str) PanelFolder

    ##   the panel folder.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PanelFolder.setter
    def PanelFolder(self, panelFolder: str):
        """
        Setter for property: (str) PanelFolder
          the panel folder.  
             
         
        """
        pass
    
    ## Getter for property: (@link EcadPanelImportBuilder.PanelLocationEnum NXOpen.PcbExchange.EcadPanelImportBuilder.PanelLocationEnum@endlink) PanelLocation
    ##   the ECAD Panel file location option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return EcadPanelImportBuilder.PanelLocationEnum
    @property
    def PanelLocation(self) -> EcadPanelImportBuilder.PanelLocationEnum:
        """
        Getter for property: (@link EcadPanelImportBuilder.PanelLocationEnum NXOpen.PcbExchange.EcadPanelImportBuilder.PanelLocationEnum@endlink) PanelLocation
          the ECAD Panel file location option.  
             
         
        """
        pass
    
    ## Setter for property: (@link EcadPanelImportBuilder.PanelLocationEnum NXOpen.PcbExchange.EcadPanelImportBuilder.PanelLocationEnum@endlink) PanelLocation

    ##   the ECAD Panel file location option.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @PanelLocation.setter
    def PanelLocation(self, panelLocation: EcadPanelImportBuilder.PanelLocationEnum):
        """
        Setter for property: (@link EcadPanelImportBuilder.PanelLocationEnum NXOpen.PcbExchange.EcadPanelImportBuilder.PanelLocationEnum@endlink) PanelLocation
          the ECAD Panel file location option.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowLog
    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowLog

    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ## Getter for property: (bool) SolderMasks
    ##   the flag indicating whether to create solder masks.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def SolderMasks(self) -> bool:
        """
        Getter for property: (bool) SolderMasks
          the flag indicating whether to create solder masks.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SolderMasks

    ##   the flag indicating whether to create solder masks.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SolderMasks.setter
    def SolderMasks(self, solderMasks: bool):
        """
        Setter for property: (bool) SolderMasks
          the flag indicating whether to create solder masks.  
             
         
        """
        pass
    
    ## Getter for property: (str) TcItemNumber
    ##   the ECAD number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def TcItemNumber(self) -> str:
        """
        Getter for property: (str) TcItemNumber
          the ECAD number.  
             
         
        """
        pass
    
    ## Setter for property: (str) TcItemNumber

    ##   the ECAD number.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @TcItemNumber.setter
    def TcItemNumber(self, tcItemNumber: str):
        """
        Setter for property: (str) TcItemNumber
          the ECAD number.  
             
         
        """
        pass
    
    ## Getter for property: (str) TcItemRevision
    ##   the ECAD revision.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def TcItemRevision(self) -> str:
        """
        Getter for property: (str) TcItemRevision
          the ECAD revision.  
             
         
        """
        pass
    
    ## Setter for property: (str) TcItemRevision

    ##   the ECAD revision.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @TcItemRevision.setter
    def TcItemRevision(self, tcItemRevision: str):
        """
        Setter for property: (str) TcItemRevision
          the ECAD revision.  
             
         
        """
        pass
    
    ## Getter for property: (@link EcadPanelImportBuilder.ThievingOptions NXOpen.PcbExchange.EcadPanelImportBuilder.ThievingOptions@endlink) Thieving
    ##   the thieving creation option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return EcadPanelImportBuilder.ThievingOptions
    @property
    def Thieving(self) -> EcadPanelImportBuilder.ThievingOptions:
        """
        Getter for property: (@link EcadPanelImportBuilder.ThievingOptions NXOpen.PcbExchange.EcadPanelImportBuilder.ThievingOptions@endlink) Thieving
          the thieving creation option.  
             
         
        """
        pass
    
    ## Setter for property: (@link EcadPanelImportBuilder.ThievingOptions NXOpen.PcbExchange.EcadPanelImportBuilder.ThievingOptions@endlink) Thieving

    ##   the thieving creation option.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Thieving.setter
    def Thieving(self, thieving: EcadPanelImportBuilder.ThievingOptions):
        """
        Setter for property: (@link EcadPanelImportBuilder.ThievingOptions NXOpen.PcbExchange.EcadPanelImportBuilder.ThievingOptions@endlink) Thieving
          the thieving creation option.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseCurrentWorkPart
    ##   the flag indicating whether to use the current work part.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def UseCurrentWorkPart(self) -> bool:
        """
        Getter for property: (bool) UseCurrentWorkPart
          the flag indicating whether to use the current work part.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseCurrentWorkPart

    ##   the flag indicating whether to use the current work part.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @UseCurrentWorkPart.setter
    def UseCurrentWorkPart(self, useCurrentWorkPart: bool):
        """
        Setter for property: (bool) UseCurrentWorkPart
          the flag indicating whether to use the current work part.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseEntityFilter
    ##   the flag indicating whether to use the entity filter.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def UseEntityFilter(self) -> bool:
        """
        Getter for property: (bool) UseEntityFilter
          the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseEntityFilter

    ##   the flag indicating whether to use the entity filter.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @UseEntityFilter.setter
    def UseEntityFilter(self, useEntityFilter: bool):
        """
        Setter for property: (bool) UseEntityFilter
          the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    
    ##  Gets the entity filter. 
    ##  @return filter (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEntityFilter(builder: EcadPanelImportBuilder) -> EntityFilter:
        """
         Gets the entity filter. 
         @return filter (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink): .
        """
        pass
    
    ##  Gets the output names. 
    ##  @return outputsNames (List[str]):  Outputs names list .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetOutputNames(builder: EcadPanelImportBuilder) -> List[str]:
        """
         Gets the output names. 
         @return outputsNames (List[str]):  Outputs names list .
        """
        pass
    
    ##  Gets the output parts. 
    ##  @return outputsParts (List[str]):  Outputs parts list .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetOutputParts(builder: EcadPanelImportBuilder) -> List[str]:
        """
         Gets the output parts. 
         @return outputsParts (List[str]):  Outputs parts list .
        """
        pass
    
    ##  Create temporary folder of ODB Panel data from TGZ-file, in managed mode it it is required import data from Item Revision. 
    ##  @return folderName (str): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def PrepareOdbFolder(builder: EcadPanelImportBuilder) -> str:
        """
         Create temporary folder of ODB Panel data from TGZ-file, in managed mode it it is required import data from Item Revision. 
         @return folderName (str): .
        """
        pass
    
    ##  Sets the entity filter. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="filter"> (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) </param>
    def SetEntityFilter(builder: EcadPanelImportBuilder, filter: EntityFilter) -> None:
        """
         Sets the entity filter. 
        """
        pass
    
    ##  Sets the output names. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  Outputs names list 
    def SetOutputNames(builder: EcadPanelImportBuilder, outputsNames: List[str]) -> None:
        """
         Sets the output names. 
        """
        pass
    
    ##  Sets the output parts. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  Outputs parts list 
    def SetOutputParts(builder: EcadPanelImportBuilder, outputsParts: List[str]) -> None:
        """
         Sets the output parts. 
        """
        pass
    
##  Defines a category of Pcb Exchange entity. 
##  Entity is a Component. 
class EntityCategory(Enum):
    """
    Members Include: <Component> <Board> <Mechanical> <KeepOut> <Copper> <WireBond> <CopperArea>
    """
    Component: int
    Board: int
    Mechanical: int
    KeepOut: int
    Copper: int
    WireBond: int
    CopperArea: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> EntityCategory:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents a builder to create or edit @link NXOpen::PcbExchange::EntityFilter NXOpen::PcbExchange::EntityFilter@endlink .  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateEntityFilterBuilder  NXOpen::PcbExchange::Manager::CreateEntityFilterBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ComponentMaxHeight </term> <description> 
##  
## 999 </description> </item> 
## 
## <item><term> 
##  
## ComponentMaxSize </term> <description> 
##  
## 999 </description> </item> 
## 
## <item><term> 
##  
## ComponentMinHeight </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ComponentMinSize </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## HoleMaxDiameter </term> <description> 
##  
## 999 </description> </item> 
## 
## <item><term> 
##  
## HoleMaxSize </term> <description> 
##  
## 999 </description> </item> 
## 
## <item><term> 
##  
## HoleMinDiameter </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## HoleMinSize </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## LengthUnits </term> <description> 
##  
## Millimeters </description> </item> 
## 
## <item><term> 
##  
## RemoveBlindBuriedViaHoles </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveComponentsWithHeight </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveComponentsWithSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveEcadComponents </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveHolesWithDiameter </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveHolesWithSize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveMcadComponents </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveMountingHoles </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveOtherHoles </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveOtherKeepoutAreas </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemovePinHoles </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemovePlacedComponents </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemovePlacementGroupKeepinAreas </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemovePlacementKeepinAreas </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemovePlacementKeepoutAreas </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveRoutingKeepinAreas </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveRoutingKeepoutAreas </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveToolingHoles </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveUnplacedComponents </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveViaHoles </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RemoveViaKeepoutAreas </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class EntityFilterBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit <ja_class>NXOpen.PcbExchange.EntityFilter</ja_class>. """


    ##  The length unit options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Millimeters</term><description> 
    ## </description> </item><item><term> 
    ## Inches</term><description> 
    ## </description> </item></list>
    class LengthUnitsEnum(Enum):
        """
        Members Include: <Millimeters> <Inches>
        """
        Millimeters: int
        Inches: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EntityFilterBuilder.LengthUnitsEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) ComponentMaxHeight
    ##   the maximum component height.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def ComponentMaxHeight(self) -> float:
        """
        Getter for property: (float) ComponentMaxHeight
          the maximum component height.  
             
         
        """
        pass
    
    ## Setter for property: (float) ComponentMaxHeight

    ##   the maximum component height.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ComponentMaxHeight.setter
    def ComponentMaxHeight(self, componentMaxHeight: float):
        """
        Setter for property: (float) ComponentMaxHeight
          the maximum component height.  
             
         
        """
        pass
    
    ## Getter for property: (float) ComponentMaxSize
    ##   the maximum component size.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def ComponentMaxSize(self) -> float:
        """
        Getter for property: (float) ComponentMaxSize
          the maximum component size.  
             
         
        """
        pass
    
    ## Setter for property: (float) ComponentMaxSize

    ##   the maximum component size.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ComponentMaxSize.setter
    def ComponentMaxSize(self, componentMaxSize: float):
        """
        Setter for property: (float) ComponentMaxSize
          the maximum component size.  
             
         
        """
        pass
    
    ## Getter for property: (float) ComponentMinHeight
    ##   the minimum component height.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def ComponentMinHeight(self) -> float:
        """
        Getter for property: (float) ComponentMinHeight
          the minimum component height.  
             
         
        """
        pass
    
    ## Setter for property: (float) ComponentMinHeight

    ##   the minimum component height.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ComponentMinHeight.setter
    def ComponentMinHeight(self, componentMinHeight: float):
        """
        Setter for property: (float) ComponentMinHeight
          the minimum component height.  
             
         
        """
        pass
    
    ## Getter for property: (float) ComponentMinSize
    ##   the minimum component size.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def ComponentMinSize(self) -> float:
        """
        Getter for property: (float) ComponentMinSize
          the minimum component size.  
             
         
        """
        pass
    
    ## Setter for property: (float) ComponentMinSize

    ##   the minimum component size.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ComponentMinSize.setter
    def ComponentMinSize(self, componentMinSize: float):
        """
        Setter for property: (float) ComponentMinSize
          the minimum component size.  
             
         
        """
        pass
    
    ## Getter for property: (float) HoleMaxDiameter
    ##   the maximum hole diameter.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def HoleMaxDiameter(self) -> float:
        """
        Getter for property: (float) HoleMaxDiameter
          the maximum hole diameter.  
             
         
        """
        pass
    
    ## Setter for property: (float) HoleMaxDiameter

    ##   the maximum hole diameter.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @HoleMaxDiameter.setter
    def HoleMaxDiameter(self, holeMaxDiameter: float):
        """
        Setter for property: (float) HoleMaxDiameter
          the maximum hole diameter.  
             
         
        """
        pass
    
    ## Getter for property: (float) HoleMaxSize
    ##   the maximum hole size.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def HoleMaxSize(self) -> float:
        """
        Getter for property: (float) HoleMaxSize
          the maximum hole size.  
             
         
        """
        pass
    
    ## Setter for property: (float) HoleMaxSize

    ##   the maximum hole size.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @HoleMaxSize.setter
    def HoleMaxSize(self, holeMaxSize: float):
        """
        Setter for property: (float) HoleMaxSize
          the maximum hole size.  
             
         
        """
        pass
    
    ## Getter for property: (float) HoleMinDiameter
    ##   the minimum hole diameter.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def HoleMinDiameter(self) -> float:
        """
        Getter for property: (float) HoleMinDiameter
          the minimum hole diameter.  
             
         
        """
        pass
    
    ## Setter for property: (float) HoleMinDiameter

    ##   the minimum hole diameter.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @HoleMinDiameter.setter
    def HoleMinDiameter(self, holeMinDiameter: float):
        """
        Setter for property: (float) HoleMinDiameter
          the minimum hole diameter.  
             
         
        """
        pass
    
    ## Getter for property: (float) HoleMinSize
    ##   the minimum hole size.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def HoleMinSize(self) -> float:
        """
        Getter for property: (float) HoleMinSize
          the minimum hole size.  
             
         
        """
        pass
    
    ## Setter for property: (float) HoleMinSize

    ##   the minimum hole size.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @HoleMinSize.setter
    def HoleMinSize(self, holeMinSize: float):
        """
        Setter for property: (float) HoleMinSize
          the minimum hole size.  
             
         
        """
        pass
    
    ## Getter for property: (@link EntityFilterBuilder.LengthUnitsEnum NXOpen.PcbExchange.EntityFilterBuilder.LengthUnitsEnum@endlink) LengthUnits
    ##   the length units.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return EntityFilterBuilder.LengthUnitsEnum
    @property
    def LengthUnits(self) -> EntityFilterBuilder.LengthUnitsEnum:
        """
        Getter for property: (@link EntityFilterBuilder.LengthUnitsEnum NXOpen.PcbExchange.EntityFilterBuilder.LengthUnitsEnum@endlink) LengthUnits
          the length units.  
             
         
        """
        pass
    
    ## Setter for property: (@link EntityFilterBuilder.LengthUnitsEnum NXOpen.PcbExchange.EntityFilterBuilder.LengthUnitsEnum@endlink) LengthUnits

    ##   the length units.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @LengthUnits.setter
    def LengthUnits(self, lengthUnits: EntityFilterBuilder.LengthUnitsEnum):
        """
        Setter for property: (@link EntityFilterBuilder.LengthUnitsEnum NXOpen.PcbExchange.EntityFilterBuilder.LengthUnitsEnum@endlink) LengthUnits
          the length units.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveBlindBuriedViaHoles
    ##   the flag indicating whether to remove blind buried via holes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveBlindBuriedViaHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveBlindBuriedViaHoles
          the flag indicating whether to remove blind buried via holes.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveBlindBuriedViaHoles

    ##   the flag indicating whether to remove blind buried via holes.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveBlindBuriedViaHoles.setter
    def RemoveBlindBuriedViaHoles(self, removeBlindBuriedViaHoles: bool):
        """
        Setter for property: (bool) RemoveBlindBuriedViaHoles
          the flag indicating whether to remove blind buried via holes.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveComponentsWithHeight
    ##   the flag indicating whether to remove components with a specified height.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveComponentsWithHeight(self) -> bool:
        """
        Getter for property: (bool) RemoveComponentsWithHeight
          the flag indicating whether to remove components with a specified height.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveComponentsWithHeight

    ##   the flag indicating whether to remove components with a specified height.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveComponentsWithHeight.setter
    def RemoveComponentsWithHeight(self, removeComponentsWithHeight: bool):
        """
        Setter for property: (bool) RemoveComponentsWithHeight
          the flag indicating whether to remove components with a specified height.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveComponentsWithSize
    ##   the flag indicating whether to remove components with a specified size.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveComponentsWithSize(self) -> bool:
        """
        Getter for property: (bool) RemoveComponentsWithSize
          the flag indicating whether to remove components with a specified size.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveComponentsWithSize

    ##   the flag indicating whether to remove components with a specified size.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveComponentsWithSize.setter
    def RemoveComponentsWithSize(self, removeComponentsWithSize: bool):
        """
        Setter for property: (bool) RemoveComponentsWithSize
          the flag indicating whether to remove components with a specified size.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveEcadComponents
    ##   the flag indicating whether to remove ECAD components.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveEcadComponents(self) -> bool:
        """
        Getter for property: (bool) RemoveEcadComponents
          the flag indicating whether to remove ECAD components.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveEcadComponents

    ##   the flag indicating whether to remove ECAD components.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveEcadComponents.setter
    def RemoveEcadComponents(self, removeEcadComponents: bool):
        """
        Setter for property: (bool) RemoveEcadComponents
          the flag indicating whether to remove ECAD components.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveHolesWithDiameter
    ##   the flag indicating whether to remove holes with a specified diameter.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveHolesWithDiameter(self) -> bool:
        """
        Getter for property: (bool) RemoveHolesWithDiameter
          the flag indicating whether to remove holes with a specified diameter.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveHolesWithDiameter

    ##   the flag indicating whether to remove holes with a specified diameter.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveHolesWithDiameter.setter
    def RemoveHolesWithDiameter(self, removeHolesWithDiameter: bool):
        """
        Setter for property: (bool) RemoveHolesWithDiameter
          the flag indicating whether to remove holes with a specified diameter.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveHolesWithSize
    ##   the flag indicating whether to remove holes with a specified size.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveHolesWithSize(self) -> bool:
        """
        Getter for property: (bool) RemoveHolesWithSize
          the flag indicating whether to remove holes with a specified size.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveHolesWithSize

    ##   the flag indicating whether to remove holes with a specified size.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveHolesWithSize.setter
    def RemoveHolesWithSize(self, removeHolesWithSize: bool):
        """
        Setter for property: (bool) RemoveHolesWithSize
          the flag indicating whether to remove holes with a specified size.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveMcadComponents
    ##   the flag indicating whether to remove MCAD components.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveMcadComponents(self) -> bool:
        """
        Getter for property: (bool) RemoveMcadComponents
          the flag indicating whether to remove MCAD components.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveMcadComponents

    ##   the flag indicating whether to remove MCAD components.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveMcadComponents.setter
    def RemoveMcadComponents(self, removeMcadComponents: bool):
        """
        Setter for property: (bool) RemoveMcadComponents
          the flag indicating whether to remove MCAD components.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveMountingHoles
    ##   the flag indicating whether to remove mounting holes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveMountingHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveMountingHoles
          the flag indicating whether to remove mounting holes.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveMountingHoles

    ##   the flag indicating whether to remove mounting holes.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveMountingHoles.setter
    def RemoveMountingHoles(self, removeMountingHoles: bool):
        """
        Setter for property: (bool) RemoveMountingHoles
          the flag indicating whether to remove mounting holes.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveOtherHoles
    ##   the flag indicating whether to remove other holes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveOtherHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveOtherHoles
          the flag indicating whether to remove other holes.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveOtherHoles

    ##   the flag indicating whether to remove other holes.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveOtherHoles.setter
    def RemoveOtherHoles(self, removeOtherHoles: bool):
        """
        Setter for property: (bool) RemoveOtherHoles
          the flag indicating whether to remove other holes.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveOtherKeepoutAreas
    ##   the flag indicating whether to remove other keepout areas.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveOtherKeepoutAreas(self) -> bool:
        """
        Getter for property: (bool) RemoveOtherKeepoutAreas
          the flag indicating whether to remove other keepout areas.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveOtherKeepoutAreas

    ##   the flag indicating whether to remove other keepout areas.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveOtherKeepoutAreas.setter
    def RemoveOtherKeepoutAreas(self, removeOtherKeepoutAreas: bool):
        """
        Setter for property: (bool) RemoveOtherKeepoutAreas
          the flag indicating whether to remove other keepout areas.  
             
         
        """
        pass
    
    ## Getter for property: (str) RemovePadsByPadstacks
    ##   the string indicating the padstacks, separated by commas, of the pads to remove.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def RemovePadsByPadstacks(self) -> str:
        """
        Getter for property: (str) RemovePadsByPadstacks
          the string indicating the padstacks, separated by commas, of the pads to remove.  
             
         
        """
        pass
    
    ## Setter for property: (str) RemovePadsByPadstacks

    ##   the string indicating the padstacks, separated by commas, of the pads to remove.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RemovePadsByPadstacks.setter
    def RemovePadsByPadstacks(self, removePadsByPadstacks: str):
        """
        Setter for property: (str) RemovePadsByPadstacks
          the string indicating the padstacks, separated by commas, of the pads to remove.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemovePinHoles
    ##   the flag indicating whether to remove pin holes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemovePinHoles(self) -> bool:
        """
        Getter for property: (bool) RemovePinHoles
          the flag indicating whether to remove pin holes.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemovePinHoles

    ##   the flag indicating whether to remove pin holes.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemovePinHoles.setter
    def RemovePinHoles(self, removePinHoles: bool):
        """
        Setter for property: (bool) RemovePinHoles
          the flag indicating whether to remove pin holes.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemovePlacedComponents
    ##   the flag indicating whether to remove placed components.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemovePlacedComponents(self) -> bool:
        """
        Getter for property: (bool) RemovePlacedComponents
          the flag indicating whether to remove placed components.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemovePlacedComponents

    ##   the flag indicating whether to remove placed components.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemovePlacedComponents.setter
    def RemovePlacedComponents(self, removePlacedComponents: bool):
        """
        Setter for property: (bool) RemovePlacedComponents
          the flag indicating whether to remove placed components.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemovePlacementGroupKeepinAreas
    ##   the flag indicating whether to remove placement group keepin areas.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemovePlacementGroupKeepinAreas(self) -> bool:
        """
        Getter for property: (bool) RemovePlacementGroupKeepinAreas
          the flag indicating whether to remove placement group keepin areas.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemovePlacementGroupKeepinAreas

    ##   the flag indicating whether to remove placement group keepin areas.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemovePlacementGroupKeepinAreas.setter
    def RemovePlacementGroupKeepinAreas(self, removePlacementGroupKeepinAreas: bool):
        """
        Setter for property: (bool) RemovePlacementGroupKeepinAreas
          the flag indicating whether to remove placement group keepin areas.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemovePlacementKeepinAreas
    ##   the flag indicating whether to remove placement keepin areas.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemovePlacementKeepinAreas(self) -> bool:
        """
        Getter for property: (bool) RemovePlacementKeepinAreas
          the flag indicating whether to remove placement keepin areas.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemovePlacementKeepinAreas

    ##   the flag indicating whether to remove placement keepin areas.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemovePlacementKeepinAreas.setter
    def RemovePlacementKeepinAreas(self, removePlacementKeepinAreas: bool):
        """
        Setter for property: (bool) RemovePlacementKeepinAreas
          the flag indicating whether to remove placement keepin areas.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemovePlacementKeepoutAreas
    ##   the flag indicating whether to remove placement keepout areas.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemovePlacementKeepoutAreas(self) -> bool:
        """
        Getter for property: (bool) RemovePlacementKeepoutAreas
          the flag indicating whether to remove placement keepout areas.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemovePlacementKeepoutAreas

    ##   the flag indicating whether to remove placement keepout areas.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemovePlacementKeepoutAreas.setter
    def RemovePlacementKeepoutAreas(self, removePlacementKeepoutAreas: bool):
        """
        Setter for property: (bool) RemovePlacementKeepoutAreas
          the flag indicating whether to remove placement keepout areas.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveRoutingKeepinAreas
    ##   the flag indicating whether to remove routing keepin areas.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveRoutingKeepinAreas(self) -> bool:
        """
        Getter for property: (bool) RemoveRoutingKeepinAreas
          the flag indicating whether to remove routing keepin areas.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveRoutingKeepinAreas

    ##   the flag indicating whether to remove routing keepin areas.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveRoutingKeepinAreas.setter
    def RemoveRoutingKeepinAreas(self, removeRoutingKeepinAreas: bool):
        """
        Setter for property: (bool) RemoveRoutingKeepinAreas
          the flag indicating whether to remove routing keepin areas.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveRoutingKeepoutAreas
    ##   the flag indicating whether to remove routing keepout areas.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveRoutingKeepoutAreas(self) -> bool:
        """
        Getter for property: (bool) RemoveRoutingKeepoutAreas
          the flag indicating whether to remove routing keepout areas.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveRoutingKeepoutAreas

    ##   the flag indicating whether to remove routing keepout areas.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveRoutingKeepoutAreas.setter
    def RemoveRoutingKeepoutAreas(self, removeRoutingKeepoutAreas: bool):
        """
        Setter for property: (bool) RemoveRoutingKeepoutAreas
          the flag indicating whether to remove routing keepout areas.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveToolingHoles
    ##   the flag indicating whether to remove tooling holes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveToolingHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveToolingHoles
          the flag indicating whether to remove tooling holes.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveToolingHoles

    ##   the flag indicating whether to remove tooling holes.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveToolingHoles.setter
    def RemoveToolingHoles(self, removeToolingHoles: bool):
        """
        Setter for property: (bool) RemoveToolingHoles
          the flag indicating whether to remove tooling holes.  
             
         
        """
        pass
    
    ## Getter for property: (str) RemoveTracesAndPadsByNetNames
    ##   the string indicating the net names, separated by commas, of the traces and pads to remove.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def RemoveTracesAndPadsByNetNames(self) -> str:
        """
        Getter for property: (str) RemoveTracesAndPadsByNetNames
          the string indicating the net names, separated by commas, of the traces and pads to remove.  
             
         
        """
        pass
    
    ## Setter for property: (str) RemoveTracesAndPadsByNetNames

    ##   the string indicating the net names, separated by commas, of the traces and pads to remove.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RemoveTracesAndPadsByNetNames.setter
    def RemoveTracesAndPadsByNetNames(self, removeTracesAndPadsByNetNames: str):
        """
        Setter for property: (str) RemoveTracesAndPadsByNetNames
          the string indicating the net names, separated by commas, of the traces and pads to remove.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveUnconnectedPads
    ##   the flag indicating whether to remove pads that are not connected to any components.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def RemoveUnconnectedPads(self) -> bool:
        """
        Getter for property: (bool) RemoveUnconnectedPads
          the flag indicating whether to remove pads that are not connected to any components.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveUnconnectedPads

    ##   the flag indicating whether to remove pads that are not connected to any components.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RemoveUnconnectedPads.setter
    def RemoveUnconnectedPads(self, removeUnconnectedPads: bool):
        """
        Setter for property: (bool) RemoveUnconnectedPads
          the flag indicating whether to remove pads that are not connected to any components.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveUnplacedComponents
    ##   the flag indicating whether to remove unplaced components.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveUnplacedComponents(self) -> bool:
        """
        Getter for property: (bool) RemoveUnplacedComponents
          the flag indicating whether to remove unplaced components.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveUnplacedComponents

    ##   the flag indicating whether to remove unplaced components.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveUnplacedComponents.setter
    def RemoveUnplacedComponents(self, removeUnplacedComponents: bool):
        """
        Setter for property: (bool) RemoveUnplacedComponents
          the flag indicating whether to remove unplaced components.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveViaHoles
    ##   the flag indicating whether to remove via holes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveViaHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveViaHoles
          the flag indicating whether to remove via holes.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveViaHoles

    ##   the flag indicating whether to remove via holes.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveViaHoles.setter
    def RemoveViaHoles(self, removeViaHoles: bool):
        """
        Setter for property: (bool) RemoveViaHoles
          the flag indicating whether to remove via holes.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RemoveViaKeepoutAreas
    ##   the flag indicating whether to remove via keepout areas.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RemoveViaKeepoutAreas(self) -> bool:
        """
        Getter for property: (bool) RemoveViaKeepoutAreas
          the flag indicating whether to remove via keepout areas.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RemoveViaKeepoutAreas

    ##   the flag indicating whether to remove via keepout areas.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RemoveViaKeepoutAreas.setter
    def RemoveViaKeepoutAreas(self, removeViaKeepoutAreas: bool):
        """
        Setter for property: (bool) RemoveViaKeepoutAreas
          the flag indicating whether to remove via keepout areas.  
             
         
        """
        pass
    
    ##  Sets user-defined filters. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="filters"> (List[str]) </param>
    def SetUserDefiniedFilters(builder: EntityFilterBuilder, filters: List[str]) -> None:
        """
         Sets user-defined filters. 
        """
        pass
    
import NXOpen
##  Represents a entity filter for PCB exchange.  <br> To create or edit an instance of this class, use @link NXOpen::PcbExchange::EntityFilterBuilder  NXOpen::PcbExchange::EntityFilterBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class EntityFilter(NXOpen.NXObject): 
    """ Represents a entity filter for PCB exchange. """
    pass


import NXOpen
##  Represents a builder to read the external data and update the model.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ExtdataUpdator(NXOpen.Object): 
    """ Represents a builder to read the external data and update the model. """


    ##  Reads the external data. 
    ##  @return A tuple consisting of (netNames, layerNames). 
    ##  - netNames is: List[str].
    ##  - layerNames is: List[str].

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="fName"> (str) </param>
    @staticmethod
    def Read(fName: str) -> Tuple[List[str], List[str]]:
        """
         Reads the external data. 
         @return A tuple consisting of (netNames, layerNames). 
         - netNames is: List[str].
         - layerNames is: List[str].

        """
        pass
    
    ##  Updates the external data. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="fName"> (str) </param>
    ## <param name="layerNames"> (List[str]) </param>
    ## <param name="netNames"> (List[str]) </param>
    ## <param name="bTextualFilter"> (bool) </param>
    ## <param name="textualFilterStr"> (str) </param>
    def Update(fName: str, layerNames: List[str], netNames: List[str], bTextualFilter: bool, textualFilterStr: str) -> None:
        """
         Updates the external data. 
        """
        pass
    
import NXOpen
##  Represents a builder to import external ECAD entities.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateExternalDataImportBuilder  NXOpen::PcbExchange::Manager::CreateExternalDataImportBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class ExternalDataImportBuilder(NXOpen.Builder): 
    """ Represents a builder to import external ECAD entities. """


    ##  Options for filtering entities to import. 
    ##  Import. 
    class JaPcbExternalDataImportBuilderImportoption(Enum):
        """
        Members Include: <Import> <DoNotImport>
        """
        Import: int
        DoNotImport: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Filename
    ##   the ECAD filename to import.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def Filename(self) -> str:
        """
        Getter for property: (str) Filename
          the ECAD filename to import.  
             
         
        """
        pass
    
    ## Setter for property: (str) Filename

    ##   the ECAD filename to import.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Filename.setter
    def Filename(self, filename: str):
        """
        Setter for property: (str) Filename
          the ECAD filename to import.  
             
         
        """
        pass
    
    ## Getter for property: (str) NetsFilterString
    ##   the comma-separated list of values for filtering nets.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def NetsFilterString(self) -> str:
        """
        Getter for property: (str) NetsFilterString
          the comma-separated list of values for filtering nets.  
             
         
        """
        pass
    
    ## Setter for property: (str) NetsFilterString

    ##   the comma-separated list of values for filtering nets.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @NetsFilterString.setter
    def NetsFilterString(self, filter: str):
        """
        Setter for property: (str) NetsFilterString
          the comma-separated list of values for filtering nets.  
             
         
        """
        pass
    
    ## Getter for property: (bool) NetsFilterStringEnabled
    ##   the flag indicating whether the filter string for nets is enabled.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def NetsFilterStringEnabled(self) -> bool:
        """
        Getter for property: (bool) NetsFilterStringEnabled
          the flag indicating whether the filter string for nets is enabled.  
             
         
        """
        pass
    
    ## Setter for property: (bool) NetsFilterStringEnabled

    ##   the flag indicating whether the filter string for nets is enabled.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @NetsFilterStringEnabled.setter
    def NetsFilterStringEnabled(self, enabled: bool):
        """
        Setter for property: (bool) NetsFilterStringEnabled
          the flag indicating whether the filter string for nets is enabled.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowLog
    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowLog

    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ##  Returns whether the layer should be imported. 
    ##  @return importOption (@link ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption NXOpen.PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption@endlink):  Import option. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Layer name. 
    def GetLayerImported(builder: ExternalDataImportBuilder, name: str) -> ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption:
        """
         Returns whether the layer should be imported. 
         @return importOption (@link ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption NXOpen.PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption@endlink):  Import option. .
        """
        pass
    
    ##  Returns the layer names. 
    ##  @return names (List[str]):  Layer names. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLayerNames(builder: ExternalDataImportBuilder) -> List[str]:
        """
         Returns the layer names. 
         @return names (List[str]):  Layer names. .
        """
        pass
    
    ##  Returns whether the net should be imported. 
    ##  @return importOption (@link ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption NXOpen.PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption@endlink):  Import option. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Net name. 
    def GetNetImported(builder: ExternalDataImportBuilder, name: str) -> ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption:
        """
         Returns whether the net should be imported. 
         @return importOption (@link ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption NXOpen.PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption@endlink):  Import option. .
        """
        pass
    
    ##  Returns the net names. 
    ##  @return names (List[str]):  Net names. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNetNames(builder: ExternalDataImportBuilder) -> List[str]:
        """
         Returns the net names. 
         @return names (List[str]):  Net names. .
        """
        pass
    
    ##  Returns whether the padstack should be imported. 
    ##  @return importOption (@link ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption NXOpen.PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption@endlink):  Import option. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Padstack name. 
    def GetPadstackImported(builder: ExternalDataImportBuilder, name: str) -> ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption:
        """
         Returns whether the padstack should be imported. 
         @return importOption (@link ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption NXOpen.PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption@endlink):  Import option. .
        """
        pass
    
    ##  Returns the padstack names. 
    ##  @return names (List[str]):  Padstack names. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPadstackNames(builder: ExternalDataImportBuilder) -> List[str]:
        """
         Returns the padstack names. 
         @return names (List[str]):  Padstack names. .
        """
        pass
    
    ##  Returns the part used to model pads in the padstack. 
    ##  @return part (str):  Part file. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Padstack name. 
    def GetPadstackPart(builder: ExternalDataImportBuilder, name: str) -> str:
        """
         Returns the part used to model pads in the padstack. 
         @return part (str):  Part file. .
        """
        pass
    
    ##  Queries the list of external entities available from the ECAD file. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def QueryEntities(builder: ExternalDataImportBuilder) -> None:
        """
         Queries the list of external entities available from the ECAD file. 
        """
        pass
    
    ##  Sets whether all layers should be imported. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  Import option. 
    def SetAllLayersImported(builder: ExternalDataImportBuilder, importOption: ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption) -> None:
        """
         Sets whether all layers should be imported. 
        """
        pass
    
    ##  Sets whether the layer should be imported. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  Layer name. 
    def SetLayerImported(builder: ExternalDataImportBuilder, name: str, importOption: ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption) -> None:
        """
         Sets whether the layer should be imported. 
        """
        pass
    
    ##  Sets whether the net should be imported. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  Net name. 
    def SetNetImported(builder: ExternalDataImportBuilder, name: str, importOption: ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption) -> None:
        """
         Sets whether the net should be imported. 
        """
        pass
    
    ##  Sets whether the padstack should be imported. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition")
    ##  Padstack name. 
    def SetPadstackImported(builder: ExternalDataImportBuilder, name: str, importOption: ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption) -> None:
        """
         Sets whether the padstack should be imported. 
        """
        pass
    
    ##  Sets the part used to model pads in the padstack. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition")
    ##  Padstack name. 
    def SetPadstackPart(builder: ExternalDataImportBuilder, name: str, part: str) -> None:
        """
         Sets the part used to model pads in the padstack. 
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a builder to create or edit hole attributes.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateHoleAttributesBuilder  NXOpen::PcbExchange::Manager::CreateHoleAttributesBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class HoleAttributesBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit hole attributes. """


    ##  The associated part options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Board</term><description> 
    ## </description> </item><item><term> 
    ## Norefdes</term><description> 
    ## </description> </item><item><term> 
    ## Specify</term><description> 
    ## </description> </item></list>
    class AssociatedPartEnum(Enum):
        """
        Members Include: <Board> <Norefdes> <Specify>
        """
        Board: int
        Norefdes: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HoleAttributesBuilder.AssociatedPartEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The owner options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Mcad</term><description> 
    ## </description> </item><item><term> 
    ## Ecad</term><description> 
    ## </description> </item><item><term> 
    ## Unowned</term><description> 
    ## </description> </item></list>
    class OwnerEnum(Enum):
        """
        Members Include: <Mcad> <Ecad> <Unowned>
        """
        Mcad: int
        Ecad: int
        Unowned: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HoleAttributesBuilder.OwnerEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The plating style options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## PlatedThru</term><description> 
    ## </description> </item><item><term> 
    ## NonPlatedThru</term><description> 
    ## </description> </item></list>
    class PlatingStyleEnum(Enum):
        """
        Members Include: <PlatedThru> <NonPlatedThru>
        """
        PlatedThru: int
        NonPlatedThru: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HoleAttributesBuilder.PlatingStyleEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The hole type options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Pin</term><description> 
    ## </description> </item><item><term> 
    ## Via</term><description> 
    ## </description> </item><item><term> 
    ## Mounting</term><description> 
    ## </description> </item><item><term> 
    ## Tool</term><description> 
    ## </description> </item><item><term> 
    ## Other</term><description> 
    ## </description> </item></list>
    class TypeEnum(Enum):
        """
        Members Include: <Pin> <Via> <Mounting> <Tool> <Other>
        """
        Pin: int
        Via: int
        Mounting: int
        Tool: int
        Other: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HoleAttributesBuilder.TypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link HoleAttributesBuilder.AssociatedPartEnum NXOpen.PcbExchange.HoleAttributesBuilder.AssociatedPartEnum@endlink) AssociatedPart
    ##   the hole associated part   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return HoleAttributesBuilder.AssociatedPartEnum
    @property
    def AssociatedPart(self) -> HoleAttributesBuilder.AssociatedPartEnum:
        """
        Getter for property: (@link HoleAttributesBuilder.AssociatedPartEnum NXOpen.PcbExchange.HoleAttributesBuilder.AssociatedPartEnum@endlink) AssociatedPart
          the hole associated part   
            
         
        """
        pass
    
    ## Setter for property: (@link HoleAttributesBuilder.AssociatedPartEnum NXOpen.PcbExchange.HoleAttributesBuilder.AssociatedPartEnum@endlink) AssociatedPart

    ##   the hole associated part   
    ##     
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AssociatedPart.setter
    def AssociatedPart(self, associatedPart: HoleAttributesBuilder.AssociatedPartEnum):
        """
        Setter for property: (@link HoleAttributesBuilder.AssociatedPartEnum NXOpen.PcbExchange.HoleAttributesBuilder.AssociatedPartEnum@endlink) AssociatedPart
          the hole associated part   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) Features
    ##   the feature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Features.SelectFeatureList
    @property
    def Features(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) Features
          the feature   
            
         
        """
        pass
    
    ## Getter for property: (@link HoleAttributesBuilder.TypeEnum NXOpen.PcbExchange.HoleAttributesBuilder.TypeEnum@endlink) HoleType
    ##   the hole type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return HoleAttributesBuilder.TypeEnum
    @property
    def HoleType(self) -> HoleAttributesBuilder.TypeEnum:
        """
        Getter for property: (@link HoleAttributesBuilder.TypeEnum NXOpen.PcbExchange.HoleAttributesBuilder.TypeEnum@endlink) HoleType
          the hole type   
            
         
        """
        pass
    
    ## Setter for property: (@link HoleAttributesBuilder.TypeEnum NXOpen.PcbExchange.HoleAttributesBuilder.TypeEnum@endlink) HoleType

    ##   the hole type   
    ##     
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @HoleType.setter
    def HoleType(self, type: HoleAttributesBuilder.TypeEnum):
        """
        Setter for property: (@link HoleAttributesBuilder.TypeEnum NXOpen.PcbExchange.HoleAttributesBuilder.TypeEnum@endlink) HoleType
          the hole type   
            
         
        """
        pass
    
    ## Getter for property: (@link HoleAttributesBuilder.OwnerEnum NXOpen.PcbExchange.HoleAttributesBuilder.OwnerEnum@endlink) Owner
    ##   the hole owner   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return HoleAttributesBuilder.OwnerEnum
    @property
    def Owner(self) -> HoleAttributesBuilder.OwnerEnum:
        """
        Getter for property: (@link HoleAttributesBuilder.OwnerEnum NXOpen.PcbExchange.HoleAttributesBuilder.OwnerEnum@endlink) Owner
          the hole owner   
            
         
        """
        pass
    
    ## Setter for property: (@link HoleAttributesBuilder.OwnerEnum NXOpen.PcbExchange.HoleAttributesBuilder.OwnerEnum@endlink) Owner

    ##   the hole owner   
    ##     
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Owner.setter
    def Owner(self, owner: HoleAttributesBuilder.OwnerEnum):
        """
        Setter for property: (@link HoleAttributesBuilder.OwnerEnum NXOpen.PcbExchange.HoleAttributesBuilder.OwnerEnum@endlink) Owner
          the hole owner   
            
         
        """
        pass
    
    ## Getter for property: (@link HoleAttributesBuilder.PlatingStyleEnum NXOpen.PcbExchange.HoleAttributesBuilder.PlatingStyleEnum@endlink) PlatingStyle
    ##   the hole plating style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return HoleAttributesBuilder.PlatingStyleEnum
    @property
    def PlatingStyle(self) -> HoleAttributesBuilder.PlatingStyleEnum:
        """
        Getter for property: (@link HoleAttributesBuilder.PlatingStyleEnum NXOpen.PcbExchange.HoleAttributesBuilder.PlatingStyleEnum@endlink) PlatingStyle
          the hole plating style   
            
         
        """
        pass
    
    ## Setter for property: (@link HoleAttributesBuilder.PlatingStyleEnum NXOpen.PcbExchange.HoleAttributesBuilder.PlatingStyleEnum@endlink) PlatingStyle

    ##   the hole plating style   
    ##     
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PlatingStyle.setter
    def PlatingStyle(self, platingStyle: HoleAttributesBuilder.PlatingStyleEnum):
        """
        Setter for property: (@link HoleAttributesBuilder.PlatingStyleEnum NXOpen.PcbExchange.HoleAttributesBuilder.PlatingStyleEnum@endlink) PlatingStyle
          the hole plating style   
            
         
        """
        pass
    
    ## Getter for property: (str) SpecifiedPart
    ##   the hole specified part   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def SpecifiedPart(self) -> str:
        """
        Getter for property: (str) SpecifiedPart
          the hole specified part   
            
         
        """
        pass
    
    ## Setter for property: (str) SpecifiedPart

    ##   the hole specified part   
    ##     
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @SpecifiedPart.setter
    def SpecifiedPart(self, specifiedPart: str):
        """
        Setter for property: (str) SpecifiedPart
          the hole specified part   
            
         
        """
        pass
    
import NXOpen
##  Represents a builder to compare two IDX files.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateIdxCompareBuilder  NXOpen::PcbExchange::Manager::CreateIdxCompareBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class IdxCompareBuilder(NXOpen.Builder): 
    """ Represents a builder to compare two IDX files. """


    ##  The source model options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Nx</term><description> 
    ## </description> </item><item><term> 
    ## Idx</term><description> 
    ## </description> </item></list>
    class SourceTypeEnum(Enum):
        """
        Members Include: <Nx> <Idx>
        """
        Nx: int
        Idx: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IdxCompareBuilder.SourceTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) SourceFile
    ##   the source file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def SourceFile(self) -> str:
        """
        Getter for property: (str) SourceFile
          the source file.  
             
         
        """
        pass
    
    ## Setter for property: (str) SourceFile

    ##   the source file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @SourceFile.setter
    def SourceFile(self, sourceFile: str):
        """
        Setter for property: (str) SourceFile
          the source file.  
             
         
        """
        pass
    
    ## Getter for property: (@link IdxCompareBuilder.SourceTypeEnum NXOpen.PcbExchange.IdxCompareBuilder.SourceTypeEnum@endlink) SourceType
    ##   the source model option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return IdxCompareBuilder.SourceTypeEnum
    @property
    def SourceType(self) -> IdxCompareBuilder.SourceTypeEnum:
        """
        Getter for property: (@link IdxCompareBuilder.SourceTypeEnum NXOpen.PcbExchange.IdxCompareBuilder.SourceTypeEnum@endlink) SourceType
          the source model option.  
             
         
        """
        pass
    
    ## Setter for property: (@link IdxCompareBuilder.SourceTypeEnum NXOpen.PcbExchange.IdxCompareBuilder.SourceTypeEnum@endlink) SourceType

    ##   the source model option.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @SourceType.setter
    def SourceType(self, sourceType: IdxCompareBuilder.SourceTypeEnum):
        """
        Setter for property: (@link IdxCompareBuilder.SourceTypeEnum NXOpen.PcbExchange.IdxCompareBuilder.SourceTypeEnum@endlink) SourceType
          the source model option.  
             
         
        """
        pass
    
    ## Getter for property: (str) TargetFile
    ##   the target file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def TargetFile(self) -> str:
        """
        Getter for property: (str) TargetFile
          the target file.  
             
         
        """
        pass
    
    ## Setter for property: (str) TargetFile

    ##   the target file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @TargetFile.setter
    def TargetFile(self, targetFile: str):
        """
        Setter for property: (str) TargetFile
          the target file.  
             
         
        """
        pass
    
import NXOpen
##  Represents a builder to export IDX file.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateIdxExportBuilder  NXOpen::PcbExchange::Manager::CreateIdxExportBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class IdxExportBuilder(NXOpen.Builder): 
    """ Represents a builder to export IDX file. """


    ##  Represents the file units. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Mm</term><description> 
    ## </description> </item><item><term> 
    ## Thou</term><description> 
    ## </description> </item></list>
    class ExportUnitsEnum(Enum):
        """
        Members Include: <Mm> <Thou>
        """
        Mm: int
        Thou: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IdxExportBuilder.ExportUnitsEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the file format options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Idx2</term><description> 
    ## </description> </item><item><term> 
    ## Idx3</term><description> 
    ## </description> </item></list>
    class FileFormatEnum(Enum):
        """
        Members Include: <Idx2> <Idx3>
        """
        Idx2: int
        Idx3: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IdxExportBuilder.FileFormatEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the IDX location options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Os</term><description> 
    ## </description> </item><item><term> 
    ## TeamcenterDS</term><description> 
    ## </description> </item><item><term> 
    ## TeamcenterCS</term><description> 
    ## </description> </item></list>
    class IdxLocationEnum(Enum):
        """
        Members Include: <Os> <TeamcenterDS> <TeamcenterCS>
        """
        Os: int
        TeamcenterDS: int
        TeamcenterCS: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IdxExportBuilder.IdxLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) BaselineFile
    ##   the baseline file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def BaselineFile(self) -> str:
        """
        Getter for property: (str) BaselineFile
          the baseline file.  
             
         
        """
        pass
    
    ## Setter for property: (str) BaselineFile

    ##   the baseline file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BaselineFile.setter
    def BaselineFile(self, baselineFile: str):
        """
        Setter for property: (str) BaselineFile
          the baseline file.  
             
         
        """
        pass
    
    ## Getter for property: (@link IdxExportBuilder.IdxLocationEnum NXOpen.PcbExchange.IdxExportBuilder.IdxLocationEnum@endlink) BaselineLocation
    ##   the baseline location.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return IdxExportBuilder.IdxLocationEnum
    @property
    def BaselineLocation(self) -> IdxExportBuilder.IdxLocationEnum:
        """
        Getter for property: (@link IdxExportBuilder.IdxLocationEnum NXOpen.PcbExchange.IdxExportBuilder.IdxLocationEnum@endlink) BaselineLocation
          the baseline location.  
             
         
        """
        pass
    
    ## Setter for property: (@link IdxExportBuilder.IdxLocationEnum NXOpen.PcbExchange.IdxExportBuilder.IdxLocationEnum@endlink) BaselineLocation

    ##   the baseline location.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BaselineLocation.setter
    def BaselineLocation(self, baselineLocation: IdxExportBuilder.IdxLocationEnum):
        """
        Setter for property: (@link IdxExportBuilder.IdxLocationEnum NXOpen.PcbExchange.IdxExportBuilder.IdxLocationEnum@endlink) BaselineLocation
          the baseline location.  
             
         
        """
        pass
    
    ## Getter for property: (str) BaselineNumber
    ##   the baseline number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def BaselineNumber(self) -> str:
        """
        Getter for property: (str) BaselineNumber
          the baseline number.  
             
         
        """
        pass
    
    ## Setter for property: (str) BaselineNumber

    ##   the baseline number.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BaselineNumber.setter
    def BaselineNumber(self, baselineNumber: str):
        """
        Setter for property: (str) BaselineNumber
          the baseline number.  
             
         
        """
        pass
    
    ## Getter for property: (str) BaselineRevision
    ##   the baseline revision.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def BaselineRevision(self) -> str:
        """
        Getter for property: (str) BaselineRevision
          the baseline revision.  
             
         
        """
        pass
    
    ## Setter for property: (str) BaselineRevision

    ##   the baseline revision.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BaselineRevision.setter
    def BaselineRevision(self, baselineRevision: str):
        """
        Setter for property: (str) BaselineRevision
          the baseline revision.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CloneAssembly
    ##   the flag indicating whether to clone the assembly.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def CloneAssembly(self) -> bool:
        """
        Getter for property: (bool) CloneAssembly
          the flag indicating whether to clone the assembly.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CloneAssembly

    ##   the flag indicating whether to clone the assembly.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CloneAssembly.setter
    def CloneAssembly(self, cloneAssembly: bool):
        """
        Setter for property: (bool) CloneAssembly
          the flag indicating whether to clone the assembly.  
             
         
        """
        pass
    
    ## Getter for property: (@link IdxExportBuilder.FileFormatEnum NXOpen.PcbExchange.IdxExportBuilder.FileFormatEnum@endlink) FileFormat
    ##   the file format.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return IdxExportBuilder.FileFormatEnum
    @property
    def FileFormat(self) -> IdxExportBuilder.FileFormatEnum:
        """
        Getter for property: (@link IdxExportBuilder.FileFormatEnum NXOpen.PcbExchange.IdxExportBuilder.FileFormatEnum@endlink) FileFormat
          the file format.  
             
         
        """
        pass
    
    ## Setter for property: (@link IdxExportBuilder.FileFormatEnum NXOpen.PcbExchange.IdxExportBuilder.FileFormatEnum@endlink) FileFormat

    ##   the file format.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FileFormat.setter
    def FileFormat(self, fileFormat: IdxExportBuilder.FileFormatEnum):
        """
        Setter for property: (@link IdxExportBuilder.FileFormatEnum NXOpen.PcbExchange.IdxExportBuilder.FileFormatEnum@endlink) FileFormat
          the file format.  
             
         
        """
        pass
    
    ## Getter for property: (str) FileNote
    ##   the file note.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def FileNote(self) -> str:
        """
        Getter for property: (str) FileNote
          the file note.  
             
         
        """
        pass
    
    ## Setter for property: (str) FileNote

    ##   the file note.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FileNote.setter
    def FileNote(self, fileNote: str):
        """
        Setter for property: (str) FileNote
          the file note.  
             
         
        """
        pass
    
    ## Getter for property: (@link IdxExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.IdxExportBuilder.ExportUnitsEnum@endlink) FileUnits
    ##   the file units.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return IdxExportBuilder.ExportUnitsEnum
    @property
    def FileUnits(self) -> IdxExportBuilder.ExportUnitsEnum:
        """
        Getter for property: (@link IdxExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.IdxExportBuilder.ExportUnitsEnum@endlink) FileUnits
          the file units.  
             
         
        """
        pass
    
    ## Setter for property: (@link IdxExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.IdxExportBuilder.ExportUnitsEnum@endlink) FileUnits

    ##   the file units.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FileUnits.setter
    def FileUnits(self, exportUnits: IdxExportBuilder.ExportUnitsEnum):
        """
        Setter for property: (@link IdxExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.IdxExportBuilder.ExportUnitsEnum@endlink) FileUnits
          the file units.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectedObjects
    ##   the selected objects.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def SelectedObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectedObjects
          the selected objects.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowLog
    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowLog

    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ## Getter for property: (bool) TagModel
    ##   the flag indicating whether to tag the model.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def TagModel(self) -> bool:
        """
        Getter for property: (bool) TagModel
          the flag indicating whether to tag the model.  
             
         
        """
        pass
    
    ## Setter for property: (bool) TagModel

    ##   the flag indicating whether to tag the model.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @TagModel.setter
    def TagModel(self, tagModel: bool):
        """
        Setter for property: (bool) TagModel
          the flag indicating whether to tag the model.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseCloneSelection
    ##   the flag indicating whether to clone only selected objects.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def UseCloneSelection(self) -> bool:
        """
        Getter for property: (bool) UseCloneSelection
          the flag indicating whether to clone only selected objects.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseCloneSelection

    ##   the flag indicating whether to clone only selected objects.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @UseCloneSelection.setter
    def UseCloneSelection(self, canUseCloneSelection: bool):
        """
        Setter for property: (bool) UseCloneSelection
          the flag indicating whether to clone only selected objects.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseCurrentWorkPart
    ##   the flag indicating whether to use the current work part.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def UseCurrentWorkPart(self) -> bool:
        """
        Getter for property: (bool) UseCurrentWorkPart
          the flag indicating whether to use the current work part.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseCurrentWorkPart

    ##   the flag indicating whether to use the current work part.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @UseCurrentWorkPart.setter
    def UseCurrentWorkPart(self, useCurrentWorkPart: bool):
        """
        Setter for property: (bool) UseCurrentWorkPart
          the flag indicating whether to use the current work part.  
             
         
        """
        pass
    
    ##  Runs the pre-export baseline hook and sets the baseline file, if defined. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def RunPreExportBaselineHook(builder: IdxExportBuilder) -> None:
        """
         Runs the pre-export baseline hook and sets the baseline file, if defined. 
        """
        pass
    
import NXOpen
##  Represents a builder to import IDX file.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateIdxImportBuilder  NXOpen::PcbExchange::Manager::CreateIdxImportBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class IdxImportBuilder(NXOpen.Builder): 
    """ Represents a builder to import IDX file. """


    ##  The IDX data location options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Local</term><description> 
    ## </description> </item><item><term> 
    ## TeamcenterDS</term><description> 
    ## </description> </item><item><term> 
    ## TeamcenterCS</term><description> 
    ## </description> </item></list>
    class DataLocation(Enum):
        """
        Members Include: <Local> <TeamcenterDS> <TeamcenterCS>
        """
        Local: int
        TeamcenterDS: int
        TeamcenterCS: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IdxImportBuilder.DataLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) AssemblyName
    ##   the assembly name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def AssemblyName(self) -> str:
        """
        Getter for property: (str) AssemblyName
          the assembly name.  
             
         
        """
        pass
    
    ## Setter for property: (str) AssemblyName

    ##   the assembly name.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AssemblyName.setter
    def AssemblyName(self, assemblyName: str):
        """
        Setter for property: (str) AssemblyName
          the assembly name.  
             
         
        """
        pass
    
    ## Getter for property: (str) AssemblyNumber
    ##   the assembly number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def AssemblyNumber(self) -> str:
        """
        Getter for property: (str) AssemblyNumber
          the assembly number.  
             
         
        """
        pass
    
    ## Setter for property: (str) AssemblyNumber

    ##   the assembly number.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AssemblyNumber.setter
    def AssemblyNumber(self, assemblyNumber: str):
        """
        Setter for property: (str) AssemblyNumber
          the assembly number.  
             
         
        """
        pass
    
    ## Getter for property: (str) AssemblyRevision
    ##   the assembly revision.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def AssemblyRevision(self) -> str:
        """
        Getter for property: (str) AssemblyRevision
          the assembly revision.  
             
         
        """
        pass
    
    ## Setter for property: (str) AssemblyRevision

    ##   the assembly revision.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AssemblyRevision.setter
    def AssemblyRevision(self, assemblyRevision: str):
        """
        Setter for property: (str) AssemblyRevision
          the assembly revision.  
             
         
        """
        pass
    
    ## Getter for property: (str) BaselineFile
    ##   the baseline file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def BaselineFile(self) -> str:
        """
        Getter for property: (str) BaselineFile
          the baseline file.  
             
         
        """
        pass
    
    ## Setter for property: (str) BaselineFile

    ##   the baseline file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BaselineFile.setter
    def BaselineFile(self, baselineFile: str):
        """
        Setter for property: (str) BaselineFile
          the baseline file.  
             
         
        """
        pass
    
    ## Getter for property: (str) CollaborationDir
    ##   the collaboration directory.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def CollaborationDir(self) -> str:
        """
        Getter for property: (str) CollaborationDir
          the collaboration directory.  
             
         
        """
        pass
    
    ## Setter for property: (str) CollaborationDir

    ##   the collaboration directory.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CollaborationDir.setter
    def CollaborationDir(self, foldername: str):
        """
        Setter for property: (str) CollaborationDir
          the collaboration directory.  
             
         
        """
        pass
    
    ## Getter for property: (@link IdxImportBuilder.DataLocation NXOpen.PcbExchange.IdxImportBuilder.DataLocation@endlink) IdxDataFrom
    ##   the location of IDX data.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return IdxImportBuilder.DataLocation
    @property
    def IdxDataFrom(self) -> IdxImportBuilder.DataLocation:
        """
        Getter for property: (@link IdxImportBuilder.DataLocation NXOpen.PcbExchange.IdxImportBuilder.DataLocation@endlink) IdxDataFrom
          the location of IDX data.  
             
         
        """
        pass
    
    ## Setter for property: (@link IdxImportBuilder.DataLocation NXOpen.PcbExchange.IdxImportBuilder.DataLocation@endlink) IdxDataFrom

    ##   the location of IDX data.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @IdxDataFrom.setter
    def IdxDataFrom(self, idxDataFrom: IdxImportBuilder.DataLocation):
        """
        Setter for property: (@link IdxImportBuilder.DataLocation NXOpen.PcbExchange.IdxImportBuilder.DataLocation@endlink) IdxDataFrom
          the location of IDX data.  
             
         
        """
        pass
    
    ## Getter for property: (str) IdxNumber
    ##   the IDX number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def IdxNumber(self) -> str:
        """
        Getter for property: (str) IdxNumber
          the IDX number.  
             
         
        """
        pass
    
    ## Setter for property: (str) IdxNumber

    ##   the IDX number.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @IdxNumber.setter
    def IdxNumber(self, idxNumber: str):
        """
        Setter for property: (str) IdxNumber
          the IDX number.  
             
         
        """
        pass
    
    ## Getter for property: (str) IdxRevision
    ##   the IDX revision.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def IdxRevision(self) -> str:
        """
        Getter for property: (str) IdxRevision
          the IDX revision.  
             
         
        """
        pass
    
    ## Setter for property: (str) IdxRevision

    ##   the IDX revision.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @IdxRevision.setter
    def IdxRevision(self, idxRevision: str):
        """
        Setter for property: (str) IdxRevision
          the IDX revision.  
             
         
        """
        pass
    
    ## Getter for property: (str) OutputPartFile
    ##   the output part file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def OutputPartFile(self) -> str:
        """
        Getter for property: (str) OutputPartFile
          the output part file.  
             
         
        """
        pass
    
    ## Setter for property: (str) OutputPartFile

    ##   the output part file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @OutputPartFile.setter
    def OutputPartFile(self, outputPartString: str):
        """
        Setter for property: (str) OutputPartFile
          the output part file.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseCurrentPart
    ##   the flag indicating whether to use the current work part.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def UseCurrentPart(self) -> bool:
        """
        Getter for property: (bool) UseCurrentPart
          the flag indicating whether to use the current work part.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseCurrentPart

    ##   the flag indicating whether to use the current work part.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @UseCurrentPart.setter
    def UseCurrentPart(self, useCurrentPart: bool):
        """
        Setter for property: (bool) UseCurrentPart
          the flag indicating whether to use the current work part.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseExistComp
    ##   the flag indicating whether to use existing components.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def UseExistComp(self) -> bool:
        """
        Getter for property: (bool) UseExistComp
          the flag indicating whether to use existing components.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseExistComp

    ##   the flag indicating whether to use existing components.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @UseExistComp.setter
    def UseExistComp(self, useExistComp: bool):
        """
        Setter for property: (bool) UseExistComp
          the flag indicating whether to use existing components.  
             
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::PcbExchange::IncrementalChange NXOpen::PcbExchange::IncrementalChange@endlink .  <br> No support for KF.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class IncrementalChange(NXOpen.TaggedObject): 
    """ Represents a <ja_class>NXOpen.PcbExchange.IncrementalChange</ja_class>. """


    ## Getter for property: (bool) Accepted
    ##   the flag indicating whether a change is accepted.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def Accepted(self) -> bool:
        """
        Getter for property: (bool) Accepted
          the flag indicating whether a change is accepted.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Accepted

    ##   the flag indicating whether a change is accepted.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Accepted.setter
    def Accepted(self, isAccepted: bool):
        """
        Setter for property: (bool) Accepted
          the flag indicating whether a change is accepted.  
             
         
        """
        pass
    
    ## Getter for property: (str) Comments
    ##   the comments.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def Comments(self) -> str:
        """
        Getter for property: (str) Comments
          the comments.  
             
         
        """
        pass
    
    ## Setter for property: (str) Comments

    ##   the comments.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Comments.setter
    def Comments(self, comments: str):
        """
        Setter for property: (str) Comments
          the comments.  
             
         
        """
        pass
    
    ## Getter for property: (str) Transaction
    ##   the transaction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def Transaction(self) -> str:
        """
        Getter for property: (str) Transaction
          the transaction.  
             
         
        """
        pass
    
    ## Setter for property: (str) Transaction

    ##   the transaction.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Transaction.setter
    def Transaction(self, transaction: str):
        """
        Setter for property: (str) Transaction
          the transaction.  
             
         
        """
        pass
    
    ##  Returns the attributes. 
    ##  @return A tuple consisting of (values, names). 
    ##  - values is: List[str]. Attribute values. .
    ##  - names is: List[str]. Attribute names. .

    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAttributes(change: IncrementalChange) -> Tuple[List[str], List[str]]:
        """
         Returns the attributes. 
         @return A tuple consisting of (values, names). 
         - values is: List[str]. Attribute values. .
         - names is: List[str]. Attribute names. .

        """
        pass
    
import NXOpen
##  Represents a builder to export incremental changes.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateIncrementalExportBuilder  NXOpen::PcbExchange::Manager::CreateIncrementalExportBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class IncrementalExportBuilder(NXOpen.Builder): 
    """ Represents a builder to export incremental changes. """


    ##  Represents the file units. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Mm</term><description> 
    ## </description> </item><item><term> 
    ## Thou</term><description> 
    ## </description> </item></list>
    class ExportUnitsEnum(Enum):
        """
        Members Include: <Mm> <Thou>
        """
        Mm: int
        Thou: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IncrementalExportBuilder.ExportUnitsEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the incremental file format options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Idx2</term><description> 
    ## </description> </item><item><term> 
    ## Idx3</term><description> 
    ## </description> </item></list>
    class FormatEnum(Enum):
        """
        Members Include: <Idx2> <Idx3>
        """
        Idx2: int
        Idx3: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IncrementalExportBuilder.FormatEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the target data location options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Os</term><description> 
    ## </description> </item><item><term> 
    ## TeamcenterCS</term><description> 
    ## </description> </item></list>
    class TargetLocationEnum(Enum):
        """
        Members Include: <Os> <TeamcenterCS>
        """
        Os: int
        TeamcenterCS: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IncrementalExportBuilder.TargetLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CloneAssembly
    ##   the flag indicating whether to clone the assembly.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def CloneAssembly(self) -> bool:
        """
        Getter for property: (bool) CloneAssembly
          the flag indicating whether to clone the assembly.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CloneAssembly

    ##   the flag indicating whether to clone the assembly.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CloneAssembly.setter
    def CloneAssembly(self, cloneAssembly: bool):
        """
        Setter for property: (bool) CloneAssembly
          the flag indicating whether to clone the assembly.  
             
         
        """
        pass
    
    ## Getter for property: (@link IncrementalExportBuilder.FormatEnum NXOpen.PcbExchange.IncrementalExportBuilder.FormatEnum@endlink) FileFormat
    ##   the file format.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return IncrementalExportBuilder.FormatEnum
    @property
    def FileFormat(self) -> IncrementalExportBuilder.FormatEnum:
        """
        Getter for property: (@link IncrementalExportBuilder.FormatEnum NXOpen.PcbExchange.IncrementalExportBuilder.FormatEnum@endlink) FileFormat
          the file format.  
             
         
        """
        pass
    
    ## Setter for property: (@link IncrementalExportBuilder.FormatEnum NXOpen.PcbExchange.IncrementalExportBuilder.FormatEnum@endlink) FileFormat

    ##   the file format.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FileFormat.setter
    def FileFormat(self, fileFormat: IncrementalExportBuilder.FormatEnum):
        """
        Setter for property: (@link IncrementalExportBuilder.FormatEnum NXOpen.PcbExchange.IncrementalExportBuilder.FormatEnum@endlink) FileFormat
          the file format.  
             
         
        """
        pass
    
    ## Getter for property: (str) FileNote
    ##   the file note.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def FileNote(self) -> str:
        """
        Getter for property: (str) FileNote
          the file note.  
             
         
        """
        pass
    
    ## Setter for property: (str) FileNote

    ##   the file note.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FileNote.setter
    def FileNote(self, fileNote: str):
        """
        Setter for property: (str) FileNote
          the file note.  
             
         
        """
        pass
    
    ## Getter for property: (@link IncrementalExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.IncrementalExportBuilder.ExportUnitsEnum@endlink) FileUnits
    ##   the file units.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return IncrementalExportBuilder.ExportUnitsEnum
    @property
    def FileUnits(self) -> IncrementalExportBuilder.ExportUnitsEnum:
        """
        Getter for property: (@link IncrementalExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.IncrementalExportBuilder.ExportUnitsEnum@endlink) FileUnits
          the file units.  
             
         
        """
        pass
    
    ## Setter for property: (@link IncrementalExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.IncrementalExportBuilder.ExportUnitsEnum@endlink) FileUnits

    ##   the file units.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @FileUnits.setter
    def FileUnits(self, exportUnits: IncrementalExportBuilder.ExportUnitsEnum):
        """
        Setter for property: (@link IncrementalExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.IncrementalExportBuilder.ExportUnitsEnum@endlink) FileUnits
          the file units.  
             
         
        """
        pass
    
    ## Getter for property: (str) Output
    ##   the output file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def Output(self) -> str:
        """
        Getter for property: (str) Output
          the output file.  
             
         
        """
        pass
    
    ## Setter for property: (str) Output

    ##   the output file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Output.setter
    def Output(self, filename: str):
        """
        Setter for property: (str) Output
          the output file.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectedObjects
    ##   the selected objects.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def SelectedObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectedObjects
          the selected objects.  
             
         
        """
        pass
    
    ## Getter for property: (@link IncrementalExportBuilder.TargetLocationEnum NXOpen.PcbExchange.IncrementalExportBuilder.TargetLocationEnum@endlink) TargetLocation
    ##   the target location.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return IncrementalExportBuilder.TargetLocationEnum
    @property
    def TargetLocation(self) -> IncrementalExportBuilder.TargetLocationEnum:
        """
        Getter for property: (@link IncrementalExportBuilder.TargetLocationEnum NXOpen.PcbExchange.IncrementalExportBuilder.TargetLocationEnum@endlink) TargetLocation
          the target location.  
             
         
        """
        pass
    
    ## Setter for property: (@link IncrementalExportBuilder.TargetLocationEnum NXOpen.PcbExchange.IncrementalExportBuilder.TargetLocationEnum@endlink) TargetLocation

    ##   the target location.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TargetLocation.setter
    def TargetLocation(self, targetLocation: IncrementalExportBuilder.TargetLocationEnum):
        """
        Setter for property: (@link IncrementalExportBuilder.TargetLocationEnum NXOpen.PcbExchange.IncrementalExportBuilder.TargetLocationEnum@endlink) TargetLocation
          the target location.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseCloneSelection
    ##   the flag indicating whether to clone only selected objects.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def UseCloneSelection(self) -> bool:
        """
        Getter for property: (bool) UseCloneSelection
          the flag indicating whether to clone only selected objects.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseCloneSelection

    ##   the flag indicating whether to clone only selected objects.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @UseCloneSelection.setter
    def UseCloneSelection(self, canUseCloneSelection: bool):
        """
        Setter for property: (bool) UseCloneSelection
          the flag indicating whether to clone only selected objects.  
             
         
        """
        pass
    
    ##  Compares the current model with the baseline and returns the flag indicating whether the model has changes. 
    ##  @return hasChanges (bool): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def CompareAssembly(builder: IncrementalExportBuilder) -> bool:
        """
         Compares the current model with the baseline and returns the flag indicating whether the model has changes. 
         @return hasChanges (bool): .
        """
        pass
    
    ##  Returns the incremental changes. 
    ##  @return changes (@link IncrementalChange List[NXOpen.PcbExchange.IncrementalChange]@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def GetIncrementalChanges(builder: IncrementalExportBuilder) -> List[IncrementalChange]:
        """
         Returns the incremental changes. 
         @return changes (@link IncrementalChange List[NXOpen.PcbExchange.IncrementalChange]@endlink): .
        """
        pass
    
    ##  Runs the pre-export incremental hook and sets the output file, if defined. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def RunPreExportIncrementalHook(builder: IncrementalExportBuilder) -> None:
        """
         Runs the pre-export incremental hook and sets the output file, if defined. 
        """
        pass
    
    ##  Sets the incremental changes. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="changes"> (@link IncrementalChange List[NXOpen.PcbExchange.IncrementalChange]@endlink) </param>
    def SetIncrementalChanges(builder: IncrementalExportBuilder, changes: List[IncrementalChange]) -> None:
        """
         Sets the incremental changes. 
        """
        pass
    
import NXOpen
##  Represents a builder to import incremental changes.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateIncrementalImportBuilder  NXOpen::PcbExchange::Manager::CreateIncrementalImportBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class IncrementalImportBuilder(NXOpen.Builder): 
    """ Represents a builder to import incremental changes. """


    ## Getter for property: (str) Filename
    ##   the filename.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def Filename(self) -> str:
        """
        Getter for property: (str) Filename
          the filename.  
             
         
        """
        pass
    
    ## Setter for property: (str) Filename

    ##   the filename.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Filename.setter
    def Filename(self, filename: str):
        """
        Setter for property: (str) Filename
          the filename.  
             
         
        """
        pass
    
    ## Getter for property: (bool) OnlyUseExistingComponents
    ##   the flag indicating whether to only use existing components.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def OnlyUseExistingComponents(self) -> bool:
        """
        Getter for property: (bool) OnlyUseExistingComponents
          the flag indicating whether to only use existing components.  
             
         
        """
        pass
    
    ## Setter for property: (bool) OnlyUseExistingComponents

    ##   the flag indicating whether to only use existing components.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @OnlyUseExistingComponents.setter
    def OnlyUseExistingComponents(self, onlyUseExistingComp: bool):
        """
        Setter for property: (bool) OnlyUseExistingComponents
          the flag indicating whether to only use existing components.  
             
         
        """
        pass
    
    ## Getter for property: (str) Output
    ##   the output file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def Output(self) -> str:
        """
        Getter for property: (str) Output
          the output file.  
             
         
        """
        pass
    
    ## Setter for property: (str) Output

    ##   the output file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Output.setter
    def Output(self, output: str):
        """
        Setter for property: (str) Output
          the output file.  
             
         
        """
        pass
    
    ##  Accepts all changes. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def AcceptAll(builder: IncrementalImportBuilder) -> None:
        """
         Accepts all changes. 
        """
        pass
    
    ##  Sets the board change state to true and accepts change with id. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="id"> (str) </param>
    def AcceptBoardChange(builder: IncrementalImportBuilder, id: str) -> None:
        """
         Sets the board change state to true and accepts change with id. 
        """
        pass
    
    ##  Accepts a change. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="id"> (str) </param>
    def AcceptChange(builder: IncrementalImportBuilder, id: str) -> None:
        """
         Accepts a change. 
        """
        pass
    
    ##  Acknowledges all changes. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def AcknowledgeAll(builder: IncrementalImportBuilder) -> None:
        """
         Acknowledges all changes. 
        """
        pass
    
    ##  Acknowledges a change. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="id"> (str) </param>
    def AcknowledgeResponse(builder: IncrementalImportBuilder, id: str) -> None:
        """
         Acknowledges a change. 
        """
        pass
    
    ##  Adds a new comment to a response. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="id"> (str) </param>
    ## <param name="comment"> (str) </param>
    def AddNewComment(builder: IncrementalImportBuilder, id: str, comment: str) -> None:
        """
         Adds a new comment to a response. 
        """
        pass
    
    ##  Cancels increment review. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def CancelIncrementReview(builder: IncrementalImportBuilder) -> None:
        """
         Cancels increment review. 
        """
        pass
    
    ##  Clear processed incremental group. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def ClearProcessedIncrementalGroupVec(builder: IncrementalImportBuilder) -> None:
        """
         Clear processed incremental group. 
        """
        pass
    
    ##  Ignores all changes. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def IgnoreAll(builder: IncrementalImportBuilder) -> None:
        """
         Ignores all changes. 
        """
        pass
    
    ##  Ignores a change. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="id"> (str) </param>
    def IgnoreResponse(builder: IncrementalImportBuilder, id: str) -> None:
        """
         Ignores a change. 
        """
        pass
    
    ##  Previews all changes. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def PreviewChanges(builder: IncrementalImportBuilder) -> None:
        """
         Previews all changes. 
        """
        pass
    
    ##  Reads the import file. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def ReadImportFile(builder: IncrementalImportBuilder) -> None:
        """
         Reads the import file. 
        """
        pass
    
    ##  Rejects all changes. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def RejectAll(builder: IncrementalImportBuilder) -> None:
        """
         Rejects all changes. 
        """
        pass
    
    ##  Sets the board change state to false and rejects change with id. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="id"> (str) </param>
    def RejectBoardChange(builder: IncrementalImportBuilder, id: str) -> None:
        """
         Sets the board change state to false and rejects change with id. 
        """
        pass
    
    ##  Rejects a change. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="id"> (str) </param>
    def RejectChange(builder: IncrementalImportBuilder, id: str) -> None:
        """
         Rejects a change. 
        """
        pass
    
    ##  Sets board update status. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="updated"> (bool) </param>
    def SetBoardUpdated(builder: IncrementalImportBuilder, updated: bool) -> None:
        """
         Sets board update status. 
        """
        pass
    
    ##  Makes the supplied part the display part. 
    ##  @return existingPartTag (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def SetExistingPart(builder: IncrementalImportBuilder) -> NXOpen.DisplayableObject:
        """
         Makes the supplied part the display part. 
         @return existingPartTag (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink): .
        """
        pass
    
    ##  Un-highlights all. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def UnhighlightAll(builder: IncrementalImportBuilder) -> None:
        """
         Un-highlights all. 
        """
        pass
    
import NXOpen
##  Represents a PCB exchange manager.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class Manager(NXOpen.Object): 
    """ Represents a PCB exchange manager. """


    ##  Returns the PcbExchange.AlternateComponentManager instance belonging to this instance. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @link AlternateComponentManager NXOpen.PcbExchange.AlternateComponentManager@endlink
    @property
    def AlternateComponentManager() -> AlternateComponentManager:
        """
         Returns the PcbExchange.AlternateComponentManager instance belonging to this instance. 
        """
        pass
    
    ##  Returns the PcbExchange.PendingComponentManager instance belonging to this instance. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @link PendingComponentManager NXOpen.PcbExchange.PendingComponentManager@endlink
    @property
    def PendingComponentManager() -> PendingComponentManager:
        """
         Returns the PcbExchange.PendingComponentManager instance belonging to this instance. 
        """
        pass
    
    ##  Returns the PcbExchange.NotificationManager instance belonging to this instance. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @link NotificationManager NXOpen.PcbExchange.NotificationManager@endlink
    @property
    def NotificationManager() -> NotificationManager:
        """
         Returns the PcbExchange.NotificationManager instance belonging to this instance. 
        """
        pass
    
    ##  Automatically creates areas. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def AutoCreateAreas() -> None:
        """
         Automatically creates areas. 
        """
        pass
    
    ##  Automatically creates components. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def AutoCreateComponents() -> None:
        """
         Automatically creates components. 
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::AdvancedConductivityBuilder PcbExchange::AdvancedConductivityBuilder@endlink . 
    ##  @return builder (@link AdvancedConductivityBuilder NXOpen.PcbExchange.AdvancedConductivityBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateAdvancedConductivityBuilder(part: NXOpen.NXObject) -> AdvancedConductivityBuilder:
        """
         Creates an instance of @link PcbExchange::AdvancedConductivityBuilder PcbExchange::AdvancedConductivityBuilder@endlink . 
         @return builder (@link AdvancedConductivityBuilder NXOpen.PcbExchange.AdvancedConductivityBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::AreaAttributesBuilder PcbExchange::AreaAttributesBuilder@endlink   
    ##  @return builder (@link AreaAttributesBuilder NXOpen.PcbExchange.AreaAttributesBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateAreaAttributesBuilder(part: NXOpen.NXObject) -> AreaAttributesBuilder:
        """
         Creates an instance of @link PcbExchange::AreaAttributesBuilder PcbExchange::AreaAttributesBuilder@endlink   
         @return builder (@link AreaAttributesBuilder NXOpen.PcbExchange.AreaAttributesBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates or edit an instance of @link PcbExchange::AreaMappingBuilder PcbExchange::AreaMappingBuilder@endlink . 
    ##  @return builder (@link AreaMappingBuilder NXOpen.PcbExchange.AreaMappingBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  the area mapping to be edited 
    def CreateAreaMappingBuilder(part: NXOpen.NXObject, areaMapping: AreaMapping) -> AreaMappingBuilder:
        """
         Creates or edit an instance of @link PcbExchange::AreaMappingBuilder PcbExchange::AreaMappingBuilder@endlink . 
         @return builder (@link AreaMappingBuilder NXOpen.PcbExchange.AreaMappingBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::BoardAttributesBuilder PcbExchange::BoardAttributesBuilder@endlink . 
    ##  @return builder (@link BoardAttributesBuilder NXOpen.PcbExchange.BoardAttributesBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateBoardAttributesBuilder(part: NXOpen.NXObject) -> BoardAttributesBuilder:
        """
         Creates an instance of @link PcbExchange::BoardAttributesBuilder PcbExchange::BoardAttributesBuilder@endlink . 
         @return builder (@link BoardAttributesBuilder NXOpen.PcbExchange.BoardAttributesBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::BoardPropertiesBuilder PcbExchange::BoardPropertiesBuilder@endlink . 
    ##  @return builder (@link BoardPropertiesBuilder NXOpen.PcbExchange.BoardPropertiesBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateBoardPropertiesBuilder(part: NXOpen.NXObject) -> BoardPropertiesBuilder:
        """
         Creates an instance of @link PcbExchange::BoardPropertiesBuilder PcbExchange::BoardPropertiesBuilder@endlink . 
         @return builder (@link BoardPropertiesBuilder NXOpen.PcbExchange.BoardPropertiesBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::CompareAndUpdateBuilder PcbExchange::CompareAndUpdateBuilder@endlink . 
    ##  @return builder (@link CompareAndUpdateBuilder NXOpen.PcbExchange.CompareAndUpdateBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateCompareAndUpdateBuilder(part: NXOpen.NXObject) -> CompareAndUpdateBuilder:
        """
         Creates an instance of @link PcbExchange::CompareAndUpdateBuilder PcbExchange::CompareAndUpdateBuilder@endlink . 
         @return builder (@link CompareAndUpdateBuilder NXOpen.PcbExchange.CompareAndUpdateBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::ComponentAttributesBuilder PcbExchange::ComponentAttributesBuilder@endlink . 
    ##  @return builder (@link ComponentAttributesBuilder NXOpen.PcbExchange.ComponentAttributesBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateComponentAttributesBuilder(part: NXOpen.NXObject) -> ComponentAttributesBuilder:
        """
         Creates an instance of @link PcbExchange::ComponentAttributesBuilder PcbExchange::ComponentAttributesBuilder@endlink . 
         @return builder (@link ComponentAttributesBuilder NXOpen.PcbExchange.ComponentAttributesBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::ComponentConstraintsBuilder PcbExchange::ComponentConstraintsBuilder@endlink . 
    ##  @return builder (@link ComponentConstraintsBuilder NXOpen.PcbExchange.ComponentConstraintsBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateComponentConstraintsBuilder(part: NXOpen.NXObject) -> ComponentConstraintsBuilder:
        """
         Creates an instance of @link PcbExchange::ComponentConstraintsBuilder PcbExchange::ComponentConstraintsBuilder@endlink . 
         @return builder (@link ComponentConstraintsBuilder NXOpen.PcbExchange.ComponentConstraintsBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::ComponentCsysBuilder PcbExchange::ComponentCsysBuilder@endlink . 
    ##  @return builder (@link ComponentCsysBuilder NXOpen.PcbExchange.ComponentCsysBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateComponentCsysBuilder(part: NXOpen.NXObject) -> ComponentCsysBuilder:
        """
         Creates an instance of @link PcbExchange::ComponentCsysBuilder PcbExchange::ComponentCsysBuilder@endlink . 
         @return builder (@link ComponentCsysBuilder NXOpen.PcbExchange.ComponentCsysBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::ComponentPlacementOutlineBuilder PcbExchange::ComponentPlacementOutlineBuilder@endlink . 
    ##  @return builder (@link ComponentPlacementOutlineBuilder NXOpen.PcbExchange.ComponentPlacementOutlineBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateComponentPlacementOutlineBuilder(part: NXOpen.NXObject) -> ComponentPlacementOutlineBuilder:
        """
         Creates an instance of @link PcbExchange::ComponentPlacementOutlineBuilder PcbExchange::ComponentPlacementOutlineBuilder@endlink . 
         @return builder (@link ComponentPlacementOutlineBuilder NXOpen.PcbExchange.ComponentPlacementOutlineBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates a @link PcbExchange::DesignRuleBuilder PcbExchange::DesignRuleBuilder@endlink  which creates a @link NXOpen::PcbExchange::DesignRule NXOpen::PcbExchange::DesignRule@endlink  in the given part. 
    ##  @return builder (@link DesignRuleBuilder NXOpen.PcbExchange.DesignRuleBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  part 
    @overload
    def CreateDesignRuleBuilder(self, part: NXOpen.NXObject) -> DesignRuleBuilder:
        """
         Creates a @link PcbExchange::DesignRuleBuilder PcbExchange::DesignRuleBuilder@endlink  which creates a @link NXOpen::PcbExchange::DesignRule NXOpen::PcbExchange::DesignRule@endlink  in the given part. 
         @return builder (@link DesignRuleBuilder NXOpen.PcbExchange.DesignRuleBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates a @link PcbExchange::DesignRuleBuilder PcbExchange::DesignRuleBuilder@endlink  which edits a @link NXOpen::PcbExchange::DesignRule NXOpen::PcbExchange::DesignRule@endlink . 
    ##  @return builder (@link DesignRuleBuilder NXOpen.PcbExchange.DesignRuleBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  rule to edit 
    @overload
    def CreateDesignRuleBuilder(self, ruleToEdit: DesignRule) -> DesignRuleBuilder:
        """
         Creates a @link PcbExchange::DesignRuleBuilder PcbExchange::DesignRuleBuilder@endlink  which edits a @link NXOpen::PcbExchange::DesignRule NXOpen::PcbExchange::DesignRule@endlink . 
         @return builder (@link DesignRuleBuilder NXOpen.PcbExchange.DesignRuleBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates a @link PcbExchange::DesignValidator PcbExchange::DesignValidator@endlink  to validate the design rules in the given part. 
    ##  @return validator (@link DesignValidator NXOpen.PcbExchange.DesignValidator@endlink):  created validator. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition")
    ##  part 
    def CreateDesignValidator(part: NXOpen.NXObject) -> DesignValidator:
        """
         Creates a @link PcbExchange::DesignValidator PcbExchange::DesignValidator@endlink  to validate the design rules in the given part. 
         @return validator (@link DesignValidator NXOpen.PcbExchange.DesignValidator@endlink):  created validator. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::EcadExportBuilder PcbExchange::EcadExportBuilder@endlink . 
    ##  @return builder (@link EcadExportBuilder NXOpen.PcbExchange.EcadExportBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateEcadExportBuilder(part: NXOpen.NXObject) -> EcadExportBuilder:
        """
         Creates an instance of @link PcbExchange::EcadExportBuilder PcbExchange::EcadExportBuilder@endlink . 
         @return builder (@link EcadExportBuilder NXOpen.PcbExchange.EcadExportBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::EcadImportBuilder PcbExchange::EcadImportBuilder@endlink . 
    ##  @return builder (@link EcadImportBuilder NXOpen.PcbExchange.EcadImportBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateEcadImportBuilder(part: NXOpen.NXObject) -> EcadImportBuilder:
        """
         Creates an instance of @link PcbExchange::EcadImportBuilder PcbExchange::EcadImportBuilder@endlink . 
         @return builder (@link EcadImportBuilder NXOpen.PcbExchange.EcadImportBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::EcadPanelImportBuilder PcbExchange::EcadPanelImportBuilder@endlink . 
    ##  @return builder (@link EcadPanelImportBuilder NXOpen.PcbExchange.EcadPanelImportBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateEcadPanelImportBuilder(part: NXOpen.NXObject) -> EcadPanelImportBuilder:
        """
         Creates an instance of @link PcbExchange::EcadPanelImportBuilder PcbExchange::EcadPanelImportBuilder@endlink . 
         @return builder (@link EcadPanelImportBuilder NXOpen.PcbExchange.EcadPanelImportBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::EntityFilterBuilder PcbExchange::EntityFilterBuilder@endlink . 
    ##  @return builder (@link EntityFilterBuilder NXOpen.PcbExchange.EntityFilterBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  the entity filter to be edited 
    def CreateEntityFilterBuilder(part: NXOpen.NXObject, entityFilter: EntityFilter) -> EntityFilterBuilder:
        """
         Creates an instance of @link PcbExchange::EntityFilterBuilder PcbExchange::EntityFilterBuilder@endlink . 
         @return builder (@link EntityFilterBuilder NXOpen.PcbExchange.EntityFilterBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::ExternalDataImportBuilder PcbExchange::ExternalDataImportBuilder@endlink . 
    ##  @return builder (@link ExternalDataImportBuilder NXOpen.PcbExchange.ExternalDataImportBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  part 
    def CreateExternalDataImportBuilder(part: NXOpen.NXObject) -> ExternalDataImportBuilder:
        """
         Creates an instance of @link PcbExchange::ExternalDataImportBuilder PcbExchange::ExternalDataImportBuilder@endlink . 
         @return builder (@link ExternalDataImportBuilder NXOpen.PcbExchange.ExternalDataImportBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::HoleAttributesBuilder PcbExchange::HoleAttributesBuilder@endlink . 
    ##  @return builder (@link HoleAttributesBuilder NXOpen.PcbExchange.HoleAttributesBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateHoleAttributesBuilder(part: NXOpen.NXObject) -> HoleAttributesBuilder:
        """
         Creates an instance of @link PcbExchange::HoleAttributesBuilder PcbExchange::HoleAttributesBuilder@endlink . 
         @return builder (@link HoleAttributesBuilder NXOpen.PcbExchange.HoleAttributesBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::IdxCompareBuilder PcbExchange::IdxCompareBuilder@endlink . 
    ##  @return builder (@link IdxCompareBuilder NXOpen.PcbExchange.IdxCompareBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateIdxCompareBuilder(part: NXOpen.NXObject) -> IdxCompareBuilder:
        """
         Creates an instance of @link PcbExchange::IdxCompareBuilder PcbExchange::IdxCompareBuilder@endlink . 
         @return builder (@link IdxCompareBuilder NXOpen.PcbExchange.IdxCompareBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::IdxExportBuilder PcbExchange::IdxExportBuilder@endlink . 
    ##  @return builder (@link IdxExportBuilder NXOpen.PcbExchange.IdxExportBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateIdxExportBuilder(part: NXOpen.NXObject) -> IdxExportBuilder:
        """
         Creates an instance of @link PcbExchange::IdxExportBuilder PcbExchange::IdxExportBuilder@endlink . 
         @return builder (@link IdxExportBuilder NXOpen.PcbExchange.IdxExportBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::IdxImportBuilder PcbExchange::IdxImportBuilder@endlink . 
    ##  @return builder (@link IdxImportBuilder NXOpen.PcbExchange.IdxImportBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateIdxImportBuilder(part: NXOpen.NXObject) -> IdxImportBuilder:
        """
         Creates an instance of @link PcbExchange::IdxImportBuilder PcbExchange::IdxImportBuilder@endlink . 
         @return builder (@link IdxImportBuilder NXOpen.PcbExchange.IdxImportBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::IncrementalChange PcbExchange::IncrementalChange@endlink . 
    ##  @return change (@link IncrementalChange NXOpen.PcbExchange.IncrementalChange@endlink):  created IncrementalChange .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    def CreateIncrementalChange() -> IncrementalChange:
        """
         Creates an instance of @link PcbExchange::IncrementalChange PcbExchange::IncrementalChange@endlink . 
         @return change (@link IncrementalChange NXOpen.PcbExchange.IncrementalChange@endlink):  created IncrementalChange .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::IncrementalExportBuilder PcbExchange::IncrementalExportBuilder@endlink . 
    ##  @return builder (@link IncrementalExportBuilder NXOpen.PcbExchange.IncrementalExportBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateIncrementalExportBuilder(part: NXOpen.NXObject) -> IncrementalExportBuilder:
        """
         Creates an instance of @link PcbExchange::IncrementalExportBuilder PcbExchange::IncrementalExportBuilder@endlink . 
         @return builder (@link IncrementalExportBuilder NXOpen.PcbExchange.IncrementalExportBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::IncrementalImportBuilder PcbExchange::IncrementalImportBuilder@endlink . 
    ##  @return builder (@link IncrementalImportBuilder NXOpen.PcbExchange.IncrementalImportBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateIncrementalImportBuilder(part: NXOpen.NXObject) -> IncrementalImportBuilder:
        """
         Creates an instance of @link PcbExchange::IncrementalImportBuilder PcbExchange::IncrementalImportBuilder@endlink . 
         @return builder (@link IncrementalImportBuilder NXOpen.PcbExchange.IncrementalImportBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::PreferencesBuilder PcbExchange::PreferencesBuilder@endlink . 
    ##  @return builder (@link PreferencesBuilder NXOpen.PcbExchange.PreferencesBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreatePreferencesBuilder(part: NXOpen.NXObject) -> PreferencesBuilder:
        """
         Creates an instance of @link PcbExchange::PreferencesBuilder PcbExchange::PreferencesBuilder@endlink . 
         @return builder (@link PreferencesBuilder NXOpen.PcbExchange.PreferencesBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::ReportBuilder PcbExchange::ReportBuilder@endlink . 
    ##  @return builder (@link ReportBuilder NXOpen.PcbExchange.ReportBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  part 
    def CreateReportBuilder(part: NXOpen.NXObject) -> ReportBuilder:
        """
         Creates an instance of @link PcbExchange::ReportBuilder PcbExchange::ReportBuilder@endlink . 
         @return builder (@link ReportBuilder NXOpen.PcbExchange.ReportBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::TemplateBuilder PcbExchange::TemplateBuilder@endlink . 
    ##  @return builder (@link TemplateBuilder NXOpen.PcbExchange.TemplateBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateTemplateBuilder(part: NXOpen.NXObject) -> TemplateBuilder:
        """
         Creates an instance of @link PcbExchange::TemplateBuilder PcbExchange::TemplateBuilder@endlink . 
         @return builder (@link TemplateBuilder NXOpen.PcbExchange.TemplateBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates an instance of @link PcbExchange::VariantManagerBuilder PcbExchange::VariantManagerBuilder@endlink . 
    ##  @return builder (@link VariantManagerBuilder NXOpen.PcbExchange.VariantManagerBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateVariantManagerBuilder(part: NXOpen.NXObject) -> VariantManagerBuilder:
        """
         Creates an instance of @link PcbExchange::VariantManagerBuilder PcbExchange::VariantManagerBuilder@endlink . 
         @return builder (@link VariantManagerBuilder NXOpen.PcbExchange.VariantManagerBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Initialize copper for bending. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def InitializeCopperForBending() -> None:
        """
         Initialize copper for bending. 
        """
        pass
    
    ##  Updates the components using the library components. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="components"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    @staticmethod
    def ReplaceWithLibraryComponent(components: List[NXOpen.NXObject]) -> None:
        """
         Updates the components using the library components. 
        """
        pass
    
    ##  Resumes PCB exchange navigator update. 
    ## 
    ##   <br>  Created in NX1969.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## <param name="refreshNavigator"> (bool) </param>
    @staticmethod
    def ResumeNavigatorUpdate(refreshNavigator: bool) -> None:
        """
         Resumes PCB exchange navigator update. 
        """
        pass
    
    ##  Suspends PCB exchange navigator update. 
    ## 
    ##   <br>  Created in NX1969.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def SuspendNavigatorUpdate() -> None:
        """
         Suspends PCB exchange navigator update. 
        """
        pass
    
    ##  Tags the work part model as baseline. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def TagModelAsBaseline() -> None:
        """
         Tags the work part model as baseline. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::PcbExchange::NotificationManager NXOpen::PcbExchange::NotificationManager@endlink .  <br> To obtain an instance of this class, refer to @link NXOpen::PcbExchange::Manager  NXOpen::PcbExchange::Manager @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class NotificationManager(NXOpen.Object): 
    """ Represents a <ja_class>NXOpen.PcbExchange.NotificationManager</ja_class>. """


    ##  Sends a notificatoin to delete the pending component from PCB navigator. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  pending component to be deleted from PCB navigator. 
    @staticmethod
    def DeletePendingComponent(pendingComponent: str) -> None:
        """
         Sends a notificatoin to delete the pending component from PCB navigator. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::PcbExchange::PendingComponentManager NXOpen::PcbExchange::PendingComponentManager@endlink .  <br> To obtain an instance of this class, refer to @link NXOpen::PcbExchange::Manager  NXOpen::PcbExchange::Manager @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class PendingComponentManager(NXOpen.Object): 
    """ Represents a <ja_class>NXOpen.PcbExchange.PendingComponentManager</ja_class>. """


    ##  Adds the pending components. 
    ##  @return A tuple consisting of (numComponents, components). 
    ##  - numComponents is: int.
    ##  - components is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink. added components. .

    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  pending components. 
    @staticmethod
    def Add(pendingComponents: List[str], isNonGeometric: bool) -> Tuple[int, List[NXOpen.NXObject]]:
        """
         Adds the pending components. 
         @return A tuple consisting of (numComponents, components). 
         - numComponents is: int.
         - components is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink. added components. .

        """
        pass
    
    ##  Deletes the pending components. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ##  pending components. 
    @staticmethod
    def Delete(pendingComponents: List[str]) -> None:
        """
         Deletes the pending components. 
        """
        pass
    
import NXOpen
##  Represents a builder to create or edit PCB exchange preferences <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreatePreferencesBuilder  NXOpen::PcbExchange::Manager::CreatePreferencesBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class PreferencesBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit PCB exchange preferences"""


    ##  Defines the thickness source. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FromPart</term><description> 
    ## </description> </item><item><term> 
    ## Specify</term><description> 
    ## </description> </item></list>
    class BoardThicknessSourceTypeName(Enum):
        """
        Members Include: <FromPart> <Specify>
        """
        FromPart: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.BoardThicknessSourceTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the component load options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## LoadAndCreateAssemblyComponents</term><description> 
    ## </description> </item><item><term> 
    ## CreateBodiesOnly</term><description> 
    ## </description> </item><item><term> 
    ## LoadAssemblyComponentsCreateBodies</term><description> 
    ## </description> </item></list>
    class ComponentLoadOptionsTypeName(Enum):
        """
        Members Include: <LoadAndCreateAssemblyComponents> <CreateBodiesOnly> <LoadAssemblyComponentsCreateBodies>
        """
        LoadAndCreateAssemblyComponents: int
        CreateBodiesOnly: int
        LoadAssemblyComponentsCreateBodies: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentLoadOptionsTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the components connection to board type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Rbe2</term><description> 
    ## </description> </item><item><term> 
    ## Rbe3</term><description> 
    ## </description> </item></list>
    class ComponentsConnectionToBoardTypeName(Enum):
        """
        Members Include: <Rbe2> <Rbe3>
        """
        Rbe2: int
        Rbe3: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentsConnectionToBoardTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the components element size options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Auto</term><description> 
    ## </description> </item><item><term> 
    ## Specify</term><description> 
    ## </description> </item></list>
    class ComponentsElementSizeOptionsTypeName(Enum):
        """
        Members Include: <Auto> <Specify>
        """
        Auto: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentsElementSizeOptionsTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the components element thickness options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Null</term><description> 
    ## </description> </item><item><term> 
    ## Specify</term><description> 
    ## </description> </item></list>
    class ComponentsElementThicknessOptionsTypeName(Enum):
        """
        Members Include: <Null> <Specify>
        """
        Null: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentsElementThicknessOptionsTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the components height source. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FootprintDefinition</term><description> 
    ## </description> </item><item><term> 
    ## PartDefinition</term><description> 
    ## </description> </item></list>
    class ComponentsHeightFromTypeName(Enum):
        """
        Members Include: <FootprintDefinition> <PartDefinition>
        """
        FootprintDefinition: int
        PartDefinition: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentsHeightFromTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the components material source. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Pcb</term><description> 
    ## </description> </item><item><term> 
    ## Nx</term><description> 
    ## </description> </item></list>
    class ComponentsMaterialFromTypeName(Enum):
        """
        Members Include: <Pcb> <Nx>
        """
        Pcb: int
        Nx: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentsMaterialFromTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the components model type for thermal model. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ZeroResistor</term><description> 
    ## </description> </item><item><term> 
    ## OneResistor</term><description> 
    ## </description> </item><item><term> 
    ## TwoResistor</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item></list>
    class ComponentsModelTypeName(Enum):
        """
        Members Include: <ZeroResistor> <OneResistor> <TwoResistor> <NotSet>
        """
        ZeroResistor: int
        OneResistor: int
        TwoResistor: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentsModelTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the options where new components are created. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## DirectoryOfECADFiles</term><description> 
    ## </description> </item><item><term> 
    ## DirectoryOfNXParts</term><description> 
    ## </description> </item><item><term> 
    ## Specify</term><description> 
    ## </description> </item></list>
    class CreateNewComponentsInTypeName(Enum):
        """
        Members Include: <DirectoryOfECADFiles> <DirectoryOfNXParts> <Specify>
        """
        DirectoryOfECADFiles: int
        DirectoryOfNXParts: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.CreateNewComponentsInTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines how to create the PCA name. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CurrentNXModel</term><description> 
    ## </description> </item><item><term> 
    ## ECADModelName</term><description> 
    ## </description> </item><item><term> 
    ## SpecifyAtImport</term><description> 
    ## </description> </item></list>
    class DefaultPcaNameTypeName(Enum):
        """
        Members Include: <CurrentNXModel> <ECADModelName> <SpecifyAtImport>
        """
        CurrentNXModel: int
        ECADModelName: int
        SpecifyAtImport: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.DefaultPcaNameTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the mesh element type for structural analysis. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Ctria3</term><description> 
    ## </description> </item><item><term> 
    ## Cquad4</term><description> 
    ## </description> </item><item><term> 
    ## Ctria6</term><description> 
    ## </description> </item><item><term> 
    ## Cquad8</term><description> 
    ## </description> </item></list>
    class ElementTypeForStructuralAnalysisTypeName(Enum):
        """
        Members Include: <Ctria3> <Cquad4> <Ctria6> <Cquad8>
        """
        Ctria3: int
        Cquad4: int
        Ctria6: int
        Cquad8: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the way to group components. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Type</term><description> 
    ## </description> </item><item><term> 
    ## Layer</term><description> 
    ## </description> </item></list>
    class GroupEntityComponentsByTypeName(Enum):
        """
        Members Include: <NotSet> <Type> <Layer>
        """
        NotSet: int
        Type: int
        Layer: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.GroupEntityComponentsByTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines whether to import and/or export flexible printed circuit boards in their bent state instead of their flat state. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## No</term><description> 
    ## </description> </item><item><term> 
    ## ExportOnly</term><description> 
    ## </description> </item><item><term> 
    ## ImportAndExport</term><description> 
    ## </description> </item></list>
    class ImportExportFlexBentType(Enum):
        """
        Members Include: <No> <ExportOnly> <ImportAndExport>
        """
        No: int
        ExportOnly: int
        ImportAndExport: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ImportExportFlexBentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the import generic type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Curves</term><description> 
    ## </description> </item><item><term> 
    ## Sheets</term><description> 
    ## </description> </item><item><term> 
    ## Bodies</term><description> 
    ## </description> </item></list>
    class ImportGenericMenuTypeName(Enum):
        """
        Members Include: <Curves> <Sheets> <Bodies>
        """
        Curves: int
        Sheets: int
        Bodies: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ImportGenericMenuTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the import mask type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Curves</term><description> 
    ## </description> </item><item><term> 
    ## Sheets</term><description> 
    ## </description> </item><item><term> 
    ## Bodies</term><description> 
    ## </description> </item></list>
    class ImportMaskMenuTypeName(Enum):
        """
        Members Include: <Curves> <Sheets> <Bodies>
        """
        Curves: int
        Sheets: int
        Bodies: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ImportMaskMenuTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines Mask import method. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Positive</term><description> 
    ## </description> </item><item><term> 
    ## Negative</term><description> 
    ## </description> </item><item><term> 
    ## NegativeWithHoles</term><description> 
    ## </description> </item></list>
    class ImportMasksMethodType(Enum):
        """
        Members Include: <Positive> <Negative> <NegativeWithHoles>
        """
        Positive: int
        Negative: int
        NegativeWithHoles: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ImportMasksMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the import pad type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Curves</term><description> 
    ## </description> </item><item><term> 
    ## Sheets</term><description> 
    ## </description> </item><item><term> 
    ## Bodies</term><description> 
    ## </description> </item></list>
    class ImportPadMenuTypeName(Enum):
        """
        Members Include: <Curves> <Sheets> <Bodies>
        """
        Curves: int
        Sheets: int
        Bodies: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ImportPadMenuTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the import trace type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Curves</term><description> 
    ## </description> </item><item><term> 
    ## Sheets</term><description> 
    ## </description> </item><item><term> 
    ## Bodies</term><description> 
    ## </description> </item></list>
    class ImportTraceMenuTypeName(Enum):
        """
        Members Include: <Curves> <Sheets> <Bodies>
        """
        Curves: int
        Sheets: int
        Bodies: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ImportTraceMenuTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the mail protocol. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Mapi</term><description> 
    ## </description> </item><item><term> 
    ## Smtp</term><description> 
    ## </description> </item></list>
    class MailProtocolTypeName(Enum):
        """
        Members Include: <Mapi> <Smtp>
        """
        Mapi: int
        Smtp: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.MailProtocolTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the copper entity merge type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## TracesByNet</term><description> 
    ## </description> </item><item><term> 
    ## TracesAndPadsByNet</term><description> 
    ## </description> </item><item><term> 
    ## HolesAndTracesAndPadsByNet</term><description> 
    ## </description> </item></list>
    class MergeTracesAndPadsType(Enum):
        """
        Members Include: <NotSet> <TracesByNet> <TracesAndPadsByNet> <HolesAndTracesAndPadsByNet>
        """
        NotSet: int
        TracesByNet: int
        TracesAndPadsByNet: int
        HolesAndTracesAndPadsByNet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.MergeTracesAndPadsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the mesh type for structural analysis. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SingleLayer</term><description> 
    ## </description> </item><item><term> 
    ## MultiLayer</term><description> 
    ## </description> </item></list>
    class ModelForStructuralAnalysisTypeName(Enum):
        """
        Members Include: <SingleLayer> <MultiLayer>
        """
        SingleLayer: int
        MultiLayer: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ModelForStructuralAnalysisTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the mesh type for thermal analysis. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SingleLayer</term><description> 
    ## </description> </item><item><term> 
    ## TopAndBottom</term><description> 
    ## </description> </item><item><term> 
    ## MultiLayer</term><description> 
    ## </description> </item><item><term> 
    ## Solid</term><description> 
    ## </description> </item></list>
    class ModelForThermalAnalysisTypeName(Enum):
        """
        Members Include: <SingleLayer> <TopAndBottom> <MultiLayer> <Solid>
        """
        SingleLayer: int
        TopAndBottom: int
        MultiLayer: int
        Solid: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ModelForThermalAnalysisTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the default resistor model type for thermal simulations. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## DissipationOnly</term><description> 
    ## </description> </item><item><term> 
    ## ThetaCB</term><description> 
    ## </description> </item><item><term> 
    ## ThetaJCJB</term><description> 
    ## </description> </item><item><term> 
    ## ThetaJCCB</term><description> 
    ## </description> </item></list>
    class ResistorModelTypeName(Enum):
        """
        Members Include: <NotSet> <DissipationOnly> <ThetaCB> <ThetaJCJB> <ThetaJCCB>
        """
        NotSet: int
        DissipationOnly: int
        ThetaCB: int
        ThetaJCJB: int
        ThetaJCCB: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ResistorModelTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the setting source. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## IniFiles</term><description> 
    ## </description> </item><item><term> 
    ## SpecifiedSettingsFolder</term><description> 
    ## </description> </item><item><term> 
    ## CustomerDefaults</term><description> 
    ## </description> </item></list>
    class SettingsSourceTypeName(Enum):
        """
        Members Include: <IniFiles> <SpecifiedSettingsFolder> <CustomerDefaults>
        """
        IniFiles: int
        SpecifiedSettingsFolder: int
        CustomerDefaults: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.SettingsSourceTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the algorithm for structural analysis. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Equivalent</term><description> 
    ## </description> </item></list>
    class StructuralAlgorithmTypeName(Enum):
        """
        Members Include: <Equivalent>
        """
        Equivalent: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.StructuralAlgorithmTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the algorithm for thermal analysis. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Discretized</term><description> 
    ## </description> </item><item><term> 
    ## Equivalent</term><description> 
    ## </description> </item></list>
    class ThermalAlgorithmTypeName(Enum):
        """
        Members Include: <Discretized> <Equivalent>
        """
        Discretized: int
        Equivalent: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ThermalAlgorithmTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the board thickness source for structural analysis. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FromPart</term><description> 
    ## </description> </item><item><term> 
    ## Specify</term><description> 
    ## </description> </item></list>
    class ThicknessSourceForStructuralAnalysisTypeName(Enum):
        """
        Members Include: <FromPart> <Specify>
        """
        FromPart: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) AreaNamePrefix
    ##   the area name prefix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def AreaNamePrefix(self) -> str:
        """
        Getter for property: (str) AreaNamePrefix
          the area name prefix.  
             
         
        """
        pass
    
    ## Setter for property: (str) AreaNamePrefix

    ##   the area name prefix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AreaNamePrefix.setter
    def AreaNamePrefix(self, mAreaNamePrefix: str):
        """
        Setter for property: (str) AreaNamePrefix
          the area name prefix.  
             
         
        """
        pass
    
    ## Getter for property: (str) AreaNameSuffix
    ##   the area name suffix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def AreaNameSuffix(self) -> str:
        """
        Getter for property: (str) AreaNameSuffix
          the area name suffix.  
             
         
        """
        pass
    
    ## Setter for property: (str) AreaNameSuffix

    ##   the area name suffix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AreaNameSuffix.setter
    def AreaNameSuffix(self, mAreaNameSuffix: str):
        """
        Setter for property: (str) AreaNameSuffix
          the area name suffix.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AreasAsAssemblyComponents
    ##   the flag indicating whether to create areas as assembly components.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def AreasAsAssemblyComponents(self) -> bool:
        """
        Getter for property: (bool) AreasAsAssemblyComponents
          the flag indicating whether to create areas as assembly components.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AreasAsAssemblyComponents

    ##   the flag indicating whether to create areas as assembly components.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AreasAsAssemblyComponents.setter
    def AreasAsAssemblyComponents(self, mAreasAsAssemblyComponents: bool):
        """
        Setter for property: (bool) AreasAsAssemblyComponents
          the flag indicating whether to create areas as assembly components.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AssociateAreaBodies
    ##   the flag indicating whether to associate areas as bodies.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def AssociateAreaBodies(self) -> bool:
        """
        Getter for property: (bool) AssociateAreaBodies
          the flag indicating whether to associate areas as bodies.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AssociateAreaBodies

    ##   the flag indicating whether to associate areas as bodies.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @AssociateAreaBodies.setter
    def AssociateAreaBodies(self, associateAreaBodies: bool):
        """
        Setter for property: (bool) AssociateAreaBodies
          the flag indicating whether to associate areas as bodies.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AssociateComponentBodies
    ##   the flag indicating whether to associate components as bodies.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def AssociateComponentBodies(self) -> bool:
        """
        Getter for property: (bool) AssociateComponentBodies
          the flag indicating whether to associate components as bodies.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AssociateComponentBodies

    ##   the flag indicating whether to associate components as bodies.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @AssociateComponentBodies.setter
    def AssociateComponentBodies(self, associateComponentBodies: bool):
        """
        Setter for property: (bool) AssociateComponentBodies
          the flag indicating whether to associate components as bodies.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AssociateCopperObjects
    ##   the flag indicating whether to associate copper objects.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def AssociateCopperObjects(self) -> bool:
        """
        Getter for property: (bool) AssociateCopperObjects
          the flag indicating whether to associate copper objects.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AssociateCopperObjects

    ##   the flag indicating whether to associate copper objects.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @AssociateCopperObjects.setter
    def AssociateCopperObjects(self, associateCopperObjects: bool):
        """
        Setter for property: (bool) AssociateCopperObjects
          the flag indicating whether to associate copper objects.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticallySaveAllCreatedParts
    ##   the flag indicating whether to automatically save all created parts.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def AutomaticallySaveAllCreatedParts(self) -> bool:
        """
        Getter for property: (bool) AutomaticallySaveAllCreatedParts
          the flag indicating whether to automatically save all created parts.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticallySaveAllCreatedParts

    ##   the flag indicating whether to automatically save all created parts.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AutomaticallySaveAllCreatedParts.setter
    def AutomaticallySaveAllCreatedParts(self, mAutomaticallySaveAllCreatedParts: bool):
        """
        Setter for property: (bool) AutomaticallySaveAllCreatedParts
          the flag indicating whether to automatically save all created parts.  
             
         
        """
        pass
    
    ## Getter for property: (bool) BoardAsAssemblyComponent
    ##   the flag indicating whether to create the board as an assembly component.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def BoardAsAssemblyComponent(self) -> bool:
        """
        Getter for property: (bool) BoardAsAssemblyComponent
          the flag indicating whether to create the board as an assembly component.  
             
         
        """
        pass
    
    ## Setter for property: (bool) BoardAsAssemblyComponent

    ##   the flag indicating whether to create the board as an assembly component.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @BoardAsAssemblyComponent.setter
    def BoardAsAssemblyComponent(self, mBoardAsAssemblyComponent: bool):
        """
        Setter for property: (bool) BoardAsAssemblyComponent
          the flag indicating whether to create the board as an assembly component.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BoardColor
    ##   the board color.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def BoardColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BoardColor
          the board color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BoardColor

    ##   the board color.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @BoardColor.setter
    def BoardColor(self, mBoardColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BoardColor
          the board color.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardDefaultPlatingThickness
    ##   the plating thickness for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BoardDefaultPlatingThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardDefaultPlatingThickness
          the plating thickness for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardDefaultThickness
    ##   the board default thickness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BoardDefaultThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardDefaultThickness
          the board default thickness.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardDefaultTraceThickness
    ##   the trace thickness for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BoardDefaultTraceThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardDefaultTraceThickness
          the trace thickness for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BoardElementColor
    ##   the board mesh element color for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def BoardElementColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BoardElementColor
          the board mesh element color for thermal analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BoardElementColor

    ##   the board mesh element color for thermal analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BoardElementColor.setter
    def BoardElementColor(self, mBoardElementColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BoardElementColor
          the board mesh element color for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardElementSize
    ##   the board mesh element size for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BoardElementSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardElementSize
          the board mesh element size for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (int) BoardLayer
    ##   the board layer.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def BoardLayer(self) -> int:
        """
        Getter for property: (int) BoardLayer
          the board layer.  
             
         
        """
        pass
    
    ## Setter for property: (int) BoardLayer

    ##   the board layer.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @BoardLayer.setter
    def BoardLayer(self, mBoardLayer: int):
        """
        Setter for property: (int) BoardLayer
          the board layer.  
             
         
        """
        pass
    
    ## Getter for property: (str) BoardNamePrefix
    ##   the board name prefix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def BoardNamePrefix(self) -> str:
        """
        Getter for property: (str) BoardNamePrefix
          the board name prefix.  
             
         
        """
        pass
    
    ## Setter for property: (str) BoardNamePrefix

    ##   the board name prefix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @BoardNamePrefix.setter
    def BoardNamePrefix(self, mBoardNamePrefix: str):
        """
        Setter for property: (str) BoardNamePrefix
          the board name prefix.  
             
         
        """
        pass
    
    ## Getter for property: (str) BoardNameSuffix
    ##   the board name suffix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def BoardNameSuffix(self) -> str:
        """
        Getter for property: (str) BoardNameSuffix
          the board name suffix.  
             
         
        """
        pass
    
    ## Setter for property: (str) BoardNameSuffix

    ##   the board name suffix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @BoardNameSuffix.setter
    def BoardNameSuffix(self, mBoardNameSuffix: str):
        """
        Setter for property: (str) BoardNameSuffix
          the board name suffix.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardThickness
    ##   the specified board thickness for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BoardThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoardThickness
          the specified board thickness for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.BoardThicknessSourceTypeName NXOpen.PcbExchange.PreferencesBuilder.BoardThicknessSourceTypeName@endlink) BoardThicknessSource
    ##   the board thickness source for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PreferencesBuilder.BoardThicknessSourceTypeName
    @property
    def BoardThicknessSource(self) -> PreferencesBuilder.BoardThicknessSourceTypeName:
        """
        Getter for property: (@link PreferencesBuilder.BoardThicknessSourceTypeName NXOpen.PcbExchange.PreferencesBuilder.BoardThicknessSourceTypeName@endlink) BoardThicknessSource
          the board thickness source for thermal analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.BoardThicknessSourceTypeName NXOpen.PcbExchange.PreferencesBuilder.BoardThicknessSourceTypeName@endlink) BoardThicknessSource

    ##   the board thickness source for thermal analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BoardThicknessSource.setter
    def BoardThicknessSource(self, mBoardThicknessSource: PreferencesBuilder.BoardThicknessSourceTypeName):
        """
        Setter for property: (@link PreferencesBuilder.BoardThicknessSourceTypeName NXOpen.PcbExchange.PreferencesBuilder.BoardThicknessSourceTypeName@endlink) BoardThicknessSource
          the board thickness source for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (int) BoardTranslucency
    ##   the board translucency.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def BoardTranslucency(self) -> int:
        """
        Getter for property: (int) BoardTranslucency
          the board translucency.  
             
         
        """
        pass
    
    ## Setter for property: (int) BoardTranslucency

    ##   the board translucency.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @BoardTranslucency.setter
    def BoardTranslucency(self, mBoardTranslucency: int):
        """
        Setter for property: (int) BoardTranslucency
          the board translucency.  
             
         
        """
        pass
    
    ## Getter for property: (str) BrowseEcadFilesFromDir
    ##   the ECAD files directory.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def BrowseEcadFilesFromDir(self) -> str:
        """
        Getter for property: (str) BrowseEcadFilesFromDir
          the ECAD files directory.  
             
         
        """
        pass
    
    ## Setter for property: (str) BrowseEcadFilesFromDir

    ##   the ECAD files directory.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @BrowseEcadFilesFromDir.setter
    def BrowseEcadFilesFromDir(self, foldername: str):
        """
        Setter for property: (str) BrowseEcadFilesFromDir
          the ECAD files directory.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ComparePrimaryPinLocations
    ##   the flag indicating whether to compare primary pin locations.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ComparePrimaryPinLocations(self) -> bool:
        """
        Getter for property: (bool) ComparePrimaryPinLocations
          the flag indicating whether to compare primary pin locations.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ComparePrimaryPinLocations

    ##   the flag indicating whether to compare primary pin locations.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ComparePrimaryPinLocations.setter
    def ComparePrimaryPinLocations(self, mComparePrimaryPinLocations: bool):
        """
        Setter for property: (bool) ComparePrimaryPinLocations
          the flag indicating whether to compare primary pin locations.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ComponentLoadOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentLoadOptionsTypeName@endlink) ComponentLoadOptions
    ##   the component load options.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PreferencesBuilder.ComponentLoadOptionsTypeName
    @property
    def ComponentLoadOptions(self) -> PreferencesBuilder.ComponentLoadOptionsTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ComponentLoadOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentLoadOptionsTypeName@endlink) ComponentLoadOptions
          the component load options.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ComponentLoadOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentLoadOptionsTypeName@endlink) ComponentLoadOptions

    ##   the component load options.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ComponentLoadOptions.setter
    def ComponentLoadOptions(self, mComponentLoadOptions: PreferencesBuilder.ComponentLoadOptionsTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ComponentLoadOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentLoadOptionsTypeName@endlink) ComponentLoadOptions
          the component load options.  
             
         
        """
        pass
    
    ## Getter for property: (str) ComponentNamePrefix
    ##   the component name prefix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def ComponentNamePrefix(self) -> str:
        """
        Getter for property: (str) ComponentNamePrefix
          the component name prefix.  
             
         
        """
        pass
    
    ## Setter for property: (str) ComponentNamePrefix

    ##   the component name prefix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ComponentNamePrefix.setter
    def ComponentNamePrefix(self, mComponentNamePrefix: str):
        """
        Setter for property: (str) ComponentNamePrefix
          the component name prefix.  
             
         
        """
        pass
    
    ## Getter for property: (str) ComponentNameSuffix
    ##   the component name suffix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def ComponentNameSuffix(self) -> str:
        """
        Getter for property: (str) ComponentNameSuffix
          the component name suffix.  
             
         
        """
        pass
    
    ## Setter for property: (str) ComponentNameSuffix

    ##   the component name suffix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ComponentNameSuffix.setter
    def ComponentNameSuffix(self, mComponentNameSuffix: str):
        """
        Setter for property: (str) ComponentNameSuffix
          the component name suffix.  
             
         
        """
        pass
    
    ## Getter for property: (str) ComponentXMLFileBrowse
    ##   the component XML file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def ComponentXMLFileBrowse(self) -> str:
        """
        Getter for property: (str) ComponentXMLFileBrowse
          the component XML file.  
             
         
        """
        pass
    
    ## Setter for property: (str) ComponentXMLFileBrowse

    ##   the component XML file.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ComponentXMLFileBrowse.setter
    def ComponentXMLFileBrowse(self, filename: str):
        """
        Setter for property: (str) ComponentXMLFileBrowse
          the component XML file.  
             
         
        """
        pass
    
    ## Getter for property: (int) ComponentsCaseMaterial
    ##   the component case material.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def ComponentsCaseMaterial(self) -> int:
        """
        Getter for property: (int) ComponentsCaseMaterial
          the component case material.  
             
         
        """
        pass
    
    ## Setter for property: (int) ComponentsCaseMaterial

    ##   the component case material.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ComponentsCaseMaterial.setter
    def ComponentsCaseMaterial(self, mMaterial: int):
        """
        Setter for property: (int) ComponentsCaseMaterial
          the component case material.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ComponentsColor
    ##   the component color.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def ComponentsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ComponentsColor
          the component color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ComponentsColor

    ##   the component color.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ComponentsColor.setter
    def ComponentsColor(self, mComponentsColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ComponentsColor
          the component color.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ComponentsConnectionToBoardTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsConnectionToBoardTypeName@endlink) ComponentsConnectionToBoard
    ##   the method by which components are connected to the board for structural analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PreferencesBuilder.ComponentsConnectionToBoardTypeName
    @property
    def ComponentsConnectionToBoard(self) -> PreferencesBuilder.ComponentsConnectionToBoardTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ComponentsConnectionToBoardTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsConnectionToBoardTypeName@endlink) ComponentsConnectionToBoard
          the method by which components are connected to the board for structural analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ComponentsConnectionToBoardTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsConnectionToBoardTypeName@endlink) ComponentsConnectionToBoard

    ##   the method by which components are connected to the board for structural analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ComponentsConnectionToBoard.setter
    def ComponentsConnectionToBoard(self, mComponentsConnectionToBoard: PreferencesBuilder.ComponentsConnectionToBoardTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ComponentsConnectionToBoardTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsConnectionToBoardTypeName@endlink) ComponentsConnectionToBoard
          the method by which components are connected to the board for structural analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsDefaultHeight
    ##   the component default height.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsDefaultHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsDefaultHeight
          the component default height.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsDefaultMass
    ##   the default component mass for structural analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsDefaultMass(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsDefaultMass
          the default component mass for structural analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsDissipation
    ##   the dissipation rate for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsDissipation(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsDissipation
          the dissipation rate for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ComponentsElementColor
    ##   the component mesh element color for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def ComponentsElementColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ComponentsElementColor
          the component mesh element color for thermal analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ComponentsElementColor

    ##   the component mesh element color for thermal analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ComponentsElementColor.setter
    def ComponentsElementColor(self, mComponentsElementColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ComponentsElementColor
          the component mesh element color for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ComponentsElementSizeOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsElementSizeOptionsTypeName@endlink) ComponentsElementSizeOptions
    ##   the component mesh element size option for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PreferencesBuilder.ComponentsElementSizeOptionsTypeName
    @property
    def ComponentsElementSizeOptions(self) -> PreferencesBuilder.ComponentsElementSizeOptionsTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ComponentsElementSizeOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsElementSizeOptionsTypeName@endlink) ComponentsElementSizeOptions
          the component mesh element size option for thermal analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ComponentsElementSizeOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsElementSizeOptionsTypeName@endlink) ComponentsElementSizeOptions

    ##   the component mesh element size option for thermal analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ComponentsElementSizeOptions.setter
    def ComponentsElementSizeOptions(self, mComponentsElementSizeOptions: PreferencesBuilder.ComponentsElementSizeOptionsTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ComponentsElementSizeOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsElementSizeOptionsTypeName@endlink) ComponentsElementSizeOptions
          the component mesh element size option for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsElementSizeValue
    ##   the component mesh element size for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsElementSizeValue(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsElementSizeValue
          the component mesh element size for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ComponentsElementThicknessOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsElementThicknessOptionsTypeName@endlink) ComponentsElementThicknessOptions
    ##   the component thickness option for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PreferencesBuilder.ComponentsElementThicknessOptionsTypeName
    @property
    def ComponentsElementThicknessOptions(self) -> PreferencesBuilder.ComponentsElementThicknessOptionsTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ComponentsElementThicknessOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsElementThicknessOptionsTypeName@endlink) ComponentsElementThicknessOptions
          the component thickness option for thermal analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ComponentsElementThicknessOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsElementThicknessOptionsTypeName@endlink) ComponentsElementThicknessOptions

    ##   the component thickness option for thermal analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ComponentsElementThicknessOptions.setter
    def ComponentsElementThicknessOptions(self, mComponentsElementThicknessOptions: PreferencesBuilder.ComponentsElementThicknessOptionsTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ComponentsElementThicknessOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsElementThicknessOptionsTypeName@endlink) ComponentsElementThicknessOptions
          the component thickness option for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsElementThicknessValue
    ##   the component thickness for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsElementThicknessValue(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsElementThicknessValue
          the component thickness for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ComponentsHeightFromTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsHeightFromTypeName@endlink) ComponentsHeightFrom
    ##   the component height source.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PreferencesBuilder.ComponentsHeightFromTypeName
    @property
    def ComponentsHeightFrom(self) -> PreferencesBuilder.ComponentsHeightFromTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ComponentsHeightFromTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsHeightFromTypeName@endlink) ComponentsHeightFrom
          the component height source.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ComponentsHeightFromTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsHeightFromTypeName@endlink) ComponentsHeightFrom

    ##   the component height source.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ComponentsHeightFrom.setter
    def ComponentsHeightFrom(self, mComponentsHeightFrom: PreferencesBuilder.ComponentsHeightFromTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ComponentsHeightFromTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsHeightFromTypeName@endlink) ComponentsHeightFrom
          the component height source.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsJunctionCapacitance
    ##   the junction capacitance for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsJunctionCapacitance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsJunctionCapacitance
          the junction capacitance for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsJunctionCapacity
    ##   the junction capacitance for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::PcbExchange::PreferencesBuilder::ComponentsJunctionCapacitance NXOpen::PcbExchange::PreferencesBuilder::ComponentsJunctionCapacitance@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsJunctionCapacity(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsJunctionCapacity
          the junction capacitance for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ComponentsMaterialFromTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsMaterialFromTypeName@endlink) ComponentsMaterialFrom
    ##   the source library for component materials.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PreferencesBuilder.ComponentsMaterialFromTypeName
    @property
    def ComponentsMaterialFrom(self) -> PreferencesBuilder.ComponentsMaterialFromTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ComponentsMaterialFromTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsMaterialFromTypeName@endlink) ComponentsMaterialFrom
          the source library for component materials.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ComponentsMaterialFromTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsMaterialFromTypeName@endlink) ComponentsMaterialFrom

    ##   the source library for component materials.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ComponentsMaterialFrom.setter
    def ComponentsMaterialFrom(self, mComponentsMaterialFrom: PreferencesBuilder.ComponentsMaterialFromTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ComponentsMaterialFromTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsMaterialFromTypeName@endlink) ComponentsMaterialFrom
          the source library for component materials.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ComponentsModelTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsModelTypeName@endlink) ComponentsModel
    ##   the component model for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::PcbExchange::PreferencesBuilder::ResistorModel NXOpen::PcbExchange::PreferencesBuilder::ResistorModel@endlink  instead.  <br> 

    ## @return PreferencesBuilder.ComponentsModelTypeName
    @property
    def ComponentsModel(self) -> PreferencesBuilder.ComponentsModelTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ComponentsModelTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsModelTypeName@endlink) ComponentsModel
          the component model for thermal analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ComponentsModelTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsModelTypeName@endlink) ComponentsModel

    ##   the component model for thermal analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::PcbExchange::PreferencesBuilder::SetResistorModel NXOpen::PcbExchange::PreferencesBuilder::SetResistorModel@endlink  instead.  <br> 

    @ComponentsModel.setter
    def ComponentsModel(self, mComponentsModel: PreferencesBuilder.ComponentsModelTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ComponentsModelTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsModelTypeName@endlink) ComponentsModel
          the component model for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsThetaCB
    ##   the component-to-board resistance for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsThetaCB(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsThetaCB
          the component-to-board resistance for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsThetaJB
    ##   the junction-to-board resistance for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsThetaJB(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsThetaJB
          the junction-to-board resistance for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsThetaJC
    ##   the component-to-junction resistance for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsThetaJC(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsThetaJC
          the component-to-junction resistance for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsTmax
    ##   the maximum component temperature for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsTmax(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsTmax
          the maximum component temperature for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsTmaxCase
    ##   the maximum case temperature for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsTmaxCase(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsTmaxCase
          the maximum case temperature for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsTmaxJunction
    ##   the maximum junction temperature for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ComponentsTmaxJunction(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ComponentsTmaxJunction
          the maximum junction temperature for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (int) ComponentsTranslucency
    ##   the component translucency.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def ComponentsTranslucency(self) -> int:
        """
        Getter for property: (int) ComponentsTranslucency
          the component translucency.  
             
         
        """
        pass
    
    ## Setter for property: (int) ComponentsTranslucency

    ##   the component translucency.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ComponentsTranslucency.setter
    def ComponentsTranslucency(self, mComponentsTranslucency: int):
        """
        Setter for property: (int) ComponentsTranslucency
          the component translucency.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ConnectComponentsToPads
    ##   the flag indicating whether to use component model with pads if the resistor model allows it.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def ConnectComponentsToPads(self) -> bool:
        """
        Getter for property: (bool) ConnectComponentsToPads
          the flag indicating whether to use component model with pads if the resistor model allows it.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ConnectComponentsToPads

    ##   the flag indicating whether to use component model with pads if the resistor model allows it.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ConnectComponentsToPads.setter
    def ConnectComponentsToPads(self, connectComponentsToPads: bool):
        """
        Setter for property: (bool) ConnectComponentsToPads
          the flag indicating whether to use component model with pads if the resistor model allows it.  
             
         
        """
        pass
    
    ## Getter for property: (str) CreateNewComponentInDir
    ##   the directory where new components are created.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def CreateNewComponentInDir(self) -> str:
        """
        Getter for property: (str) CreateNewComponentInDir
          the directory where new components are created.  
             
         
        """
        pass
    
    ## Setter for property: (str) CreateNewComponentInDir

    ##   the directory where new components are created.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CreateNewComponentInDir.setter
    def CreateNewComponentInDir(self, foldername: str):
        """
        Setter for property: (str) CreateNewComponentInDir
          the directory where new components are created.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.CreateNewComponentsInTypeName NXOpen.PcbExchange.PreferencesBuilder.CreateNewComponentsInTypeName@endlink) CreateNewComponentsIn
    ##   the create new components option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PreferencesBuilder.CreateNewComponentsInTypeName
    @property
    def CreateNewComponentsIn(self) -> PreferencesBuilder.CreateNewComponentsInTypeName:
        """
        Getter for property: (@link PreferencesBuilder.CreateNewComponentsInTypeName NXOpen.PcbExchange.PreferencesBuilder.CreateNewComponentsInTypeName@endlink) CreateNewComponentsIn
          the create new components option.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.CreateNewComponentsInTypeName NXOpen.PcbExchange.PreferencesBuilder.CreateNewComponentsInTypeName@endlink) CreateNewComponentsIn

    ##   the create new components option.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CreateNewComponentsIn.setter
    def CreateNewComponentsIn(self, mCreateNewComponentsIn: PreferencesBuilder.CreateNewComponentsInTypeName):
        """
        Setter for property: (@link PreferencesBuilder.CreateNewComponentsInTypeName NXOpen.PcbExchange.PreferencesBuilder.CreateNewComponentsInTypeName@endlink) CreateNewComponentsIn
          the create new components option.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateTempBoard
    ##   the flag indicating whether to create a new temporary board if required when updating the NX model.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateTempBoard(self) -> bool:
        """
        Getter for property: (bool) CreateTempBoard
          the flag indicating whether to create a new temporary board if required when updating the NX model.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateTempBoard

    ##   the flag indicating whether to create a new temporary board if required when updating the NX model.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateTempBoard.setter
    def CreateTempBoard(self, createTempBoard: bool):
        """
        Setter for property: (bool) CreateTempBoard
          the flag indicating whether to create a new temporary board if required when updating the NX model.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.DefaultPcaNameTypeName NXOpen.PcbExchange.PreferencesBuilder.DefaultPcaNameTypeName@endlink) DefaultPcaName
    ##   the default PCA name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PreferencesBuilder.DefaultPcaNameTypeName
    @property
    def DefaultPcaName(self) -> PreferencesBuilder.DefaultPcaNameTypeName:
        """
        Getter for property: (@link PreferencesBuilder.DefaultPcaNameTypeName NXOpen.PcbExchange.PreferencesBuilder.DefaultPcaNameTypeName@endlink) DefaultPcaName
          the default PCA name.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.DefaultPcaNameTypeName NXOpen.PcbExchange.PreferencesBuilder.DefaultPcaNameTypeName@endlink) DefaultPcaName

    ##   the default PCA name.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DefaultPcaName.setter
    def DefaultPcaName(self, mDefaultPcaName: PreferencesBuilder.DefaultPcaNameTypeName):
        """
        Setter for property: (@link PreferencesBuilder.DefaultPcaNameTypeName NXOpen.PcbExchange.PreferencesBuilder.DefaultPcaNameTypeName@endlink) DefaultPcaName
          the default PCA name.  
             
         
        """
        pass
    
    ## Getter for property: (str) EcadFilePostProcessor
    ##   the ECAD file post processor text.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def EcadFilePostProcessor(self) -> str:
        """
        Getter for property: (str) EcadFilePostProcessor
          the ECAD file post processor text.  
             
         
        """
        pass
    
    ## Setter for property: (str) EcadFilePostProcessor

    ##   the ECAD file post processor text.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EcadFilePostProcessor.setter
    def EcadFilePostProcessor(self, mEcadFilePostProcessor: str):
        """
        Setter for property: (str) EcadFilePostProcessor
          the ECAD file post processor text.  
             
         
        """
        pass
    
    ## Getter for property: (str) EcadFilePreProcessor
    ##   the ECAD file pre processor text.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def EcadFilePreProcessor(self) -> str:
        """
        Getter for property: (str) EcadFilePreProcessor
          the ECAD file pre processor text.  
             
         
        """
        pass
    
    ## Setter for property: (str) EcadFilePreProcessor

    ##   the ECAD file pre processor text.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EcadFilePreProcessor.setter
    def EcadFilePreProcessor(self, mEcadFilePreProcessor: str):
        """
        Setter for property: (str) EcadFilePreProcessor
          the ECAD file pre processor text.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EcadFloatTolerance
    ##   the ECAD float tolerance.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EcadFloatTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EcadFloatTolerance
          the ECAD float tolerance.  
             
         
        """
        pass
    
    ## Getter for property: (str) EdmdDir
    ##   the EDMD directory.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def EdmdDir(self) -> str:
        """
        Getter for property: (str) EdmdDir
          the EDMD directory.  
             
         
        """
        pass
    
    ## Setter for property: (str) EdmdDir

    ##   the EDMD directory.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EdmdDir.setter
    def EdmdDir(self, foldername: str):
        """
        Setter for property: (str) EdmdDir
          the EDMD directory.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ElementColorForStructuralAnalysis
    ##   the mesh element color for structural analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def ElementColorForStructuralAnalysis(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ElementColorForStructuralAnalysis
          the mesh element color for structural analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ElementColorForStructuralAnalysis

    ##   the mesh element color for structural analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ElementColorForStructuralAnalysis.setter
    def ElementColorForStructuralAnalysis(self, mElementColorForStructuralAnalysis: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ElementColorForStructuralAnalysis
          the mesh element color for structural analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ElementSizeForStructuralAnalysis
    ##   the mesh element size for structural analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ElementSizeForStructuralAnalysis(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ElementSizeForStructuralAnalysis
          the mesh element size for structural analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName@endlink) ElementTypeForStructuralAnalysis
    ##   the mesh element type for structural analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName
    @property
    def ElementTypeForStructuralAnalysis(self) -> PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName@endlink) ElementTypeForStructuralAnalysis
          the mesh element type for structural analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName@endlink) ElementTypeForStructuralAnalysis

    ##   the mesh element type for structural analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ElementTypeForStructuralAnalysis.setter
    def ElementTypeForStructuralAnalysis(self, mElementTypeForStructuralAnalysis: PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName@endlink) ElementTypeForStructuralAnalysis
          the mesh element type for structural analysis.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ErrorChecking
    ##   the error checking state.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ErrorChecking(self) -> bool:
        """
        Getter for property: (bool) ErrorChecking
          the error checking state.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ErrorChecking

    ##   the error checking state.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ErrorChecking.setter
    def ErrorChecking(self, mErrorChecking: bool):
        """
        Setter for property: (bool) ErrorChecking
          the error checking state.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ExportBends
    ##   the flag indicating whether to export bends.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ExportBends(self) -> bool:
        """
        Getter for property: (bool) ExportBends
          the flag indicating whether to export bends.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ExportBends

    ##   the flag indicating whether to export bends.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ExportBends.setter
    def ExportBends(self, mExportBends: bool):
        """
        Setter for property: (bool) ExportBends
          the flag indicating whether to export bends.  
             
         
        """
        pass
    
    ## Getter for property: (bool) FilterEcadToggle
    ##   the flag indicating whether to filter the ECAD model.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def FilterEcadToggle(self) -> bool:
        """
        Getter for property: (bool) FilterEcadToggle
          the flag indicating whether to filter the ECAD model.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FilterEcadToggle

    ##   the flag indicating whether to filter the ECAD model.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @FilterEcadToggle.setter
    def FilterEcadToggle(self, mFilterEcadToggle: bool):
        """
        Setter for property: (bool) FilterEcadToggle
          the flag indicating whether to filter the ECAD model.  
             
         
        """
        pass
    
    ## Getter for property: (bool) FilterMcadToggle
    ##   the flag indicating whether to filter the MCAD model.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def FilterMcadToggle(self) -> bool:
        """
        Getter for property: (bool) FilterMcadToggle
          the flag indicating whether to filter the MCAD model.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FilterMcadToggle

    ##   the flag indicating whether to filter the MCAD model.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @FilterMcadToggle.setter
    def FilterMcadToggle(self, mFilterMcadToggle: bool):
        """
        Setter for property: (bool) FilterMcadToggle
          the flag indicating whether to filter the MCAD model.  
             
         
        """
        pass
    
    ## Getter for property: (int) GenericMaxNumber
    ##   the generic shapes max number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def GenericMaxNumber(self) -> int:
        """
        Getter for property: (int) GenericMaxNumber
          the generic shapes max number.  
             
         
        """
        pass
    
    ## Setter for property: (int) GenericMaxNumber

    ##   the generic shapes max number.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @GenericMaxNumber.setter
    def GenericMaxNumber(self, mGenericMaxNumber: int):
        """
        Setter for property: (int) GenericMaxNumber
          the generic shapes max number.  
             
         
        """
        pass
    
    ## Getter for property: (str) GenericNamePrefix
    ##   the generic shapes name prefix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def GenericNamePrefix(self) -> str:
        """
        Getter for property: (str) GenericNamePrefix
          the generic shapes name prefix.  
             
         
        """
        pass
    
    ## Setter for property: (str) GenericNamePrefix

    ##   the generic shapes name prefix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @GenericNamePrefix.setter
    def GenericNamePrefix(self, mGenericNamePrefix: str):
        """
        Setter for property: (str) GenericNamePrefix
          the generic shapes name prefix.  
             
         
        """
        pass
    
    ## Getter for property: (str) GenericNameSuffix
    ##   the generic shapes name suffix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def GenericNameSuffix(self) -> str:
        """
        Getter for property: (str) GenericNameSuffix
          the generic shapes name suffix.  
             
         
        """
        pass
    
    ## Setter for property: (str) GenericNameSuffix

    ##   the generic shapes name suffix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @GenericNameSuffix.setter
    def GenericNameSuffix(self, mGenericNameSuffix: str):
        """
        Setter for property: (str) GenericNameSuffix
          the generic shapes name suffix.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.GroupEntityComponentsByTypeName NXOpen.PcbExchange.PreferencesBuilder.GroupEntityComponentsByTypeName@endlink) GroupEntityComponentsBy
    ##   the group entity option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PreferencesBuilder.GroupEntityComponentsByTypeName
    @property
    def GroupEntityComponentsBy(self) -> PreferencesBuilder.GroupEntityComponentsByTypeName:
        """
        Getter for property: (@link PreferencesBuilder.GroupEntityComponentsByTypeName NXOpen.PcbExchange.PreferencesBuilder.GroupEntityComponentsByTypeName@endlink) GroupEntityComponentsBy
          the group entity option.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.GroupEntityComponentsByTypeName NXOpen.PcbExchange.PreferencesBuilder.GroupEntityComponentsByTypeName@endlink) GroupEntityComponentsBy

    ##   the group entity option.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @GroupEntityComponentsBy.setter
    def GroupEntityComponentsBy(self, mGroupEntityComponentsBy: PreferencesBuilder.GroupEntityComponentsByTypeName):
        """
        Setter for property: (@link PreferencesBuilder.GroupEntityComponentsByTypeName NXOpen.PcbExchange.PreferencesBuilder.GroupEntityComponentsByTypeName@endlink) GroupEntityComponentsBy
          the group entity option.  
             
         
        """
        pass
    
    ## Getter for property: (bool) GroupPads
    ##   the flag indicating whether to group pads.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def GroupPads(self) -> bool:
        """
        Getter for property: (bool) GroupPads
          the flag indicating whether to group pads.  
             
         
        """
        pass
    
    ## Setter for property: (bool) GroupPads

    ##   the flag indicating whether to group pads.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @GroupPads.setter
    def GroupPads(self, mGroupPads: bool):
        """
        Setter for property: (bool) GroupPads
          the flag indicating whether to group pads.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HolesDefaultDiameter
    ##   the default hole diameter.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HolesDefaultDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HolesDefaultDiameter
          the default hole diameter.  
             
         
        """
        pass
    
    ## Getter for property: (int) IdfFloatPrecision
    ##   the IDF float precision.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def IdfFloatPrecision(self) -> int:
        """
        Getter for property: (int) IdfFloatPrecision
          the IDF float precision.  
             
         
        """
        pass
    
    ## Setter for property: (int) IdfFloatPrecision

    ##   the IDF float precision.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @IdfFloatPrecision.setter
    def IdfFloatPrecision(self, mIdfFloatPrecision: int):
        """
        Setter for property: (int) IdfFloatPrecision
          the IDF float precision.  
             
         
        """
        pass
    
    ## Getter for property: (int) IdfFloatWidth
    ##   the IDF float width.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def IdfFloatWidth(self) -> int:
        """
        Getter for property: (int) IdfFloatWidth
          the IDF float width.  
             
         
        """
        pass
    
    ## Setter for property: (int) IdfFloatWidth

    ##   the IDF float width.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @IdfFloatWidth.setter
    def IdfFloatWidth(self, mIdfFloatWidth: int):
        """
        Setter for property: (int) IdfFloatWidth
          the IDF float width.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ImportBends
    ##   the flag indicating whether to import bends.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ImportBends(self) -> bool:
        """
        Getter for property: (bool) ImportBends
          the flag indicating whether to import bends.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ImportBends

    ##   the flag indicating whether to import bends.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ImportBends.setter
    def ImportBends(self, mImportBends: bool):
        """
        Setter for property: (bool) ImportBends
          the flag indicating whether to import bends.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ImportExportFlexBentType NXOpen.PcbExchange.PreferencesBuilder.ImportExportFlexBentType@endlink) ImportExportFlexBent
    ##   the defining state for flags of whether to import and/or export flexible printed circuit boards in their bent state instead of their flat state.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return PreferencesBuilder.ImportExportFlexBentType
    @property
    def ImportExportFlexBent(self) -> PreferencesBuilder.ImportExportFlexBentType:
        """
        Getter for property: (@link PreferencesBuilder.ImportExportFlexBentType NXOpen.PcbExchange.PreferencesBuilder.ImportExportFlexBentType@endlink) ImportExportFlexBent
          the defining state for flags of whether to import and/or export flexible printed circuit boards in their bent state instead of their flat state.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ImportExportFlexBentType NXOpen.PcbExchange.PreferencesBuilder.ImportExportFlexBentType@endlink) ImportExportFlexBent

    ##   the defining state for flags of whether to import and/or export flexible printed circuit boards in their bent state instead of their flat state.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ImportExportFlexBent.setter
    def ImportExportFlexBent(self, importExportFlexBent: PreferencesBuilder.ImportExportFlexBentType):
        """
        Setter for property: (@link PreferencesBuilder.ImportExportFlexBentType NXOpen.PcbExchange.PreferencesBuilder.ImportExportFlexBentType@endlink) ImportExportFlexBent
          the defining state for flags of whether to import and/or export flexible printed circuit boards in their bent state instead of their flat state.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ImportGenericMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportGenericMenuTypeName@endlink) ImportGenericMenu
    ##   the import generic shapes type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PreferencesBuilder.ImportGenericMenuTypeName
    @property
    def ImportGenericMenu(self) -> PreferencesBuilder.ImportGenericMenuTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ImportGenericMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportGenericMenuTypeName@endlink) ImportGenericMenu
          the import generic shapes type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ImportGenericMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportGenericMenuTypeName@endlink) ImportGenericMenu

    ##   the import generic shapes type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ImportGenericMenu.setter
    def ImportGenericMenu(self, mImportGenericMenu: PreferencesBuilder.ImportGenericMenuTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ImportGenericMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportGenericMenuTypeName@endlink) ImportGenericMenu
          the import generic shapes type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ImportGenericToggle
    ##   the flag indicating whether to import generic shapes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ImportGenericToggle(self) -> bool:
        """
        Getter for property: (bool) ImportGenericToggle
          the flag indicating whether to import generic shapes.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ImportGenericToggle

    ##   the flag indicating whether to import generic shapes.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ImportGenericToggle.setter
    def ImportGenericToggle(self, mImportGenericToggle: bool):
        """
        Setter for property: (bool) ImportGenericToggle
          the flag indicating whether to import generic shapes.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ImportMaskMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportMaskMenuTypeName@endlink) ImportMaskMenu
    ##   the import mask type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PreferencesBuilder.ImportMaskMenuTypeName
    @property
    def ImportMaskMenu(self) -> PreferencesBuilder.ImportMaskMenuTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ImportMaskMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportMaskMenuTypeName@endlink) ImportMaskMenu
          the import mask type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ImportMaskMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportMaskMenuTypeName@endlink) ImportMaskMenu

    ##   the import mask type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ImportMaskMenu.setter
    def ImportMaskMenu(self, mImportMaskMenu: PreferencesBuilder.ImportMaskMenuTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ImportMaskMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportMaskMenuTypeName@endlink) ImportMaskMenu
          the import mask type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ImportMaskToggle
    ##   the flag indicating whether to import masks.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ImportMaskToggle(self) -> bool:
        """
        Getter for property: (bool) ImportMaskToggle
          the flag indicating whether to import masks.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ImportMaskToggle

    ##   the flag indicating whether to import masks.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ImportMaskToggle.setter
    def ImportMaskToggle(self, mImportMaskToggle: bool):
        """
        Setter for property: (bool) ImportMaskToggle
          the flag indicating whether to import masks.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ImportMasksMethodType NXOpen.PcbExchange.PreferencesBuilder.ImportMasksMethodType@endlink) ImportMasksMethod
    ##   the flag indicating import masks method.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return PreferencesBuilder.ImportMasksMethodType
    @property
    def ImportMasksMethod(self) -> PreferencesBuilder.ImportMasksMethodType:
        """
        Getter for property: (@link PreferencesBuilder.ImportMasksMethodType NXOpen.PcbExchange.PreferencesBuilder.ImportMasksMethodType@endlink) ImportMasksMethod
          the flag indicating import masks method.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ImportMasksMethodType NXOpen.PcbExchange.PreferencesBuilder.ImportMasksMethodType@endlink) ImportMasksMethod

    ##   the flag indicating import masks method.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ImportMasksMethod.setter
    def ImportMasksMethod(self, mImportMaskMethod: PreferencesBuilder.ImportMasksMethodType):
        """
        Setter for property: (@link PreferencesBuilder.ImportMasksMethodType NXOpen.PcbExchange.PreferencesBuilder.ImportMasksMethodType@endlink) ImportMasksMethod
          the flag indicating import masks method.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ImportPadMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportPadMenuTypeName@endlink) ImportPadMenu
    ##   the import pad type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PreferencesBuilder.ImportPadMenuTypeName
    @property
    def ImportPadMenu(self) -> PreferencesBuilder.ImportPadMenuTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ImportPadMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportPadMenuTypeName@endlink) ImportPadMenu
          the import pad type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ImportPadMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportPadMenuTypeName@endlink) ImportPadMenu

    ##   the import pad type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ImportPadMenu.setter
    def ImportPadMenu(self, mImportPadMenu: PreferencesBuilder.ImportPadMenuTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ImportPadMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportPadMenuTypeName@endlink) ImportPadMenu
          the import pad type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ImportPadToggle
    ##   the flag indicating whether to import pads.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ImportPadToggle(self) -> bool:
        """
        Getter for property: (bool) ImportPadToggle
          the flag indicating whether to import pads.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ImportPadToggle

    ##   the flag indicating whether to import pads.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ImportPadToggle.setter
    def ImportPadToggle(self, mImportPadToggle: bool):
        """
        Setter for property: (bool) ImportPadToggle
          the flag indicating whether to import pads.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ImportMaskMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportMaskMenuTypeName@endlink) ImportPasteMaskMenu
    ##   the import pastemask type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return PreferencesBuilder.ImportMaskMenuTypeName
    @property
    def ImportPasteMaskMenu(self) -> PreferencesBuilder.ImportMaskMenuTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ImportMaskMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportMaskMenuTypeName@endlink) ImportPasteMaskMenu
          the import pastemask type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ImportMaskMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportMaskMenuTypeName@endlink) ImportPasteMaskMenu

    ##   the import pastemask type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ImportPasteMaskMenu.setter
    def ImportPasteMaskMenu(self, mImportPasteMaskMenu: PreferencesBuilder.ImportMaskMenuTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ImportMaskMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportMaskMenuTypeName@endlink) ImportPasteMaskMenu
          the import pastemask type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ImportPasteMaskToggle
    ##   the flag indicating whether to import pastemasks.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ImportPasteMaskToggle(self) -> bool:
        """
        Getter for property: (bool) ImportPasteMaskToggle
          the flag indicating whether to import pastemasks.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ImportPasteMaskToggle

    ##   the flag indicating whether to import pastemasks.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ImportPasteMaskToggle.setter
    def ImportPasteMaskToggle(self, mImportPasteMaskToggle: bool):
        """
        Setter for property: (bool) ImportPasteMaskToggle
          the flag indicating whether to import pastemasks.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ImportTraceMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportTraceMenuTypeName@endlink) ImportTraceMenu
    ##   the import trace type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PreferencesBuilder.ImportTraceMenuTypeName
    @property
    def ImportTraceMenu(self) -> PreferencesBuilder.ImportTraceMenuTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ImportTraceMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportTraceMenuTypeName@endlink) ImportTraceMenu
          the import trace type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ImportTraceMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportTraceMenuTypeName@endlink) ImportTraceMenu

    ##   the import trace type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ImportTraceMenu.setter
    def ImportTraceMenu(self, mImportTraceMenu: PreferencesBuilder.ImportTraceMenuTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ImportTraceMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportTraceMenuTypeName@endlink) ImportTraceMenu
          the import trace type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ImportTraceToggle
    ##   the flag indicating whether to import traces.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ImportTraceToggle(self) -> bool:
        """
        Getter for property: (bool) ImportTraceToggle
          the flag indicating whether to import traces.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ImportTraceToggle

    ##   the flag indicating whether to import traces.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ImportTraceToggle.setter
    def ImportTraceToggle(self, mImportTraceToggle: bool):
        """
        Setter for property: (bool) ImportTraceToggle
          the flag indicating whether to import traces.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ImportWireBondToggle
    ##   the flag indicating whether to import wire bonds.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ImportWireBondToggle(self) -> bool:
        """
        Getter for property: (bool) ImportWireBondToggle
          the flag indicating whether to import wire bonds.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ImportWireBondToggle

    ##   the flag indicating whether to import wire bonds.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ImportWireBondToggle.setter
    def ImportWireBondToggle(self, mImportWireBondToggle: bool):
        """
        Setter for property: (bool) ImportWireBondToggle
          the flag indicating whether to import wire bonds.  
             
         
        """
        pass
    
    ## Getter for property: (bool) InternalLayers
    ##   the flag indicating whether to import internal layers.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def InternalLayers(self) -> bool:
        """
        Getter for property: (bool) InternalLayers
          the flag indicating whether to import internal layers.  
             
         
        """
        pass
    
    ## Setter for property: (bool) InternalLayers

    ##   the flag indicating whether to import internal layers.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @InternalLayers.setter
    def InternalLayers(self, mInternalLayers: bool):
        """
        Setter for property: (bool) InternalLayers
          the flag indicating whether to import internal layers.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) KeepInColor
    ##   the keepin area color.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def KeepInColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) KeepInColor
          the keepin area color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) KeepInColor

    ##   the keepin area color.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @KeepInColor.setter
    def KeepInColor(self, mKeepInColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) KeepInColor
          the keepin area color.  
             
         
        """
        pass
    
    ## Getter for property: (int) KeepInLayer
    ##   the keepin area layer.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def KeepInLayer(self) -> int:
        """
        Getter for property: (int) KeepInLayer
          the keepin area layer.  
             
         
        """
        pass
    
    ## Setter for property: (int) KeepInLayer

    ##   the keepin area layer.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @KeepInLayer.setter
    def KeepInLayer(self, mKeepInLayer: int):
        """
        Setter for property: (int) KeepInLayer
          the keepin area layer.  
             
         
        """
        pass
    
    ## Getter for property: (int) KeepInTranslucency
    ##   the keepin area translucency.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def KeepInTranslucency(self) -> int:
        """
        Getter for property: (int) KeepInTranslucency
          the keepin area translucency.  
             
         
        """
        pass
    
    ## Setter for property: (int) KeepInTranslucency

    ##   the keepin area translucency.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @KeepInTranslucency.setter
    def KeepInTranslucency(self, mKeepInTranslucency: int):
        """
        Setter for property: (int) KeepInTranslucency
          the keepin area translucency.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) KeepOutColor
    ##   the keepout area color.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def KeepOutColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) KeepOutColor
          the keepout area color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) KeepOutColor

    ##   the keepout area color.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @KeepOutColor.setter
    def KeepOutColor(self, mKeepOutColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) KeepOutColor
          the keepout area color.  
             
         
        """
        pass
    
    ## Getter for property: (int) KeepOutLayer
    ##   the keepout area layer.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def KeepOutLayer(self) -> int:
        """
        Getter for property: (int) KeepOutLayer
          the keepout area layer.  
             
         
        """
        pass
    
    ## Setter for property: (int) KeepOutLayer

    ##   the keepout area layer.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @KeepOutLayer.setter
    def KeepOutLayer(self, mKeepOutLayer: int):
        """
        Setter for property: (int) KeepOutLayer
          the keepout area layer.  
             
         
        """
        pass
    
    ## Getter for property: (int) KeepOutTranslucency
    ##   the keepout area translucency.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def KeepOutTranslucency(self) -> int:
        """
        Getter for property: (int) KeepOutTranslucency
          the keepout area translucency.  
             
         
        """
        pass
    
    ## Setter for property: (int) KeepOutTranslucency

    ##   the keepout area translucency.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @KeepOutTranslucency.setter
    def KeepOutTranslucency(self, mKeepOutTranslucency: int):
        """
        Setter for property: (int) KeepOutTranslucency
          the keepout area translucency.  
             
         
        """
        pass
    
    ## Getter for property: (bool) MailNotify
    ##   the flag indicating whether to send email notifications.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def MailNotify(self) -> bool:
        """
        Getter for property: (bool) MailNotify
          the flag indicating whether to send email notifications.  
             
         
        """
        pass
    
    ## Setter for property: (bool) MailNotify

    ##   the flag indicating whether to send email notifications.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MailNotify.setter
    def MailNotify(self, mMailNotify: bool):
        """
        Setter for property: (bool) MailNotify
          the flag indicating whether to send email notifications.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.MailProtocolTypeName NXOpen.PcbExchange.PreferencesBuilder.MailProtocolTypeName@endlink) MailProtocol
    ##   the email protocol.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PreferencesBuilder.MailProtocolTypeName
    @property
    def MailProtocol(self) -> PreferencesBuilder.MailProtocolTypeName:
        """
        Getter for property: (@link PreferencesBuilder.MailProtocolTypeName NXOpen.PcbExchange.PreferencesBuilder.MailProtocolTypeName@endlink) MailProtocol
          the email protocol.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.MailProtocolTypeName NXOpen.PcbExchange.PreferencesBuilder.MailProtocolTypeName@endlink) MailProtocol

    ##   the email protocol.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MailProtocol.setter
    def MailProtocol(self, mMailProtocol: PreferencesBuilder.MailProtocolTypeName):
        """
        Setter for property: (@link PreferencesBuilder.MailProtocolTypeName NXOpen.PcbExchange.PreferencesBuilder.MailProtocolTypeName@endlink) MailProtocol
          the email protocol.  
             
         
        """
        pass
    
    ## Getter for property: (int) MaskMaxNumber
    ##   the mask max number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def MaskMaxNumber(self) -> int:
        """
        Getter for property: (int) MaskMaxNumber
          the mask max number.  
             
         
        """
        pass
    
    ## Setter for property: (int) MaskMaxNumber

    ##   the mask max number.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MaskMaxNumber.setter
    def MaskMaxNumber(self, mMaskMaxNumber: int):
        """
        Setter for property: (int) MaskMaxNumber
          the mask max number.  
             
         
        """
        pass
    
    ## Getter for property: (str) MaskNamePrefix
    ##   the mask name prefix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def MaskNamePrefix(self) -> str:
        """
        Getter for property: (str) MaskNamePrefix
          the mask name prefix.  
             
         
        """
        pass
    
    ## Setter for property: (str) MaskNamePrefix

    ##   the mask name prefix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MaskNamePrefix.setter
    def MaskNamePrefix(self, mMaskNamePrefix: str):
        """
        Setter for property: (str) MaskNamePrefix
          the mask name prefix.  
             
         
        """
        pass
    
    ## Getter for property: (str) MaskNameSuffix
    ##   the mask name suffix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def MaskNameSuffix(self) -> str:
        """
        Getter for property: (str) MaskNameSuffix
          the mask name suffix.  
             
         
        """
        pass
    
    ## Setter for property: (str) MaskNameSuffix

    ##   the mask name suffix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MaskNameSuffix.setter
    def MaskNameSuffix(self, mMaskNameSuffix: str):
        """
        Setter for property: (str) MaskNameSuffix
          the mask name suffix.  
             
         
        """
        pass
    
    ## Getter for property: (bool) MergeTracesAndPads
    ##   the flag indicating whether to merge traces and pads.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link NXOpen::PcbExchange::PreferencesBuilder::MergeTracesAndPadsWithEnum NXOpen::PcbExchange::PreferencesBuilder::MergeTracesAndPadsWithEnum@endlink  instead.  <br> 

    ## @return bool
    @property
    def MergeTracesAndPads(self) -> bool:
        """
        Getter for property: (bool) MergeTracesAndPads
          the flag indicating whether to merge traces and pads.  
             
         
        """
        pass
    
    ## Setter for property: (bool) MergeTracesAndPads

    ##   the flag indicating whether to merge traces and pads.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link NXOpen::PcbExchange::PreferencesBuilder::SetMergeTracesAndPadsWithEnum NXOpen::PcbExchange::PreferencesBuilder::SetMergeTracesAndPadsWithEnum@endlink  instead.  <br> 

    @MergeTracesAndPads.setter
    def MergeTracesAndPads(self, mMergeTracesAndPads: bool):
        """
        Setter for property: (bool) MergeTracesAndPads
          the flag indicating whether to merge traces and pads.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.MergeTracesAndPadsType NXOpen.PcbExchange.PreferencesBuilder.MergeTracesAndPadsType@endlink) MergeTracesAndPadsWithEnum
    ##   the flag indicating whether to merge traces and/or pads.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return PreferencesBuilder.MergeTracesAndPadsType
    @property
    def MergeTracesAndPadsWithEnum(self) -> PreferencesBuilder.MergeTracesAndPadsType:
        """
        Getter for property: (@link PreferencesBuilder.MergeTracesAndPadsType NXOpen.PcbExchange.PreferencesBuilder.MergeTracesAndPadsType@endlink) MergeTracesAndPadsWithEnum
          the flag indicating whether to merge traces and/or pads.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.MergeTracesAndPadsType NXOpen.PcbExchange.PreferencesBuilder.MergeTracesAndPadsType@endlink) MergeTracesAndPadsWithEnum

    ##   the flag indicating whether to merge traces and/or pads.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @MergeTracesAndPadsWithEnum.setter
    def MergeTracesAndPadsWithEnum(self, mMergeTracesAndPads: PreferencesBuilder.MergeTracesAndPadsType):
        """
        Setter for property: (@link PreferencesBuilder.MergeTracesAndPadsType NXOpen.PcbExchange.PreferencesBuilder.MergeTracesAndPadsType@endlink) MergeTracesAndPadsWithEnum
          the flag indicating whether to merge traces and/or pads.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ModelForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ModelForStructuralAnalysisTypeName@endlink) ModelForStructuralAnalysis
    ##   the board mesh type for structural analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PreferencesBuilder.ModelForStructuralAnalysisTypeName
    @property
    def ModelForStructuralAnalysis(self) -> PreferencesBuilder.ModelForStructuralAnalysisTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ModelForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ModelForStructuralAnalysisTypeName@endlink) ModelForStructuralAnalysis
          the board mesh type for structural analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ModelForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ModelForStructuralAnalysisTypeName@endlink) ModelForStructuralAnalysis

    ##   the board mesh type for structural analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ModelForStructuralAnalysis.setter
    def ModelForStructuralAnalysis(self, mModelForStructuralAnalysis: PreferencesBuilder.ModelForStructuralAnalysisTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ModelForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ModelForStructuralAnalysisTypeName@endlink) ModelForStructuralAnalysis
          the board mesh type for structural analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ModelForThermalAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ModelForThermalAnalysisTypeName@endlink) ModelForThermalAnalysis
    ##   the board mesh type for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PreferencesBuilder.ModelForThermalAnalysisTypeName
    @property
    def ModelForThermalAnalysis(self) -> PreferencesBuilder.ModelForThermalAnalysisTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ModelForThermalAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ModelForThermalAnalysisTypeName@endlink) ModelForThermalAnalysis
          the board mesh type for thermal analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ModelForThermalAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ModelForThermalAnalysisTypeName@endlink) ModelForThermalAnalysis

    ##   the board mesh type for thermal analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ModelForThermalAnalysis.setter
    def ModelForThermalAnalysis(self, mModelForThermalAnalysis: PreferencesBuilder.ModelForThermalAnalysisTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ModelForThermalAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ModelForThermalAnalysisTypeName@endlink) ModelForThermalAnalysis
          the board mesh type for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (bool) MonitorEDMDToggle
    ##   the flag indicating whether to monitor the EDMD directory.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def MonitorEDMDToggle(self) -> bool:
        """
        Getter for property: (bool) MonitorEDMDToggle
          the flag indicating whether to monitor the EDMD directory.  
             
         
        """
        pass
    
    ## Setter for property: (bool) MonitorEDMDToggle

    ##   the flag indicating whether to monitor the EDMD directory.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MonitorEDMDToggle.setter
    def MonitorEDMDToggle(self, mMonitorEDMDToggle: bool):
        """
        Setter for property: (bool) MonitorEDMDToggle
          the flag indicating whether to monitor the EDMD directory.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Negative
    ##   the flag indicating whether to import the negative copper shapes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link NXOpen::PcbExchange::PreferencesBuilder::ImportMasksMethod NXOpen::PcbExchange::PreferencesBuilder::ImportMasksMethod@endlink  instead.  <br> 

    ## @return bool
    @property
    def Negative(self) -> bool:
        """
        Getter for property: (bool) Negative
          the flag indicating whether to import the negative copper shapes.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Negative

    ##   the flag indicating whether to import the negative copper shapes.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link NXOpen::PcbExchange::PreferencesBuilder::ImportMasksMethod NXOpen::PcbExchange::PreferencesBuilder::ImportMasksMethod@endlink  instead.  <br> 

    @Negative.setter
    def Negative(self, mNegative: bool):
        """
        Setter for property: (bool) Negative
          the flag indicating whether to import the negative copper shapes.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OtherColor
    ##   the other area color.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def OtherColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OtherColor
          the other area color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OtherColor

    ##   the other area color.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OtherColor.setter
    def OtherColor(self, mOtherColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OtherColor
          the other area color.  
             
         
        """
        pass
    
    ## Getter for property: (int) OtherLayer
    ##   the other area layer.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def OtherLayer(self) -> int:
        """
        Getter for property: (int) OtherLayer
          the other area layer.  
             
         
        """
        pass
    
    ## Setter for property: (int) OtherLayer

    ##   the other area layer.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OtherLayer.setter
    def OtherLayer(self, mOtherLayer: int):
        """
        Setter for property: (int) OtherLayer
          the other area layer.  
             
         
        """
        pass
    
    ## Getter for property: (int) OtherTranslucency
    ##   the other area translucency.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def OtherTranslucency(self) -> int:
        """
        Getter for property: (int) OtherTranslucency
          the other area translucency.  
             
         
        """
        pass
    
    ## Setter for property: (int) OtherTranslucency

    ##   the other area translucency.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OtherTranslucency.setter
    def OtherTranslucency(self, mOtherTranslucency: int):
        """
        Setter for property: (int) OtherTranslucency
          the other area translucency.  
             
         
        """
        pass
    
    ## Getter for property: (int) PadMaxNumber
    ##   the pad max number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def PadMaxNumber(self) -> int:
        """
        Getter for property: (int) PadMaxNumber
          the pad max number.  
             
         
        """
        pass
    
    ## Setter for property: (int) PadMaxNumber

    ##   the pad max number.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PadMaxNumber.setter
    def PadMaxNumber(self, mPadMaxNumber: int):
        """
        Setter for property: (int) PadMaxNumber
          the pad max number.  
             
         
        """
        pass
    
    ## Getter for property: (str) PadNamePrefix
    ##   the pad name prefix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def PadNamePrefix(self) -> str:
        """
        Getter for property: (str) PadNamePrefix
          the pad name prefix.  
             
         
        """
        pass
    
    ## Setter for property: (str) PadNamePrefix

    ##   the pad name prefix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PadNamePrefix.setter
    def PadNamePrefix(self, mPadNamePrefix: str):
        """
        Setter for property: (str) PadNamePrefix
          the pad name prefix.  
             
         
        """
        pass
    
    ## Getter for property: (str) PadNameSuffix
    ##   the pad name suffix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def PadNameSuffix(self) -> str:
        """
        Getter for property: (str) PadNameSuffix
          the pad name suffix.  
             
         
        """
        pass
    
    ## Setter for property: (str) PadNameSuffix

    ##   the pad name suffix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PadNameSuffix.setter
    def PadNameSuffix(self, mPadNameSuffix: str):
        """
        Setter for property: (str) PadNameSuffix
          the pad name suffix.  
             
         
        """
        pass
    
    ## Getter for property: (int) PasteMaskMaxNumber
    ##   the pastemask max number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def PasteMaskMaxNumber(self) -> int:
        """
        Getter for property: (int) PasteMaskMaxNumber
          the pastemask max number.  
             
         
        """
        pass
    
    ## Setter for property: (int) PasteMaskMaxNumber

    ##   the pastemask max number.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @PasteMaskMaxNumber.setter
    def PasteMaskMaxNumber(self, mPasteMaskMaxNumber: int):
        """
        Setter for property: (int) PasteMaskMaxNumber
          the pastemask max number.  
             
         
        """
        pass
    
    ## Getter for property: (str) PasteMaskNamePrefix
    ##   the pastemask name prefix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def PasteMaskNamePrefix(self) -> str:
        """
        Getter for property: (str) PasteMaskNamePrefix
          the pastemask name prefix.  
             
         
        """
        pass
    
    ## Setter for property: (str) PasteMaskNamePrefix

    ##   the pastemask name prefix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @PasteMaskNamePrefix.setter
    def PasteMaskNamePrefix(self, mPasteMaskNamePrefix: str):
        """
        Setter for property: (str) PasteMaskNamePrefix
          the pastemask name prefix.  
             
         
        """
        pass
    
    ## Getter for property: (str) PasteMaskNameSuffix
    ##   the pastemask name suffix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def PasteMaskNameSuffix(self) -> str:
        """
        Getter for property: (str) PasteMaskNameSuffix
          the pastemask name suffix.  
             
         
        """
        pass
    
    ## Setter for property: (str) PasteMaskNameSuffix

    ##   the pastemask name suffix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @PasteMaskNameSuffix.setter
    def PasteMaskNameSuffix(self, mPasteMaskNameSuffix: str):
        """
        Setter for property: (str) PasteMaskNameSuffix
          the pastemask name suffix.  
             
         
        """
        pass
    
    ## Getter for property: (str) PcaNamePrefix
    ##   the PCA name prefix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def PcaNamePrefix(self) -> str:
        """
        Getter for property: (str) PcaNamePrefix
          the PCA name prefix.  
             
         
        """
        pass
    
    ## Setter for property: (str) PcaNamePrefix

    ##   the PCA name prefix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PcaNamePrefix.setter
    def PcaNamePrefix(self, mPcaNamePrefix: str):
        """
        Setter for property: (str) PcaNamePrefix
          the PCA name prefix.  
             
         
        """
        pass
    
    ## Getter for property: (str) PcaNameSuffix
    ##   the PCA name suffix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def PcaNameSuffix(self) -> str:
        """
        Getter for property: (str) PcaNameSuffix
          the PCA name suffix.  
             
         
        """
        pass
    
    ## Setter for property: (str) PcaNameSuffix

    ##   the PCA name suffix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PcaNameSuffix.setter
    def PcaNameSuffix(self, mPcaNameSuffix: str):
        """
        Setter for property: (str) PcaNameSuffix
          the PCA name suffix.  
             
         
        """
        pass
    
    ## Getter for property: (str) ProjectView
    ##   the project view.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def ProjectView(self) -> str:
        """
        Getter for property: (str) ProjectView
          the project view.  
             
         
        """
        pass
    
    ## Setter for property: (str) ProjectView

    ##   the project view.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ProjectView.setter
    def ProjectView(self, mProjectView: str):
        """
        Setter for property: (str) ProjectView
          the project view.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ProjectViewToggle
    ##   the flag indicating whether to project the view.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ProjectViewToggle(self) -> bool:
        """
        Getter for property: (bool) ProjectViewToggle
          the flag indicating whether to project the view.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ProjectViewToggle

    ##   the flag indicating whether to project the view.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ProjectViewToggle.setter
    def ProjectViewToggle(self, mProjectViewToggle: bool):
        """
        Setter for property: (bool) ProjectViewToggle
          the flag indicating whether to project the view.  
             
         
        """
        pass
    
    ## Getter for property: (str) ReadWriteDir
    ##   the read/write directory.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def ReadWriteDir(self) -> str:
        """
        Getter for property: (str) ReadWriteDir
          the read/write directory.  
             
         
        """
        pass
    
    ## Setter for property: (str) ReadWriteDir

    ##   the read/write directory.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ReadWriteDir.setter
    def ReadWriteDir(self, foldername: str):
        """
        Setter for property: (str) ReadWriteDir
          the read/write directory.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ResistorModelTypeName NXOpen.PcbExchange.PreferencesBuilder.ResistorModelTypeName@endlink) ResistorModel
    ##   the resistor model for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return PreferencesBuilder.ResistorModelTypeName
    @property
    def ResistorModel(self) -> PreferencesBuilder.ResistorModelTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ResistorModelTypeName NXOpen.PcbExchange.PreferencesBuilder.ResistorModelTypeName@endlink) ResistorModel
          the resistor model for thermal analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ResistorModelTypeName NXOpen.PcbExchange.PreferencesBuilder.ResistorModelTypeName@endlink) ResistorModel

    ##   the resistor model for thermal analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ResistorModel.setter
    def ResistorModel(self, mComponentsModel: PreferencesBuilder.ResistorModelTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ResistorModelTypeName NXOpen.PcbExchange.PreferencesBuilder.ResistorModelTypeName@endlink) ResistorModel
          the resistor model for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (int) RevisionRule
    ##   the revision rule.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def RevisionRule(self) -> int:
        """
        Getter for property: (int) RevisionRule
          the revision rule.  
             
         
        """
        pass
    
    ## Setter for property: (int) RevisionRule

    ##   the revision rule.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @RevisionRule.setter
    def RevisionRule(self, revisionRule: int):
        """
        Setter for property: (int) RevisionRule
          the revision rule.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.SettingsSourceTypeName NXOpen.PcbExchange.PreferencesBuilder.SettingsSourceTypeName@endlink) SettingsSource
    ##   the settings source.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PreferencesBuilder.SettingsSourceTypeName
    @property
    def SettingsSource(self) -> PreferencesBuilder.SettingsSourceTypeName:
        """
        Getter for property: (@link PreferencesBuilder.SettingsSourceTypeName NXOpen.PcbExchange.PreferencesBuilder.SettingsSourceTypeName@endlink) SettingsSource
          the settings source.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.SettingsSourceTypeName NXOpen.PcbExchange.PreferencesBuilder.SettingsSourceTypeName@endlink) SettingsSource

    ##   the settings source.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SettingsSource.setter
    def SettingsSource(self, mDefaultSettingsSources: PreferencesBuilder.SettingsSourceTypeName):
        """
        Setter for property: (@link PreferencesBuilder.SettingsSourceTypeName NXOpen.PcbExchange.PreferencesBuilder.SettingsSourceTypeName@endlink) SettingsSource
          the settings source.  
             
         
        """
        pass
    
    ## Getter for property: (str) SpecifiedSettingsFolder
    ##   the ini directory.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def SpecifiedSettingsFolder(self) -> str:
        """
        Getter for property: (str) SpecifiedSettingsFolder
          the ini directory.  
             
         
        """
        pass
    
    ## Setter for property: (str) SpecifiedSettingsFolder

    ##   the ini directory.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SpecifiedSettingsFolder.setter
    def SpecifiedSettingsFolder(self, settingsFolder: str):
        """
        Setter for property: (str) SpecifiedSettingsFolder
          the ini directory.  
             
         
        """
        pass
    
    ## Getter for property: (str) SpecifyNewCompDir
    ##   the directory where new components are created if the option is 'Specify'.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def SpecifyNewCompDir(self) -> str:
        """
        Getter for property: (str) SpecifyNewCompDir
          the directory where new components are created if the option is 'Specify'.  
             
         
        """
        pass
    
    ## Setter for property: (str) SpecifyNewCompDir

    ##   the directory where new components are created if the option is 'Specify'.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SpecifyNewCompDir.setter
    def SpecifyNewCompDir(self, mSpecifyNewCompDir: str):
        """
        Setter for property: (str) SpecifyNewCompDir
          the directory where new components are created if the option is 'Specify'.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.StructuralAlgorithmTypeName NXOpen.PcbExchange.PreferencesBuilder.StructuralAlgorithmTypeName@endlink) StructuralAlgorithm
    ##   the algorithm to calculate board properties for structural analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PreferencesBuilder.StructuralAlgorithmTypeName
    @property
    def StructuralAlgorithm(self) -> PreferencesBuilder.StructuralAlgorithmTypeName:
        """
        Getter for property: (@link PreferencesBuilder.StructuralAlgorithmTypeName NXOpen.PcbExchange.PreferencesBuilder.StructuralAlgorithmTypeName@endlink) StructuralAlgorithm
          the algorithm to calculate board properties for structural analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.StructuralAlgorithmTypeName NXOpen.PcbExchange.PreferencesBuilder.StructuralAlgorithmTypeName@endlink) StructuralAlgorithm

    ##   the algorithm to calculate board properties for structural analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @StructuralAlgorithm.setter
    def StructuralAlgorithm(self, mStructuralAlgorithm: PreferencesBuilder.StructuralAlgorithmTypeName):
        """
        Setter for property: (@link PreferencesBuilder.StructuralAlgorithmTypeName NXOpen.PcbExchange.PreferencesBuilder.StructuralAlgorithmTypeName@endlink) StructuralAlgorithm
          the algorithm to calculate board properties for structural analysis.  
             
         
        """
        pass
    
    ## Getter for property: (int) TempBoardLayer
    ##   the temporary board layer.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def TempBoardLayer(self) -> int:
        """
        Getter for property: (int) TempBoardLayer
          the temporary board layer.  
             
         
        """
        pass
    
    ## Setter for property: (int) TempBoardLayer

    ##   the temporary board layer.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @TempBoardLayer.setter
    def TempBoardLayer(self, tempBoardLayer: int):
        """
        Setter for property: (int) TempBoardLayer
          the temporary board layer.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ThermalAlgorithmTypeName NXOpen.PcbExchange.PreferencesBuilder.ThermalAlgorithmTypeName@endlink) ThermalAlgorithm
    ##   the algorithm to calculate board properties for thermal analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PreferencesBuilder.ThermalAlgorithmTypeName
    @property
    def ThermalAlgorithm(self) -> PreferencesBuilder.ThermalAlgorithmTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ThermalAlgorithmTypeName NXOpen.PcbExchange.PreferencesBuilder.ThermalAlgorithmTypeName@endlink) ThermalAlgorithm
          the algorithm to calculate board properties for thermal analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ThermalAlgorithmTypeName NXOpen.PcbExchange.PreferencesBuilder.ThermalAlgorithmTypeName@endlink) ThermalAlgorithm

    ##   the algorithm to calculate board properties for thermal analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ThermalAlgorithm.setter
    def ThermalAlgorithm(self, mThermalAlgorithm: PreferencesBuilder.ThermalAlgorithmTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ThermalAlgorithmTypeName NXOpen.PcbExchange.PreferencesBuilder.ThermalAlgorithmTypeName@endlink) ThermalAlgorithm
          the algorithm to calculate board properties for thermal analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThicknessForStructuralAnalysis
    ##   the board thickness for structural analysis when the thickness source is "Specify".  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ThicknessForStructuralAnalysis(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThicknessForStructuralAnalysis
          the board thickness for structural analysis when the thickness source is "Specify".  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName@endlink) ThicknessSourceForStructuralAnalysis
    ##   the thickness source for structural analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName
    @property
    def ThicknessSourceForStructuralAnalysis(self) -> PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName:
        """
        Getter for property: (@link PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName@endlink) ThicknessSourceForStructuralAnalysis
          the thickness source for structural analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName@endlink) ThicknessSourceForStructuralAnalysis

    ##   the thickness source for structural analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ThicknessSourceForStructuralAnalysis.setter
    def ThicknessSourceForStructuralAnalysis(self, mThicknessSourceForStructuralAnalysis: PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName):
        """
        Setter for property: (@link PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName@endlink) ThicknessSourceForStructuralAnalysis
          the thickness source for structural analysis.  
             
         
        """
        pass
    
    ## Getter for property: (int) TraceMaxNumber
    ##   the trace max number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def TraceMaxNumber(self) -> int:
        """
        Getter for property: (int) TraceMaxNumber
          the trace max number.  
             
         
        """
        pass
    
    ## Setter for property: (int) TraceMaxNumber

    ##   the trace max number.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @TraceMaxNumber.setter
    def TraceMaxNumber(self, mTraceMaxNumber: int):
        """
        Setter for property: (int) TraceMaxNumber
          the trace max number.  
             
         
        """
        pass
    
    ## Getter for property: (str) TraceNamePrefix
    ##   the trace name prefix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def TraceNamePrefix(self) -> str:
        """
        Getter for property: (str) TraceNamePrefix
          the trace name prefix.  
             
         
        """
        pass
    
    ## Setter for property: (str) TraceNamePrefix

    ##   the trace name prefix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @TraceNamePrefix.setter
    def TraceNamePrefix(self, mTraceNamePrefix: str):
        """
        Setter for property: (str) TraceNamePrefix
          the trace name prefix.  
             
         
        """
        pass
    
    ## Getter for property: (str) TraceNameSuffix
    ##   the trace name suffix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def TraceNameSuffix(self) -> str:
        """
        Getter for property: (str) TraceNameSuffix
          the trace name suffix.  
             
         
        """
        pass
    
    ## Setter for property: (str) TraceNameSuffix

    ##   the trace name suffix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @TraceNameSuffix.setter
    def TraceNameSuffix(self, mtraceNameSuffix: str):
        """
        Setter for property: (str) TraceNameSuffix
          the trace name suffix.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseRevisionRule
    ##   the flag indicating whether or not to use additional revision rule.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def UseRevisionRule(self) -> bool:
        """
        Getter for property: (bool) UseRevisionRule
          the flag indicating whether or not to use additional revision rule.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseRevisionRule

    ##   the flag indicating whether or not to use additional revision rule.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @UseRevisionRule.setter
    def UseRevisionRule(self, useRevisionRule: bool):
        """
        Setter for property: (bool) UseRevisionRule
          the flag indicating whether or not to use additional revision rule.  
             
         
        """
        pass
    
    ##  Gets the area mapping. 
    ##  @return areaMapping (@link AreaMapping NXOpen.PcbExchange.AreaMapping@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAreaMapping(builder: PreferencesBuilder) -> AreaMapping:
        """
         Gets the area mapping. 
         @return areaMapping (@link AreaMapping NXOpen.PcbExchange.AreaMapping@endlink): .
        """
        pass
    
    ##  Gets the ECAD entity filter. 
    ##  @return filter (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEcadEntityFilter(builder: PreferencesBuilder) -> EntityFilter:
        """
         Gets the ECAD entity filter. 
         @return filter (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink): .
        """
        pass
    
    ##  Returns the email recipients. 
    ##  @return mMailRecipients (List[str]): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMailRecipients(builder: PreferencesBuilder) -> List[str]:
        """
         Returns the email recipients. 
         @return mMailRecipients (List[str]): .
        """
        pass
    
    ##  Gets the MCAD entity filter. 
    ##  @return filter (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMcadEntityFilter(builder: PreferencesBuilder) -> EntityFilter:
        """
         Gets the MCAD entity filter. 
         @return filter (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink): .
        """
        pass
    
    ##  Refreshs PCB settings. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def RefreshSettings(builder: PreferencesBuilder) -> None:
        """
         Refreshs PCB settings. 
        """
        pass
    
    ##  Sets the area mapping. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="areaMapping"> (@link AreaMapping NXOpen.PcbExchange.AreaMapping@endlink) </param>
    def SetAreaMapping(builder: PreferencesBuilder, areaMapping: AreaMapping) -> None:
        """
         Sets the area mapping. 
        """
        pass
    
    ##  Sets the ECAD entity filter. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="filter"> (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) </param>
    def SetEcadEntityFilter(builder: PreferencesBuilder, filter: EntityFilter) -> None:
        """
         Sets the ECAD entity filter. 
        """
        pass
    
    ##  Sets the email recipients. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The mail recipient 
    def SetMailRecipients(builder: PreferencesBuilder, mMailRecipients: List[str]) -> None:
        """
         Sets the email recipients. 
        """
        pass
    
    ##  Sets the MCAD entity filter. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="filter"> (@link EntityFilter NXOpen.PcbExchange.EntityFilter@endlink) </param>
    def SetMcadEntityFilter(builder: PreferencesBuilder, filter: EntityFilter) -> None:
        """
         Sets the MCAD entity filter. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::PcbExchange::ReportBuilder NXOpen::PcbExchange::ReportBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateReportBuilder  NXOpen::PcbExchange::Manager::CreateReportBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ReportBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.PcbExchange.ReportBuilder</ja_class>. """


    ##  The report types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Validation</term><description> 
    ## </description> </item><item><term> 
    ## LightweightValidation</term><description> 
    ## </description> </item><item><term> 
    ## Component</term><description> 
    ## </description> </item><item><term> 
    ## ThermalDatabase</term><description> 
    ## </description> </item><item><term> 
    ## PanelValidation</term><description> 
    ## </description> </item></list>
    class TypeEnum(Enum):
        """
        Members Include: <Validation> <LightweightValidation> <Component> <ThermalDatabase> <PanelValidation>
        """
        Validation: int
        LightweightValidation: int
        Component: int
        ThermalDatabase: int
        PanelValidation: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReportBuilder.TypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ReportBuilder.TypeEnum NXOpen.PcbExchange.ReportBuilder.TypeEnum@endlink) ReportType
    ##   the report type.  
    ##      
    ##  
    ## Getter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return ReportBuilder.TypeEnum
    @property
    def ReportType(self) -> ReportBuilder.TypeEnum:
        """
        Getter for property: (@link ReportBuilder.TypeEnum NXOpen.PcbExchange.ReportBuilder.TypeEnum@endlink) ReportType
          the report type.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReportBuilder.TypeEnum NXOpen.PcbExchange.ReportBuilder.TypeEnum@endlink) ReportType

    ##   the report type.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ReportType.setter
    def ReportType(self, type: ReportBuilder.TypeEnum):
        """
        Setter for property: (@link ReportBuilder.TypeEnum NXOpen.PcbExchange.ReportBuilder.TypeEnum@endlink) ReportType
          the report type.  
             
         
        """
        pass
    
import NXOpen
##  Represents a builder to create or edit template.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateTemplateBuilder  NXOpen::PcbExchange::Manager::CreateTemplateBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class TemplateBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit template. """


    ## Getter for property: (str) AreaItemType
    ##   the area item type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def AreaItemType(self) -> str:
        """
        Getter for property: (str) AreaItemType
          the area item type.  
             
         
        """
        pass
    
    ## Setter for property: (str) AreaItemType

    ##   the area item type.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @AreaItemType.setter
    def AreaItemType(self, itemType: str):
        """
        Setter for property: (str) AreaItemType
          the area item type.  
             
         
        """
        pass
    
    ## Getter for property: (int) AreaTemplate
    ##   the area template.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def AreaTemplate(self) -> int:
        """
        Getter for property: (int) AreaTemplate
          the area template.  
             
         
        """
        pass
    
    ## Setter for property: (int) AreaTemplate

    ##   the area template.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AreaTemplate.setter
    def AreaTemplate(self, areaTemplate: int):
        """
        Setter for property: (int) AreaTemplate
          the area template.  
             
         
        """
        pass
    
    ## Getter for property: (str) AssemblyItemType
    ##   the assembly item type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def AssemblyItemType(self) -> str:
        """
        Getter for property: (str) AssemblyItemType
          the assembly item type.  
             
         
        """
        pass
    
    ## Setter for property: (str) AssemblyItemType

    ##   the assembly item type.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @AssemblyItemType.setter
    def AssemblyItemType(self, itemType: str):
        """
        Setter for property: (str) AssemblyItemType
          the assembly item type.  
             
         
        """
        pass
    
    ## Getter for property: (int) AssemblyTemplate
    ##   the assembly template.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def AssemblyTemplate(self) -> int:
        """
        Getter for property: (int) AssemblyTemplate
          the assembly template.  
             
         
        """
        pass
    
    ## Setter for property: (int) AssemblyTemplate

    ##   the assembly template.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AssemblyTemplate.setter
    def AssemblyTemplate(self, assemblyTemplate: int):
        """
        Setter for property: (int) AssemblyTemplate
          the assembly template.  
             
         
        """
        pass
    
    ## Getter for property: (str) BoardItemType
    ##   the board item type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def BoardItemType(self) -> str:
        """
        Getter for property: (str) BoardItemType
          the board item type.  
             
         
        """
        pass
    
    ## Setter for property: (str) BoardItemType

    ##   the board item type.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @BoardItemType.setter
    def BoardItemType(self, itemType: str):
        """
        Setter for property: (str) BoardItemType
          the board item type.  
             
         
        """
        pass
    
    ## Getter for property: (int) BoardTemplate
    ##   the board template.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def BoardTemplate(self) -> int:
        """
        Getter for property: (int) BoardTemplate
          the board template.  
             
         
        """
        pass
    
    ## Setter for property: (int) BoardTemplate

    ##   the board template.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BoardTemplate.setter
    def BoardTemplate(self, boardTemplate: int):
        """
        Setter for property: (int) BoardTemplate
          the board template.  
             
         
        """
        pass
    
    ## Getter for property: (str) ComponentItemType
    ##   the component item type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def ComponentItemType(self) -> str:
        """
        Getter for property: (str) ComponentItemType
          the component item type.  
             
         
        """
        pass
    
    ## Setter for property: (str) ComponentItemType

    ##   the component item type.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ComponentItemType.setter
    def ComponentItemType(self, itemType: str):
        """
        Setter for property: (str) ComponentItemType
          the component item type.  
             
         
        """
        pass
    
    ## Getter for property: (int) ComponentTemplate
    ##   the component template.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def ComponentTemplate(self) -> int:
        """
        Getter for property: (int) ComponentTemplate
          the component template.  
             
         
        """
        pass
    
    ## Setter for property: (int) ComponentTemplate

    ##   the component template.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ComponentTemplate.setter
    def ComponentTemplate(self, componentTemplate: int):
        """
        Setter for property: (int) ComponentTemplate
          the component template.  
             
         
        """
        pass
    
    ## Getter for property: (str) FemItemType
    ##   the fem item type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def FemItemType(self) -> str:
        """
        Getter for property: (str) FemItemType
          the fem item type.  
             
         
        """
        pass
    
    ## Setter for property: (str) FemItemType

    ##   the fem item type.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @FemItemType.setter
    def FemItemType(self, itemType: str):
        """
        Setter for property: (str) FemItemType
          the fem item type.  
             
         
        """
        pass
    
    ## Getter for property: (int) FemTemplate
    ##   the fem template.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def FemTemplate(self) -> int:
        """
        Getter for property: (int) FemTemplate
          the fem template.  
             
         
        """
        pass
    
    ## Setter for property: (int) FemTemplate

    ##   the fem template.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FemTemplate.setter
    def FemTemplate(self, femTemplate: int):
        """
        Setter for property: (int) FemTemplate
          the fem template.  
             
         
        """
        pass
    
    ## Getter for property: (str) SimItemType
    ##   the sim item type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def SimItemType(self) -> str:
        """
        Getter for property: (str) SimItemType
          the sim item type.  
             
         
        """
        pass
    
    ## Setter for property: (str) SimItemType

    ##   the sim item type.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @SimItemType.setter
    def SimItemType(self, itemType: str):
        """
        Setter for property: (str) SimItemType
          the sim item type.  
             
         
        """
        pass
    
    ## Getter for property: (int) SimTemplate
    ##   the sim template.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def SimTemplate(self) -> int:
        """
        Getter for property: (int) SimTemplate
          the sim template.  
             
         
        """
        pass
    
    ## Setter for property: (int) SimTemplate

    ##   the sim template.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SimTemplate.setter
    def SimTemplate(self, simTemplate: int):
        """
        Setter for property: (int) SimTemplate
          the sim template.  
             
         
        """
        pass
    
    ## Getter for property: (str) SubAssemblyItemType
    ##   the subassembly item type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def SubAssemblyItemType(self) -> str:
        """
        Getter for property: (str) SubAssemblyItemType
          the subassembly item type.  
             
         
        """
        pass
    
    ## Setter for property: (str) SubAssemblyItemType

    ##   the subassembly item type.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @SubAssemblyItemType.setter
    def SubAssemblyItemType(self, itemType: str):
        """
        Setter for property: (str) SubAssemblyItemType
          the subassembly item type.  
             
         
        """
        pass
    
    ## Getter for property: (int) SubAssemblyTemplate
    ##   the subassembly template.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def SubAssemblyTemplate(self) -> int:
        """
        Getter for property: (int) SubAssemblyTemplate
          the subassembly template.  
             
         
        """
        pass
    
    ## Setter for property: (int) SubAssemblyTemplate

    ##   the subassembly template.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SubAssemblyTemplate.setter
    def SubAssemblyTemplate(self, subAssemblyTemplate: int):
        """
        Setter for property: (int) SubAssemblyTemplate
          the subassembly template.  
             
         
        """
        pass
    
import NXOpen
##  Represents a variant manager builder.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateVariantManagerBuilder  NXOpen::PcbExchange::Manager::CreateVariantManagerBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class VariantManagerBuilder(NXOpen.Builder): 
    """ Represents a variant manager builder. """


    ##  the ECAD data location options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Local</term><description> 
    ## </description> </item><item><term> 
    ## Dataset</term><description> 
    ## </description> </item><item><term> 
    ## ItemRevision</term><description> 
    ## </description> </item><item><term> 
    ## VariantRelationship</term><description> 
    ## </description> </item></list>
    class EcadLocationEnum(Enum):
        """
        Members Include: <Local> <Dataset> <ItemRevision> <VariantRelationship>
        """
        Local: int
        Dataset: int
        ItemRevision: int
        VariantRelationship: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VariantManagerBuilder.EcadLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the update options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Specify</term><description> 
    ## </description> </item></list>
    class UpdateOptionEnum(Enum):
        """
        Members Include: <All> <NotSet> <Specify>
        """
        All: int
        NotSet: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VariantManagerBuilder.UpdateOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the update target options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## External</term><description> 
    ## </description> </item><item><term> 
    ## Current</term><description> 
    ## </description> </item></list>
    class UpdateTargetEnum(Enum):
        """
        Members Include: <External> <Current>
        """
        External: int
        Current: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VariantManagerBuilder.UpdateTargetEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) BoardFile
    ##   the board file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def BoardFile(self) -> str:
        """
        Getter for property: (str) BoardFile
          the board file.  
             
         
        """
        pass
    
    ## Setter for property: (str) BoardFile

    ##   the board file.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @BoardFile.setter
    def BoardFile(self, boardFile: str):
        """
        Setter for property: (str) BoardFile
          the board file.  
             
         
        """
        pass
    
    ## Getter for property: (@link VariantManagerBuilder.EcadLocationEnum NXOpen.PcbExchange.VariantManagerBuilder.EcadLocationEnum@endlink) EcadLocation
    ##   the ECAD data location.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return VariantManagerBuilder.EcadLocationEnum
    @property
    def EcadLocation(self) -> VariantManagerBuilder.EcadLocationEnum:
        """
        Getter for property: (@link VariantManagerBuilder.EcadLocationEnum NXOpen.PcbExchange.VariantManagerBuilder.EcadLocationEnum@endlink) EcadLocation
          the ECAD data location.  
             
         
        """
        pass
    
    ## Setter for property: (@link VariantManagerBuilder.EcadLocationEnum NXOpen.PcbExchange.VariantManagerBuilder.EcadLocationEnum@endlink) EcadLocation

    ##   the ECAD data location.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @EcadLocation.setter
    def EcadLocation(self, ecadLocation: VariantManagerBuilder.EcadLocationEnum):
        """
        Setter for property: (@link VariantManagerBuilder.EcadLocationEnum NXOpen.PcbExchange.VariantManagerBuilder.EcadLocationEnum@endlink) EcadLocation
          the ECAD data location.  
             
         
        """
        pass
    
    ## Getter for property: (str) ItemRevision
    ##   the item revision.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def ItemRevision(self) -> str:
        """
        Getter for property: (str) ItemRevision
          the item revision.  
             
         
        """
        pass
    
    ## Setter for property: (str) ItemRevision

    ##   the item revision.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ItemRevision.setter
    def ItemRevision(self, itemRevision: str):
        """
        Setter for property: (str) ItemRevision
          the item revision.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowLog
    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowLog

    ##   the flag indicating whether to show the log.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
          the flag indicating whether to show the log.  
             
         
        """
        pass
    
    ## Getter for property: (@link VariantManagerBuilder.UpdateOptionEnum NXOpen.PcbExchange.VariantManagerBuilder.UpdateOptionEnum@endlink) UpdateOption
    ##   the update option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return VariantManagerBuilder.UpdateOptionEnum
    @property
    def UpdateOption(self) -> VariantManagerBuilder.UpdateOptionEnum:
        """
        Getter for property: (@link VariantManagerBuilder.UpdateOptionEnum NXOpen.PcbExchange.VariantManagerBuilder.UpdateOptionEnum@endlink) UpdateOption
          the update option.  
             
         
        """
        pass
    
    ## Setter for property: (@link VariantManagerBuilder.UpdateOptionEnum NXOpen.PcbExchange.VariantManagerBuilder.UpdateOptionEnum@endlink) UpdateOption

    ##   the update option.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @UpdateOption.setter
    def UpdateOption(self, updateOption: VariantManagerBuilder.UpdateOptionEnum):
        """
        Setter for property: (@link VariantManagerBuilder.UpdateOptionEnum NXOpen.PcbExchange.VariantManagerBuilder.UpdateOptionEnum@endlink) UpdateOption
          the update option.  
             
         
        """
        pass
    
    ## Getter for property: (@link VariantManagerBuilder.UpdateTargetEnum NXOpen.PcbExchange.VariantManagerBuilder.UpdateTargetEnum@endlink) UpdateTarget
    ##   the update target.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return VariantManagerBuilder.UpdateTargetEnum
    @property
    def UpdateTarget(self) -> VariantManagerBuilder.UpdateTargetEnum:
        """
        Getter for property: (@link VariantManagerBuilder.UpdateTargetEnum NXOpen.PcbExchange.VariantManagerBuilder.UpdateTargetEnum@endlink) UpdateTarget
          the update target.  
             
         
        """
        pass
    
    ## Setter for property: (@link VariantManagerBuilder.UpdateTargetEnum NXOpen.PcbExchange.VariantManagerBuilder.UpdateTargetEnum@endlink) UpdateTarget

    ##   the update target.  
    ##      
    ##  
    ## Setter License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @UpdateTarget.setter
    def UpdateTarget(self, updateTarget: VariantManagerBuilder.UpdateTargetEnum):
        """
        Setter for property: (@link VariantManagerBuilder.UpdateTargetEnum NXOpen.PcbExchange.VariantManagerBuilder.UpdateTargetEnum@endlink) UpdateTarget
          the update target.  
             
         
        """
        pass
    
    ##  Compares the models. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def Compare(builder: VariantManagerBuilder) -> None:
        """
         Compares the models. 
        """
        pass
    
    ##  Sets the update status for the variant assembly. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    ## 
    ## <param name="variantName"> (str) </param>
    ## <param name="canUpdate"> (bool) </param>
    def SetUpdate(builder: VariantManagerBuilder, variantName: str, canUpdate: bool) -> None:
        """
         Sets the update status for the variant assembly. 
        """
        pass
    
    ##  Shows comparison details. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken")
    @staticmethod
    def ShowComparisonDetails(builder: VariantManagerBuilder) -> None:
        """
         Shows comparison details. 
        """
        pass
    
##  Defines the position of a wire bond. 
##  Any wire bond. 
class WireBondSide(Enum):
    """
    Members Include: <All> <Top> <Bottom>
    """
    All: int
    Top: int
    Bottom: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> WireBondSide:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## @package NXOpen.PcbExchange
## Classes, Enums and Structs under NXOpen.PcbExchange namespace

##  @link AreaAttributesBuilderLayerEnum NXOpen.PcbExchange.AreaAttributesBuilderLayerEnum @endlink is an alias for @link AreaAttributesBuilder.LayerEnum NXOpen.PcbExchange.AreaAttributesBuilder.LayerEnum@endlink
AreaAttributesBuilderLayerEnum = AreaAttributesBuilder.LayerEnum


##  @link AreaAttributesBuilderOwnerEnum NXOpen.PcbExchange.AreaAttributesBuilderOwnerEnum @endlink is an alias for @link AreaAttributesBuilder.OwnerEnum NXOpen.PcbExchange.AreaAttributesBuilder.OwnerEnum@endlink
AreaAttributesBuilderOwnerEnum = AreaAttributesBuilder.OwnerEnum


##  @link AreaAttributesBuilderTypeEnum NXOpen.PcbExchange.AreaAttributesBuilderTypeEnum @endlink is an alias for @link AreaAttributesBuilder.TypeEnum NXOpen.PcbExchange.AreaAttributesBuilder.TypeEnum@endlink
AreaAttributesBuilderTypeEnum = AreaAttributesBuilder.TypeEnum


##  @link AttributeRemoverOption NXOpen.PcbExchange.AttributeRemoverOption @endlink is an alias for @link AttributeRemover.Option NXOpen.PcbExchange.AttributeRemover.Option@endlink
AttributeRemoverOption = AttributeRemover.Option


##  @link BoardAttributesBuilderOwnerEnum NXOpen.PcbExchange.BoardAttributesBuilderOwnerEnum @endlink is an alias for @link BoardAttributesBuilder.OwnerEnum NXOpen.PcbExchange.BoardAttributesBuilder.OwnerEnum@endlink
BoardAttributesBuilderOwnerEnum = BoardAttributesBuilder.OwnerEnum


##  @link BoardPropertiesBuilderBoardStackupOption NXOpen.PcbExchange.BoardPropertiesBuilderBoardStackupOption @endlink is an alias for @link BoardPropertiesBuilder.BoardStackupOption NXOpen.PcbExchange.BoardPropertiesBuilder.BoardStackupOption@endlink
BoardPropertiesBuilderBoardStackupOption = BoardPropertiesBuilder.BoardStackupOption


##  @link BoardPropertiesBuilderMaterialsFromOption NXOpen.PcbExchange.BoardPropertiesBuilderMaterialsFromOption @endlink is an alias for @link BoardPropertiesBuilder.MaterialsFromOption NXOpen.PcbExchange.BoardPropertiesBuilder.MaterialsFromOption@endlink
BoardPropertiesBuilderMaterialsFromOption = BoardPropertiesBuilder.MaterialsFromOption


##  @link BoardPropertiesBuilderStructuralAlgorithmOption NXOpen.PcbExchange.BoardPropertiesBuilderStructuralAlgorithmOption @endlink is an alias for @link BoardPropertiesBuilder.StructuralAlgorithmOption NXOpen.PcbExchange.BoardPropertiesBuilder.StructuralAlgorithmOption@endlink
BoardPropertiesBuilderStructuralAlgorithmOption = BoardPropertiesBuilder.StructuralAlgorithmOption


##  @link BoardPropertiesBuilderThermalAlgorithmOption NXOpen.PcbExchange.BoardPropertiesBuilderThermalAlgorithmOption @endlink is an alias for @link BoardPropertiesBuilder.ThermalAlgorithmOption NXOpen.PcbExchange.BoardPropertiesBuilder.ThermalAlgorithmOption@endlink
BoardPropertiesBuilderThermalAlgorithmOption = BoardPropertiesBuilder.ThermalAlgorithmOption


##  @link CompareAndUpdateBuilderAssemblyUpdateEnum NXOpen.PcbExchange.CompareAndUpdateBuilderAssemblyUpdateEnum @endlink is an alias for @link CompareAndUpdateBuilder.AssemblyUpdateEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.AssemblyUpdateEnum@endlink
CompareAndUpdateBuilderAssemblyUpdateEnum = CompareAndUpdateBuilder.AssemblyUpdateEnum


##  @link CompareAndUpdateBuilderBoardUpdateEnum NXOpen.PcbExchange.CompareAndUpdateBuilderBoardUpdateEnum @endlink is an alias for @link CompareAndUpdateBuilder.BoardUpdateEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.BoardUpdateEnum@endlink
CompareAndUpdateBuilderBoardUpdateEnum = CompareAndUpdateBuilder.BoardUpdateEnum


##  @link CompareAndUpdateBuilderCompareEnum NXOpen.PcbExchange.CompareAndUpdateBuilderCompareEnum @endlink is an alias for @link CompareAndUpdateBuilder.CompareEnum NXOpen.PcbExchange.CompareAndUpdateBuilder.CompareEnum@endlink
CompareAndUpdateBuilderCompareEnum = CompareAndUpdateBuilder.CompareEnum


##  @link ComponentAttributesBuilderPlacementOwnerEnum NXOpen.PcbExchange.ComponentAttributesBuilderPlacementOwnerEnum @endlink is an alias for @link ComponentAttributesBuilder.PlacementOwnerEnum NXOpen.PcbExchange.ComponentAttributesBuilder.PlacementOwnerEnum@endlink
ComponentAttributesBuilderPlacementOwnerEnum = ComponentAttributesBuilder.PlacementOwnerEnum


##  @link ComponentConstraintsBuilderActionEnum NXOpen.PcbExchange.ComponentConstraintsBuilderActionEnum @endlink is an alias for @link ComponentConstraintsBuilder.ActionEnum NXOpen.PcbExchange.ComponentConstraintsBuilder.ActionEnum@endlink
ComponentConstraintsBuilderActionEnum = ComponentConstraintsBuilder.ActionEnum


##  @link DesignRuleBuilderComponentFilter NXOpen.PcbExchange.DesignRuleBuilderComponentFilter @endlink is an alias for @link DesignRuleBuilder.ComponentFilter NXOpen.PcbExchange.DesignRuleBuilder.ComponentFilter@endlink
DesignRuleBuilderComponentFilter = DesignRuleBuilder.ComponentFilter


##  @link EcadExportBuilderEcadLocationEnum NXOpen.PcbExchange.EcadExportBuilderEcadLocationEnum @endlink is an alias for @link EcadExportBuilder.EcadLocationEnum NXOpen.PcbExchange.EcadExportBuilder.EcadLocationEnum@endlink
EcadExportBuilderEcadLocationEnum = EcadExportBuilder.EcadLocationEnum


##  @link EcadExportBuilderExportUnitsEnum NXOpen.PcbExchange.EcadExportBuilderExportUnitsEnum @endlink is an alias for @link EcadExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.EcadExportBuilder.ExportUnitsEnum@endlink
EcadExportBuilderExportUnitsEnum = EcadExportBuilder.ExportUnitsEnum


##  @link EcadExportBuilderFileFormatEnum NXOpen.PcbExchange.EcadExportBuilderFileFormatEnum @endlink is an alias for @link EcadExportBuilder.FileFormatEnum NXOpen.PcbExchange.EcadExportBuilder.FileFormatEnum@endlink
EcadExportBuilderFileFormatEnum = EcadExportBuilder.FileFormatEnum


##  @link EcadImportBuilderEcadLocationEnum NXOpen.PcbExchange.EcadImportBuilderEcadLocationEnum @endlink is an alias for @link EcadImportBuilder.EcadLocationEnum NXOpen.PcbExchange.EcadImportBuilder.EcadLocationEnum@endlink
EcadImportBuilderEcadLocationEnum = EcadImportBuilder.EcadLocationEnum


##  @link EcadImportBuilderImportOptionEnum NXOpen.PcbExchange.EcadImportBuilderImportOptionEnum @endlink is an alias for @link EcadImportBuilder.ImportOptionEnum NXOpen.PcbExchange.EcadImportBuilder.ImportOptionEnum@endlink
EcadImportBuilderImportOptionEnum = EcadImportBuilder.ImportOptionEnum


##  @link EcadPanelImportBuilderOptimizationMethodOptions NXOpen.PcbExchange.EcadPanelImportBuilderOptimizationMethodOptions @endlink is an alias for @link EcadPanelImportBuilder.OptimizationMethodOptions NXOpen.PcbExchange.EcadPanelImportBuilder.OptimizationMethodOptions@endlink
EcadPanelImportBuilderOptimizationMethodOptions = EcadPanelImportBuilder.OptimizationMethodOptions


##  @link EcadPanelImportBuilderPanelLocationEnum NXOpen.PcbExchange.EcadPanelImportBuilderPanelLocationEnum @endlink is an alias for @link EcadPanelImportBuilder.PanelLocationEnum NXOpen.PcbExchange.EcadPanelImportBuilder.PanelLocationEnum@endlink
EcadPanelImportBuilderPanelLocationEnum = EcadPanelImportBuilder.PanelLocationEnum


##  @link EcadPanelImportBuilderThievingOptions NXOpen.PcbExchange.EcadPanelImportBuilderThievingOptions @endlink is an alias for @link EcadPanelImportBuilder.ThievingOptions NXOpen.PcbExchange.EcadPanelImportBuilder.ThievingOptions@endlink
EcadPanelImportBuilderThievingOptions = EcadPanelImportBuilder.ThievingOptions


##  @link EntityFilterBuilderLengthUnitsEnum NXOpen.PcbExchange.EntityFilterBuilderLengthUnitsEnum @endlink is an alias for @link EntityFilterBuilder.LengthUnitsEnum NXOpen.PcbExchange.EntityFilterBuilder.LengthUnitsEnum@endlink
EntityFilterBuilderLengthUnitsEnum = EntityFilterBuilder.LengthUnitsEnum


##  @link ExternalDataImportBuilderJaPcbExternalDataImportBuilderImportoption NXOpen.PcbExchange.ExternalDataImportBuilderJaPcbExternalDataImportBuilderImportoption @endlink is an alias for @link ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption NXOpen.PcbExchange.ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption@endlink
ExternalDataImportBuilderJaPcbExternalDataImportBuilderImportoption = ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption


##  @link HoleAttributesBuilderAssociatedPartEnum NXOpen.PcbExchange.HoleAttributesBuilderAssociatedPartEnum @endlink is an alias for @link HoleAttributesBuilder.AssociatedPartEnum NXOpen.PcbExchange.HoleAttributesBuilder.AssociatedPartEnum@endlink
HoleAttributesBuilderAssociatedPartEnum = HoleAttributesBuilder.AssociatedPartEnum


##  @link HoleAttributesBuilderOwnerEnum NXOpen.PcbExchange.HoleAttributesBuilderOwnerEnum @endlink is an alias for @link HoleAttributesBuilder.OwnerEnum NXOpen.PcbExchange.HoleAttributesBuilder.OwnerEnum@endlink
HoleAttributesBuilderOwnerEnum = HoleAttributesBuilder.OwnerEnum


##  @link HoleAttributesBuilderPlatingStyleEnum NXOpen.PcbExchange.HoleAttributesBuilderPlatingStyleEnum @endlink is an alias for @link HoleAttributesBuilder.PlatingStyleEnum NXOpen.PcbExchange.HoleAttributesBuilder.PlatingStyleEnum@endlink
HoleAttributesBuilderPlatingStyleEnum = HoleAttributesBuilder.PlatingStyleEnum


##  @link HoleAttributesBuilderTypeEnum NXOpen.PcbExchange.HoleAttributesBuilderTypeEnum @endlink is an alias for @link HoleAttributesBuilder.TypeEnum NXOpen.PcbExchange.HoleAttributesBuilder.TypeEnum@endlink
HoleAttributesBuilderTypeEnum = HoleAttributesBuilder.TypeEnum


##  @link IdxCompareBuilderSourceTypeEnum NXOpen.PcbExchange.IdxCompareBuilderSourceTypeEnum @endlink is an alias for @link IdxCompareBuilder.SourceTypeEnum NXOpen.PcbExchange.IdxCompareBuilder.SourceTypeEnum@endlink
IdxCompareBuilderSourceTypeEnum = IdxCompareBuilder.SourceTypeEnum


##  @link IdxExportBuilderExportUnitsEnum NXOpen.PcbExchange.IdxExportBuilderExportUnitsEnum @endlink is an alias for @link IdxExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.IdxExportBuilder.ExportUnitsEnum@endlink
IdxExportBuilderExportUnitsEnum = IdxExportBuilder.ExportUnitsEnum


##  @link IdxExportBuilderFileFormatEnum NXOpen.PcbExchange.IdxExportBuilderFileFormatEnum @endlink is an alias for @link IdxExportBuilder.FileFormatEnum NXOpen.PcbExchange.IdxExportBuilder.FileFormatEnum@endlink
IdxExportBuilderFileFormatEnum = IdxExportBuilder.FileFormatEnum


##  @link IdxExportBuilderIdxLocationEnum NXOpen.PcbExchange.IdxExportBuilderIdxLocationEnum @endlink is an alias for @link IdxExportBuilder.IdxLocationEnum NXOpen.PcbExchange.IdxExportBuilder.IdxLocationEnum@endlink
IdxExportBuilderIdxLocationEnum = IdxExportBuilder.IdxLocationEnum


##  @link IdxImportBuilderDataLocation NXOpen.PcbExchange.IdxImportBuilderDataLocation @endlink is an alias for @link IdxImportBuilder.DataLocation NXOpen.PcbExchange.IdxImportBuilder.DataLocation@endlink
IdxImportBuilderDataLocation = IdxImportBuilder.DataLocation


##  @link IncrementalExportBuilderExportUnitsEnum NXOpen.PcbExchange.IncrementalExportBuilderExportUnitsEnum @endlink is an alias for @link IncrementalExportBuilder.ExportUnitsEnum NXOpen.PcbExchange.IncrementalExportBuilder.ExportUnitsEnum@endlink
IncrementalExportBuilderExportUnitsEnum = IncrementalExportBuilder.ExportUnitsEnum


##  @link IncrementalExportBuilderFormatEnum NXOpen.PcbExchange.IncrementalExportBuilderFormatEnum @endlink is an alias for @link IncrementalExportBuilder.FormatEnum NXOpen.PcbExchange.IncrementalExportBuilder.FormatEnum@endlink
IncrementalExportBuilderFormatEnum = IncrementalExportBuilder.FormatEnum


##  @link IncrementalExportBuilderTargetLocationEnum NXOpen.PcbExchange.IncrementalExportBuilderTargetLocationEnum @endlink is an alias for @link IncrementalExportBuilder.TargetLocationEnum NXOpen.PcbExchange.IncrementalExportBuilder.TargetLocationEnum@endlink
IncrementalExportBuilderTargetLocationEnum = IncrementalExportBuilder.TargetLocationEnum


##  @link PreferencesBuilderBoardThicknessSourceTypeName NXOpen.PcbExchange.PreferencesBuilderBoardThicknessSourceTypeName @endlink is an alias for @link PreferencesBuilder.BoardThicknessSourceTypeName NXOpen.PcbExchange.PreferencesBuilder.BoardThicknessSourceTypeName@endlink
PreferencesBuilderBoardThicknessSourceTypeName = PreferencesBuilder.BoardThicknessSourceTypeName


##  @link PreferencesBuilderComponentLoadOptionsTypeName NXOpen.PcbExchange.PreferencesBuilderComponentLoadOptionsTypeName @endlink is an alias for @link PreferencesBuilder.ComponentLoadOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentLoadOptionsTypeName@endlink
PreferencesBuilderComponentLoadOptionsTypeName = PreferencesBuilder.ComponentLoadOptionsTypeName


##  @link PreferencesBuilderComponentsConnectionToBoardTypeName NXOpen.PcbExchange.PreferencesBuilderComponentsConnectionToBoardTypeName @endlink is an alias for @link PreferencesBuilder.ComponentsConnectionToBoardTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsConnectionToBoardTypeName@endlink
PreferencesBuilderComponentsConnectionToBoardTypeName = PreferencesBuilder.ComponentsConnectionToBoardTypeName


##  @link PreferencesBuilderComponentsElementSizeOptionsTypeName NXOpen.PcbExchange.PreferencesBuilderComponentsElementSizeOptionsTypeName @endlink is an alias for @link PreferencesBuilder.ComponentsElementSizeOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsElementSizeOptionsTypeName@endlink
PreferencesBuilderComponentsElementSizeOptionsTypeName = PreferencesBuilder.ComponentsElementSizeOptionsTypeName


##  @link PreferencesBuilderComponentsElementThicknessOptionsTypeName NXOpen.PcbExchange.PreferencesBuilderComponentsElementThicknessOptionsTypeName @endlink is an alias for @link PreferencesBuilder.ComponentsElementThicknessOptionsTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsElementThicknessOptionsTypeName@endlink
PreferencesBuilderComponentsElementThicknessOptionsTypeName = PreferencesBuilder.ComponentsElementThicknessOptionsTypeName


##  @link PreferencesBuilderComponentsHeightFromTypeName NXOpen.PcbExchange.PreferencesBuilderComponentsHeightFromTypeName @endlink is an alias for @link PreferencesBuilder.ComponentsHeightFromTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsHeightFromTypeName@endlink
PreferencesBuilderComponentsHeightFromTypeName = PreferencesBuilder.ComponentsHeightFromTypeName


##  @link PreferencesBuilderComponentsMaterialFromTypeName NXOpen.PcbExchange.PreferencesBuilderComponentsMaterialFromTypeName @endlink is an alias for @link PreferencesBuilder.ComponentsMaterialFromTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsMaterialFromTypeName@endlink
PreferencesBuilderComponentsMaterialFromTypeName = PreferencesBuilder.ComponentsMaterialFromTypeName


##  @link PreferencesBuilderComponentsModelTypeName NXOpen.PcbExchange.PreferencesBuilderComponentsModelTypeName @endlink is an alias for @link PreferencesBuilder.ComponentsModelTypeName NXOpen.PcbExchange.PreferencesBuilder.ComponentsModelTypeName@endlink
PreferencesBuilderComponentsModelTypeName = PreferencesBuilder.ComponentsModelTypeName


##  @link PreferencesBuilderCreateNewComponentsInTypeName NXOpen.PcbExchange.PreferencesBuilderCreateNewComponentsInTypeName @endlink is an alias for @link PreferencesBuilder.CreateNewComponentsInTypeName NXOpen.PcbExchange.PreferencesBuilder.CreateNewComponentsInTypeName@endlink
PreferencesBuilderCreateNewComponentsInTypeName = PreferencesBuilder.CreateNewComponentsInTypeName


##  @link PreferencesBuilderDefaultPcaNameTypeName NXOpen.PcbExchange.PreferencesBuilderDefaultPcaNameTypeName @endlink is an alias for @link PreferencesBuilder.DefaultPcaNameTypeName NXOpen.PcbExchange.PreferencesBuilder.DefaultPcaNameTypeName@endlink
PreferencesBuilderDefaultPcaNameTypeName = PreferencesBuilder.DefaultPcaNameTypeName


##  @link PreferencesBuilderElementTypeForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilderElementTypeForStructuralAnalysisTypeName @endlink is an alias for @link PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName@endlink
PreferencesBuilderElementTypeForStructuralAnalysisTypeName = PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName


##  @link PreferencesBuilderGroupEntityComponentsByTypeName NXOpen.PcbExchange.PreferencesBuilderGroupEntityComponentsByTypeName @endlink is an alias for @link PreferencesBuilder.GroupEntityComponentsByTypeName NXOpen.PcbExchange.PreferencesBuilder.GroupEntityComponentsByTypeName@endlink
PreferencesBuilderGroupEntityComponentsByTypeName = PreferencesBuilder.GroupEntityComponentsByTypeName


##  @link PreferencesBuilderImportExportFlexBentType NXOpen.PcbExchange.PreferencesBuilderImportExportFlexBentType @endlink is an alias for @link PreferencesBuilder.ImportExportFlexBentType NXOpen.PcbExchange.PreferencesBuilder.ImportExportFlexBentType@endlink
PreferencesBuilderImportExportFlexBentType = PreferencesBuilder.ImportExportFlexBentType


##  @link PreferencesBuilderImportGenericMenuTypeName NXOpen.PcbExchange.PreferencesBuilderImportGenericMenuTypeName @endlink is an alias for @link PreferencesBuilder.ImportGenericMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportGenericMenuTypeName@endlink
PreferencesBuilderImportGenericMenuTypeName = PreferencesBuilder.ImportGenericMenuTypeName


##  @link PreferencesBuilderImportMaskMenuTypeName NXOpen.PcbExchange.PreferencesBuilderImportMaskMenuTypeName @endlink is an alias for @link PreferencesBuilder.ImportMaskMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportMaskMenuTypeName@endlink
PreferencesBuilderImportMaskMenuTypeName = PreferencesBuilder.ImportMaskMenuTypeName


##  @link PreferencesBuilderImportMasksMethodType NXOpen.PcbExchange.PreferencesBuilderImportMasksMethodType @endlink is an alias for @link PreferencesBuilder.ImportMasksMethodType NXOpen.PcbExchange.PreferencesBuilder.ImportMasksMethodType@endlink
PreferencesBuilderImportMasksMethodType = PreferencesBuilder.ImportMasksMethodType


##  @link PreferencesBuilderImportPadMenuTypeName NXOpen.PcbExchange.PreferencesBuilderImportPadMenuTypeName @endlink is an alias for @link PreferencesBuilder.ImportPadMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportPadMenuTypeName@endlink
PreferencesBuilderImportPadMenuTypeName = PreferencesBuilder.ImportPadMenuTypeName


##  @link PreferencesBuilderImportTraceMenuTypeName NXOpen.PcbExchange.PreferencesBuilderImportTraceMenuTypeName @endlink is an alias for @link PreferencesBuilder.ImportTraceMenuTypeName NXOpen.PcbExchange.PreferencesBuilder.ImportTraceMenuTypeName@endlink
PreferencesBuilderImportTraceMenuTypeName = PreferencesBuilder.ImportTraceMenuTypeName


##  @link PreferencesBuilderMailProtocolTypeName NXOpen.PcbExchange.PreferencesBuilderMailProtocolTypeName @endlink is an alias for @link PreferencesBuilder.MailProtocolTypeName NXOpen.PcbExchange.PreferencesBuilder.MailProtocolTypeName@endlink
PreferencesBuilderMailProtocolTypeName = PreferencesBuilder.MailProtocolTypeName


##  @link PreferencesBuilderMergeTracesAndPadsType NXOpen.PcbExchange.PreferencesBuilderMergeTracesAndPadsType @endlink is an alias for @link PreferencesBuilder.MergeTracesAndPadsType NXOpen.PcbExchange.PreferencesBuilder.MergeTracesAndPadsType@endlink
PreferencesBuilderMergeTracesAndPadsType = PreferencesBuilder.MergeTracesAndPadsType


##  @link PreferencesBuilderModelForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilderModelForStructuralAnalysisTypeName @endlink is an alias for @link PreferencesBuilder.ModelForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ModelForStructuralAnalysisTypeName@endlink
PreferencesBuilderModelForStructuralAnalysisTypeName = PreferencesBuilder.ModelForStructuralAnalysisTypeName


##  @link PreferencesBuilderModelForThermalAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilderModelForThermalAnalysisTypeName @endlink is an alias for @link PreferencesBuilder.ModelForThermalAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ModelForThermalAnalysisTypeName@endlink
PreferencesBuilderModelForThermalAnalysisTypeName = PreferencesBuilder.ModelForThermalAnalysisTypeName


##  @link PreferencesBuilderResistorModelTypeName NXOpen.PcbExchange.PreferencesBuilderResistorModelTypeName @endlink is an alias for @link PreferencesBuilder.ResistorModelTypeName NXOpen.PcbExchange.PreferencesBuilder.ResistorModelTypeName@endlink
PreferencesBuilderResistorModelTypeName = PreferencesBuilder.ResistorModelTypeName


##  @link PreferencesBuilderSettingsSourceTypeName NXOpen.PcbExchange.PreferencesBuilderSettingsSourceTypeName @endlink is an alias for @link PreferencesBuilder.SettingsSourceTypeName NXOpen.PcbExchange.PreferencesBuilder.SettingsSourceTypeName@endlink
PreferencesBuilderSettingsSourceTypeName = PreferencesBuilder.SettingsSourceTypeName


##  @link PreferencesBuilderStructuralAlgorithmTypeName NXOpen.PcbExchange.PreferencesBuilderStructuralAlgorithmTypeName @endlink is an alias for @link PreferencesBuilder.StructuralAlgorithmTypeName NXOpen.PcbExchange.PreferencesBuilder.StructuralAlgorithmTypeName@endlink
PreferencesBuilderStructuralAlgorithmTypeName = PreferencesBuilder.StructuralAlgorithmTypeName


##  @link PreferencesBuilderThermalAlgorithmTypeName NXOpen.PcbExchange.PreferencesBuilderThermalAlgorithmTypeName @endlink is an alias for @link PreferencesBuilder.ThermalAlgorithmTypeName NXOpen.PcbExchange.PreferencesBuilder.ThermalAlgorithmTypeName@endlink
PreferencesBuilderThermalAlgorithmTypeName = PreferencesBuilder.ThermalAlgorithmTypeName


##  @link PreferencesBuilderThicknessSourceForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilderThicknessSourceForStructuralAnalysisTypeName @endlink is an alias for @link PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName NXOpen.PcbExchange.PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName@endlink
PreferencesBuilderThicknessSourceForStructuralAnalysisTypeName = PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName


##  @link ReportBuilderTypeEnum NXOpen.PcbExchange.ReportBuilderTypeEnum @endlink is an alias for @link ReportBuilder.TypeEnum NXOpen.PcbExchange.ReportBuilder.TypeEnum@endlink
ReportBuilderTypeEnum = ReportBuilder.TypeEnum


##  @link VariantManagerBuilderEcadLocationEnum NXOpen.PcbExchange.VariantManagerBuilderEcadLocationEnum @endlink is an alias for @link VariantManagerBuilder.EcadLocationEnum NXOpen.PcbExchange.VariantManagerBuilder.EcadLocationEnum@endlink
VariantManagerBuilderEcadLocationEnum = VariantManagerBuilder.EcadLocationEnum


##  @link VariantManagerBuilderUpdateOptionEnum NXOpen.PcbExchange.VariantManagerBuilderUpdateOptionEnum @endlink is an alias for @link VariantManagerBuilder.UpdateOptionEnum NXOpen.PcbExchange.VariantManagerBuilder.UpdateOptionEnum@endlink
VariantManagerBuilderUpdateOptionEnum = VariantManagerBuilder.UpdateOptionEnum


##  @link VariantManagerBuilderUpdateTargetEnum NXOpen.PcbExchange.VariantManagerBuilderUpdateTargetEnum @endlink is an alias for @link VariantManagerBuilder.UpdateTargetEnum NXOpen.PcbExchange.VariantManagerBuilder.UpdateTargetEnum@endlink
VariantManagerBuilderUpdateTargetEnum = VariantManagerBuilder.UpdateTargetEnum


