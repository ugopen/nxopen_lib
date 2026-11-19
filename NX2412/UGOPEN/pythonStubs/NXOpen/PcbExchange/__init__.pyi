from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AdvancedConductivityBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.PcbExchange.AdvancedConductivityBuilder """
    def GetDiameters(self) -> List[float]:
        """
         Method to get diameters 
         Returns diameters (List[float]): .
        """
        pass
    def GetEndLayers(self) -> List[int]:
        """
         Method to get endLayers 
         Returns endLayers (List[int]): .
        """
        pass
    def GetFillMaterials(self) -> List[int]:
        """
         Method to get fillMaterials 
         Returns fillMaterials (List[int]): .
        """
        pass
    def GetFilled(self) -> List[bool]:
        """
         Method to get bFilleds 
         Returns bFilleds (List[bool]): .
        """
        pass
    def GetHolesCounts(self) -> List[int]:
        """
         Method to get holes counts 
         Returns holesCounts (List[int]): .
        """
        pass
    def GetNetsList(self) -> List[str]:
        """
         Method to get netsList 
         Returns nets (List[str]): .
        """
        pass
    def GetNetsToFilterString(self) -> str:
        """
         Method to get netsToFilterString 
         Returns nets (str): .
        """
        pass
    def GetPadstacks(self) -> List[str]:
        """
         Method to get padstacks 
         Returns padstacks (List[str]): .
        """
        pass
    def GetPlatingMaterials(self) -> List[int]:
        """
         Method to get platingMaterials 
         Returns platingMaterials (List[int]): .
        """
        pass
    def GetPlatingThicknesses(self) -> List[float]:
        """
         Method to get platingThicknesses 
         Returns platingThicknesses (List[float]): .
        """
        pass
    def GetStartLayers(self) -> List[int]:
        """
         Method to get startLayers 
         Returns startLayers (List[int]): .
        """
        pass
    def GetT(self) -> List[int]:
        """
         Method to get tags 
         Returns t (List[int]): .
        """
        pass
    def GetTextualFilter(self) -> bool:
        """
         Method to get textualFilter 
         Returns filter (bool): .
        """
        pass
    def GetTypes(self) -> List[int]:
        """
         Method to get types 
         Returns types (List[int]): .
        """
        pass
    def SetDiameters(self, diameters: List[float]) -> None:
        """
         Method to set diameters 
        """
        pass
    def SetEndLayers(self, endLayers: List[int]) -> None:
        """
         Method to set endLayers 
        """
        pass
    def SetFillMaterials(self, fillMaterials: List[int]) -> None:
        """
         Method to set fillMaterials 
        """
        pass
    def SetFilled(self, bFilleds: List[int]) -> None:
        """
         Method to set fillMaterials 
        """
        pass
    def SetHolesCounts(self, holesCounts: List[int]) -> None:
        """
         Method to set holes counts 
        """
        pass
    def SetNetsList(self, nets: List[str]) -> None:
        """
         Method to set netsList 
        """
        pass
    def SetNetsToFilterString(self, nets: str) -> None:
        """
         Method to set netsToFilterString 
        """
        pass
    def SetPadstacks(self, nets: List[str]) -> None:
        """
         Method to set padstacks 
        """
        pass
    def SetPlatingMaterials(self, platingMaterials: List[int]) -> None:
        """
         Method to set platingMaterials 
        """
        pass
    def SetPlatingThicknesses(self, platingThicknesses: List[float]) -> None:
        """
         Method to set platingThicknesses 
        """
        pass
    def SetStartLayers(self, startLayers: List[int]) -> None:
        """
         Method to set startLayers 
        """
        pass
    def SetT(self, t: List[int]) -> None:
        """
         Method to set tags 
        """
        pass
    def SetTextualFilter(self, filter: bool) -> None:
        """
         Method to set textualFilter 
        """
        pass
    def SetTypes(self, types: List[int]) -> None:
        """
         Method to set types 
        """
        pass
import NXOpen
class AlternateComponentManager(NXOpen.Object): 
    """ Represents a NXOpen.PcbExchange.AlternateComponentManager. """
    def Replace(component: NXOpen.NXObject, datasetName: str) -> None:
        """
         Replaces the component with alternate one. 
        """
        pass
import NXOpen
class AreaAttributesBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit area attributes. """
    class LayerEnum(Enum):
        """
        Members Include: 
         |Current| 
         |Both| 
         |Inner| 
         |All| 

        """
        Current: int
        Both: int
        Inner: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> AreaAttributesBuilder.LayerEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OwnerEnum(Enum):
        """
        Members Include: 
         |Unowned| 
         |Mcad| 
         |Ecad| 

        """
        Unowned: int
        Mcad: int
        Ecad: int
        @staticmethod
        def ValueOf(value: int) -> AreaAttributesBuilder.OwnerEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeEnum(Enum):
        """
        Members Include: 
         |Keepout| 
         |Keepin| 
         |Other| 
         |Copper| 

        """
        Keepout: int
        Keepin: int
        Other: int
        Copper: int
        @staticmethod
        def ValueOf(value: int) -> AreaAttributesBuilder.TypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AreaType(self) -> AreaAttributesBuilder.TypeEnum:
        """
        Getter for property: ( AreaAttributesBuilder.TypeEnum NXOpen.P) AreaType
         Returns the area type.  
             
         
        """
        pass
    @AreaType.setter
    def AreaType(self, type: AreaAttributesBuilder.TypeEnum):
        """
        Setter for property: ( AreaAttributesBuilder.TypeEnum NXOpen.P) AreaType
         Returns the area type.  
             
         
        """
        pass
    @property
    def Color(self) -> int:
        """
        Getter for property: (int) Color
         Returns the area color.  
             
         
        """
        pass
    @Color.setter
    def Color(self, color: int):
        """
        Setter for property: (int) Color
         Returns the area color.  
             
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the area height.  
             
         
        """
        pass
    @property
    def InvertedVolume(self) -> bool:
        """
        Getter for property: (bool) InvertedVolume
         Returns the flag indicating whether an area has an inverted volume.  
             
         
        """
        pass
    @InvertedVolume.setter
    def InvertedVolume(self, invertedVolume: bool):
        """
        Setter for property: (bool) InvertedVolume
         Returns the flag indicating whether an area has an inverted volume.  
             
         
        """
        pass
    @property
    def Layer(self) -> AreaAttributesBuilder.LayerEnum:
        """
        Getter for property: ( AreaAttributesBuilder.LayerEnum NXOpen.P) Layer
         Returns the area layer.  
             
         
        """
        pass
    @Layer.setter
    def Layer(self, type: AreaAttributesBuilder.LayerEnum):
        """
        Setter for property: ( AreaAttributesBuilder.LayerEnum NXOpen.P) Layer
         Returns the area layer.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the area name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the area name.  
             
         
        """
        pass
    @property
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Objects
         Returns the selected objects.  
             
         
        """
        pass
    @property
    def Owner(self) -> AreaAttributesBuilder.OwnerEnum:
        """
        Getter for property: ( AreaAttributesBuilder.OwnerEnum NXOpen.P) Owner
         Returns the area owner.  
             
         
        """
        pass
    @Owner.setter
    def Owner(self, type: AreaAttributesBuilder.OwnerEnum):
        """
        Setter for property: ( AreaAttributesBuilder.OwnerEnum NXOpen.P) Owner
         Returns the area owner.  
             
         
        """
        pass
    @property
    def Subtype(self) -> str:
        """
        Getter for property: (str) Subtype
         Returns the area subtype.  
             
         
        """
        pass
    @Subtype.setter
    def Subtype(self, subtype: str):
        """
        Setter for property: (str) Subtype
         Returns the area subtype.  
             
         
        """
        pass
import NXOpen
class AreaMappingBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit area mapping. """
    def PrintMapping(self) -> None:
        """
         Prints area mapping areas. 
        """
        pass
    def SetCopperAreas(self, copperAreaList: List[str]) -> None:
        """
         Sets copper areas. 
        """
        pass
    def SetKeepinAreas(self, keepinAreaList: List[str]) -> None:
        """
         Sets keepin areas. 
        """
        pass
    def SetKeepoutAreas(self, keepoutAreaList: List[str]) -> None:
        """
         Sets keepout areas. 
        """
        pass
    def SetOtherAreas(self, otherAreaList: List[str]) -> None:
        """
         Sets other areas. 
        """
        pass
import NXOpen
class AreaMapping(NXOpen.NXObject): 
    """ Represents a Area Mapping for Pcb Exchange. """
    pass
import NXOpen
class AttributeRemover(NXOpen.Object): 
    """ Represents  a NXOpen.PcbExchange.AttributeRemover. """
    class Option(Enum):
        """
        Members Include: 
         |Board|  Remove board attributes 
         |Components|  Remove components attributes 
         |Areas|  Remove areas attributes 
         |Holes|  Remove drilled holes attributes 
         |Traces|  Remove traces attributes 
         |Pads|  Remove pads attributes 
         |All|  Remove all pcbx attributes 

        """
        Board: int
        Components: int
        Areas: int
        Holes: int
        Traces: int
        Pads: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> AttributeRemover.Option:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def RemoveAttributes(action: AttributeRemover.Option, objTags: List[NXOpen.TaggedObject]) -> None:
        """
         Removes the attributes. 
        """
        pass
import NXOpen
import NXOpen.Features
class BoardAttributesBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit board attributes. """
    class OwnerEnum(Enum):
        """
        Members Include: 
         |Unowned| 
         |Mcad| 
         |Ecad| 

        """
        Unowned: int
        Mcad: int
        Ecad: int
        @staticmethod
        def ValueOf(value: int) -> BoardAttributesBuilder.OwnerEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoardFeature(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) BoardFeature
         Returns the board feature   
            
         
        """
        pass
    @property
    def CsysSelection(self) -> NXOpen.Features.SelectDatumCsys:
        """
        Getter for property: ( NXOpen.Features.SelectDatumCsys) CsysSelection
         Returns the coordinate system for selection.  
             
         
        """
        pass
    @property
    def Owner(self) -> BoardAttributesBuilder.OwnerEnum:
        """
        Getter for property: ( BoardAttributesBuilder.OwnerEnum NXOpen.P) Owner
         Returns the board owner.  
             
         
        """
        pass
    @Owner.setter
    def Owner(self, owner: BoardAttributesBuilder.OwnerEnum):
        """
        Setter for property: ( BoardAttributesBuilder.OwnerEnum NXOpen.P) Owner
         Returns the board owner.  
             
         
        """
        pass
    @property
    def Part(self) -> str:
        """
        Getter for property: (str) Part
         Returns the board part name.  
             
         
        """
        pass
    @Part.setter
    def Part(self, part: str):
        """
        Setter for property: (str) Part
         Returns the board part name.  
             
         
        """
        pass
    @property
    def Revision(self) -> int:
        """
        Getter for property: (int) Revision
         Returns the board revision.  
             
         
        """
        pass
    @Revision.setter
    def Revision(self, revision: int):
        """
        Setter for property: (int) Revision
         Returns the board revision.  
             
         
        """
        pass
import NXOpen
class BoardPropertiesBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit board properties. """
    class BoardStackupOption(Enum):
        """
        Members Include: 
         |FromPart| 
         |FromFile| 
         |FromODB| 
         |FromTeamcenter| 

        """
        FromPart: int
        FromFile: int
        FromODB: int
        FromTeamcenter: int
        @staticmethod
        def ValueOf(value: int) -> BoardPropertiesBuilder.BoardStackupOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GeneratorOption(Enum):
        """
        Members Include: 
         |BoardProperties| 
         |EDABridge| 

        """
        BoardProperties: int
        EDABridge: int
        @staticmethod
        def ValueOf(value: int) -> BoardPropertiesBuilder.GeneratorOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaterialsFromOption(Enum):
        """
        Members Include: 
         |PCBMaterialLibrary| 
         |NXMaterialLibrary| 

        """
        PCBMaterialLibrary: int
        NXMaterialLibrary: int
        @staticmethod
        def ValueOf(value: int) -> BoardPropertiesBuilder.MaterialsFromOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StructuralAlgorithmOption(Enum):
        """
        Members Include: 
         |Equivalent| 

        """
        Equivalent: int
        @staticmethod
        def ValueOf(value: int) -> BoardPropertiesBuilder.StructuralAlgorithmOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThermalAlgorithmOption(Enum):
        """
        Members Include: 
         |Discretized| 
         |Equivalent| 

        """
        Discretized: int
        Equivalent: int
        @staticmethod
        def ValueOf(value: int) -> BoardPropertiesBuilder.ThermalAlgorithmOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AdvancedOptionsFromFile(self) -> bool:
        """
        Getter for property: (bool) AdvancedOptionsFromFile
         Returns the flag indicating whether the advanced options are from the file.  
             
         
        """
        pass
    @AdvancedOptionsFromFile.setter
    def AdvancedOptionsFromFile(self, advancedOptionsFromFile: bool):
        """
        Setter for property: (bool) AdvancedOptionsFromFile
         Returns the flag indicating whether the advanced options are from the file.  
             
         
        """
        pass
    @property
    def AdvancedOptionsFromPart(self) -> bool:
        """
        Getter for property: (bool) AdvancedOptionsFromPart
         Returns the flag indicating whether the advanced options are from the part.  
             
         
        """
        pass
    @AdvancedOptionsFromPart.setter
    def AdvancedOptionsFromPart(self, advancedOptionsFromPart: bool):
        """
        Setter for property: (bool) AdvancedOptionsFromPart
         Returns the flag indicating whether the advanced options are from the part.  
             
         
        """
        pass
    @property
    def BoardPropertyFile(self) -> str:
        """
        Getter for property: (str) BoardPropertyFile
         Returns the board property file.  
             
         
        """
        pass
    @BoardPropertyFile.setter
    def BoardPropertyFile(self, boardPropertyFile: str):
        """
        Setter for property: (str) BoardPropertyFile
         Returns the board property file.  
             
         
        """
        pass
    @property
    def BoardStackup(self) -> BoardPropertiesBuilder.BoardStackupOption:
        """
        Getter for property: ( BoardPropertiesBuilder.BoardStackupOption NXOpen.P) BoardStackup
         Returns the board stackup.  
             
         
        """
        pass
    @BoardStackup.setter
    def BoardStackup(self, boardStackup: BoardPropertiesBuilder.BoardStackupOption):
        """
        Setter for property: ( BoardPropertiesBuilder.BoardStackupOption NXOpen.P) BoardStackup
         Returns the board stackup.  
             
         
        """
        pass
    @property
    def BoardStackupFile(self) -> str:
        """
        Getter for property: (str) BoardStackupFile
         Returns the board stackup file.  
             
         
        """
        pass
    @BoardStackupFile.setter
    def BoardStackupFile(self, boardStackupFile: str):
        """
        Setter for property: (str) BoardStackupFile
         Returns the board stackup file.  
             
         
        """
        pass
    @property
    def BoardStackupNumber(self) -> str:
        """
        Getter for property: (str) BoardStackupNumber
         Returns the board stackup number.  
             
         
        """
        pass
    @BoardStackupNumber.setter
    def BoardStackupNumber(self, stackupNumber: str):
        """
        Setter for property: (str) BoardStackupNumber
         Returns the board stackup number.  
             
         
        """
        pass
    @property
    def BoardStackupODBFolder(self) -> str:
        """
        Getter for property: (str) BoardStackupODBFolder
         Returns the board stackup ODB folder.  
             
         
        """
        pass
    @BoardStackupODBFolder.setter
    def BoardStackupODBFolder(self, boardStackupODBFolder: str):
        """
        Setter for property: (str) BoardStackupODBFolder
         Returns the board stackup ODB folder.  
             
         
        """
        pass
    @property
    def BoardStackupRevision(self) -> str:
        """
        Getter for property: (str) BoardStackupRevision
         Returns the board stackup revision.  
             
         
        """
        pass
    @BoardStackupRevision.setter
    def BoardStackupRevision(self, stackupRevision: str):
        """
        Setter for property: (str) BoardStackupRevision
         Returns the board stackup revision.  
             
         
        """
        pass
    @property
    def CalculationPointsPrecision(self) -> int:
        """
        Getter for property: (int) CalculationPointsPrecision
         Returns the calculation points precision.  
             
         
        """
        pass
    @CalculationPointsPrecision.setter
    def CalculationPointsPrecision(self, calculationPointsPrecision: int):
        """
        Setter for property: (int) CalculationPointsPrecision
         Returns the calculation points precision.  
             
         
        """
        pass
    @property
    def DefaultHolePlatingThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DefaultHolePlatingThickness
         Returns the default hole plating thickness.  
             
         
        """
        pass
    @property
    def DielectricNxMaterial(self) -> int:
        """
        Getter for property: (int) DielectricNxMaterial
         Returns the dielectric material when materials are from the NX material library.  
             
         
        """
        pass
    @DielectricNxMaterial.setter
    def DielectricNxMaterial(self, dielectricNxMaterial: int):
        """
        Setter for property: (int) DielectricNxMaterial
         Returns the dielectric material when materials are from the NX material library.  
             
         
        """
        pass
    @property
    def DielectricPcbMaterial(self) -> int:
        """
        Getter for property: (int) DielectricPcbMaterial
         Returns the dielectric material when materials are from the PCB material library.  
             
         
        """
        pass
    @DielectricPcbMaterial.setter
    def DielectricPcbMaterial(self, dielectricPcbMaterial: int):
        """
        Setter for property: (int) DielectricPcbMaterial
         Returns the dielectric material when materials are from the PCB material library.  
             
         
        """
        pass
    @property
    def Generator(self) -> BoardPropertiesBuilder.GeneratorOption:
        """
        Getter for property: ( BoardPropertiesBuilder.GeneratorOption NXOpen.P) Generator
         Returns the generator.  
             
         
        """
        pass
    @Generator.setter
    def Generator(self, option: BoardPropertiesBuilder.GeneratorOption):
        """
        Setter for property: ( BoardPropertiesBuilder.GeneratorOption NXOpen.P) Generator
         Returns the generator.  
             
         
        """
        pass
    @property
    def MaterialsFrom(self) -> BoardPropertiesBuilder.MaterialsFromOption:
        """
        Getter for property: ( BoardPropertiesBuilder.MaterialsFromOption NXOpen.P) MaterialsFrom
         Returns the materials source.  
             
         
        """
        pass
    @MaterialsFrom.setter
    def MaterialsFrom(self, materialsFrom: BoardPropertiesBuilder.MaterialsFromOption):
        """
        Setter for property: ( BoardPropertiesBuilder.MaterialsFromOption NXOpen.P) MaterialsFrom
         Returns the materials source.  
             
         
        """
        pass
    @property
    def NumberOfCalculationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfCalculationPoints
         Returns the number of calculation points.  
             
         
        """
        pass
    @NumberOfCalculationPoints.setter
    def NumberOfCalculationPoints(self, numberOfCalculationPoints: int):
        """
        Setter for property: (int) NumberOfCalculationPoints
         Returns the number of calculation points.  
             
         
        """
        pass
    @property
    def ReadViasFromFile(self) -> bool:
        """
        Getter for property: (bool) ReadViasFromFile
         Returns the flag indicating whether to read vias from file.  
             
         
        """
        pass
    @ReadViasFromFile.setter
    def ReadViasFromFile(self, readViasFromFile: bool):
        """
        Setter for property: (bool) ReadViasFromFile
         Returns the flag indicating whether to read vias from file.  
             
         
        """
        pass
    @property
    def StructuralAlgorithm(self) -> BoardPropertiesBuilder.StructuralAlgorithmOption:
        """
        Getter for property: ( BoardPropertiesBuilder.StructuralAlgorithmOption NXOpen.P) StructuralAlgorithm
         Returns the structural algorithm.  
             
         
        """
        pass
    @StructuralAlgorithm.setter
    def StructuralAlgorithm(self, algorithm: BoardPropertiesBuilder.StructuralAlgorithmOption):
        """
        Setter for property: ( BoardPropertiesBuilder.StructuralAlgorithmOption NXOpen.P) StructuralAlgorithm
         Returns the structural algorithm.  
             
         
        """
        pass
    @property
    def ThermalAlgorithm(self) -> BoardPropertiesBuilder.ThermalAlgorithmOption:
        """
        Getter for property: ( BoardPropertiesBuilder.ThermalAlgorithmOption NXOpen.P) ThermalAlgorithm
         Returns the thermal algorithm.  
             
         
        """
        pass
    @ThermalAlgorithm.setter
    def ThermalAlgorithm(self, algorithm: BoardPropertiesBuilder.ThermalAlgorithmOption):
        """
        Setter for property: ( BoardPropertiesBuilder.ThermalAlgorithmOption NXOpen.P) ThermalAlgorithm
         Returns the thermal algorithm.  
             
         
        """
        pass
    @property
    def TraceNxMaterial(self) -> int:
        """
        Getter for property: (int) TraceNxMaterial
         Returns the trace material when materials are from theNX material library.  
             
         
        """
        pass
    @TraceNxMaterial.setter
    def TraceNxMaterial(self, traceNxMaterial: int):
        """
        Setter for property: (int) TraceNxMaterial
         Returns the trace material when materials are from theNX material library.  
             
         
        """
        pass
    @property
    def TracePcbMaterial(self) -> int:
        """
        Getter for property: (int) TracePcbMaterial
         Returns the trace material when materials are from the PCB material library.  
             
         
        """
        pass
    @TracePcbMaterial.setter
    def TracePcbMaterial(self, tracePcbMaterial: int):
        """
        Setter for property: (int) TracePcbMaterial
         Returns the trace material when materials are from the PCB material library.  
             
         
        """
        pass
    @property
    def UseCurrentWorkPart(self) -> bool:
        """
        Getter for property: (bool) UseCurrentWorkPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    @UseCurrentWorkPart.setter
    def UseCurrentWorkPart(self, useCurrentWorkPart: bool):
        """
        Setter for property: (bool) UseCurrentWorkPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    @property
    def ViaNxMaterial(self) -> int:
        """
        Getter for property: (int) ViaNxMaterial
         Returns the via material when materials are from the NX material library.  
             
         
        """
        pass
    @ViaNxMaterial.setter
    def ViaNxMaterial(self, viaNxMaterial: int):
        """
        Setter for property: (int) ViaNxMaterial
         Returns the via material when materials are from the NX material library.  
             
         
        """
        pass
    @property
    def ViaPcbMaterial(self) -> int:
        """
        Getter for property: (int) ViaPcbMaterial
         Returns the via material when materials are from the PCB material library.  
             
         
        """
        pass
    @ViaPcbMaterial.setter
    def ViaPcbMaterial(self, viaPcbMaterial: int):
        """
        Setter for property: (int) ViaPcbMaterial
         Returns the via material when materials are from the PCB material library.  
             
         
        """
        pass
    @property
    def ViewCalculationReport(self) -> bool:
        """
        Getter for property: (bool) ViewCalculationReport
         Returns the flag indicating whether to show the calculation report after the calculation.  
             
         
        """
        pass
    @ViewCalculationReport.setter
    def ViewCalculationReport(self, viewCalculationReport: bool):
        """
        Setter for property: (bool) ViewCalculationReport
         Returns the flag indicating whether to show the calculation report after the calculation.  
             
         
        """
        pass
class BoardSide(Enum):
    """
    Members Include: 
     |Both|  Either side. 
     |Top|  The Top side. 
     |Bottom|  The Bottom side. 

    """
    Both: int
    Top: int
    Bottom: int
    @staticmethod
    def ValueOf(value: int) -> BoardSide:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class CompareAndUpdateBuilder(NXOpen.Builder): 
    """ Represents a builder to compare MCAD and ECAD files and update. """
    class AssemblyUpdateEnum(Enum):
        """
        Members Include: 
         |All| 
         |NotSet| 
         |Specify| 

        """
        All: int
        NotSet: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> CompareAndUpdateBuilder.AssemblyUpdateEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BoardUpdateEnum(Enum):
        """
        Members Include: 
         |All| 
         |NotSet| 

        """
        All: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> CompareAndUpdateBuilder.BoardUpdateEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CompareEnum(Enum):
        """
        Members Include: 
         |All| 
         |BoardOnly| 

        """
        All: int
        BoardOnly: int
        @staticmethod
        def ValueOf(value: int) -> CompareAndUpdateBuilder.CompareEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EcadLocationEnum(Enum):
        """
        Members Include: 
         |Local| 
         |Teamcenter| 

        """
        Local: int
        Teamcenter: int
        @staticmethod
        def ValueOf(value: int) -> CompareAndUpdateBuilder.EcadLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssemblyUpdateOptions(self) -> CompareAndUpdateBuilder.AssemblyUpdateEnum:
        """
        Getter for property: ( CompareAndUpdateBuilder.AssemblyUpdateEnum NXOpen.P) AssemblyUpdateOptions
         Returns the assembly update options.  
             
         
        """
        pass
    @AssemblyUpdateOptions.setter
    def AssemblyUpdateOptions(self, assemblyUpdateOptions: CompareAndUpdateBuilder.AssemblyUpdateEnum):
        """
        Setter for property: ( CompareAndUpdateBuilder.AssemblyUpdateEnum NXOpen.P) AssemblyUpdateOptions
         Returns the assembly update options.  
             
         
        """
        pass
    @property
    def BoardFile(self) -> str:
        """
        Getter for property: (str) BoardFile
         Returns the board file when the board does not come from ODB.  
             
         
        """
        pass
    @BoardFile.setter
    def BoardFile(self, boardFile: str):
        """
        Setter for property: (str) BoardFile
         Returns the board file when the board does not come from ODB.  
             
         
        """
        pass
    @property
    def BoardFolder(self) -> str:
        """
        Getter for property: (str) BoardFolder
         Returns the folder when the board comes from ODB.  
             
         
        """
        pass
    @BoardFolder.setter
    def BoardFolder(self, boardFolder: str):
        """
        Setter for property: (str) BoardFolder
         Returns the folder when the board comes from ODB.  
             
         
        """
        pass
    @property
    def BoardThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BoardThickness
         Returns the board thickness when the thickness is overriden.  
             
         
        """
        pass
    @property
    def BoardUpdateOptions(self) -> CompareAndUpdateBuilder.BoardUpdateEnum:
        """
        Getter for property: ( CompareAndUpdateBuilder.BoardUpdateEnum NXOpen.P) BoardUpdateOptions
         Returns the board update options.  
             
         
        """
        pass
    @BoardUpdateOptions.setter
    def BoardUpdateOptions(self, boardUpdateOptions: CompareAndUpdateBuilder.BoardUpdateEnum):
        """
        Setter for property: ( CompareAndUpdateBuilder.BoardUpdateEnum NXOpen.P) BoardUpdateOptions
         Returns the board update options.  
             
         
        """
        pass
    @property
    def CompareOptions(self) -> CompareAndUpdateBuilder.CompareEnum:
        """
        Getter for property: ( CompareAndUpdateBuilder.CompareEnum NXOpen.P) CompareOptions
         Returns the compare options.  
             
         
        """
        pass
    @CompareOptions.setter
    def CompareOptions(self, compareOptions: CompareAndUpdateBuilder.CompareEnum):
        """
        Setter for property: ( CompareAndUpdateBuilder.CompareEnum NXOpen.P) CompareOptions
         Returns the compare options.  
             
         
        """
        pass
    @property
    def ECADEntityFilter(self) -> EntityFilter:
        """
        Getter for property: ( EntityFilter NXOpen.P) ECADEntityFilter
         Returns the ECAD filters.  
             
         
        """
        pass
    @ECADEntityFilter.setter
    def ECADEntityFilter(self, filter: EntityFilter):
        """
        Setter for property: ( EntityFilter NXOpen.P) ECADEntityFilter
         Returns the ECAD filters.  
             
         
        """
        pass
    @property
    def EcadLocation(self) -> CompareAndUpdateBuilder.EcadLocationEnum:
        """
        Getter for property: ( CompareAndUpdateBuilder.EcadLocationEnum NXOpen.P) EcadLocation
         Returns the ECAD file location option.  
             
         
        """
        pass
    @EcadLocation.setter
    def EcadLocation(self, ecadLocation: CompareAndUpdateBuilder.EcadLocationEnum):
        """
        Setter for property: ( CompareAndUpdateBuilder.EcadLocationEnum NXOpen.P) EcadLocation
         Returns the ECAD file location option.  
             
         
        """
        pass
    @property
    def EcadNumber(self) -> str:
        """
        Getter for property: (str) EcadNumber
         Returns the ECAD number.  
             
         
        """
        pass
    @EcadNumber.setter
    def EcadNumber(self, ecadNumber: str):
        """
        Setter for property: (str) EcadNumber
         Returns the ECAD number.  
             
         
        """
        pass
    @property
    def EcadRevision(self) -> str:
        """
        Getter for property: (str) EcadRevision
         Returns the ECAD revision.  
             
         
        """
        pass
    @EcadRevision.setter
    def EcadRevision(self, ecadRevision: str):
        """
        Setter for property: (str) EcadRevision
         Returns the ECAD revision.  
             
         
        """
        pass
    @property
    def FilterEcadModel(self) -> bool:
        """
        Getter for property: (bool) FilterEcadModel
         Returns the flag indicating whether to filter the ECAD model.  
             
         
        """
        pass
    @FilterEcadModel.setter
    def FilterEcadModel(self, filterEcadModel: bool):
        """
        Setter for property: (bool) FilterEcadModel
         Returns the flag indicating whether to filter the ECAD model.  
             
         
        """
        pass
    @property
    def FilterNxModel(self) -> bool:
        """
        Getter for property: (bool) FilterNxModel
         Returns the flag indicating whether to filter the NX model.  
             
         
        """
        pass
    @FilterNxModel.setter
    def FilterNxModel(self, filterNxModel: bool):
        """
        Setter for property: (bool) FilterNxModel
         Returns the flag indicating whether to filter the NX model.  
             
         
        """
        pass
    @property
    def FromOdbFolder(self) -> bool:
        """
        Getter for property: (bool) FromOdbFolder
         Returns the flag indicating whether the board comes from ODB.  
             
         
        """
        pass
    @FromOdbFolder.setter
    def FromOdbFolder(self, fromOdbFolder: bool):
        """
        Setter for property: (bool) FromOdbFolder
         Returns the flag indicating whether the board comes from ODB.  
             
         
        """
        pass
    @property
    def LibraryFile(self) -> str:
        """
        Getter for property: (str) LibraryFile
         Returns the library file when the board does not come from ODB.  
             
         
        """
        pass
    @LibraryFile.setter
    def LibraryFile(self, libraryFile: str):
        """
        Setter for property: (str) LibraryFile
         Returns the library file when the board does not come from ODB.  
             
         
        """
        pass
    @property
    def NXEntityFilter(self) -> EntityFilter:
        """
        Getter for property: ( EntityFilter NXOpen.P) NXEntityFilter
         Returns the NX model filters.  
             
         
        """
        pass
    @NXEntityFilter.setter
    def NXEntityFilter(self, filter: EntityFilter):
        """
        Setter for property: ( EntityFilter NXOpen.P) NXEntityFilter
         Returns the NX model filters.  
             
         
        """
        pass
    @property
    def OnlyUseExistingComponents(self) -> bool:
        """
        Getter for property: (bool) OnlyUseExistingComponents
         Returns the flag indicating whether to only use existing components.  
             
         
        """
        pass
    @OnlyUseExistingComponents.setter
    def OnlyUseExistingComponents(self, onlyUseExistingComponents: bool):
        """
        Setter for property: (bool) OnlyUseExistingComponents
         Returns the flag indicating whether to only use existing components.  
             
         
        """
        pass
    @property
    def OverrideBoardThickness(self) -> bool:
        """
        Getter for property: (bool) OverrideBoardThickness
         Returns the flag indicating whether to override the board thickness.  
             
         
        """
        pass
    @OverrideBoardThickness.setter
    def OverrideBoardThickness(self, overrideBoardThickness: bool):
        """
        Setter for property: (bool) OverrideBoardThickness
         Returns the flag indicating whether to override the board thickness.  
             
         
        """
        pass
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @property
    def UseCurrentWorkPart(self) -> bool:
        """
        Getter for property: (bool) UseCurrentWorkPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    @UseCurrentWorkPart.setter
    def UseCurrentWorkPart(self, useCurrentWorkPart: bool):
        """
        Setter for property: (bool) UseCurrentWorkPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    def Compare(self) -> None:
        """
         Compares the assemblies. 
        """
        pass
    def PreviewChanges(self) -> None:
        """
         Previews all changes. 
        """
        pass
    def SetUpdateOption(self, resDef: str, status: bool) -> None:
        """
         Sets the update option flag. 
        """
        pass
    def UnhighlightAll(self) -> None:
        """
         Un-highlights all. 
        """
        pass
import NXOpen
class ComponentAttributesBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit component attributes. """
    class PlacementOwnerEnum(Enum):
        """
        Members Include: 
         |Mcad| 
         |Ecad| 
         |Placed| 
         |Unplaced| 

        """
        Mcad: int
        Ecad: int
        Placed: int
        Unplaced: int
        @staticmethod
        def ValueOf(value: int) -> ComponentAttributesBuilder.PlacementOwnerEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Components(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Components
         Returns the components.  
             
         
        """
        pass
    @property
    def PackageClearanceTypesModification(self) -> bool:
        """
        Getter for property: (bool) PackageClearanceTypesModification
         Returns the flag indicating whether a component package clearance types change is allowed.  
             
         
        """
        pass
    @PackageClearanceTypesModification.setter
    def PackageClearanceTypesModification(self, canModification: bool):
        """
        Setter for property: (bool) PackageClearanceTypesModification
         Returns the flag indicating whether a component package clearance types change is allowed.  
             
         
        """
        pass
    @property
    def PackageName(self) -> str:
        """
        Getter for property: (str) PackageName
         Returns the component package name.  
             
         
        """
        pass
    @PackageName.setter
    def PackageName(self, packageName: str):
        """
        Setter for property: (str) PackageName
         Returns the component package name.  
             
         
        """
        pass
    @property
    def PackageNameModification(self) -> bool:
        """
        Getter for property: (bool) PackageNameModification
         Returns the flag indicating whether a component package name change is allowed.  
             
         
        """
        pass
    @PackageNameModification.setter
    def PackageNameModification(self, canModification: bool):
        """
        Setter for property: (bool) PackageNameModification
         Returns the flag indicating whether a component package name change is allowed.  
             
         
        """
        pass
    @property
    def PartNumber(self) -> str:
        """
        Getter for property: (str) PartNumber
         Returns the component part number.  
             
         
        """
        pass
    @PartNumber.setter
    def PartNumber(self, partNumber: str):
        """
        Setter for property: (str) PartNumber
         Returns the component part number.  
             
         
        """
        pass
    @property
    def PartNumberModification(self) -> bool:
        """
        Getter for property: (bool) PartNumberModification
         Returns the flag indicating whether a component part number change is allowed.  
             
         
        """
        pass
    @PartNumberModification.setter
    def PartNumberModification(self, canModification: bool):
        """
        Setter for property: (bool) PartNumberModification
         Returns the flag indicating whether a component part number change is allowed.  
             
         
        """
        pass
    @property
    def PlacementOwner(self) -> ComponentAttributesBuilder.PlacementOwnerEnum:
        """
        Getter for property: ( ComponentAttributesBuilder.PlacementOwnerEnum NXOpen.P) PlacementOwner
         Returns the component placementowner.  
             
         
        """
        pass
    @PlacementOwner.setter
    def PlacementOwner(self, placementOwner: ComponentAttributesBuilder.PlacementOwnerEnum):
        """
        Setter for property: ( ComponentAttributesBuilder.PlacementOwnerEnum NXOpen.P) PlacementOwner
         Returns the component placementowner.  
             
         
        """
        pass
    @property
    def ReferenceDesignator(self) -> str:
        """
        Getter for property: (str) ReferenceDesignator
         Returns the component reference designator.  
             
         
        """
        pass
    @ReferenceDesignator.setter
    def ReferenceDesignator(self, referenceDesignator: str):
        """
        Setter for property: (str) ReferenceDesignator
         Returns the component reference designator.  
             
         
        """
        pass
    @property
    def ReferenceDesignatorModification(self) -> bool:
        """
        Getter for property: (bool) ReferenceDesignatorModification
         Returns the flag indicating whether a component reference designator change is allowed.  
             
         
        """
        pass
    @ReferenceDesignatorModification.setter
    def ReferenceDesignatorModification(self, canModification: bool):
        """
        Setter for property: (bool) ReferenceDesignatorModification
         Returns the flag indicating whether a component reference designator change is allowed.  
             
         
        """
        pass
    def GetPackageClearanceTypes(self) -> List[str]:
        """
         Gets the package clearance types. 
         Returns data (List[str]): .
        """
        pass
    def SetPackageClearanceTypes(self, data: List[str]) -> None:
        """
         Sets the package clearance types. 
        """
        pass
import NXOpen
class ComponentConstraintsBuilder(NXOpen.Builder): 
    """ Represents a builder to create, edit, or remove automatic component-board constraints. """
    class ActionEnum(Enum):
        """
        Members Include: 
         |Add| 
         |Remove| 

        """
        Add: int
        Remove: int
        @staticmethod
        def ValueOf(value: int) -> ComponentConstraintsBuilder.ActionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Action(self) -> ComponentConstraintsBuilder.ActionEnum:
        """
        Getter for property: ( ComponentConstraintsBuilder.ActionEnum NXOpen.P) Action
         Returns the action to be performed on the component-board constraints by the builder.  
             
         
        """
        pass
    @Action.setter
    def Action(self, action: ComponentConstraintsBuilder.ActionEnum):
        """
        Setter for property: ( ComponentConstraintsBuilder.ActionEnum NXOpen.P) Action
         Returns the action to be performed on the component-board constraints by the builder.  
             
         
        """
        pass
    @property
    def BoardFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BoardFaces
         Returns the selected board faces.  
             
         
        """
        pass
import NXOpen
import NXOpen.Features
class ComponentCsysBuilder(NXOpen.Builder): 
    """ Represents a builder to create a component csys attribute. """
    @property
    def Selection(self) -> NXOpen.Features.SelectDatumCsys:
        """
        Getter for property: ( NXOpen.Features.SelectDatumCsys) Selection
         Returns the csys selection.  
            
         
        """
        pass
import NXOpen
class ComponentPlacementOutlineBuilder(NXOpen.Builder): 
    """ Represents a builder to create a component placement outline attribute. """
    @property
    def Sketch(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Sketch
         Returns the sketch.  
            
         
        """
        pass
class ConductiveLayerSide(Enum):
    """
    Members Include: 
     |All|  Any layer. 
     |Top|  The Top layer. 
     |Bottom|  The Bottom layer. 
     |Outer|  Either Top or Bottom layer. 
     |Inner|  Inner layer. 

    """
    All: int
    Top: int
    Bottom: int
    Outer: int
    Inner: int
    @staticmethod
    def ValueOf(value: int) -> ConductiveLayerSide:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class DesignInterference(NXOpen.TaggedObject): 
    """ Represents a Design Interference for Pcb Exchange Design Validation. """
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
         Returns the distance.  
             
         
        """
        pass
    @property
    def PrimaryEntity(self) -> str:
        """
        Getter for property: (str) PrimaryEntity
         Returns the primary entity.  
             
         
        """
        pass
    @property
    def ResultType(self) -> str:
        """
        Getter for property: (str) ResultType
         Returns the result type.  
             
         
        """
        pass
    @property
    def Rule(self) -> DesignRule:
        """
        Getter for property: ( DesignRule NXOpen.P) Rule
         Returns the rule.  
             
         
        """
        pass
    @property
    def RuleMeasurement(self) -> str:
        """
        Getter for property: (str) RuleMeasurement
         Returns the rule measurement.  
             
         
        """
        pass
    @property
    def RuleName(self) -> str:
        """
        Getter for property: (str) RuleName
         Returns the rule name.  
             
         
        """
        pass
    @property
    def RuleSeverity(self) -> str:
        """
        Getter for property: (str) RuleSeverity
         Returns the rule severity.  
             
         
        """
        pass
    @property
    def RuleType(self) -> str:
        """
        Getter for property: (str) RuleType
         Returns the rule type.  
             
         
        """
        pass
    @property
    def SecondaryEntity(self) -> str:
        """
        Getter for property: (str) SecondaryEntity
         Returns the secondary entity.  
             
         
        """
        pass
import NXOpen
class DesignRuleBuilder(NXOpen.Builder): 
    """ Creates or edits NXOpen.PcbExchange.DesignRule.
        A call to NXOpen.Builder.Commit on this builder will only return .
    """
    class ComponentFilter(Enum):
        """
        Members Include: 
         |Any|  Accept any Pcb Components. 
         |ByPackage|  Filter Pcb Components by Package Name. 
         |ByOwner|  Filter Pcb Components by Owner. 
         |ByRefDes|  Filter Pcb Components by Reference Designator. 
         |ByPartNumber|  Filter Pcb Components by Part Number. 
         |ByCompType|  Filter Pcb Components by Type. 
         |ByPartName|  Filter Mechnanical entity by Part Name. 
         |ByAreaName|  Filter Area by Name. 
         |ByAreaSubtype|  Filter Area by Subtype. 
         |ByAreaOwner|  Filter Area by Owner. 
         |ByAreaLayer|  Filter Area by Layer. 
         |Specify|  Filter by selection. 
         |ByNetName|  Filter Copper by Net Name. 
         |ByPackageClearanceType|  Filter Pcb Components by Package Clearance Type. 
         |ByWireBondNetName|  Filter Wire Bond by Net Name. 

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
        @staticmethod
        def ValueOf(value: int) -> DesignRuleBuilder.ComponentFilter:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConstraintType(self) -> DesignRuleType:
        """
        Getter for property: ( DesignRuleType NXOpen.P) ConstraintType
         Returns the constraint type.  
             
         
        """
        pass
    @ConstraintType.setter
    def ConstraintType(self, constraintType: DesignRuleType):
        """
        Setter for property: ( DesignRuleType NXOpen.P) ConstraintType
         Returns the constraint type.  
             
         
        """
        pass
    @property
    def MeasurementType(self) -> DesignRuleMeasurement:
        """
        Getter for property: ( DesignRuleMeasurement NXOpen.P) MeasurementType
         Returns the measurement type.  
             
         
        """
        pass
    @MeasurementType.setter
    def MeasurementType(self, measurementType: DesignRuleMeasurement):
        """
        Setter for property: ( DesignRuleMeasurement NXOpen.P) MeasurementType
         Returns the measurement type.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the rule name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the rule name.  
             
         
        """
        pass
    @property
    def Severity(self) -> DesignRuleSeverity:
        """
        Getter for property: ( DesignRuleSeverity NXOpen.P) Severity
         Returns the design rule severity.  
             
         
        """
        pass
    @Severity.setter
    def Severity(self, severity: DesignRuleSeverity):
        """
        Setter for property: ( DesignRuleSeverity NXOpen.P) Severity
         Returns the design rule severity.  
             
         
        """
        pass
    def GetBoardSide(self, filterIndex: int) -> BoardSide:
        """
         Gets an optional board side parameter for the component filter for a given side of the constraint. 
         Returns side ( BoardSide NXOpen.P): .
        """
        pass
    def GetClearance(self, direction: DesignRuleMargin) -> float:
        """
         Gets the clearance requirement in a given direction. The value is expressed in Part Units. 
         Returns clearance (float):  The clearance value in Part Units. .
        """
        pass
    def GetComponentFilter(self, filterIndex: int) -> DesignRuleBuilder.ComponentFilter:
        """
         Gets the component filter criteria for a given side of the constraint. Only applicable when NXOpen.PcbExchange.EntityCategory is NXOpen.PcbExchange.EntityCategory.Component. 
         Returns componentFilter ( DesignRuleBuilder.ComponentFilter NXOpen.P): .
        """
        pass
    def GetConductiveLayerSide(self, filterIndex: int) -> ConductiveLayerSide:
        """
         Gets an optional conductive layer side parameter for the copper filter for a given side of the constraint. 
         Returns side ( ConductiveLayerSide NXOpen.P): .
        """
        pass
    def GetEntityType(self, filterIndex: int) -> EntityCategory:
        """
         Gets the entity category for a given side of the constraint. 
         Returns entityType ( EntityCategory NXOpen.P): .
        """
        pass
    def GetFilterData(self, filterIndex: int) -> List[str]:
        """
         Gets an optional string parameters for the component filter for a given side of the constraint. 
         Returns data (List[str]): .
        """
        pass
    def GetWireBondSide(self, filterIndex: int) -> WireBondSide:
        """
         Gets an optional wire bond side parameter for the wire bond filter for a given side of the constraint. 
         Returns side ( WireBondSide NXOpen.P): .
        """
        pass
    def SetBoardSide(self, filterIndex: int, side: BoardSide) -> None:
        """
         Sets an optional board side parameter for the component filter for a given side of the constraint. 
        """
        pass
    def SetClearance(self, direction: DesignRuleMargin, clearance: float) -> None:
        """
         Sets the clearance requirement in a given direction. The value is expressed in Part Units. 
        """
        pass
    def SetComponentFilter(self, filterIndex: int, componentFilter: DesignRuleBuilder.ComponentFilter) -> None:
        """
         Sets the component filter criteria for a given side of the constraint. Only applicable when NXOpen.PcbExchange.EntityCategory is NXOpen.PcbExchange.EntityCategory.Component. 
        """
        pass
    def SetConductiveLayerSide(self, filterIndex: int, side: ConductiveLayerSide) -> None:
        """
         Sets an optional conductive layer side parameter for the copper filter for a given side of the constraint. 
        """
        pass
    def SetEntityType(self, filterIndex: int, entityType: EntityCategory) -> None:
        """
         Sets the entity category for a given side of the constraint. 
        """
        pass
    @overload
    def SetFilterData(self, filterIndex: int, data: str) -> None:
        """
         Sets an optional string parameter for the component filter for a given side of the constraint. 
        """
        pass
    @overload
    def SetFilterData(self, filterIndex: int, data: List[str]) -> None:
        """
         Sets optional string parameters for the component filter for a given side of the constraint. 
        """
        pass
    def SetWireBondSide(self, filterIndex: int, side: WireBondSide) -> None:
        """
         Sets an optional wire bond side parameter for the wire bond filter for a given side of the constraint. 
        """
        pass
class DesignRuleMargin(Enum):
    """
    Members Include: 
     |OrthoXY|  The XY constraint of a NXOpen.PcbExchange.DesignRuleType.Ortho rule. 
     |OrthoZ|  The Z constraint of a NXOpen.PcbExchange.DesignRuleType.Ortho rule. 
     |Xyz|  The XYZ constraint of a NXOpen.PcbExchange.DesignRuleType.Distance rule. 
     |LongToLong|  The long side to long side constraint of a NXOpen.PcbExchange.DesignRuleType.EdgeToEdge rule. 
     |ShortToShort|  The short side to short side constraint of a NXOpen.PcbExchange.DesignRuleType.EdgeToEdge rule. 
     |LongToShort|  The long side to short side constraint of a NXOpen.PcbExchange.DesignRuleType.EdgeToEdge rule. 
     |ShortToLong|  The short side to long side constraint of a NXOpen.PcbExchange.DesignRuleType.EdgeToEdge rule. 
     |Z|  The Z constraint of a NXOpen.PcbExchange.DesignRuleType.EdgeToEdge rule. 

    """
    OrthoXY: int
    OrthoZ: int
    Xyz: int
    LongToLong: int
    ShortToShort: int
    LongToShort: int
    ShortToLong: int
    Z: int
    @staticmethod
    def ValueOf(value: int) -> DesignRuleMargin:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DesignRuleMeasurement(Enum):
    """
    Members Include: 
     |Lightweight| 
     |Exact| 

    """
    Lightweight: int
    Exact: int
    @staticmethod
    def ValueOf(value: int) -> DesignRuleMeasurement:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DesignRuleSeverity(Enum):
    """
    Members Include: 
     |Minimum|  The constraints specifies the minimum threshold. 
     |Optimal|  The constraints specifies the optimal threshold. 

    """
    Minimum: int
    Optimal: int
    @staticmethod
    def ValueOf(value: int) -> DesignRuleSeverity:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DesignRuleType(Enum):
    """
    Members Include: 
     |Ortho|  Orthogonal check. The clearance requirement is expressed independently in the XY plane, and along the Z axis. 
     |Distance|  Cartesian distance check. The clearance requirement is defined as a 3D distance. 
     |EdgeToEdge|  Edge to edge distance check. The clearance requirement is defined as the distance between shorter andor longer sides of the objects. 

    """
    Ortho: int
    Distance: int
    EdgeToEdge: int
    @staticmethod
    def ValueOf(value: int) -> DesignRuleType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class DesignRule(NXOpen.TaggedObject): 
    """ Represents a Design Rule for Pcb Exchange Design Validation. """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the rule name.  
             
         
        """
        pass
    def DecreasePriority(self) -> DesignRule:
        """
         Decreases the rule priority. Moves the rule down in the priority ranking. Returns the rule that was immediately below it, or  if the rule is already in last place. 
         Returns otherRule ( DesignRule NXOpen.P):  Rule substituted with. .
        """
        pass
    def Destroy(self) -> None:
        """
         Deletes the rule. 
        """
        pass
    def IncreasePriority(self) -> DesignRule:
        """
         Increases the rule priority. Moves the rule up in the priority ranking. Returns the rule that was immediately above it, or  if the rule is already in first place. 
         Returns otherRule ( DesignRule NXOpen.P):  Rule substituted with. .
        """
        pass
import NXOpen
class DesignValidator(NXOpen.TransientObject): 
    """ Performs validation of Pcb Exchange design. """
    @property
    def InterferenceCount(self) -> int:
        """
        Getter for property: (int) InterferenceCount
         Returns the number of interferences.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Disposes of this instance. 
        """
        pass
    def ExportInterferences(self, filename: str) -> None:
        """
         Exports the list of interferences to a file. 
        """
        pass
    def GetInterferences(self) -> List[DesignInterference]:
        """
         Gets the list of interferences. 
         Returns interferences ( DesignInterference List[NXOpen): .
        """
        pass
    def PerformAnalysis(self) -> None:
        """
         Performs design analysis. 
        """
        pass
    def PerformAnalysisBasedOnScope(self, isWorkPartOnly: bool) -> None:
        """
         Performs design analysis based on the assembly scope. 
        """
        pass
    def ResetAnalysis(self) -> None:
        """
         Clears the list of interferences and resets the analysis state. 
        """
        pass
import NXOpen
class EcadExportBuilder(NXOpen.Builder): 
    """ Represents a builder to export ECAD model. """
    class EcadLocationEnum(Enum):
        """
        Members Include: 
         |Os| 
         |Tc| 

        """
        Os: int
        Tc: int
        @staticmethod
        def ValueOf(value: int) -> EcadExportBuilder.EcadLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ExportUnitsEnum(Enum):
        """
        Members Include: 
         |Mm| 
         |Thou| 

        """
        Mm: int
        Thou: int
        @staticmethod
        def ValueOf(value: int) -> EcadExportBuilder.ExportUnitsEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FileFormatEnum(Enum):
        """
        Members Include: 
         |Idf2| 
         |Idf3| 
         |Idf4| 
         |Zbmb| 
         |Zpcb| 
         |Idx2| 
         |Idx3| 

        """
        Idf2: int
        Idf3: int
        Idf4: int
        Zbmb: int
        Zpcb: int
        Idx2: int
        Idx3: int
        @staticmethod
        def ValueOf(value: int) -> EcadExportBuilder.FileFormatEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoardFile(self) -> str:
        """
        Getter for property: (str) BoardFile
         Returns the board file.  
             
         
        """
        pass
    @BoardFile.setter
    def BoardFile(self, boardFile: str):
        """
        Setter for property: (str) BoardFile
         Returns the board file.  
             
         
        """
        pass
    @property
    def BoardOnly(self) -> bool:
        """
        Getter for property: (bool) BoardOnly
         Returns the flag indicating whether to export only the board.  
             
         
        """
        pass
    @BoardOnly.setter
    def BoardOnly(self, boardOnly: bool):
        """
        Setter for property: (bool) BoardOnly
         Returns the flag indicating whether to export only the board.  
             
         
        """
        pass
    @property
    def EcadLocation(self) -> EcadExportBuilder.EcadLocationEnum:
        """
        Getter for property: ( EcadExportBuilder.EcadLocationEnum NXOpen.P) EcadLocation
         Returns the location of the ECAD file.  
             
         
        """
        pass
    @EcadLocation.setter
    def EcadLocation(self, ecadLocation: EcadExportBuilder.EcadLocationEnum):
        """
        Setter for property: ( EcadExportBuilder.EcadLocationEnum NXOpen.P) EcadLocation
         Returns the location of the ECAD file.  
             
         
        """
        pass
    @property
    def EcadNumber(self) -> str:
        """
        Getter for property: (str) EcadNumber
         Returns the ECAD number.  
             
         
        """
        pass
    @EcadNumber.setter
    def EcadNumber(self, ecadNumber: str):
        """
        Setter for property: (str) EcadNumber
         Returns the ECAD number.  
             
         
        """
        pass
    @property
    def EcadRevision(self) -> str:
        """
        Getter for property: (str) EcadRevision
         Returns the ECAD revision.  
             
         
        """
        pass
    @EcadRevision.setter
    def EcadRevision(self, ecadRevision: str):
        """
        Setter for property: (str) EcadRevision
         Returns the ECAD revision.  
             
         
        """
        pass
    @property
    def FileFormat(self) -> EcadExportBuilder.FileFormatEnum:
        """
        Getter for property: ( EcadExportBuilder.FileFormatEnum NXOpen.P) FileFormat
         Returns the file format.  
             
         
        """
        pass
    @FileFormat.setter
    def FileFormat(self, fileFormat: EcadExportBuilder.FileFormatEnum):
        """
        Setter for property: ( EcadExportBuilder.FileFormatEnum NXOpen.P) FileFormat
         Returns the file format.  
             
         
        """
        pass
    @property
    def FileUnits(self) -> EcadExportBuilder.ExportUnitsEnum:
        """
        Getter for property: ( EcadExportBuilder.ExportUnitsEnum NXOpen.P) FileUnits
         Returns the file units.  
             
         
        """
        pass
    @FileUnits.setter
    def FileUnits(self, exportUnits: EcadExportBuilder.ExportUnitsEnum):
        """
        Setter for property: ( EcadExportBuilder.ExportUnitsEnum NXOpen.P) FileUnits
         Returns the file units.  
             
         
        """
        pass
    @property
    def LibraryFile(self) -> str:
        """
        Getter for property: (str) LibraryFile
         Returns the library file.  
             
         
        """
        pass
    @LibraryFile.setter
    def LibraryFile(self, libraryFile: str):
        """
        Setter for property: (str) LibraryFile
         Returns the library file.  
             
         
        """
        pass
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @property
    def UseCurrentWorkPart(self) -> bool:
        """
        Getter for property: (bool) UseCurrentWorkPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    @UseCurrentWorkPart.setter
    def UseCurrentWorkPart(self, useCurrentWorkPart: bool):
        """
        Setter for property: (bool) UseCurrentWorkPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    @property
    def UseEntityFilter(self) -> bool:
        """
        Getter for property: (bool) UseEntityFilter
         Returns the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    @UseEntityFilter.setter
    def UseEntityFilter(self, useEntityFilter: bool):
        """
        Setter for property: (bool) UseEntityFilter
         Returns the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    def GetAreaMapping(self) -> AreaMapping:
        """
         Gets the area mapping. 
         Returns areaMapping ( AreaMapping NXOpen.P): .
        """
        pass
    def GetEntityFilter(self) -> EntityFilter:
        """
         Gets the entity filter. 
         Returns filter ( EntityFilter NXOpen.P): .
        """
        pass
    def RunPreExportEcadHook(self) -> None:
        """
         Runs the pre-export ECAD hook and sets the board file, if defined. 
        """
        pass
    def SetAreaMapping(self, areaMapping: AreaMapping) -> None:
        """
         Sets the area mapping. 
        """
        pass
    def SetEntityFilter(self, filter: EntityFilter) -> None:
        """
         Sets the entity filter. 
        """
        pass
import NXOpen
class EcadImportBuilder(NXOpen.Builder): 
    """ Represents a builder to import ECAD model. """
    class EcadLocationEnum(Enum):
        """
        Members Include: 
         |Os| 
         |Tc| 

        """
        Os: int
        Tc: int
        @staticmethod
        def ValueOf(value: int) -> EcadImportBuilder.EcadLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImportOptionEnum(Enum):
        """
        Members Include: 
         |All| 
         |BoardOnly| 

        """
        All: int
        BoardOnly: int
        @staticmethod
        def ValueOf(value: int) -> EcadImportBuilder.ImportOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoardFile(self) -> str:
        """
        Getter for property: (str) BoardFile
         Returns the board file.  
             
         
        """
        pass
    @BoardFile.setter
    def BoardFile(self, boardFile: str):
        """
        Setter for property: (str) BoardFile
         Returns the board file.  
             
         
        """
        pass
    @property
    def BoardFolder(self) -> str:
        """
        Getter for property: (str) BoardFolder
         Returns the board folder.  
             
         
        """
        pass
    @BoardFolder.setter
    def BoardFolder(self, boardFolder: str):
        """
        Setter for property: (str) BoardFolder
         Returns the board folder.  
             
         
        """
        pass
    @property
    def BoardThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BoardThickness
         Returns the board thickness when the thickness is overriden.  
             
         
        """
        pass
    @property
    def EcadDatasetName(self) -> str:
        """
        Getter for property: (str) EcadDatasetName
         Returns the ECAD dataset name.  
             
         
        """
        pass
    @EcadDatasetName.setter
    def EcadDatasetName(self, ecadDataset: str):
        """
        Setter for property: (str) EcadDatasetName
         Returns the ECAD dataset name.  
             
         
        """
        pass
    @property
    def EcadLocation(self) -> EcadImportBuilder.EcadLocationEnum:
        """
        Getter for property: ( EcadImportBuilder.EcadLocationEnum NXOpen.P) EcadLocation
         Returns the ECAD file location option.  
             
         
        """
        pass
    @EcadLocation.setter
    def EcadLocation(self, ecadLocation: EcadImportBuilder.EcadLocationEnum):
        """
        Setter for property: ( EcadImportBuilder.EcadLocationEnum NXOpen.P) EcadLocation
         Returns the ECAD file location option.  
             
         
        """
        pass
    @property
    def EcadNumber(self) -> str:
        """
        Getter for property: (str) EcadNumber
         Returns the ECAD number.  
             
         
        """
        pass
    @EcadNumber.setter
    def EcadNumber(self, ecadNumber: str):
        """
        Setter for property: (str) EcadNumber
         Returns the ECAD number.  
             
         
        """
        pass
    @property
    def EcadRevision(self) -> str:
        """
        Getter for property: (str) EcadRevision
         Returns the ECAD revision.  
             
         
        """
        pass
    @EcadRevision.setter
    def EcadRevision(self, ecadRevision: str):
        """
        Setter for property: (str) EcadRevision
         Returns the ECAD revision.  
             
         
        """
        pass
    @property
    def ImportOption(self) -> EcadImportBuilder.ImportOptionEnum:
        """
        Getter for property: ( EcadImportBuilder.ImportOptionEnum NXOpen.P) ImportOption
         Returns the import option.  
             
         
        """
        pass
    @ImportOption.setter
    def ImportOption(self, importOption: EcadImportBuilder.ImportOptionEnum):
        """
        Setter for property: ( EcadImportBuilder.ImportOptionEnum NXOpen.P) ImportOption
         Returns the import option.  
             
         
        """
        pass
    @property
    def IsOdbFolder(self) -> bool:
        """
        Getter for property: (bool) IsOdbFolder
         Returns the flag indicating whether the input is from an ODB folder.  
             
         
        """
        pass
    @IsOdbFolder.setter
    def IsOdbFolder(self, isOdbFolder: bool):
        """
        Setter for property: (bool) IsOdbFolder
         Returns the flag indicating whether the input is from an ODB folder.  
             
         
        """
        pass
    @property
    def LibraryFile(self) -> str:
        """
        Getter for property: (str) LibraryFile
         Returns the library file.  
             
         
        """
        pass
    @LibraryFile.setter
    def LibraryFile(self, libraryFile: str):
        """
        Setter for property: (str) LibraryFile
         Returns the library file.  
             
         
        """
        pass
    @property
    def OnlyUseExistingComponents(self) -> bool:
        """
        Getter for property: (bool) OnlyUseExistingComponents
         Returns the flag indicating whether to only use existing components.  
             
         
        """
        pass
    @OnlyUseExistingComponents.setter
    def OnlyUseExistingComponents(self, onlyUseExistingComp: bool):
        """
        Setter for property: (bool) OnlyUseExistingComponents
         Returns the flag indicating whether to only use existing components.  
             
         
        """
        pass
    @property
    def OutputPart(self) -> str:
        """
        Getter for property: (str) OutputPart
         Returns the output part.  
             
         
        """
        pass
    @OutputPart.setter
    def OutputPart(self, outputPart: str):
        """
        Setter for property: (str) OutputPart
         Returns the output part.  
             
         
        """
        pass
    @property
    def OverrideBoardThickness(self) -> bool:
        """
        Getter for property: (bool) OverrideBoardThickness
         Returns the flag indicating whether to override the board thickness.  
             
         
        """
        pass
    @OverrideBoardThickness.setter
    def OverrideBoardThickness(self, overrideBoardThickness: bool):
        """
        Setter for property: (bool) OverrideBoardThickness
         Returns the flag indicating whether to override the board thickness.  
             
         
        """
        pass
    @property
    def PartName(self) -> str:
        """
        Getter for property: (str) PartName
         Returns the part name.  
             
         
        """
        pass
    @PartName.setter
    def PartName(self, partName: str):
        """
        Setter for property: (str) PartName
         Returns the part name.  
             
         
        """
        pass
    @property
    def PartNumber(self) -> str:
        """
        Getter for property: (str) PartNumber
         Returns the part number.  
             
         
        """
        pass
    @PartNumber.setter
    def PartNumber(self, partNumber: str):
        """
        Setter for property: (str) PartNumber
         Returns the part number.  
             
         
        """
        pass
    @property
    def PartRevision(self) -> str:
        """
        Getter for property: (str) PartRevision
         Returns the part revision.  
             
         
        """
        pass
    @PartRevision.setter
    def PartRevision(self, partRevision: str):
        """
        Setter for property: (str) PartRevision
         Returns the part revision.  
             
         
        """
        pass
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @property
    def UseCurrentWorkPart(self) -> bool:
        """
        Getter for property: (bool) UseCurrentWorkPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    @UseCurrentWorkPart.setter
    def UseCurrentWorkPart(self, useCurrentWorkPart: bool):
        """
        Setter for property: (bool) UseCurrentWorkPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    @property
    def UseEntityFilter(self) -> bool:
        """
        Getter for property: (bool) UseEntityFilter
         Returns the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    @UseEntityFilter.setter
    def UseEntityFilter(self, useEntityFilter: bool):
        """
        Setter for property: (bool) UseEntityFilter
         Returns the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    def GetEntityFilter(self) -> EntityFilter:
        """
         Gets the entity filter. 
         Returns filter ( EntityFilter NXOpen.P): .
        """
        pass
    def SetEntityFilter(self, filter: EntityFilter) -> None:
        """
         Sets the entity filter. 
        """
        pass
import NXOpen
class EcadPanelImportBuilder(NXOpen.Builder): 
    """ Represents a builder to import ECAD panel. """
    class OptimizationMethodOptions(Enum):
        """
        Members Include: 
         |NotSet| 
         |Pattern| 

        """
        NotSet: int
        Pattern: int
        @staticmethod
        def ValueOf(value: int) -> EcadPanelImportBuilder.OptimizationMethodOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PanelLocationEnum(Enum):
        """
        Members Include: 
         |Os| 
         |Tc| 

        """
        Os: int
        Tc: int
        @staticmethod
        def ValueOf(value: int) -> EcadPanelImportBuilder.PanelLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThievingOptions(Enum):
        """
        Members Include: 
         |NotSet| 
         |Curve| 
         |SolidBody| 

        """
        NotSet: int
        Curve: int
        SolidBody: int
        @staticmethod
        def ValueOf(value: int) -> EcadPanelImportBuilder.ThievingOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Breakaway(self) -> bool:
        """
        Getter for property: (bool) Breakaway
         Returns the flag indicating whether to create breakaway.  
             
         
        """
        pass
    @Breakaway.setter
    def Breakaway(self, breakaway: bool):
        """
        Setter for property: (bool) Breakaway
         Returns the flag indicating whether to create breakaway.  
             
         
        """
        pass
    @property
    def IsPanelFolder(self) -> bool:
        """
        Getter for property: (bool) IsPanelFolder
         Returns the flag indicating whether the input is from a panel folder.  
             
         
        """
        pass
    @IsPanelFolder.setter
    def IsPanelFolder(self, isPanelFolder: bool):
        """
        Setter for property: (bool) IsPanelFolder
         Returns the flag indicating whether the input is from a panel folder.  
             
         
        """
        pass
    @property
    def OptimizationMethod(self) -> EcadPanelImportBuilder.OptimizationMethodOptions:
        """
        Getter for property: ( EcadPanelImportBuilder.OptimizationMethodOptions NXOpen.P) OptimizationMethod
         Returns the optimization method option.  
             
         
        """
        pass
    @OptimizationMethod.setter
    def OptimizationMethod(self, optimizationMethod: EcadPanelImportBuilder.OptimizationMethodOptions):
        """
        Setter for property: ( EcadPanelImportBuilder.OptimizationMethodOptions NXOpen.P) OptimizationMethod
         Returns the optimization method option.  
             
         
        """
        pass
    @property
    def PanelFile(self) -> str:
        """
        Getter for property: (str) PanelFile
         Returns the panel file.  
             
         
        """
        pass
    @PanelFile.setter
    def PanelFile(self, panelFile: str):
        """
        Setter for property: (str) PanelFile
         Returns the panel file.  
             
         
        """
        pass
    @property
    def PanelFolder(self) -> str:
        """
        Getter for property: (str) PanelFolder
         Returns the panel folder.  
             
         
        """
        pass
    @PanelFolder.setter
    def PanelFolder(self, panelFolder: str):
        """
        Setter for property: (str) PanelFolder
         Returns the panel folder.  
             
         
        """
        pass
    @property
    def PanelLocation(self) -> EcadPanelImportBuilder.PanelLocationEnum:
        """
        Getter for property: ( EcadPanelImportBuilder.PanelLocationEnum NXOpen.P) PanelLocation
         Returns the ECAD Panel file location option.  
             
         
        """
        pass
    @PanelLocation.setter
    def PanelLocation(self, panelLocation: EcadPanelImportBuilder.PanelLocationEnum):
        """
        Setter for property: ( EcadPanelImportBuilder.PanelLocationEnum NXOpen.P) PanelLocation
         Returns the ECAD Panel file location option.  
             
         
        """
        pass
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @property
    def SolderMasks(self) -> bool:
        """
        Getter for property: (bool) SolderMasks
         Returns the flag indicating whether to create solder masks.  
             
         
        """
        pass
    @SolderMasks.setter
    def SolderMasks(self, solderMasks: bool):
        """
        Setter for property: (bool) SolderMasks
         Returns the flag indicating whether to create solder masks.  
             
         
        """
        pass
    @property
    def TcItemNumber(self) -> str:
        """
        Getter for property: (str) TcItemNumber
         Returns the ECAD number.  
             
         
        """
        pass
    @TcItemNumber.setter
    def TcItemNumber(self, tcItemNumber: str):
        """
        Setter for property: (str) TcItemNumber
         Returns the ECAD number.  
             
         
        """
        pass
    @property
    def TcItemRevision(self) -> str:
        """
        Getter for property: (str) TcItemRevision
         Returns the ECAD revision.  
             
         
        """
        pass
    @TcItemRevision.setter
    def TcItemRevision(self, tcItemRevision: str):
        """
        Setter for property: (str) TcItemRevision
         Returns the ECAD revision.  
             
         
        """
        pass
    @property
    def Thieving(self) -> EcadPanelImportBuilder.ThievingOptions:
        """
        Getter for property: ( EcadPanelImportBuilder.ThievingOptions NXOpen.P) Thieving
         Returns the thieving creation option.  
             
         
        """
        pass
    @Thieving.setter
    def Thieving(self, thieving: EcadPanelImportBuilder.ThievingOptions):
        """
        Setter for property: ( EcadPanelImportBuilder.ThievingOptions NXOpen.P) Thieving
         Returns the thieving creation option.  
             
         
        """
        pass
    @property
    def UseCurrentWorkPart(self) -> bool:
        """
        Getter for property: (bool) UseCurrentWorkPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    @UseCurrentWorkPart.setter
    def UseCurrentWorkPart(self, useCurrentWorkPart: bool):
        """
        Setter for property: (bool) UseCurrentWorkPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    @property
    def UseEntityFilter(self) -> bool:
        """
        Getter for property: (bool) UseEntityFilter
         Returns the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    @UseEntityFilter.setter
    def UseEntityFilter(self, useEntityFilter: bool):
        """
        Setter for property: (bool) UseEntityFilter
         Returns the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    def GetEntityFilter(self) -> EntityFilter:
        """
         Gets the entity filter. 
         Returns filter ( EntityFilter NXOpen.P): .
        """
        pass
    def GetOutputNames(self) -> List[str]:
        """
         Gets the output names. 
         Returns outputsNames (List[str]):  Outputs names list .
        """
        pass
    def GetOutputParts(self) -> List[str]:
        """
         Gets the output parts. 
         Returns outputsParts (List[str]):  Outputs parts list .
        """
        pass
    def PrepareOdbFolder(self) -> str:
        """
         Create temporary folder of ODB Panel data from TGZ-file, in managed mode it it is required import data from Item Revision. 
         Returns folderName (str): .
        """
        pass
    def SetEntityFilter(self, filter: EntityFilter) -> None:
        """
         Sets the entity filter. 
        """
        pass
    def SetOutputNames(self, outputsNames: List[str]) -> None:
        """
         Sets the output names. 
        """
        pass
    def SetOutputParts(self, outputsParts: List[str]) -> None:
        """
         Sets the output parts. 
        """
        pass
class EntityCategory(Enum):
    """
    Members Include: 
     |Component|  Entity is a Component. 
     |Board|  Entity is a Board. 
     |Mechanical|  Entity is Mechanical. 
     |KeepOut|  Entity is a Keep-out Area. 
     |Copper|  Entity is Copper. 
     |WireBond|  Entity is WireBond. 
     |CopperArea|  Entity is a Copper Area. 

    """
    Component: int
    Board: int
    Mechanical: int
    KeepOut: int
    Copper: int
    WireBond: int
    CopperArea: int
    @staticmethod
    def ValueOf(value: int) -> EntityCategory:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class EntityFilterBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit NXOpen.PcbExchange.EntityFilter. """
    class LengthUnitsEnum(Enum):
        """
        Members Include: 
         |Millimeters| 
         |Inches| 

        """
        Millimeters: int
        Inches: int
        @staticmethod
        def ValueOf(value: int) -> EntityFilterBuilder.LengthUnitsEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ComponentMaxHeight(self) -> float:
        """
        Getter for property: (float) ComponentMaxHeight
         Returns the maximum component height.  
             
         
        """
        pass
    @ComponentMaxHeight.setter
    def ComponentMaxHeight(self, componentMaxHeight: float):
        """
        Setter for property: (float) ComponentMaxHeight
         Returns the maximum component height.  
             
         
        """
        pass
    @property
    def ComponentMaxSize(self) -> float:
        """
        Getter for property: (float) ComponentMaxSize
         Returns the maximum component size.  
             
         
        """
        pass
    @ComponentMaxSize.setter
    def ComponentMaxSize(self, componentMaxSize: float):
        """
        Setter for property: (float) ComponentMaxSize
         Returns the maximum component size.  
             
         
        """
        pass
    @property
    def ComponentMinHeight(self) -> float:
        """
        Getter for property: (float) ComponentMinHeight
         Returns the minimum component height.  
             
         
        """
        pass
    @ComponentMinHeight.setter
    def ComponentMinHeight(self, componentMinHeight: float):
        """
        Setter for property: (float) ComponentMinHeight
         Returns the minimum component height.  
             
         
        """
        pass
    @property
    def ComponentMinSize(self) -> float:
        """
        Getter for property: (float) ComponentMinSize
         Returns the minimum component size.  
             
         
        """
        pass
    @ComponentMinSize.setter
    def ComponentMinSize(self, componentMinSize: float):
        """
        Setter for property: (float) ComponentMinSize
         Returns the minimum component size.  
             
         
        """
        pass
    @property
    def HoleMaxDiameter(self) -> float:
        """
        Getter for property: (float) HoleMaxDiameter
         Returns the maximum hole diameter.  
             
         
        """
        pass
    @HoleMaxDiameter.setter
    def HoleMaxDiameter(self, holeMaxDiameter: float):
        """
        Setter for property: (float) HoleMaxDiameter
         Returns the maximum hole diameter.  
             
         
        """
        pass
    @property
    def HoleMaxSize(self) -> float:
        """
        Getter for property: (float) HoleMaxSize
         Returns the maximum hole size.  
             
         
        """
        pass
    @HoleMaxSize.setter
    def HoleMaxSize(self, holeMaxSize: float):
        """
        Setter for property: (float) HoleMaxSize
         Returns the maximum hole size.  
             
         
        """
        pass
    @property
    def HoleMinDiameter(self) -> float:
        """
        Getter for property: (float) HoleMinDiameter
         Returns the minimum hole diameter.  
             
         
        """
        pass
    @HoleMinDiameter.setter
    def HoleMinDiameter(self, holeMinDiameter: float):
        """
        Setter for property: (float) HoleMinDiameter
         Returns the minimum hole diameter.  
             
         
        """
        pass
    @property
    def HoleMinSize(self) -> float:
        """
        Getter for property: (float) HoleMinSize
         Returns the minimum hole size.  
             
         
        """
        pass
    @HoleMinSize.setter
    def HoleMinSize(self, holeMinSize: float):
        """
        Setter for property: (float) HoleMinSize
         Returns the minimum hole size.  
             
         
        """
        pass
    @property
    def LengthUnits(self) -> EntityFilterBuilder.LengthUnitsEnum:
        """
        Getter for property: ( EntityFilterBuilder.LengthUnitsEnum NXOpen.P) LengthUnits
         Returns the length units.  
             
         
        """
        pass
    @LengthUnits.setter
    def LengthUnits(self, lengthUnits: EntityFilterBuilder.LengthUnitsEnum):
        """
        Setter for property: ( EntityFilterBuilder.LengthUnitsEnum NXOpen.P) LengthUnits
         Returns the length units.  
             
         
        """
        pass
    @property
    def RemoveBlindBuriedViaHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveBlindBuriedViaHoles
         Returns the flag indicating whether to remove blind buried via holes.  
             
         
        """
        pass
    @RemoveBlindBuriedViaHoles.setter
    def RemoveBlindBuriedViaHoles(self, removeBlindBuriedViaHoles: bool):
        """
        Setter for property: (bool) RemoveBlindBuriedViaHoles
         Returns the flag indicating whether to remove blind buried via holes.  
             
         
        """
        pass
    @property
    def RemoveComponentsWithHeight(self) -> bool:
        """
        Getter for property: (bool) RemoveComponentsWithHeight
         Returns the flag indicating whether to remove components with a specified height.  
             
         
        """
        pass
    @RemoveComponentsWithHeight.setter
    def RemoveComponentsWithHeight(self, removeComponentsWithHeight: bool):
        """
        Setter for property: (bool) RemoveComponentsWithHeight
         Returns the flag indicating whether to remove components with a specified height.  
             
         
        """
        pass
    @property
    def RemoveComponentsWithSize(self) -> bool:
        """
        Getter for property: (bool) RemoveComponentsWithSize
         Returns the flag indicating whether to remove components with a specified size.  
             
         
        """
        pass
    @RemoveComponentsWithSize.setter
    def RemoveComponentsWithSize(self, removeComponentsWithSize: bool):
        """
        Setter for property: (bool) RemoveComponentsWithSize
         Returns the flag indicating whether to remove components with a specified size.  
             
         
        """
        pass
    @property
    def RemoveEcadComponents(self) -> bool:
        """
        Getter for property: (bool) RemoveEcadComponents
         Returns the flag indicating whether to remove ECAD components.  
             
         
        """
        pass
    @RemoveEcadComponents.setter
    def RemoveEcadComponents(self, removeEcadComponents: bool):
        """
        Setter for property: (bool) RemoveEcadComponents
         Returns the flag indicating whether to remove ECAD components.  
             
         
        """
        pass
    @property
    def RemoveHolesWithDiameter(self) -> bool:
        """
        Getter for property: (bool) RemoveHolesWithDiameter
         Returns the flag indicating whether to remove holes with a specified diameter.  
             
         
        """
        pass
    @RemoveHolesWithDiameter.setter
    def RemoveHolesWithDiameter(self, removeHolesWithDiameter: bool):
        """
        Setter for property: (bool) RemoveHolesWithDiameter
         Returns the flag indicating whether to remove holes with a specified diameter.  
             
         
        """
        pass
    @property
    def RemoveHolesWithSize(self) -> bool:
        """
        Getter for property: (bool) RemoveHolesWithSize
         Returns the flag indicating whether to remove holes with a specified size.  
             
         
        """
        pass
    @RemoveHolesWithSize.setter
    def RemoveHolesWithSize(self, removeHolesWithSize: bool):
        """
        Setter for property: (bool) RemoveHolesWithSize
         Returns the flag indicating whether to remove holes with a specified size.  
             
         
        """
        pass
    @property
    def RemoveMcadComponents(self) -> bool:
        """
        Getter for property: (bool) RemoveMcadComponents
         Returns the flag indicating whether to remove MCAD components.  
             
         
        """
        pass
    @RemoveMcadComponents.setter
    def RemoveMcadComponents(self, removeMcadComponents: bool):
        """
        Setter for property: (bool) RemoveMcadComponents
         Returns the flag indicating whether to remove MCAD components.  
             
         
        """
        pass
    @property
    def RemoveMountingHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveMountingHoles
         Returns the flag indicating whether to remove mounting holes.  
             
         
        """
        pass
    @RemoveMountingHoles.setter
    def RemoveMountingHoles(self, removeMountingHoles: bool):
        """
        Setter for property: (bool) RemoveMountingHoles
         Returns the flag indicating whether to remove mounting holes.  
             
         
        """
        pass
    @property
    def RemoveOtherHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveOtherHoles
         Returns the flag indicating whether to remove other holes.  
             
         
        """
        pass
    @RemoveOtherHoles.setter
    def RemoveOtherHoles(self, removeOtherHoles: bool):
        """
        Setter for property: (bool) RemoveOtherHoles
         Returns the flag indicating whether to remove other holes.  
             
         
        """
        pass
    @property
    def RemoveOtherKeepoutAreas(self) -> bool:
        """
        Getter for property: (bool) RemoveOtherKeepoutAreas
         Returns the flag indicating whether to remove other keepout areas.  
             
         
        """
        pass
    @RemoveOtherKeepoutAreas.setter
    def RemoveOtherKeepoutAreas(self, removeOtherKeepoutAreas: bool):
        """
        Setter for property: (bool) RemoveOtherKeepoutAreas
         Returns the flag indicating whether to remove other keepout areas.  
             
         
        """
        pass
    @property
    def RemovePadsByPadstacks(self) -> str:
        """
        Getter for property: (str) RemovePadsByPadstacks
         Returns the string indicating the padstacks, separated by commas, of the pads to remove.  
             
         
        """
        pass
    @RemovePadsByPadstacks.setter
    def RemovePadsByPadstacks(self, removePadsByPadstacks: str):
        """
        Setter for property: (str) RemovePadsByPadstacks
         Returns the string indicating the padstacks, separated by commas, of the pads to remove.  
             
         
        """
        pass
    @property
    def RemovePinHoles(self) -> bool:
        """
        Getter for property: (bool) RemovePinHoles
         Returns the flag indicating whether to remove pin holes.  
             
         
        """
        pass
    @RemovePinHoles.setter
    def RemovePinHoles(self, removePinHoles: bool):
        """
        Setter for property: (bool) RemovePinHoles
         Returns the flag indicating whether to remove pin holes.  
             
         
        """
        pass
    @property
    def RemovePlacedComponents(self) -> bool:
        """
        Getter for property: (bool) RemovePlacedComponents
         Returns the flag indicating whether to remove placed components.  
             
         
        """
        pass
    @RemovePlacedComponents.setter
    def RemovePlacedComponents(self, removePlacedComponents: bool):
        """
        Setter for property: (bool) RemovePlacedComponents
         Returns the flag indicating whether to remove placed components.  
             
         
        """
        pass
    @property
    def RemovePlacementGroupKeepinAreas(self) -> bool:
        """
        Getter for property: (bool) RemovePlacementGroupKeepinAreas
         Returns the flag indicating whether to remove placement group keepin areas.  
             
         
        """
        pass
    @RemovePlacementGroupKeepinAreas.setter
    def RemovePlacementGroupKeepinAreas(self, removePlacementGroupKeepinAreas: bool):
        """
        Setter for property: (bool) RemovePlacementGroupKeepinAreas
         Returns the flag indicating whether to remove placement group keepin areas.  
             
         
        """
        pass
    @property
    def RemovePlacementKeepinAreas(self) -> bool:
        """
        Getter for property: (bool) RemovePlacementKeepinAreas
         Returns the flag indicating whether to remove placement keepin areas.  
             
         
        """
        pass
    @RemovePlacementKeepinAreas.setter
    def RemovePlacementKeepinAreas(self, removePlacementKeepinAreas: bool):
        """
        Setter for property: (bool) RemovePlacementKeepinAreas
         Returns the flag indicating whether to remove placement keepin areas.  
             
         
        """
        pass
    @property
    def RemovePlacementKeepoutAreas(self) -> bool:
        """
        Getter for property: (bool) RemovePlacementKeepoutAreas
         Returns the flag indicating whether to remove placement keepout areas.  
             
         
        """
        pass
    @RemovePlacementKeepoutAreas.setter
    def RemovePlacementKeepoutAreas(self, removePlacementKeepoutAreas: bool):
        """
        Setter for property: (bool) RemovePlacementKeepoutAreas
         Returns the flag indicating whether to remove placement keepout areas.  
             
         
        """
        pass
    @property
    def RemoveRoutingKeepinAreas(self) -> bool:
        """
        Getter for property: (bool) RemoveRoutingKeepinAreas
         Returns the flag indicating whether to remove routing keepin areas.  
             
         
        """
        pass
    @RemoveRoutingKeepinAreas.setter
    def RemoveRoutingKeepinAreas(self, removeRoutingKeepinAreas: bool):
        """
        Setter for property: (bool) RemoveRoutingKeepinAreas
         Returns the flag indicating whether to remove routing keepin areas.  
             
         
        """
        pass
    @property
    def RemoveRoutingKeepoutAreas(self) -> bool:
        """
        Getter for property: (bool) RemoveRoutingKeepoutAreas
         Returns the flag indicating whether to remove routing keepout areas.  
             
         
        """
        pass
    @RemoveRoutingKeepoutAreas.setter
    def RemoveRoutingKeepoutAreas(self, removeRoutingKeepoutAreas: bool):
        """
        Setter for property: (bool) RemoveRoutingKeepoutAreas
         Returns the flag indicating whether to remove routing keepout areas.  
             
         
        """
        pass
    @property
    def RemoveToolingHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveToolingHoles
         Returns the flag indicating whether to remove tooling holes.  
             
         
        """
        pass
    @RemoveToolingHoles.setter
    def RemoveToolingHoles(self, removeToolingHoles: bool):
        """
        Setter for property: (bool) RemoveToolingHoles
         Returns the flag indicating whether to remove tooling holes.  
             
         
        """
        pass
    @property
    def RemoveTracesAndPadsByNetNames(self) -> str:
        """
        Getter for property: (str) RemoveTracesAndPadsByNetNames
         Returns the string indicating the net names, separated by commas, of the traces and pads to remove.  
             
         
        """
        pass
    @RemoveTracesAndPadsByNetNames.setter
    def RemoveTracesAndPadsByNetNames(self, removeTracesAndPadsByNetNames: str):
        """
        Setter for property: (str) RemoveTracesAndPadsByNetNames
         Returns the string indicating the net names, separated by commas, of the traces and pads to remove.  
             
         
        """
        pass
    @property
    def RemoveUnconnectedPads(self) -> bool:
        """
        Getter for property: (bool) RemoveUnconnectedPads
         Returns the flag indicating whether to remove pads that are not connected to any components.  
             
         
        """
        pass
    @RemoveUnconnectedPads.setter
    def RemoveUnconnectedPads(self, removeUnconnectedPads: bool):
        """
        Setter for property: (bool) RemoveUnconnectedPads
         Returns the flag indicating whether to remove pads that are not connected to any components.  
             
         
        """
        pass
    @property
    def RemoveUnplacedComponents(self) -> bool:
        """
        Getter for property: (bool) RemoveUnplacedComponents
         Returns the flag indicating whether to remove unplaced components.  
             
         
        """
        pass
    @RemoveUnplacedComponents.setter
    def RemoveUnplacedComponents(self, removeUnplacedComponents: bool):
        """
        Setter for property: (bool) RemoveUnplacedComponents
         Returns the flag indicating whether to remove unplaced components.  
             
         
        """
        pass
    @property
    def RemoveViaHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveViaHoles
         Returns the flag indicating whether to remove via holes.  
             
         
        """
        pass
    @RemoveViaHoles.setter
    def RemoveViaHoles(self, removeViaHoles: bool):
        """
        Setter for property: (bool) RemoveViaHoles
         Returns the flag indicating whether to remove via holes.  
             
         
        """
        pass
    @property
    def RemoveViaKeepoutAreas(self) -> bool:
        """
        Getter for property: (bool) RemoveViaKeepoutAreas
         Returns the flag indicating whether to remove via keepout areas.  
             
         
        """
        pass
    @RemoveViaKeepoutAreas.setter
    def RemoveViaKeepoutAreas(self, removeViaKeepoutAreas: bool):
        """
        Setter for property: (bool) RemoveViaKeepoutAreas
         Returns the flag indicating whether to remove via keepout areas.  
             
         
        """
        pass
    def SetUserDefiniedFilters(self, filters: List[str]) -> None:
        """
         Sets user-defined filters. 
        """
        pass
import NXOpen
class EntityFilter(NXOpen.NXObject): 
    """ Represents a entity filter for PCB exchange. """
    pass
import NXOpen
class ExtdataUpdator(NXOpen.Object): 
    """ Represents a builder to read the external data and update the model. """
    def Read(fName: str) -> Tuple[List[str], List[str]]:
        """
         Reads the external data. 
         Returns A tuple consisting of (netNames, layerNames). 
         - netNames is: List[str].
         - layerNames is: List[str].

        """
        pass
    def Update(fName: str, layerNames: List[str], netNames: List[str], bTextualFilter: bool, textualFilterStr: str) -> None:
        """
         Updates the external data. 
        """
        pass
import NXOpen
class ExternalDataImportBuilder(NXOpen.Builder): 
    """ Represents a builder to import external ECAD entities. """
    class JaPcbExternalDataImportBuilderImportoption(Enum):
        """
        Members Include: 
         |Import|  Import. 
         |DoNotImport|  Do not import. 

        """
        Import: int
        DoNotImport: int
        @staticmethod
        def ValueOf(value: int) -> ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Filename(self) -> str:
        """
        Getter for property: (str) Filename
         Returns the ECAD filename to import.  
             
         
        """
        pass
    @Filename.setter
    def Filename(self, filename: str):
        """
        Setter for property: (str) Filename
         Returns the ECAD filename to import.  
             
         
        """
        pass
    @property
    def NetsFilterString(self) -> str:
        """
        Getter for property: (str) NetsFilterString
         Returns the comma-separated list of values for filtering nets.  
             
         
        """
        pass
    @NetsFilterString.setter
    def NetsFilterString(self, filter: str):
        """
        Setter for property: (str) NetsFilterString
         Returns the comma-separated list of values for filtering nets.  
             
         
        """
        pass
    @property
    def NetsFilterStringEnabled(self) -> bool:
        """
        Getter for property: (bool) NetsFilterStringEnabled
         Returns the flag indicating whether the filter string for nets is enabled.  
             
         
        """
        pass
    @NetsFilterStringEnabled.setter
    def NetsFilterStringEnabled(self, enabled: bool):
        """
        Setter for property: (bool) NetsFilterStringEnabled
         Returns the flag indicating whether the filter string for nets is enabled.  
             
         
        """
        pass
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    def GetLayerImported(self, name: str) -> ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption:
        """
         Returns whether the layer should be imported. 
         Returns importOption ( ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption NXOpen.P):  Import option. .
        """
        pass
    def GetLayerNames(self) -> List[str]:
        """
         Returns the layer names. 
         Returns names (List[str]):  Layer names. .
        """
        pass
    def GetNetImported(self, name: str) -> ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption:
        """
         Returns whether the net should be imported. 
         Returns importOption ( ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption NXOpen.P):  Import option. .
        """
        pass
    def GetNetNames(self) -> List[str]:
        """
         Returns the net names. 
         Returns names (List[str]):  Net names. .
        """
        pass
    def GetPadstackImported(self, name: str) -> ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption:
        """
         Returns whether the padstack should be imported. 
         Returns importOption ( ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption NXOpen.P):  Import option. .
        """
        pass
    def GetPadstackNames(self) -> List[str]:
        """
         Returns the padstack names. 
         Returns names (List[str]):  Padstack names. .
        """
        pass
    def GetPadstackPart(self, name: str) -> str:
        """
         Returns the part used to model pads in the padstack. 
         Returns part (str):  Part file. .
        """
        pass
    def QueryEntities(self) -> None:
        """
         Queries the list of external entities available from the ECAD file. 
        """
        pass
    def SetAllLayersImported(self, importOption: ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption) -> None:
        """
         Sets whether all layers should be imported. 
        """
        pass
    def SetLayerImported(self, name: str, importOption: ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption) -> None:
        """
         Sets whether the layer should be imported. 
        """
        pass
    def SetNetImported(self, name: str, importOption: ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption) -> None:
        """
         Sets whether the net should be imported. 
        """
        pass
    def SetPadstackImported(self, name: str, importOption: ExternalDataImportBuilder.JaPcbExternalDataImportBuilderImportoption) -> None:
        """
         Sets whether the padstack should be imported. 
        """
        pass
    def SetPadstackPart(self, name: str, part: str) -> None:
        """
         Sets the part used to model pads in the padstack. 
        """
        pass
import NXOpen
import NXOpen.Features
class HoleAttributesBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit hole attributes. """
    class AssociatedPartEnum(Enum):
        """
        Members Include: 
         |Board| 
         |Norefdes| 
         |Specify| 

        """
        Board: int
        Norefdes: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> HoleAttributesBuilder.AssociatedPartEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OwnerEnum(Enum):
        """
        Members Include: 
         |Mcad| 
         |Ecad| 
         |Unowned| 

        """
        Mcad: int
        Ecad: int
        Unowned: int
        @staticmethod
        def ValueOf(value: int) -> HoleAttributesBuilder.OwnerEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlatingStyleEnum(Enum):
        """
        Members Include: 
         |PlatedThru| 
         |NonPlatedThru| 

        """
        PlatedThru: int
        NonPlatedThru: int
        @staticmethod
        def ValueOf(value: int) -> HoleAttributesBuilder.PlatingStyleEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeEnum(Enum):
        """
        Members Include: 
         |Pin| 
         |Via| 
         |Mounting| 
         |Tool| 
         |Other| 

        """
        Pin: int
        Via: int
        Mounting: int
        Tool: int
        Other: int
        @staticmethod
        def ValueOf(value: int) -> HoleAttributesBuilder.TypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssociatedPart(self) -> HoleAttributesBuilder.AssociatedPartEnum:
        """
        Getter for property: ( HoleAttributesBuilder.AssociatedPartEnum NXOpen.P) AssociatedPart
         Returns the hole associated part   
            
         
        """
        pass
    @AssociatedPart.setter
    def AssociatedPart(self, associatedPart: HoleAttributesBuilder.AssociatedPartEnum):
        """
        Setter for property: ( HoleAttributesBuilder.AssociatedPartEnum NXOpen.P) AssociatedPart
         Returns the hole associated part   
            
         
        """
        pass
    @property
    def Features(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) Features
         Returns the feature   
            
         
        """
        pass
    @property
    def HoleType(self) -> HoleAttributesBuilder.TypeEnum:
        """
        Getter for property: ( HoleAttributesBuilder.TypeEnum NXOpen.P) HoleType
         Returns the hole type   
            
         
        """
        pass
    @HoleType.setter
    def HoleType(self, type: HoleAttributesBuilder.TypeEnum):
        """
        Setter for property: ( HoleAttributesBuilder.TypeEnum NXOpen.P) HoleType
         Returns the hole type   
            
         
        """
        pass
    @property
    def Owner(self) -> HoleAttributesBuilder.OwnerEnum:
        """
        Getter for property: ( HoleAttributesBuilder.OwnerEnum NXOpen.P) Owner
         Returns the hole owner   
            
         
        """
        pass
    @Owner.setter
    def Owner(self, owner: HoleAttributesBuilder.OwnerEnum):
        """
        Setter for property: ( HoleAttributesBuilder.OwnerEnum NXOpen.P) Owner
         Returns the hole owner   
            
         
        """
        pass
    @property
    def PlatingStyle(self) -> HoleAttributesBuilder.PlatingStyleEnum:
        """
        Getter for property: ( HoleAttributesBuilder.PlatingStyleEnum NXOpen.P) PlatingStyle
         Returns the hole plating style   
            
         
        """
        pass
    @PlatingStyle.setter
    def PlatingStyle(self, platingStyle: HoleAttributesBuilder.PlatingStyleEnum):
        """
        Setter for property: ( HoleAttributesBuilder.PlatingStyleEnum NXOpen.P) PlatingStyle
         Returns the hole plating style   
            
         
        """
        pass
    @property
    def SpecifiedPart(self) -> str:
        """
        Getter for property: (str) SpecifiedPart
         Returns the hole specified part   
            
         
        """
        pass
    @SpecifiedPart.setter
    def SpecifiedPart(self, specifiedPart: str):
        """
        Setter for property: (str) SpecifiedPart
         Returns the hole specified part   
            
         
        """
        pass
import NXOpen
class IdxCompareBuilder(NXOpen.Builder): 
    """ Represents a builder to compare two IDX files. """
    class SourceTypeEnum(Enum):
        """
        Members Include: 
         |Nx| 
         |Idx| 

        """
        Nx: int
        Idx: int
        @staticmethod
        def ValueOf(value: int) -> IdxCompareBuilder.SourceTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SourceFile(self) -> str:
        """
        Getter for property: (str) SourceFile
         Returns the source file.  
             
         
        """
        pass
    @SourceFile.setter
    def SourceFile(self, sourceFile: str):
        """
        Setter for property: (str) SourceFile
         Returns the source file.  
             
         
        """
        pass
    @property
    def SourceType(self) -> IdxCompareBuilder.SourceTypeEnum:
        """
        Getter for property: ( IdxCompareBuilder.SourceTypeEnum NXOpen.P) SourceType
         Returns the source model option.  
             
         
        """
        pass
    @SourceType.setter
    def SourceType(self, sourceType: IdxCompareBuilder.SourceTypeEnum):
        """
        Setter for property: ( IdxCompareBuilder.SourceTypeEnum NXOpen.P) SourceType
         Returns the source model option.  
             
         
        """
        pass
    @property
    def TargetFile(self) -> str:
        """
        Getter for property: (str) TargetFile
         Returns the target file.  
             
         
        """
        pass
    @TargetFile.setter
    def TargetFile(self, targetFile: str):
        """
        Setter for property: (str) TargetFile
         Returns the target file.  
             
         
        """
        pass
import NXOpen
class IdxExportBuilder(NXOpen.Builder): 
    """ Represents a builder to export IDX file. """
    class ExportUnitsEnum(Enum):
        """
        Members Include: 
         |Mm| 
         |Thou| 

        """
        Mm: int
        Thou: int
        @staticmethod
        def ValueOf(value: int) -> IdxExportBuilder.ExportUnitsEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FileFormatEnum(Enum):
        """
        Members Include: 
         |Idx2| 
         |Idx3| 

        """
        Idx2: int
        Idx3: int
        @staticmethod
        def ValueOf(value: int) -> IdxExportBuilder.FileFormatEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IdxLocationEnum(Enum):
        """
        Members Include: 
         |Os| 
         |TeamcenterDS| 
         |TeamcenterCS| 

        """
        Os: int
        TeamcenterDS: int
        TeamcenterCS: int
        @staticmethod
        def ValueOf(value: int) -> IdxExportBuilder.IdxLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BaselineFile(self) -> str:
        """
        Getter for property: (str) BaselineFile
         Returns the baseline file.  
             
         
        """
        pass
    @BaselineFile.setter
    def BaselineFile(self, baselineFile: str):
        """
        Setter for property: (str) BaselineFile
         Returns the baseline file.  
             
         
        """
        pass
    @property
    def BaselineLocation(self) -> IdxExportBuilder.IdxLocationEnum:
        """
        Getter for property: ( IdxExportBuilder.IdxLocationEnum NXOpen.P) BaselineLocation
         Returns the baseline location.  
             
         
        """
        pass
    @BaselineLocation.setter
    def BaselineLocation(self, baselineLocation: IdxExportBuilder.IdxLocationEnum):
        """
        Setter for property: ( IdxExportBuilder.IdxLocationEnum NXOpen.P) BaselineLocation
         Returns the baseline location.  
             
         
        """
        pass
    @property
    def BaselineNumber(self) -> str:
        """
        Getter for property: (str) BaselineNumber
         Returns the baseline number.  
             
         
        """
        pass
    @BaselineNumber.setter
    def BaselineNumber(self, baselineNumber: str):
        """
        Setter for property: (str) BaselineNumber
         Returns the baseline number.  
             
         
        """
        pass
    @property
    def BaselineRevision(self) -> str:
        """
        Getter for property: (str) BaselineRevision
         Returns the baseline revision.  
             
         
        """
        pass
    @BaselineRevision.setter
    def BaselineRevision(self, baselineRevision: str):
        """
        Setter for property: (str) BaselineRevision
         Returns the baseline revision.  
             
         
        """
        pass
    @property
    def CloneAssembly(self) -> bool:
        """
        Getter for property: (bool) CloneAssembly
         Returns the flag indicating whether to clone the assembly.  
             
         
        """
        pass
    @CloneAssembly.setter
    def CloneAssembly(self, cloneAssembly: bool):
        """
        Setter for property: (bool) CloneAssembly
         Returns the flag indicating whether to clone the assembly.  
             
         
        """
        pass
    @property
    def FileFormat(self) -> IdxExportBuilder.FileFormatEnum:
        """
        Getter for property: ( IdxExportBuilder.FileFormatEnum NXOpen.P) FileFormat
         Returns the file format.  
             
         
        """
        pass
    @FileFormat.setter
    def FileFormat(self, fileFormat: IdxExportBuilder.FileFormatEnum):
        """
        Setter for property: ( IdxExportBuilder.FileFormatEnum NXOpen.P) FileFormat
         Returns the file format.  
             
         
        """
        pass
    @property
    def FileNote(self) -> str:
        """
        Getter for property: (str) FileNote
         Returns the file note.  
             
         
        """
        pass
    @FileNote.setter
    def FileNote(self, fileNote: str):
        """
        Setter for property: (str) FileNote
         Returns the file note.  
             
         
        """
        pass
    @property
    def FileUnits(self) -> IdxExportBuilder.ExportUnitsEnum:
        """
        Getter for property: ( IdxExportBuilder.ExportUnitsEnum NXOpen.P) FileUnits
         Returns the file units.  
             
         
        """
        pass
    @FileUnits.setter
    def FileUnits(self, exportUnits: IdxExportBuilder.ExportUnitsEnum):
        """
        Setter for property: ( IdxExportBuilder.ExportUnitsEnum NXOpen.P) FileUnits
         Returns the file units.  
             
         
        """
        pass
    @property
    def SelectedObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectedObjects
         Returns the selected objects.  
             
         
        """
        pass
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @property
    def TagModel(self) -> bool:
        """
        Getter for property: (bool) TagModel
         Returns the flag indicating whether to tag the model.  
             
         
        """
        pass
    @TagModel.setter
    def TagModel(self, tagModel: bool):
        """
        Setter for property: (bool) TagModel
         Returns the flag indicating whether to tag the model.  
             
         
        """
        pass
    @property
    def UseCloneSelection(self) -> bool:
        """
        Getter for property: (bool) UseCloneSelection
         Returns the flag indicating whether to clone only selected objects.  
             
         
        """
        pass
    @UseCloneSelection.setter
    def UseCloneSelection(self, canUseCloneSelection: bool):
        """
        Setter for property: (bool) UseCloneSelection
         Returns the flag indicating whether to clone only selected objects.  
             
         
        """
        pass
    @property
    def UseCurrentWorkPart(self) -> bool:
        """
        Getter for property: (bool) UseCurrentWorkPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    @UseCurrentWorkPart.setter
    def UseCurrentWorkPart(self, useCurrentWorkPart: bool):
        """
        Setter for property: (bool) UseCurrentWorkPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    def RunPreExportBaselineHook(self) -> None:
        """
         Runs the pre-export baseline hook and sets the baseline file, if defined. 
        """
        pass
import NXOpen
class IdxImportBuilder(NXOpen.Builder): 
    """ Represents a builder to import IDX file. """
    class DataLocation(Enum):
        """
        Members Include: 
         |Local| 
         |TeamcenterDS| 
         |TeamcenterCS| 

        """
        Local: int
        TeamcenterDS: int
        TeamcenterCS: int
        @staticmethod
        def ValueOf(value: int) -> IdxImportBuilder.DataLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssemblyName(self) -> str:
        """
        Getter for property: (str) AssemblyName
         Returns the assembly name.  
             
         
        """
        pass
    @AssemblyName.setter
    def AssemblyName(self, assemblyName: str):
        """
        Setter for property: (str) AssemblyName
         Returns the assembly name.  
             
         
        """
        pass
    @property
    def AssemblyNumber(self) -> str:
        """
        Getter for property: (str) AssemblyNumber
         Returns the assembly number.  
             
         
        """
        pass
    @AssemblyNumber.setter
    def AssemblyNumber(self, assemblyNumber: str):
        """
        Setter for property: (str) AssemblyNumber
         Returns the assembly number.  
             
         
        """
        pass
    @property
    def AssemblyRevision(self) -> str:
        """
        Getter for property: (str) AssemblyRevision
         Returns the assembly revision.  
             
         
        """
        pass
    @AssemblyRevision.setter
    def AssemblyRevision(self, assemblyRevision: str):
        """
        Setter for property: (str) AssemblyRevision
         Returns the assembly revision.  
             
         
        """
        pass
    @property
    def BaselineFile(self) -> str:
        """
        Getter for property: (str) BaselineFile
         Returns the baseline file.  
             
         
        """
        pass
    @BaselineFile.setter
    def BaselineFile(self, baselineFile: str):
        """
        Setter for property: (str) BaselineFile
         Returns the baseline file.  
             
         
        """
        pass
    @property
    def CollaborationDir(self) -> str:
        """
        Getter for property: (str) CollaborationDir
         Returns the collaboration directory.  
             
         
        """
        pass
    @CollaborationDir.setter
    def CollaborationDir(self, foldername: str):
        """
        Setter for property: (str) CollaborationDir
         Returns the collaboration directory.  
             
         
        """
        pass
    @property
    def IdxDataFrom(self) -> IdxImportBuilder.DataLocation:
        """
        Getter for property: ( IdxImportBuilder.DataLocation NXOpen.P) IdxDataFrom
         Returns the location of IDX data.  
             
         
        """
        pass
    @IdxDataFrom.setter
    def IdxDataFrom(self, idxDataFrom: IdxImportBuilder.DataLocation):
        """
        Setter for property: ( IdxImportBuilder.DataLocation NXOpen.P) IdxDataFrom
         Returns the location of IDX data.  
             
         
        """
        pass
    @property
    def IdxNumber(self) -> str:
        """
        Getter for property: (str) IdxNumber
         Returns the IDX number.  
             
         
        """
        pass
    @IdxNumber.setter
    def IdxNumber(self, idxNumber: str):
        """
        Setter for property: (str) IdxNumber
         Returns the IDX number.  
             
         
        """
        pass
    @property
    def IdxRevision(self) -> str:
        """
        Getter for property: (str) IdxRevision
         Returns the IDX revision.  
             
         
        """
        pass
    @IdxRevision.setter
    def IdxRevision(self, idxRevision: str):
        """
        Setter for property: (str) IdxRevision
         Returns the IDX revision.  
             
         
        """
        pass
    @property
    def OutputPartFile(self) -> str:
        """
        Getter for property: (str) OutputPartFile
         Returns the output part file.  
             
         
        """
        pass
    @OutputPartFile.setter
    def OutputPartFile(self, outputPartString: str):
        """
        Setter for property: (str) OutputPartFile
         Returns the output part file.  
             
         
        """
        pass
    @property
    def UseCurrentPart(self) -> bool:
        """
        Getter for property: (bool) UseCurrentPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    @UseCurrentPart.setter
    def UseCurrentPart(self, useCurrentPart: bool):
        """
        Setter for property: (bool) UseCurrentPart
         Returns the flag indicating whether to use the current work part.  
             
         
        """
        pass
    @property
    def UseExistComp(self) -> bool:
        """
        Getter for property: (bool) UseExistComp
         Returns the flag indicating whether to use existing components.  
             
         
        """
        pass
    @UseExistComp.setter
    def UseExistComp(self, useExistComp: bool):
        """
        Setter for property: (bool) UseExistComp
         Returns the flag indicating whether to use existing components.  
             
         
        """
        pass
import NXOpen
class IncrementalChange(NXOpen.TaggedObject): 
    """ Represents a NXOpen.PcbExchange.IncrementalChange. """
    @property
    def Accepted(self) -> bool:
        """
        Getter for property: (bool) Accepted
         Returns the flag indicating whether a change is accepted.  
             
         
        """
        pass
    @Accepted.setter
    def Accepted(self, isAccepted: bool):
        """
        Setter for property: (bool) Accepted
         Returns the flag indicating whether a change is accepted.  
             
         
        """
        pass
    @property
    def Comments(self) -> str:
        """
        Getter for property: (str) Comments
         Returns the comments.  
             
         
        """
        pass
    @Comments.setter
    def Comments(self, comments: str):
        """
        Setter for property: (str) Comments
         Returns the comments.  
             
         
        """
        pass
    @property
    def Transaction(self) -> str:
        """
        Getter for property: (str) Transaction
         Returns the transaction.  
             
         
        """
        pass
    @Transaction.setter
    def Transaction(self, transaction: str):
        """
        Setter for property: (str) Transaction
         Returns the transaction.  
             
         
        """
        pass
    def GetAttributes(self) -> Tuple[List[str], List[str]]:
        """
         Returns the attributes. 
         Returns A tuple consisting of (values, names). 
         - values is: List[str]. Attribute values. .
         - names is: List[str]. Attribute names. .

        """
        pass
import NXOpen
class IncrementalExportBuilder(NXOpen.Builder): 
    """ Represents a builder to export incremental changes. """
    class ExportUnitsEnum(Enum):
        """
        Members Include: 
         |Mm| 
         |Thou| 

        """
        Mm: int
        Thou: int
        @staticmethod
        def ValueOf(value: int) -> IncrementalExportBuilder.ExportUnitsEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FormatEnum(Enum):
        """
        Members Include: 
         |Idx2| 
         |Idx3| 

        """
        Idx2: int
        Idx3: int
        @staticmethod
        def ValueOf(value: int) -> IncrementalExportBuilder.FormatEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TargetLocationEnum(Enum):
        """
        Members Include: 
         |Os| 
         |TeamcenterCS| 

        """
        Os: int
        TeamcenterCS: int
        @staticmethod
        def ValueOf(value: int) -> IncrementalExportBuilder.TargetLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CloneAssembly(self) -> bool:
        """
        Getter for property: (bool) CloneAssembly
         Returns the flag indicating whether to clone the assembly.  
             
         
        """
        pass
    @CloneAssembly.setter
    def CloneAssembly(self, cloneAssembly: bool):
        """
        Setter for property: (bool) CloneAssembly
         Returns the flag indicating whether to clone the assembly.  
             
         
        """
        pass
    @property
    def FileFormat(self) -> IncrementalExportBuilder.FormatEnum:
        """
        Getter for property: ( IncrementalExportBuilder.FormatEnum NXOpen.P) FileFormat
         Returns the file format.  
             
         
        """
        pass
    @FileFormat.setter
    def FileFormat(self, fileFormat: IncrementalExportBuilder.FormatEnum):
        """
        Setter for property: ( IncrementalExportBuilder.FormatEnum NXOpen.P) FileFormat
         Returns the file format.  
             
         
        """
        pass
    @property
    def FileNote(self) -> str:
        """
        Getter for property: (str) FileNote
         Returns the file note.  
             
         
        """
        pass
    @FileNote.setter
    def FileNote(self, fileNote: str):
        """
        Setter for property: (str) FileNote
         Returns the file note.  
             
         
        """
        pass
    @property
    def FileUnits(self) -> IncrementalExportBuilder.ExportUnitsEnum:
        """
        Getter for property: ( IncrementalExportBuilder.ExportUnitsEnum NXOpen.P) FileUnits
         Returns the file units.  
             
         
        """
        pass
    @FileUnits.setter
    def FileUnits(self, exportUnits: IncrementalExportBuilder.ExportUnitsEnum):
        """
        Setter for property: ( IncrementalExportBuilder.ExportUnitsEnum NXOpen.P) FileUnits
         Returns the file units.  
             
         
        """
        pass
    @property
    def Output(self) -> str:
        """
        Getter for property: (str) Output
         Returns the output file.  
             
         
        """
        pass
    @Output.setter
    def Output(self, filename: str):
        """
        Setter for property: (str) Output
         Returns the output file.  
             
         
        """
        pass
    @property
    def SelectedObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectedObjects
         Returns the selected objects.  
             
         
        """
        pass
    @property
    def TargetLocation(self) -> IncrementalExportBuilder.TargetLocationEnum:
        """
        Getter for property: ( IncrementalExportBuilder.TargetLocationEnum NXOpen.P) TargetLocation
         Returns the target location.  
             
         
        """
        pass
    @TargetLocation.setter
    def TargetLocation(self, targetLocation: IncrementalExportBuilder.TargetLocationEnum):
        """
        Setter for property: ( IncrementalExportBuilder.TargetLocationEnum NXOpen.P) TargetLocation
         Returns the target location.  
             
         
        """
        pass
    @property
    def UseCloneSelection(self) -> bool:
        """
        Getter for property: (bool) UseCloneSelection
         Returns the flag indicating whether to clone only selected objects.  
             
         
        """
        pass
    @UseCloneSelection.setter
    def UseCloneSelection(self, canUseCloneSelection: bool):
        """
        Setter for property: (bool) UseCloneSelection
         Returns the flag indicating whether to clone only selected objects.  
             
         
        """
        pass
    def CompareAssembly(self) -> bool:
        """
         Compares the current model with the baseline and returns the flag indicating whether the model has changes. 
         Returns hasChanges (bool): .
        """
        pass
    def GetIncrementalChanges(self) -> List[IncrementalChange]:
        """
         Returns the incremental changes. 
         Returns changes ( IncrementalChange List[NXOpen): .
        """
        pass
    def RunPreExportIncrementalHook(self) -> None:
        """
         Runs the pre-export incremental hook and sets the output file, if defined. 
        """
        pass
    def SetIncrementalChanges(self, changes: List[IncrementalChange]) -> None:
        """
         Sets the incremental changes. 
        """
        pass
import NXOpen
class IncrementalImportBuilder(NXOpen.Builder): 
    """ Represents a builder to import incremental changes. """
    @property
    def Filename(self) -> str:
        """
        Getter for property: (str) Filename
         Returns the filename.  
             
         
        """
        pass
    @Filename.setter
    def Filename(self, filename: str):
        """
        Setter for property: (str) Filename
         Returns the filename.  
             
         
        """
        pass
    @property
    def OnlyUseExistingComponents(self) -> bool:
        """
        Getter for property: (bool) OnlyUseExistingComponents
         Returns the flag indicating whether to only use existing components.  
             
         
        """
        pass
    @OnlyUseExistingComponents.setter
    def OnlyUseExistingComponents(self, onlyUseExistingComp: bool):
        """
        Setter for property: (bool) OnlyUseExistingComponents
         Returns the flag indicating whether to only use existing components.  
             
         
        """
        pass
    @property
    def Output(self) -> str:
        """
        Getter for property: (str) Output
         Returns the output file.  
             
         
        """
        pass
    @Output.setter
    def Output(self, output: str):
        """
        Setter for property: (str) Output
         Returns the output file.  
             
         
        """
        pass
    def AcceptAll(self) -> None:
        """
         Accepts all changes. 
        """
        pass
    def AcceptBoardChange(self, id: str) -> None:
        """
         Sets the board change state to true and accepts change with id. 
        """
        pass
    def AcceptChange(self, id: str) -> None:
        """
         Accepts a change. 
        """
        pass
    def AcknowledgeAll(self) -> None:
        """
         Acknowledges all changes. 
        """
        pass
    def AcknowledgeResponse(self, id: str) -> None:
        """
         Acknowledges a change. 
        """
        pass
    def AddNewComment(self, id: str, comment: str) -> None:
        """
         Adds a new comment to a response. 
        """
        pass
    def CancelIncrementReview(self) -> None:
        """
         Cancels increment review. 
        """
        pass
    def ClearProcessedIncrementalGroupVec(self) -> None:
        """
         Clear processed incremental group. 
        """
        pass
    def IgnoreAll(self) -> None:
        """
         Ignores all changes. 
        """
        pass
    def IgnoreResponse(self, id: str) -> None:
        """
         Ignores a change. 
        """
        pass
    def PreviewChanges(self) -> None:
        """
         Previews all changes. 
        """
        pass
    def ReadImportFile(self) -> None:
        """
         Reads the import file. 
        """
        pass
    def RejectAll(self) -> None:
        """
         Rejects all changes. 
        """
        pass
    def RejectBoardChange(self, id: str) -> None:
        """
         Sets the board change state to false and rejects change with id. 
        """
        pass
    def RejectChange(self, id: str) -> None:
        """
         Rejects a change. 
        """
        pass
    def SetBoardUpdated(self, updated: bool) -> None:
        """
         Sets board update status. 
        """
        pass
    def SetExistingPart(self) -> NXOpen.DisplayableObject:
        """
         Makes the supplied part the display part. 
         Returns existingPartTag ( NXOpen.DisplayableObject): .
        """
        pass
    def UnhighlightAll(self) -> None:
        """
         Un-highlights all. 
        """
        pass
import NXOpen
class Manager(NXOpen.Object): 
    """ Represents a PCB exchange manager. """
    @property
    def AlternateComponentManager() -> AlternateComponentManager:
        """
         Returns the PcbExchange.AlternateComponentManager instance belonging to this instance. 
        """
        pass
    @property
    def PendingComponentManager() -> PendingComponentManager:
        """
         Returns the PcbExchange.PendingComponentManager instance belonging to this instance. 
        """
        pass
    @property
    def NotificationManager() -> NotificationManager:
        """
         Returns the PcbExchange.NotificationManager instance belonging to this instance. 
        """
        pass
    def AutoCreateAreas() -> None:
        """
         Automatically creates areas. 
        """
        pass
    def AutoCreateComponents() -> None:
        """
         Automatically creates components. 
        """
        pass
    def CreateAdvancedConductivityBuilder(part: NXOpen.NXObject) -> AdvancedConductivityBuilder:
        """
         Creates an instance of PcbExchange.AdvancedConductivityBuilder. 
         Returns builder ( AdvancedConductivityBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateAreaAttributesBuilder(part: NXOpen.NXObject) -> AreaAttributesBuilder:
        """
         Creates an instance of PcbExchange.AreaAttributesBuilder  
         Returns builder ( AreaAttributesBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateAreaMappingBuilder(part: NXOpen.NXObject, areaMapping: AreaMapping) -> AreaMappingBuilder:
        """
         Creates or edit an instance of PcbExchange.AreaMappingBuilder. 
         Returns builder ( AreaMappingBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateBoardAttributesBuilder(part: NXOpen.NXObject) -> BoardAttributesBuilder:
        """
         Creates an instance of PcbExchange.BoardAttributesBuilder. 
         Returns builder ( BoardAttributesBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateBoardPropertiesBuilder(part: NXOpen.NXObject) -> BoardPropertiesBuilder:
        """
         Creates an instance of PcbExchange.BoardPropertiesBuilder. 
         Returns builder ( BoardPropertiesBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateCompareAndUpdateBuilder(part: NXOpen.NXObject) -> CompareAndUpdateBuilder:
        """
         Creates an instance of PcbExchange.CompareAndUpdateBuilder. 
         Returns builder ( CompareAndUpdateBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateComponentAttributesBuilder(part: NXOpen.NXObject) -> ComponentAttributesBuilder:
        """
         Creates an instance of PcbExchange.ComponentAttributesBuilder. 
         Returns builder ( ComponentAttributesBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateComponentConstraintsBuilder(part: NXOpen.NXObject) -> ComponentConstraintsBuilder:
        """
         Creates an instance of PcbExchange.ComponentConstraintsBuilder. 
         Returns builder ( ComponentConstraintsBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateComponentCsysBuilder(part: NXOpen.NXObject) -> ComponentCsysBuilder:
        """
         Creates an instance of PcbExchange.ComponentCsysBuilder. 
         Returns builder ( ComponentCsysBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateComponentPlacementOutlineBuilder(part: NXOpen.NXObject) -> ComponentPlacementOutlineBuilder:
        """
         Creates an instance of PcbExchange.ComponentPlacementOutlineBuilder. 
         Returns builder ( ComponentPlacementOutlineBuilder NXOpen.P):  created builder. .
        """
        pass
    @overload
    def CreateDesignRuleBuilder(part: NXOpen.NXObject) -> DesignRuleBuilder:
        """
         Creates a PcbExchange.DesignRuleBuilder which creates a NXOpen.PcbExchange.DesignRule in the given part. 
         Returns builder ( DesignRuleBuilder NXOpen.P):  created builder. .
        """
        pass
    @overload
    def CreateDesignRuleBuilder(ruleToEdit: DesignRule) -> DesignRuleBuilder:
        """
         Creates a PcbExchange.DesignRuleBuilder which edits a NXOpen.PcbExchange.DesignRule. 
         Returns builder ( DesignRuleBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateDesignValidator(part: NXOpen.NXObject) -> DesignValidator:
        """
         Creates a PcbExchange.DesignValidator to validate the design rules in the given part. 
         Returns validator ( DesignValidator NXOpen.P):  created validator. .
        """
        pass
    def CreateEcadExportBuilder(part: NXOpen.NXObject) -> EcadExportBuilder:
        """
         Creates an instance of PcbExchange.EcadExportBuilder. 
         Returns builder ( EcadExportBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateEcadImportBuilder(part: NXOpen.NXObject) -> EcadImportBuilder:
        """
         Creates an instance of PcbExchange.EcadImportBuilder. 
         Returns builder ( EcadImportBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateEcadPanelImportBuilder(part: NXOpen.NXObject) -> EcadPanelImportBuilder:
        """
         Creates an instance of PcbExchange.EcadPanelImportBuilder. 
         Returns builder ( EcadPanelImportBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateEntityFilterBuilder(part: NXOpen.NXObject, entityFilter: EntityFilter) -> EntityFilterBuilder:
        """
         Creates an instance of PcbExchange.EntityFilterBuilder. 
         Returns builder ( EntityFilterBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateExternalDataImportBuilder(part: NXOpen.NXObject) -> ExternalDataImportBuilder:
        """
         Creates an instance of PcbExchange.ExternalDataImportBuilder. 
         Returns builder ( ExternalDataImportBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateHoleAttributesBuilder(part: NXOpen.NXObject) -> HoleAttributesBuilder:
        """
         Creates an instance of PcbExchange.HoleAttributesBuilder. 
         Returns builder ( HoleAttributesBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateIdxCompareBuilder(part: NXOpen.NXObject) -> IdxCompareBuilder:
        """
         Creates an instance of PcbExchange.IdxCompareBuilder. 
         Returns builder ( IdxCompareBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateIdxExportBuilder(part: NXOpen.NXObject) -> IdxExportBuilder:
        """
         Creates an instance of PcbExchange.IdxExportBuilder. 
         Returns builder ( IdxExportBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateIdxImportBuilder(part: NXOpen.NXObject) -> IdxImportBuilder:
        """
         Creates an instance of PcbExchange.IdxImportBuilder. 
         Returns builder ( IdxImportBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateIncrementalChange() -> IncrementalChange:
        """
         Creates an instance of PcbExchange.IncrementalChange. 
         Returns change ( IncrementalChange NXOpen.P):  created IncrementalChange .
        """
        pass
    def CreateIncrementalExportBuilder(part: NXOpen.NXObject) -> IncrementalExportBuilder:
        """
         Creates an instance of PcbExchange.IncrementalExportBuilder. 
         Returns builder ( IncrementalExportBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateIncrementalImportBuilder(part: NXOpen.NXObject) -> IncrementalImportBuilder:
        """
         Creates an instance of PcbExchange.IncrementalImportBuilder. 
         Returns builder ( IncrementalImportBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateMcadPinAttributesBuilder(part: NXOpen.NXObject) -> McadPinAttributesBuilder:
        """
         Creates an instance of PcbExchange.McadPinAttributesBuilder. 
         Returns builder ( McadPinAttributesBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateMultiHeightAreaCreateBuilder(part: NXOpen.NXObject) -> MultiHeightAreaCreateBuilder:
        """
         Creates an instance of PcbExchange.MultiHeightAreaCreateBuilder. 
         Returns builder ( MultiHeightAreaCreateBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreatePreferencesBuilder(part: NXOpen.NXObject) -> PreferencesBuilder:
        """
         Creates an instance of PcbExchange.PreferencesBuilder. 
         Returns builder ( PreferencesBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreatePrimaryPinsVisualizeBuilder(part: NXOpen.NXObject) -> PrimaryPinsVisualizeBuilder:
        """
         Creates an instance of PcbExchange.PrimaryPinsVisualizeBuilder. 
         Returns builder ( PrimaryPinsVisualizeBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateReportBuilder(part: NXOpen.NXObject) -> ReportBuilder:
        """
         Creates an instance of PcbExchange.ReportBuilder. 
         Returns builder ( ReportBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateStructuralSolutionBuilder(part: NXOpen.NXObject) -> StructuralSolutionBuilder:
        """
         Creates an instance of PcbExchange.StructuralSolutionBuilder. 
         Returns builder ( StructuralSolutionBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateTemplateBuilder(part: NXOpen.NXObject) -> TemplateBuilder:
        """
         Creates an instance of PcbExchange.TemplateBuilder. 
         Returns builder ( TemplateBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateThermalSolutionBuilder(part: NXOpen.NXObject) -> ThermalSolutionBuilder:
        """
         Creates an instance of PcbExchange.ThermalSolutionBuilder. 
         Returns builder ( ThermalSolutionBuilder NXOpen.P):  created builder. .
        """
        pass
    def CreateVariantManagerBuilder(part: NXOpen.NXObject) -> VariantManagerBuilder:
        """
         Creates an instance of PcbExchange.VariantManagerBuilder. 
         Returns builder ( VariantManagerBuilder NXOpen.P):  created builder. .
        """
        pass
    def ExportJTFile() -> str:
        """
         Exports a JT file. 
         Returns jtFilename (str): .
        """
        pass
    def HideEcadPrimaryPads() -> None:
        """
         Hides Ecad primary pads. 
        """
        pass
    def HideEcadPrimaryPins() -> None:
        """
         Hides Ecad primary pins. 
        """
        pass
    def HideMcadPrimaryPins() -> None:
        """
         Hides Mcad primary pins. 
        """
        pass
    def HideTestPoints() -> None:
        """
         Hides test points. 
        """
        pass
    def InitializeCopperForBending() -> None:
        """
         Initialize copper for bending. 
        """
        pass
    def RefreshPrimaryPinMismatchInfo() -> None:
        """
         Refreshes the primary pin mismatch information. 
        """
        pass
    def ReplaceWithLibraryComponent(components: List[NXOpen.NXObject]) -> None:
        """
         Updates the components using the library components. 
        """
        pass
    def ResumeNavigatorUpdate(refreshNavigator: bool) -> None:
        """
         Resumes PCB exchange navigator update. 
        """
        pass
    def ShowAreasAsBodies() -> None:
        """
         Displays areas as bodies. 
        """
        pass
    def ShowAreasAsSketches() -> None:
        """
         Displays areas as sketches. 
        """
        pass
    def ShowEcadPrimaryPads() -> None:
        """
         Displays Ecad primary pads. 
        """
        pass
    def ShowEcadPrimaryPins() -> None:
        """
         Displays Ecad primary pins. 
        """
        pass
    def ShowMcadPrimaryPins() -> None:
        """
         Displays Mcad primary pins. 
        """
        pass
    def ShowTestPoints() -> None:
        """
         Displays test points. 
        """
        pass
    def SuspendNavigatorUpdate() -> None:
        """
         Suspends PCB exchange navigator update. 
        """
        pass
    def TagModelAsBaseline() -> None:
        """
         Tags the work part model as baseline. 
        """
        pass
import NXOpen
class McadPinAttributesBuilder(NXOpen.Builder): 
    """ Represents a builder to set Mcad primary pin attributes. """
    @property
    def Point(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Point
         Returns the point.  
             
         
        """
        pass
import NXOpen
class MultiHeightAreaCreateBuilder(NXOpen.Builder): 
    """ Represents a builder to create a multi-height area. """
    class OwnerEnum(Enum):
        """
        Members Include: 
         |Unowned| 
         |Mcad| 
         |Ecad| 

        """
        Unowned: int
        Mcad: int
        Ecad: int
        @staticmethod
        def ValueOf(value: int) -> MultiHeightAreaCreateBuilder.OwnerEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeEnum(Enum):
        """
        Members Include: 
         |Keepout| 
         |Keepin| 

        """
        Keepout: int
        Keepin: int
        @staticmethod
        def ValueOf(value: int) -> MultiHeightAreaCreateBuilder.TypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AreaType(self) -> MultiHeightAreaCreateBuilder.TypeEnum:
        """
        Getter for property: ( MultiHeightAreaCreateBuilder.TypeEnum NXOpen.P) AreaType
         Returns the area type.  
             
         
        """
        pass
    @AreaType.setter
    def AreaType(self, type: MultiHeightAreaCreateBuilder.TypeEnum):
        """
        Setter for property: ( MultiHeightAreaCreateBuilder.TypeEnum NXOpen.P) AreaType
         Returns the area type.  
             
         
        """
        pass
    @property
    def BoundingObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) BoundingObjects
         Returns the bounding objects.  
             
         
        """
        pass
    @property
    def Color(self) -> int:
        """
        Getter for property: (int) Color
         Returns the area color.  
             
         
        """
        pass
    @Color.setter
    def Color(self, color: int):
        """
        Setter for property: (int) Color
         Returns the area color.  
             
         
        """
        pass
    @property
    def DecimalPrecision(self) -> int:
        """
        Getter for property: (int) DecimalPrecision
         Returns the decimal precision.  
             
         
        """
        pass
    @DecimalPrecision.setter
    def DecimalPrecision(self, decimalPrecision: int):
        """
        Setter for property: (int) DecimalPrecision
         Returns the decimal precision.  
             
         
        """
        pass
    @property
    def HeightClearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HeightClearance
         Returns the height clearance.  
             
         
        """
        pass
    @property
    def InvertedVolume(self) -> bool:
        """
        Getter for property: (bool) InvertedVolume
         Returns the flag indicating whether an area has an inverted volume.  
             
         
        """
        pass
    @InvertedVolume.setter
    def InvertedVolume(self, invertedVolume: bool):
        """
        Setter for property: (bool) InvertedVolume
         Returns the flag indicating whether an area has an inverted volume.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the area name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the area name.  
             
         
        """
        pass
    @property
    def Owner(self) -> MultiHeightAreaCreateBuilder.OwnerEnum:
        """
        Getter for property: ( MultiHeightAreaCreateBuilder.OwnerEnum NXOpen.P) Owner
         Returns the area owner.  
             
         
        """
        pass
    @Owner.setter
    def Owner(self, type: MultiHeightAreaCreateBuilder.OwnerEnum):
        """
        Setter for property: ( MultiHeightAreaCreateBuilder.OwnerEnum NXOpen.P) Owner
         Returns the area owner.  
             
         
        """
        pass
    @property
    def PrimaryFace(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) PrimaryFace
         Returns the primary face.  
             
         
        """
        pass
    @property
    def ResolutionX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ResolutionX
         Returns the resolution along the X axis.  
             
         
        """
        pass
    @property
    def ResolutionY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ResolutionY
         Returns the resolution along the Y axis.  
             
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the flag indicating whether to reverse the primary selection's normal direction.  
             
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the flag indicating whether to reverse the primary selection's normal direction.  
             
         
        """
        pass
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log window.  
             
         
        """
        pass
    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log window.  
             
         
        """
        pass
    @property
    def UniteBodies(self) -> bool:
        """
        Getter for property: (bool) UniteBodies
         Returns the flag indicating whether to unite the area bodies.  
             
         
        """
        pass
    @UniteBodies.setter
    def UniteBodies(self, uniteBodies: bool):
        """
        Setter for property: (bool) UniteBodies
         Returns the flag indicating whether to unite the area bodies.  
             
         
        """
        pass
import NXOpen
class NotificationManager(NXOpen.Object): 
    """ Represents a NXOpen.PcbExchange.NotificationManager. """
    def DeletePendingComponent(pendingComponent: str) -> None:
        """
         Sends a notificatoin to delete the pending component from PCB navigator. 
        """
        pass
import NXOpen
class PendingComponentManager(NXOpen.Object): 
    """ Represents a NXOpen.PcbExchange.PendingComponentManager. """
    def Add(pendingComponents: List[str], isNonGeometric: bool) -> Tuple[int, List[NXOpen.NXObject]]:
        """
         Adds the pending components. 
         Returns A tuple consisting of (numComponents, components). 
         - numComponents is: int.
         - components is:  NXOpen.NXObject Li. added components. .

        """
        pass
    def Delete(pendingComponents: List[str]) -> None:
        """
         Deletes the pending components. 
        """
        pass
import NXOpen
class PreferencesBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit PCB exchange preferences"""
    class BoardThicknessSourceTypeName(Enum):
        """
        Members Include: 
         |FromPart| 
         |Specify| 

        """
        FromPart: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.BoardThicknessSourceTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentLoadOptionsTypeName(Enum):
        """
        Members Include: 
         |LoadAndCreateAssemblyComponents| 
         |CreateBodiesOnly| 
         |LoadAssemblyComponentsCreateBodies| 

        """
        LoadAndCreateAssemblyComponents: int
        CreateBodiesOnly: int
        LoadAssemblyComponentsCreateBodies: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentLoadOptionsTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentsConnectionToBoardTypeName(Enum):
        """
        Members Include: 
         |Rbe2| 
         |Rbe3| 

        """
        Rbe2: int
        Rbe3: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentsConnectionToBoardTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentsElementSizeOptionsTypeName(Enum):
        """
        Members Include: 
         |Auto| 
         |Specify| 

        """
        Auto: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentsElementSizeOptionsTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentsElementThicknessOptionsTypeName(Enum):
        """
        Members Include: 
         |Null| 
         |Specify| 

        """
        Null: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentsElementThicknessOptionsTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentsHeightFromTypeName(Enum):
        """
        Members Include: 
         |FootprintDefinition| 
         |PartDefinition| 

        """
        FootprintDefinition: int
        PartDefinition: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentsHeightFromTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentsMaterialFromTypeName(Enum):
        """
        Members Include: 
         |Pcb| 
         |Nx| 

        """
        Pcb: int
        Nx: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentsMaterialFromTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentsModelTypeName(Enum):
        """
        Members Include: 
         |ZeroResistor| 
         |OneResistor| 
         |TwoResistor| 
         |NotSet| 

        """
        ZeroResistor: int
        OneResistor: int
        TwoResistor: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ComponentsModelTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CreateNewComponentsInTypeName(Enum):
        """
        Members Include: 
         |DirectoryOfECADFiles| 
         |DirectoryOfNXParts| 
         |Specify| 

        """
        DirectoryOfECADFiles: int
        DirectoryOfNXParts: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.CreateNewComponentsInTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DefaultPcaNameTypeName(Enum):
        """
        Members Include: 
         |CurrentNXModel| 
         |ECADModelName| 
         |SpecifyAtImport| 

        """
        CurrentNXModel: int
        ECADModelName: int
        SpecifyAtImport: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.DefaultPcaNameTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ElementTypeForStructuralAnalysisTypeName(Enum):
        """
        Members Include: 
         |Ctria3| 
         |Cquad4| 
         |Ctria6| 
         |Cquad8| 

        """
        Ctria3: int
        Cquad4: int
        Ctria6: int
        Cquad8: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GroupEntityComponentsByTypeName(Enum):
        """
        Members Include: 
         |NotSet| 
         |Type| 
         |Layer| 

        """
        NotSet: int
        Type: int
        Layer: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.GroupEntityComponentsByTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImportExportFlexBentType(Enum):
        """
        Members Include: 
         |No| 
         |ExportOnly| 
         |ImportAndExport| 

        """
        No: int
        ExportOnly: int
        ImportAndExport: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ImportExportFlexBentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImportGenericMenuTypeName(Enum):
        """
        Members Include: 
         |Curves| 
         |Sheets| 
         |Bodies| 

        """
        Curves: int
        Sheets: int
        Bodies: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ImportGenericMenuTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImportMaskMenuTypeName(Enum):
        """
        Members Include: 
         |Curves| 
         |Sheets| 
         |Bodies| 

        """
        Curves: int
        Sheets: int
        Bodies: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ImportMaskMenuTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImportMasksMethodType(Enum):
        """
        Members Include: 
         |Positive| 
         |Negative| 
         |NegativeWithHoles| 

        """
        Positive: int
        Negative: int
        NegativeWithHoles: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ImportMasksMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImportPadMenuTypeName(Enum):
        """
        Members Include: 
         |Curves| 
         |Sheets| 
         |Bodies| 

        """
        Curves: int
        Sheets: int
        Bodies: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ImportPadMenuTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImportTraceMenuTypeName(Enum):
        """
        Members Include: 
         |Curves| 
         |Sheets| 
         |Bodies| 

        """
        Curves: int
        Sheets: int
        Bodies: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ImportTraceMenuTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MailProtocolTypeName(Enum):
        """
        Members Include: 
         |Mapi| 
         |Smtp| 

        """
        Mapi: int
        Smtp: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.MailProtocolTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MergeTracesAndPadsType(Enum):
        """
        Members Include: 
         |NotSet| 
         |TracesByNet| 
         |TracesAndPadsByNet| 
         |HolesAndTracesAndPadsByNet| 

        """
        NotSet: int
        TracesByNet: int
        TracesAndPadsByNet: int
        HolesAndTracesAndPadsByNet: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.MergeTracesAndPadsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ModelForStructuralAnalysisTypeName(Enum):
        """
        Members Include: 
         |SingleLayer| 
         |MultiLayer| 

        """
        SingleLayer: int
        MultiLayer: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ModelForStructuralAnalysisTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ModelForThermalAnalysisTypeName(Enum):
        """
        Members Include: 
         |SingleLayer| 
         |TopAndBottom| 
         |MultiLayer| 
         |Solid| 

        """
        SingleLayer: int
        TopAndBottom: int
        MultiLayer: int
        Solid: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ModelForThermalAnalysisTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResistorModelTypeName(Enum):
        """
        Members Include: 
         |NotSet| 
         |DissipationOnly| 
         |ThetaCB| 
         |ThetaJCJB| 
         |ThetaJCCB| 

        """
        NotSet: int
        DissipationOnly: int
        ThetaCB: int
        ThetaJCJB: int
        ThetaJCCB: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ResistorModelTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SettingsSourceTypeName(Enum):
        """
        Members Include: 
         |IniFiles| 
         |SpecifiedSettingsFolder| 
         |CustomerDefaults| 

        """
        IniFiles: int
        SpecifiedSettingsFolder: int
        CustomerDefaults: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.SettingsSourceTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StructuralAlgorithmTypeName(Enum):
        """
        Members Include: 
         |Equivalent| 

        """
        Equivalent: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.StructuralAlgorithmTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThermalAlgorithmTypeName(Enum):
        """
        Members Include: 
         |Discretized| 
         |Equivalent| 

        """
        Discretized: int
        Equivalent: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ThermalAlgorithmTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThicknessSourceForStructuralAnalysisTypeName(Enum):
        """
        Members Include: 
         |FromPart| 
         |Specify| 

        """
        FromPart: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AreaNamePrefix(self) -> str:
        """
        Getter for property: (str) AreaNamePrefix
         Returns the area name prefix.  
             
         
        """
        pass
    @AreaNamePrefix.setter
    def AreaNamePrefix(self, mAreaNamePrefix: str):
        """
        Setter for property: (str) AreaNamePrefix
         Returns the area name prefix.  
             
         
        """
        pass
    @property
    def AreaNameSuffix(self) -> str:
        """
        Getter for property: (str) AreaNameSuffix
         Returns the area name suffix.  
             
         
        """
        pass
    @AreaNameSuffix.setter
    def AreaNameSuffix(self, mAreaNameSuffix: str):
        """
        Setter for property: (str) AreaNameSuffix
         Returns the area name suffix.  
             
         
        """
        pass
    @property
    def AreasAsAssemblyComponents(self) -> bool:
        """
        Getter for property: (bool) AreasAsAssemblyComponents
         Returns the flag indicating whether to create areas as assembly components.  
             
         
        """
        pass
    @AreasAsAssemblyComponents.setter
    def AreasAsAssemblyComponents(self, mAreasAsAssemblyComponents: bool):
        """
        Setter for property: (bool) AreasAsAssemblyComponents
         Returns the flag indicating whether to create areas as assembly components.  
             
         
        """
        pass
    @property
    def AssociateAreaBodies(self) -> bool:
        """
        Getter for property: (bool) AssociateAreaBodies
         Returns the flag indicating whether to associate areas as bodies.  
             
         
        """
        pass
    @AssociateAreaBodies.setter
    def AssociateAreaBodies(self, associateAreaBodies: bool):
        """
        Setter for property: (bool) AssociateAreaBodies
         Returns the flag indicating whether to associate areas as bodies.  
             
         
        """
        pass
    @property
    def AssociateComponentBodies(self) -> bool:
        """
        Getter for property: (bool) AssociateComponentBodies
         Returns the flag indicating whether to associate components as bodies.  
             
         
        """
        pass
    @AssociateComponentBodies.setter
    def AssociateComponentBodies(self, associateComponentBodies: bool):
        """
        Setter for property: (bool) AssociateComponentBodies
         Returns the flag indicating whether to associate components as bodies.  
             
         
        """
        pass
    @property
    def AssociateCopperObjects(self) -> bool:
        """
        Getter for property: (bool) AssociateCopperObjects
         Returns the flag indicating whether to associate copper objects.  
             
         
        """
        pass
    @AssociateCopperObjects.setter
    def AssociateCopperObjects(self, associateCopperObjects: bool):
        """
        Setter for property: (bool) AssociateCopperObjects
         Returns the flag indicating whether to associate copper objects.  
             
         
        """
        pass
    @property
    def AutomaticallySaveAllCreatedParts(self) -> bool:
        """
        Getter for property: (bool) AutomaticallySaveAllCreatedParts
         Returns the flag indicating whether to automatically save all created parts.  
             
         
        """
        pass
    @AutomaticallySaveAllCreatedParts.setter
    def AutomaticallySaveAllCreatedParts(self, mAutomaticallySaveAllCreatedParts: bool):
        """
        Setter for property: (bool) AutomaticallySaveAllCreatedParts
         Returns the flag indicating whether to automatically save all created parts.  
             
         
        """
        pass
    @property
    def BoardAsAssemblyComponent(self) -> bool:
        """
        Getter for property: (bool) BoardAsAssemblyComponent
         Returns the flag indicating whether to create the board as an assembly component.  
             
         
        """
        pass
    @BoardAsAssemblyComponent.setter
    def BoardAsAssemblyComponent(self, mBoardAsAssemblyComponent: bool):
        """
        Setter for property: (bool) BoardAsAssemblyComponent
         Returns the flag indicating whether to create the board as an assembly component.  
             
         
        """
        pass
    @property
    def BoardColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) BoardColor
         Returns the board color.  
             
         
        """
        pass
    @BoardColor.setter
    def BoardColor(self, mBoardColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) BoardColor
         Returns the board color.  
             
         
        """
        pass
    @property
    def BoardDefaultPlatingThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BoardDefaultPlatingThickness
         Returns the plating thickness for thermal analysis.  
             
         
        """
        pass
    @property
    def BoardDefaultThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BoardDefaultThickness
         Returns the board default thickness.  
             
         
        """
        pass
    @property
    def BoardDefaultTraceThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BoardDefaultTraceThickness
         Returns the trace thickness for thermal analysis.  
             
         
        """
        pass
    @property
    def BoardElementColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) BoardElementColor
         Returns the board mesh element color for thermal analysis.  
             
         
        """
        pass
    @BoardElementColor.setter
    def BoardElementColor(self, mBoardElementColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) BoardElementColor
         Returns the board mesh element color for thermal analysis.  
             
         
        """
        pass
    @property
    def BoardElementSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BoardElementSize
         Returns the board mesh element size for thermal analysis.  
             
         
        """
        pass
    @property
    def BoardLayer(self) -> int:
        """
        Getter for property: (int) BoardLayer
         Returns the board layer.  
             
         
        """
        pass
    @BoardLayer.setter
    def BoardLayer(self, mBoardLayer: int):
        """
        Setter for property: (int) BoardLayer
         Returns the board layer.  
             
         
        """
        pass
    @property
    def BoardNamePrefix(self) -> str:
        """
        Getter for property: (str) BoardNamePrefix
         Returns the board name prefix.  
             
         
        """
        pass
    @BoardNamePrefix.setter
    def BoardNamePrefix(self, mBoardNamePrefix: str):
        """
        Setter for property: (str) BoardNamePrefix
         Returns the board name prefix.  
             
         
        """
        pass
    @property
    def BoardNameSuffix(self) -> str:
        """
        Getter for property: (str) BoardNameSuffix
         Returns the board name suffix.  
             
         
        """
        pass
    @BoardNameSuffix.setter
    def BoardNameSuffix(self, mBoardNameSuffix: str):
        """
        Setter for property: (str) BoardNameSuffix
         Returns the board name suffix.  
             
         
        """
        pass
    @property
    def BoardThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BoardThickness
         Returns the specified board thickness for thermal analysis.  
             
         
        """
        pass
    @property
    def BoardThicknessSource(self) -> PreferencesBuilder.BoardThicknessSourceTypeName:
        """
        Getter for property: ( PreferencesBuilder.BoardThicknessSourceTypeName NXOpen.P) BoardThicknessSource
         Returns the board thickness source for thermal analysis.  
             
         
        """
        pass
    @BoardThicknessSource.setter
    def BoardThicknessSource(self, mBoardThicknessSource: PreferencesBuilder.BoardThicknessSourceTypeName):
        """
        Setter for property: ( PreferencesBuilder.BoardThicknessSourceTypeName NXOpen.P) BoardThicknessSource
         Returns the board thickness source for thermal analysis.  
             
         
        """
        pass
    @property
    def BoardTranslucency(self) -> int:
        """
        Getter for property: (int) BoardTranslucency
         Returns the board translucency.  
             
         
        """
        pass
    @BoardTranslucency.setter
    def BoardTranslucency(self, mBoardTranslucency: int):
        """
        Setter for property: (int) BoardTranslucency
         Returns the board translucency.  
             
         
        """
        pass
    @property
    def BrowseEcadFilesFromDir(self) -> str:
        """
        Getter for property: (str) BrowseEcadFilesFromDir
         Returns the ECAD files directory.  
             
         
        """
        pass
    @BrowseEcadFilesFromDir.setter
    def BrowseEcadFilesFromDir(self, foldername: str):
        """
        Setter for property: (str) BrowseEcadFilesFromDir
         Returns the ECAD files directory.  
             
         
        """
        pass
    @property
    def ComparePrimaryPinLocations(self) -> bool:
        """
        Getter for property: (bool) ComparePrimaryPinLocations
         Returns the flag indicating whether to compare primary pin locations.  
             
         
        """
        pass
    @ComparePrimaryPinLocations.setter
    def ComparePrimaryPinLocations(self, mComparePrimaryPinLocations: bool):
        """
        Setter for property: (bool) ComparePrimaryPinLocations
         Returns the flag indicating whether to compare primary pin locations.  
             
         
        """
        pass
    @property
    def ComponentLoadOptions(self) -> PreferencesBuilder.ComponentLoadOptionsTypeName:
        """
        Getter for property: ( PreferencesBuilder.ComponentLoadOptionsTypeName NXOpen.P) ComponentLoadOptions
         Returns the component load options.  
             
         
        """
        pass
    @ComponentLoadOptions.setter
    def ComponentLoadOptions(self, mComponentLoadOptions: PreferencesBuilder.ComponentLoadOptionsTypeName):
        """
        Setter for property: ( PreferencesBuilder.ComponentLoadOptionsTypeName NXOpen.P) ComponentLoadOptions
         Returns the component load options.  
             
         
        """
        pass
    @property
    def ComponentNamePrefix(self) -> str:
        """
        Getter for property: (str) ComponentNamePrefix
         Returns the component name prefix.  
             
         
        """
        pass
    @ComponentNamePrefix.setter
    def ComponentNamePrefix(self, mComponentNamePrefix: str):
        """
        Setter for property: (str) ComponentNamePrefix
         Returns the component name prefix.  
             
         
        """
        pass
    @property
    def ComponentNameSuffix(self) -> str:
        """
        Getter for property: (str) ComponentNameSuffix
         Returns the component name suffix.  
             
         
        """
        pass
    @ComponentNameSuffix.setter
    def ComponentNameSuffix(self, mComponentNameSuffix: str):
        """
        Setter for property: (str) ComponentNameSuffix
         Returns the component name suffix.  
             
         
        """
        pass
    @property
    def ComponentXMLFileBrowse(self) -> str:
        """
        Getter for property: (str) ComponentXMLFileBrowse
         Returns the component XML file.  
             
         
        """
        pass
    @ComponentXMLFileBrowse.setter
    def ComponentXMLFileBrowse(self, filename: str):
        """
        Setter for property: (str) ComponentXMLFileBrowse
         Returns the component XML file.  
             
         
        """
        pass
    @property
    def ComponentsCaseMaterial(self) -> int:
        """
        Getter for property: (int) ComponentsCaseMaterial
         Returns the component case material.  
             
         
        """
        pass
    @ComponentsCaseMaterial.setter
    def ComponentsCaseMaterial(self, mMaterial: int):
        """
        Setter for property: (int) ComponentsCaseMaterial
         Returns the component case material.  
             
         
        """
        pass
    @property
    def ComponentsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ComponentsColor
         Returns the component color.  
             
         
        """
        pass
    @ComponentsColor.setter
    def ComponentsColor(self, mComponentsColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ComponentsColor
         Returns the component color.  
             
         
        """
        pass
    @property
    def ComponentsConnectionToBoard(self) -> PreferencesBuilder.ComponentsConnectionToBoardTypeName:
        """
        Getter for property: ( PreferencesBuilder.ComponentsConnectionToBoardTypeName NXOpen.P) ComponentsConnectionToBoard
         Returns the method by which components are connected to the board for structural analysis.  
             
         
        """
        pass
    @ComponentsConnectionToBoard.setter
    def ComponentsConnectionToBoard(self, mComponentsConnectionToBoard: PreferencesBuilder.ComponentsConnectionToBoardTypeName):
        """
        Setter for property: ( PreferencesBuilder.ComponentsConnectionToBoardTypeName NXOpen.P) ComponentsConnectionToBoard
         Returns the method by which components are connected to the board for structural analysis.  
             
         
        """
        pass
    @property
    def ComponentsDefaultHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsDefaultHeight
         Returns the component default height.  
             
         
        """
        pass
    @property
    def ComponentsDefaultMass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsDefaultMass
         Returns the default component mass for structural analysis.  
             
         
        """
        pass
    @property
    def ComponentsDissipation(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsDissipation
         Returns the dissipation rate for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsElementColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ComponentsElementColor
         Returns the component mesh element color for thermal analysis.  
             
         
        """
        pass
    @ComponentsElementColor.setter
    def ComponentsElementColor(self, mComponentsElementColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ComponentsElementColor
         Returns the component mesh element color for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsElementSizeOptions(self) -> PreferencesBuilder.ComponentsElementSizeOptionsTypeName:
        """
        Getter for property: ( PreferencesBuilder.ComponentsElementSizeOptionsTypeName NXOpen.P) ComponentsElementSizeOptions
         Returns the component mesh element size option for thermal analysis.  
             
         
        """
        pass
    @ComponentsElementSizeOptions.setter
    def ComponentsElementSizeOptions(self, mComponentsElementSizeOptions: PreferencesBuilder.ComponentsElementSizeOptionsTypeName):
        """
        Setter for property: ( PreferencesBuilder.ComponentsElementSizeOptionsTypeName NXOpen.P) ComponentsElementSizeOptions
         Returns the component mesh element size option for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsElementSizeValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsElementSizeValue
         Returns the component mesh element size for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsElementThicknessOptions(self) -> PreferencesBuilder.ComponentsElementThicknessOptionsTypeName:
        """
        Getter for property: ( PreferencesBuilder.ComponentsElementThicknessOptionsTypeName NXOpen.P) ComponentsElementThicknessOptions
         Returns the component thickness option for thermal analysis.  
             
         
        """
        pass
    @ComponentsElementThicknessOptions.setter
    def ComponentsElementThicknessOptions(self, mComponentsElementThicknessOptions: PreferencesBuilder.ComponentsElementThicknessOptionsTypeName):
        """
        Setter for property: ( PreferencesBuilder.ComponentsElementThicknessOptionsTypeName NXOpen.P) ComponentsElementThicknessOptions
         Returns the component thickness option for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsElementThicknessValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsElementThicknessValue
         Returns the component thickness for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsHeightFrom(self) -> PreferencesBuilder.ComponentsHeightFromTypeName:
        """
        Getter for property: ( PreferencesBuilder.ComponentsHeightFromTypeName NXOpen.P) ComponentsHeightFrom
         Returns the component height source.  
             
         
        """
        pass
    @ComponentsHeightFrom.setter
    def ComponentsHeightFrom(self, mComponentsHeightFrom: PreferencesBuilder.ComponentsHeightFromTypeName):
        """
        Setter for property: ( PreferencesBuilder.ComponentsHeightFromTypeName NXOpen.P) ComponentsHeightFrom
         Returns the component height source.  
             
         
        """
        pass
    @property
    def ComponentsJunctionCapacitance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsJunctionCapacitance
         Returns the junction capacitance for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsJunctionCapacity(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsJunctionCapacity
         Returns the junction capacitance for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsMaterialFrom(self) -> PreferencesBuilder.ComponentsMaterialFromTypeName:
        """
        Getter for property: ( PreferencesBuilder.ComponentsMaterialFromTypeName NXOpen.P) ComponentsMaterialFrom
         Returns the source library for component materials.  
             
         
        """
        pass
    @ComponentsMaterialFrom.setter
    def ComponentsMaterialFrom(self, mComponentsMaterialFrom: PreferencesBuilder.ComponentsMaterialFromTypeName):
        """
        Setter for property: ( PreferencesBuilder.ComponentsMaterialFromTypeName NXOpen.P) ComponentsMaterialFrom
         Returns the source library for component materials.  
             
         
        """
        pass
    @property
    def ComponentsModel(self) -> PreferencesBuilder.ComponentsModelTypeName:
        """
        Getter for property: ( PreferencesBuilder.ComponentsModelTypeName NXOpen.P) ComponentsModel
         Returns the component model for thermal analysis.  
             
         
        """
        pass
    @ComponentsModel.setter
    def ComponentsModel(self, mComponentsModel: PreferencesBuilder.ComponentsModelTypeName):
        """
        Setter for property: ( PreferencesBuilder.ComponentsModelTypeName NXOpen.P) ComponentsModel
         Returns the component model for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsThetaCB(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsThetaCB
         Returns the component-to-board resistance for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsThetaJB(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsThetaJB
         Returns the junction-to-board resistance for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsThetaJC(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsThetaJC
         Returns the component-to-junction resistance for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsTmax(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsTmax
         Returns the maximum component temperature for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsTmaxCase(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsTmaxCase
         Returns the maximum case temperature for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsTmaxJunction(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ComponentsTmaxJunction
         Returns the maximum junction temperature for thermal analysis.  
             
         
        """
        pass
    @property
    def ComponentsTranslucency(self) -> int:
        """
        Getter for property: (int) ComponentsTranslucency
         Returns the component translucency.  
             
         
        """
        pass
    @ComponentsTranslucency.setter
    def ComponentsTranslucency(self, mComponentsTranslucency: int):
        """
        Setter for property: (int) ComponentsTranslucency
         Returns the component translucency.  
             
         
        """
        pass
    @property
    def ConnectComponentsToPads(self) -> bool:
        """
        Getter for property: (bool) ConnectComponentsToPads
         Returns the flag indicating whether to use component model with pads if the resistor model allows it.  
             
         
        """
        pass
    @ConnectComponentsToPads.setter
    def ConnectComponentsToPads(self, connectComponentsToPads: bool):
        """
        Setter for property: (bool) ConnectComponentsToPads
         Returns the flag indicating whether to use component model with pads if the resistor model allows it.  
             
         
        """
        pass
    @property
    def CreateNewComponentInDir(self) -> str:
        """
        Getter for property: (str) CreateNewComponentInDir
         Returns the directory where new components are created.  
             
         
        """
        pass
    @CreateNewComponentInDir.setter
    def CreateNewComponentInDir(self, foldername: str):
        """
        Setter for property: (str) CreateNewComponentInDir
         Returns the directory where new components are created.  
             
         
        """
        pass
    @property
    def CreateNewComponentsIn(self) -> PreferencesBuilder.CreateNewComponentsInTypeName:
        """
        Getter for property: ( PreferencesBuilder.CreateNewComponentsInTypeName NXOpen.P) CreateNewComponentsIn
         Returns the create new components option.  
             
         
        """
        pass
    @CreateNewComponentsIn.setter
    def CreateNewComponentsIn(self, mCreateNewComponentsIn: PreferencesBuilder.CreateNewComponentsInTypeName):
        """
        Setter for property: ( PreferencesBuilder.CreateNewComponentsInTypeName NXOpen.P) CreateNewComponentsIn
         Returns the create new components option.  
             
         
        """
        pass
    @property
    def CreateTempBoard(self) -> bool:
        """
        Getter for property: (bool) CreateTempBoard
         Returns the flag indicating whether to create a new temporary board if required when updating the NX model.  
             
         
        """
        pass
    @CreateTempBoard.setter
    def CreateTempBoard(self, createTempBoard: bool):
        """
        Setter for property: (bool) CreateTempBoard
         Returns the flag indicating whether to create a new temporary board if required when updating the NX model.  
             
         
        """
        pass
    @property
    def DefaultPcaName(self) -> PreferencesBuilder.DefaultPcaNameTypeName:
        """
        Getter for property: ( PreferencesBuilder.DefaultPcaNameTypeName NXOpen.P) DefaultPcaName
         Returns the default PCA name.  
             
         
        """
        pass
    @DefaultPcaName.setter
    def DefaultPcaName(self, mDefaultPcaName: PreferencesBuilder.DefaultPcaNameTypeName):
        """
        Setter for property: ( PreferencesBuilder.DefaultPcaNameTypeName NXOpen.P) DefaultPcaName
         Returns the default PCA name.  
             
         
        """
        pass
    @property
    def EcadFilePostProcessor(self) -> str:
        """
        Getter for property: (str) EcadFilePostProcessor
         Returns the ECAD file post processor text.  
             
         
        """
        pass
    @EcadFilePostProcessor.setter
    def EcadFilePostProcessor(self, mEcadFilePostProcessor: str):
        """
        Setter for property: (str) EcadFilePostProcessor
         Returns the ECAD file post processor text.  
             
         
        """
        pass
    @property
    def EcadFilePreProcessor(self) -> str:
        """
        Getter for property: (str) EcadFilePreProcessor
         Returns the ECAD file pre processor text.  
             
         
        """
        pass
    @EcadFilePreProcessor.setter
    def EcadFilePreProcessor(self, mEcadFilePreProcessor: str):
        """
        Setter for property: (str) EcadFilePreProcessor
         Returns the ECAD file pre processor text.  
             
         
        """
        pass
    @property
    def EcadFloatTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EcadFloatTolerance
         Returns the ECAD float tolerance.  
             
         
        """
        pass
    @property
    def EdmdDir(self) -> str:
        """
        Getter for property: (str) EdmdDir
         Returns the EDMD directory.  
             
         
        """
        pass
    @EdmdDir.setter
    def EdmdDir(self, foldername: str):
        """
        Setter for property: (str) EdmdDir
         Returns the EDMD directory.  
             
         
        """
        pass
    @property
    def ElementColorForStructuralAnalysis(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ElementColorForStructuralAnalysis
         Returns the mesh element color for structural analysis.  
             
         
        """
        pass
    @ElementColorForStructuralAnalysis.setter
    def ElementColorForStructuralAnalysis(self, mElementColorForStructuralAnalysis: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ElementColorForStructuralAnalysis
         Returns the mesh element color for structural analysis.  
             
         
        """
        pass
    @property
    def ElementSizeForStructuralAnalysis(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ElementSizeForStructuralAnalysis
         Returns the mesh element size for structural analysis.  
             
         
        """
        pass
    @property
    def ElementTypeForStructuralAnalysis(self) -> PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName:
        """
        Getter for property: ( PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName NXOpen.P) ElementTypeForStructuralAnalysis
         Returns the mesh element type for structural analysis.  
             
         
        """
        pass
    @ElementTypeForStructuralAnalysis.setter
    def ElementTypeForStructuralAnalysis(self, mElementTypeForStructuralAnalysis: PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName):
        """
        Setter for property: ( PreferencesBuilder.ElementTypeForStructuralAnalysisTypeName NXOpen.P) ElementTypeForStructuralAnalysis
         Returns the mesh element type for structural analysis.  
             
         
        """
        pass
    @property
    def ErrorChecking(self) -> bool:
        """
        Getter for property: (bool) ErrorChecking
         Returns the error checking state.  
             
         
        """
        pass
    @ErrorChecking.setter
    def ErrorChecking(self, mErrorChecking: bool):
        """
        Setter for property: (bool) ErrorChecking
         Returns the error checking state.  
             
         
        """
        pass
    @property
    def ExportBends(self) -> bool:
        """
        Getter for property: (bool) ExportBends
         Returns the flag indicating whether to export bends.  
             
         
        """
        pass
    @ExportBends.setter
    def ExportBends(self, mExportBends: bool):
        """
        Setter for property: (bool) ExportBends
         Returns the flag indicating whether to export bends.  
             
         
        """
        pass
    @property
    def FilterEcadToggle(self) -> bool:
        """
        Getter for property: (bool) FilterEcadToggle
         Returns the flag indicating whether to filter the ECAD model.  
             
         
        """
        pass
    @FilterEcadToggle.setter
    def FilterEcadToggle(self, mFilterEcadToggle: bool):
        """
        Setter for property: (bool) FilterEcadToggle
         Returns the flag indicating whether to filter the ECAD model.  
             
         
        """
        pass
    @property
    def FilterMcadToggle(self) -> bool:
        """
        Getter for property: (bool) FilterMcadToggle
         Returns the flag indicating whether to filter the MCAD model.  
             
         
        """
        pass
    @FilterMcadToggle.setter
    def FilterMcadToggle(self, mFilterMcadToggle: bool):
        """
        Setter for property: (bool) FilterMcadToggle
         Returns the flag indicating whether to filter the MCAD model.  
             
         
        """
        pass
    @property
    def GenericMaxNumber(self) -> int:
        """
        Getter for property: (int) GenericMaxNumber
         Returns the generic shapes max number.  
             
         
        """
        pass
    @GenericMaxNumber.setter
    def GenericMaxNumber(self, mGenericMaxNumber: int):
        """
        Setter for property: (int) GenericMaxNumber
         Returns the generic shapes max number.  
             
         
        """
        pass
    @property
    def GenericNamePrefix(self) -> str:
        """
        Getter for property: (str) GenericNamePrefix
         Returns the generic shapes name prefix.  
             
         
        """
        pass
    @GenericNamePrefix.setter
    def GenericNamePrefix(self, mGenericNamePrefix: str):
        """
        Setter for property: (str) GenericNamePrefix
         Returns the generic shapes name prefix.  
             
         
        """
        pass
    @property
    def GenericNameSuffix(self) -> str:
        """
        Getter for property: (str) GenericNameSuffix
         Returns the generic shapes name suffix.  
             
         
        """
        pass
    @GenericNameSuffix.setter
    def GenericNameSuffix(self, mGenericNameSuffix: str):
        """
        Setter for property: (str) GenericNameSuffix
         Returns the generic shapes name suffix.  
             
         
        """
        pass
    @property
    def GroupEntityComponentsBy(self) -> PreferencesBuilder.GroupEntityComponentsByTypeName:
        """
        Getter for property: ( PreferencesBuilder.GroupEntityComponentsByTypeName NXOpen.P) GroupEntityComponentsBy
         Returns the group entity option.  
             
         
        """
        pass
    @GroupEntityComponentsBy.setter
    def GroupEntityComponentsBy(self, mGroupEntityComponentsBy: PreferencesBuilder.GroupEntityComponentsByTypeName):
        """
        Setter for property: ( PreferencesBuilder.GroupEntityComponentsByTypeName NXOpen.P) GroupEntityComponentsBy
         Returns the group entity option.  
             
         
        """
        pass
    @property
    def GroupPads(self) -> bool:
        """
        Getter for property: (bool) GroupPads
         Returns the flag indicating whether to group pads.  
             
         
        """
        pass
    @GroupPads.setter
    def GroupPads(self, mGroupPads: bool):
        """
        Setter for property: (bool) GroupPads
         Returns the flag indicating whether to group pads.  
             
         
        """
        pass
    @property
    def HolesDefaultDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HolesDefaultDiameter
         Returns the default hole diameter.  
             
         
        """
        pass
    @property
    def IdfFloatPrecision(self) -> int:
        """
        Getter for property: (int) IdfFloatPrecision
         Returns the IDF float precision.  
             
         
        """
        pass
    @IdfFloatPrecision.setter
    def IdfFloatPrecision(self, mIdfFloatPrecision: int):
        """
        Setter for property: (int) IdfFloatPrecision
         Returns the IDF float precision.  
             
         
        """
        pass
    @property
    def IdfFloatWidth(self) -> int:
        """
        Getter for property: (int) IdfFloatWidth
         Returns the IDF float width.  
             
         
        """
        pass
    @IdfFloatWidth.setter
    def IdfFloatWidth(self, mIdfFloatWidth: int):
        """
        Setter for property: (int) IdfFloatWidth
         Returns the IDF float width.  
             
         
        """
        pass
    @property
    def ImportBends(self) -> bool:
        """
        Getter for property: (bool) ImportBends
         Returns the flag indicating whether to import bends.  
             
         
        """
        pass
    @ImportBends.setter
    def ImportBends(self, mImportBends: bool):
        """
        Setter for property: (bool) ImportBends
         Returns the flag indicating whether to import bends.  
             
         
        """
        pass
    @property
    def ImportExportFlexBent(self) -> PreferencesBuilder.ImportExportFlexBentType:
        """
        Getter for property: ( PreferencesBuilder.ImportExportFlexBentType NXOpen.P) ImportExportFlexBent
         Returns the defining state for flags of whether to import andor export flexible printed circuit boards in their bent state instead of their flat state.  
             
         
        """
        pass
    @ImportExportFlexBent.setter
    def ImportExportFlexBent(self, importExportFlexBent: PreferencesBuilder.ImportExportFlexBentType):
        """
        Setter for property: ( PreferencesBuilder.ImportExportFlexBentType NXOpen.P) ImportExportFlexBent
         Returns the defining state for flags of whether to import andor export flexible printed circuit boards in their bent state instead of their flat state.  
             
         
        """
        pass
    @property
    def ImportGenericMenu(self) -> PreferencesBuilder.ImportGenericMenuTypeName:
        """
        Getter for property: ( PreferencesBuilder.ImportGenericMenuTypeName NXOpen.P) ImportGenericMenu
         Returns the import generic shapes type.  
             
         
        """
        pass
    @ImportGenericMenu.setter
    def ImportGenericMenu(self, mImportGenericMenu: PreferencesBuilder.ImportGenericMenuTypeName):
        """
        Setter for property: ( PreferencesBuilder.ImportGenericMenuTypeName NXOpen.P) ImportGenericMenu
         Returns the import generic shapes type.  
             
         
        """
        pass
    @property
    def ImportGenericToggle(self) -> bool:
        """
        Getter for property: (bool) ImportGenericToggle
         Returns the flag indicating whether to import generic shapes.  
             
         
        """
        pass
    @ImportGenericToggle.setter
    def ImportGenericToggle(self, mImportGenericToggle: bool):
        """
        Setter for property: (bool) ImportGenericToggle
         Returns the flag indicating whether to import generic shapes.  
             
         
        """
        pass
    @property
    def ImportMaskMenu(self) -> PreferencesBuilder.ImportMaskMenuTypeName:
        """
        Getter for property: ( PreferencesBuilder.ImportMaskMenuTypeName NXOpen.P) ImportMaskMenu
         Returns the import mask type.  
             
         
        """
        pass
    @ImportMaskMenu.setter
    def ImportMaskMenu(self, mImportMaskMenu: PreferencesBuilder.ImportMaskMenuTypeName):
        """
        Setter for property: ( PreferencesBuilder.ImportMaskMenuTypeName NXOpen.P) ImportMaskMenu
         Returns the import mask type.  
             
         
        """
        pass
    @property
    def ImportMaskToggle(self) -> bool:
        """
        Getter for property: (bool) ImportMaskToggle
         Returns the flag indicating whether to import masks.  
             
         
        """
        pass
    @ImportMaskToggle.setter
    def ImportMaskToggle(self, mImportMaskToggle: bool):
        """
        Setter for property: (bool) ImportMaskToggle
         Returns the flag indicating whether to import masks.  
             
         
        """
        pass
    @property
    def ImportMasksMethod(self) -> PreferencesBuilder.ImportMasksMethodType:
        """
        Getter for property: ( PreferencesBuilder.ImportMasksMethodType NXOpen.P) ImportMasksMethod
         Returns the flag indicating import masks method.  
             
         
        """
        pass
    @ImportMasksMethod.setter
    def ImportMasksMethod(self, mImportMaskMethod: PreferencesBuilder.ImportMasksMethodType):
        """
        Setter for property: ( PreferencesBuilder.ImportMasksMethodType NXOpen.P) ImportMasksMethod
         Returns the flag indicating import masks method.  
             
         
        """
        pass
    @property
    def ImportPadMenu(self) -> PreferencesBuilder.ImportPadMenuTypeName:
        """
        Getter for property: ( PreferencesBuilder.ImportPadMenuTypeName NXOpen.P) ImportPadMenu
         Returns the import pad type.  
             
         
        """
        pass
    @ImportPadMenu.setter
    def ImportPadMenu(self, mImportPadMenu: PreferencesBuilder.ImportPadMenuTypeName):
        """
        Setter for property: ( PreferencesBuilder.ImportPadMenuTypeName NXOpen.P) ImportPadMenu
         Returns the import pad type.  
             
         
        """
        pass
    @property
    def ImportPadToggle(self) -> bool:
        """
        Getter for property: (bool) ImportPadToggle
         Returns the flag indicating whether to import pads.  
             
         
        """
        pass
    @ImportPadToggle.setter
    def ImportPadToggle(self, mImportPadToggle: bool):
        """
        Setter for property: (bool) ImportPadToggle
         Returns the flag indicating whether to import pads.  
             
         
        """
        pass
    @property
    def ImportPasteMaskMenu(self) -> PreferencesBuilder.ImportMaskMenuTypeName:
        """
        Getter for property: ( PreferencesBuilder.ImportMaskMenuTypeName NXOpen.P) ImportPasteMaskMenu
         Returns the import pastemask type.  
             
         
        """
        pass
    @ImportPasteMaskMenu.setter
    def ImportPasteMaskMenu(self, mImportPasteMaskMenu: PreferencesBuilder.ImportMaskMenuTypeName):
        """
        Setter for property: ( PreferencesBuilder.ImportMaskMenuTypeName NXOpen.P) ImportPasteMaskMenu
         Returns the import pastemask type.  
             
         
        """
        pass
    @property
    def ImportPasteMaskToggle(self) -> bool:
        """
        Getter for property: (bool) ImportPasteMaskToggle
         Returns the flag indicating whether to import pastemasks.  
             
         
        """
        pass
    @ImportPasteMaskToggle.setter
    def ImportPasteMaskToggle(self, mImportPasteMaskToggle: bool):
        """
        Setter for property: (bool) ImportPasteMaskToggle
         Returns the flag indicating whether to import pastemasks.  
             
         
        """
        pass
    @property
    def ImportTraceMenu(self) -> PreferencesBuilder.ImportTraceMenuTypeName:
        """
        Getter for property: ( PreferencesBuilder.ImportTraceMenuTypeName NXOpen.P) ImportTraceMenu
         Returns the import trace type.  
             
         
        """
        pass
    @ImportTraceMenu.setter
    def ImportTraceMenu(self, mImportTraceMenu: PreferencesBuilder.ImportTraceMenuTypeName):
        """
        Setter for property: ( PreferencesBuilder.ImportTraceMenuTypeName NXOpen.P) ImportTraceMenu
         Returns the import trace type.  
             
         
        """
        pass
    @property
    def ImportTraceToggle(self) -> bool:
        """
        Getter for property: (bool) ImportTraceToggle
         Returns the flag indicating whether to import traces.  
             
         
        """
        pass
    @ImportTraceToggle.setter
    def ImportTraceToggle(self, mImportTraceToggle: bool):
        """
        Setter for property: (bool) ImportTraceToggle
         Returns the flag indicating whether to import traces.  
             
         
        """
        pass
    @property
    def ImportWireBondToggle(self) -> bool:
        """
        Getter for property: (bool) ImportWireBondToggle
         Returns the flag indicating whether to import wire bonds.  
             
         
        """
        pass
    @ImportWireBondToggle.setter
    def ImportWireBondToggle(self, mImportWireBondToggle: bool):
        """
        Setter for property: (bool) ImportWireBondToggle
         Returns the flag indicating whether to import wire bonds.  
             
         
        """
        pass
    @property
    def InternalLayers(self) -> bool:
        """
        Getter for property: (bool) InternalLayers
         Returns the flag indicating whether to import internal layers.  
             
         
        """
        pass
    @InternalLayers.setter
    def InternalLayers(self, mInternalLayers: bool):
        """
        Setter for property: (bool) InternalLayers
         Returns the flag indicating whether to import internal layers.  
             
         
        """
        pass
    @property
    def KeepInColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) KeepInColor
         Returns the keepin area color.  
             
         
        """
        pass
    @KeepInColor.setter
    def KeepInColor(self, mKeepInColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) KeepInColor
         Returns the keepin area color.  
             
         
        """
        pass
    @property
    def KeepInLayer(self) -> int:
        """
        Getter for property: (int) KeepInLayer
         Returns the keepin area layer.  
             
         
        """
        pass
    @KeepInLayer.setter
    def KeepInLayer(self, mKeepInLayer: int):
        """
        Setter for property: (int) KeepInLayer
         Returns the keepin area layer.  
             
         
        """
        pass
    @property
    def KeepInTranslucency(self) -> int:
        """
        Getter for property: (int) KeepInTranslucency
         Returns the keepin area translucency.  
             
         
        """
        pass
    @KeepInTranslucency.setter
    def KeepInTranslucency(self, mKeepInTranslucency: int):
        """
        Setter for property: (int) KeepInTranslucency
         Returns the keepin area translucency.  
             
         
        """
        pass
    @property
    def KeepOutColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) KeepOutColor
         Returns the keepout area color.  
             
         
        """
        pass
    @KeepOutColor.setter
    def KeepOutColor(self, mKeepOutColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) KeepOutColor
         Returns the keepout area color.  
             
         
        """
        pass
    @property
    def KeepOutLayer(self) -> int:
        """
        Getter for property: (int) KeepOutLayer
         Returns the keepout area layer.  
             
         
        """
        pass
    @KeepOutLayer.setter
    def KeepOutLayer(self, mKeepOutLayer: int):
        """
        Setter for property: (int) KeepOutLayer
         Returns the keepout area layer.  
             
         
        """
        pass
    @property
    def KeepOutTranslucency(self) -> int:
        """
        Getter for property: (int) KeepOutTranslucency
         Returns the keepout area translucency.  
             
         
        """
        pass
    @KeepOutTranslucency.setter
    def KeepOutTranslucency(self, mKeepOutTranslucency: int):
        """
        Setter for property: (int) KeepOutTranslucency
         Returns the keepout area translucency.  
             
         
        """
        pass
    @property
    def MailNotify(self) -> bool:
        """
        Getter for property: (bool) MailNotify
         Returns the flag indicating whether to send email notifications.  
             
         
        """
        pass
    @MailNotify.setter
    def MailNotify(self, mMailNotify: bool):
        """
        Setter for property: (bool) MailNotify
         Returns the flag indicating whether to send email notifications.  
             
         
        """
        pass
    @property
    def MailProtocol(self) -> PreferencesBuilder.MailProtocolTypeName:
        """
        Getter for property: ( PreferencesBuilder.MailProtocolTypeName NXOpen.P) MailProtocol
         Returns the email protocol.  
             
         
        """
        pass
    @MailProtocol.setter
    def MailProtocol(self, mMailProtocol: PreferencesBuilder.MailProtocolTypeName):
        """
        Setter for property: ( PreferencesBuilder.MailProtocolTypeName NXOpen.P) MailProtocol
         Returns the email protocol.  
             
         
        """
        pass
    @property
    def MaskMaxNumber(self) -> int:
        """
        Getter for property: (int) MaskMaxNumber
         Returns the mask max number.  
             
         
        """
        pass
    @MaskMaxNumber.setter
    def MaskMaxNumber(self, mMaskMaxNumber: int):
        """
        Setter for property: (int) MaskMaxNumber
         Returns the mask max number.  
             
         
        """
        pass
    @property
    def MaskNamePrefix(self) -> str:
        """
        Getter for property: (str) MaskNamePrefix
         Returns the mask name prefix.  
             
         
        """
        pass
    @MaskNamePrefix.setter
    def MaskNamePrefix(self, mMaskNamePrefix: str):
        """
        Setter for property: (str) MaskNamePrefix
         Returns the mask name prefix.  
             
         
        """
        pass
    @property
    def MaskNameSuffix(self) -> str:
        """
        Getter for property: (str) MaskNameSuffix
         Returns the mask name suffix.  
             
         
        """
        pass
    @MaskNameSuffix.setter
    def MaskNameSuffix(self, mMaskNameSuffix: str):
        """
        Setter for property: (str) MaskNameSuffix
         Returns the mask name suffix.  
             
         
        """
        pass
    @property
    def MergeTracesAndPads(self) -> bool:
        """
        Getter for property: (bool) MergeTracesAndPads
         Returns the flag indicating whether to merge traces and pads.  
             
         
        """
        pass
    @MergeTracesAndPads.setter
    def MergeTracesAndPads(self, mMergeTracesAndPads: bool):
        """
        Setter for property: (bool) MergeTracesAndPads
         Returns the flag indicating whether to merge traces and pads.  
             
         
        """
        pass
    @property
    def MergeTracesAndPadsWithEnum(self) -> PreferencesBuilder.MergeTracesAndPadsType:
        """
        Getter for property: ( PreferencesBuilder.MergeTracesAndPadsType NXOpen.P) MergeTracesAndPadsWithEnum
         Returns the flag indicating whether to merge traces andor pads.  
             
         
        """
        pass
    @MergeTracesAndPadsWithEnum.setter
    def MergeTracesAndPadsWithEnum(self, mMergeTracesAndPads: PreferencesBuilder.MergeTracesAndPadsType):
        """
        Setter for property: ( PreferencesBuilder.MergeTracesAndPadsType NXOpen.P) MergeTracesAndPadsWithEnum
         Returns the flag indicating whether to merge traces andor pads.  
             
         
        """
        pass
    @property
    def ModelForStructuralAnalysis(self) -> PreferencesBuilder.ModelForStructuralAnalysisTypeName:
        """
        Getter for property: ( PreferencesBuilder.ModelForStructuralAnalysisTypeName NXOpen.P) ModelForStructuralAnalysis
         Returns the board mesh type for structural analysis.  
             
         
        """
        pass
    @ModelForStructuralAnalysis.setter
    def ModelForStructuralAnalysis(self, mModelForStructuralAnalysis: PreferencesBuilder.ModelForStructuralAnalysisTypeName):
        """
        Setter for property: ( PreferencesBuilder.ModelForStructuralAnalysisTypeName NXOpen.P) ModelForStructuralAnalysis
         Returns the board mesh type for structural analysis.  
             
         
        """
        pass
    @property
    def ModelForThermalAnalysis(self) -> PreferencesBuilder.ModelForThermalAnalysisTypeName:
        """
        Getter for property: ( PreferencesBuilder.ModelForThermalAnalysisTypeName NXOpen.P) ModelForThermalAnalysis
         Returns the board mesh type for thermal analysis.  
             
         
        """
        pass
    @ModelForThermalAnalysis.setter
    def ModelForThermalAnalysis(self, mModelForThermalAnalysis: PreferencesBuilder.ModelForThermalAnalysisTypeName):
        """
        Setter for property: ( PreferencesBuilder.ModelForThermalAnalysisTypeName NXOpen.P) ModelForThermalAnalysis
         Returns the board mesh type for thermal analysis.  
             
         
        """
        pass
    @property
    def MonitorEDMDToggle(self) -> bool:
        """
        Getter for property: (bool) MonitorEDMDToggle
         Returns the flag indicating whether to monitor the EDMD directory.  
             
         
        """
        pass
    @MonitorEDMDToggle.setter
    def MonitorEDMDToggle(self, mMonitorEDMDToggle: bool):
        """
        Setter for property: (bool) MonitorEDMDToggle
         Returns the flag indicating whether to monitor the EDMD directory.  
             
         
        """
        pass
    @property
    def Negative(self) -> bool:
        """
        Getter for property: (bool) Negative
         Returns the flag indicating whether to import the negative copper shapes.  
             
         
        """
        pass
    @Negative.setter
    def Negative(self, mNegative: bool):
        """
        Setter for property: (bool) Negative
         Returns the flag indicating whether to import the negative copper shapes.  
             
         
        """
        pass
    @property
    def OtherColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) OtherColor
         Returns the other area color.  
             
         
        """
        pass
    @OtherColor.setter
    def OtherColor(self, mOtherColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) OtherColor
         Returns the other area color.  
             
         
        """
        pass
    @property
    def OtherLayer(self) -> int:
        """
        Getter for property: (int) OtherLayer
         Returns the other area layer.  
             
         
        """
        pass
    @OtherLayer.setter
    def OtherLayer(self, mOtherLayer: int):
        """
        Setter for property: (int) OtherLayer
         Returns the other area layer.  
             
         
        """
        pass
    @property
    def OtherTranslucency(self) -> int:
        """
        Getter for property: (int) OtherTranslucency
         Returns the other area translucency.  
             
         
        """
        pass
    @OtherTranslucency.setter
    def OtherTranslucency(self, mOtherTranslucency: int):
        """
        Setter for property: (int) OtherTranslucency
         Returns the other area translucency.  
             
         
        """
        pass
    @property
    def PadMaxNumber(self) -> int:
        """
        Getter for property: (int) PadMaxNumber
         Returns the pad max number.  
             
         
        """
        pass
    @PadMaxNumber.setter
    def PadMaxNumber(self, mPadMaxNumber: int):
        """
        Setter for property: (int) PadMaxNumber
         Returns the pad max number.  
             
         
        """
        pass
    @property
    def PadNamePrefix(self) -> str:
        """
        Getter for property: (str) PadNamePrefix
         Returns the pad name prefix.  
             
         
        """
        pass
    @PadNamePrefix.setter
    def PadNamePrefix(self, mPadNamePrefix: str):
        """
        Setter for property: (str) PadNamePrefix
         Returns the pad name prefix.  
             
         
        """
        pass
    @property
    def PadNameSuffix(self) -> str:
        """
        Getter for property: (str) PadNameSuffix
         Returns the pad name suffix.  
             
         
        """
        pass
    @PadNameSuffix.setter
    def PadNameSuffix(self, mPadNameSuffix: str):
        """
        Setter for property: (str) PadNameSuffix
         Returns the pad name suffix.  
             
         
        """
        pass
    @property
    def PasteMaskMaxNumber(self) -> int:
        """
        Getter for property: (int) PasteMaskMaxNumber
         Returns the pastemask max number.  
             
         
        """
        pass
    @PasteMaskMaxNumber.setter
    def PasteMaskMaxNumber(self, mPasteMaskMaxNumber: int):
        """
        Setter for property: (int) PasteMaskMaxNumber
         Returns the pastemask max number.  
             
         
        """
        pass
    @property
    def PasteMaskNamePrefix(self) -> str:
        """
        Getter for property: (str) PasteMaskNamePrefix
         Returns the pastemask name prefix.  
             
         
        """
        pass
    @PasteMaskNamePrefix.setter
    def PasteMaskNamePrefix(self, mPasteMaskNamePrefix: str):
        """
        Setter for property: (str) PasteMaskNamePrefix
         Returns the pastemask name prefix.  
             
         
        """
        pass
    @property
    def PasteMaskNameSuffix(self) -> str:
        """
        Getter for property: (str) PasteMaskNameSuffix
         Returns the pastemask name suffix.  
             
         
        """
        pass
    @PasteMaskNameSuffix.setter
    def PasteMaskNameSuffix(self, mPasteMaskNameSuffix: str):
        """
        Setter for property: (str) PasteMaskNameSuffix
         Returns the pastemask name suffix.  
             
         
        """
        pass
    @property
    def PcaNamePrefix(self) -> str:
        """
        Getter for property: (str) PcaNamePrefix
         Returns the PCA name prefix.  
             
         
        """
        pass
    @PcaNamePrefix.setter
    def PcaNamePrefix(self, mPcaNamePrefix: str):
        """
        Setter for property: (str) PcaNamePrefix
         Returns the PCA name prefix.  
             
         
        """
        pass
    @property
    def PcaNameSuffix(self) -> str:
        """
        Getter for property: (str) PcaNameSuffix
         Returns the PCA name suffix.  
             
         
        """
        pass
    @PcaNameSuffix.setter
    def PcaNameSuffix(self, mPcaNameSuffix: str):
        """
        Setter for property: (str) PcaNameSuffix
         Returns the PCA name suffix.  
             
         
        """
        pass
    @property
    def ProjectView(self) -> str:
        """
        Getter for property: (str) ProjectView
         Returns the project view.  
             
         
        """
        pass
    @ProjectView.setter
    def ProjectView(self, mProjectView: str):
        """
        Setter for property: (str) ProjectView
         Returns the project view.  
             
         
        """
        pass
    @property
    def ProjectViewToggle(self) -> bool:
        """
        Getter for property: (bool) ProjectViewToggle
         Returns the flag indicating whether to project the view.  
             
         
        """
        pass
    @ProjectViewToggle.setter
    def ProjectViewToggle(self, mProjectViewToggle: bool):
        """
        Setter for property: (bool) ProjectViewToggle
         Returns the flag indicating whether to project the view.  
             
         
        """
        pass
    @property
    def ReadWriteDir(self) -> str:
        """
        Getter for property: (str) ReadWriteDir
         Returns the readwrite directory.  
             
         
        """
        pass
    @ReadWriteDir.setter
    def ReadWriteDir(self, foldername: str):
        """
        Setter for property: (str) ReadWriteDir
         Returns the readwrite directory.  
             
         
        """
        pass
    @property
    def ResistorModel(self) -> PreferencesBuilder.ResistorModelTypeName:
        """
        Getter for property: ( PreferencesBuilder.ResistorModelTypeName NXOpen.P) ResistorModel
         Returns the resistor model for thermal analysis.  
             
         
        """
        pass
    @ResistorModel.setter
    def ResistorModel(self, mComponentsModel: PreferencesBuilder.ResistorModelTypeName):
        """
        Setter for property: ( PreferencesBuilder.ResistorModelTypeName NXOpen.P) ResistorModel
         Returns the resistor model for thermal analysis.  
             
         
        """
        pass
    @property
    def RevisionRule(self) -> int:
        """
        Getter for property: (int) RevisionRule
         Returns the revision rule.  
             
         
        """
        pass
    @RevisionRule.setter
    def RevisionRule(self, revisionRule: int):
        """
        Setter for property: (int) RevisionRule
         Returns the revision rule.  
             
         
        """
        pass
    @property
    def SettingsSource(self) -> PreferencesBuilder.SettingsSourceTypeName:
        """
        Getter for property: ( PreferencesBuilder.SettingsSourceTypeName NXOpen.P) SettingsSource
         Returns the settings source.  
             
         
        """
        pass
    @SettingsSource.setter
    def SettingsSource(self, mDefaultSettingsSources: PreferencesBuilder.SettingsSourceTypeName):
        """
        Setter for property: ( PreferencesBuilder.SettingsSourceTypeName NXOpen.P) SettingsSource
         Returns the settings source.  
             
         
        """
        pass
    @property
    def SpecifiedSettingsFolder(self) -> str:
        """
        Getter for property: (str) SpecifiedSettingsFolder
         Returns the ini directory.  
             
         
        """
        pass
    @SpecifiedSettingsFolder.setter
    def SpecifiedSettingsFolder(self, settingsFolder: str):
        """
        Setter for property: (str) SpecifiedSettingsFolder
         Returns the ini directory.  
             
         
        """
        pass
    @property
    def SpecifyNewCompDir(self) -> str:
        """
        Getter for property: (str) SpecifyNewCompDir
         Returns the directory where new components are created if the option is 'Specify'.  
             
         
        """
        pass
    @SpecifyNewCompDir.setter
    def SpecifyNewCompDir(self, mSpecifyNewCompDir: str):
        """
        Setter for property: (str) SpecifyNewCompDir
         Returns the directory where new components are created if the option is 'Specify'.  
             
         
        """
        pass
    @property
    def StructuralAlgorithm(self) -> PreferencesBuilder.StructuralAlgorithmTypeName:
        """
        Getter for property: ( PreferencesBuilder.StructuralAlgorithmTypeName NXOpen.P) StructuralAlgorithm
         Returns the algorithm to calculate board properties for structural analysis.  
             
         
        """
        pass
    @StructuralAlgorithm.setter
    def StructuralAlgorithm(self, mStructuralAlgorithm: PreferencesBuilder.StructuralAlgorithmTypeName):
        """
        Setter for property: ( PreferencesBuilder.StructuralAlgorithmTypeName NXOpen.P) StructuralAlgorithm
         Returns the algorithm to calculate board properties for structural analysis.  
             
         
        """
        pass
    @property
    def TempBoardLayer(self) -> int:
        """
        Getter for property: (int) TempBoardLayer
         Returns the temporary board layer.  
             
         
        """
        pass
    @TempBoardLayer.setter
    def TempBoardLayer(self, tempBoardLayer: int):
        """
        Setter for property: (int) TempBoardLayer
         Returns the temporary board layer.  
             
         
        """
        pass
    @property
    def ThermalAlgorithm(self) -> PreferencesBuilder.ThermalAlgorithmTypeName:
        """
        Getter for property: ( PreferencesBuilder.ThermalAlgorithmTypeName NXOpen.P) ThermalAlgorithm
         Returns the algorithm to calculate board properties for thermal analysis.  
             
         
        """
        pass
    @ThermalAlgorithm.setter
    def ThermalAlgorithm(self, mThermalAlgorithm: PreferencesBuilder.ThermalAlgorithmTypeName):
        """
        Setter for property: ( PreferencesBuilder.ThermalAlgorithmTypeName NXOpen.P) ThermalAlgorithm
         Returns the algorithm to calculate board properties for thermal analysis.  
             
         
        """
        pass
    @property
    def ThicknessForStructuralAnalysis(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThicknessForStructuralAnalysis
         Returns the board thickness for structural analysis when the thickness source is "Specify".  
             
         
        """
        pass
    @property
    def ThicknessSourceForStructuralAnalysis(self) -> PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName:
        """
        Getter for property: ( PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName NXOpen.P) ThicknessSourceForStructuralAnalysis
         Returns the thickness source for structural analysis.  
             
         
        """
        pass
    @ThicknessSourceForStructuralAnalysis.setter
    def ThicknessSourceForStructuralAnalysis(self, mThicknessSourceForStructuralAnalysis: PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName):
        """
        Setter for property: ( PreferencesBuilder.ThicknessSourceForStructuralAnalysisTypeName NXOpen.P) ThicknessSourceForStructuralAnalysis
         Returns the thickness source for structural analysis.  
             
         
        """
        pass
    @property
    def TraceMaxNumber(self) -> int:
        """
        Getter for property: (int) TraceMaxNumber
         Returns the trace max number.  
             
         
        """
        pass
    @TraceMaxNumber.setter
    def TraceMaxNumber(self, mTraceMaxNumber: int):
        """
        Setter for property: (int) TraceMaxNumber
         Returns the trace max number.  
             
         
        """
        pass
    @property
    def TraceNamePrefix(self) -> str:
        """
        Getter for property: (str) TraceNamePrefix
         Returns the trace name prefix.  
             
         
        """
        pass
    @TraceNamePrefix.setter
    def TraceNamePrefix(self, mTraceNamePrefix: str):
        """
        Setter for property: (str) TraceNamePrefix
         Returns the trace name prefix.  
             
         
        """
        pass
    @property
    def TraceNameSuffix(self) -> str:
        """
        Getter for property: (str) TraceNameSuffix
         Returns the trace name suffix.  
             
         
        """
        pass
    @TraceNameSuffix.setter
    def TraceNameSuffix(self, mtraceNameSuffix: str):
        """
        Setter for property: (str) TraceNameSuffix
         Returns the trace name suffix.  
             
         
        """
        pass
    @property
    def UseRevisionRule(self) -> bool:
        """
        Getter for property: (bool) UseRevisionRule
         Returns the flag indicating whether or not to use additional revision rule.  
             
         
        """
        pass
    @UseRevisionRule.setter
    def UseRevisionRule(self, useRevisionRule: bool):
        """
        Setter for property: (bool) UseRevisionRule
         Returns the flag indicating whether or not to use additional revision rule.  
             
         
        """
        pass
    def EditComponentSimulationDatabase(self) -> None:
        """
         Edits the component simulation database. 
        """
        pass
    def GetAreaMapping(self) -> AreaMapping:
        """
         Gets the area mapping. 
         Returns areaMapping ( AreaMapping NXOpen.P): .
        """
        pass
    def GetEcadEntityFilter(self) -> EntityFilter:
        """
         Gets the ECAD entity filter. 
         Returns filter ( EntityFilter NXOpen.P): .
        """
        pass
    def GetMailRecipients(self) -> List[str]:
        """
         Returns the email recipients. 
         Returns mMailRecipients (List[str]): .
        """
        pass
    def GetMcadEntityFilter(self) -> EntityFilter:
        """
         Gets the MCAD entity filter. 
         Returns filter ( EntityFilter NXOpen.P): .
        """
        pass
    def RefreshSettings(self) -> None:
        """
         Refreshs PCB settings. 
        """
        pass
    def SetAreaMapping(self, areaMapping: AreaMapping) -> None:
        """
         Sets the area mapping. 
        """
        pass
    def SetEcadEntityFilter(self, filter: EntityFilter) -> None:
        """
         Sets the ECAD entity filter. 
        """
        pass
    def SetMailRecipients(self, mMailRecipients: List[str]) -> None:
        """
         Sets the email recipients. 
        """
        pass
    def SetMcadEntityFilter(self, filter: EntityFilter) -> None:
        """
         Sets the MCAD entity filter. 
        """
        pass
import NXOpen
class PrimaryPinsVisualizeBuilder(NXOpen.Builder): 
    """ Represents a builder to visualize primary pins. """
    @property
    def Components(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Components
         Returns the components.  
             
         
        """
        pass
    @property
    def ShowInfoWindow(self) -> bool:
        """
        Getter for property: (bool) ShowInfoWindow
         Returns the flag indicating whether to show the information window.  
             
         
        """
        pass
    @ShowInfoWindow.setter
    def ShowInfoWindow(self, showInfoWindow: bool):
        """
        Setter for property: (bool) ShowInfoWindow
         Returns the flag indicating whether to show the information window.  
             
         
        """
        pass
    def DisplayPrimaryPins(self, isDisplayed: bool) -> None:
        """
         Shows or hides the selected components' primary pins. 
        """
        pass
import NXOpen
class ReportBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.PcbExchange.ReportBuilder. """
    class TypeEnum(Enum):
        """
        Members Include: 
         |Validation| 
         |LightweightValidation| 
         |Component| 
         |ThermalDatabase| 
         |PanelValidation| 

        """
        Validation: int
        LightweightValidation: int
        Component: int
        ThermalDatabase: int
        PanelValidation: int
        @staticmethod
        def ValueOf(value: int) -> ReportBuilder.TypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ReportType(self) -> ReportBuilder.TypeEnum:
        """
        Getter for property: ( ReportBuilder.TypeEnum NXOpen.P) ReportType
         Returns the report type.  
             
         
        """
        pass
    @ReportType.setter
    def ReportType(self, type: ReportBuilder.TypeEnum):
        """
        Setter for property: ( ReportBuilder.TypeEnum NXOpen.P) ReportType
         Returns the report type.  
             
         
        """
        pass
import NXOpen
class StructuralSolutionBuilder(NXOpen.Builder): 
    """ Represents a builder to create a structural solution. """
    class ActionOption(Enum):
        """
        Members Include: 
         |CreateSolution| 
         |UpdateSolution| 

        """
        CreateSolution: int
        UpdateSolution: int
        @staticmethod
        def ValueOf(value: int) -> StructuralSolutionBuilder.ActionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SolutionTypeOption(Enum):
        """
        Members Include: 
         |LinearStatics| 
         |NormalModes| 

        """
        LinearStatics: int
        NormalModes: int
        @staticmethod
        def ValueOf(value: int) -> StructuralSolutionBuilder.SolutionTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UpdateOption(Enum):
        """
        Members Include: 
         |UpdateComponents| 
         |UpdatePCB| 

        """
        UpdateComponents: int
        UpdatePCB: int
        @staticmethod
        def ValueOf(value: int) -> StructuralSolutionBuilder.UpdateOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Action(self) -> StructuralSolutionBuilder.ActionOption:
        """
        Getter for property: ( StructuralSolutionBuilder.ActionOption NXOpen.P) Action
         Returns the action.  
             
         
        """
        pass
    @Action.setter
    def Action(self, action: StructuralSolutionBuilder.ActionOption):
        """
        Setter for property: ( StructuralSolutionBuilder.ActionOption NXOpen.P) Action
         Returns the action.  
             
         
        """
        pass
    @property
    def BoardPropertiesFile(self) -> str:
        """
        Getter for property: (str) BoardPropertiesFile
         Returns the board properties file.  
             
         
        """
        pass
    @BoardPropertiesFile.setter
    def BoardPropertiesFile(self, file: str):
        """
        Setter for property: (str) BoardPropertiesFile
         Returns the board properties file.  
             
         
        """
        pass
    @property
    def ComponentSimulationDataFile(self) -> str:
        """
        Getter for property: (str) ComponentSimulationDataFile
         Returns the component simulation database.  
             
         
        """
        pass
    @ComponentSimulationDataFile.setter
    def ComponentSimulationDataFile(self, file: str):
        """
        Setter for property: (str) ComponentSimulationDataFile
         Returns the component simulation database.  
             
         
        """
        pass
    @property
    def CreateHoleConstraints(self) -> bool:
        """
        Getter for property: (bool) CreateHoleConstraints
         Returns the flag indicating whether to create hole constraints.  
             
         
        """
        pass
    @CreateHoleConstraints.setter
    def CreateHoleConstraints(self, isCreateHoleConstraints: bool):
        """
        Setter for property: (bool) CreateHoleConstraints
         Returns the flag indicating whether to create hole constraints.  
             
         
        """
        pass
    @property
    def CreateIdealizedPart(self) -> bool:
        """
        Getter for property: (bool) CreateIdealizedPart
         Returns the flag indicating whether to create an idealized part.  
             
         
        """
        pass
    @CreateIdealizedPart.setter
    def CreateIdealizedPart(self, isCreate: bool):
        """
        Setter for property: (bool) CreateIdealizedPart
         Returns the flag indicating whether to create an idealized part.  
             
         
        """
        pass
    @property
    def ElementStartLabel(self) -> int:
        """
        Getter for property: (int) ElementStartLabel
         Returns the element start label.  
             
         
        """
        pass
    @ElementStartLabel.setter
    def ElementStartLabel(self, start: int):
        """
        Setter for property: (int) ElementStartLabel
         Returns the element start label.  
             
         
        """
        pass
    @property
    def FemFile(self) -> str:
        """
        Getter for property: (str) FemFile
         Returns the fem file.  
             
         
        """
        pass
    @FemFile.setter
    def FemFile(self, file: str):
        """
        Setter for property: (str) FemFile
         Returns the fem file.  
             
         
        """
        pass
    @property
    def FemName(self) -> str:
        """
        Getter for property: (str) FemName
         Returns the fem file name.  
             
         
        """
        pass
    @FemName.setter
    def FemName(self, femName: str):
        """
        Setter for property: (str) FemName
         Returns the fem file name.  
             
         
        """
        pass
    @property
    def FemNumber(self) -> str:
        """
        Getter for property: (str) FemNumber
         Returns the fem file number.  
             
         
        """
        pass
    @FemNumber.setter
    def FemNumber(self, femNumber: str):
        """
        Setter for property: (str) FemNumber
         Returns the fem file number.  
             
         
        """
        pass
    @property
    def FemRevision(self) -> str:
        """
        Getter for property: (str) FemRevision
         Returns the fem file revision.  
             
         
        """
        pass
    @FemRevision.setter
    def FemRevision(self, femRevision: str):
        """
        Setter for property: (str) FemRevision
         Returns the fem file revision.  
             
         
        """
        pass
    @property
    def Folder(self) -> str:
        """
        Getter for property: (str) Folder
         Returns the simulation items folder.  
             
         
        """
        pass
    @Folder.setter
    def Folder(self, folderName: str):
        """
        Setter for property: (str) Folder
         Returns the simulation items folder.  
             
         
        """
        pass
    @property
    def IPartFile(self) -> str:
        """
        Getter for property: (str) IPartFile
         Returns the idealized part file.  
             
         
        """
        pass
    @IPartFile.setter
    def IPartFile(self, file: str):
        """
        Setter for property: (str) IPartFile
         Returns the idealized part file.  
             
         
        """
        pass
    @property
    def IPartName(self) -> str:
        """
        Getter for property: (str) IPartName
         Returns the i-part file name.  
             
         
        """
        pass
    @IPartName.setter
    def IPartName(self, iPartName: str):
        """
        Setter for property: (str) IPartName
         Returns the i-part file name.  
             
         
        """
        pass
    @property
    def IPartNumber(self) -> str:
        """
        Getter for property: (str) IPartNumber
         Returns the i-part file number.  
             
         
        """
        pass
    @IPartNumber.setter
    def IPartNumber(self, iPartNumber: str):
        """
        Setter for property: (str) IPartNumber
         Returns the i-part file number.  
             
         
        """
        pass
    @property
    def IPartRevision(self) -> str:
        """
        Getter for property: (str) IPartRevision
         Returns the i-part file revision.  
             
         
        """
        pass
    @IPartRevision.setter
    def IPartRevision(self, iPartRevision: str):
        """
        Setter for property: (str) IPartRevision
         Returns the i-part file revision.  
             
         
        """
        pass
    @property
    def NodeStartLabel(self) -> int:
        """
        Getter for property: (int) NodeStartLabel
         Returns the node start label.  
             
         
        """
        pass
    @NodeStartLabel.setter
    def NodeStartLabel(self, start: int):
        """
        Setter for property: (int) NodeStartLabel
         Returns the node start label.  
             
         
        """
        pass
    @property
    def SimName(self) -> str:
        """
        Getter for property: (str) SimName
         Returns the simulation file name.  
             
         
        """
        pass
    @SimName.setter
    def SimName(self, simName: str):
        """
        Setter for property: (str) SimName
         Returns the simulation file name.  
             
         
        """
        pass
    @property
    def SimNumber(self) -> str:
        """
        Getter for property: (str) SimNumber
         Returns the simulation file number.  
             
         
        """
        pass
    @SimNumber.setter
    def SimNumber(self, simNumber: str):
        """
        Setter for property: (str) SimNumber
         Returns the simulation file number.  
             
         
        """
        pass
    @property
    def SimRevision(self) -> str:
        """
        Getter for property: (str) SimRevision
         Returns the simulation file revision.  
             
         
        """
        pass
    @SimRevision.setter
    def SimRevision(self, simRevision: str):
        """
        Setter for property: (str) SimRevision
         Returns the simulation file revision.  
             
         
        """
        pass
    @property
    def SimulationFile(self) -> str:
        """
        Getter for property: (str) SimulationFile
         Returns the simulation file.  
             
         
        """
        pass
    @SimulationFile.setter
    def SimulationFile(self, file: str):
        """
        Setter for property: (str) SimulationFile
         Returns the simulation file.  
             
         
        """
        pass
    @property
    def SolutionType(self) -> StructuralSolutionBuilder.SolutionTypeOption:
        """
        Getter for property: ( StructuralSolutionBuilder.SolutionTypeOption NXOpen.P) SolutionType
         Returns the solution type.  
             
         
        """
        pass
    @SolutionType.setter
    def SolutionType(self, type: StructuralSolutionBuilder.SolutionTypeOption):
        """
        Setter for property: ( StructuralSolutionBuilder.SolutionTypeOption NXOpen.P) SolutionType
         Returns the solution type.  
             
         
        """
        pass
    @property
    def UpdateType(self) -> StructuralSolutionBuilder.UpdateOption:
        """
        Getter for property: ( StructuralSolutionBuilder.UpdateOption NXOpen.P) UpdateType
         Returns the update type.  
             
         
        """
        pass
    @UpdateType.setter
    def UpdateType(self, type: StructuralSolutionBuilder.UpdateOption):
        """
        Setter for property: ( StructuralSolutionBuilder.UpdateOption NXOpen.P) UpdateType
         Returns the update type.  
             
         
        """
        pass
    @property
    def UseBoardPropertiesFile(self) -> bool:
        """
        Getter for property: (bool) UseBoardPropertiesFile
         Returns the flag indicating whether to use a board properties file.  
             
         
        """
        pass
    @UseBoardPropertiesFile.setter
    def UseBoardPropertiesFile(self, isUseFile: bool):
        """
        Setter for property: (bool) UseBoardPropertiesFile
         Returns the flag indicating whether to use a board properties file.  
             
         
        """
        pass
    @property
    def UseComponentSimulationData(self) -> bool:
        """
        Getter for property: (bool) UseComponentSimulationData
         Returns the flag indicating whether to use a component simulation database.  
             
         
        """
        pass
    @UseComponentSimulationData.setter
    def UseComponentSimulationData(self, isUseDatabase: bool):
        """
        Setter for property: (bool) UseComponentSimulationData
         Returns the flag indicating whether to use a component simulation database.  
             
         
        """
        pass
    @property
    def UseEntityFilter(self) -> bool:
        """
        Getter for property: (bool) UseEntityFilter
         Returns the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    @UseEntityFilter.setter
    def UseEntityFilter(self, isUseFilter: bool):
        """
        Setter for property: (bool) UseEntityFilter
         Returns the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    def AssignPartNumberAndRevisions(self) -> Tuple[str, str, str, str, str, str]:
        """
         Automatically assign item number and revision for simulation, fem and i-part files. 
         Returns A tuple consisting of (simNumber, simRevision, femNumber, femRevision, iPartNumber, iPartRevision). 
         - simNumber is: str.
         - simRevision is: str.
         - femNumber is: str.
         - femRevision is: str.
         - iPartNumber is: str.
         - iPartRevision is: str.

        """
        pass
    def EditComponentSimulationDatabase(self) -> None:
        """
         Edits the component simulation database. 
        """
        pass
    def GetEntityFilter(self) -> EntityFilter:
        """
         Gets the entity filter. 
         Returns filter ( EntityFilter NXOpen.P): .
        """
        pass
    def SetEntityFilter(self, filter: EntityFilter) -> None:
        """
         Sets the entity filter. 
        """
        pass
import NXOpen
class TemplateBuilder(NXOpen.Builder): 
    """ Represents a builder to create or edit template. """
    @property
    def AreaItemType(self) -> str:
        """
        Getter for property: (str) AreaItemType
         Returns the area item type.  
             
         
        """
        pass
    @AreaItemType.setter
    def AreaItemType(self, itemType: str):
        """
        Setter for property: (str) AreaItemType
         Returns the area item type.  
             
         
        """
        pass
    @property
    def AreaTemplate(self) -> int:
        """
        Getter for property: (int) AreaTemplate
         Returns the area template.  
             
         
        """
        pass
    @AreaTemplate.setter
    def AreaTemplate(self, areaTemplate: int):
        """
        Setter for property: (int) AreaTemplate
         Returns the area template.  
             
         
        """
        pass
    @property
    def AssemblyItemType(self) -> str:
        """
        Getter for property: (str) AssemblyItemType
         Returns the assembly item type.  
             
         
        """
        pass
    @AssemblyItemType.setter
    def AssemblyItemType(self, itemType: str):
        """
        Setter for property: (str) AssemblyItemType
         Returns the assembly item type.  
             
         
        """
        pass
    @property
    def AssemblyTemplate(self) -> int:
        """
        Getter for property: (int) AssemblyTemplate
         Returns the assembly template.  
             
         
        """
        pass
    @AssemblyTemplate.setter
    def AssemblyTemplate(self, assemblyTemplate: int):
        """
        Setter for property: (int) AssemblyTemplate
         Returns the assembly template.  
             
         
        """
        pass
    @property
    def BoardItemType(self) -> str:
        """
        Getter for property: (str) BoardItemType
         Returns the board item type.  
             
         
        """
        pass
    @BoardItemType.setter
    def BoardItemType(self, itemType: str):
        """
        Setter for property: (str) BoardItemType
         Returns the board item type.  
             
         
        """
        pass
    @property
    def BoardTemplate(self) -> int:
        """
        Getter for property: (int) BoardTemplate
         Returns the board template.  
             
         
        """
        pass
    @BoardTemplate.setter
    def BoardTemplate(self, boardTemplate: int):
        """
        Setter for property: (int) BoardTemplate
         Returns the board template.  
             
         
        """
        pass
    @property
    def ComponentItemType(self) -> str:
        """
        Getter for property: (str) ComponentItemType
         Returns the component item type.  
             
         
        """
        pass
    @ComponentItemType.setter
    def ComponentItemType(self, itemType: str):
        """
        Setter for property: (str) ComponentItemType
         Returns the component item type.  
             
         
        """
        pass
    @property
    def ComponentTemplate(self) -> int:
        """
        Getter for property: (int) ComponentTemplate
         Returns the component template.  
             
         
        """
        pass
    @ComponentTemplate.setter
    def ComponentTemplate(self, componentTemplate: int):
        """
        Setter for property: (int) ComponentTemplate
         Returns the component template.  
             
         
        """
        pass
    @property
    def FemItemType(self) -> str:
        """
        Getter for property: (str) FemItemType
         Returns the fem item type.  
             
         
        """
        pass
    @FemItemType.setter
    def FemItemType(self, itemType: str):
        """
        Setter for property: (str) FemItemType
         Returns the fem item type.  
             
         
        """
        pass
    @property
    def FemTemplate(self) -> int:
        """
        Getter for property: (int) FemTemplate
         Returns the fem template.  
             
         
        """
        pass
    @FemTemplate.setter
    def FemTemplate(self, femTemplate: int):
        """
        Setter for property: (int) FemTemplate
         Returns the fem template.  
             
         
        """
        pass
    @property
    def SimItemType(self) -> str:
        """
        Getter for property: (str) SimItemType
         Returns the sim item type.  
             
         
        """
        pass
    @SimItemType.setter
    def SimItemType(self, itemType: str):
        """
        Setter for property: (str) SimItemType
         Returns the sim item type.  
             
         
        """
        pass
    @property
    def SimTemplate(self) -> int:
        """
        Getter for property: (int) SimTemplate
         Returns the sim template.  
             
         
        """
        pass
    @SimTemplate.setter
    def SimTemplate(self, simTemplate: int):
        """
        Setter for property: (int) SimTemplate
         Returns the sim template.  
             
         
        """
        pass
    @property
    def SubAssemblyItemType(self) -> str:
        """
        Getter for property: (str) SubAssemblyItemType
         Returns the subassembly item type.  
             
         
        """
        pass
    @SubAssemblyItemType.setter
    def SubAssemblyItemType(self, itemType: str):
        """
        Setter for property: (str) SubAssemblyItemType
         Returns the subassembly item type.  
             
         
        """
        pass
    @property
    def SubAssemblyTemplate(self) -> int:
        """
        Getter for property: (int) SubAssemblyTemplate
         Returns the subassembly template.  
             
         
        """
        pass
    @SubAssemblyTemplate.setter
    def SubAssemblyTemplate(self, subAssemblyTemplate: int):
        """
        Setter for property: (int) SubAssemblyTemplate
         Returns the subassembly template.  
             
         
        """
        pass
import NXOpen
class ThermalSolutionBuilder(NXOpen.Builder): 
    """ Represents a builder to create a thermal solution. """
    class ActionOption(Enum):
        """
        Members Include: 
         |CreateSolution| 
         |UpdateSolution| 

        """
        CreateSolution: int
        UpdateSolution: int
        @staticmethod
        def ValueOf(value: int) -> ThermalSolutionBuilder.ActionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BoundaryConditionOption(Enum):
        """
        Members Include: 
         |NotSet| 
         |Thermal| 

        """
        NotSet: int
        Thermal: int
        @staticmethod
        def ValueOf(value: int) -> ThermalSolutionBuilder.BoundaryConditionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MeshOption(Enum):
        """
        Members Include: 
         |Board| 
         |BoardComponents| 

        """
        Board: int
        BoardComponents: int
        @staticmethod
        def ValueOf(value: int) -> ThermalSolutionBuilder.MeshOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SolutionTypeOption(Enum):
        """
        Members Include: 
         |Thermal| 
         |ElectronicSystemsCooling| 
         |SpaceSystemsThermal| 
         |Floefd| 

        """
        Thermal: int
        ElectronicSystemsCooling: int
        SpaceSystemsThermal: int
        Floefd: int
        @staticmethod
        def ValueOf(value: int) -> ThermalSolutionBuilder.SolutionTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UpdateOption(Enum):
        """
        Members Include: 
         |UpdateComponents| 
         |UpdatePCB| 

        """
        UpdateComponents: int
        UpdatePCB: int
        @staticmethod
        def ValueOf(value: int) -> ThermalSolutionBuilder.UpdateOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Action(self) -> ThermalSolutionBuilder.ActionOption:
        """
        Getter for property: ( ThermalSolutionBuilder.ActionOption NXOpen.P) Action
         Returns the action.  
             
         
        """
        pass
    @Action.setter
    def Action(self, action: ThermalSolutionBuilder.ActionOption):
        """
        Setter for property: ( ThermalSolutionBuilder.ActionOption NXOpen.P) Action
         Returns the action.  
             
         
        """
        pass
    @property
    def BoardThermalConductivityFile(self) -> str:
        """
        Getter for property: (str) BoardThermalConductivityFile
         Returns the board thermal conductivity file.  
             
         
        """
        pass
    @BoardThermalConductivityFile.setter
    def BoardThermalConductivityFile(self, dir: str):
        """
        Setter for property: (str) BoardThermalConductivityFile
         Returns the board thermal conductivity file.  
             
         
        """
        pass
    @property
    def BoundaryConditionType(self) -> ThermalSolutionBuilder.BoundaryConditionOption:
        """
        Getter for property: ( ThermalSolutionBuilder.BoundaryConditionOption NXOpen.P) BoundaryConditionType
         Returns the boundary condition type.  
             
         
        """
        pass
    @BoundaryConditionType.setter
    def BoundaryConditionType(self, type: ThermalSolutionBuilder.BoundaryConditionOption):
        """
        Setter for property: ( ThermalSolutionBuilder.BoundaryConditionOption NXOpen.P) BoundaryConditionType
         Returns the boundary condition type.  
             
         
        """
        pass
    @property
    def ComponentSimulationDataFile(self) -> str:
        """
        Getter for property: (str) ComponentSimulationDataFile
         Returns the component simulation database.  
             
         
        """
        pass
    @ComponentSimulationDataFile.setter
    def ComponentSimulationDataFile(self, file: str):
        """
        Setter for property: (str) ComponentSimulationDataFile
         Returns the component simulation database.  
             
         
        """
        pass
    @property
    def CreateIdealizedPart(self) -> bool:
        """
        Getter for property: (bool) CreateIdealizedPart
         Returns the flag indicating whether to create an idealized part.  
             
         
        """
        pass
    @CreateIdealizedPart.setter
    def CreateIdealizedPart(self, isIPartCreated: bool):
        """
        Setter for property: (bool) CreateIdealizedPart
         Returns the flag indicating whether to create an idealized part.  
             
         
        """
        pass
    @property
    def ElementStartLabel(self) -> int:
        """
        Getter for property: (int) ElementStartLabel
         Returns the element start label.  
             
         
        """
        pass
    @ElementStartLabel.setter
    def ElementStartLabel(self, start: int):
        """
        Setter for property: (int) ElementStartLabel
         Returns the element start label.  
             
         
        """
        pass
    @property
    def FemFile(self) -> str:
        """
        Getter for property: (str) FemFile
         Returns the fem file.  
             
         
        """
        pass
    @FemFile.setter
    def FemFile(self, file: str):
        """
        Setter for property: (str) FemFile
         Returns the fem file.  
             
         
        """
        pass
    @property
    def FemName(self) -> str:
        """
        Getter for property: (str) FemName
         Returns the fem file name.  
             
         
        """
        pass
    @FemName.setter
    def FemName(self, femName: str):
        """
        Setter for property: (str) FemName
         Returns the fem file name.  
             
         
        """
        pass
    @property
    def FemNumber(self) -> str:
        """
        Getter for property: (str) FemNumber
         Returns the fem file number.  
             
         
        """
        pass
    @FemNumber.setter
    def FemNumber(self, femNumber: str):
        """
        Setter for property: (str) FemNumber
         Returns the fem file number.  
             
         
        """
        pass
    @property
    def FemRevision(self) -> str:
        """
        Getter for property: (str) FemRevision
         Returns the fem file revision.  
             
         
        """
        pass
    @FemRevision.setter
    def FemRevision(self, femRevision: str):
        """
        Setter for property: (str) FemRevision
         Returns the fem file revision.  
             
         
        """
        pass
    @property
    def Folder(self) -> str:
        """
        Getter for property: (str) Folder
         Returns the simulation items folder.  
             
         
        """
        pass
    @Folder.setter
    def Folder(self, folderName: str):
        """
        Setter for property: (str) Folder
         Returns the simulation items folder.  
             
         
        """
        pass
    @property
    def IPartFile(self) -> str:
        """
        Getter for property: (str) IPartFile
         Returns the idealized part file.  
             
         
        """
        pass
    @IPartFile.setter
    def IPartFile(self, file: str):
        """
        Setter for property: (str) IPartFile
         Returns the idealized part file.  
             
         
        """
        pass
    @property
    def IPartName(self) -> str:
        """
        Getter for property: (str) IPartName
         Returns the i-part file name.  
             
         
        """
        pass
    @IPartName.setter
    def IPartName(self, iPartName: str):
        """
        Setter for property: (str) IPartName
         Returns the i-part file name.  
             
         
        """
        pass
    @property
    def IPartNumber(self) -> str:
        """
        Getter for property: (str) IPartNumber
         Returns the i-part file number.  
             
         
        """
        pass
    @IPartNumber.setter
    def IPartNumber(self, iPartNumber: str):
        """
        Setter for property: (str) IPartNumber
         Returns the i-part file number.  
             
         
        """
        pass
    @property
    def IPartRevision(self) -> str:
        """
        Getter for property: (str) IPartRevision
         Returns the i-part file revision.  
             
         
        """
        pass
    @IPartRevision.setter
    def IPartRevision(self, iPartRevision: str):
        """
        Setter for property: (str) IPartRevision
         Returns the i-part file revision.  
             
         
        """
        pass
    @property
    def MeshType(self) -> ThermalSolutionBuilder.MeshOption:
        """
        Getter for property: ( ThermalSolutionBuilder.MeshOption NXOpen.P) MeshType
         Returns the mesh type.  
             
         
        """
        pass
    @MeshType.setter
    def MeshType(self, type: ThermalSolutionBuilder.MeshOption):
        """
        Setter for property: ( ThermalSolutionBuilder.MeshOption NXOpen.P) MeshType
         Returns the mesh type.  
             
         
        """
        pass
    @property
    def NodeStartLabel(self) -> int:
        """
        Getter for property: (int) NodeStartLabel
         Returns the node start label.  
             
         
        """
        pass
    @NodeStartLabel.setter
    def NodeStartLabel(self, start: int):
        """
        Setter for property: (int) NodeStartLabel
         Returns the node start label.  
             
         
        """
        pass
    @property
    def SimName(self) -> str:
        """
        Getter for property: (str) SimName
         Returns the simulation file name.  
             
         
        """
        pass
    @SimName.setter
    def SimName(self, simName: str):
        """
        Setter for property: (str) SimName
         Returns the simulation file name.  
             
         
        """
        pass
    @property
    def SimNumber(self) -> str:
        """
        Getter for property: (str) SimNumber
         Returns the simulation file number.  
             
         
        """
        pass
    @SimNumber.setter
    def SimNumber(self, simNumber: str):
        """
        Setter for property: (str) SimNumber
         Returns the simulation file number.  
             
         
        """
        pass
    @property
    def SimRevision(self) -> str:
        """
        Getter for property: (str) SimRevision
         Returns the simulation file revision.  
             
         
        """
        pass
    @SimRevision.setter
    def SimRevision(self, simRevision: str):
        """
        Setter for property: (str) SimRevision
         Returns the simulation file revision.  
             
         
        """
        pass
    @property
    def SimulationFile(self) -> str:
        """
        Getter for property: (str) SimulationFile
         Returns the simulation file.  
             
         
        """
        pass
    @SimulationFile.setter
    def SimulationFile(self, file: str):
        """
        Setter for property: (str) SimulationFile
         Returns the simulation file.  
             
         
        """
        pass
    @property
    def SolutionType(self) -> ThermalSolutionBuilder.SolutionTypeOption:
        """
        Getter for property: ( ThermalSolutionBuilder.SolutionTypeOption NXOpen.P) SolutionType
         Returns the solution type.  
             
         
        """
        pass
    @SolutionType.setter
    def SolutionType(self, type: ThermalSolutionBuilder.SolutionTypeOption):
        """
        Setter for property: ( ThermalSolutionBuilder.SolutionTypeOption NXOpen.P) SolutionType
         Returns the solution type.  
             
         
        """
        pass
    @property
    def UpdateType(self) -> ThermalSolutionBuilder.UpdateOption:
        """
        Getter for property: ( ThermalSolutionBuilder.UpdateOption NXOpen.P) UpdateType
         Returns the update type.  
             
         
        """
        pass
    @UpdateType.setter
    def UpdateType(self, type: ThermalSolutionBuilder.UpdateOption):
        """
        Setter for property: ( ThermalSolutionBuilder.UpdateOption NXOpen.P) UpdateType
         Returns the update type.  
             
         
        """
        pass
    @property
    def UseBoardThermalConductivityFile(self) -> bool:
        """
        Getter for property: (bool) UseBoardThermalConductivityFile
         Returns the flag indicating whether to use a board thermal conductivity file.  
             
         
        """
        pass
    @UseBoardThermalConductivityFile.setter
    def UseBoardThermalConductivityFile(self, useConductivityFile: bool):
        """
        Setter for property: (bool) UseBoardThermalConductivityFile
         Returns the flag indicating whether to use a board thermal conductivity file.  
             
         
        """
        pass
    @property
    def UseComponentSimulationData(self) -> bool:
        """
        Getter for property: (bool) UseComponentSimulationData
         Returns the flag indicating whether to use a component simulation database.  
             
         
        """
        pass
    @UseComponentSimulationData.setter
    def UseComponentSimulationData(self, useDatabase: bool):
        """
        Setter for property: (bool) UseComponentSimulationData
         Returns the flag indicating whether to use a component simulation database.  
             
         
        """
        pass
    @property
    def UseEntityFilter(self) -> bool:
        """
        Getter for property: (bool) UseEntityFilter
         Returns the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    @UseEntityFilter.setter
    def UseEntityFilter(self, useEntityFilter: bool):
        """
        Setter for property: (bool) UseEntityFilter
         Returns the flag indicating whether to use the entity filter.  
             
         
        """
        pass
    def AssignPartNumberAndRevisions(self) -> Tuple[str, str, str, str, str, str]:
        """
         Automatically assign item number and revision for simulation, fem and i-part files. 
         Returns A tuple consisting of (simNumber, simRevision, femNumber, femRevision, iPartNumber, iPartRevision). 
         - simNumber is: str.
         - simRevision is: str.
         - femNumber is: str.
         - femRevision is: str.
         - iPartNumber is: str.
         - iPartRevision is: str.

        """
        pass
    def EditComponentSimulationDatabase(self) -> None:
        """
         Edits the component simulation database. 
        """
        pass
    def GetEntityFilter(self) -> EntityFilter:
        """
         Gets the entity filter. 
         Returns filter ( EntityFilter NXOpen.P): .
        """
        pass
    def SetEntityFilter(self, filter: EntityFilter) -> None:
        """
         Sets the entity filter. 
        """
        pass
import NXOpen
class VariantManagerBuilder(NXOpen.Builder): 
    """ Represents a variant manager builder. """
    class EcadLocationEnum(Enum):
        """
        Members Include: 
         |Local| 
         |Dataset| 
         |ItemRevision| 
         |VariantRelationship| 

        """
        Local: int
        Dataset: int
        ItemRevision: int
        VariantRelationship: int
        @staticmethod
        def ValueOf(value: int) -> VariantManagerBuilder.EcadLocationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UpdateOptionEnum(Enum):
        """
        Members Include: 
         |All| 
         |NotSet| 
         |Specify| 

        """
        All: int
        NotSet: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> VariantManagerBuilder.UpdateOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UpdateTargetEnum(Enum):
        """
        Members Include: 
         |External| 
         |Current| 

        """
        External: int
        Current: int
        @staticmethod
        def ValueOf(value: int) -> VariantManagerBuilder.UpdateTargetEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoardFile(self) -> str:
        """
        Getter for property: (str) BoardFile
         Returns the board file.  
             
         
        """
        pass
    @BoardFile.setter
    def BoardFile(self, boardFile: str):
        """
        Setter for property: (str) BoardFile
         Returns the board file.  
             
         
        """
        pass
    @property
    def EcadLocation(self) -> VariantManagerBuilder.EcadLocationEnum:
        """
        Getter for property: ( VariantManagerBuilder.EcadLocationEnum NXOpen.P) EcadLocation
         Returns the ECAD data location.  
             
         
        """
        pass
    @EcadLocation.setter
    def EcadLocation(self, ecadLocation: VariantManagerBuilder.EcadLocationEnum):
        """
        Setter for property: ( VariantManagerBuilder.EcadLocationEnum NXOpen.P) EcadLocation
         Returns the ECAD data location.  
             
         
        """
        pass
    @property
    def ItemRevision(self) -> str:
        """
        Getter for property: (str) ItemRevision
         Returns the item revision.  
             
         
        """
        pass
    @ItemRevision.setter
    def ItemRevision(self, itemRevision: str):
        """
        Setter for property: (str) ItemRevision
         Returns the item revision.  
             
         
        """
        pass
    @property
    def ShowLog(self) -> bool:
        """
        Getter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @ShowLog.setter
    def ShowLog(self, showLog: bool):
        """
        Setter for property: (bool) ShowLog
         Returns the flag indicating whether to show the log.  
             
         
        """
        pass
    @property
    def UpdateOption(self) -> VariantManagerBuilder.UpdateOptionEnum:
        """
        Getter for property: ( VariantManagerBuilder.UpdateOptionEnum NXOpen.P) UpdateOption
         Returns the update option.  
             
         
        """
        pass
    @UpdateOption.setter
    def UpdateOption(self, updateOption: VariantManagerBuilder.UpdateOptionEnum):
        """
        Setter for property: ( VariantManagerBuilder.UpdateOptionEnum NXOpen.P) UpdateOption
         Returns the update option.  
             
         
        """
        pass
    @property
    def UpdateTarget(self) -> VariantManagerBuilder.UpdateTargetEnum:
        """
        Getter for property: ( VariantManagerBuilder.UpdateTargetEnum NXOpen.P) UpdateTarget
         Returns the update target.  
             
         
        """
        pass
    @UpdateTarget.setter
    def UpdateTarget(self, updateTarget: VariantManagerBuilder.UpdateTargetEnum):
        """
        Setter for property: ( VariantManagerBuilder.UpdateTargetEnum NXOpen.P) UpdateTarget
         Returns the update target.  
             
         
        """
        pass
    def Compare(self) -> None:
        """
         Compares the models. 
        """
        pass
    def SetUpdate(self, variantName: str, canUpdate: bool) -> None:
        """
         Sets the update status for the variant assembly. 
        """
        pass
    def ShowComparisonDetails(self) -> None:
        """
         Shows comparison details. 
        """
        pass
class WireBondSide(Enum):
    """
    Members Include: 
     |All|  Any wire bond. 
     |Top|  The Top wire bond. 
     |Bottom|  The Bottom wire bond. 

    """
    All: int
    Top: int
    Bottom: int
    @staticmethod
    def ValueOf(value: int) -> WireBondSide:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
