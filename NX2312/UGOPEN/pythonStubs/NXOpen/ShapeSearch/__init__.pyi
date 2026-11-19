from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  This class manages Shape Search.  <br> To obtain an instance of this class, refer to @link NXOpen::PartCollection  NXOpen::PartCollection @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class SearchManager(NXOpen.Object): 
    """ This class manages Shape Search. """


    ##  Creates a @link NXOpen::ShapeSearch::ShapeSearchBuilder NXOpen::ShapeSearch::ShapeSearchBuilder@endlink  object. 
    ##  @return builder (@link ShapeSearchBuilder NXOpen.ShapeSearch.ShapeSearchBuilder@endlink):  ShapeSearchBuilder object .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: shape_search ("Shape Search")
    ##  the part 
    def CreateShapeSearchBuilder(part: NXOpen.Part) -> ShapeSearchBuilder:
        """
         Creates a @link NXOpen::ShapeSearch::ShapeSearchBuilder NXOpen::ShapeSearch::ShapeSearchBuilder@endlink  object. 
         @return builder (@link ShapeSearchBuilder NXOpen.ShapeSearch.ShapeSearchBuilder@endlink):  ShapeSearchBuilder object .
        """
        pass
    
import NXOpen
##  This class provides the methods to execute shape search and get the searched results.
##         The operation that this builder supports has three types: (set by @link ShapeSearch::ShapeSearchBuilder::SetSearchType ShapeSearch::ShapeSearchBuilder::SetSearchType@endlink )
##         <ol>
##            <li> Search by attributes.
##            <ul>
##               <li> @link ShapeSearch::ShapeSearchBuilder::SetInputAttributesName ShapeSearch::ShapeSearchBuilder::SetInputAttributesName@endlink  </li>
##               <li> @link ShapeSearch::ShapeSearchBuilder::SetInputAttributesFilter ShapeSearch::ShapeSearchBuilder::SetInputAttributesFilter@endlink  </li>
##            </ul>
##            </li>
##                
##            <li>Search by body combined attributes with shape similarity and shape size condition. Support multiple bodies.
##            <ul>
##               <li> @link ShapeSearch::ShapeSearchBuilder::InputBody ShapeSearch::ShapeSearchBuilder::InputBody@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetInputAttributesName ShapeSearch::ShapeSearchBuilder::SetInputAttributesName@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetInputAttributesFilter ShapeSearch::ShapeSearchBuilder::SetInputAttributesFilter@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetSearchShapeSimilarity ShapeSearch::ShapeSearchBuilder::SetSearchShapeSimilarity@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetSearchShapeSize ShapeSearch::ShapeSearchBuilder::SetSearchShapeSize@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetUseCustomShapeSize ShapeSearch::ShapeSearchBuilder::SetUseCustomShapeSize@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetCustomShapeSizeLowerLimit ShapeSearch::ShapeSearchBuilder::SetCustomShapeSizeLowerLimit@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetCustomShapeSizeUpperLimit ShapeSearch::ShapeSearchBuilder::SetCustomShapeSizeUpperLimit@endlink  </li>
##            </ul>
##            </li>
##                
##            <li>Search by part combined attributes with shape similarity and shape size condition. Support loaded part, OS part, Teamcenter part and component.
##            <ul>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetInputPart ShapeSearch::ShapeSearchBuilder::SetInputPart@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetInputAttributesName ShapeSearch::ShapeSearchBuilder::SetInputAttributesName@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetInputAttributesFilter ShapeSearch::ShapeSearchBuilder::SetInputAttributesFilter@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetReferenceSetName ShapeSearch::ShapeSearchBuilder::SetReferenceSetName@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetSearchShapeSimilarity ShapeSearch::ShapeSearchBuilder::SetSearchShapeSimilarity@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetSearchShapeSize ShapeSearch::ShapeSearchBuilder::SetSearchShapeSize@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetUseCustomShapeSize ShapeSearch::ShapeSearchBuilder::SetUseCustomShapeSize@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetCustomShapeSizeLowerLimit ShapeSearch::ShapeSearchBuilder::SetCustomShapeSizeLowerLimit@endlink  </li>
##                <li> @link ShapeSearch::ShapeSearchBuilder::SetCustomShapeSizeUpperLimit ShapeSearch::ShapeSearchBuilder::SetCustomShapeSizeUpperLimit@endlink  </li>
##            </ul>
##            </li>
##         </ol>
## 
##         When initialize builder, we will load all saved searches from work directory and add them to
##         search list. You can implement 
##         @link ShapeSearch::ShapeSearchBuilder::ExecuteSearch ShapeSearch::ShapeSearchBuilder::ExecuteSearch@endlink  to run the saved search.
## 
##         After define the search criteria, function @link ShapeSearch::ShapeSearchBuilder::ExecuteSearch ShapeSearch::ShapeSearchBuilder::ExecuteSearch@endlink  can search
##         the shape from database and return the searched results count and error message if fails.  The search is specified by 'searchName' parameter.
## 
##         The method @link ShapeSearch::ShapeSearchBuilder::GetResults ShapeSearch::ShapeSearchBuilder::GetResults@endlink   can get the specified results from database.         The range of results is specified by the parameters 'startResultId' and 'endResultId', the search is
##         specified by 'searchName' parameter.
## 
##         The method @link ShapeSearch::ShapeSearchBuilder::OpenResultPart ShapeSearch::ShapeSearchBuilder::OpenResultPart@endlink  can open the selected result part of the
##         specified search. The result is specified by 'resultId' parameter, the search is specified by 'searchName' parameter.
## 
##      <br> To create a new instance of this class, use @link NXOpen::ShapeSearch::SearchManager::CreateShapeSearchBuilder  NXOpen::ShapeSearch::SearchManager::CreateShapeSearchBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class ShapeSearchBuilder(NXOpen.Builder): 
    """ This class provides the methods to execute shape search and get the searched results.
        The operation that this builder supports has three types: (set by <ja_property_set>ShapeSearch.ShapeSearchBuilder.SearchType</ja_property_set>)
        <ol>
           <li> Search by attributes.
           <ul>
              <li> <ja_method>ShapeSearch.ShapeSearchBuilder.SetInputAttributesName</ja_method> </li>
              <li> <ja_method>ShapeSearch.ShapeSearchBuilder.SetInputAttributesFilter</ja_method> </li>
           </ul>
           </li>
               
           <li>Search by body combined attributes with shape similarity and shape size condition. Support multiple bodies.
           <ul>
              <li> <ja_property_get>ShapeSearch.ShapeSearchBuilder.InputBody</ja_property_get> </li>
               <li> <ja_method>ShapeSearch.ShapeSearchBuilder.SetInputAttributesName</ja_method> </li>
               <li> <ja_method>ShapeSearch.ShapeSearchBuilder.SetInputAttributesFilter</ja_method> </li>
               <li> <ja_property_set>ShapeSearch.ShapeSearchBuilder.SearchShapeSimilarity</ja_property_set> </li>
               <li> <ja_property_set>ShapeSearch.ShapeSearchBuilder.SearchShapeSize</ja_property_set> </li>
               <li> <ja_property_set>ShapeSearch.ShapeSearchBuilder.UseCustomShapeSize</ja_property_set> </li>
               <li> <ja_property_set>ShapeSearch.ShapeSearchBuilder.CustomShapeSizeLowerLimit</ja_property_set> </li>
               <li> <ja_property_set>ShapeSearch.ShapeSearchBuilder.CustomShapeSizeUpperLimit</ja_property_set> </li>
           </ul>
           </li>
               
           <li>Search by part combined attributes with shape similarity and shape size condition. Support loaded part, OS part, Teamcenter part and component.
           <ul>
               <li> <ja_property_set>ShapeSearch.ShapeSearchBuilder.InputPart</ja_property_set> </li>
               <li> <ja_method>ShapeSearch.ShapeSearchBuilder.SetInputAttributesName</ja_method> </li>
               <li> <ja_method>ShapeSearch.ShapeSearchBuilder.SetInputAttributesFilter</ja_method> </li>
               <li> <ja_property_set>ShapeSearch.ShapeSearchBuilder.ReferenceSetName</ja_property_set> </li>
               <li> <ja_property_set>ShapeSearch.ShapeSearchBuilder.SearchShapeSimilarity</ja_property_set> </li>
               <li> <ja_property_set>ShapeSearch.ShapeSearchBuilder.SearchShapeSize</ja_property_set> </li>
               <li> <ja_property_set>ShapeSearch.ShapeSearchBuilder.UseCustomShapeSize</ja_property_set> </li>
               <li> <ja_property_set>ShapeSearch.ShapeSearchBuilder.CustomShapeSizeLowerLimit</ja_property_set> </li>
               <li> <ja_property_set>ShapeSearch.ShapeSearchBuilder.CustomShapeSizeUpperLimit</ja_property_set> </li>
           </ul>
           </li>
        </ol>

        When initialize builder, we will load all saved searches from work directory and add them to
        search list. You can implement 
        <ja_method>ShapeSearch.ShapeSearchBuilder.ExecuteSearch</ja_method> to run the saved search.

        After define the search criteria, function <ja_method>ShapeSearch.ShapeSearchBuilder.ExecuteSearch</ja_method> can search
        the shape from database and return the searched results count and error message if fails.  The search is specified by 'searchName' parameter.

        The method <ja_method>ShapeSearch.ShapeSearchBuilder.GetResults</ja_method>  can get the specified results from database.         The range of results is specified by the parameters 'startResultId' and 'endResultId', the search is
        specified by 'searchName' parameter.

        The method <ja_method>ShapeSearch.ShapeSearchBuilder.OpenResultPart</ja_method> can open the selected result part of the
        specified search. The result is specified by 'resultId' parameter, the search is specified by 'searchName' parameter.

    """


    ##  The open part type enum 
    ##  Not set the opened part as display part 
    class OpenPartType(Enum):
        """
        Members Include: <NotSetDisplayPart> <SetDisplayPartOnlyWhenOpen> <AlwaysSetDisplayPart>
        """
        NotSetDisplayPart: int
        SetDisplayPartOnlyWhenOpen: int
        AlwaysSetDisplayPart: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShapeSearchBuilder.OpenPartType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The search type enum 
    ##  search by attributes 
    class SearchByType(Enum):
        """
        Members Include: <Attribute> <Body> <Part>
        """
        Attribute: int
        Body: int
        Part: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShapeSearchBuilder.SearchByType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The search shape similarity enum 
    ##  search with identical condition    
    class ShapeSimilarity(Enum):
        """
        Members Include: <Gradient1> <Gradient2> <Gradient3> <Gradient4> <Gradient5> <Gradient6> <Gradient7> <Gradient8> <Gradient9> <Gradient10>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShapeSearchBuilder.ShapeSimilarity:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The search shape size enum 
    ##  search with shape size 90%-110% condition 
    class ShapeSize(Enum):
        """
        Members Include: <P90P110> <P80P120> <P70P130> <P50P200> <P25P400>
        """
        P90P110: int
        P80P120: int
        P70P130: int
        P50P200: int
        P25P400: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShapeSearchBuilder.ShapeSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) CustomShapeSizeLowerLimit
    ##   the custom shape size lower limit to be set for search.  
    ##    It is used only when use custom shape size is true.
    ##             It must be greater than zero and less than upper limit.   
    ##  
    ## Getter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def CustomShapeSizeLowerLimit(self) -> int:
        """
        Getter for property: (int) CustomShapeSizeLowerLimit
          the custom shape size lower limit to be set for search.  
           It is used only when use custom shape size is true.
                    It must be greater than zero and less than upper limit.   
         
        """
        pass
    
    ## Setter for property: (int) CustomShapeSizeLowerLimit

    ##   the custom shape size lower limit to be set for search.  
    ##    It is used only when use custom shape size is true.
    ##             It must be greater than zero and less than upper limit.   
    ##  
    ## Setter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @CustomShapeSizeLowerLimit.setter
    def CustomShapeSizeLowerLimit(self, customShapeSizeLowerLimit: int):
        """
        Setter for property: (int) CustomShapeSizeLowerLimit
          the custom shape size lower limit to be set for search.  
           It is used only when use custom shape size is true.
                    It must be greater than zero and less than upper limit.   
         
        """
        pass
    
    ## Getter for property: (int) CustomShapeSizeUpperLimit
    ##   the custom shape size upper limit to be set for search.  
    ##    It is used only when use custom shape size is true.
    ##             It must be greater than lower limit.   
    ##  
    ## Getter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def CustomShapeSizeUpperLimit(self) -> int:
        """
        Getter for property: (int) CustomShapeSizeUpperLimit
          the custom shape size upper limit to be set for search.  
           It is used only when use custom shape size is true.
                    It must be greater than lower limit.   
         
        """
        pass
    
    ## Setter for property: (int) CustomShapeSizeUpperLimit

    ##   the custom shape size upper limit to be set for search.  
    ##    It is used only when use custom shape size is true.
    ##             It must be greater than lower limit.   
    ##  
    ## Setter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @CustomShapeSizeUpperLimit.setter
    def CustomShapeSizeUpperLimit(self, customShapeSizeUpperLimit: int):
        """
        Setter for property: (int) CustomShapeSizeUpperLimit
          the custom shape size upper limit to be set for search.  
           It is used only when use custom shape size is true.
                    It must be greater than lower limit.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) InputBody
    ##   the input body to be searched   
    ##     
    ##  
    ## Getter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def InputBody(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) InputBody
          the input body to be searched   
            
         
        """
        pass
    
    ## Getter for property: (str) InputPart
    ##   the input part to be searched   
    ##     
    ##  
    ## Getter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return str
    @property
    def InputPart(self) -> str:
        """
        Getter for property: (str) InputPart
          the input part to be searched   
            
         
        """
        pass
    
    ## Setter for property: (str) InputPart

    ##   the input part to be searched   
    ##     
    ##  
    ## Setter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @InputPart.setter
    def InputPart(self, inputPart: str):
        """
        Setter for property: (str) InputPart
          the input part to be searched   
            
         
        """
        pass
    
    ## Getter for property: (str) ReferenceSetName
    ##   the part reference set name to be set for search   
    ##     
    ##  
    ## Getter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return str
    @property
    def ReferenceSetName(self) -> str:
        """
        Getter for property: (str) ReferenceSetName
          the part reference set name to be set for search   
            
         
        """
        pass
    
    ## Setter for property: (str) ReferenceSetName

    ##   the part reference set name to be set for search   
    ##     
    ##  
    ## Setter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ReferenceSetName.setter
    def ReferenceSetName(self, referenceSetName: str):
        """
        Setter for property: (str) ReferenceSetName
          the part reference set name to be set for search   
            
         
        """
        pass
    
    ## Getter for property: (@link ShapeSearchBuilder.ShapeSimilarity NXOpen.ShapeSearch.ShapeSearchBuilder.ShapeSimilarity@endlink) SearchShapeSimilarity
    ##   the shape similarity to be set for search   
    ##     
    ##  
    ## Getter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return ShapeSearchBuilder.ShapeSimilarity
    @property
    def SearchShapeSimilarity(self) -> ShapeSearchBuilder.ShapeSimilarity:
        """
        Getter for property: (@link ShapeSearchBuilder.ShapeSimilarity NXOpen.ShapeSearch.ShapeSearchBuilder.ShapeSimilarity@endlink) SearchShapeSimilarity
          the shape similarity to be set for search   
            
         
        """
        pass
    
    ## Setter for property: (@link ShapeSearchBuilder.ShapeSimilarity NXOpen.ShapeSearch.ShapeSearchBuilder.ShapeSimilarity@endlink) SearchShapeSimilarity

    ##   the shape similarity to be set for search   
    ##     
    ##  
    ## Setter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @SearchShapeSimilarity.setter
    def SearchShapeSimilarity(self, searchShapeSimilarity: ShapeSearchBuilder.ShapeSimilarity):
        """
        Setter for property: (@link ShapeSearchBuilder.ShapeSimilarity NXOpen.ShapeSearch.ShapeSearchBuilder.ShapeSimilarity@endlink) SearchShapeSimilarity
          the shape similarity to be set for search   
            
         
        """
        pass
    
    ## Getter for property: (@link ShapeSearchBuilder.ShapeSize NXOpen.ShapeSearch.ShapeSearchBuilder.ShapeSize@endlink) SearchShapeSize
    ##   the shape size to be set for search.  
    ##    It is used only when use custom shape size is false.   
    ##  
    ## Getter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return ShapeSearchBuilder.ShapeSize
    @property
    def SearchShapeSize(self) -> ShapeSearchBuilder.ShapeSize:
        """
        Getter for property: (@link ShapeSearchBuilder.ShapeSize NXOpen.ShapeSearch.ShapeSearchBuilder.ShapeSize@endlink) SearchShapeSize
          the shape size to be set for search.  
           It is used only when use custom shape size is false.   
         
        """
        pass
    
    ## Setter for property: (@link ShapeSearchBuilder.ShapeSize NXOpen.ShapeSearch.ShapeSearchBuilder.ShapeSize@endlink) SearchShapeSize

    ##   the shape size to be set for search.  
    ##    It is used only when use custom shape size is false.   
    ##  
    ## Setter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @SearchShapeSize.setter
    def SearchShapeSize(self, searchShapeSize: ShapeSearchBuilder.ShapeSize):
        """
        Setter for property: (@link ShapeSearchBuilder.ShapeSize NXOpen.ShapeSearch.ShapeSearchBuilder.ShapeSize@endlink) SearchShapeSize
          the shape size to be set for search.  
           It is used only when use custom shape size is false.   
         
        """
        pass
    
    ## Getter for property: (@link ShapeSearchBuilder.SearchByType NXOpen.ShapeSearch.ShapeSearchBuilder.SearchByType@endlink) SearchType
    ##   the search type   
    ##     
    ##  
    ## Getter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return ShapeSearchBuilder.SearchByType
    @property
    def SearchType(self) -> ShapeSearchBuilder.SearchByType:
        """
        Getter for property: (@link ShapeSearchBuilder.SearchByType NXOpen.ShapeSearch.ShapeSearchBuilder.SearchByType@endlink) SearchType
          the search type   
            
         
        """
        pass
    
    ## Setter for property: (@link ShapeSearchBuilder.SearchByType NXOpen.ShapeSearch.ShapeSearchBuilder.SearchByType@endlink) SearchType

    ##   the search type   
    ##     
    ##  
    ## Setter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @SearchType.setter
    def SearchType(self, searchType: ShapeSearchBuilder.SearchByType):
        """
        Setter for property: (@link ShapeSearchBuilder.SearchByType NXOpen.ShapeSearch.ShapeSearchBuilder.SearchByType@endlink) SearchType
          the search type   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseCustomShapeSize
    ##   the use custom shape size to control use shape size option or custom shape size   
    ##     
    ##  
    ## Getter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def UseCustomShapeSize(self) -> bool:
        """
        Getter for property: (bool) UseCustomShapeSize
          the use custom shape size to control use shape size option or custom shape size   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseCustomShapeSize

    ##   the use custom shape size to control use shape size option or custom shape size   
    ##     
    ##  
    ## Setter License requirements: shape_search ("Shape Search")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @UseCustomShapeSize.setter
    def UseCustomShapeSize(self, useCustomShapeSize: bool):
        """
        Setter for property: (bool) UseCustomShapeSize
          the use custom shape size to control use shape size option or custom shape size   
            
         
        """
        pass
    
    ##  Execute new search or saved search and output error message if error. 
    ##  @return A tuple consisting of (nTotalResults, errorMessage). 
    ##  - nTotalResults is: int. Search result total number .
    ##  - errorMessage is: str. Search error message .

    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: shape_search ("Shape Search")
    ##  True is executing new search, False is executing saved search 
    @staticmethod
    def ExecuteSearch(builder: ShapeSearchBuilder, isNew: bool, searchName: str) -> Tuple[int, str]:
        """
         Execute new search or saved search and output error message if error. 
         @return A tuple consisting of (nTotalResults, errorMessage). 
         - nTotalResults is: int. Search result total number .
         - errorMessage is: str. Search error message .

        """
        pass
    
    ##  The input attributes filter to be searched 
    ##  @return inputAttributesFilter (List[str]): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: shape_search ("Shape Search")
    @staticmethod
    def GetInputAttributesFilter(builder: ShapeSearchBuilder) -> List[str]:
        """
         The input attributes filter to be searched 
         @return inputAttributesFilter (List[str]): .
        """
        pass
    
    ##  The input attributes name to be searched 
    ##  @return inputAttributesName (List[str]): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: shape_search ("Shape Search")
    @staticmethod
    def GetInputAttributesName(builder: ShapeSearchBuilder) -> List[str]:
        """
         The input attributes name to be searched 
         @return inputAttributesName (List[str]): .
        """
        pass
    
    ##  Get specified search results from database. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: shape_search ("Shape Search")
    ##  Search name 
    def GetResults(builder: ShapeSearchBuilder, searchName: str, startResultId: int, endResultId: int) -> None:
        """
         Get specified search results from database. 
        """
        pass
    
    ##  Open the searched result part. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: shape_search ("Shape Search")
    ##  Open part type 
    def OpenResultPart(builder: ShapeSearchBuilder, openPartType: ShapeSearchBuilder.OpenPartType, searchName: str, resultId: int) -> None:
        """
         Open the searched result part. 
        """
        pass
    
    ##  The input attributes filter to be searched 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: shape_search ("Shape Search")
    ##  Search attributes filter 
    def SetInputAttributesFilter(builder: ShapeSearchBuilder, inputAttributesFilter: List[str]) -> None:
        """
         The input attributes filter to be searched 
        """
        pass
    
    ##  The input attributes name to be searched 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: shape_search ("Shape Search")
    ##  Search attributes Name 
    def SetInputAttributesName(builder: ShapeSearchBuilder, inputAttributesName: List[str]) -> None:
        """
         The input attributes name to be searched 
        """
        pass
    
## @package NXOpen.ShapeSearch
## Classes, Enums and Structs under NXOpen.ShapeSearch namespace

##  @link ShapeSearchBuilderOpenPartType NXOpen.ShapeSearch.ShapeSearchBuilderOpenPartType @endlink is an alias for @link ShapeSearchBuilder.OpenPartType NXOpen.ShapeSearch.ShapeSearchBuilder.OpenPartType@endlink
ShapeSearchBuilderOpenPartType = ShapeSearchBuilder.OpenPartType


##  @link ShapeSearchBuilderSearchByType NXOpen.ShapeSearch.ShapeSearchBuilderSearchByType @endlink is an alias for @link ShapeSearchBuilder.SearchByType NXOpen.ShapeSearch.ShapeSearchBuilder.SearchByType@endlink
ShapeSearchBuilderSearchByType = ShapeSearchBuilder.SearchByType


##  @link ShapeSearchBuilderShapeSimilarity NXOpen.ShapeSearch.ShapeSearchBuilderShapeSimilarity @endlink is an alias for @link ShapeSearchBuilder.ShapeSimilarity NXOpen.ShapeSearch.ShapeSearchBuilder.ShapeSimilarity@endlink
ShapeSearchBuilderShapeSimilarity = ShapeSearchBuilder.ShapeSimilarity


##  @link ShapeSearchBuilderShapeSize NXOpen.ShapeSearch.ShapeSearchBuilderShapeSize @endlink is an alias for @link ShapeSearchBuilder.ShapeSize NXOpen.ShapeSearch.ShapeSearchBuilder.ShapeSize@endlink
ShapeSearchBuilderShapeSize = ShapeSearchBuilder.ShapeSize


