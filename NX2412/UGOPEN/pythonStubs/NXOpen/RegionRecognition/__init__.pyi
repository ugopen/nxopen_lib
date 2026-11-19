from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class EdgeShapeRegion(NXOpen.TaggedObject): 
    """ Represents an edge region result for RegionRecognition. """
    def FindMatchingEdge(self, seedEdge: NXOpen.Edge) -> NXOpen.Edge:
        """
         Find a matching edge 
         Returns matchingEdge ( NXOpen.Edge):  matching edge in the similar region .
        """
        pass
    def GetEdges(self) -> List[NXOpen.Edge]:
        """
         Get all edges in the region 
         Returns edges ( NXOpen.Edge Li):  edges in the region .
        """
        pass
import NXOpen
class Manager(NXOpen.Object): 
    """ Represents the manager of the RegionRecognition module """
    def CreateRegionLibrary(part: NXOpen.NXObject) -> RegionLibrary:
        """
         Creates a RegionRecognition.RegionLibrary 
         Returns builder ( RegionLibrary NXOpen.Regi):  created builder. .
        """
        pass
    def CreateRegionShapesBuilder(part: NXOpen.NXObject, regionDataTag: RegionShapes) -> RegionShapesBuilder:
        """
         Creates a RegionRecognition.RegionShapesBuilder 
         Returns builder ( RegionShapesBuilder NXOpen.Regi):  created builder. .
        """
        pass
    def CreateSelectSimilarEdgesBuilder(part: NXOpen.NXObject) -> SelectSimilarEdgesBuilder:
        """
         Creates a RegionRecognition.SelectSimilarEdgesBuilder 
         Returns builder ( SelectSimilarEdgesBuilder NXOpen.Regi):  created builder. .
        """
        pass
    def CreateSelectSimilarFacesBuilder(part: NXOpen.NXObject) -> SelectSimilarFacesBuilder:
        """
         Creates a RegionRecognition.SelectSimilarFacesBuilder 
         Returns builder ( SelectSimilarFacesBuilder NXOpen.Regi):  created builder. .
        """
        pass
    def CreateValidationExportBuilder(part: NXOpen.NXObject) -> ValidationExportBuilder:
        """
         Creates a RegionRecognition.ValidationExportBuilder 
         Returns builder ( ValidationExportBuilder NXOpen.Regi):  created builder. .
        """
        pass
    def PrintRegionInformations(part: NXOpen.NXObject, outputDir: str) -> None:
        """
          
        """
        pass
import NXOpen
class RegionLibrary(NXOpen.Builder): 
    """ Represents a RegionRecognition.RegionLibrary. """
    @property
    def RegionData(self) -> RegionShapes:
        """
        Getter for property: ( RegionShapes NXOpen.Regi) RegionData
         Returns the region data.  
             
         
        """
        pass
    @RegionData.setter
    def RegionData(self, regionData: RegionShapes):
        """
        Setter for property: ( RegionShapes NXOpen.Regi) RegionData
         Returns the region data.  
             
         
        """
        pass
    def AddRegion(self) -> None:
        """
         Add a region to library 
        """
        pass
    def DeleteRegion(self, regionName: str) -> None:
        """
         Delete a region from library 
        """
        pass
import NXOpen
import NXOpen.Gateway
class RegionShapesBuilder(NXOpen.Builder): 
    """ Represents a RegionRecognition.RegionShapes builder """
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
         Returns the region category.  
             
         
        """
        pass
    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
         Returns the region category.  
             
         
        """
        pass
    @property
    def ImageCapture(self) -> NXOpen.Gateway.ImageCaptureBuilder:
        """
        Getter for property: ( NXOpen.Gateway.ImageCaptureBuilder) ImageCapture
         Returns the image capture builder  
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the region name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the region name.  
             
         
        """
        pass
    def SetFaceNames(self, faceNames: List[str]) -> None:
        """
         Assigns custom names to region faces. Ignored if the number of names differs from the number of faces. 
        """
        pass
    def SetFaces(self, faces: List[NXOpen.Face]) -> None:
        """
         Sets the region faces.
        """
        pass
import NXOpen
class RegionShapes(NXOpen.TaggedObject): 
    """ """
    pass
import NXOpen
class SelectSimilarEdgesBuilder(NXOpen.Builder): 
    """ Represents a RegionRecognition.SelectSimilarEdgesBuilder builder. """
    def PerformSearch(self) -> List[EdgeShapeRegion]:
        """
         Perform a search 
         Returns resultRegions ( EdgeShapeRegion List[NXOpen.Re):  similar regions .
        """
        pass
    def SetPartsToSearch(self, parts: List[NXOpen.TaggedObject]) -> bool:
        """
         Set parts to search 
         Returns added (bool):  True if succesully added parts to the builder, otherwise return False. .
        """
        pass
    def SetSeedRegionFromEdges(self, objects: List[NXOpen.TaggedObject]) -> bool:
        """
         Set a new seed region to the builder from selected edges, this function will remove all of old regions from the builder 
         Returns added (bool):  True if succesully added this region to the builder, otherwise return False. .
        """
        pass
    def SetSelectedEdges(self, selected_edges: List[NXOpen.TaggedObject]) -> None:
        """
         Set selected edges 
        """
        pass
import NXOpen
class SelectSimilarFacesBuilder(NXOpen.Builder): 
    """ Represents a RegionRecognition.SelectSimilarFacesBuilder builder. """
    class ResultTypeOptions(Enum):
        """
        Members Include: 
         |Regions| 
         |Faces| 

        """
        Regions: int
        Faces: int
        @staticmethod
        def ValueOf(value: int) -> SelectSimilarFacesBuilder.ResultTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SearchFromOptions(Enum):
        """
        Members Include: 
         |Selection| 
         |Library| 
         |Reuse| 
         |Update| 

        """
        Selection: int
        Library: int
        Reuse: int
        Update: int
        @staticmethod
        def ValueOf(value: int) -> SelectSimilarFacesBuilder.SearchFromOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ResultType(self) -> SelectSimilarFacesBuilder.ResultTypeOptions:
        """
        Getter for property: ( SelectSimilarFacesBuilder.ResultTypeOptions NXOpen.Regi) ResultType
         Returns the result type option.  
             
         
        """
        pass
    @ResultType.setter
    def ResultType(self, resultOption: SelectSimilarFacesBuilder.ResultTypeOptions):
        """
        Setter for property: ( SelectSimilarFacesBuilder.ResultTypeOptions NXOpen.Regi) ResultType
         Returns the result type option.  
             
         
        """
        pass
    @property
    def Type(self) -> SelectSimilarFacesBuilder.SearchFromOptions:
        """
        Getter for property: ( SelectSimilarFacesBuilder.SearchFromOptions NXOpen.Regi) Type
         Returns the search option.  
             
         
        """
        pass
    @Type.setter
    def Type(self, searchOption: SelectSimilarFacesBuilder.SearchFromOptions):
        """
        Setter for property: ( SelectSimilarFacesBuilder.SearchFromOptions NXOpen.Regi) Type
         Returns the search option.  
             
         
        """
        pass
    def AISearchRegion(self, onnxModelPath: str) -> List[ShapeRegion]:
        """
         Use AI to Search Region
         Returns resultRegions ( ShapeRegion List[NXOpen.Re):   .
        """
        pass
    def FindRibs(self, body: NXOpen.TaggedObject, direction: NXOpen.Vector3d) -> List[ShapeRegion]:
        """
         Find ribs 
         Returns resultRegions ( ShapeRegion List[NXOpen.Re):   .
        """
        pass
    def MergeOverlappingRegions(self, originalReigons: List[ShapeRegion]) -> List[ShapeRegion]:
        """
         Merge overlapping regions 
         Returns mergedReigons ( ShapeRegion List[NXOpen.Re):  number of merged regions .
        """
        pass
    def PerformSearch(self) -> List[ShapeRegion]:
        """
         Perform a search 
         Returns resultRegions ( ShapeRegion List[NXOpen.Re):   .
        """
        pass
    def SetKeyFaces(self, selected_key_faces: List[NXOpen.TaggedObject]) -> None:
        """
         Set key faces 
        """
        pass
    def SetObjectsToSearchIn(self, objects: List[NXOpen.TaggedObject]) -> bool:
        """
         Set objects (parts, bodies or faces) to search in 
         Returns added (bool):  True if succesully added objects to the builder, otherwise return False. .
        """
        pass
    def SetPartsToSearch(self, parts: List[NXOpen.TaggedObject]) -> bool:
        """
         Set parts to search 
         Returns added (bool):  True if succesully added parts to the builder, otherwise return False. .
        """
        pass
    def SetSeedRegionFromFaces(self, objects: List[NXOpen.TaggedObject]) -> bool:
        """
         Set a new seed region to the builder from selected faces, this function will remove all of old regions from the builder 
         Returns added (bool):  True if succesully added this region to the builder, otherwise return False. .
        """
        pass
    def SetSeedRegionFromLibrary(self, regionName: str) -> bool:
        """
         Set a new seed region to the builder from file, this function will remove all of old regions from the builder 
         Returns added (bool):  True if succesully added this region to the builder, otherwise return False. .
        """
        pass
    def SetSeedRegionFromReuseLibrary(self, regionPath: str, regionName: str) -> bool:
        """
         Set a new seed region to the builder from reuse region file, this function will remove all of old regions from the builder 
         Returns added (bool):  True if succesully added this region to the builder, otherwise return False. .
        """
        pass
    def SetSelectedFaces(self, selected_faces: List[NXOpen.TaggedObject]) -> None:
        """
         Set a selected faces 
        """
        pass
    def UpdateRib(self, sideFace1: NXOpen.TaggedObject, sideFace2: NXOpen.TaggedObject, direction: NXOpen.Vector3d) -> ShapeRegion:
        """
         Update rib 
         Returns updatedRegions ( ShapeRegion NXOpen.Regi):   .
        """
        pass
import NXOpen
class ShapeRegion(NXOpen.TaggedObject): 
    """ Represents a region for RegionRecognition. """
    def AskCategory(self) -> str:
        """
         Ask a category 
         Returns regionCategory (str): .
        """
        pass
    def AskName(self) -> str:
        """
         Ask a name 
         Returns regionName (str): .
        """
        pass
    def FindFaceByCustomName(self, customName: str) -> NXOpen.Face:
        """
         Find a matching face 
         Returns matchingFace ( NXOpen.Face): .
        """
        pass
    def FindMatchingEdges(self, seedEdge: NXOpen.Edge) -> List[NXOpen.Edge]:
        """
         Find a matching edge 
         Returns matchingEdges ( NXOpen.Edge Li): .
        """
        pass
    def FindMatchingFace(self, seedFace: NXOpen.Face) -> NXOpen.Face:
        """
         Find a matching face 
         Returns matchingFace ( NXOpen.Face): .
        """
        pass
    def GetEdges(self) -> List[NXOpen.Edge]:
        """
         Get a region edges 
         Returns edges ( NXOpen.Edge Li): .
        """
        pass
    def GetFaces(self) -> List[NXOpen.Face]:
        """
         Get a region faces 
         Returns faces ( NXOpen.Face Li):   .
        """
        pass
import NXOpen
class ValidationExportBuilder(NXOpen.Builder): 
    """ Represents a RegionRecognition.ValidationExportBuilder builder """
    def AssignAttrToEdges(self, writePartTag: NXOpen.NXObject) -> bool:
        """
         Assign search result information to edge attributes 
         Returns assigned (bool): .
        """
        pass
    def AssignSidToResultRegions(self, writePartTag: NXOpen.NXObject) -> bool:
        """
         Set a new seed region to the builder from file, this function will remove all of old regions from the builder 
         Returns added (bool):  True if succesully added this region to the builder, otherwise return False. .
        """
        pass
    def SetEdgeResultRegions(self, edgeResultRegions: List[EdgeShapeRegion]) -> None:
        """
         Set edge result regions to be validated 
        """
        pass
    def SetPartOccsOfEdgeRegions(self, partOccs: List[NXOpen.TaggedObject]) -> None:
        """
         Set part occs where the result edge regions is located 
        """
        pass
    def SetRegionProperty(self, regionName: str, seedRegionName: str, selfFacesSid: List[str], mappingFacesSid: List[str], selfFacesTag: List[NXOpen.TaggedObject], selfFacesTagSid: List[str], regionFacesTag: List[NXOpen.TaggedObject], isSeedRegion: bool) -> bool:
        """
         Set a new seed region to the builder from file, this function will remove all of old regions from the builder 
         Returns added (bool):  True if succesully added this region to the builder, otherwise return False. .
        """
        pass
