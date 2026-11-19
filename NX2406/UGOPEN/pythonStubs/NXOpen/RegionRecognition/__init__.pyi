from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents the manager of the RegionRecognition module  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Manager(NXOpen.Object): 
    """ Represents the manager of the RegionRecognition module """


    ##  Creates a @link RegionRecognition::RegionLibrary RegionRecognition::RegionLibrary@endlink  
    ##  @return builder (@link RegionLibrary NXOpen.RegionRecognition.RegionLibrary@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateRegionLibrary(part: NXOpen.NXObject) -> RegionLibrary:
        """
         Creates a @link RegionRecognition::RegionLibrary RegionRecognition::RegionLibrary@endlink  
         @return builder (@link RegionLibrary NXOpen.RegionRecognition.RegionLibrary@endlink):  created builder. .
        """
        pass
    
    ##  Creates a @link RegionRecognition::RegionShapesBuilder RegionRecognition::RegionShapesBuilder@endlink  
    ##  @return builder (@link RegionShapesBuilder NXOpen.RegionRecognition.RegionShapesBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="regionDataTag"> (@link RegionShapes NXOpen.RegionRecognition.RegionShapes@endlink) </param>
    def CreateRegionShapesBuilder(part: NXOpen.NXObject, regionDataTag: RegionShapes) -> RegionShapesBuilder:
        """
         Creates a @link RegionRecognition::RegionShapesBuilder RegionRecognition::RegionShapesBuilder@endlink  
         @return builder (@link RegionShapesBuilder NXOpen.RegionRecognition.RegionShapesBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates a @link RegionRecognition::SelectSimilarFacesBuilder RegionRecognition::SelectSimilarFacesBuilder@endlink  
    ##  @return builder (@link SelectSimilarFacesBuilder NXOpen.RegionRecognition.SelectSimilarFacesBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateSelectSimilarFacesBuilder(part: NXOpen.NXObject) -> SelectSimilarFacesBuilder:
        """
         Creates a @link RegionRecognition::SelectSimilarFacesBuilder RegionRecognition::SelectSimilarFacesBuilder@endlink  
         @return builder (@link SelectSimilarFacesBuilder NXOpen.RegionRecognition.SelectSimilarFacesBuilder@endlink):  created builder. .
        """
        pass
    
    ##  Creates a @link RegionRecognition::ValidationExportBuilder RegionRecognition::ValidationExportBuilder@endlink  
    ##  @return builder (@link ValidationExportBuilder NXOpen.RegionRecognition.ValidationExportBuilder@endlink):  created builder. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateValidationExportBuilder(part: NXOpen.NXObject) -> ValidationExportBuilder:
        """
         Creates a @link RegionRecognition::ValidationExportBuilder RegionRecognition::ValidationExportBuilder@endlink  
         @return builder (@link ValidationExportBuilder NXOpen.RegionRecognition.ValidationExportBuilder@endlink):  created builder. .
        """
        pass
    
    ##   
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="outputDir"> (str) </param>
    def PrintRegionInformations(part: NXOpen.NXObject, outputDir: str) -> None:
        """
          
        """
        pass
    
import NXOpen
##  Represents a @link RegionRecognition::RegionLibrary RegionRecognition::RegionLibrary@endlink .  <br> To create a new instance of this class, use @link NXOpen::RegionRecognition::Manager::CreateRegionLibrary  NXOpen::RegionRecognition::Manager::CreateRegionLibrary @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class RegionLibrary(NXOpen.Builder): 
    """ Represents a <ja_class>RegionRecognition.RegionLibrary</ja_class>. """


    ## Getter for property: (@link RegionShapes NXOpen.RegionRecognition.RegionShapes@endlink) RegionData
    ##  Returns the region data.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return RegionShapes
    @property
    def RegionData(self) -> RegionShapes:
        """
        Getter for property: (@link RegionShapes NXOpen.RegionRecognition.RegionShapes@endlink) RegionData
         Returns the region data.  
             
         
        """
        pass
    
    ## Setter for property: (@link RegionShapes NXOpen.RegionRecognition.RegionShapes@endlink) RegionData

    ##  Returns the region data.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RegionData.setter
    def RegionData(self, regionData: RegionShapes):
        """
        Setter for property: (@link RegionShapes NXOpen.RegionRecognition.RegionShapes@endlink) RegionData
         Returns the region data.  
             
         
        """
        pass
    
    ##  Add a region to library 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def AddRegion(self) -> None:
        """
         Add a region to library 
        """
        pass
    
    ##  Delete a region from library 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="regionName"> (str) </param>
    def DeleteRegion(self, regionName: str) -> None:
        """
         Delete a region from library 
        """
        pass
    
import NXOpen
import NXOpen.Gateway
##  Represents a @link RegionRecognition::RegionShapes RegionRecognition::RegionShapes@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::RegionRecognition::Manager::CreateRegionShapesBuilder  NXOpen::RegionRecognition::Manager::CreateRegionShapesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ImageCapture.CaptureMethod </term> <description> 
##  
## GraphicsArea </description> </item> 
## 
## <item><term> 
##  
## ImageCapture.Format </term> <description> 
##  
## Bmp </description> </item> 
## 
## <item><term> 
##  
## ImageCapture.Size </term> <description> 
##  
## Pixels64 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class RegionShapesBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>RegionRecognition.RegionShapes</ja_class> builder """


    ## Getter for property: (str) Category
    ##  Returns the region category.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
         Returns the region category.  
             
         
        """
        pass
    
    ## Setter for property: (str) Category

    ##  Returns the region category.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
         Returns the region category.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Gateway.ImageCaptureBuilder NXOpen.Gateway.ImageCaptureBuilder@endlink) ImageCapture
    ##  Returns the image capture builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Gateway.ImageCaptureBuilder
    @property
    def ImageCapture(self) -> NXOpen.Gateway.ImageCaptureBuilder:
        """
        Getter for property: (@link NXOpen.Gateway.ImageCaptureBuilder NXOpen.Gateway.ImageCaptureBuilder@endlink) ImageCapture
         Returns the image capture builder  
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the region name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the region name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the region name.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the region name.  
             
         
        """
        pass
    
    ##  Assigns custom names to region faces. Ignored if the number of names differs from the number of faces. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="faceNames"> (List[str])  Region face names </param>
    def SetFaceNames(self, faceNames: List[str]) -> None:
        """
         Assigns custom names to region faces. Ignored if the number of names differs from the number of faces. 
        """
        pass
    
    ##  Sets the region faces.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="faces"> (@link NXOpen.Face List[NXOpen.Face]@endlink)  Region faces </param>
    def SetFaces(self, faces: List[NXOpen.Face]) -> None:
        """
         Sets the region faces.
        """
        pass
    
import NXOpen
##   <br> To create or edit an instance of this class, use @link NXOpen::RegionRecognition::RegionShapesBuilder  NXOpen::RegionRecognition::RegionShapesBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class RegionShapes(NXOpen.TaggedObject): 
    """ """
    pass


import NXOpen
##  Represents a @link RegionRecognition::SelectSimilarFacesBuilder RegionRecognition::SelectSimilarFacesBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::RegionRecognition::Manager::CreateSelectSimilarFacesBuilder  NXOpen::RegionRecognition::Manager::CreateSelectSimilarFacesBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SelectSimilarFacesBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>RegionRecognition.SelectSimilarFacesBuilder</ja_class> builder. """


    ##  The result type options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Regions</term><description> 
    ## </description> </item><item><term> 
    ## Faces</term><description> 
    ## </description> </item></list>
    class ResultTypeOptions(Enum):
        """
        Members Include: <Regions> <Faces>
        """
        Regions: int
        Faces: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SelectSimilarFacesBuilder.ResultTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The search options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Selection</term><description> 
    ## </description> </item><item><term> 
    ## Library</term><description> 
    ## </description> </item><item><term> 
    ## Reuse</term><description> 
    ## </description> </item><item><term> 
    ## Update</term><description> 
    ## </description> </item></list>
    class SearchFromOptions(Enum):
        """
        Members Include: <Selection> <Library> <Reuse> <Update>
        """
        Selection: int
        Library: int
        Reuse: int
        Update: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SelectSimilarFacesBuilder.SearchFromOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SelectSimilarFacesBuilder.ResultTypeOptions NXOpen.RegionRecognition.SelectSimilarFacesBuilder.ResultTypeOptions@endlink) ResultType
    ##  Returns the result type option.  
    ##      
    ##  
    ## Getter License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return SelectSimilarFacesBuilder.ResultTypeOptions
    @property
    def ResultType(self) -> SelectSimilarFacesBuilder.ResultTypeOptions:
        """
        Getter for property: (@link SelectSimilarFacesBuilder.ResultTypeOptions NXOpen.RegionRecognition.SelectSimilarFacesBuilder.ResultTypeOptions@endlink) ResultType
         Returns the result type option.  
             
         
        """
        pass
    
    ## Setter for property: (@link SelectSimilarFacesBuilder.ResultTypeOptions NXOpen.RegionRecognition.SelectSimilarFacesBuilder.ResultTypeOptions@endlink) ResultType

    ##  Returns the result type option.  
    ##      
    ##  
    ## Setter License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ResultType.setter
    def ResultType(self, resultOption: SelectSimilarFacesBuilder.ResultTypeOptions):
        """
        Setter for property: (@link SelectSimilarFacesBuilder.ResultTypeOptions NXOpen.RegionRecognition.SelectSimilarFacesBuilder.ResultTypeOptions@endlink) ResultType
         Returns the result type option.  
             
         
        """
        pass
    
    ## Getter for property: (@link SelectSimilarFacesBuilder.SearchFromOptions NXOpen.RegionRecognition.SelectSimilarFacesBuilder.SearchFromOptions@endlink) Type
    ##  Returns the search option.  
    ##      
    ##  
    ## Getter License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return SelectSimilarFacesBuilder.SearchFromOptions
    @property
    def Type(self) -> SelectSimilarFacesBuilder.SearchFromOptions:
        """
        Getter for property: (@link SelectSimilarFacesBuilder.SearchFromOptions NXOpen.RegionRecognition.SelectSimilarFacesBuilder.SearchFromOptions@endlink) Type
         Returns the search option.  
             
         
        """
        pass
    
    ## Setter for property: (@link SelectSimilarFacesBuilder.SearchFromOptions NXOpen.RegionRecognition.SelectSimilarFacesBuilder.SearchFromOptions@endlink) Type

    ##  Returns the search option.  
    ##      
    ##  
    ## Setter License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Type.setter
    def Type(self, searchOption: SelectSimilarFacesBuilder.SearchFromOptions):
        """
        Setter for property: (@link SelectSimilarFacesBuilder.SearchFromOptions NXOpen.RegionRecognition.SelectSimilarFacesBuilder.SearchFromOptions@endlink) Type
         Returns the search option.  
             
         
        """
        pass
    
    ##  Use AI to Search Region
    ##  @return resultRegions (@link ShapeRegion List[NXOpen.RegionRecognition.ShapeRegion]@endlink):   .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="onnxModelPath"> (str) </param>
    def AISearchRegion(self, onnxModelPath: str) -> List[ShapeRegion]:
        """
         Use AI to Search Region
         @return resultRegions (@link ShapeRegion List[NXOpen.RegionRecognition.ShapeRegion]@endlink):   .
        """
        pass
    
    ##  Find ribs 
    ##  @return resultRegions (@link ShapeRegion List[NXOpen.RegionRecognition.ShapeRegion]@endlink):   .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="body"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="direction"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def FindRibs(self, body: NXOpen.TaggedObject, direction: NXOpen.Vector3d) -> List[ShapeRegion]:
        """
         Find ribs 
         @return resultRegions (@link ShapeRegion List[NXOpen.RegionRecognition.ShapeRegion]@endlink):   .
        """
        pass
    
    ##  Merge overlapping regions 
    ##  @return mergedReigons (@link ShapeRegion List[NXOpen.RegionRecognition.ShapeRegion]@endlink):  number of merged regions .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="originalReigons"> (@link ShapeRegion List[NXOpen.RegionRecognition.ShapeRegion]@endlink)  number of regions to be merged </param>
    def MergeOverlappingRegions(self, originalReigons: List[ShapeRegion]) -> List[ShapeRegion]:
        """
         Merge overlapping regions 
         @return mergedReigons (@link ShapeRegion List[NXOpen.RegionRecognition.ShapeRegion]@endlink):  number of merged regions .
        """
        pass
    
    ##  Perform a search 
    ##  @return resultRegions (@link ShapeRegion List[NXOpen.RegionRecognition.ShapeRegion]@endlink):   .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    def PerformSearch(self) -> List[ShapeRegion]:
        """
         Perform a search 
         @return resultRegions (@link ShapeRegion List[NXOpen.RegionRecognition.ShapeRegion]@endlink):   .
        """
        pass
    
    ##  Set key faces 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="selected_key_faces"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  selected key faces </param>
    def SetKeyFaces(self, selected_key_faces: List[NXOpen.TaggedObject]) -> None:
        """
         Set key faces 
        """
        pass
    
    ##  Set objects (parts, bodies or faces) to search in 
    ##  @return added (bool):  True if succesully added objects to the builder, otherwise return False. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="objects"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  number of objects to search in </param>
    def SetObjectsToSearchIn(self, objects: List[NXOpen.TaggedObject]) -> bool:
        """
         Set objects (parts, bodies or faces) to search in 
         @return added (bool):  True if succesully added objects to the builder, otherwise return False. .
        """
        pass
    
    ##  Set parts to search 
    ##  @return added (bool):  True if succesully added parts to the builder, otherwise return False. .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="parts"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  number of parts to search in </param>
    def SetPartsToSearch(self, parts: List[NXOpen.TaggedObject]) -> bool:
        """
         Set parts to search 
         @return added (bool):  True if succesully added parts to the builder, otherwise return False. .
        """
        pass
    
    ##  Set a new seed region to the builder from selected faces, this function will remove all of old regions from the builder 
    ##  @return added (bool):  True if succesully added this region to the builder, otherwise return False. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="objects"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  number of items for this region </param>
    def SetSeedRegionFromFaces(self, objects: List[NXOpen.TaggedObject]) -> bool:
        """
         Set a new seed region to the builder from selected faces, this function will remove all of old regions from the builder 
         @return added (bool):  True if succesully added this region to the builder, otherwise return False. .
        """
        pass
    
    ##  Set a new seed region to the builder from file, this function will remove all of old regions from the builder 
    ##  @return added (bool):  True if succesully added this region to the builder, otherwise return False. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="regionName"> (str) </param>
    def SetSeedRegionFromLibrary(self, regionName: str) -> bool:
        """
         Set a new seed region to the builder from file, this function will remove all of old regions from the builder 
         @return added (bool):  True if succesully added this region to the builder, otherwise return False. .
        """
        pass
    
    ##  Set a new seed region to the builder from reuse region file, this function will remove all of old regions from the builder 
    ##  @return added (bool):  True if succesully added this region to the builder, otherwise return False. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="regionPath"> (str) </param>
    ## <param name="regionName"> (str) </param>
    def SetSeedRegionFromReuseLibrary(self, regionPath: str, regionName: str) -> bool:
        """
         Set a new seed region to the builder from reuse region file, this function will remove all of old regions from the builder 
         @return added (bool):  True if succesully added this region to the builder, otherwise return False. .
        """
        pass
    
    ##  Set a selected faces 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="selected_faces"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  selected faces </param>
    def SetSelectedFaces(self, selected_faces: List[NXOpen.TaggedObject]) -> None:
        """
         Set a selected faces 
        """
        pass
    
    ##  Update rib 
    ##  @return updatedRegions (@link ShapeRegion NXOpen.RegionRecognition.ShapeRegion@endlink):   .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="sideFace1"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="sideFace2"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="direction"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def UpdateRib(self, sideFace1: NXOpen.TaggedObject, sideFace2: NXOpen.TaggedObject, direction: NXOpen.Vector3d) -> ShapeRegion:
        """
         Update rib 
         @return updatedRegions (@link ShapeRegion NXOpen.RegionRecognition.ShapeRegion@endlink):   .
        """
        pass
    
import NXOpen
##  Represents a region for RegionRecognition.  <br> Creation of ShapeRegion is not supported yet.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ShapeRegion(NXOpen.TaggedObject): 
    """ Represents a region for RegionRecognition. """


    ##  Ask a category 
    ##  @return regionCategory (str): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    def AskCategory(self) -> str:
        """
         Ask a category 
         @return regionCategory (str): .
        """
        pass
    
    ##  Ask a name 
    ##  @return regionName (str): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    def AskName(self) -> str:
        """
         Ask a name 
         @return regionName (str): .
        """
        pass
    
    ##  Find a matching face 
    ##  @return matchingFace (@link NXOpen.Face NXOpen.Face@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="customName"> (str) </param>
    def FindFaceByCustomName(self, customName: str) -> NXOpen.Face:
        """
         Find a matching face 
         @return matchingFace (@link NXOpen.Face NXOpen.Face@endlink): .
        """
        pass
    
    ##  Find a matching edge 
    ##  @return matchingEdges (@link NXOpen.Edge List[NXOpen.Edge]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="seedEdge"> (@link NXOpen.Edge NXOpen.Edge@endlink) </param>
    def FindMatchingEdges(self, seedEdge: NXOpen.Edge) -> List[NXOpen.Edge]:
        """
         Find a matching edge 
         @return matchingEdges (@link NXOpen.Edge List[NXOpen.Edge]@endlink): .
        """
        pass
    
    ##  Find a matching face 
    ##  @return matchingFace (@link NXOpen.Face NXOpen.Face@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="seedFace"> (@link NXOpen.Face NXOpen.Face@endlink) </param>
    def FindMatchingFace(self, seedFace: NXOpen.Face) -> NXOpen.Face:
        """
         Find a matching face 
         @return matchingFace (@link NXOpen.Face NXOpen.Face@endlink): .
        """
        pass
    
    ##  Get a region edges 
    ##  @return edges (@link NXOpen.Edge List[NXOpen.Edge]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    def GetEdges(self) -> List[NXOpen.Edge]:
        """
         Get a region edges 
         @return edges (@link NXOpen.Edge List[NXOpen.Edge]@endlink): .
        """
        pass
    
    ##  Get a region faces 
    ##  @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink):   .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    def GetFaces(self) -> List[NXOpen.Face]:
        """
         Get a region faces 
         @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink):   .
        """
        pass
    
import NXOpen
##  Represents a @link RegionRecognition::ValidationExportBuilder RegionRecognition::ValidationExportBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::RegionRecognition::Manager::CreateValidationExportBuilder  NXOpen::RegionRecognition::Manager::CreateValidationExportBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ValidationExportBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>RegionRecognition.ValidationExportBuilder</ja_class> builder """


    ##  Set a new seed region to the builder from file, this function will remove all of old regions from the builder 
    ##  @return added (bool):  True if succesully added this region to the builder, otherwise return False. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="writePartTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def AssignSidToResultRegions(self, writePartTag: NXOpen.NXObject) -> bool:
        """
         Set a new seed region to the builder from file, this function will remove all of old regions from the builder 
         @return added (bool):  True if succesully added this region to the builder, otherwise return False. .
        """
        pass
    
    ##  Set a new seed region to the builder from file, this function will remove all of old regions from the builder 
    ##  @return added (bool):  True if succesully added this region to the builder, otherwise return False. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_ml_region_finder (" Shape Region Recognition")
    ## 
    ## <param name="regionName"> (str) </param>
    ## <param name="seedRegionName"> (str) </param>
    ## <param name="selfFacesSid"> (List[str]) </param>
    ## <param name="mappingFacesSid"> (List[str]) </param>
    ## <param name="selfFacesTag"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    ## <param name="selfFacesTagSid"> (List[str]) </param>
    ## <param name="regionFacesTag"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    ## <param name="isSeedRegion"> (bool) </param>
    def SetRegionProperty(self, regionName: str, seedRegionName: str, selfFacesSid: List[str], mappingFacesSid: List[str], selfFacesTag: List[NXOpen.TaggedObject], selfFacesTagSid: List[str], regionFacesTag: List[NXOpen.TaggedObject], isSeedRegion: bool) -> bool:
        """
         Set a new seed region to the builder from file, this function will remove all of old regions from the builder 
         @return added (bool):  True if succesully added this region to the builder, otherwise return False. .
        """
        pass
    
## @package NXOpen.RegionRecognition
## Classes, Enums and Structs under NXOpen.RegionRecognition namespace

##  @link SelectSimilarFacesBuilderResultTypeOptions NXOpen.RegionRecognition.SelectSimilarFacesBuilderResultTypeOptions @endlink is an alias for @link SelectSimilarFacesBuilder.ResultTypeOptions NXOpen.RegionRecognition.SelectSimilarFacesBuilder.ResultTypeOptions@endlink
SelectSimilarFacesBuilderResultTypeOptions = SelectSimilarFacesBuilder.ResultTypeOptions


##  @link SelectSimilarFacesBuilderSearchFromOptions NXOpen.RegionRecognition.SelectSimilarFacesBuilderSearchFromOptions @endlink is an alias for @link SelectSimilarFacesBuilder.SearchFromOptions NXOpen.RegionRecognition.SelectSimilarFacesBuilder.SearchFromOptions@endlink
SelectSimilarFacesBuilderSearchFromOptions = SelectSimilarFacesBuilder.SearchFromOptions


