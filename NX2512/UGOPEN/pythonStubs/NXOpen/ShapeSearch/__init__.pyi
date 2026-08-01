from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class SearchManager(NXOpen.Object): 
    """ This class manages Shape Search. """
    def CreateShapeSearchBuilder(part: NXOpen.Part) -> ShapeSearchBuilder:
        """
         Creates a NXOpen.ShapeSearch.ShapeSearchBuilder object. 
         Returns builder ( ShapeSearchBuilder NXOpen.S):  ShapeSearchBuilder object .
        """
        pass
import NXOpen
class ShapeSearchBuilder(NXOpen.Builder): 
    """ This class provides the methods to execute shape search and get the searched results.
        The operation that this builder supports has three types: (set by ShapeSearch.ShapeSearchBuilder.SearchType)
        
            Search by attributes.
           
               ShapeSearch.ShapeSearchBuilder.SetInputAttributesName 
               ShapeSearch.ShapeSearchBuilder.SetInputAttributesFilter 
           
           
               
           Search by body combined attributes with shape similarity and shape size condition. Support multiple bodies.
           
               ShapeSearch.ShapeSearchBuilder.InputBody 
                ShapeSearch.ShapeSearchBuilder.SetInputAttributesName 
                ShapeSearch.ShapeSearchBuilder.SetInputAttributesFilter 
                ShapeSearch.ShapeSearchBuilder.SearchShapeSimilarity 
                ShapeSearch.ShapeSearchBuilder.SearchShapeSize 
                ShapeSearch.ShapeSearchBuilder.UseCustomShapeSize 
                ShapeSearch.ShapeSearchBuilder.CustomShapeSizeLowerLimit 
                ShapeSearch.ShapeSearchBuilder.CustomShapeSizeUpperLimit 
           
           
               
           Search by part combined attributes with shape similarity and shape size condition. Support loaded part, OS part, Teamcenter part and component.
           
                ShapeSearch.ShapeSearchBuilder.InputPart 
                ShapeSearch.ShapeSearchBuilder.SetInputAttributesName 
                ShapeSearch.ShapeSearchBuilder.SetInputAttributesFilter 
                ShapeSearch.ShapeSearchBuilder.ReferenceSetName 
                ShapeSearch.ShapeSearchBuilder.SearchShapeSimilarity 
                ShapeSearch.ShapeSearchBuilder.SearchShapeSize 
                ShapeSearch.ShapeSearchBuilder.UseCustomShapeSize 
                ShapeSearch.ShapeSearchBuilder.CustomShapeSizeLowerLimit 
                ShapeSearch.ShapeSearchBuilder.CustomShapeSizeUpperLimit 
           
           
        

        When initialize builder, we will load all saved searches from work directory and add them to
        search list. You can implement 
        ShapeSearch.ShapeSearchBuilder.ExecuteSearch to run the saved search.

        After define the search criteria, function ShapeSearch.ShapeSearchBuilder.ExecuteSearch can search
        the shape from database and return the searched results count and error message if fails.  The search is specified by 'searchName' parameter.

        The method ShapeSearch.ShapeSearchBuilder.GetResults  can get the specified results from database.         The range of results is specified by the parameters 'startResultId' and 'endResultId', the search is
        specified by 'searchName' parameter.

        The method ShapeSearch.ShapeSearchBuilder.OpenResultPart can open the selected result part of the
        specified search. The result is specified by 'resultId' parameter, the search is specified by 'searchName' parameter.

    """
    class OpenPartType(Enum):
        """
        Members Include: 
         |NotSetDisplayPart|  Not set the opened part as display part 
         |SetDisplayPartOnlyWhenOpen|  Set the opened part as display part only when it doesn't exist in the session 
         |AlwaysSetDisplayPart|  Always set the opened part as display part whether it exists in the session 

        """
        NotSetDisplayPart: int
        SetDisplayPartOnlyWhenOpen: int
        AlwaysSetDisplayPart: int
        @staticmethod
        def ValueOf(value: int) -> ShapeSearchBuilder.OpenPartType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SearchByType(Enum):
        """
        Members Include: 
         |Attribute|  search by attributes 
         |Body|  search by bodies     
         |Part|  search by part       

        """
        Attribute: int
        Body: int
        Part: int
        @staticmethod
        def ValueOf(value: int) -> ShapeSearchBuilder.SearchByType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShapeSimilarity(Enum):
        """
        Members Include: 
         |Gradient1|  search with identical condition    
         |Gradient2| 
         |Gradient3| 
         |Gradient4| 
         |Gradient5| 
         |Gradient6|  search with very similar condition 
         |Gradient7| 
         |Gradient8| 
         |Gradient9| 
         |Gradient10|  search with similar condition      

        """
        Gradient1: int
        Gradient2: int
        Gradient3: int
        Gradient4: int
        Gradient5: int
        Gradient6: int
        Gradient7: int
        Gradient8: int
        Gradient9: int
        Gradient10: int
        @staticmethod
        def ValueOf(value: int) -> ShapeSearchBuilder.ShapeSimilarity:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShapeSize(Enum):
        """
        Members Include: 
         |P90P110|  search with shape size 90%-110% condition 
         |P80P120|  search with shape size 80%-120% condition 
         |P70P130|  search with shape size 70%-130% condition 
         |P50P200|  search with shape size 50%-200% condition 
         |P25P400|  search with shape size 25%-400% condition 

        """
        P90P110: int
        P80P120: int
        P70P130: int
        P50P200: int
        P25P400: int
        @staticmethod
        def ValueOf(value: int) -> ShapeSearchBuilder.ShapeSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CustomShapeSizeLowerLimit(self) -> int:
        """
        Getter for property: (int) CustomShapeSizeLowerLimit
         Returns the custom shape size lower limit to be set for search.  
           It is used only when use custom shape size is true.
                    It must be greater than zero and less than upper limit.   
         
        """
        pass
    @CustomShapeSizeLowerLimit.setter
    def CustomShapeSizeLowerLimit(self, customShapeSizeLowerLimit: int):
        """
        Setter for property: (int) CustomShapeSizeLowerLimit
         Returns the custom shape size lower limit to be set for search.  
           It is used only when use custom shape size is true.
                    It must be greater than zero and less than upper limit.   
         
        """
        pass
    @property
    def CustomShapeSizeUpperLimit(self) -> int:
        """
        Getter for property: (int) CustomShapeSizeUpperLimit
         Returns the custom shape size upper limit to be set for search.  
           It is used only when use custom shape size is true.
                    It must be greater than lower limit.   
         
        """
        pass
    @CustomShapeSizeUpperLimit.setter
    def CustomShapeSizeUpperLimit(self, customShapeSizeUpperLimit: int):
        """
        Setter for property: (int) CustomShapeSizeUpperLimit
         Returns the custom shape size upper limit to be set for search.  
           It is used only when use custom shape size is true.
                    It must be greater than lower limit.   
         
        """
        pass
    @property
    def InputBody(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) InputBody
         Returns the input body to be searched   
            
         
        """
        pass
    @property
    def InputPart(self) -> str:
        """
        Getter for property: (str) InputPart
         Returns the input part to be searched   
            
         
        """
        pass
    @InputPart.setter
    def InputPart(self, inputPart: str):
        """
        Setter for property: (str) InputPart
         Returns the input part to be searched   
            
         
        """
        pass
    @property
    def ReferenceSetName(self) -> str:
        """
        Getter for property: (str) ReferenceSetName
         Returns the part reference set name to be set for search   
            
         
        """
        pass
    @ReferenceSetName.setter
    def ReferenceSetName(self, referenceSetName: str):
        """
        Setter for property: (str) ReferenceSetName
         Returns the part reference set name to be set for search   
            
         
        """
        pass
    @property
    def SearchShapeSimilarity(self) -> ShapeSearchBuilder.ShapeSimilarity:
        """
        Getter for property: ( ShapeSearchBuilder.ShapeSimilarity NXOpen.S) SearchShapeSimilarity
         Returns the shape similarity to be set for search   
            
         
        """
        pass
    @SearchShapeSimilarity.setter
    def SearchShapeSimilarity(self, searchShapeSimilarity: ShapeSearchBuilder.ShapeSimilarity):
        """
        Setter for property: ( ShapeSearchBuilder.ShapeSimilarity NXOpen.S) SearchShapeSimilarity
         Returns the shape similarity to be set for search   
            
         
        """
        pass
    @property
    def SearchShapeSize(self) -> ShapeSearchBuilder.ShapeSize:
        """
        Getter for property: ( ShapeSearchBuilder.ShapeSize NXOpen.S) SearchShapeSize
         Returns the shape size to be set for search.  
           It is used only when use custom shape size is false.   
         
        """
        pass
    @SearchShapeSize.setter
    def SearchShapeSize(self, searchShapeSize: ShapeSearchBuilder.ShapeSize):
        """
        Setter for property: ( ShapeSearchBuilder.ShapeSize NXOpen.S) SearchShapeSize
         Returns the shape size to be set for search.  
           It is used only when use custom shape size is false.   
         
        """
        pass
    @property
    def SearchType(self) -> ShapeSearchBuilder.SearchByType:
        """
        Getter for property: ( ShapeSearchBuilder.SearchByType NXOpen.S) SearchType
         Returns the search type   
            
         
        """
        pass
    @SearchType.setter
    def SearchType(self, searchType: ShapeSearchBuilder.SearchByType):
        """
        Setter for property: ( ShapeSearchBuilder.SearchByType NXOpen.S) SearchType
         Returns the search type   
            
         
        """
        pass
    @property
    def UseCustomShapeSize(self) -> bool:
        """
        Getter for property: (bool) UseCustomShapeSize
         Returns the use custom shape size to control use shape size option or custom shape size   
            
         
        """
        pass
    @UseCustomShapeSize.setter
    def UseCustomShapeSize(self, useCustomShapeSize: bool):
        """
        Setter for property: (bool) UseCustomShapeSize
         Returns the use custom shape size to control use shape size option or custom shape size   
            
         
        """
        pass
    def ExecuteSearch(self, isNew: bool, searchName: str) -> Tuple[int, str]:
        """
         Execute new search or saved search and output error message if error. 
         Returns A tuple consisting of (nTotalResults, errorMessage). 
         - nTotalResults is: int. Search result total number .
         - errorMessage is: str. Search error message .

        """
        pass
    def GetInputAttributesFilter(self) -> List[str]:
        """
         The input attributes filter to be searched 
         Returns inputAttributesFilter (List[str]): .
        """
        pass
    def GetInputAttributesName(self) -> List[str]:
        """
         The input attributes name to be searched 
         Returns inputAttributesName (List[str]): .
        """
        pass
    def GetResults(self, searchName: str, startResultId: int, endResultId: int) -> None:
        """
         Get specified search results from database. 
        """
        pass
    def OpenResultPart(self, openPartType: ShapeSearchBuilder.OpenPartType, searchName: str, resultId: int) -> None:
        """
         Open the searched result part. 
        """
        pass
    def SetInputAttributesFilter(self, inputAttributesFilter: List[str]) -> None:
        """
         The input attributes filter to be searched 
        """
        pass
    def SetInputAttributesName(self, inputAttributesName: List[str]) -> None:
        """
         The input attributes name to be searched 
        """
        pass
