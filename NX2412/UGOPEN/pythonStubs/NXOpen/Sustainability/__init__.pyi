from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class CalculateScoresBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Sustainability.CalculateScoresBuilder used to calculate sustainability scores.
    """
    class UnselectedSubtypeScoresOption(Enum):
        """
        Members Include: 
         |Delete| 
         |Retain| 

        """
        Delete: int
        Retain: int
        @staticmethod
        def ValueOf(value: int) -> CalculateScoresBuilder.UnselectedSubtypeScoresOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SubtypeNominal(self) -> bool:
        """
        Getter for property: (bool) SubtypeNominal
         Returns the subtype nominal   
            
         
        """
        pass
    @SubtypeNominal.setter
    def SubtypeNominal(self, subtypeNominal: bool):
        """
        Setter for property: (bool) SubtypeNominal
         Returns the subtype nominal   
            
         
        """
        pass
    @property
    def SubtypeRecycled(self) -> bool:
        """
        Getter for property: (bool) SubtypeRecycled
         Returns the subtype recycled   
            
         
        """
        pass
    @SubtypeRecycled.setter
    def SubtypeRecycled(self, subtypeRecycled: bool):
        """
        Setter for property: (bool) SubtypeRecycled
         Returns the subtype recycled   
            
         
        """
        pass
    @property
    def SubtypeRenewable(self) -> bool:
        """
        Getter for property: (bool) SubtypeRenewable
         Returns the subtype renewable   
            
         
        """
        pass
    @SubtypeRenewable.setter
    def SubtypeRenewable(self, subtypeRenewable: bool):
        """
        Setter for property: (bool) SubtypeRenewable
         Returns the subtype renewable   
            
         
        """
        pass
    @property
    def UnselectedSubtypeScores(self) -> CalculateScoresBuilder.UnselectedSubtypeScoresOption:
        """
        Getter for property: ( CalculateScoresBuilder.UnselectedSubtypeScoresOption NXOpen.Sus) UnselectedSubtypeScores
         Returns the unselected subtype scores option  
            
         
        """
        pass
    @UnselectedSubtypeScores.setter
    def UnselectedSubtypeScores(self, option: CalculateScoresBuilder.UnselectedSubtypeScoresOption):
        """
        Setter for property: ( CalculateScoresBuilder.UnselectedSubtypeScoresOption NXOpen.Sus) UnselectedSubtypeScores
         Returns the unselected subtype scores option  
            
         
        """
        pass
    def GetMaterialsOfBody(self, body: NXOpen.Body) -> Tuple[str, str]:
        """
         Get the materials of body 
         Returns A tuple consisting of (environmentMaterial, physicalMaterial). 
         - environmentMaterial is: str.
         - physicalMaterial is: str.

        """
        pass
    def GetScoresOfBody(self, body: NXOpen.Body, subtype: str) -> Tuple[List[float], List[str]]:
        """
         Get the scores of body 
         Returns A tuple consisting of (scoreValues, scoreTitles). 
         - scoreValues is: List[float].
         - scoreTitles is: List[str].

        """
        pass
import NXOpen
class MakeProcessBuilder(NXOpen.Builder): 
    """ 
    Represents a NXOpen.Sustainability.MakeProcessBuilder used to make process.
    """
    @property
    def BodySelectOption(self) -> bool:
        """
        Getter for property: (bool) BodySelectOption
         Returns the body select option of make processes   
            
         
        """
        pass
    @BodySelectOption.setter
    def BodySelectOption(self, bodySelectOption: bool):
        """
        Setter for property: (bool) BodySelectOption
         Returns the body select option of make processes   
            
         
        """
        pass
    def ShowInfo(self) -> None:
        """
         Show information of make processes 
        """
        pass
import NXOpen
class MapEnvironmentalMaterialBuilder(NXOpen.Builder): 
    """ 
    Represents a NXOpen.Sustainability.MapEnvironmentalMaterialBuilder used to map environmental materials.
    """
    @property
    def LibFileBrowser(self) -> str:
        """
        Getter for property: (str) LibFileBrowser
         Returns the environmental material file browser   
            
         
        """
        pass
    @LibFileBrowser.setter
    def LibFileBrowser(self, foldername: str):
        """
        Setter for property: (str) LibFileBrowser
         Returns the environmental material file browser   
            
         
        """
        pass
    @property
    def MappingFileBrowser(self) -> str:
        """
        Getter for property: (str) MappingFileBrowser
         Returns the environmental material mapping file browser   
            
         
        """
        pass
    @MappingFileBrowser.setter
    def MappingFileBrowser(self, foldername: str):
        """
        Setter for property: (str) MappingFileBrowser
         Returns the environmental material mapping file browser   
            
         
        """
        pass
    def DownloadButton(self) -> None:
        """
         Download the environmental material files from the web service 
        """
        pass
    def InfoButton(self) -> None:
        """
         Information of mapping between physical and environmental materials 
        """
        pass
import NXOpen
class SustainabilityManager(NXOpen.Object): 
    """
     Represents an NX NXOpen.Sustainability.SustainabilityManager object.
    """
    def CreateCalculateScoresBuilder(self) -> CalculateScoresBuilder:
        """
         Create a NXOpen.Sustainability.CalculateScoresBuilder 
         Returns calculate_scores_builder ( CalculateScoresBuilder NXOpen.Sus):  calculate scores builder .
        """
        pass
    def CreateMakeProcessBuilder(self) -> MakeProcessBuilder:
        """
         Create a NXOpen.Sustainability.MakeProcessBuilder 
         Returns make_process_builder ( MakeProcessBuilder NXOpen.Sus):  NXOpen.Sustainability.MakeProcessBuilder .
        """
        pass
    def CreateMapEnvironmentalMaterialBuilder(self) -> MapEnvironmentalMaterialBuilder:
        """
         Create a NXOpen.Sustainability.MapEnvironmentalMaterialBuilder 
         Returns map_environmental_material_builder ( MapEnvironmentalMaterialBuilder NXOpen.Sus):  NXOpen.Sustainability.MapEnvironmentalMaterialBuilder .
        """
        pass
    def UpdateSustainabilityScores(self) -> None:
        """
         Update sustainability scores of the given part 
        """
        pass
