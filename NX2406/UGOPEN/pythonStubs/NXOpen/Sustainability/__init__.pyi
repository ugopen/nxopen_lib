from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
## 
##     Represents a @link NXOpen::Sustainability::CalculateScoresBuilder NXOpen::Sustainability::CalculateScoresBuilder@endlink  used to calculate sustainability scores.
##      <br> To create a new instance of this class, use @link NXOpen::Sustainability::SustainabilityManager::CreateCalculateScoresBuilder  NXOpen::Sustainability::SustainabilityManager::CreateCalculateScoresBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## SubtypeNominal </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## SubtypeRecycled </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SubtypeRenewable </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## UnselectedSubtypeScores </term> <description> 
##  
## Retain </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2312.0.0  <br> 

class CalculateScoresBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Sustainability.CalculateScoresBuilder</ja_class> used to calculate sustainability scores.
    """


    ##  The option specifies if unselected subtype scores should be deleted or retained. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Delete</term><description> 
    ## </description> </item><item><term> 
    ## Retain</term><description> 
    ## </description> </item></list>
    class UnselectedSubtypeScoresOption(Enum):
        """
        Members Include: <Delete> <Retain>
        """
        Delete: int
        Retain: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CalculateScoresBuilder.UnselectedSubtypeScoresOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) SubtypeNominal
    ##  Returns the subtype nominal   
    ##     
    ##  
    ## Getter License requirements: nx_sustainability (" Design for Sustainability")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def SubtypeNominal(self) -> bool:
        """
        Getter for property: (bool) SubtypeNominal
         Returns the subtype nominal   
            
         
        """
        pass
    
    ## Setter for property: (bool) SubtypeNominal

    ##  Returns the subtype nominal   
    ##     
    ##  
    ## Setter License requirements: nx_sustainability (" Design for Sustainability")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SubtypeNominal.setter
    def SubtypeNominal(self, subtypeNominal: bool):
        """
        Setter for property: (bool) SubtypeNominal
         Returns the subtype nominal   
            
         
        """
        pass
    
    ## Getter for property: (bool) SubtypeRecycled
    ##  Returns the subtype recycled   
    ##     
    ##  
    ## Getter License requirements: nx_sustainability (" Design for Sustainability")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def SubtypeRecycled(self) -> bool:
        """
        Getter for property: (bool) SubtypeRecycled
         Returns the subtype recycled   
            
         
        """
        pass
    
    ## Setter for property: (bool) SubtypeRecycled

    ##  Returns the subtype recycled   
    ##     
    ##  
    ## Setter License requirements: nx_sustainability (" Design for Sustainability")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SubtypeRecycled.setter
    def SubtypeRecycled(self, subtypeRecycled: bool):
        """
        Setter for property: (bool) SubtypeRecycled
         Returns the subtype recycled   
            
         
        """
        pass
    
    ## Getter for property: (bool) SubtypeRenewable
    ##  Returns the subtype renewable   
    ##     
    ##  
    ## Getter License requirements: nx_sustainability (" Design for Sustainability")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def SubtypeRenewable(self) -> bool:
        """
        Getter for property: (bool) SubtypeRenewable
         Returns the subtype renewable   
            
         
        """
        pass
    
    ## Setter for property: (bool) SubtypeRenewable

    ##  Returns the subtype renewable   
    ##     
    ##  
    ## Setter License requirements: nx_sustainability (" Design for Sustainability")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SubtypeRenewable.setter
    def SubtypeRenewable(self, subtypeRenewable: bool):
        """
        Setter for property: (bool) SubtypeRenewable
         Returns the subtype renewable   
            
         
        """
        pass
    
    ## Getter for property: (@link CalculateScoresBuilder.UnselectedSubtypeScoresOption NXOpen.Sustainability.CalculateScoresBuilder.UnselectedSubtypeScoresOption@endlink) UnselectedSubtypeScores
    ##  Returns the unselected subtype scores option  
    ##     
    ##  
    ## Getter License requirements: nx_sustainability (" Design for Sustainability")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return CalculateScoresBuilder.UnselectedSubtypeScoresOption
    @property
    def UnselectedSubtypeScores(self) -> CalculateScoresBuilder.UnselectedSubtypeScoresOption:
        """
        Getter for property: (@link CalculateScoresBuilder.UnselectedSubtypeScoresOption NXOpen.Sustainability.CalculateScoresBuilder.UnselectedSubtypeScoresOption@endlink) UnselectedSubtypeScores
         Returns the unselected subtype scores option  
            
         
        """
        pass
    
    ## Setter for property: (@link CalculateScoresBuilder.UnselectedSubtypeScoresOption NXOpen.Sustainability.CalculateScoresBuilder.UnselectedSubtypeScoresOption@endlink) UnselectedSubtypeScores

    ##  Returns the unselected subtype scores option  
    ##     
    ##  
    ## Setter License requirements: nx_sustainability (" Design for Sustainability")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @UnselectedSubtypeScores.setter
    def UnselectedSubtypeScores(self, option: CalculateScoresBuilder.UnselectedSubtypeScoresOption):
        """
        Setter for property: (@link CalculateScoresBuilder.UnselectedSubtypeScoresOption NXOpen.Sustainability.CalculateScoresBuilder.UnselectedSubtypeScoresOption@endlink) UnselectedSubtypeScores
         Returns the unselected subtype scores option  
            
         
        """
        pass
    
    ##  Get the materials of body 
    ##  @return A tuple consisting of (environmentMaterial, physicalMaterial). 
    ##  - environmentMaterial is: str.
    ##  - physicalMaterial is: str.

    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_sustainability (" Design for Sustainability")
    ## 
    ## <param name="body"> (@link NXOpen.Body NXOpen.Body@endlink) </param>
    def GetMaterialsOfBody(self, body: NXOpen.Body) -> Tuple[str, str]:
        """
         Get the materials of body 
         @return A tuple consisting of (environmentMaterial, physicalMaterial). 
         - environmentMaterial is: str.
         - physicalMaterial is: str.

        """
        pass
    
    ##  Get the scores of body 
    ##  @return A tuple consisting of (scoreValues, scoreTitles). 
    ##  - scoreValues is: List[float].
    ##  - scoreTitles is: List[str].

    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_sustainability (" Design for Sustainability")
    ## 
    ## <param name="body"> (@link NXOpen.Body NXOpen.Body@endlink) </param>
    ## <param name="subtype"> (str) </param>
    def GetScoresOfBody(self, body: NXOpen.Body, subtype: str) -> Tuple[List[float], List[str]]:
        """
         Get the scores of body 
         @return A tuple consisting of (scoreValues, scoreTitles). 
         - scoreValues is: List[float].
         - scoreTitles is: List[str].

        """
        pass
    
import NXOpen
##  
##     Represents a @link NXOpen::Sustainability::MapEnvironmentalMaterialBuilder NXOpen::Sustainability::MapEnvironmentalMaterialBuilder@endlink  used to map environmental materials.
##      <br> To create a new instance of this class, use @link NXOpen::Sustainability::SustainabilityManager::CreateMapEnvironmentalMaterialBuilder  NXOpen::Sustainability::SustainabilityManager::CreateMapEnvironmentalMaterialBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class MapEnvironmentalMaterialBuilder(NXOpen.Builder): 
    """ 
    Represents a <ja_class>NXOpen.Sustainability.MapEnvironmentalMaterialBuilder</ja_class> used to map environmental materials.
    """


    ## Getter for property: (str) LibFileBrowser
    ##  Returns the environmental material file browser   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return str
    @property
    def LibFileBrowser(self) -> str:
        """
        Getter for property: (str) LibFileBrowser
         Returns the environmental material file browser   
            
         
        """
        pass
    
    ## Setter for property: (str) LibFileBrowser

    ##  Returns the environmental material file browser   
    ##     
    ##  
    ## Setter License requirements: nx_sustainability (" Design for Sustainability")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @LibFileBrowser.setter
    def LibFileBrowser(self, foldername: str):
        """
        Setter for property: (str) LibFileBrowser
         Returns the environmental material file browser   
            
         
        """
        pass
    
    ## Getter for property: (str) MappingFileBrowser
    ##  Returns the environmental material mapping file browser   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return str
    @property
    def MappingFileBrowser(self) -> str:
        """
        Getter for property: (str) MappingFileBrowser
         Returns the environmental material mapping file browser   
            
         
        """
        pass
    
    ## Setter for property: (str) MappingFileBrowser

    ##  Returns the environmental material mapping file browser   
    ##     
    ##  
    ## Setter License requirements: nx_sustainability (" Design for Sustainability")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @MappingFileBrowser.setter
    def MappingFileBrowser(self, foldername: str):
        """
        Setter for property: (str) MappingFileBrowser
         Returns the environmental material mapping file browser   
            
         
        """
        pass
    
    ##  Download the environmental material files from the web service 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_sustainability (" Design for Sustainability")
    def DownloadButton(self) -> None:
        """
         Download the environmental material files from the web service 
        """
        pass
    
    ##  Information of mapping between physical and environmental materials 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_sustainability (" Design for Sustainability")
    def InfoButton(self) -> None:
        """
         Information of mapping between physical and environmental materials 
        """
        pass
    
import NXOpen
## 
##      Represents an NX @link NXOpen::Sustainability::SustainabilityManager NXOpen::Sustainability::SustainabilityManager@endlink  object.
##      <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class SustainabilityManager(NXOpen.Object): 
    """
     Represents an NX <ja_class>NXOpen.Sustainability.SustainabilityManager</ja_class> object.
    """


    ##  Create a @link NXOpen::Sustainability::CalculateScoresBuilder NXOpen::Sustainability::CalculateScoresBuilder@endlink  
    ##  @return calculate_scores_builder (@link CalculateScoresBuilder NXOpen.Sustainability.CalculateScoresBuilder@endlink):  calculate scores builder .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_sustainability (" Design for Sustainability")
    def CreateCalculateScoresBuilder(self) -> CalculateScoresBuilder:
        """
         Create a @link NXOpen::Sustainability::CalculateScoresBuilder NXOpen::Sustainability::CalculateScoresBuilder@endlink  
         @return calculate_scores_builder (@link CalculateScoresBuilder NXOpen.Sustainability.CalculateScoresBuilder@endlink):  calculate scores builder .
        """
        pass
    
    ##  Create a @link NXOpen::Sustainability::MapEnvironmentalMaterialBuilder NXOpen::Sustainability::MapEnvironmentalMaterialBuilder@endlink  
    ##  @return map_environmental_material_builder (@link MapEnvironmentalMaterialBuilder NXOpen.Sustainability.MapEnvironmentalMaterialBuilder@endlink):  @link NXOpen::Sustainability::MapEnvironmentalMaterialBuilder NXOpen::Sustainability::MapEnvironmentalMaterialBuilder@endlink  .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_sustainability (" Design for Sustainability")
    def CreateMapEnvironmentalMaterialBuilder(self) -> MapEnvironmentalMaterialBuilder:
        """
         Create a @link NXOpen::Sustainability::MapEnvironmentalMaterialBuilder NXOpen::Sustainability::MapEnvironmentalMaterialBuilder@endlink  
         @return map_environmental_material_builder (@link MapEnvironmentalMaterialBuilder NXOpen.Sustainability.MapEnvironmentalMaterialBuilder@endlink):  @link NXOpen::Sustainability::MapEnvironmentalMaterialBuilder NXOpen::Sustainability::MapEnvironmentalMaterialBuilder@endlink  .
        """
        pass
    
    ##  Update sustainability scores of the given part 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_sustainability (" Design for Sustainability")
    def UpdateSustainabilityScores(self) -> None:
        """
         Update sustainability scores of the given part 
        """
        pass
    
## @package NXOpen.Sustainability
## Classes, Enums and Structs under NXOpen.Sustainability namespace

##  @link CalculateScoresBuilderUnselectedSubtypeScoresOption NXOpen.Sustainability.CalculateScoresBuilderUnselectedSubtypeScoresOption @endlink is an alias for @link CalculateScoresBuilder.UnselectedSubtypeScoresOption NXOpen.Sustainability.CalculateScoresBuilder.UnselectedSubtypeScoresOption@endlink
CalculateScoresBuilderUnselectedSubtypeScoresOption = CalculateScoresBuilder.UnselectedSubtypeScoresOption


