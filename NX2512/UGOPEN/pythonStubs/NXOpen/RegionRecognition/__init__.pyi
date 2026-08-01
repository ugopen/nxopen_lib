from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class EdgeSelectorBuilder(NXOpen.Builder): 
    """ Represents a RegionRecognition.EdgeSelectorBuilder builder. """
    @property
    def EdgeCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) EdgeCollector
         Returns the selected edge   
            
         
        """
        pass
    def ClearBoundFunctionForReusedRegion(self) -> None:
        """
         Clear bound function for reused region 
        """
        pass
    def SetBoundFunctionForReusedRegion(self) -> None:
        """
         Set bound function for reused region 
        """
        pass
    def SetCustomNames(self, name: List[str]) -> None:
        """
         Set custom names 
        """
        pass
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
class FaceSelectorBuilder(NXOpen.Builder): 
    """ Represents a RegionRecognition.FaceSelectorBuilder builder. """
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector
         Returns the selected face   
            
         
        """
        pass
    @property
    def KeyFaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) KeyFaceCollector
         Returns the selected key face   
            
         
        """
        pass
    def ClearBoundFunctionForReusedRegion(self) -> None:
        """
         Clear bound function for reused region 
        """
        pass
    def RegionObjectPostConstructor(self, reusedRegionFileName: str) -> None:
        """
         Region object post constructor 
        """
        pass
    def SetBoundFunctionForReusedRegion(self) -> None:
        """
         Set bound function for reused region 
        """
        pass
    def SetCustomNames(self, name: List[str]) -> None:
        """
         Set custom names 
        """
        pass
import NXOpen
class Manager(NXOpen.Object): 
    """ Represents the manager of the RegionRecognition module """
    class FaceColor(Enum):
        """
        Members Include: 
         |NoColor| 
         |Red| 
         |Blue| 
         |Yellow| 
         |Green| 
         |Purple| 
         |Orange| 
         |Black| 
         |White| 
         |Pink| 

        """
        NoColor: int
        Red: int
        Blue: int
        Yellow: int
        Green: int
        Purple: int
        Orange: int
        Black: int
        White: int
        Pink: int
        @staticmethod
        def ValueOf(value: int) -> Manager.FaceColor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SearchScope(Enum):
        """
        Members Include: 
         |WorkPartOnly| 
         |EntireAssembly| 
         |WorkPartAndComponents| 

        """
        WorkPartOnly: int
        EntireAssembly: int
        WorkPartAndComponents: int
        @staticmethod
        def ValueOf(value: int) -> Manager.SearchScope:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResultsManagerOption:
        """
         Options for the results manager operation, indicating which attributes and properties to copy or include during post-processing of region recognition results 
         ManagerResultsManagerOption_Struct NXOpen.Regi is an alias for  Manager.ResultsManagerOption NXOpen.Regi.
        """
        @property
        def CopyPMI(self) -> bool:
            """
            Getter for property CopyPMI
            indicates whether to copy PMI during the operation

            """
            pass
        @CopyPMI.setter
        def CopyPMI(self, value: bool):
            """
            Getter for property CopyPMI
            indicates whether to copy PMI during the operation
            Setter for property CopyPMI
            indicates whether to copy PMI during the operation

            """
            pass
        @property
        def CopyColor(self) -> bool:
            """
            Getter for property CopyColor
            indicates whether to copy color attributes during the operation

            """
            pass
        @CopyColor.setter
        def CopyColor(self, value: bool):
            """
            Getter for property CopyColor
            indicates whether to copy color attributes during the operation
            Setter for property CopyColor
            indicates whether to copy color attributes during the operation

            """
            pass
        @property
        def CopyAttribute(self) -> bool:
            """
            Getter for property CopyAttribute
            indicates whether to copy custom attributes during the operation

            """
            pass
        @CopyAttribute.setter
        def CopyAttribute(self, value: bool):
            """
            Getter for property CopyAttribute
            indicates whether to copy custom attributes during the operation
            Setter for property CopyAttribute
            indicates whether to copy custom attributes during the operation

            """
            pass
        @property
        def IncludeSubFolders(self) -> bool:
            """
            Getter for property IncludeSubFolders
            indicates whether to include subfolders in the operation

            """
            pass
        @IncludeSubFolders.setter
        def IncludeSubFolders(self, value: bool):
            """
            Getter for property IncludeSubFolders
            indicates whether to include subfolders in the operation
            Setter for property IncludeSubFolders
            indicates whether to include subfolders in the operation

            """
            pass
        @property
        def IncludeFaceTags(self) -> bool:
            """
            Getter for property IncludeFaceTags
            indicates whether to export face tags in the result of the post-processing operation

            """
            pass
        @IncludeFaceTags.setter
        def IncludeFaceTags(self, value: bool):
            """
            Getter for property IncludeFaceTags
            indicates whether to export face tags in the result of the post-processing operation
            Setter for property IncludeFaceTags
            indicates whether to export face tags in the result of the post-processing operation

            """
            pass
        @property
        def Similarity(self) -> int:
            """
            Getter for property Similarity
            specifies the similarity threshold for the operation

            """
            pass
        @Similarity.setter
        def Similarity(self, value: int):
            """
            Getter for property Similarity
            specifies the similarity threshold for the operation
            Setter for property Similarity
            specifies the similarity threshold for the operation

            """
            pass
        @property
        def Scope(self) -> Manager.SearchScope:
            """
            Getter for property Scope
            specifies the search scope for the operation

            """
            pass
        @Scope.setter
        def Scope(self, value: Manager.SearchScope):
            """
            Getter for property Scope
            specifies the search scope for the operation
            Setter for property Scope
            specifies the search scope for the operation

            """
            pass
        @property
        def ColorToAssign(self) -> Manager.FaceColor:
            """
            Getter for property ColorToAssign
            specifies the color to assign during the operation

            """
            pass
        @ColorToAssign.setter
        def ColorToAssign(self, value: Manager.FaceColor):
            """
            Getter for property ColorToAssign
            specifies the color to assign during the operation
            Setter for property ColorToAssign
            specifies the color to assign during the operation

            """
            pass
    def CreateEdgeSelectorBuilder(part: NXOpen.NXObject) -> EdgeSelectorBuilder:
        """
         Creates a RegionRecognition.EdgeSelectorBuilder 
         Returns builder ( EdgeSelectorBuilder NXOpen.Regi):  created builder. .
        """
        pass
    def CreateFaceSelectorBuilder(part: NXOpen.NXObject) -> FaceSelectorBuilder:
        """
         Creates a RegionRecognition.FaceSelectorBuilder 
         Returns builder ( FaceSelectorBuilder NXOpen.Regi):  created builder. .
        """
        pass
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
    def ResultsManagerProcess(shapeFolder: str, resMgrOption: Manager.ResultsManagerOption) -> str:
        """
         Post-processes the results after searching for similar faces in the specified shape region category folder 
         Returns outputJson (str):  the result of the post-processing operation .
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
    class SearchScopes(Enum):
        """
        Members Include: 
         |WorkPartOnly| 
         |EntireAssembly| 
         |WorkPartAndComponents| 
         |SpecifiedParts| 

        """
        WorkPartOnly: int
        EntireAssembly: int
        WorkPartAndComponents: int
        SpecifiedParts: int
        @staticmethod
        def ValueOf(value: int) -> SelectSimilarEdgesBuilder.SearchScopes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Selection| 
         |Reuse| 

        """
        Selection: int
        Reuse: int
        @staticmethod
        def ValueOf(value: int) -> SelectSimilarEdgesBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SearchScope(self) -> SelectSimilarEdgesBuilder.SearchScopes:
        """
        Getter for property: ( SelectSimilarEdgesBuilder.SearchScopes NXOpen.Regi) SearchScope
         Returns the search scope options.  
             
         
        """
        pass
    @SearchScope.setter
    def SearchScope(self, searchScope: SelectSimilarEdgesBuilder.SearchScopes):
        """
        Setter for property: ( SelectSimilarEdgesBuilder.SearchScopes NXOpen.Regi) SearchScope
         Returns the search scope options.  
             
         
        """
        pass
    @property
    def Type(self) -> SelectSimilarEdgesBuilder.Types:
        """
        Getter for property: ( SelectSimilarEdgesBuilder.Types NXOpen.Regi) Type
         Returns the search type.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: SelectSimilarEdgesBuilder.Types):
        """
        Setter for property: ( SelectSimilarEdgesBuilder.Types NXOpen.Regi) Type
         Returns the search type.  
             
         
        """
        pass
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
    def SetSeedRegionFromReuseLibrary(self, filename: str, regionName: str) -> bool:
        """
         Set a new seed region to the builder from reuse region file, this function will remove all of old regions from the builder 
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
