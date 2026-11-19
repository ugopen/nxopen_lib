from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents an Acceleration type load in the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  context.  <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::EnvironmentLoadBuilder  NXOpen::DesignSimulation::EnvironmentLoadBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class Acceleration(NXOpen.NXObject): 
    """ Represents an Acceleration type load in the <ja_class>NXOpen.DesignSimulation.Study</ja_class> context. """


    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
    ##  Returns the direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Direction(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
         Returns the direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Magnitude
    ##  Returns the magnitude   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Magnitude(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Magnitude
         Returns the magnitude   
            
         
        """
        pass
    
import NXOpen
##  Represents analysis results for an @link NXOpen::DesignSimulation::AnalysisBody NXOpen::DesignSimulation::AnalysisBody@endlink .  <br> Analysis results are created internally by the owning Study  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class AnalysisBodyResults(NXOpen.NXObject): 
    """ Represents analysis results for an <ja_class>NXOpen.DesignSimulation.AnalysisBody</ja_class>. """


    ##  Represents a triangular facet with ordered indices of its vertices. 
    ## @link AnalysisBodyResultsFacet_Struct NXOpen.DesignSimulation.AnalysisBodyResultsFacet_Struct@endlink is an alias for @link AnalysisBodyResults.Facet NXOpen.DesignSimulation.AnalysisBodyResults.Facet@endlink.
    class Facet:
        """
         Represents a triangular facet with ordered indices of its vertices. 
        @link AnalysisBodyResultsFacet_Struct NXOpen.DesignSimulation.AnalysisBodyResultsFacet_Struct@endlink is an alias for @link AnalysisBodyResults.Facet NXOpen.DesignSimulation.AnalysisBodyResults.Facet@endlink.
        """
        ## Getter for property :(int) V1
        ## vertex 1
        ## @return int
        @property
        def V1(self) -> int:
            """
            Getter for property V1
            vertex 1

            """
            pass
        
        ## Setter for property :(int) V1
        @V1.setter
        def V1(self, value: int):
            """
            Getter for property V1
            vertex 1
            Setter for property V1
            vertex 1

            """
            pass
        
        ## Getter for property :(int) V2
        ## vertex 2
        ## @return int
        @property
        def V2(self) -> int:
            """
            Getter for property V2
            vertex 2

            """
            pass
        
        ## Setter for property :(int) V2
        @V2.setter
        def V2(self, value: int):
            """
            Getter for property V2
            vertex 2
            Setter for property V2
            vertex 2

            """
            pass
        
        ## Getter for property :(int) V3
        ## vertex 3
        ## @return int
        @property
        def V3(self) -> int:
            """
            Getter for property V3
            vertex 3

            """
            pass
        
        ## Setter for property :(int) V3
        @V3.setter
        def V3(self, value: int):
            """
            Getter for property V3
            vertex 3
            Setter for property V3
            vertex 3

            """
            pass
        
    
    
    ## Getter for property: (bool) IsBlanked
    ##  Returns the blank status of this analysis body result.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def IsBlanked(self) -> bool:
        """
        Getter for property: (bool) IsBlanked
         Returns the blank status of this analysis body result.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfContourFacets
    ##  Returns the number of facets in the analysis results contour   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def NumberOfContourFacets(self) -> int:
        """
        Getter for property: (int) NumberOfContourFacets
         Returns the number of facets in the analysis results contour   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfContourVertices
    ##  Returns the number of vertices in the analysis results contour   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def NumberOfContourVertices(self) -> int:
        """
        Getter for property: (int) NumberOfContourVertices
         Returns the number of vertices in the analysis results contour   
            
         
        """
        pass
    
    ##  Blanks the analysis body result. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def Blank(self) -> None:
        """
         Blanks the analysis body result. 
        """
        pass
    
    ##  Get facet at given index. The index must be between 0 and @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourFacets NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourFacets @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourFacets NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourFacets @endlink . 
    ##  @return facet (@link AnalysisBodyResults.Facet NXOpen.DesignSimulation.AnalysisBodyResults.Facet@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetContourFacetAt(self, index: int) -> AnalysisBodyResults.Facet:
        """
         Get facet at given index. The index must be between 0 and @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourFacets NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourFacets @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourFacets NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourFacets @endlink . 
         @return facet (@link AnalysisBodyResults.Facet NXOpen.DesignSimulation.AnalysisBodyResults.Facet@endlink): .
        """
        pass
    
    ##  Gets all the facets (triangular) in the analysis results contour. Count should match @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourFacets NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourFacets @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourFacets NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourFacets @endlink . 
    ##  @return facets (@link AnalysisBodyResults.Facet List[NXOpen.DesignSimulation.AnalysisBodyResults.Facet]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetContourFacets(self) -> List[AnalysisBodyResults.Facet]:
        """
         Gets all the facets (triangular) in the analysis results contour. Count should match @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourFacets NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourFacets @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourFacets NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourFacets @endlink . 
         @return facets (@link AnalysisBodyResults.Facet List[NXOpen.DesignSimulation.AnalysisBodyResults.Facet]@endlink): .
        """
        pass
    
    ##  Get vertex coordinates at given index. The index must be between 0 and @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink . 
    ##  @return vertex (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetContourVertexAt(self, index: int) -> NXOpen.Point3d:
        """
         Get vertex coordinates at given index. The index must be between 0 and @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink . 
         @return vertex (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
        """
        pass
    
    ##  Gets all the vertices in the analysis results contour. Count should match @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink . 
    ##  @return vertices (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetContourVertices(self) -> List[NXOpen.Point3d]:
        """
         Gets all the vertices in the analysis results contour. Count should match @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink . 
         @return vertices (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink): .
        """
        pass
    
    ##  Returns the analysis result data per @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink  in the owning @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink .
    ##             @link NXOpen::DesignSimulation::AnalysisBodySubcaseResults NXOpen::DesignSimulation::AnalysisBodySubcaseResults@endlink  will have results for @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink  vertices. 
    ##  @return subcaseResults (@link AnalysisBodySubcaseResults List[NXOpen.DesignSimulation.AnalysisBodySubcaseResults]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetSubcaseResults(self) -> List[AnalysisBodySubcaseResults]:
        """
         Returns the analysis result data per @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink  in the owning @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink .
                    @link NXOpen::DesignSimulation::AnalysisBodySubcaseResults NXOpen::DesignSimulation::AnalysisBodySubcaseResults@endlink  will have results for @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink  vertices. 
         @return subcaseResults (@link AnalysisBodySubcaseResults List[NXOpen.DesignSimulation.AnalysisBodySubcaseResults]@endlink): .
        """
        pass
    
    ##  Unblanks the analysis body result. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def Unblank(self) -> None:
        """
         Unblanks the analysis body result. 
        """
        pass
    
import NXOpen
##  Represents analysis results for an @link NXOpen::DesignSimulation::AnalysisBody NXOpen::DesignSimulation::AnalysisBody@endlink  per @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink  in the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  context.  <br> Analysis results are created internally by the owning Study  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class AnalysisBodySubcaseResults(NXOpen.NXObject): 
    """ Represents analysis results for an <ja_class>NXOpen.DesignSimulation.AnalysisBody</ja_class> per <ja_class>NXOpen.DesignSimulation.Subcase</ja_class> in the <ja_class>NXOpen.DesignSimulation.Study</ja_class> context. """


    ##  Result type option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Displacement</term><description> 
    ##  Nodal displacement vector </description> </item><item><term> 
    ## StressVonMises</term><description> 
    ##  Nodal stress scalar </description> </item><item><term> 
    ## StressWorstPrincipal</term><description> 
    ##  Nodal stress scalar </description> </item></list>
    class ResultType(Enum):
        """
        Members Include: <Displacement> <StressVonMises> <StressWorstPrincipal>
        """
        Displacement: int
        StressVonMises: int
        StressWorstPrincipal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisBodySubcaseResults.ResultType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Get all scalar result values of given type. Count should match @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink . 
    ##             Stress results are returned as a scalar value. 
    ##  @return values (List[float]): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultType"> (@link AnalysisBodySubcaseResults.ResultType NXOpen.DesignSimulation.AnalysisBodySubcaseResults.ResultType@endlink) </param>
    def GetAllScalarResults(self, resultType: AnalysisBodySubcaseResults.ResultType) -> List[float]:
        """
         Get all scalar result values of given type. Count should match @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink . 
                    Stress results are returned as a scalar value. 
         @return values (List[float]): .
        """
        pass
    
    ##  Get all vector results of given type. Count should match @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink . 
    ##             Displacement results are returned as a vector with X, Y and Z components. 
    ##  @return values (@link NXOpen.Vector3d List[NXOpen.Vector3d]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultType"> (@link AnalysisBodySubcaseResults.ResultType NXOpen.DesignSimulation.AnalysisBodySubcaseResults.ResultType@endlink) </param>
    def GetAllVectorResults(self, resultType: AnalysisBodySubcaseResults.ResultType) -> List[NXOpen.Vector3d]:
        """
         Get all vector results of given type. Count should match @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink . 
                    Displacement results are returned as a vector with X, Y and Z components. 
         @return values (@link NXOpen.Vector3d List[NXOpen.Vector3d]@endlink): .
        """
        pass
    
    ##  Get maximum magnitude of given type of analysis result and the position of the maxima. 
    ##  @return A tuple consisting of (maxMagnitudePosition, maxMagnitude). 
    ##  - maxMagnitudePosition is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink.
    ##  - maxMagnitude is: float.

    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultType"> (@link AnalysisBodySubcaseResults.ResultType NXOpen.DesignSimulation.AnalysisBodySubcaseResults.ResultType@endlink) </param>
    def GetMaxMagnitudeAndLocation(self, resultType: AnalysisBodySubcaseResults.ResultType) -> Tuple[NXOpen.Vector3d, float]:
        """
         Get maximum magnitude of given type of analysis result and the position of the maxima. 
         @return A tuple consisting of (maxMagnitudePosition, maxMagnitude). 
         - maxMagnitudePosition is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink.
         - maxMagnitude is: float.

        """
        pass
    
    ##  Get scalar result value of given type at given index. The index must be between 0 and @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink . 
    ##             Stress results are returned as a scalar value. 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultType"> (@link AnalysisBodySubcaseResults.ResultType NXOpen.DesignSimulation.AnalysisBodySubcaseResults.ResultType@endlink) </param>
    ## <param name="index"> (int) </param>
    def GetScalarResultAt(self, resultType: AnalysisBodySubcaseResults.ResultType, index: int) -> float:
        """
         Get scalar result value of given type at given index. The index must be between 0 and @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink . 
                    Stress results are returned as a scalar value. 
         @return value (float): .
        """
        pass
    
    ##  Get vector result of given type at given index. The index must be between 0 and @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink . 
    ##             Displacement results are returned as a vector with X, Y and Z components. 
    ##  @return value (@link NXOpen.Vector3d NXOpen.Vector3d@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultType"> (@link AnalysisBodySubcaseResults.ResultType NXOpen.DesignSimulation.AnalysisBodySubcaseResults.ResultType@endlink) </param>
    ## <param name="index"> (int) </param>
    def GetVectorResultAt(self, resultType: AnalysisBodySubcaseResults.ResultType, index: int) -> NXOpen.Vector3d:
        """
         Get vector result of given type at given index. The index must be between 0 and @link NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::NumberOfContourVertices @endlink and @link NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices NXOpen::DesignSimulation::AnalysisBodyResults::SetNumberOfContourVertices @endlink . 
                    Displacement results are returned as a vector with X, Y and Z components. 
         @return value (@link NXOpen.Vector3d NXOpen.Vector3d@endlink): .
        """
        pass
    
    ##  Checks availability of analysis results by result type. 
    ##  @return hasResults (bool): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultType"> (@link AnalysisBodySubcaseResults.ResultType NXOpen.DesignSimulation.AnalysisBodySubcaseResults.ResultType@endlink) </param>
    def HasResults(self, resultType: AnalysisBodySubcaseResults.ResultType) -> bool:
        """
         Checks availability of analysis results by result type. 
         @return hasResults (bool): .
        """
        pass
    
import NXOpen
##  Represents an Analysis Body in the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  context.  <br> Abstract base class that cannot be instantiated  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class AnalysisBody(NXOpen.NXObject): 
    """ Represents an Analysis Body in the <ja_class>NXOpen.DesignSimulation.Study</ja_class> context. """


    ## Getter for property: (@link NXOpen.Body NXOpen.Body@endlink) Body
    ##  Returns the referenced body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Body
    @property
    def Body(self) -> NXOpen.Body:
        """
        Getter for property: (@link NXOpen.Body NXOpen.Body@endlink) Body
         Returns the referenced body   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsBlanked
    ##  Returns the blank status of this analysis body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def IsBlanked(self) -> bool:
        """
        Getter for property: (bool) IsBlanked
         Returns the blank status of this analysis body.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
    ##  Returns the physical material (if any) to be used for analysis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Material
    @property
    def Material(self) -> NXOpen.Material:
        """
        Getter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
         Returns the physical material (if any) to be used for analysis   
            
         
        """
        pass
    
    ## Getter for property: (str) ReferencedBodyName
    ##  Returns the name of the referenced body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def ReferencedBodyName(self) -> str:
        """
        Getter for property: (str) ReferencedBodyName
         Returns the name of the referenced body   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisBodyResults NXOpen.DesignSimulation.AnalysisBodyResults@endlink) Results
    ##  Returns the analysis results data from the last simulation run, if any, for the owning @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return AnalysisBodyResults
    @property
    def Results(self) -> AnalysisBodyResults:
        """
        Getter for property: (@link AnalysisBodyResults NXOpen.DesignSimulation.AnalysisBodyResults@endlink) Results
         Returns the analysis results data from the last simulation run, if any, for the owning @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink    
            
         
        """
        pass
    
    ##  Blanks the analysis body. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def Blank(self) -> None:
        """
         Blanks the analysis body. 
        """
        pass
    
    ##  Get the mass of the analysis body in part base units 
    ##  @return A tuple consisting of (massValue, massUnit). 
    ##  - massValue is: float.
    ##  - massUnit is: @link NXOpen.Unit NXOpen.Unit@endlink.

    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetMass(self) -> Tuple[float, NXOpen.Unit]:
        """
         Get the mass of the analysis body in part base units 
         @return A tuple consisting of (massValue, massUnit). 
         - massValue is: float.
         - massUnit is: @link NXOpen.Unit NXOpen.Unit@endlink.

        """
        pass
    
    ##  Unblanks the analysis body. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def Unblank(self) -> None:
        """
         Unblanks the analysis body. 
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::DesignSimulation::AnalysisConstraint NXOpen::DesignSimulation::AnalysisConstraint@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateAnalysisConstraintBuilder  NXOpen::DesignSimulation::Study::CreateAnalysisConstraintBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class AnalysisConstraintBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.DesignSimulation.AnalysisConstraint</ja_class> builder
    """


    ##  Analysis Constraints Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Fixed</term><description> 
    ## </description> </item><item><term> 
    ## Pinned</term><description> 
    ## </description> </item><item><term> 
    ## PinnedSlider</term><description> 
    ## </description> </item><item><term> 
    ## LinearSlider</term><description> 
    ## </description> </item><item><term> 
    ## PlanarSlider</term><description> 
    ## </description> </item><item><term> 
    ## Temperature</term><description> 
    ## </description> </item></list>
    class ConstraintType(Enum):
        """
        Members Include: <Fixed> <Pinned> <PinnedSlider> <LinearSlider> <PlanarSlider> <Temperature>
        """
        Fixed: int
        Pinned: int
        PinnedSlider: int
        LinearSlider: int
        PlanarSlider: int
        Temperature: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisConstraintBuilder.ConstraintType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) LinearSliderVector
    ##  Returns the linear slider vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def LinearSliderVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) LinearSliderVector
         Returns the linear slider vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) LinearSliderVector

    ##  Returns the linear slider vector   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LinearSliderVector.setter
    def LinearSliderVector(self, linearSliderVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) LinearSliderVector
         Returns the linear slider vector   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the fe constraint name   
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
         Returns the fe constraint name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the fe constraint name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Name.setter
    def Name(self, feConstraintName: str):
        """
        Setter for property: (str) Name
         Returns the fe constraint name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSliderPlane
    ##  Returns the planar slider plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def PlanarSliderPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSliderPlane
         Returns the planar slider plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSliderPlane

    ##  Returns the planar slider plane   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PlanarSliderPlane.setter
    def PlanarSliderPlane(self, planarSliderPlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSliderPlane
         Returns the planar slider plane   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectFace
    ##  Returns the fe selected face   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectFace
         Returns the fe selected face   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Temperature
    ##  Returns the temperature expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Temperature(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Temperature
         Returns the temperature expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThickenOffset
    ##  Returns the thicken offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ThickenOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThickenOffset
         Returns the thicken offset   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisConstraintBuilder.ConstraintType NXOpen.DesignSimulation.AnalysisConstraintBuilder.ConstraintType@endlink) Type
    ##  Returns the constraint type enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return AnalysisConstraintBuilder.ConstraintType
    @property
    def Type(self) -> AnalysisConstraintBuilder.ConstraintType:
        """
        Getter for property: (@link AnalysisConstraintBuilder.ConstraintType NXOpen.DesignSimulation.AnalysisConstraintBuilder.ConstraintType@endlink) Type
         Returns the constraint type enum   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisConstraintBuilder.ConstraintType NXOpen.DesignSimulation.AnalysisConstraintBuilder.ConstraintType@endlink) Type

    ##  Returns the constraint type enum   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Type.setter
    def Type(self, type: AnalysisConstraintBuilder.ConstraintType):
        """
        Setter for property: (@link AnalysisConstraintBuilder.ConstraintType NXOpen.DesignSimulation.AnalysisConstraintBuilder.ConstraintType@endlink) Type
         Returns the constraint type enum   
            
         
        """
        pass
    
    ## Getter for property: (bool) UserSetName
    ##  Returns the flag indicating whether the object uses an user-defined name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    
    ## Setter for property: (bool) UserSetName

    ##  Returns the flag indicating whether the object uses an user-defined name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @UserSetName.setter
    def UserSetName(self, userSetName: bool):
        """
        Setter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    
    ##  Update constraint display symbol 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def UpdateDisplay(self) -> None:
        """
         Update constraint display symbol 
        """
        pass
    
import NXOpen
##  Represents a Design Simulation Study Analysis Constraint  <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::AnalysisConstraintBuilder  NXOpen::DesignSimulation::AnalysisConstraintBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class AnalysisConstraint(NXOpen.NXObject): 
    """ Represents a Design Simulation Study Analysis Constraint """


    ## Getter for property: (bool) IsBlanked
    ##  Returns the blank status of this analysis constraint.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def IsBlanked(self) -> bool:
        """
        Getter for property: (bool) IsBlanked
         Returns the blank status of this analysis constraint.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) LinearSliderVector
    ##  Returns the slider vector for LinearSlider type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def LinearSliderVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) LinearSliderVector
         Returns the slider vector for LinearSlider type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSliderPlane
    ##  Returns the planar slider plane for PlanarSlider type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def PlanarSliderPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSliderPlane
         Returns the planar slider plane for PlanarSlider type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Temperature
    ##  Returns the temperature expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Temperature(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Temperature
         Returns the temperature expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThickenOffset
    ##  Returns the thicken offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ThickenOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThickenOffset
         Returns the thicken offset   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisConstraintBuilder.ConstraintType NXOpen.DesignSimulation.AnalysisConstraintBuilder.ConstraintType@endlink) Type
    ##  Returns the constraint type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return AnalysisConstraintBuilder.ConstraintType
    @property
    def Type(self) -> AnalysisConstraintBuilder.ConstraintType:
        """
        Getter for property: (@link AnalysisConstraintBuilder.ConstraintType NXOpen.DesignSimulation.AnalysisConstraintBuilder.ConstraintType@endlink) Type
         Returns the constraint type   
            
         
        """
        pass
    
    ##  Blanks the analysis constraint. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def Blank(self) -> None:
        """
         Blanks the analysis constraint. 
        """
        pass
    
    ##  Gets the faces which the constraint is applied on. 
    ##  @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetFaces(self) -> List[NXOpen.Face]:
        """
         Gets the faces which the constraint is applied on. 
         @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink): .
        """
        pass
    
    ##  Unblanks the analysis constraint. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def Unblank(self) -> None:
        """
         Unblanks the analysis constraint. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::DesignSimulation::AnalysisLoad NXOpen::DesignSimulation::AnalysisLoad@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateAnalysisLoadBuilder  NXOpen::DesignSimulation::Study::CreateAnalysisLoadBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Acceleration.Value </term> <description> 
##  
## 9806.65 (millimeters part),  386.08858 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class AnalysisLoadBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.DesignSimulation.AnalysisLoad</ja_class> builder """


    ##  Analysis Loads force type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ByVector</term><description> 
    ## </description> </item><item><term> 
    ## ByComponent</term><description> 
    ## </description> </item></list>
    class AnalysisLoadForceType(Enum):
        """
        Members Include: <ByVector> <ByComponent>
        """
        ByVector: int
        ByComponent: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisLoadBuilder.AnalysisLoadForceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Analysis Loads Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Force</term><description> 
    ## </description> </item><item><term> 
    ## BearingLoad</term><description> 
    ## </description> </item><item><term> 
    ## Pressure</term><description> 
    ## </description> </item><item><term> 
    ## Torque</term><description> 
    ## </description> </item><item><term> 
    ## Acceleration</term><description> 
    ## </description> </item><item><term> 
    ## EnforcedDisplacement</term><description> 
    ## </description> </item><item><term> 
    ## RemoteForce</term><description> 
    ## </description> </item><item><term> 
    ## HeatFlux</term><description> 
    ## </description> </item></list>
    class AnalysisLoadType(Enum):
        """
        Members Include: <Force> <BearingLoad> <Pressure> <Torque> <Acceleration> <EnforcedDisplacement> <RemoteForce> <HeatFlux>
        """
        Force: int
        BearingLoad: int
        Pressure: int
        Torque: int
        Acceleration: int
        EnforcedDisplacement: int
        RemoteForce: int
        HeatFlux: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisLoadBuilder.AnalysisLoadType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Force Distribution Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## EvenOverFaceArea</term><description> 
    ## </description> </item><item><term> 
    ## EvenOverFaceNumber</term><description> 
    ## </description> </item><item><term> 
    ## ConstantPerFace</term><description> 
    ## </description> </item></list>
    class ForceDistributionType(Enum):
        """
        Members Include: <EvenOverFaceArea> <EvenOverFaceNumber> <ConstantPerFace>
        """
        EvenOverFaceArea: int
        EvenOverFaceNumber: int
        ConstantPerFace: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisLoadBuilder.ForceDistributionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Force Object type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Face</term><description> 
    ## </description> </item><item><term> 
    ## Point</term><description> 
    ## </description> </item></list>
    class ForceObjectType(Enum):
        """
        Members Include: <Face> <Point>
        """
        Face: int
        Point: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisLoadBuilder.ForceObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Remote Load Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Force</term><description> 
    ## </description> </item><item><term> 
    ## Moment</term><description> 
    ## </description> </item><item><term> 
    ## ForceAndMoment</term><description> 
    ## </description> </item></list>
    class RemoteForceType(Enum):
        """
        Members Include: <Force> <Moment> <ForceAndMoment>
        """
        Force: int
        Moment: int
        ForceAndMoment: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisLoadBuilder.RemoteForceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Acceleration
    ##  Returns the acceleration expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Acceleration(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Acceleration
         Returns the acceleration expression   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadForceType@endlink) AnalysisRemoteForceType
    ##  Returns the analysis remote force type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return AnalysisLoadBuilder.AnalysisLoadForceType
    @property
    def AnalysisRemoteForceType(self) -> AnalysisLoadBuilder.AnalysisLoadForceType:
        """
        Getter for property: (@link AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadForceType@endlink) AnalysisRemoteForceType
         Returns the analysis remote force type   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadForceType@endlink) AnalysisRemoteForceType

    ##  Returns the analysis remote force type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @AnalysisRemoteForceType.setter
    def AnalysisRemoteForceType(self, typeOfForce: AnalysisLoadBuilder.AnalysisLoadForceType):
        """
        Setter for property: (@link AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadForceType@endlink) AnalysisRemoteForceType
         Returns the analysis remote force type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BearingAngular
    ##  Returns the bearing angular expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BearingAngular(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BearingAngular
         Returns the bearing angular expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) ComponentCSYS
    ##  Returns the component CSYS   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def ComponentCSYS(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) ComponentCSYS
         Returns the component CSYS   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) ComponentCSYS

    ##  Returns the component CSYS   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ComponentCSYS.setter
    def ComponentCSYS(self, componentCSYS: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) ComponentCSYS
         Returns the component CSYS   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FaceVector
    ##  Returns the face vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def FaceVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FaceVector
         Returns the face vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FaceVector

    ##  Returns the face vector   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @FaceVector.setter
    def FaceVector(self, faceVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FaceVector
         Returns the face vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Force
    ##  Returns the force expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Force(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Force
         Returns the force expression   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisLoadBuilder.ForceDistributionType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceDistributionType@endlink) ForceDistributionMethod
    ##  Returns the distribution method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return AnalysisLoadBuilder.ForceDistributionType
    @property
    def ForceDistributionMethod(self) -> AnalysisLoadBuilder.ForceDistributionType:
        """
        Getter for property: (@link AnalysisLoadBuilder.ForceDistributionType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceDistributionType@endlink) ForceDistributionMethod
         Returns the distribution method   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisLoadBuilder.ForceDistributionType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceDistributionType@endlink) ForceDistributionMethod

    ##  Returns the distribution method   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ForceDistributionMethod.setter
    def ForceDistributionMethod(self, distributionMethod: AnalysisLoadBuilder.ForceDistributionType):
        """
        Setter for property: (@link AnalysisLoadBuilder.ForceDistributionType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceDistributionType@endlink) ForceDistributionMethod
         Returns the distribution method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ForceLocation
    ##  Returns the point selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def ForceLocation(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ForceLocation
         Returns the point selection   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ForceLocation

    ##  Returns the point selection   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ForceLocation.setter
    def ForceLocation(self, forcePoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ForceLocation
         Returns the point selection   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisLoadBuilder.ForceObjectType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceObjectType@endlink) ForceObjectOption
    ##  Returns the face point type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return AnalysisLoadBuilder.ForceObjectType
    @property
    def ForceObjectOption(self) -> AnalysisLoadBuilder.ForceObjectType:
        """
        Getter for property: (@link AnalysisLoadBuilder.ForceObjectType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceObjectType@endlink) ForceObjectOption
         Returns the face point type   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisLoadBuilder.ForceObjectType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceObjectType@endlink) ForceObjectOption

    ##  Returns the face point type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ForceObjectOption.setter
    def ForceObjectOption(self, forceObjectOption: AnalysisLoadBuilder.ForceObjectType):
        """
        Setter for property: (@link AnalysisLoadBuilder.ForceObjectType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceObjectType@endlink) ForceObjectOption
         Returns the face point type   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadForceType@endlink) ForceType
    ##  Returns the force type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return AnalysisLoadBuilder.AnalysisLoadForceType
    @property
    def ForceType(self) -> AnalysisLoadBuilder.AnalysisLoadForceType:
        """
        Getter for property: (@link AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadForceType@endlink) ForceType
         Returns the force type   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadForceType@endlink) ForceType

    ##  Returns the force type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ForceType.setter
    def ForceType(self, typeOfForce: AnalysisLoadBuilder.AnalysisLoadForceType):
        """
        Setter for property: (@link AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadForceType@endlink) ForceType
         Returns the force type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ForceX
    ##  Returns the force x expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ForceX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ForceX
         Returns the force x expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ForceY
    ##  Returns the force y expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ForceY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ForceY
         Returns the force y expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ForceZ
    ##  Returns the force z expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ForceZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ForceZ
         Returns the force z expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeatFlux
    ##  Returns the thermal load expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HeatFlux(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeatFlux
         Returns the thermal load expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDisplacement
    ##  Returns the maximum displacement expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDisplacement(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDisplacement
         Returns the maximum displacement expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Moment
    ##  Returns the moment expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Moment(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Moment
         Returns the moment expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MomentX
    ##  Returns the moment x expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MomentX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MomentX
         Returns the moment x expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MomentY
    ##  Returns the moment y expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MomentY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MomentY
         Returns the moment y expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MomentZ
    ##  Returns the moment z expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MomentZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MomentZ
         Returns the moment z expression   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the Analysis Load name   
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
         Returns the Analysis Load name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the Analysis Load name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the Analysis Load name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Pressure
    ##  Returns the pressure expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Pressure(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Pressure
         Returns the pressure expression   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisLoadBuilder.RemoteForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.RemoteForceType@endlink) RemoteForceOption
    ##  Returns the remote load type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return AnalysisLoadBuilder.RemoteForceType
    @property
    def RemoteForceOption(self) -> AnalysisLoadBuilder.RemoteForceType:
        """
        Getter for property: (@link AnalysisLoadBuilder.RemoteForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.RemoteForceType@endlink) RemoteForceOption
         Returns the remote load type   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisLoadBuilder.RemoteForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.RemoteForceType@endlink) RemoteForceOption

    ##  Returns the remote load type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @RemoteForceOption.setter
    def RemoteForceOption(self, remoteForceOption: AnalysisLoadBuilder.RemoteForceType):
        """
        Setter for property: (@link AnalysisLoadBuilder.RemoteForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.RemoteForceType@endlink) RemoteForceOption
         Returns the remote load type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) RemoteForcePoint
    ##  Returns the remote point selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def RemoteForcePoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) RemoteForcePoint
         Returns the remote point selection   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) RemoteForcePoint

    ##  Returns the remote point selection   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @RemoteForcePoint.setter
    def RemoteForcePoint(self, remotePoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) RemoteForcePoint
         Returns the remote point selection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) RemoteMomentVector
    ##  Returns the remote moment vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def RemoteMomentVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) RemoteMomentVector
         Returns the remote moment vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) RemoteMomentVector

    ##  Returns the remote moment vector   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @RemoteMomentVector.setter
    def RemoteMomentVector(self, remoteMomentVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) RemoteMomentVector
         Returns the remote moment vector   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReverseBearingLoadDirection
    ##  Returns the flag indicating bearing load force direction is reversed or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ReverseBearingLoadDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseBearingLoadDirection
         Returns the flag indicating bearing load force direction is reversed or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) ReverseBearingLoadDirection

    ##  Returns the flag indicating bearing load force direction is reversed or not   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ReverseBearingLoadDirection.setter
    def ReverseBearingLoadDirection(self, reverseForceDirection: bool):
        """
        Setter for property: (bool) ReverseBearingLoadDirection
         Returns the flag indicating bearing load force direction is reversed or not   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReversePressureDirection
    ##  Returns the flag indicating pressure direction is reversed or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ReversePressureDirection(self) -> bool:
        """
        Getter for property: (bool) ReversePressureDirection
         Returns the flag indicating pressure direction is reversed or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) ReversePressureDirection

    ##  Returns the flag indicating pressure direction is reversed or not   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ReversePressureDirection.setter
    def ReversePressureDirection(self, reverseFlag: bool):
        """
        Setter for property: (bool) ReversePressureDirection
         Returns the flag indicating pressure direction is reversed or not   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectFace
    ##  Returns the face(s) to apply the load on   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectFace
         Returns the face(s) to apply the load on   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Torque
    ##  Returns the torque expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Torque(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Torque
         Returns the torque expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) TorqueAxis
    ##  Returns the torque axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Axis
    @property
    def TorqueAxis(self) -> NXOpen.Axis:
        """
        Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) TorqueAxis
         Returns the torque axis   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) TorqueAxis

    ##  Returns the torque axis   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @TorqueAxis.setter
    def TorqueAxis(self, torqueAxis: NXOpen.Axis):
        """
        Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) TorqueAxis
         Returns the torque axis   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisLoadBuilder.AnalysisLoadType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadType@endlink) Type
    ##  Returns the Analysis Load type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return AnalysisLoadBuilder.AnalysisLoadType
    @property
    def Type(self) -> AnalysisLoadBuilder.AnalysisLoadType:
        """
        Getter for property: (@link AnalysisLoadBuilder.AnalysisLoadType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadType@endlink) Type
         Returns the Analysis Load type   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisLoadBuilder.AnalysisLoadType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadType@endlink) Type

    ##  Returns the Analysis Load type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Type.setter
    def Type(self, type: AnalysisLoadBuilder.AnalysisLoadType):
        """
        Setter for property: (@link AnalysisLoadBuilder.AnalysisLoadType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadType@endlink) Type
         Returns the Analysis Load type   
            
         
        """
        pass
    
    ## Getter for property: (bool) UserSetName
    ##  Returns the flag indicating whether the object uses an user-defined name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    
    ## Setter for property: (bool) UserSetName

    ##  Returns the flag indicating whether the object uses an user-defined name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @UserSetName.setter
    def UserSetName(self, userSetName: bool):
        """
        Setter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    
    ##  Update load display symbol 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def UpdateDisplay(self) -> None:
        """
         Update load display symbol 
        """
        pass
    
import NXOpen
##  Represents a Design Simulation Study Analysis Load  <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::AnalysisLoadBuilder  NXOpen::DesignSimulation::AnalysisLoadBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class AnalysisLoad(NXOpen.NXObject): 
    """ Represents a Design Simulation Study Analysis Load """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Acceleration
    ##  Returns the acceleration expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Acceleration(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Acceleration
         Returns the acceleration expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularRange
    ##  Returns the angular range expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AngularRange(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularRange
         Returns the angular range expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) ComponentCSYS
    ##  Returns the component CSYS   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def ComponentCSYS(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) ComponentCSYS
         Returns the component CSYS   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FaceVector
    ##  Returns the face vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def FaceVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FaceVector
         Returns the face vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Force
    ##  Returns the force expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Force(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Force
         Returns the force expression   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisLoadBuilder.ForceDistributionType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceDistributionType@endlink) ForceDistributionMethod
    ##  Returns the distribution method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return AnalysisLoadBuilder.ForceDistributionType
    @property
    def ForceDistributionMethod(self) -> AnalysisLoadBuilder.ForceDistributionType:
        """
        Getter for property: (@link AnalysisLoadBuilder.ForceDistributionType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceDistributionType@endlink) ForceDistributionMethod
         Returns the distribution method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ForceLocation
    ##  Returns the point selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def ForceLocation(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ForceLocation
         Returns the point selection   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisLoadBuilder.ForceObjectType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceObjectType@endlink) ForceObjectOption
    ##  Returns the face point type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return AnalysisLoadBuilder.ForceObjectType
    @property
    def ForceObjectOption(self) -> AnalysisLoadBuilder.ForceObjectType:
        """
        Getter for property: (@link AnalysisLoadBuilder.ForceObjectType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceObjectType@endlink) ForceObjectOption
         Returns the face point type   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadForceType@endlink) ForceType
    ##  Returns the force type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return AnalysisLoadBuilder.AnalysisLoadForceType
    @property
    def ForceType(self) -> AnalysisLoadBuilder.AnalysisLoadForceType:
        """
        Getter for property: (@link AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadForceType@endlink) ForceType
         Returns the force type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ForceX
    ##  Returns the force x expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ForceX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ForceX
         Returns the force x expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ForceY
    ##  Returns the force y expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ForceY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ForceY
         Returns the force y expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ForceZ
    ##  Returns the force z expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ForceZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ForceZ
         Returns the force z expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeatFlux
    ##  Returns the heat flux expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HeatFlux(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeatFlux
         Returns the heat flux expression   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsBlanked
    ##  Returns the blank status of this analysis load.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def IsBlanked(self) -> bool:
        """
        Getter for property: (bool) IsBlanked
         Returns the blank status of this analysis load.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDisplacement
    ##  Returns the maximum displacement expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDisplacement(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDisplacement
         Returns the maximum displacement expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Moment
    ##  Returns the moment expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Moment(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Moment
         Returns the moment expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MomentX
    ##  Returns the moment x expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MomentX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MomentX
         Returns the moment x expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MomentY
    ##  Returns the moment y expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MomentY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MomentY
         Returns the moment y expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MomentZ
    ##  Returns the moment z expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MomentZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MomentZ
         Returns the moment z expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Pressure
    ##  Returns the pressure expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Pressure(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Pressure
         Returns the pressure expression   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisLoadBuilder.RemoteForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.RemoteForceType@endlink) RemoteForceOption
    ##  Returns the remote force load type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return AnalysisLoadBuilder.RemoteForceType
    @property
    def RemoteForceOption(self) -> AnalysisLoadBuilder.RemoteForceType:
        """
        Getter for property: (@link AnalysisLoadBuilder.RemoteForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.RemoteForceType@endlink) RemoteForceOption
         Returns the remote force load type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) RemoteMomentVector
    ##  Returns the remote moment vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def RemoteMomentVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) RemoteMomentVector
         Returns the remote moment vector   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReverseBearingLoadDirection
    ##  Returns the flag indicating bearing load force direction is reversed or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ReverseBearingLoadDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseBearingLoadDirection
         Returns the flag indicating bearing load force direction is reversed or not   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReversePressureDirection
    ##  Returns the flag indicating pressure direction is reversed or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ReversePressureDirection(self) -> bool:
        """
        Getter for property: (bool) ReversePressureDirection
         Returns the flag indicating pressure direction is reversed or not   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Torque
    ##  Returns the torque expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Torque(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Torque
         Returns the torque expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) TorqueAxis
    ##  Returns the torque axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Axis
    @property
    def TorqueAxis(self) -> NXOpen.Axis:
        """
        Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) TorqueAxis
         Returns the torque axis   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisLoadBuilder.AnalysisLoadType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadType@endlink) Type
    ##  Returns the Analysis Load type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return AnalysisLoadBuilder.AnalysisLoadType
    @property
    def Type(self) -> AnalysisLoadBuilder.AnalysisLoadType:
        """
        Getter for property: (@link AnalysisLoadBuilder.AnalysisLoadType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadType@endlink) Type
         Returns the Analysis Load type   
            
         
        """
        pass
    
    ##  Blanks the analysis load. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def Blank(self) -> None:
        """
         Blanks the analysis load. 
        """
        pass
    
    ##  Gets the faces which the load is applied on. 
    ##  @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetFaces(self) -> List[NXOpen.Face]:
        """
         Gets the faces which the load is applied on. 
         @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink): .
        """
        pass
    
    ##  Returns the load expressions, typically just one. Force load specified by components has three. Editing the expression values will make
    ##            the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  results out of date until the analysis or optimization operation is rerun. 
    ##  @return expressions (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetLoadExpressions(self) -> List[NXOpen.Expression]:
        """
         Returns the load expressions, typically just one. Force load specified by components has three. Editing the expression values will make
                   the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  results out of date until the analysis or optimization operation is rerun. 
         @return expressions (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
        """
        pass
    
    ##  Unblanks the analysis load. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def Unblank(self) -> None:
        """
         Unblanks the analysis load. 
        """
        pass
    
import NXOpen
##  Represents a builder for specifying Analysis Report Settings used to publish a report for a Performance Predictor Analysis. <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateAnalysisReportBuilder  NXOpen::DesignSimulation::Study::CreateAnalysisReportBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class AnalysisReportBuilder(NXOpen.Builder): 
    """ Represents a builder for specifying Analysis Report Settings used to publish a report for a Performance Predictor Analysis."""


    ##  Image Background type option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Original</term><description> 
    ## </description> </item><item><term> 
    ## Transparent</term><description> 
    ## </description> </item></list>
    class ImageBackgroundOption(Enum):
        """
        Members Include: <Original> <Transparent>
        """
        Original: int
        Transparent: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisReportBuilder.ImageBackgroundOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Image Size type option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Small</term><description> 
    ## </description> </item><item><term> 
    ## Medium</term><description> 
    ## </description> </item><item><term> 
    ## Large</term><description> 
    ## </description> </item></list>
    class ImageSizeOption(Enum):
        """
        Members Include: <Small> <Medium> <Large>
        """
        Small: int
        Medium: int
        Large: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisReportBuilder.ImageSizeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the save option to be used when running Teamcenter managed mode 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Create</term><description> 
    ## </description> </item><item><term> 
    ## Overwrite</term><description> 
    ## </description> </item><item><term> 
    ## Native</term><description> 
    ## </description> </item></list>
    class SaveBehaviorOption(Enum):
        """
        Members Include: <Create> <Overwrite> <Native>
        """
        Create: int
        Overwrite: int
        Native: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisReportBuilder.SaveBehaviorOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) DatasetName
    ##  Returns the dataset name  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def DatasetName(self) -> str:
        """
        Getter for property: (str) DatasetName
         Returns the dataset name  
            
         
        """
        pass
    
    ## Setter for property: (str) DatasetName

    ##  Returns the dataset name  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @DatasetName.setter
    def DatasetName(self, datasetName: str):
        """
        Setter for property: (str) DatasetName
         Returns the dataset name  
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisReportBuilder.ImageBackgroundOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageBackgroundOption@endlink) ImageBackground
    ##  Returns the image background option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return AnalysisReportBuilder.ImageBackgroundOption
    @property
    def ImageBackground(self) -> AnalysisReportBuilder.ImageBackgroundOption:
        """
        Getter for property: (@link AnalysisReportBuilder.ImageBackgroundOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageBackgroundOption@endlink) ImageBackground
         Returns the image background option   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisReportBuilder.ImageBackgroundOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageBackgroundOption@endlink) ImageBackground

    ##  Returns the image background option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ImageBackground.setter
    def ImageBackground(self, imageBackgroundType: AnalysisReportBuilder.ImageBackgroundOption):
        """
        Setter for property: (@link AnalysisReportBuilder.ImageBackgroundOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageBackgroundOption@endlink) ImageBackground
         Returns the image background option   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisReportBuilder.ImageSizeOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageSizeOption@endlink) ImageSize
    ##  Returns the image size option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return AnalysisReportBuilder.ImageSizeOption
    @property
    def ImageSize(self) -> AnalysisReportBuilder.ImageSizeOption:
        """
        Getter for property: (@link AnalysisReportBuilder.ImageSizeOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageSizeOption@endlink) ImageSize
         Returns the image size option   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisReportBuilder.ImageSizeOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageSizeOption@endlink) ImageSize

    ##  Returns the image size option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ImageSize.setter
    def ImageSize(self, imageSize: AnalysisReportBuilder.ImageSizeOption):
        """
        Setter for property: (@link AnalysisReportBuilder.ImageSizeOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageSizeOption@endlink) ImageSize
         Returns the image size option   
            
         
        """
        pass
    
    ## Getter for property: (int) NumTextLabels
    ##  Returns the number of text labels.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def NumTextLabels(self) -> int:
        """
        Getter for property: (int) NumTextLabels
         Returns the number of text labels.  
            
         
        """
        pass
    
    ## Getter for property: (bool) OpenDocument
    ##  Returns a flag specifying if the report should be opened automatically after creation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def OpenDocument(self) -> bool:
        """
        Getter for property: (bool) OpenDocument
         Returns a flag specifying if the report should be opened automatically after creation   
            
         
        """
        pass
    
    ## Setter for property: (bool) OpenDocument

    ##  Returns a flag specifying if the report should be opened automatically after creation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @OpenDocument.setter
    def OpenDocument(self, openDocument: bool):
        """
        Setter for property: (bool) OpenDocument
         Returns a flag specifying if the report should be opened automatically after creation   
            
         
        """
        pass
    
    ## Getter for property: (str) OutputFileName
    ##  Returns the output file name  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def OutputFileName(self) -> str:
        """
        Getter for property: (str) OutputFileName
         Returns the output file name  
            
         
        """
        pass
    
    ## Setter for property: (str) OutputFileName

    ##  Returns the output file name  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @OutputFileName.setter
    def OutputFileName(self, outputFileName: str):
        """
        Setter for property: (str) OutputFileName
         Returns the output file name  
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisReportBuilder.SaveBehaviorOption NXOpen.DesignSimulation.AnalysisReportBuilder.SaveBehaviorOption@endlink) SaveBehavior
    ##  Returns the save option to be used when running in Teamcenter managed mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return AnalysisReportBuilder.SaveBehaviorOption
    @property
    def SaveBehavior(self) -> AnalysisReportBuilder.SaveBehaviorOption:
        """
        Getter for property: (@link AnalysisReportBuilder.SaveBehaviorOption NXOpen.DesignSimulation.AnalysisReportBuilder.SaveBehaviorOption@endlink) SaveBehavior
         Returns the save option to be used when running in Teamcenter managed mode   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisReportBuilder.SaveBehaviorOption NXOpen.DesignSimulation.AnalysisReportBuilder.SaveBehaviorOption@endlink) SaveBehavior

    ##  Returns the save option to be used when running in Teamcenter managed mode   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @SaveBehavior.setter
    def SaveBehavior(self, saveBehaviorOption: AnalysisReportBuilder.SaveBehaviorOption):
        """
        Setter for property: (@link AnalysisReportBuilder.SaveBehaviorOption NXOpen.DesignSimulation.AnalysisReportBuilder.SaveBehaviorOption@endlink) SaveBehavior
         Returns the save option to be used when running in Teamcenter managed mode   
            
         
        """
        pass
    
    ## Getter for property: (bool) SaveImages
    ##  Returns a flag specifying if the Viewport images should be saved in the report folder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def SaveImages(self) -> bool:
        """
        Getter for property: (bool) SaveImages
         Returns a flag specifying if the Viewport images should be saved in the report folder   
            
         
        """
        pass
    
    ## Setter for property: (bool) SaveImages

    ##  Returns a flag specifying if the Viewport images should be saved in the report folder   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @SaveImages.setter
    def SaveImages(self, saveImages: bool):
        """
        Setter for property: (bool) SaveImages
         Returns a flag specifying if the Viewport images should be saved in the report folder   
            
         
        """
        pass
    
    ## Getter for property: (str) TemplateFileName
    ##  Returns the name of the analysis report template file  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def TemplateFileName(self) -> str:
        """
        Getter for property: (str) TemplateFileName
         Returns the name of the analysis report template file  
            
         
        """
        pass
    
    ## Setter for property: (str) TemplateFileName

    ##  Returns the name of the analysis report template file  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @TemplateFileName.setter
    def TemplateFileName(self, templateFileName: str):
        """
        Setter for property: (str) TemplateFileName
         Returns the name of the analysis report template file  
            
         
        """
        pass
    
    ## Getter for property: (int) ViewportSettingsBuilderCount
    ##  Returns the number of viewport settings builders   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def ViewportSettingsBuilderCount(self) -> int:
        """
        Getter for property: (int) ViewportSettingsBuilderCount
         Returns the number of viewport settings builders   
            
         
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::ViewportSettingsBuilder NXOpen::DesignSimulation::ViewportSettingsBuilder@endlink . 
    ##  @return newBuilder (@link ViewportSettingsBuilder NXOpen.DesignSimulation.ViewportSettingsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def CreateViewportSettingsBuilder(self) -> ViewportSettingsBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::ViewportSettingsBuilder NXOpen::DesignSimulation::ViewportSettingsBuilder@endlink . 
         @return newBuilder (@link ViewportSettingsBuilder NXOpen.DesignSimulation.ViewportSettingsBuilder@endlink): .
        """
        pass
    
    ##  Returns the ID text label of index.
    ##  @return label (str): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="textLabelIndex"> (int) </param>
    def GetNthTextLabelID(self, textLabelIndex: int) -> str:
        """
         Returns the ID text label of index.
         @return label (str): .
        """
        pass
    
    ##  Returns the user name text label of index.
    ##  @return userName (str): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="textLabelIndex"> (int) </param>
    def GetNthTextLabelUserName(self, textLabelIndex: int) -> str:
        """
         Returns the user name text label of index.
         @return userName (str): .
        """
        pass
    
    ##  Returns the value of the text with the given label, if the text exists.
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str) </param>
    def GetTextValueOfLabel(self, label: str) -> str:
        """
         Returns the value of the text with the given label, if the text exists.
         @return value (str): .
        """
        pass
    
    ##  Returns the viewport settings builder of specified index 
    ##  @return viewportSettingsBuilder (@link ViewportSettingsBuilder NXOpen.DesignSimulation.ViewportSettingsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetViewportSettingsBuilder(self, index: int) -> ViewportSettingsBuilder:
        """
         Returns the viewport settings builder of specified index 
         @return viewportSettingsBuilder (@link ViewportSettingsBuilder NXOpen.DesignSimulation.ViewportSettingsBuilder@endlink): .
        """
        pass
    
    ##  Returns the user name text label of index.
    ##  @return isReadOnly (bool): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="textLabelIndex"> (int) </param>
    def IsNthTextLabelReadOnly(self, textLabelIndex: int) -> bool:
        """
         Returns the user name text label of index.
         @return isReadOnly (bool): .
        """
        pass
    
    ##  Removes viewport settings builder and viewport settings at specified index 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def RemoveViewportSettingsBuilder(self, index: int) -> None:
        """
         Removes viewport settings builder and viewport settings at specified index 
        """
        pass
    
    ##  Sets the value of the text with the given label, if the text exists.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str) </param>
    ## <param name="value"> (str) </param>
    def SetTextValueOfLabel(self, label: str, value: str) -> None:
        """
         Sets the value of the text with the given label, if the text exists.
        """
        pass
    
import NXOpen
##  Represents an Analysis Report Settings used to publish a report for a Performance Predictor Analysis. <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::AnalysisReportBuilder  NXOpen::DesignSimulation::AnalysisReportBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class AnalysisReportSettings(NXOpen.NXObject): 
    """ Represents an Analysis Report Settings used to publish a report for a Performance Predictor Analysis."""


    ## Getter for property: (@link AnalysisReportBuilder.ImageBackgroundOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageBackgroundOption@endlink) ImageBackground
    ##  Returns the image background option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return AnalysisReportBuilder.ImageBackgroundOption
    @property
    def ImageBackground(self) -> AnalysisReportBuilder.ImageBackgroundOption:
        """
        Getter for property: (@link AnalysisReportBuilder.ImageBackgroundOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageBackgroundOption@endlink) ImageBackground
         Returns the image background option   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisReportBuilder.ImageSizeOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageSizeOption@endlink) ImageSize
    ##  Returns the image size option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return AnalysisReportBuilder.ImageSizeOption
    @property
    def ImageSize(self) -> AnalysisReportBuilder.ImageSizeOption:
        """
        Getter for property: (@link AnalysisReportBuilder.ImageSizeOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageSizeOption@endlink) ImageSize
         Returns the image size option   
            
         
        """
        pass
    
    ## Getter for property: (bool) OpenDocument
    ##  Returns a flag specifying if the report should be opened automatically after creation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def OpenDocument(self) -> bool:
        """
        Getter for property: (bool) OpenDocument
         Returns a flag specifying if the report should be opened automatically after creation   
            
         
        """
        pass
    
    ## Getter for property: (str) OutputFileName
    ##  Returns the output file name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def OutputFileName(self) -> str:
        """
        Getter for property: (str) OutputFileName
         Returns the output file name   
            
         
        """
        pass
    
    ## Getter for property: (bool) SaveImages
    ##  Returns a flag specifying if the Viewport images should be saved in the report folder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def SaveImages(self) -> bool:
        """
        Getter for property: (bool) SaveImages
         Returns a flag specifying if the Viewport images should be saved in the report folder   
            
         
        """
        pass
    
    ## Getter for property: (str) TemplateFileName
    ##  Returns the name of the analysis report template file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def TemplateFileName(self) -> str:
        """
        Getter for property: (str) TemplateFileName
         Returns the name of the analysis report template file   
            
         
        """
        pass
    
    ## Getter for property: (int) ViewportSettingsCount
    ##  Returns the number of viewport settings   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def ViewportSettingsCount(self) -> int:
        """
        Getter for property: (int) ViewportSettingsCount
         Returns the number of viewport settings   
            
         
        """
        pass
    
    ##  Returns the value of the text with the given label, if the text exists. 
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str) </param>
    def GetTextValueOfLabel(self, label: str) -> str:
        """
         Returns the value of the text with the given label, if the text exists. 
         @return value (str): .
        """
        pass
    
    ##  Returns the viewport settings of specified index 
    ##  @return viewportSettings (@link ViewportSettings NXOpen.DesignSimulation.ViewportSettings@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetViewportSettings(self, index: int) -> ViewportSettings:
        """
         Returns the viewport settings of specified index 
         @return viewportSettings (@link ViewportSettings NXOpen.DesignSimulation.ViewportSettings@endlink): .
        """
        pass
    
import NXOpen
## 
##     Represents animation controls and play settings
##      <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::PostManager::CreateAnimationController  NXOpen::DesignSimulation::PostManager::CreateAnimationController @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class AnimationController(NXOpen.TransientObject): 
    """
    Represents animation controls and play settings
    """


    ##  Animation States option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Play</term><description> 
    ## </description> </item><item><term> 
    ## Stop</term><description> 
    ## </description> </item><item><term> 
    ## Pause</term><description> 
    ## </description> </item><item><term> 
    ## Next</term><description> 
    ## </description> </item><item><term> 
    ## Previous</term><description> 
    ## </description> </item></list>
    class State(Enum):
        """
        Members Include: <Play> <Stop> <Pause> <Next> <Previous>
        """
        Play: int
        Stop: int
        Pause: int
        Next: int
        Previous: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimationController.State:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) FullCycle
    ##  Returns the animation is full cycle or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def FullCycle(self) -> bool:
        """
        Getter for property: (bool) FullCycle
         Returns the animation is full cycle or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) FullCycle

    ##  Returns the animation is full cycle or not   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @FullCycle.setter
    def FullCycle(self, isFullCycle: bool):
        """
        Setter for property: (bool) FullCycle
         Returns the animation is full cycle or not   
            
         
        """
        pass
    
    ##  Controls the contour animation 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="animState"> (@link AnimationController.State NXOpen.DesignSimulation.AnimationController.State@endlink) </param>
    def AnimateContour(self, animState: AnimationController.State) -> None:
        """
         Controls the contour animation 
        """
        pass
    
    ##  Destroys the object. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Destroys the object. 
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::DesignSimulation::Connection NXOpen::DesignSimulation::Connection@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateConnectionBuilder  NXOpen::DesignSimulation::Study::CreateConnectionBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AutoConnection </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## ShellOffset1.Value </term> <description> 
##  
## 5 (millimeters part), 0.02 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ShellOffset2.Value </term> <description> 
##  
## 5 (millimeters part), 0.02 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class ConnectionBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.DesignSimulation.Connection</ja_class> builder
    """


    ##  define connection types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## BodyToBody</term><description> 
    ## </description> </item><item><term> 
    ## FaceToFace</term><description> 
    ## </description> </item></list>
    class Types(Enum):
        """
        Members Include: <BodyToBody> <FaceToFace>
        """
        BodyToBody: int
        FaceToFace: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConnectionBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AutoConnection
    ##  Returns the flag indicating whether or not to utilize automatic connection detection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def AutoConnection(self) -> bool:
        """
        Getter for property: (bool) AutoConnection
         Returns the flag indicating whether or not to utilize automatic connection detection   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutoConnection

    ##  Returns the flag indicating whether or not to utilize automatic connection detection   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @AutoConnection.setter
    def AutoConnection(self, autoConnection: bool):
        """
        Setter for property: (bool) AutoConnection
         Returns the flag indicating whether or not to utilize automatic connection detection   
            
         
        """
        pass
    
    ## Getter for property: (str) ConnectionName
    ##  Returns the connection name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def ConnectionName(self) -> str:
        """
        Getter for property: (str) ConnectionName
         Returns the connection name   
            
         
        """
        pass
    
    ## Setter for property: (str) ConnectionName

    ##  Returns the connection name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ConnectionName.setter
    def ConnectionName(self, connectionName: str):
        """
        Setter for property: (str) ConnectionName
         Returns the connection name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBody NXOpen.SelectBody@endlink) SelectBody1
    ##  Returns the select body1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectBody
    @property
    def SelectBody1(self) -> NXOpen.SelectBody:
        """
        Getter for property: (@link NXOpen.SelectBody NXOpen.SelectBody@endlink) SelectBody1
         Returns the select body1   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBody NXOpen.SelectBody@endlink) SelectBody2
    ##  Returns the select body2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectBody
    @property
    def SelectBody2(self) -> NXOpen.SelectBody:
        """
        Getter for property: (@link NXOpen.SelectBody NXOpen.SelectBody@endlink) SelectBody2
         Returns the select body2   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectFaces1
    ##  Returns the select faces1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectFaces1(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectFaces1
         Returns the select faces1   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectFaces2
    ##  Returns the select faces2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectFaces2(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectFaces2
         Returns the select faces2   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ShellOffset1
    ##  Returns the shell offset for faces1 or body1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ShellOffset1(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ShellOffset1
         Returns the shell offset for faces1 or body1   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ShellOffset2
    ##  Returns the shell offset for faces2 or body2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ShellOffset2(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ShellOffset2
         Returns the shell offset for faces2 or body2   
            
         
        """
        pass
    
    ## Getter for property: (@link ConnectionBuilder.Types NXOpen.DesignSimulation.ConnectionBuilder.Types@endlink) Type
    ##  Returns the type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ConnectionBuilder.Types
    @property
    def Type(self) -> ConnectionBuilder.Types:
        """
        Getter for property: (@link ConnectionBuilder.Types NXOpen.DesignSimulation.ConnectionBuilder.Types@endlink) Type
         Returns the type   
            
         
        """
        pass
    
    ## Setter for property: (@link ConnectionBuilder.Types NXOpen.DesignSimulation.ConnectionBuilder.Types@endlink) Type

    ##  Returns the type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Type.setter
    def Type(self, type: ConnectionBuilder.Types):
        """
        Setter for property: (@link ConnectionBuilder.Types NXOpen.DesignSimulation.ConnectionBuilder.Types@endlink) Type
         Returns the type   
            
         
        """
        pass
    
    ## Getter for property: (bool) UserSetName
    ##  Returns the flag indicating whether the object uses an user-defined name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    
    ## Setter for property: (bool) UserSetName

    ##  Returns the flag indicating whether the object uses an user-defined name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @UserSetName.setter
    def UserSetName(self, userSetName: bool):
        """
        Setter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Design Simulation Study Connection  <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::ConnectionBuilder  NXOpen::DesignSimulation::ConnectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Connection(NXOpen.NXObject): 
    """ Represents a Design Simulation Study Connection """
    pass


import NXOpen
##  Represents a @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateConstructionBodyBuilder  NXOpen::DesignSimulation::Study::CreateConstructionBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BlendRadius.Value </term> <description> 
##  
## 1 (millimeters part), 0.04 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ChamferDistance.Value </term> <description> 
##  
## 1 (millimeters part), 0.04 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Method </term> <description> 
##  
## KeepIn </description> </item> 
## 
## <item><term> 
##  
## Offset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## OffsetEdgesType </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## ThickenOffset.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Type </term> <description> 
##  
## ByBody </description> </item> 
## 
## <item><term> 
##  
## WallThickness.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class ConstructionBodyBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.DesignSimulation.ConstructionBody</ja_class> builder """


    ##  Construction type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ByBody</term><description> 
    ## </description> </item><item><term> 
    ## ByFace</term><description> 
    ## </description> </item></list>
    class ConstructionType(Enum):
        """
        Members Include: <ByBody> <ByFace>
        """
        ByBody: int
        ByFace: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConstructionBodyBuilder.ConstructionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Construction Body grouping type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Separate</term><description> 
    ## </description> </item><item><term> 
    ## Collection</term><description> 
    ## </description> </item></list>
    class GroupingType(Enum):
        """
        Members Include: <Separate> <Collection>
        """
        Separate: int
        Collection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConstructionBodyBuilder.GroupingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Construction Body Method 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## KeepIn</term><description> 
    ## </description> </item><item><term> 
    ## KeepOut</term><description> 
    ## </description> </item><item><term> 
    ## Shell</term><description> 
    ## </description> </item></list>
    class MethodOption(Enum):
        """
        Members Include: <KeepIn> <KeepOut> <Shell>
        """
        KeepIn: int
        KeepOut: int
        Shell: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConstructionBodyBuilder.MethodOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Offset Edges Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Automatic</term><description> 
    ## </description> </item><item><term> 
    ## WithRadius</term><description> 
    ## </description> </item><item><term> 
    ## WithChamfer</term><description> 
    ## </description> </item></list>
    class OffsetType(Enum):
        """
        Members Include: <NotSet> <Automatic> <WithRadius> <WithChamfer>
        """
        NotSet: int
        Automatic: int
        WithRadius: int
        WithChamfer: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConstructionBodyBuilder.OffsetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BlendRadius
    ##  Returns the blend radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BlendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BlendRadius
         Returns the blend radius   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) Bodies
    ##  Returns the body selection for 'Single' grouping type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def Bodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) Bodies
         Returns the body selection for 'Single' grouping type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodyCollector
    ##  Returns the body collector for 'Collection' grouping type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BodyCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodyCollector
         Returns the body collector for 'Collection' grouping type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ChamferDistance
    ##  Returns the chamfer distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ChamferDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ChamferDistance
         Returns the chamfer distance   
            
         
        """
        pass
    
    ## Getter for property: (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) DesignSpace
    ##  Returns the design space   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return DesignSpace
    @property
    def DesignSpace(self) -> DesignSpace:
        """
        Getter for property: (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) DesignSpace
         Returns the design space   
            
         
        """
        pass
    
    ## Setter for property: (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) DesignSpace

    ##  Returns the design space   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DesignSpace.setter
    def DesignSpace(self, designSpace: DesignSpace):
        """
        Setter for property: (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) DesignSpace
         Returns the design space   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector
    ##  Returns the face collector for 'By Face' type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector
         Returns the face collector for 'By Face' type   
            
         
        """
        pass
    
    ## Getter for property: (@link ConstructionBodyBuilder.GroupingType NXOpen.DesignSimulation.ConstructionBodyBuilder.GroupingType@endlink) GroupingOption
    ##  Returns the grouping option for construction bodies   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ConstructionBodyBuilder.GroupingType
    @property
    def GroupingOption(self) -> ConstructionBodyBuilder.GroupingType:
        """
        Getter for property: (@link ConstructionBodyBuilder.GroupingType NXOpen.DesignSimulation.ConstructionBodyBuilder.GroupingType@endlink) GroupingOption
         Returns the grouping option for construction bodies   
            
         
        """
        pass
    
    ## Setter for property: (@link ConstructionBodyBuilder.GroupingType NXOpen.DesignSimulation.ConstructionBodyBuilder.GroupingType@endlink) GroupingOption

    ##  Returns the grouping option for construction bodies   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @GroupingOption.setter
    def GroupingOption(self, groupAs: ConstructionBodyBuilder.GroupingType):
        """
        Setter for property: (@link ConstructionBodyBuilder.GroupingType NXOpen.DesignSimulation.ConstructionBodyBuilder.GroupingType@endlink) GroupingOption
         Returns the grouping option for construction bodies   
            
         
        """
        pass
    
    ## Getter for property: (@link ConstructionBodyBuilder.MethodOption NXOpen.DesignSimulation.ConstructionBodyBuilder.MethodOption@endlink) Method
    ##  Returns the method type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ConstructionBodyBuilder.MethodOption
    @property
    def Method(self) -> ConstructionBodyBuilder.MethodOption:
        """
        Getter for property: (@link ConstructionBodyBuilder.MethodOption NXOpen.DesignSimulation.ConstructionBodyBuilder.MethodOption@endlink) Method
         Returns the method type   
            
         
        """
        pass
    
    ## Setter for property: (@link ConstructionBodyBuilder.MethodOption NXOpen.DesignSimulation.ConstructionBodyBuilder.MethodOption@endlink) Method

    ##  Returns the method type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Method.setter
    def Method(self, methodOption: ConstructionBodyBuilder.MethodOption):
        """
        Setter for property: (@link ConstructionBodyBuilder.MethodOption NXOpen.DesignSimulation.ConstructionBodyBuilder.MethodOption@endlink) Method
         Returns the method type   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the construction body name   
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
         Returns the construction body name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the construction body name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Name.setter
    def Name(self, constructionBodyName: str):
        """
        Setter for property: (str) Name
         Returns the construction body name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##  Returns the offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
         Returns the offset   
            
         
        """
        pass
    
    ## Getter for property: (@link ConstructionBodyBuilder.OffsetType NXOpen.DesignSimulation.ConstructionBodyBuilder.OffsetType@endlink) OffsetEdgesType
    ##  Returns the offset edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ConstructionBodyBuilder.OffsetType
    @property
    def OffsetEdgesType(self) -> ConstructionBodyBuilder.OffsetType:
        """
        Getter for property: (@link ConstructionBodyBuilder.OffsetType NXOpen.DesignSimulation.ConstructionBodyBuilder.OffsetType@endlink) OffsetEdgesType
         Returns the offset edges   
            
         
        """
        pass
    
    ## Setter for property: (@link ConstructionBodyBuilder.OffsetType NXOpen.DesignSimulation.ConstructionBodyBuilder.OffsetType@endlink) OffsetEdgesType

    ##  Returns the offset edges   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @OffsetEdgesType.setter
    def OffsetEdgesType(self, offsetEdgesType: ConstructionBodyBuilder.OffsetType):
        """
        Setter for property: (@link ConstructionBodyBuilder.OffsetType NXOpen.DesignSimulation.ConstructionBodyBuilder.OffsetType@endlink) OffsetEdgesType
         Returns the offset edges   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThickenOffset
    ##  Returns the thicken offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ThickenOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThickenOffset
         Returns the thicken offset   
            
         
        """
        pass
    
    ## Getter for property: (@link ConstructionBodyBuilder.ConstructionType NXOpen.DesignSimulation.ConstructionBodyBuilder.ConstructionType@endlink) Type
    ##  Returns the input type for defining a construction body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return ConstructionBodyBuilder.ConstructionType
    @property
    def Type(self) -> ConstructionBodyBuilder.ConstructionType:
        """
        Getter for property: (@link ConstructionBodyBuilder.ConstructionType NXOpen.DesignSimulation.ConstructionBodyBuilder.ConstructionType@endlink) Type
         Returns the input type for defining a construction body   
            
         
        """
        pass
    
    ## Setter for property: (@link ConstructionBodyBuilder.ConstructionType NXOpen.DesignSimulation.ConstructionBodyBuilder.ConstructionType@endlink) Type

    ##  Returns the input type for defining a construction body   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Type.setter
    def Type(self, constrOption: ConstructionBodyBuilder.ConstructionType):
        """
        Setter for property: (@link ConstructionBodyBuilder.ConstructionType NXOpen.DesignSimulation.ConstructionBodyBuilder.ConstructionType@endlink) Type
         Returns the input type for defining a construction body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) WallThickness
    ##  Returns the wall thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def WallThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) WallThickness
         Returns the wall thickness   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  created by selecting faces.  <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::ConstructionBodyBuilder  NXOpen::DesignSimulation::ConstructionBodyBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class ConstructionBodyByFaces(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.DesignSimulation.ConstructionBody</ja_class> created by selecting faces. """
    pass


import NXOpen
##  Represents a @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  collection for a @link NXOpen::DesignSimulation::DesignSpace NXOpen::DesignSimulation::DesignSpace@endlink   <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::ConstructionBodyBuilder  NXOpen::DesignSimulation::ConstructionBodyBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ConstructionBodyCollector(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.DesignSimulation.ConstructionBody</ja_class> collection for a <ja_class>NXOpen.DesignSimulation.DesignSpace</ja_class> """


    ## Getter for property: (bool) IsBlanked
    ##  Returns the blank status of this construction body collector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def IsBlanked(self) -> bool:
        """
        Getter for property: (bool) IsBlanked
         Returns the blank status of this construction body collector.  
             
         
        """
        pass
    
    ## Add a @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  to this @link NXOpen::DesignSimulation::ConstructionBodyCollector NXOpen::DesignSimulation::ConstructionBodyCollector@endlink  collection.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ## <param name="bFromCollectorToCollector"> (bool) </param>
    ## <param name="constructionBody"> (@link ConstructionBody NXOpen.DesignSimulation.ConstructionBody@endlink) </param>
    def AddMember(self, bFromCollectorToCollector: bool, constructionBody: ConstructionBody) -> None:
        """
        Add a @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  to this @link NXOpen::DesignSimulation::ConstructionBodyCollector NXOpen::DesignSimulation::ConstructionBodyCollector@endlink  collection.
        """
        pass
    
    ##  Blanks the construction body collector (blank ojects within collector). 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def Blank(self) -> None:
        """
         Blanks the construction body collector (blank ojects within collector). 
        """
        pass
    
    ## Remove a @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  from this @link NXOpen::DesignSimulation::ConstructionBodyCollector NXOpen::DesignSimulation::ConstructionBodyCollector@endlink  collection.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ## <param name="bFromCollectorToCollector"> (bool) </param>
    ## <param name="constructionBody"> (@link ConstructionBody NXOpen.DesignSimulation.ConstructionBody@endlink) </param>
    def RemoveMember(self, bFromCollectorToCollector: bool, constructionBody: ConstructionBody) -> None:
        """
        Remove a @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  from this @link NXOpen::DesignSimulation::ConstructionBodyCollector NXOpen::DesignSimulation::ConstructionBodyCollector@endlink  collection.
        """
        pass
    
    ##  Unblanks the construction body collector (allow ojects within collector to be visible). 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def Unblank(self) -> None:
        """
         Unblanks the construction body collector (allow ojects within collector to be visible). 
        """
        pass
    
    ## Separate all @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  members and delete this @link NXOpen::DesignSimulation::ConstructionBodyCollector NXOpen::DesignSimulation::ConstructionBodyCollector@endlink  collection.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    def Ungroup(self) -> None:
        """
        Separate all @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  members and delete this @link NXOpen::DesignSimulation::ConstructionBodyCollector NXOpen::DesignSimulation::ConstructionBodyCollector@endlink  collection.
        """
        pass
    
##  Represents a @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  for a @link NXOpen::DesignSimulation::DesignSpace NXOpen::DesignSimulation::DesignSpace@endlink  <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::ConstructionBodyBuilder  NXOpen::DesignSimulation::ConstructionBodyBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ConstructionBody(AnalysisBody): 
    """ Represents a <ja_class>NXOpen.DesignSimulation.ConstructionBody</ja_class> for a <ja_class>NXOpen.DesignSimulation.DesignSpace</ja_class>"""
    pass


import NXOpen
##  Represents a Design Simulation Container object <br> A @link NXOpen::DesignSimulation::Container NXOpen::DesignSimulation::Container@endlink  cannot be created independently. @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  and @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink  are types of containers that can be created and deleted by the user.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Container(NXOpen.NXObject): 
    """ Represents a Design Simulation Container object"""


    ##  Reorder operation type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Before</term><description> 
    ##  Reorder an object before another object in the same container </description> </item><item><term> 
    ## After</term><description> 
    ##  Reorder an object after another object in the same container </description> </item><item><term> 
    ## Into</term><description> 
    ##  Reorder an object into the container which does not have it </description> </item></list>
    class ReorderType(Enum):
        """
        Members Include: <Before> <After> <Into>
        """
        Before: int
        After: int
        Into: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Container.ReorderType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Gets all @link NXOpen::NXObject NXOpen::NXObject@endlink  members in the order they are referenced. 
    ##  @return members (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING") OR features_modeling ("FEATURES MODELING")
    def GetMembers(self) -> List[NXOpen.NXObject]:
        """
         Gets all @link NXOpen::NXObject NXOpen::NXObject@endlink  members in the order they are referenced. 
         @return members (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  Reorders a child object 'before' or 'after' another child object belonging to the same @link NXOpen::DesignSimulation::Container NXOpen::DesignSimulation::Container@endlink .
    ##             Reordering an object 'into' the @link NXOpen::DesignSimulation::Container NXOpen::DesignSimulation::Container@endlink  that does not have it will be implemented in the future. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="source"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="target"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="type"> (@link Container.ReorderType NXOpen.DesignSimulation.Container.ReorderType@endlink) </param>
    def Reorder(self, source: NXOpen.NXObject, target: NXOpen.NXObject, type: Container.ReorderType) -> None:
        """
         Reorders a child object 'before' or 'after' another child object belonging to the same @link NXOpen::DesignSimulation::Container NXOpen::DesignSimulation::Container@endlink .
                    Reordering an object 'into' the @link NXOpen::DesignSimulation::Container NXOpen::DesignSimulation::Container@endlink  that does not have it will be implemented in the future. 
        """
        pass
    
import NXOpen
##  Represents a base class for the builders creating contour result settings. <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class ContourSettingsBuilder(NXOpen.Builder): 
    """ Represents a base class for the builders creating contour result settings."""


    ##  Color style option for contotur display 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Default</term><description> 
    ## </description> </item><item><term> 
    ## Spotlight</term><description> 
    ## </description> </item><item><term> 
    ## MaterialLimit</term><description> 
    ## </description> </item></list>
    class ColorStyleOption(Enum):
        """
        Members Include: <Default> <Spotlight> <MaterialLimit>
        """
        Default: int
        Spotlight: int
        MaterialLimit: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ContourSettingsBuilder.ColorStyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Result type and component type option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Magnitude</term><description> 
    ## </description> </item><item><term> 
    ## WorstInXYZ</term><description> 
    ## </description> </item><item><term> 
    ## X</term><description> 
    ## </description> </item><item><term> 
    ## Y</term><description> 
    ## </description> </item><item><term> 
    ## Z</term><description> 
    ## </description> </item><item><term> 
    ## All</term><description> 
    ##  All includes Worst in XYZ, X, Y and Z</description> </item><item><term> 
    ## VonMises</term><description> 
    ## </description> </item><item><term> 
    ## WorstPrincipal</term><description> 
    ## </description> </item><item><term> 
    ## Scalar</term><description> 
    ## </description> </item></list>
    class ComponentTypeOption(Enum):
        """
        Members Include: <Magnitude> <WorstInXYZ> <X> <Y> <Z> <All> <VonMises> <WorstPrincipal> <Scalar>
        """
        Magnitude: int
        WorstInXYZ: int
        X: int
        Y: int
        Z: int
        All: int
        VonMises: int
        WorstPrincipal: int
        Scalar: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ContourSettingsBuilder.ComponentTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Contour limit computation option for displaying results contour 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AnalysisBodyMaterial</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item></list>
    class ContourLimitOption(Enum):
        """
        Members Include: <AnalysisBodyMaterial> <UserDefined>
        """
        AnalysisBodyMaterial: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ContourSettingsBuilder.ContourLimitOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Contour style option for contour display 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Smooth</term><description> 
    ## </description> </item><item><term> 
    ## Banded</term><description> 
    ## </description> </item></list>
    class ContourStyleOption(Enum):
        """
        Members Include: <Smooth> <Banded>
        """
        Smooth: int
        Banded: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ContourSettingsBuilder.ContourStyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Result type option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Displacement</term><description> 
    ## </description> </item><item><term> 
    ## Stress</term><description> 
    ## </description> </item><item><term> 
    ## FactorOfSafety</term><description> 
    ## </description> </item><item><term> 
    ## ModalAmplitude</term><description> 
    ## </description> </item><item><term> 
    ## Temperature</term><description> 
    ## </description> </item></list>
    class ResultTypeOption(Enum):
        """
        Members Include: <Displacement> <Stress> <FactorOfSafety> <ModalAmplitude> <Temperature>
        """
        Displacement: int
        Stress: int
        FactorOfSafety: int
        ModalAmplitude: int
        Temperature: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ContourSettingsBuilder.ResultTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ContourSettingsBuilder.ColorStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ColorStyleOption@endlink) ColorStyle
    ##  Returns the display color style.  
    ##    This option is for different color schema's for highlighting the results ranges.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return ContourSettingsBuilder.ColorStyleOption
    @property
    def ColorStyle(self) -> ContourSettingsBuilder.ColorStyleOption:
        """
        Getter for property: (@link ContourSettingsBuilder.ColorStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ColorStyleOption@endlink) ColorStyle
         Returns the display color style.  
           This option is for different color schema's for highlighting the results ranges.  
         
        """
        pass
    
    ## Setter for property: (@link ContourSettingsBuilder.ColorStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ColorStyleOption@endlink) ColorStyle

    ##  Returns the display color style.  
    ##    This option is for different color schema's for highlighting the results ranges.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ColorStyle.setter
    def ColorStyle(self, colorStyle: ContourSettingsBuilder.ColorStyleOption):
        """
        Setter for property: (@link ContourSettingsBuilder.ColorStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ColorStyleOption@endlink) ColorStyle
         Returns the display color style.  
           This option is for different color schema's for highlighting the results ranges.  
         
        """
        pass
    
    ## Getter for property: (@link ContourSettingsBuilder.ComponentTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ComponentTypeOption@endlink) ComponentType
    ##  Returns the result component type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return ContourSettingsBuilder.ComponentTypeOption
    @property
    def ComponentType(self) -> ContourSettingsBuilder.ComponentTypeOption:
        """
        Getter for property: (@link ContourSettingsBuilder.ComponentTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ComponentTypeOption@endlink) ComponentType
         Returns the result component type   
            
         
        """
        pass
    
    ## Setter for property: (@link ContourSettingsBuilder.ComponentTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ComponentTypeOption@endlink) ComponentType

    ##  Returns the result component type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ComponentType.setter
    def ComponentType(self, componentType: ContourSettingsBuilder.ComponentTypeOption):
        """
        Setter for property: (@link ContourSettingsBuilder.ComponentTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ComponentTypeOption@endlink) ComponentType
         Returns the result component type   
            
         
        """
        pass
    
    ## Getter for property: (@link ContourSettingsBuilder.ContourStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourStyleOption@endlink) ContourStyle
    ##  Returns the display contour style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return ContourSettingsBuilder.ContourStyleOption
    @property
    def ContourStyle(self) -> ContourSettingsBuilder.ContourStyleOption:
        """
        Getter for property: (@link ContourSettingsBuilder.ContourStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourStyleOption@endlink) ContourStyle
         Returns the display contour style   
            
         
        """
        pass
    
    ## Setter for property: (@link ContourSettingsBuilder.ContourStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourStyleOption@endlink) ContourStyle

    ##  Returns the display contour style   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ContourStyle.setter
    def ContourStyle(self, contourStyle: ContourSettingsBuilder.ContourStyleOption):
        """
        Setter for property: (@link ContourSettingsBuilder.ContourStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourStyleOption@endlink) ContourStyle
         Returns the display contour style   
            
         
        """
        pass
    
    ## Getter for property: (int) FrequenciesCount
    ##  Returns the number of frequencies.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def FrequenciesCount(self) -> int:
        """
        Getter for property: (int) FrequenciesCount
         Returns the number of frequencies.  
            
         
        """
        pass
    
    ## Getter for property: (int) FrequencyIndex
    ##  Returns the index of the Frequency to display for Natural Frequencies analysis type.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def FrequencyIndex(self) -> int:
        """
        Getter for property: (int) FrequencyIndex
         Returns the index of the Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    
    ## Setter for property: (int) FrequencyIndex

    ##  Returns the index of the Frequency to display for Natural Frequencies analysis type.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @FrequencyIndex.setter
    def FrequencyIndex(self, frequencyIndex: int):
        """
        Setter for property: (int) FrequencyIndex
         Returns the index of the Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    
    ## Getter for property: (@link ContourSettingsBuilder.ResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption@endlink) ResultType
    ##  Returns the result type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return ContourSettingsBuilder.ResultTypeOption
    @property
    def ResultType(self) -> ContourSettingsBuilder.ResultTypeOption:
        """
        Getter for property: (@link ContourSettingsBuilder.ResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption@endlink) ResultType
         Returns the result type   
            
         
        """
        pass
    
    ## Setter for property: (@link ContourSettingsBuilder.ResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption@endlink) ResultType

    ##  Returns the result type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ResultType.setter
    def ResultType(self, resultType: ContourSettingsBuilder.ResultTypeOption):
        """
        Setter for property: (@link ContourSettingsBuilder.ResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption@endlink) ResultType
         Returns the result type   
            
         
        """
        pass
    
    ##  Returns the color display styles available for a result type
    ##  @return colorStyles (@link ContourSettingsBuilder.ColorStyleOption List[NXOpen.DesignSimulation.ContourSettingsBuilder.ColorStyleOption]@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultType"> (@link ContourSettingsBuilder.ResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption@endlink) </param>
    def GetAvailableColorStyles(self, resultType: ContourSettingsBuilder.ResultTypeOption) -> List[ContourSettingsBuilder.ColorStyleOption]:
        """
         Returns the color display styles available for a result type
         @return colorStyles (@link ContourSettingsBuilder.ColorStyleOption List[NXOpen.DesignSimulation.ContourSettingsBuilder.ColorStyleOption]@endlink): .
        """
        pass
    
    ##  Returns the result components available for a result type
    ##  @return componentTypes (@link ContourSettingsBuilder.ComponentTypeOption List[NXOpen.DesignSimulation.ContourSettingsBuilder.ComponentTypeOption]@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultType"> (@link ContourSettingsBuilder.ResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption@endlink) </param>
    def GetAvailableComponentTypes(self, resultType: ContourSettingsBuilder.ResultTypeOption) -> List[ContourSettingsBuilder.ComponentTypeOption]:
        """
         Returns the result components available for a result type
         @return componentTypes (@link ContourSettingsBuilder.ComponentTypeOption List[NXOpen.DesignSimulation.ContourSettingsBuilder.ComponentTypeOption]@endlink): .
        """
        pass
    
    ##  Returns the contour display styles available for a available for a result type
    ##  @return contourStyles (@link ContourSettingsBuilder.ContourStyleOption List[NXOpen.DesignSimulation.ContourSettingsBuilder.ContourStyleOption]@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultType"> (@link ContourSettingsBuilder.ResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption@endlink) </param>
    def GetAvailableContourStyles(self, resultType: ContourSettingsBuilder.ResultTypeOption) -> List[ContourSettingsBuilder.ContourStyleOption]:
        """
         Returns the contour display styles available for a available for a result type
         @return contourStyles (@link ContourSettingsBuilder.ContourStyleOption List[NXOpen.DesignSimulation.ContourSettingsBuilder.ContourStyleOption]@endlink): .
        """
        pass
    
    ##  Returns the available result types 
    ##  @return resultTypes (@link ContourSettingsBuilder.ResultTypeOption List[NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption]@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetAvailableResultTypes(self) -> List[ContourSettingsBuilder.ResultTypeOption]:
        """
         Returns the available result types 
         @return resultTypes (@link ContourSettingsBuilder.ResultTypeOption List[NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption]@endlink): .
        """
        pass
    
    ##  Returns the name and the description of a color display option
    ##  @return A tuple consisting of (name, description). 
    ##  - name is: str.
    ##  - description is: str.

    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="colorStyle"> (@link ContourSettingsBuilder.ColorStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ColorStyleOption@endlink) </param>
    def GetColorStyleInfo(self, colorStyle: ContourSettingsBuilder.ColorStyleOption) -> Tuple[str, str]:
        """
         Returns the name and the description of a color display option
         @return A tuple consisting of (name, description). 
         - name is: str.
         - description is: str.

        """
        pass
    
    ##  Returns the name and the description of a result component
    ##  @return A tuple consisting of (name, description). 
    ##  - name is: str.
    ##  - description is: str.

    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="componentType"> (@link ContourSettingsBuilder.ComponentTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ComponentTypeOption@endlink) </param>
    def GetComponentTypeInfo(self, componentType: ContourSettingsBuilder.ComponentTypeOption) -> Tuple[str, str]:
        """
         Returns the name and the description of a result component
         @return A tuple consisting of (name, description). 
         - name is: str.
         - description is: str.

        """
        pass
    
    ##  Returns the name and the description of a contour display option
    ##  @return A tuple consisting of (name, description). 
    ##  - name is: str.
    ##  - description is: str.

    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="contourStyle"> (@link ContourSettingsBuilder.ContourStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourStyleOption@endlink) </param>
    def GetContourStyleInfo(self, contourStyle: ContourSettingsBuilder.ContourStyleOption) -> Tuple[str, str]:
        """
         Returns the name and the description of a contour display option
         @return A tuple consisting of (name, description). 
         - name is: str.
         - description is: str.

        """
        pass
    
    ##  Returns the frequency id of specified index 
    ##  @return frequencyId (int): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetFrequencyId(self, index: int) -> int:
        """
         Returns the frequency id of specified index 
         @return frequencyId (int): .
        """
        pass
    
    ##  Returns the name and the description of a result type
    ##  @return A tuple consisting of (name, description). 
    ##  - name is: str.
    ##  - description is: str.

    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultType"> (@link ContourSettingsBuilder.ResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption@endlink) </param>
    def GetResultTypeInfo(self, resultType: ContourSettingsBuilder.ResultTypeOption) -> Tuple[str, str]:
        """
         Returns the name and the description of a result type
         @return A tuple consisting of (name, description). 
         - name is: str.
         - description is: str.

        """
        pass
    
    ##  Reset contour options: Result Component, Color Style and Contour Style to 
    ##             the default values of the result type received as parameter.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultType"> (@link ContourSettingsBuilder.ResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption@endlink) </param>
    def ResetContourOptions(self, resultType: ContourSettingsBuilder.ResultTypeOption) -> None:
        """
         Reset contour options: Result Component, Color Style and Contour Style to 
                    the default values of the result type received as parameter.
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::DesignSimulation::DesignSpace NXOpen::DesignSimulation::DesignSpace@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateDesignSpaceBuilder  NXOpen::DesignSimulation::Study::CreateDesignSpaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class DesignSpaceBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.DesignSimulation.DesignSpace</ja_class> builder
    """


    ## Getter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
    ##  Returns the material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Material
    @property
    def Material(self) -> NXOpen.Material:
        """
        Getter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
         Returns the material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material

    ##  Returns the material   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Material.setter
    def Material(self, assignedMaterial: NXOpen.Material):
        """
        Setter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
         Returns the material   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the scenery body name   
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
         Returns the scenery body name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the scenery body name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the scenery body name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBody NXOpen.SelectBody@endlink) SelectBody
    ##  Returns the selected body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectBody
    @property
    def SelectBody(self) -> NXOpen.SelectBody:
        """
        Getter for property: (@link NXOpen.SelectBody NXOpen.SelectBody@endlink) SelectBody
         Returns the selected body   
            
         
        """
        pass
    
import NXOpen
##  Represents a Design Simulation Design Space data  <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::DesignSpaceBuilder  NXOpen::DesignSimulation::DesignSpaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class DesignSpace(AnalysisBody): 
    """ Represents a Design Simulation Design Space data """


    ## Add a @link NXOpen::DesignSimulation::ShapeConstraint NXOpen::DesignSimulation::ShapeConstraint@endlink  or @link NXOpen::DesignSimulation::OptimizationConstraint NXOpen::DesignSimulation::OptimizationConstraint@endlink  to the @link NXOpen::DesignSimulation::DesignSpace NXOpen::DesignSimulation::DesignSpace@endlink .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="constraintObjectTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def AddConstraint(self, constraintObjectTag: NXOpen.NXObject) -> None:
        """
        Add a @link NXOpen::DesignSimulation::ShapeConstraint NXOpen::DesignSimulation::ShapeConstraint@endlink  or @link NXOpen::DesignSimulation::OptimizationConstraint NXOpen::DesignSimulation::OptimizationConstraint@endlink  to the @link NXOpen::DesignSimulation::DesignSpace NXOpen::DesignSimulation::DesignSpace@endlink .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::ConstructionBodyCollector NXOpen::DesignSimulation::ConstructionBodyCollector@endlink  from @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  members. 
    ##  @return collection (@link ConstructionBodyCollector NXOpen.DesignSimulation.ConstructionBodyCollector@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="constructionBodies"> (@link ConstructionBody List[NXOpen.DesignSimulation.ConstructionBody]@endlink) </param>
    def CreateConstructionBodyGroup(self, constructionBodies: List[ConstructionBody]) -> ConstructionBodyCollector:
        """
         Creates a @link NXOpen::DesignSimulation::ConstructionBodyCollector NXOpen::DesignSimulation::ConstructionBodyCollector@endlink  from @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  members. 
         @return collection (@link ConstructionBodyCollector NXOpen.DesignSimulation.ConstructionBodyCollector@endlink): .
        """
        pass
    
    ## Remove a @link NXOpen::DesignSimulation::ShapeConstraint NXOpen::DesignSimulation::ShapeConstraint@endlink  or @link NXOpen::DesignSimulation::OptimizationConstraint NXOpen::DesignSimulation::OptimizationConstraint@endlink   from the @link NXOpen::DesignSimulation::DesignSpace NXOpen::DesignSimulation::DesignSpace@endlink .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="constraintObjectTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def RemoveConstraint(self, constraintObjectTag: NXOpen.NXObject) -> None:
        """
        Remove a @link NXOpen::DesignSimulation::ShapeConstraint NXOpen::DesignSimulation::ShapeConstraint@endlink  or @link NXOpen::DesignSimulation::OptimizationConstraint NXOpen::DesignSimulation::OptimizationConstraint@endlink   from the @link NXOpen::DesignSimulation::DesignSpace NXOpen::DesignSimulation::DesignSpace@endlink .
        """
        pass
    
import NXOpen
##  Represents a builder to define environmental loads for an optimization study or analysis.  <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateEnvironmentLoadBuilder  NXOpen::DesignSimulation::Study::CreateEnvironmentLoadBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## GravityEnabled </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## GravityMagnitude.Value </term> <description> 
##  
## 9806.65 (millimeters part), 32.17417 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class EnvironmentLoadBuilder(NXOpen.Builder): 
    """ Represents a builder to define environmental loads for an optimization study or analysis. """


    ## Getter for property: (bool) AmbientTemperatureEnabled
    ##  Returns the control to enable / disable use of ambient temperature for thermal analysis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def AmbientTemperatureEnabled(self) -> bool:
        """
        Getter for property: (bool) AmbientTemperatureEnabled
         Returns the control to enable / disable use of ambient temperature for thermal analysis   
            
         
        """
        pass
    
    ## Setter for property: (bool) AmbientTemperatureEnabled

    ##  Returns the control to enable / disable use of ambient temperature for thermal analysis   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @AmbientTemperatureEnabled.setter
    def AmbientTemperatureEnabled(self, enabled: bool):
        """
        Setter for property: (bool) AmbientTemperatureEnabled
         Returns the control to enable / disable use of ambient temperature for thermal analysis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AmbientTemperatureMagnitude
    ##  Returns the ambient temperature magnitude   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AmbientTemperatureMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AmbientTemperatureMagnitude
         Returns the ambient temperature magnitude   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) GravityDirection
    ##  Returns the gravity direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def GravityDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) GravityDirection
         Returns the gravity direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) GravityDirection

    ##  Returns the gravity direction   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @GravityDirection.setter
    def GravityDirection(self, gravityDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) GravityDirection
         Returns the gravity direction   
            
         
        """
        pass
    
    ## Getter for property: (bool) GravityEnabled
    ##  Returns the control to enable / disable use of gravity for the optimization or analysis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def GravityEnabled(self) -> bool:
        """
        Getter for property: (bool) GravityEnabled
         Returns the control to enable / disable use of gravity for the optimization or analysis   
            
         
        """
        pass
    
    ## Setter for property: (bool) GravityEnabled

    ##  Returns the control to enable / disable use of gravity for the optimization or analysis   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @GravityEnabled.setter
    def GravityEnabled(self, enabled: bool):
        """
        Setter for property: (bool) GravityEnabled
         Returns the control to enable / disable use of gravity for the optimization or analysis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) GravityMagnitude
    ##  Returns the gravity magnitude   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def GravityMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) GravityMagnitude
         Returns the gravity magnitude   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a builder to specify contour display settings and plot contours according to the settings
##      <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateExportToCaeBuilder  NXOpen::DesignSimulation::Study::CreateExportToCaeBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class ExportToCaeBuilder(NXOpen.Builder): 
    """
    Represents a builder to specify contour display settings and plot contours according to the settings
    """


    ##  Solver type Option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SimcenterNastran</term><description> 
    ## </description> </item></list>
    class SolverTypeOption(Enum):
        """
        Members Include: <SimcenterNastran>
        """
        SimcenterNastran: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExportToCaeBuilder.SolverTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Use body option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AllBodies</term><description> 
    ## </description> </item><item><term> 
    ## StudyBodies</term><description> 
    ## </description> </item></list>
    class UseBodyOption(Enum):
        """
        Members Include: <AllBodies> <StudyBodies>
        """
        AllBodies: int
        StudyBodies: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExportToCaeBuilder.UseBodyOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ExportToCaeBuilder.UseBodyOption NXOpen.DesignSimulation.ExportToCaeBuilder.UseBodyOption@endlink) BodyOption
    ##  Returns the use body option choice   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ExportToCaeBuilder.UseBodyOption
    @property
    def BodyOption(self) -> ExportToCaeBuilder.UseBodyOption:
        """
        Getter for property: (@link ExportToCaeBuilder.UseBodyOption NXOpen.DesignSimulation.ExportToCaeBuilder.UseBodyOption@endlink) BodyOption
         Returns the use body option choice   
            
         
        """
        pass
    
    ## Setter for property: (@link ExportToCaeBuilder.UseBodyOption NXOpen.DesignSimulation.ExportToCaeBuilder.UseBodyOption@endlink) BodyOption

    ##  Returns the use body option choice   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @BodyOption.setter
    def BodyOption(self, bodyOption: ExportToCaeBuilder.UseBodyOption):
        """
        Setter for property: (@link ExportToCaeBuilder.UseBodyOption NXOpen.DesignSimulation.ExportToCaeBuilder.UseBodyOption@endlink) BodyOption
         Returns the use body option choice   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateIdealizedPart
    ##  Returns the create idealized part option
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def CreateIdealizedPart(self) -> bool:
        """
        Getter for property: (bool) CreateIdealizedPart
         Returns the create idealized part option
                  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateIdealizedPart

    ##  Returns the create idealized part option
    ##           
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @CreateIdealizedPart.setter
    def CreateIdealizedPart(self, createIdealizedPart: bool):
        """
        Setter for property: (bool) CreateIdealizedPart
         Returns the create idealized part option
                  
            
         
        """
        pass
    
    ## Getter for property: (str) FemPartName
    ##  Returns the fem part name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def FemPartName(self) -> str:
        """
        Getter for property: (str) FemPartName
         Returns the fem part name   
            
         
        """
        pass
    
    ## Setter for property: (str) FemPartName

    ##  Returns the fem part name   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @FemPartName.setter
    def FemPartName(self, femPartName: str):
        """
        Setter for property: (str) FemPartName
         Returns the fem part name   
            
         
        """
        pass
    
    ## Getter for property: (str) IdealizedPartName
    ##  Returns the idealized part name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def IdealizedPartName(self) -> str:
        """
        Getter for property: (str) IdealizedPartName
         Returns the idealized part name   
            
         
        """
        pass
    
    ## Setter for property: (str) IdealizedPartName

    ##  Returns the idealized part name   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @IdealizedPartName.setter
    def IdealizedPartName(self, idealizedPartName: str):
        """
        Setter for property: (str) IdealizedPartName
         Returns the idealized part name   
            
         
        """
        pass
    
    ## Getter for property: (str) SimPartName
    ##  Returns the sim part name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def SimPartName(self) -> str:
        """
        Getter for property: (str) SimPartName
         Returns the sim part name   
            
         
        """
        pass
    
    ## Setter for property: (str) SimPartName

    ##  Returns the sim part name   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SimPartName.setter
    def SimPartName(self, simPartName: str):
        """
        Setter for property: (str) SimPartName
         Returns the sim part name   
            
         
        """
        pass
    
    ## Getter for property: (@link ExportToCaeBuilder.SolverTypeOption NXOpen.DesignSimulation.ExportToCaeBuilder.SolverTypeOption@endlink) SolverType
    ##  Returns the solver name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ExportToCaeBuilder.SolverTypeOption
    @property
    def SolverType(self) -> ExportToCaeBuilder.SolverTypeOption:
        """
        Getter for property: (@link ExportToCaeBuilder.SolverTypeOption NXOpen.DesignSimulation.ExportToCaeBuilder.SolverTypeOption@endlink) SolverType
         Returns the solver name   
            
         
        """
        pass
    
    ## Setter for property: (@link ExportToCaeBuilder.SolverTypeOption NXOpen.DesignSimulation.ExportToCaeBuilder.SolverTypeOption@endlink) SolverType

    ##  Returns the solver name   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SolverType.setter
    def SolverType(self, solverType: ExportToCaeBuilder.SolverTypeOption):
        """
        Setter for property: (@link ExportToCaeBuilder.SolverTypeOption NXOpen.DesignSimulation.ExportToCaeBuilder.SolverTypeOption@endlink) SolverType
         Returns the solver name   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::DesignSimulation::OptimizationConstraint NXOpen::DesignSimulation::OptimizationConstraint@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateOptimizationConstraintBuilder  NXOpen::DesignSimulation::Study::CreateOptimizationConstraintBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Type </term> <description> 
##  
## MaximumMassLimit </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class OptimizationConstraintBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.DesignSimulation.OptimizationConstraint</ja_class> builder """


    ##  define optimization constraint type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## MassTarget</term><description> 
    ## </description> </item><item><term> 
    ## MinimumMassLimit</term><description> 
    ## </description> </item><item><term> 
    ## MaximumMassLimit</term><description> 
    ## </description> </item><item><term> 
    ## MaximumStressLimit</term><description> 
    ## </description> </item><item><term> 
    ## MaximumDisplacementLimit</term><description> 
    ## </description> </item><item><term> 
    ## FirstFlexibleModeTarget</term><description> 
    ## </description> </item><item><term> 
    ## MinimumFirstFlexibleModeLimit</term><description> 
    ## </description> </item><item><term> 
    ## MaximumFirstFlexibleModeLimit</term><description> 
    ## </description> </item></list>
    class ConstraintType(Enum):
        """
        Members Include: <MassTarget> <MinimumMassLimit> <MaximumMassLimit> <MaximumStressLimit> <MaximumDisplacementLimit> <FirstFlexibleModeTarget> <MinimumFirstFlexibleModeLimit> <MaximumFirstFlexibleModeLimit>
        """
        MassTarget: int
        MinimumMassLimit: int
        MaximumMassLimit: int
        MaximumStressLimit: int
        MaximumDisplacementLimit: int
        FirstFlexibleModeTarget: int
        MinimumFirstFlexibleModeLimit: int
        MaximumFirstFlexibleModeLimit: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationConstraintBuilder.ConstraintType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  define displacement enum 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AbsoluteMagnitude</term><description> 
    ## </description> </item><item><term> 
    ## X</term><description> 
    ## </description> </item><item><term> 
    ## Y</term><description> 
    ## </description> </item><item><term> 
    ## Z</term><description> 
    ## </description> </item><item><term> 
    ## AlongVector</term><description> 
    ## </description> </item></list>
    class DisplacementOption(Enum):
        """
        Members Include: <AbsoluteMagnitude> <X> <Y> <Z> <AlongVector>
        """
        AbsoluteMagnitude: int
        X: int
        Y: int
        Z: int
        AlongVector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationConstraintBuilder.DisplacementOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  define maximum stress enum 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## UltimateTensileStrength</term><description> 
    ## </description> </item><item><term> 
    ## Yield</term><description> 
    ## </description> </item><item><term> 
    ## Absolute</term><description> 
    ## </description> </item></list>
    class MaximumStressOption(Enum):
        """
        Members Include: <UltimateTensileStrength> <Yield> <Absolute>
        """
        UltimateTensileStrength: int
        Yield: int
        Absolute: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OptimizationConstraintBuilder.MaximumStressOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AbsoluteValueOfStress
    ##  Returns the finite value of stress expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AbsoluteValueOfStress(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AbsoluteValueOfStress
         Returns the finite value of stress expression   
            
         
        """
        pass
    
    ## Getter for property: (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) DesignSpace
    ##  Returns the design space   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return DesignSpace
    @property
    def DesignSpace(self) -> DesignSpace:
        """
        Getter for property: (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) DesignSpace
         Returns the design space   
            
         
        """
        pass
    
    ## Setter for property: (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) DesignSpace

    ##  Returns the design space   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DesignSpace.setter
    def DesignSpace(self, designSpace: DesignSpace):
        """
        Setter for property: (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) DesignSpace
         Returns the design space   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) DisplacementLocation
    ##  Returns the defined location for displacement limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def DisplacementLocation(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) DisplacementLocation
         Returns the defined location for displacement limit   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) DisplacementLocation

    ##  Returns the defined location for displacement limit   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DisplacementLocation.setter
    def DisplacementLocation(self, location: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) DisplacementLocation
         Returns the defined location for displacement limit   
            
         
        """
        pass
    
    ## Getter for property: (@link OptimizationConstraintBuilder.DisplacementOption NXOpen.DesignSimulation.OptimizationConstraintBuilder.DisplacementOption@endlink) DisplacementType
    ##  Returns the displacement type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return OptimizationConstraintBuilder.DisplacementOption
    @property
    def DisplacementType(self) -> OptimizationConstraintBuilder.DisplacementOption:
        """
        Getter for property: (@link OptimizationConstraintBuilder.DisplacementOption NXOpen.DesignSimulation.OptimizationConstraintBuilder.DisplacementOption@endlink) DisplacementType
         Returns the displacement type   
            
         
        """
        pass
    
    ## Setter for property: (@link OptimizationConstraintBuilder.DisplacementOption NXOpen.DesignSimulation.OptimizationConstraintBuilder.DisplacementOption@endlink) DisplacementType

    ##  Returns the displacement type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DisplacementType.setter
    def DisplacementType(self, displacementType: OptimizationConstraintBuilder.DisplacementOption):
        """
        Setter for property: (@link OptimizationConstraintBuilder.DisplacementOption NXOpen.DesignSimulation.OptimizationConstraintBuilder.DisplacementOption@endlink) DisplacementType
         Returns the displacement type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DisplacementVector
    ##  Returns the displacement vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def DisplacementVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DisplacementVector
         Returns the displacement vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DisplacementVector

    ##  Returns the displacement vector   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DisplacementVector.setter
    def DisplacementVector(self, displacementVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DisplacementVector
         Returns the displacement vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FirstFlexibleFrequency
    ##  Returns the first flexible frequency expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FirstFlexibleFrequency(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FirstFlexibleFrequency
         Returns the first flexible frequency expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
    ##  Returns the mass expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
         Returns the mass expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDisplacement
    ##  Returns the max displacement expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDisplacement(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDisplacement
         Returns the max displacement expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxFirstFlexFrequency
    ##  Returns the max first flex frequency expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxFirstFlexFrequency(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxFirstFlexFrequency
         Returns the max first flex frequency expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxPercentOfStress
    ##  Returns the max percent of stress expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxPercentOfStress(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxPercentOfStress
         Returns the max percent of stress expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumMass
    ##  Returns the maximum mass expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumMass(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumMass
         Returns the maximum mass expression   
            
         
        """
        pass
    
    ## Getter for property: (@link OptimizationConstraintBuilder.MaximumStressOption NXOpen.DesignSimulation.OptimizationConstraintBuilder.MaximumStressOption@endlink) MaximumStressType
    ##  Returns the maximum stress type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return OptimizationConstraintBuilder.MaximumStressOption
    @property
    def MaximumStressType(self) -> OptimizationConstraintBuilder.MaximumStressOption:
        """
        Getter for property: (@link OptimizationConstraintBuilder.MaximumStressOption NXOpen.DesignSimulation.OptimizationConstraintBuilder.MaximumStressOption@endlink) MaximumStressType
         Returns the maximum stress type   
            
         
        """
        pass
    
    ## Setter for property: (@link OptimizationConstraintBuilder.MaximumStressOption NXOpen.DesignSimulation.OptimizationConstraintBuilder.MaximumStressOption@endlink) MaximumStressType

    ##  Returns the maximum stress type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MaximumStressType.setter
    def MaximumStressType(self, maxStressType: OptimizationConstraintBuilder.MaximumStressOption):
        """
        Setter for property: (@link OptimizationConstraintBuilder.MaximumStressOption NXOpen.DesignSimulation.OptimizationConstraintBuilder.MaximumStressOption@endlink) MaximumStressType
         Returns the maximum stress type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinFirstFlexFrequency
    ##  Returns the min first flex frequency expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinFirstFlexFrequency(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinFirstFlexFrequency
         Returns the min first flex frequency expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumMass
    ##  Returns the minimum mass expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinimumMass(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumMass
         Returns the minimum mass expression   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the optimization constraint name   
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
         Returns the optimization constraint name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the optimization constraint name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Name.setter
    def Name(self, optimizationConstraintName: str):
        """
        Setter for property: (str) Name
         Returns the optimization constraint name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectFace
    ##  Returns the select face   
    ##     
    ##  
    ## Getter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectFace
         Returns the select face   
            
         
        """
        pass
    
    ## Getter for property: (@link OptimizationConstraintBuilder.ConstraintType NXOpen.DesignSimulation.OptimizationConstraintBuilder.ConstraintType@endlink) Type
    ##  Returns the type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return OptimizationConstraintBuilder.ConstraintType
    @property
    def Type(self) -> OptimizationConstraintBuilder.ConstraintType:
        """
        Getter for property: (@link OptimizationConstraintBuilder.ConstraintType NXOpen.DesignSimulation.OptimizationConstraintBuilder.ConstraintType@endlink) Type
         Returns the type   
            
         
        """
        pass
    
    ## Setter for property: (@link OptimizationConstraintBuilder.ConstraintType NXOpen.DesignSimulation.OptimizationConstraintBuilder.ConstraintType@endlink) Type

    ##  Returns the type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Type.setter
    def Type(self, type: OptimizationConstraintBuilder.ConstraintType):
        """
        Setter for property: (@link OptimizationConstraintBuilder.ConstraintType NXOpen.DesignSimulation.OptimizationConstraintBuilder.ConstraintType@endlink) Type
         Returns the type   
            
         
        """
        pass
    
    ## Getter for property: (bool) UserSetName
    ##  Returns the flag indicating whether the object uses an user-defined name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    
    ## Setter for property: (bool) UserSetName

    ##  Returns the flag indicating whether the object uses an user-defined name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @UserSetName.setter
    def UserSetName(self, userSetName: bool):
        """
        Setter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Design Simulation Study Optimization Constraint  <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::OptimizationConstraintBuilder  NXOpen::DesignSimulation::OptimizationConstraintBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class OptimizationConstraint(NXOpen.NXObject): 
    """ Represents a Design Simulation Study Optimization Constraint """
    pass


import NXOpen
##  Represents the Performance Predictor Manager class. <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class PerformancePredictorManager(NXOpen.Object): 
    """ Represents the Performance Predictor Manager class."""


    ##  Abort all running Performance Predictor Analysis 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    def AbortAllSimulations() -> None:
        """
         Abort all running Performance Predictor Analysis 
        """
        pass
    
    ##  Prepare for export for CAE 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    def CreateAttributes() -> None:
        """
         Prepare for export for CAE 
        """
        pass
    
    ##  Enter live simulation application 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    def EnterPerformancePredictorApplication() -> None:
        """
         Enter live simulation application 
        """
        pass
    
    ##  Exit live simulation application 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    def ExitPerformancePredictorApplication() -> None:
        """
         Exit live simulation application 
        """
        pass
    
    ##  Gets whether delay is enabled or not 
    ##  @return delay (bool): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetDelay() -> bool:
        """
         Gets whether delay is enabled or not 
         @return delay (bool): .
        """
        pass
    
    ##  Gets whether store results is enabled or not 
    ##  @return storeResult (bool): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetStoreResults() -> bool:
        """
         Gets whether store results is enabled or not 
         @return storeResult (bool): .
        """
        pass
    
    ##  Resets measure histories of Performance Predictor 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    def ResetMeasureHistory() -> None:
        """
         Resets measure histories of Performance Predictor 
        """
        pass
    
    ##  Sets delay of Performance Predictor 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    ## <param name="delay"> (bool) </param>
    def SetDelay(delay: bool) -> None:
        """
         Sets delay of Performance Predictor 
        """
        pass
    
    ##  Sets store results of Performance Predictor 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    ## <param name="storeResult"> (bool) </param>
    def SetStoreResults(storeResult: bool) -> None:
        """
         Sets store results of Performance Predictor 
        """
        pass
    
import NXOpen
##  Represents a Design Simulation Post Manager  <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class PostManager(NXOpen.Object): 
    """ Represents a Design Simulation Post Manager """


    ##  Creates a @link NXOpen::DesignSimulation::AnimationController NXOpen::DesignSimulation::AnimationController@endlink .
    ##         
    ##  @return animationController (@link AnimationController NXOpen.DesignSimulation.AnimationController@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def CreateAnimationController(self) -> AnimationController:
        """
         Creates a @link NXOpen::DesignSimulation::AnimationController NXOpen::DesignSimulation::AnimationController@endlink .
                
         @return animationController (@link AnimationController NXOpen.DesignSimulation.AnimationController@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::ResultSettingsBuilder NXOpen::DesignSimulation::ResultSettingsBuilder@endlink .
    ##         
    ##  @return builder (@link ResultSettingsBuilder NXOpen.DesignSimulation.ResultSettingsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def CreateResultSettingsBuilder(self) -> ResultSettingsBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::ResultSettingsBuilder NXOpen::DesignSimulation::ResultSettingsBuilder@endlink .
                
         @return builder (@link ResultSettingsBuilder NXOpen.DesignSimulation.ResultSettingsBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::ViewContourBuilder NXOpen::DesignSimulation::ViewContourBuilder@endlink .
    ##         
    ##  @return builder (@link ViewContourBuilder NXOpen.DesignSimulation.ViewContourBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def CreateViewContourBuilder(self) -> ViewContourBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::ViewContourBuilder NXOpen::DesignSimulation::ViewContourBuilder@endlink .
                
         @return builder (@link ViewContourBuilder NXOpen.DesignSimulation.ViewContourBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::ViewTabularResultBuilder NXOpen::DesignSimulation::ViewTabularResultBuilder@endlink .
    ##         
    ##  @return builder (@link ViewTabularResultBuilder NXOpen.DesignSimulation.ViewTabularResultBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def CreateViewTabularResultBuilder(self) -> ViewTabularResultBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::ViewTabularResultBuilder NXOpen::DesignSimulation::ViewTabularResultBuilder@endlink .
                
         @return builder (@link ViewTabularResultBuilder NXOpen.DesignSimulation.ViewTabularResultBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::ViewXygraphBuilder NXOpen::DesignSimulation::ViewXygraphBuilder@endlink .
    ##         
    ##  @return builder (@link ViewXygraphBuilder NXOpen.DesignSimulation.ViewXygraphBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def CreateViewXygraphBuilder(self) -> ViewXygraphBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::ViewXygraphBuilder NXOpen::DesignSimulation::ViewXygraphBuilder@endlink .
                
         @return builder (@link ViewXygraphBuilder NXOpen.DesignSimulation.ViewXygraphBuilder@endlink): .
        """
        pass
    
    ##  Exports the playing contour animation to a GIF file. If there is no contour animation playing, an error will be thrown.
    ##         
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="fileName"> (str) </param>
    def ExportAnimationToGif(self, fileName: str) -> None:
        """
         Exports the playing contour animation to a GIF file. If there is no contour animation playing, an error will be thrown.
                
        """
        pass
    
    ##  Gets the Min and Max limits of a displayed Contour Plot.
    ##         
    ##  @return A tuple consisting of (minValue, maxValue, unitTag). 
    ##  - minValue is: float.
    ##  - maxValue is: float.
    ##  - unitTag is: @link NXOpen.Unit NXOpen.Unit@endlink.

    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="contourIndex"> (int) </param>
    def GetContourLimits(self, contourIndex: int) -> Tuple[float, float, NXOpen.Unit]:
        """
         Gets the Min and Max limits of a displayed Contour Plot.
                
         @return A tuple consisting of (minValue, maxValue, unitTag). 
         - minValue is: float.
         - maxValue is: float.
         - unitTag is: @link NXOpen.Unit NXOpen.Unit@endlink.

        """
        pass
    
    ##  Hides the contour.
    ##         
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def HideContour(self) -> None:
        """
         Hides the contour.
                
        """
        pass
    
    ##  Asks whether there is animation playing.
    ##         
    ##  @return isPlaying (bool): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def IsAnimationPlaying(self) -> bool:
        """
         Asks whether there is animation playing.
                
         @return isPlaying (bool): .
        """
        pass
    
    ##  Asks whether there is contour shown.
    ##         
    ##  @return isContourShown (bool): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def IsContourShown(self) -> bool:
        """
         Asks whether there is contour shown.
                
         @return isContourShown (bool): .
        """
        pass
    
    ##  Plots contour according to existing view contour settings.
    ##         
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def ShowContour(self) -> None:
        """
         Plots contour according to existing view contour settings.
                
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::DesignSimulation::ResultMeasure NXOpen::DesignSimulation::ResultMeasure@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateResultMeasureBuilder  NXOpen::DesignSimulation::Study::CreateResultMeasureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ResultValue </term> <description> 
##  
## Maximum </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2306.0.0  <br> 

class ResultMeasureBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.DesignSimulation.ResultMeasure</ja_class> builder
    """


    ##  Result component type option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## DisplacementMagnitude</term><description> 
    ## </description> </item><item><term> 
    ## DisplacementWorstInXYZ</term><description> 
    ## </description> </item><item><term> 
    ## DisplacementX</term><description> 
    ## </description> </item><item><term> 
    ## DisplacementY</term><description> 
    ## </description> </item><item><term> 
    ## DisplacementZ</term><description> 
    ## </description> </item><item><term> 
    ## StressVonMises</term><description> 
    ## </description> </item><item><term> 
    ## StressWorstPrincipal</term><description> 
    ## </description> </item><item><term> 
    ## SafetyFactorVonMises</term><description> 
    ## </description> </item><item><term> 
    ## Temperature</term><description> 
    ## </description> </item></list>
    class ResultComponentOption(Enum):
        """
        Members Include: <DisplacementMagnitude> <DisplacementWorstInXYZ> <DisplacementX> <DisplacementY> <DisplacementZ> <StressVonMises> <StressWorstPrincipal> <SafetyFactorVonMises> <Temperature>
        """
        DisplacementMagnitude: int
        DisplacementWorstInXYZ: int
        DisplacementX: int
        DisplacementY: int
        DisplacementZ: int
        StressVonMises: int
        StressWorstPrincipal: int
        SafetyFactorVonMises: int
        Temperature: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ResultMeasureBuilder.ResultComponentOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Result type option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Displacement</term><description> 
    ## </description> </item><item><term> 
    ## Stress</term><description> 
    ## </description> </item><item><term> 
    ## SafetyFactor</term><description> 
    ## </description> </item><item><term> 
    ## Thermal</term><description> 
    ## </description> </item></list>
    class ResultTypeOption(Enum):
        """
        Members Include: <Displacement> <Stress> <SafetyFactor> <Thermal>
        """
        Displacement: int
        Stress: int
        SafetyFactor: int
        Thermal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ResultMeasureBuilder.ResultTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Result value option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Minimum</term><description> 
    ## </description> </item><item><term> 
    ## Maximum</term><description> 
    ## </description> </item></list>
    class ResultValueOption(Enum):
        """
        Members Include: <Minimum> <Maximum>
        """
        Minimum: int
        Maximum: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ResultMeasureBuilder.ResultValueOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) LabelPMI
    ##  Returns the label PMI   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def LabelPMI(self) -> bool:
        """
        Getter for property: (bool) LabelPMI
         Returns the label PMI   
            
         
        """
        pass
    
    ## Setter for property: (bool) LabelPMI

    ##  Returns the label PMI   
    ##     
    ##  
    ## Setter License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @LabelPMI.setter
    def LabelPMI(self, labelPMI: bool):
        """
        Setter for property: (bool) LabelPMI
         Returns the label PMI   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the result measure name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the result measure name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the result measure name   
    ##     
    ##  
    ## Setter License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Name.setter
    def Name(self, resultMeasureName: str):
        """
        Setter for property: (str) Name
         Returns the result measure name   
            
         
        """
        pass
    
    ## Getter for property: (int) NaturalFrequenciesCount
    ##  Returns the number of Natural Frequencies computed for Natural Frequencies analysis type.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def NaturalFrequenciesCount(self) -> int:
        """
        Getter for property: (int) NaturalFrequenciesCount
         Returns the number of Natural Frequencies computed for Natural Frequencies analysis type.  
            
         
        """
        pass
    
    ## Getter for property: (int) NaturalFrequencyIndex
    ##  Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
    ##     
    ##  
    ## Getter License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def NaturalFrequencyIndex(self) -> int:
        """
        Getter for property: (int) NaturalFrequencyIndex
         Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    
    ## Setter for property: (int) NaturalFrequencyIndex

    ##  Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
    ##     
    ##  
    ## Setter License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @NaturalFrequencyIndex.setter
    def NaturalFrequencyIndex(self, resultModeIndex: int):
        """
        Setter for property: (int) NaturalFrequencyIndex
         Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    
    ## Getter for property: (@link ResultMeasureBuilder.ResultComponentOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultComponentOption@endlink) ResultComponent
    ##  Returns the result component   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ResultMeasureBuilder.ResultComponentOption
    @property
    def ResultComponent(self) -> ResultMeasureBuilder.ResultComponentOption:
        """
        Getter for property: (@link ResultMeasureBuilder.ResultComponentOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultComponentOption@endlink) ResultComponent
         Returns the result component   
            
         
        """
        pass
    
    ## Setter for property: (@link ResultMeasureBuilder.ResultComponentOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultComponentOption@endlink) ResultComponent

    ##  Returns the result component   
    ##     
    ##  
    ## Setter License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ResultComponent.setter
    def ResultComponent(self, resultComponentType: ResultMeasureBuilder.ResultComponentOption):
        """
        Setter for property: (@link ResultMeasureBuilder.ResultComponentOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultComponentOption@endlink) ResultComponent
         Returns the result component   
            
         
        """
        pass
    
    ## Getter for property: (@link ResultMeasureBuilder.ResultTypeOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultTypeOption@endlink) ResultType
    ##  Returns the result type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ResultMeasureBuilder.ResultTypeOption
    @property
    def ResultType(self) -> ResultMeasureBuilder.ResultTypeOption:
        """
        Getter for property: (@link ResultMeasureBuilder.ResultTypeOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultTypeOption@endlink) ResultType
         Returns the result type   
            
         
        """
        pass
    
    ## Setter for property: (@link ResultMeasureBuilder.ResultTypeOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultTypeOption@endlink) ResultType

    ##  Returns the result type   
    ##     
    ##  
    ## Setter License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ResultType.setter
    def ResultType(self, resultType: ResultMeasureBuilder.ResultTypeOption):
        """
        Setter for property: (@link ResultMeasureBuilder.ResultTypeOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultTypeOption@endlink) ResultType
         Returns the result type   
            
         
        """
        pass
    
    ## Getter for property: (@link ResultMeasureBuilder.ResultValueOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultValueOption@endlink) ResultValue
    ##  Returns the oepration type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ResultMeasureBuilder.ResultValueOption
    @property
    def ResultValue(self) -> ResultMeasureBuilder.ResultValueOption:
        """
        Getter for property: (@link ResultMeasureBuilder.ResultValueOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultValueOption@endlink) ResultValue
         Returns the oepration type   
            
         
        """
        pass
    
    ## Setter for property: (@link ResultMeasureBuilder.ResultValueOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultValueOption@endlink) ResultValue

    ##  Returns the oepration type   
    ##     
    ##  
    ## Setter License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ResultValue.setter
    def ResultValue(self, resultValueType: ResultMeasureBuilder.ResultValueOption):
        """
        Setter for property: (@link ResultMeasureBuilder.ResultValueOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultValueOption@endlink) ResultValue
         Returns the oepration type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectedEntities
    ##  Returns the selected entity  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectedEntities(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectedEntities
         Returns the selected entity  
            
         
        """
        pass
    
    ## Getter for property: (bool) UserSetName
    ##  Returns the flag indicating whether the object uses an user-defined name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    
    ## Setter for property: (bool) UserSetName

    ##  Returns the flag indicating whether the object uses an user-defined name   
    ##     
    ##  
    ## Setter License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @UserSetName.setter
    def UserSetName(self, userSetName: bool):
        """
        Setter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    
import NXOpen
##  Represents a Design Simulation Result Measure  <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::ResultMeasureBuilder  NXOpen::DesignSimulation::ResultMeasureBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class ResultMeasure(NXOpen.NXObject): 
    """ Represents a Design Simulation Result Measure """


    ## Getter for property: (bool) IsBlanked
    ##  Returns the blank status of this result measure.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def IsBlanked(self) -> bool:
        """
        Getter for property: (bool) IsBlanked
         Returns the blank status of this result measure.  
             
         
        """
        pass
    
    ## Getter for property: (bool) LabelPMI
    ##  Returns the label PMI   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def LabelPMI(self) -> bool:
        """
        Getter for property: (bool) LabelPMI
         Returns the label PMI   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the result measure name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the result measure name   
            
         
        """
        pass
    
    ## Getter for property: (float) NaturalFrequency
    ##  Returns the Natural Frequency (in Hz) for result measures created for natural frequencies analysis.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return float
    @property
    def NaturalFrequency(self) -> float:
        """
        Getter for property: (float) NaturalFrequency
         Returns the Natural Frequency (in Hz) for result measures created for natural frequencies analysis.  
            
         
        """
        pass
    
    ## Getter for property: (int) NaturalFrequencyIndex
    ##  Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
    ##     
    ##  
    ## Getter License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def NaturalFrequencyIndex(self) -> int:
        """
        Getter for property: (int) NaturalFrequencyIndex
         Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    
    ## Getter for property: (@link ResultMeasureBuilder.ResultComponentOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultComponentOption@endlink) ResultComponent
    ##  Returns the result component   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return ResultMeasureBuilder.ResultComponentOption
    @property
    def ResultComponent(self) -> ResultMeasureBuilder.ResultComponentOption:
        """
        Getter for property: (@link ResultMeasureBuilder.ResultComponentOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultComponentOption@endlink) ResultComponent
         Returns the result component   
            
         
        """
        pass
    
    ## Getter for property: (@link ResultMeasureBuilder.ResultTypeOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultTypeOption@endlink) ResultMeasureType
    ##  Returns the result type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return ResultMeasureBuilder.ResultTypeOption
    @property
    def ResultMeasureType(self) -> ResultMeasureBuilder.ResultTypeOption:
        """
        Getter for property: (@link ResultMeasureBuilder.ResultTypeOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultTypeOption@endlink) ResultMeasureType
         Returns the result type   
            
         
        """
        pass
    
    ## Getter for property: (@link ResultMeasureBuilder.ResultValueOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultValueOption@endlink) ResultValueType
    ##  Returns the operation type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return ResultMeasureBuilder.ResultValueOption
    @property
    def ResultValueType(self) -> ResultMeasureBuilder.ResultValueOption:
        """
        Getter for property: (@link ResultMeasureBuilder.ResultValueOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultValueOption@endlink) ResultValueType
         Returns the operation type   
            
         
        """
        pass
    
    ## Getter for property: (bool) UserSetName
    ##  Returns the flag indicating whether the object uses an user-defined name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Value
    ##  Returns the value of Result Measure as an Expression   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Value(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Value
         Returns the value of Result Measure as an Expression   
            
         
        """
        pass
    
    ##  Blanks the result measure. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def Blank(self) -> None:
        """
         Blanks the result measure. 
        """
        pass
    
    ##  Get the objects selected for measuring 
    ##  @return displayableObject (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetSelectedObjects(self) -> List[NXOpen.DisplayableObject]:
        """
         Get the objects selected for measuring 
         @return displayableObject (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
        """
        pass
    
    ##  Populates the validation object. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="validationTag"> (@link NXOpen.Validation NXOpen.Validation@endlink) </param>
    def PopulateValidation(self, validationTag: NXOpen.Validation) -> None:
        """
         Populates the validation object. 
        """
        pass
    
    ##  Unblanks the result measure. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def Unblank(self) -> None:
        """
         Unblanks the result measure. 
        """
        pass
    
import NXOpen
##  Represents a builder for specifying result settings used to display contour results for Performance Predictor Analysis. <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::PostManager::CreateResultSettingsBuilder  NXOpen::DesignSimulation::PostManager::CreateResultSettingsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ResultSettingsBuilder(ContourSettingsBuilder): 
    """ Represents a builder for specifying result settings used to display contour results for Performance Predictor Analysis."""


    ## Getter for property: (@link ViewContourBuilder.ColorDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ColorDisplayStyleOption@endlink) ColorDisplayStyle
    ##  Returns the display color style.  
    ##    This option is for different color schema's for highlighting the results ranges.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use ColorStyle from @link NXOpen::DesignSimulation::ContourSettingsBuilder NXOpen::DesignSimulation::ContourSettingsBuilder@endlink  base class instead.  <br> 

    ## @return ViewContourBuilder.ColorDisplayStyleOption
    @property
    def ColorDisplayStyle(self) -> ViewContourBuilder.ColorDisplayStyleOption:
        """
        Getter for property: (@link ViewContourBuilder.ColorDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ColorDisplayStyleOption@endlink) ColorDisplayStyle
         Returns the display color style.  
           This option is for different color schema's for highlighting the results ranges.  
         
        """
        pass
    
    ## Setter for property: (@link ViewContourBuilder.ColorDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ColorDisplayStyleOption@endlink) ColorDisplayStyle

    ##  Returns the display color style.  
    ##    This option is for different color schema's for highlighting the results ranges.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use ColorStyle from @link NXOpen::DesignSimulation::ContourSettingsBuilder NXOpen::DesignSimulation::ContourSettingsBuilder@endlink  base class instead.  <br> 

    @ColorDisplayStyle.setter
    def ColorDisplayStyle(self, colorDisplayStyle: ViewContourBuilder.ColorDisplayStyleOption):
        """
        Setter for property: (@link ViewContourBuilder.ColorDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ColorDisplayStyleOption@endlink) ColorDisplayStyle
         Returns the display color style.  
           This option is for different color schema's for highlighting the results ranges.  
         
        """
        pass
    
    ## Getter for property: (@link ViewContourBuilder.ContourDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ContourDisplayStyleOption@endlink) ContourDisplayStyle
    ##  Returns the contour display style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use ContourStyle from @link NXOpen::DesignSimulation::ContourSettingsBuilder NXOpen::DesignSimulation::ContourSettingsBuilder@endlink  base class instead.  <br> 

    ## @return ViewContourBuilder.ContourDisplayStyleOption
    @property
    def ContourDisplayStyle(self) -> ViewContourBuilder.ContourDisplayStyleOption:
        """
        Getter for property: (@link ViewContourBuilder.ContourDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ContourDisplayStyleOption@endlink) ContourDisplayStyle
         Returns the contour display style   
            
         
        """
        pass
    
    ## Setter for property: (@link ViewContourBuilder.ContourDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ContourDisplayStyleOption@endlink) ContourDisplayStyle

    ##  Returns the contour display style   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use ContourStyle from @link NXOpen::DesignSimulation::ContourSettingsBuilder NXOpen::DesignSimulation::ContourSettingsBuilder@endlink  base class instead.  <br> 

    @ContourDisplayStyle.setter
    def ContourDisplayStyle(self, contourDisplayStyle: ViewContourBuilder.ContourDisplayStyleOption):
        """
        Setter for property: (@link ViewContourBuilder.ContourDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ContourDisplayStyleOption@endlink) ContourDisplayStyle
         Returns the contour display style   
            
         
        """
        pass
    
    ## Getter for property: (@link ContourSettingsBuilder.ContourLimitOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourLimitOption@endlink) ContourLimit
    ##  Returns the Contour limit computation option for displaying results contour.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return ContourSettingsBuilder.ContourLimitOption
    @property
    def ContourLimit(self) -> ContourSettingsBuilder.ContourLimitOption:
        """
        Getter for property: (@link ContourSettingsBuilder.ContourLimitOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourLimitOption@endlink) ContourLimit
         Returns the Contour limit computation option for displaying results contour.  
             
         
        """
        pass
    
    ## Setter for property: (@link ContourSettingsBuilder.ContourLimitOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourLimitOption@endlink) ContourLimit

    ##  Returns the Contour limit computation option for displaying results contour.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ContourLimit.setter
    def ContourLimit(self, contourLimit: ContourSettingsBuilder.ContourLimitOption):
        """
        Setter for property: (@link ContourSettingsBuilder.ContourLimitOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourLimitOption@endlink) ContourLimit
         Returns the Contour limit computation option for displaying results contour.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
    ##  Returns the Material used when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material   DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material @endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Material limit from material no longer supported.  <br> 

    ## @return NXOpen.Material
    @property
    def Material(self) -> NXOpen.Material:
        """
        Getter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
         Returns the Material used when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material   DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material @endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material

    ##  Returns the Material used when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material   DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material @endlink    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Material limit from material no longer supported.  <br> 

    @Material.setter
    def Material(self, assignedMaterial: NXOpen.Material):
        """
        Setter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
         Returns the Material used when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material   DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material @endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link ViewContourBuilder.MaterialLimitOption NXOpen.DesignSimulation.ViewContourBuilder.MaterialLimitOption@endlink) MaterialLimit
    ##  Returns the Material Option  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use ContourLimit instead.  <br> 

    ## @return ViewContourBuilder.MaterialLimitOption
    @property
    def MaterialLimit(self) -> ViewContourBuilder.MaterialLimitOption:
        """
        Getter for property: (@link ViewContourBuilder.MaterialLimitOption NXOpen.DesignSimulation.ViewContourBuilder.MaterialLimitOption@endlink) MaterialLimit
         Returns the Material Option  
            
         
        """
        pass
    
    ## Setter for property: (@link ViewContourBuilder.MaterialLimitOption NXOpen.DesignSimulation.ViewContourBuilder.MaterialLimitOption@endlink) MaterialLimit

    ##  Returns the Material Option  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use ContourLimit instead.  <br> 

    @MaterialLimit.setter
    def MaterialLimit(self, materialLimitOption: ViewContourBuilder.MaterialLimitOption):
        """
        Setter for property: (@link ViewContourBuilder.MaterialLimitOption NXOpen.DesignSimulation.ViewContourBuilder.MaterialLimitOption@endlink) MaterialLimit
         Returns the Material Option  
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisBody NXOpen.DesignSimulation.AnalysisBody@endlink) MaterialLimitBody
    ##  Returns the Analysis Body used when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody   DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody @endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return AnalysisBody
    @property
    def MaterialLimitBody(self) -> AnalysisBody:
        """
        Getter for property: (@link AnalysisBody NXOpen.DesignSimulation.AnalysisBody@endlink) MaterialLimitBody
         Returns the Analysis Body used when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody   DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody @endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisBody NXOpen.DesignSimulation.AnalysisBody@endlink) MaterialLimitBody

    ##  Returns the Analysis Body used when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody   DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody @endlink    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MaterialLimitBody.setter
    def MaterialLimitBody(self, body: AnalysisBody):
        """
        Setter for property: (@link AnalysisBody NXOpen.DesignSimulation.AnalysisBody@endlink) MaterialLimitBody
         Returns the Analysis Body used when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody   DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody @endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxStressCompression
    ##  Returns the Max Stress Compression expression used for Stress Worst Principal when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined   DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined @endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxStressCompression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxStressCompression
         Returns the Max Stress Compression expression used for Stress Worst Principal when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined   DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined @endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxStressTension
    ##  Returns the Max Stress Tension expression used for Stress Worst Principal when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined   DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined @endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxStressTension(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxStressTension
         Returns the Max Stress Tension expression used for Stress Worst Principal when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined   DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined @endlink    
            
         
        """
        pass
    
    ## Getter for property: (int) NaturalFrequenciesCount
    ##  Returns the number of Natural Frequencies computed for Natural Frequencies analysis type.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use FrequenciesCount from @link NXOpen::DesignSimulation::ContourSettingsBuilder NXOpen::DesignSimulation::ContourSettingsBuilder@endlink  base class instead.  <br> 

    ## @return int
    @property
    def NaturalFrequenciesCount(self) -> int:
        """
        Getter for property: (int) NaturalFrequenciesCount
         Returns the number of Natural Frequencies computed for Natural Frequencies analysis type.  
            
         
        """
        pass
    
    ## Getter for property: (int) NaturalFrequencyIndex
    ##  Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use FrequencyIndex from @link NXOpen::DesignSimulation::ContourSettingsBuilder NXOpen::DesignSimulation::ContourSettingsBuilder@endlink  base class instead.  <br> 

    ## @return int
    @property
    def NaturalFrequencyIndex(self) -> int:
        """
        Getter for property: (int) NaturalFrequencyIndex
         Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    
    ## Setter for property: (int) NaturalFrequencyIndex

    ##  Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use FrequencyIndex from @link NXOpen::DesignSimulation::ContourSettingsBuilder NXOpen::DesignSimulation::ContourSettingsBuilder@endlink  base class instead.  <br> 

    @NaturalFrequencyIndex.setter
    def NaturalFrequencyIndex(self, frequencyIndex: int):
        """
        Setter for property: (int) NaturalFrequencyIndex
         Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    
    ## Getter for property: (@link ViewContourBuilder.ResultComponentOption NXOpen.DesignSimulation.ViewContourBuilder.ResultComponentOption@endlink) ResultComponent
    ##  Returns the result component type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use ResultType and ComponentType from @link NXOpen::DesignSimulation::ContourSettingsBuilder NXOpen::DesignSimulation::ContourSettingsBuilder@endlink  base class instead.  <br> 

    ## @return ViewContourBuilder.ResultComponentOption
    @property
    def ResultComponent(self) -> ViewContourBuilder.ResultComponentOption:
        """
        Getter for property: (@link ViewContourBuilder.ResultComponentOption NXOpen.DesignSimulation.ViewContourBuilder.ResultComponentOption@endlink) ResultComponent
         Returns the result component type   
            
         
        """
        pass
    
    ## Setter for property: (@link ViewContourBuilder.ResultComponentOption NXOpen.DesignSimulation.ViewContourBuilder.ResultComponentOption@endlink) ResultComponent

    ##  Returns the result component type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use ResultType and ComponentType from @link NXOpen::DesignSimulation::ContourSettingsBuilder NXOpen::DesignSimulation::ContourSettingsBuilder@endlink  base class instead.  <br> 

    @ResultComponent.setter
    def ResultComponent(self, resultComponentType: ViewContourBuilder.ResultComponentOption):
        """
        Setter for property: (@link ViewContourBuilder.ResultComponentOption NXOpen.DesignSimulation.ViewContourBuilder.ResultComponentOption@endlink) ResultComponent
         Returns the result component type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YieldStrength
    ##  Returns the Yield Strength expression used for Stress Von Mises when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined   DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined @endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YieldStrength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YieldStrength
         Returns the Yield Strength expression used for Stress Von Mises when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined   DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined @endlink    
            
         
        """
        pass
    
    ##  Checks the selected for animation state of coresponding Frequency index.
    ##  @return isFrequencySelected (bool): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="frequrncyIndex"> (int) </param>
    def IsFrequencySelectedForAnimation(self, frequrncyIndex: int) -> bool:
        """
         Checks the selected for animation state of coresponding Frequency index.
         @return isFrequencySelected (bool): .
        """
        pass
    
    ##  The check state of coresponding Natural Frequency mode 
    ##  @return isFrequencySelected (bool): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use IsFrequencySelectedForAnimation method instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="frequrncyIndex"> (int) </param>
    def IsNaturalFrequencySelectedForAnimation(self, frequrncyIndex: int) -> bool:
        """
         The check state of coresponding Natural Frequency mode 
         @return isFrequencySelected (bool): .
        """
        pass
    
    ##  Sets the selected for animation state of coresponding Frequency index.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="frequencyIndex"> (int) </param>
    ## <param name="isFrequencySelected"> (bool) </param>
    def SetFrequencySelectedForAnimation(self, frequencyIndex: int, isFrequencySelected: bool) -> None:
        """
         Sets the selected for animation state of coresponding Frequency index.
        """
        pass
    
    ##  The check state of coresponding Natural Frequency mode.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use SetFrequencySelectedForAnimation method instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="frequencyIndex"> (int) </param>
    ## <param name="isFrequencySelected"> (bool) </param>
    def SetNaturalFrequencySelectedForAnimation(self, frequencyIndex: int, isFrequencySelected: bool) -> None:
        """
         The check state of coresponding Natural Frequency mode.
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::DesignSimulation::SceneryBody NXOpen::DesignSimulation::SceneryBody@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateSceneryBodyBuilder  NXOpen::DesignSimulation::Study::CreateSceneryBodyBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SceneryBodyBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.DesignSimulation.SceneryBody</ja_class> builder
    """


    ##  This enum specifies how the material is defined 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## InheritedFromBody</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item><item><term> 
    ## Default</term><description> 
    ## </description> </item></list>
    class MaterialDefinitionType(Enum):
        """
        Members Include: <InheritedFromBody> <UserDefined> <Default>
        """
        InheritedFromBody: int
        UserDefined: int
        Default: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SceneryBodyBuilder.MaterialDefinitionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) Bodies
    ##  Returns the selected body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def Bodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) Bodies
         Returns the selected body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
    ##  Returns the assigned material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Material
    @property
    def Material(self) -> NXOpen.Material:
        """
        Getter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
         Returns the assigned material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material

    ##  Returns the assigned material   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Material.setter
    def Material(self, assignedMaterial: NXOpen.Material):
        """
        Setter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
         Returns the assigned material   
            
         
        """
        pass
    
    ## Getter for property: (@link SceneryBodyBuilder.MaterialDefinitionType NXOpen.DesignSimulation.SceneryBodyBuilder.MaterialDefinitionType@endlink) MaterialDefinition
    ##  Returns the way material is assigned   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return SceneryBodyBuilder.MaterialDefinitionType
    @property
    def MaterialDefinition(self) -> SceneryBodyBuilder.MaterialDefinitionType:
        """
        Getter for property: (@link SceneryBodyBuilder.MaterialDefinitionType NXOpen.DesignSimulation.SceneryBodyBuilder.MaterialDefinitionType@endlink) MaterialDefinition
         Returns the way material is assigned   
            
         
        """
        pass
    
    ## Setter for property: (@link SceneryBodyBuilder.MaterialDefinitionType NXOpen.DesignSimulation.SceneryBodyBuilder.MaterialDefinitionType@endlink) MaterialDefinition

    ##  Returns the way material is assigned   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @MaterialDefinition.setter
    def MaterialDefinition(self, materialDefinition: SceneryBodyBuilder.MaterialDefinitionType):
        """
        Setter for property: (@link SceneryBodyBuilder.MaterialDefinitionType NXOpen.DesignSimulation.SceneryBodyBuilder.MaterialDefinitionType@endlink) MaterialDefinition
         Returns the way material is assigned   
            
         
        """
        pass
    
    ## Getter for property: (str) SceneryBodyName
    ##  Returns the scenery body name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def SceneryBodyName(self) -> str:
        """
        Getter for property: (str) SceneryBodyName
         Returns the scenery body name   
            
         
        """
        pass
    
    ## Setter for property: (str) SceneryBodyName

    ##  Returns the scenery body name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SceneryBodyName.setter
    def SceneryBodyName(self, sceneryBodyName: str):
        """
        Setter for property: (str) SceneryBodyName
         Returns the scenery body name   
            
         
        """
        pass
    
##  Represents a Design Simulation Study Scenery Body   <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::SceneryBodyBuilder  NXOpen::DesignSimulation::SceneryBodyBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SceneryBody(AnalysisBody): 
    """ Represents a Design Simulation Study Scenery Body  """
    pass


import NXOpen
##  Represents a @link NXOpen::DesignSimulation::ShapeConstraint NXOpen::DesignSimulation::ShapeConstraint@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateShapeConstraintBuilder  NXOpen::DesignSimulation::Study::CreateShapeConstraintBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CenterOfGravityPlaneOffset1.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## CenterOfGravityPlaneOffset2.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## CenterOfGravityZoneRadius.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## DraftAngle.Value </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DraftPartingObjectOptions </term> <description> 
##  
## SpecifiedPlane </description> </item> 
## 
## <item><term> 
##  
## ExtrudeBiDirectionFlag </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## FillFromDirectionOptions </term> <description> 
##  
## Unidirectional </description> </item> 
## 
## <item><term> 
##  
## MaxOverhangAngle </term> <description> 
##  
## Degrees45 </description> </item> 
## 
## <item><term> 
##  
## MaximumDiameter.Value </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MaximumWallThickness.Value </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MinimumDiameter.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MinimumWallThickness.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MultiAxisToolingOption </term> <description> 
##  
## TwoAndHalfAxis </description> </item> 
## 
## <item><term> 
##  
## PlanarSymmetryInputMode </term> <description> 
##  
## Whole </description> </item> 
## 
## <item><term> 
##  
## Type </term> <description> 
##  
## PlanarSymmetry </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class ShapeConstraintBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.DesignSimulation.ShapeConstraint</ja_class> builder """


    ##  Center of Gravity Option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## KeepWithinSphere</term><description> 
    ## </description> </item><item><term> 
    ## KeepWithinCylinder</term><description> 
    ## </description> </item><item><term> 
    ## KeepOnPlane</term><description> 
    ## </description> </item><item><term> 
    ## KeepWithinDistanceToPlane</term><description> 
    ## </description> </item></list>
    class CenterOfGravityLocationType(Enum):
        """
        Members Include: <KeepWithinSphere> <KeepWithinCylinder> <KeepOnPlane> <KeepWithinDistanceToPlane>
        """
        KeepWithinSphere: int
        KeepWithinCylinder: int
        KeepOnPlane: int
        KeepWithinDistanceToPlane: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.CenterOfGravityLocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Shape Constraint Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## PlanarSymmetry</term><description> 
    ## </description> </item><item><term> 
    ## RepeatedRotationalSymmetry</term><description> 
    ## </description> </item><item><term> 
    ## SegmentalRotationalSymmetry</term><description> 
    ## </description> </item><item><term> 
    ## ExtrudeAlongVector</term><description> 
    ## </description> </item><item><term> 
    ## DraftAngle</term><description> 
    ## </description> </item><item><term> 
    ## MinimumMemberSize</term><description> 
    ## </description> </item><item><term> 
    ## MaximumMemberSize</term><description> 
    ## </description> </item><item><term> 
    ## MinimumWallThickness</term><description> 
    ## </description> </item><item><term> 
    ## MaximumWallThickness</term><description> 
    ## </description> </item><item><term> 
    ## OverhangingGeometryPrevention</term><description> 
    ## </description> </item><item><term> 
    ## SelfSupporting</term><description> 
    ## </description> </item><item><term> 
    ## ThroughHolePrevention</term><description> 
    ## </description> </item><item><term> 
    ## RevolutionAxis</term><description> 
    ## </description> </item><item><term> 
    ## CenterOfGravityLocation</term><description> 
    ## </description> </item><item><term> 
    ## FillVoid</term><description> 
    ## </description> </item><item><term> 
    ## FillFromDirection</term><description> 
    ## </description> </item><item><term> 
    ## MultiAxisTooling</term><description> 
    ## </description> </item></list>
    class ConstraintType(Enum):
        """
        Members Include: <PlanarSymmetry> <RepeatedRotationalSymmetry> <SegmentalRotationalSymmetry> <ExtrudeAlongVector> <DraftAngle> <MinimumMemberSize> <MaximumMemberSize> <MinimumWallThickness> <MaximumWallThickness> <OverhangingGeometryPrevention> <SelfSupporting> <ThroughHolePrevention> <RevolutionAxis> <CenterOfGravityLocation> <FillVoid> <FillFromDirection> <MultiAxisTooling>
        """
        PlanarSymmetry: int
        RepeatedRotationalSymmetry: int
        SegmentalRotationalSymmetry: int
        ExtrudeAlongVector: int
        DraftAngle: int
        MinimumMemberSize: int
        MaximumMemberSize: int
        MinimumWallThickness: int
        MaximumWallThickness: int
        OverhangingGeometryPrevention: int
        SelfSupporting: int
        ThroughHolePrevention: int
        RevolutionAxis: int
        CenterOfGravityLocation: int
        FillVoid: int
        FillFromDirection: int
        MultiAxisTooling: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.ConstraintType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Draft Angle Parting Object Options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SpecifiedPlane</term><description> 
    ## </description> </item><item><term> 
    ## SpecifiedFace</term><description> 
    ## </description> </item><item><term> 
    ## AutomaticFace</term><description> 
    ## </description> </item></list>
    class DraftPartingObjectType(Enum):
        """
        Members Include: <SpecifiedPlane> <SpecifiedFace> <AutomaticFace>
        """
        SpecifiedPlane: int
        SpecifiedFace: int
        AutomaticFace: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.DraftPartingObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Fill from Direction Options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unidirectional</term><description> 
    ## </description> </item><item><term> 
    ## BidirectionalFromPlane</term><description> 
    ## </description> </item><item><term> 
    ## SymmetricalFromPlane</term><description> 
    ## </description> </item><item><term> 
    ## BidirectionalInBetween</term><description> 
    ## </description> </item></list>
    class FillFromDirectionType(Enum):
        """
        Members Include: <Unidirectional> <BidirectionalFromPlane> <SymmetricalFromPlane> <BidirectionalInBetween>
        """
        Unidirectional: int
        BidirectionalFromPlane: int
        SymmetricalFromPlane: int
        BidirectionalInBetween: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.FillFromDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Max Overhang Angle Option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Degrees27</term><description> 
    ## </description> </item><item><term> 
    ## Degrees45</term><description> 
    ## </description> </item><item><term> 
    ## Degrees65</term><description> 
    ## </description> </item></list>
    class MaxOverhangAngleValue(Enum):
        """
        Members Include: <Degrees27> <Degrees45> <Degrees65>
        """
        Degrees27: int
        Degrees45: int
        Degrees65: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.MaxOverhangAngleValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Multi Axis Tooling Options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## TwoAndHalfAxis</term><description> 
    ## </description> </item><item><term> 
    ## ThreeAxis</term><description> 
    ## </description> </item><item><term> 
    ## FiveAxis</term><description> 
    ## </description> </item></list>
    class MultiAxisToolingType(Enum):
        """
        Members Include: <TwoAndHalfAxis> <ThreeAxis> <FiveAxis>
        """
        TwoAndHalfAxis: int
        ThreeAxis: int
        FiveAxis: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.MultiAxisToolingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Planar Symmetry Input Option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Segment</term><description> 
    ## </description> </item><item><term> 
    ## Whole</term><description> 
    ## </description> </item></list>
    class PlanarSymmetryInputOption(Enum):
        """
        Members Include: <Segment> <Whole>
        """
        Segment: int
        Whole: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.PlanarSymmetryInputOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BasePlaneNormal
    ##  Returns the Multi Axis Tooling base plane normal   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def BasePlaneNormal(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BasePlaneNormal
         Returns the Multi Axis Tooling base plane normal   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BasePlaneNormal

    ##  Returns the Multi Axis Tooling base plane normal   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BasePlaneNormal.setter
    def BasePlaneNormal(self, basePlaneNormal: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BasePlaneNormal
         Returns the Multi Axis Tooling base plane normal   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) CenterOfGravityAxis
    ##  Returns the Center of Gravity Axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Axis
    @property
    def CenterOfGravityAxis(self) -> NXOpen.Axis:
        """
        Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) CenterOfGravityAxis
         Returns the Center of Gravity Axis   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) CenterOfGravityAxis

    ##  Returns the Center of Gravity Axis   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CenterOfGravityAxis.setter
    def CenterOfGravityAxis(self, centerOfGravityAxis: NXOpen.Axis):
        """
        Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) CenterOfGravityAxis
         Returns the Center of Gravity Axis   
            
         
        """
        pass
    
    ## Getter for property: (@link ShapeConstraintBuilder.CenterOfGravityLocationType NXOpen.DesignSimulation.ShapeConstraintBuilder.CenterOfGravityLocationType@endlink) CenterOfGravityLocationOption
    ##  Returns the Center of Gravity Option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ShapeConstraintBuilder.CenterOfGravityLocationType
    @property
    def CenterOfGravityLocationOption(self) -> ShapeConstraintBuilder.CenterOfGravityLocationType:
        """
        Getter for property: (@link ShapeConstraintBuilder.CenterOfGravityLocationType NXOpen.DesignSimulation.ShapeConstraintBuilder.CenterOfGravityLocationType@endlink) CenterOfGravityLocationOption
         Returns the Center of Gravity Option   
            
         
        """
        pass
    
    ## Setter for property: (@link ShapeConstraintBuilder.CenterOfGravityLocationType NXOpen.DesignSimulation.ShapeConstraintBuilder.CenterOfGravityLocationType@endlink) CenterOfGravityLocationOption

    ##  Returns the Center of Gravity Option   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CenterOfGravityLocationOption.setter
    def CenterOfGravityLocationOption(self, centerOfGravityOption: ShapeConstraintBuilder.CenterOfGravityLocationType):
        """
        Setter for property: (@link ShapeConstraintBuilder.CenterOfGravityLocationType NXOpen.DesignSimulation.ShapeConstraintBuilder.CenterOfGravityLocationType@endlink) CenterOfGravityLocationOption
         Returns the Center of Gravity Option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) CenterOfGravityPlane
    ##  Returns the Center of Gravity Plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def CenterOfGravityPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) CenterOfGravityPlane
         Returns the Center of Gravity Plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) CenterOfGravityPlane

    ##  Returns the Center of Gravity Plane   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CenterOfGravityPlane.setter
    def CenterOfGravityPlane(self, centerOfGravityPlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) CenterOfGravityPlane
         Returns the Center of Gravity Plane   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CenterOfGravityPlaneOffset1
    ##  Returns the Center of Gravity Plane Upper Limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def CenterOfGravityPlaneOffset1(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CenterOfGravityPlaneOffset1
         Returns the Center of Gravity Plane Upper Limit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CenterOfGravityPlaneOffset2
    ##  Returns the Center of Gravity Plane Lower Limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def CenterOfGravityPlaneOffset2(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CenterOfGravityPlaneOffset2
         Returns the Center of Gravity Plane Lower Limit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) CenterOfGravityPoint
    ##  Returns the Center of Gravity Location   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def CenterOfGravityPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) CenterOfGravityPoint
         Returns the Center of Gravity Location   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) CenterOfGravityPoint

    ##  Returns the Center of Gravity Location   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CenterOfGravityPoint.setter
    def CenterOfGravityPoint(self, locationPt: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) CenterOfGravityPoint
         Returns the Center of Gravity Location   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CenterOfGravityZoneRadius
    ##  Returns the Center of Gravity Zone Radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def CenterOfGravityZoneRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CenterOfGravityZoneRadius
         Returns the Center of Gravity Zone Radius   
            
         
        """
        pass
    
    ## Getter for property: (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) DesignSpace
    ##  Returns the design space   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return DesignSpace
    @property
    def DesignSpace(self) -> DesignSpace:
        """
        Getter for property: (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) DesignSpace
         Returns the design space   
            
         
        """
        pass
    
    ## Setter for property: (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) DesignSpace

    ##  Returns the design space   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DesignSpace.setter
    def DesignSpace(self, designSpace: DesignSpace):
        """
        Setter for property: (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) DesignSpace
         Returns the design space   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DraftAngle
    ##  Returns the draft angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DraftAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DraftAngle
         Returns the draft angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DraftDrawDirection
    ##  Returns the draft draw direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def DraftDrawDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DraftDrawDirection
         Returns the draft draw direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DraftDrawDirection

    ##  Returns the draft draw direction   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DraftDrawDirection.setter
    def DraftDrawDirection(self, draftDrawDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DraftDrawDirection
         Returns the draft draw direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) DraftPartingFace
    ##  Returns the draft parting faces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def DraftPartingFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) DraftPartingFace
         Returns the draft parting faces   
            
         
        """
        pass
    
    ## Getter for property: (@link ShapeConstraintBuilder.DraftPartingObjectType NXOpen.DesignSimulation.ShapeConstraintBuilder.DraftPartingObjectType@endlink) DraftPartingObjectOptions
    ##  Returns the Draft Angle Parting Object Options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ShapeConstraintBuilder.DraftPartingObjectType
    @property
    def DraftPartingObjectOptions(self) -> ShapeConstraintBuilder.DraftPartingObjectType:
        """
        Getter for property: (@link ShapeConstraintBuilder.DraftPartingObjectType NXOpen.DesignSimulation.ShapeConstraintBuilder.DraftPartingObjectType@endlink) DraftPartingObjectOptions
         Returns the Draft Angle Parting Object Options   
            
         
        """
        pass
    
    ## Setter for property: (@link ShapeConstraintBuilder.DraftPartingObjectType NXOpen.DesignSimulation.ShapeConstraintBuilder.DraftPartingObjectType@endlink) DraftPartingObjectOptions

    ##  Returns the Draft Angle Parting Object Options   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DraftPartingObjectOptions.setter
    def DraftPartingObjectOptions(self, draftPartingObjectOptions: ShapeConstraintBuilder.DraftPartingObjectType):
        """
        Setter for property: (@link ShapeConstraintBuilder.DraftPartingObjectType NXOpen.DesignSimulation.ShapeConstraintBuilder.DraftPartingObjectType@endlink) DraftPartingObjectOptions
         Returns the Draft Angle Parting Object Options   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) DraftPartingPlane
    ##  Returns the draft parting plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def DraftPartingPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) DraftPartingPlane
         Returns the draft parting plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) DraftPartingPlane

    ##  Returns the draft parting plane   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DraftPartingPlane.setter
    def DraftPartingPlane(self, draftPartingPlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) DraftPartingPlane
         Returns the draft parting plane   
            
         
        """
        pass
    
    ## Getter for property: (bool) ExtrudeBiDirectionFlag
    ##  Returns the extrude along vector bi-direction flag   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ExtrudeBiDirectionFlag(self) -> bool:
        """
        Getter for property: (bool) ExtrudeBiDirectionFlag
         Returns the extrude along vector bi-direction flag   
            
         
        """
        pass
    
    ## Setter for property: (bool) ExtrudeBiDirectionFlag

    ##  Returns the extrude along vector bi-direction flag   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ExtrudeBiDirectionFlag.setter
    def ExtrudeBiDirectionFlag(self, extBiDirection: bool):
        """
        Setter for property: (bool) ExtrudeBiDirectionFlag
         Returns the extrude along vector bi-direction flag   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ExtrudeDirection
    ##  Returns the extrude along vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ExtrudeDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ExtrudeDirection
         Returns the extrude along vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ExtrudeDirection

    ##  Returns the extrude along vector   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ExtrudeDirection.setter
    def ExtrudeDirection(self, extDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ExtrudeDirection
         Returns the extrude along vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) FillBasePlane
    ##  Returns the fill base plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def FillBasePlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) FillBasePlane
         Returns the fill base plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) FillBasePlane

    ##  Returns the fill base plane   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @FillBasePlane.setter
    def FillBasePlane(self, fillBasePlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) FillBasePlane
         Returns the fill base plane   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FillDirection
    ##  Returns the fill direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def FillDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FillDirection
         Returns the fill direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FillDirection

    ##  Returns the fill direction   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @FillDirection.setter
    def FillDirection(self, fillDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FillDirection
         Returns the fill direction   
            
         
        """
        pass
    
    ## Getter for property: (@link ShapeConstraintBuilder.FillFromDirectionType NXOpen.DesignSimulation.ShapeConstraintBuilder.FillFromDirectionType@endlink) FillFromDirectionOptions
    ##  Returns the Fill from Direction Options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return ShapeConstraintBuilder.FillFromDirectionType
    @property
    def FillFromDirectionOptions(self) -> ShapeConstraintBuilder.FillFromDirectionType:
        """
        Getter for property: (@link ShapeConstraintBuilder.FillFromDirectionType NXOpen.DesignSimulation.ShapeConstraintBuilder.FillFromDirectionType@endlink) FillFromDirectionOptions
         Returns the Fill from Direction Options   
            
         
        """
        pass
    
    ## Setter for property: (@link ShapeConstraintBuilder.FillFromDirectionType NXOpen.DesignSimulation.ShapeConstraintBuilder.FillFromDirectionType@endlink) FillFromDirectionOptions

    ##  Returns the Fill from Direction Options   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @FillFromDirectionOptions.setter
    def FillFromDirectionOptions(self, fillFromDirectionOptions: ShapeConstraintBuilder.FillFromDirectionType):
        """
        Setter for property: (@link ShapeConstraintBuilder.FillFromDirectionType NXOpen.DesignSimulation.ShapeConstraintBuilder.FillFromDirectionType@endlink) FillFromDirectionOptions
         Returns the Fill from Direction Options   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) FirstLimitPlane
    ##  Returns the first limit plane for Segmental Rotational Symmetry type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def FirstLimitPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) FirstLimitPlane
         Returns the first limit plane for Segmental Rotational Symmetry type   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) FirstLimitPlane

    ##  Returns the first limit plane for Segmental Rotational Symmetry type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @FirstLimitPlane.setter
    def FirstLimitPlane(self, firstLimitPlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) FirstLimitPlane
         Returns the first limit plane for Segmental Rotational Symmetry type   
            
         
        """
        pass
    
    ## Getter for property: (@link ShapeConstraintBuilder.MaxOverhangAngleValue NXOpen.DesignSimulation.ShapeConstraintBuilder.MaxOverhangAngleValue@endlink) MaxOverhangAngle
    ##  Returns the Max Overhang Angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ShapeConstraintBuilder.MaxOverhangAngleValue
    @property
    def MaxOverhangAngle(self) -> ShapeConstraintBuilder.MaxOverhangAngleValue:
        """
        Getter for property: (@link ShapeConstraintBuilder.MaxOverhangAngleValue NXOpen.DesignSimulation.ShapeConstraintBuilder.MaxOverhangAngleValue@endlink) MaxOverhangAngle
         Returns the Max Overhang Angle   
            
         
        """
        pass
    
    ## Setter for property: (@link ShapeConstraintBuilder.MaxOverhangAngleValue NXOpen.DesignSimulation.ShapeConstraintBuilder.MaxOverhangAngleValue@endlink) MaxOverhangAngle

    ##  Returns the Max Overhang Angle   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MaxOverhangAngle.setter
    def MaxOverhangAngle(self, maxOverhangAngle: ShapeConstraintBuilder.MaxOverhangAngleValue):
        """
        Setter for property: (@link ShapeConstraintBuilder.MaxOverhangAngleValue NXOpen.DesignSimulation.ShapeConstraintBuilder.MaxOverhangAngleValue@endlink) MaxOverhangAngle
         Returns the Max Overhang Angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumDiameter
    ##  Returns the Maximum Member Size diameter value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumDiameter
         Returns the Maximum Member Size diameter value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumWallThickness
    ##  Returns the Maximum Member Wall Thickness value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumWallThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumWallThickness
         Returns the Maximum Member Wall Thickness value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumDiameter
    ##  Returns the Minimum Member Size diameter value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinimumDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumDiameter
         Returns the Minimum Member Size diameter value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumWallThickness
    ##  Returns the Minimum Member Wall Thickness value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinimumWallThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumWallThickness
         Returns the Minimum Member Wall Thickness value   
            
         
        """
        pass
    
    ## Getter for property: (@link ShapeConstraintBuilder.MultiAxisToolingType NXOpen.DesignSimulation.ShapeConstraintBuilder.MultiAxisToolingType@endlink) MultiAxisToolingOption
    ##  Returns the Multi Axis Tooling Option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return ShapeConstraintBuilder.MultiAxisToolingType
    @property
    def MultiAxisToolingOption(self) -> ShapeConstraintBuilder.MultiAxisToolingType:
        """
        Getter for property: (@link ShapeConstraintBuilder.MultiAxisToolingType NXOpen.DesignSimulation.ShapeConstraintBuilder.MultiAxisToolingType@endlink) MultiAxisToolingOption
         Returns the Multi Axis Tooling Option   
            
         
        """
        pass
    
    ## Setter for property: (@link ShapeConstraintBuilder.MultiAxisToolingType NXOpen.DesignSimulation.ShapeConstraintBuilder.MultiAxisToolingType@endlink) MultiAxisToolingOption

    ##  Returns the Multi Axis Tooling Option   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @MultiAxisToolingOption.setter
    def MultiAxisToolingOption(self, multiAxisToolingOption: ShapeConstraintBuilder.MultiAxisToolingType):
        """
        Setter for property: (@link ShapeConstraintBuilder.MultiAxisToolingType NXOpen.DesignSimulation.ShapeConstraintBuilder.MultiAxisToolingType@endlink) MultiAxisToolingOption
         Returns the Multi Axis Tooling Option   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the shape constraint name   
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
         Returns the shape constraint name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the shape constraint name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Name.setter
    def Name(self, shapeConstraintName: str):
        """
        Setter for property: (str) Name
         Returns the shape constraint name   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfSegments
    ##  Returns the number of segments   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def NumberOfSegments(self) -> int:
        """
        Getter for property: (int) NumberOfSegments
         Returns the number of segments   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfSegments

    ##  Returns the number of segments   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NumberOfSegments.setter
    def NumberOfSegments(self, numberOfSegments: int):
        """
        Setter for property: (int) NumberOfSegments
         Returns the number of segments   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OverhangVector
    ##  Returns the overhang vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def OverhangVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OverhangVector
         Returns the overhang vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OverhangVector

    ##  Returns the overhang vector   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @OverhangVector.setter
    def OverhangVector(self, overhangVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OverhangVector
         Returns the overhang vector   
            
         
        """
        pass
    
    ## Getter for property: (@link ShapeConstraintBuilder.PlanarSymmetryInputOption NXOpen.DesignSimulation.ShapeConstraintBuilder.PlanarSymmetryInputOption@endlink) PlanarSymmetryInputMode
    ##  Returns the input mode for planar symmetry    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ShapeConstraintBuilder.PlanarSymmetryInputOption
    @property
    def PlanarSymmetryInputMode(self) -> ShapeConstraintBuilder.PlanarSymmetryInputOption:
        """
        Getter for property: (@link ShapeConstraintBuilder.PlanarSymmetryInputOption NXOpen.DesignSimulation.ShapeConstraintBuilder.PlanarSymmetryInputOption@endlink) PlanarSymmetryInputMode
         Returns the input mode for planar symmetry    
            
         
        """
        pass
    
    ## Setter for property: (@link ShapeConstraintBuilder.PlanarSymmetryInputOption NXOpen.DesignSimulation.ShapeConstraintBuilder.PlanarSymmetryInputOption@endlink) PlanarSymmetryInputMode

    ##  Returns the input mode for planar symmetry    
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PlanarSymmetryInputMode.setter
    def PlanarSymmetryInputMode(self, planarSymmetyrInputMode: ShapeConstraintBuilder.PlanarSymmetryInputOption):
        """
        Setter for property: (@link ShapeConstraintBuilder.PlanarSymmetryInputOption NXOpen.DesignSimulation.ShapeConstraintBuilder.PlanarSymmetryInputOption@endlink) PlanarSymmetryInputMode
         Returns the input mode for planar symmetry    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSymmetryPlane1
    ##  Returns the first symmetry plane for Planar Symmetry type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def PlanarSymmetryPlane1(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSymmetryPlane1
         Returns the first symmetry plane for Planar Symmetry type   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSymmetryPlane1

    ##  Returns the first symmetry plane for Planar Symmetry type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PlanarSymmetryPlane1.setter
    def PlanarSymmetryPlane1(self, symmetryPlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSymmetryPlane1
         Returns the first symmetry plane for Planar Symmetry type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSymmetryPlane2
    ##  Returns the second symmetry plane for Planar Symmetry type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def PlanarSymmetryPlane2(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSymmetryPlane2
         Returns the second symmetry plane for Planar Symmetry type   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSymmetryPlane2

    ##  Returns the second symmetry plane for Planar Symmetry type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PlanarSymmetryPlane2.setter
    def PlanarSymmetryPlane2(self, symmetryPlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlanarSymmetryPlane2
         Returns the second symmetry plane for Planar Symmetry type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) RevolutionAxis
    ##  Returns the Revolve about axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Axis
    @property
    def RevolutionAxis(self) -> NXOpen.Axis:
        """
        Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) RevolutionAxis
         Returns the Revolve about axis   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) RevolutionAxis

    ##  Returns the Revolve about axis   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RevolutionAxis.setter
    def RevolutionAxis(self, revolutionAxis: NXOpen.Axis):
        """
        Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) RevolutionAxis
         Returns the Revolve about axis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) RotationalSymmetryAxis
    ##  Returns the Rotational Symmetry axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Axis
    @property
    def RotationalSymmetryAxis(self) -> NXOpen.Axis:
        """
        Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) RotationalSymmetryAxis
         Returns the Rotational Symmetry axis   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) RotationalSymmetryAxis

    ##  Returns the Rotational Symmetry axis   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RotationalSymmetryAxis.setter
    def RotationalSymmetryAxis(self, symmetryAxis: NXOpen.Axis):
        """
        Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) RotationalSymmetryAxis
         Returns the Rotational Symmetry axis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) SecondLimitPlane
    ##  Returns the first second plane for Segmental Rotational Symmetry type    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def SecondLimitPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) SecondLimitPlane
         Returns the first second plane for Segmental Rotational Symmetry type    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) SecondLimitPlane

    ##  Returns the first second plane for Segmental Rotational Symmetry type    
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SecondLimitPlane.setter
    def SecondLimitPlane(self, secondLimitPlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) SecondLimitPlane
         Returns the first second plane for Segmental Rotational Symmetry type    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) SegmentLimitHelpAxis
    ##  Returns the help axis for Segmental Rotational Symmetry    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Axis
    @property
    def SegmentLimitHelpAxis(self) -> NXOpen.Axis:
        """
        Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) SegmentLimitHelpAxis
         Returns the help axis for Segmental Rotational Symmetry    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) SegmentLimitHelpAxis

    ##  Returns the help axis for Segmental Rotational Symmetry    
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SegmentLimitHelpAxis.setter
    def SegmentLimitHelpAxis(self, helpAxis: NXOpen.Axis):
        """
        Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) SegmentLimitHelpAxis
         Returns the help axis for Segmental Rotational Symmetry    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SupportedFaces
    ##  Returns the supported faces for self supporting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SupportedFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SupportedFaces
         Returns the supported faces for self supporting   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ThroughHoleVector
    ##  Returns the Through Hole vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ThroughHoleVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ThroughHoleVector
         Returns the Through Hole vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ThroughHoleVector

    ##  Returns the Through Hole vector   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ThroughHoleVector.setter
    def ThroughHoleVector(self, throughHoleVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ThroughHoleVector
         Returns the Through Hole vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ToolDiameter
    ##  Returns the tool diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ToolDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ToolDiameter
         Returns the tool diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ToolLength
    ##  Returns the tool length   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ToolLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ToolLength
         Returns the tool length   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ToolTipAngle
    ##  Returns the tool tip angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  This is for NX2212 but not used either, do not use this method.  <br> 

    ## @return NXOpen.Expression
    @property
    def ToolTipAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ToolTipAngle
         Returns the tool tip angle   
            
         
        """
        pass
    
    ## Getter for property: (@link ShapeConstraintBuilder.ConstraintType NXOpen.DesignSimulation.ShapeConstraintBuilder.ConstraintType@endlink) Type
    ##  Returns the Constraint type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ShapeConstraintBuilder.ConstraintType
    @property
    def Type(self) -> ShapeConstraintBuilder.ConstraintType:
        """
        Getter for property: (@link ShapeConstraintBuilder.ConstraintType NXOpen.DesignSimulation.ShapeConstraintBuilder.ConstraintType@endlink) Type
         Returns the Constraint type   
            
         
        """
        pass
    
    ## Setter for property: (@link ShapeConstraintBuilder.ConstraintType NXOpen.DesignSimulation.ShapeConstraintBuilder.ConstraintType@endlink) Type

    ##  Returns the Constraint type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Type.setter
    def Type(self, type: ShapeConstraintBuilder.ConstraintType):
        """
        Setter for property: (@link ShapeConstraintBuilder.ConstraintType NXOpen.DesignSimulation.ShapeConstraintBuilder.ConstraintType@endlink) Type
         Returns the Constraint type   
            
         
        """
        pass
    
    ## Getter for property: (bool) UserSetName
    ##  Returns the user set name flag   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the user set name flag   
            
         
        """
        pass
    
    ## Setter for property: (bool) UserSetName

    ##  Returns the user set name flag   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @UserSetName.setter
    def UserSetName(self, userSetName: bool):
        """
        Setter for property: (bool) UserSetName
         Returns the user set name flag   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::DesignSimulation::ShapeConstraint NXOpen::DesignSimulation::ShapeConstraint@endlink  for a @link NXOpen::DesignSimulation::DesignSpace NXOpen::DesignSimulation::DesignSpace@endlink   <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::ShapeConstraintBuilder  NXOpen::DesignSimulation::ShapeConstraintBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ShapeConstraint(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.DesignSimulation.ShapeConstraint</ja_class> for a <ja_class>NXOpen.DesignSimulation.DesignSpace</ja_class> """
    pass


import NXOpen
## 
##     Represents a @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::Features::TopologyOptimizationFeature::CreateStudyBuilder  NXOpen::Features::TopologyOptimizationFeature::CreateStudyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AnalysisType </term> <description> 
##  
## LinearStatics </description> </item> 
## 
## <item><term> 
##  
## OptimizationObjectiveType </term> <description> 
##  
## MaximumStiffness </description> </item> 
## 
## <item><term> 
##  
## ResolutionVoxelSize.Value </term> <description> 
##  
## 1 (millimeters part), 0.04 (inches part) </description> </item> 
## 
## <item><term> 
##  
## StudyQuality </term> <description> 
##  
## 5 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class StudyBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.DesignSimulation.Study</ja_class> builder
    """


    ##  Study Analysis type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## LinearStatics</term><description> 
    ## </description> </item><item><term> 
    ## NormalModes</term><description> 
    ## </description> </item><item><term> 
    ## Thermal</term><description> 
    ## </description> </item></list>
    class AnalysisOption(Enum):
        """
        Members Include: <LinearStatics> <NormalModes> <Thermal>
        """
        LinearStatics: int
        NormalModes: int
        Thermal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StudyBuilder.AnalysisOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Study Optimization Objective type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## MinimumMass</term><description> 
    ## </description> </item><item><term> 
    ## MinimumVolume</term><description> 
    ## </description> </item><item><term> 
    ## MaximumStiffness</term><description> 
    ## </description> </item><item><term> 
    ## MaximumFirstFlexibleMode</term><description> 
    ## </description> </item></list>
    class OptimizationObjectiveOption(Enum):
        """
        Members Include: <MinimumMass> <MinimumVolume> <MaximumStiffness> <MaximumFirstFlexibleMode>
        """
        MinimumMass: int
        MinimumVolume: int
        MaximumStiffness: int
        MaximumFirstFlexibleMode: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StudyBuilder.OptimizationObjectiveOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Subcase Summation for Stiffness Objective
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Maximum</term><description> 
    ## </description> </item><item><term> 
    ## Normalized</term><description> 
    ## </description> </item></list>
    class SubcaseSummationOption(Enum):
        """
        Members Include: <Maximum> <Normalized>
        """
        Maximum: int
        Normalized: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StudyBuilder.SubcaseSummationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link StudyBuilder.AnalysisOption NXOpen.DesignSimulation.StudyBuilder.AnalysisOption@endlink) AnalysisType
    ##  Returns the analysis type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return StudyBuilder.AnalysisOption
    @property
    def AnalysisType(self) -> StudyBuilder.AnalysisOption:
        """
        Getter for property: (@link StudyBuilder.AnalysisOption NXOpen.DesignSimulation.StudyBuilder.AnalysisOption@endlink) AnalysisType
         Returns the analysis type   
            
         
        """
        pass
    
    ## Setter for property: (@link StudyBuilder.AnalysisOption NXOpen.DesignSimulation.StudyBuilder.AnalysisOption@endlink) AnalysisType

    ##  Returns the analysis type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AnalysisType.setter
    def AnalysisType(self, analysisType: StudyBuilder.AnalysisOption):
        """
        Setter for property: (@link StudyBuilder.AnalysisOption NXOpen.DesignSimulation.StudyBuilder.AnalysisOption@endlink) AnalysisType
         Returns the analysis type   
            
         
        """
        pass
    
    ## Getter for property: (bool) FixedVoxelSize
    ##  Returns the control for automatic or user-defined fixed voxel size.  
    ##   
    ##             Set to false to automatically calculate voxel size based on the study quality control and size of selected bodies.
    ##             Set to true to use a user-defined fixed value for voxel size independent of the size of selected bodies.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def FixedVoxelSize(self) -> bool:
        """
        Getter for property: (bool) FixedVoxelSize
         Returns the control for automatic or user-defined fixed voxel size.  
          
                    Set to false to automatically calculate voxel size based on the study quality control and size of selected bodies.
                    Set to true to use a user-defined fixed value for voxel size independent of the size of selected bodies.
                  
         
        """
        pass
    
    ## Setter for property: (bool) FixedVoxelSize

    ##  Returns the control for automatic or user-defined fixed voxel size.  
    ##   
    ##             Set to false to automatically calculate voxel size based on the study quality control and size of selected bodies.
    ##             Set to true to use a user-defined fixed value for voxel size independent of the size of selected bodies.
    ##           
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @FixedVoxelSize.setter
    def FixedVoxelSize(self, isFixed: bool):
        """
        Setter for property: (bool) FixedVoxelSize
         Returns the control for automatic or user-defined fixed voxel size.  
          
                    Set to false to automatically calculate voxel size based on the study quality control and size of selected bodies.
                    Set to true to use a user-defined fixed value for voxel size independent of the size of selected bodies.
                  
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFrequencies
    ##  Returns the number of frequencies.  
    ##    It has range 1 to 100.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def NumberOfFrequencies(self) -> int:
        """
        Getter for property: (int) NumberOfFrequencies
         Returns the number of frequencies.  
           It has range 1 to 100.  
         
        """
        pass
    
    ## Setter for property: (int) NumberOfFrequencies

    ##  Returns the number of frequencies.  
    ##    It has range 1 to 100.  
    ##  
    ## Setter License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @NumberOfFrequencies.setter
    def NumberOfFrequencies(self, numberOfFrequencies: int):
        """
        Setter for property: (int) NumberOfFrequencies
         Returns the number of frequencies.  
           It has range 1 to 100.  
         
        """
        pass
    
    ## Getter for property: (@link StudyBuilder.OptimizationObjectiveOption NXOpen.DesignSimulation.StudyBuilder.OptimizationObjectiveOption@endlink) OptimizationObjectiveType
    ##  Returns the optimization objective type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return StudyBuilder.OptimizationObjectiveOption
    @property
    def OptimizationObjectiveType(self) -> StudyBuilder.OptimizationObjectiveOption:
        """
        Getter for property: (@link StudyBuilder.OptimizationObjectiveOption NXOpen.DesignSimulation.StudyBuilder.OptimizationObjectiveOption@endlink) OptimizationObjectiveType
         Returns the optimization objective type   
            
         
        """
        pass
    
    ## Setter for property: (@link StudyBuilder.OptimizationObjectiveOption NXOpen.DesignSimulation.StudyBuilder.OptimizationObjectiveOption@endlink) OptimizationObjectiveType

    ##  Returns the optimization objective type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @OptimizationObjectiveType.setter
    def OptimizationObjectiveType(self, optimizationObjectiveType: StudyBuilder.OptimizationObjectiveOption):
        """
        Setter for property: (@link StudyBuilder.OptimizationObjectiveOption NXOpen.DesignSimulation.StudyBuilder.OptimizationObjectiveOption@endlink) OptimizationObjectiveType
         Returns the optimization objective type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ResolutionVoxelSize
    ##  Returns the resolution voxel size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ResolutionVoxelSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ResolutionVoxelSize
         Returns the resolution voxel size   
            
         
        """
        pass
    
    ## Getter for property: (str) StudyName
    ##  Returns the study name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def StudyName(self) -> str:
        """
        Getter for property: (str) StudyName
         Returns the study name   
            
         
        """
        pass
    
    ## Setter for property: (str) StudyName

    ##  Returns the study name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @StudyName.setter
    def StudyName(self, studyName: str):
        """
        Setter for property: (str) StudyName
         Returns the study name   
            
         
        """
        pass
    
    ## Getter for property: (int) StudyQuality
    ##  Returns the study quality.  
    ##    It has range 1 to 9. 
    ##             value 1 means high quality but could take long time to get ultra fine optimization result;
    ##             value 9 means low quality and get coarse optimization result.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def StudyQuality(self) -> int:
        """
        Getter for property: (int) StudyQuality
         Returns the study quality.  
           It has range 1 to 9. 
                    value 1 means high quality but could take long time to get ultra fine optimization result;
                    value 9 means low quality and get coarse optimization result.
                  
         
        """
        pass
    
    ## Setter for property: (int) StudyQuality

    ##  Returns the study quality.  
    ##    It has range 1 to 9. 
    ##             value 1 means high quality but could take long time to get ultra fine optimization result;
    ##             value 9 means low quality and get coarse optimization result.
    ##           
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @StudyQuality.setter
    def StudyQuality(self, studyQualityFactor: int):
        """
        Setter for property: (int) StudyQuality
         Returns the study quality.  
           It has range 1 to 9. 
                    value 1 means high quality but could take long time to get ultra fine optimization result;
                    value 9 means low quality and get coarse optimization result.
                  
         
        """
        pass
    
    ## Getter for property: (@link StudyBuilder.SubcaseSummationOption NXOpen.DesignSimulation.StudyBuilder.SubcaseSummationOption@endlink) SubcaseSummationType
    ##  Returns the subcase summation type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return StudyBuilder.SubcaseSummationOption
    @property
    def SubcaseSummationType(self) -> StudyBuilder.SubcaseSummationOption:
        """
        Getter for property: (@link StudyBuilder.SubcaseSummationOption NXOpen.DesignSimulation.StudyBuilder.SubcaseSummationOption@endlink) SubcaseSummationType
         Returns the subcase summation type   
            
         
        """
        pass
    
    ## Setter for property: (@link StudyBuilder.SubcaseSummationOption NXOpen.DesignSimulation.StudyBuilder.SubcaseSummationOption@endlink) SubcaseSummationType

    ##  Returns the subcase summation type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SubcaseSummationType.setter
    def SubcaseSummationType(self, subcaseSummationType: StudyBuilder.SubcaseSummationOption):
        """
        Setter for property: (@link StudyBuilder.SubcaseSummationOption NXOpen.DesignSimulation.StudyBuilder.SubcaseSummationOption@endlink) SubcaseSummationType
         Returns the subcase summation type   
            
         
        """
        pass
    
    ##  Set resolution voxel size by the given study quality (on a scale of 1 - 9) 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use @link NXOpen::DesignSimulation::StudyBuilder::SetStudyQuality NXOpen::DesignSimulation::StudyBuilder::SetStudyQuality@endlink  instead.  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="studyQualityFactor"> (int) </param>
    def SetResolutionVoxelSizeByStudyQuality(self, studyQualityFactor: int) -> None:
        """
         Set resolution voxel size by the given study quality (on a scale of 1 - 9) 
        """
        pass
    
import NXOpen
##  Represents a Design Simulation Study  <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::StudyBuilder  NXOpen::DesignSimulation::StudyBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Study(Container): 
    """ Represents a Design Simulation Study """


    ## Getter for property: (bool) Active
    ##  Returns the active state.  
    ##    There should be only one active Study per @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink 
    ##             and only one active @link NXOpen::GeometricAnalysis::PerformancePredictor NXOpen::GeometricAnalysis::PerformancePredictor@endlink  Study per part.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def Active(self) -> bool:
        """
        Getter for property: (bool) Active
         Returns the active state.  
           There should be only one active Study per @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink 
                    and only one active @link NXOpen::GeometricAnalysis::PerformancePredictor NXOpen::GeometricAnalysis::PerformancePredictor@endlink  Study per part.   
         
        """
        pass
    
    ## Getter for property: (@link AnalysisReportSettings NXOpen.DesignSimulation.AnalysisReportSettings@endlink) AnalysisReportSettings
    ##  Returns the Analysis Report Settings to be used when publishing a report for this study.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return AnalysisReportSettings
    @property
    def AnalysisReportSettings(self) -> AnalysisReportSettings:
        """
        Getter for property: (@link AnalysisReportSettings NXOpen.DesignSimulation.AnalysisReportSettings@endlink) AnalysisReportSettings
         Returns the Analysis Report Settings to be used when publishing a report for this study.  
             
         
        """
        pass
    
    ## Getter for property: (@link StudyBuilder.AnalysisOption NXOpen.DesignSimulation.StudyBuilder.AnalysisOption@endlink) AnalysisType
    ##  Returns the analysis type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return StudyBuilder.AnalysisOption
    @property
    def AnalysisType(self) -> StudyBuilder.AnalysisOption:
        """
        Getter for property: (@link StudyBuilder.AnalysisOption NXOpen.DesignSimulation.StudyBuilder.AnalysisOption@endlink) AnalysisType
         Returns the analysis type   
            
         
        """
        pass
    
    ## Setter for property: (@link StudyBuilder.AnalysisOption NXOpen.DesignSimulation.StudyBuilder.AnalysisOption@endlink) AnalysisType

    ##  Returns the analysis type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AnalysisType.setter
    def AnalysisType(self, type: StudyBuilder.AnalysisOption):
        """
        Setter for property: (@link StudyBuilder.AnalysisOption NXOpen.DesignSimulation.StudyBuilder.AnalysisOption@endlink) AnalysisType
         Returns the analysis type   
            
         
        """
        pass
    
    ## Getter for property: (str) AnalysisTypeDesc
    ##  Returns the analysis type description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def AnalysisTypeDesc(self) -> str:
        """
        Getter for property: (str) AnalysisTypeDesc
         Returns the analysis type description   
            
         
        """
        pass
    
    ## Getter for property: (bool) AutoInferVoxelResolution
    ##  Returns the control for automatic or user-defined voxel resolution.  
    ##   
    ##             Set to TRUE to automatically calculate voxel size based on the study quality control and size of selected bodies.
    ##             Set to FALSE to use a user-defined fixed resolution value for voxel size independent of the size of selected bodies.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def AutoInferVoxelResolution(self) -> bool:
        """
        Getter for property: (bool) AutoInferVoxelResolution
         Returns the control for automatic or user-defined voxel resolution.  
          
                    Set to TRUE to automatically calculate voxel size based on the study quality control and size of selected bodies.
                    Set to FALSE to use a user-defined fixed resolution value for voxel size independent of the size of selected bodies.
                  
         
        """
        pass
    
    ## Setter for property: (bool) AutoInferVoxelResolution

    ##  Returns the control for automatic or user-defined voxel resolution.  
    ##   
    ##             Set to TRUE to automatically calculate voxel size based on the study quality control and size of selected bodies.
    ##             Set to FALSE to use a user-defined fixed resolution value for voxel size independent of the size of selected bodies.
    ##           
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AutoInferVoxelResolution.setter
    def AutoInferVoxelResolution(self, isAutoInferred: bool):
        """
        Setter for property: (bool) AutoInferVoxelResolution
         Returns the control for automatic or user-defined voxel resolution.  
          
                    Set to TRUE to automatically calculate voxel size based on the study quality control and size of selected bodies.
                    Set to FALSE to use a user-defined fixed resolution value for voxel size independent of the size of selected bodies.
                  
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFrequencies
    ##  Returns the number of frequencies.  
    ##    It has range 1 to 100.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def NumberOfFrequencies(self) -> int:
        """
        Getter for property: (int) NumberOfFrequencies
         Returns the number of frequencies.  
           It has range 1 to 100.  
         
        """
        pass
    
    ## Getter for property: (@link StudyBuilder.OptimizationObjectiveOption NXOpen.DesignSimulation.StudyBuilder.OptimizationObjectiveOption@endlink) OptimizationObjective
    ##  Returns the optimization objective type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return StudyBuilder.OptimizationObjectiveOption
    @property
    def OptimizationObjective(self) -> StudyBuilder.OptimizationObjectiveOption:
        """
        Getter for property: (@link StudyBuilder.OptimizationObjectiveOption NXOpen.DesignSimulation.StudyBuilder.OptimizationObjectiveOption@endlink) OptimizationObjective
         Returns the optimization objective type   
            
         
        """
        pass
    
    ## Setter for property: (@link StudyBuilder.OptimizationObjectiveOption NXOpen.DesignSimulation.StudyBuilder.OptimizationObjectiveOption@endlink) OptimizationObjective

    ##  Returns the optimization objective type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @OptimizationObjective.setter
    def OptimizationObjective(self, objective: StudyBuilder.OptimizationObjectiveOption):
        """
        Setter for property: (@link StudyBuilder.OptimizationObjectiveOption NXOpen.DesignSimulation.StudyBuilder.OptimizationObjectiveOption@endlink) OptimizationObjective
         Returns the optimization objective type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ResolutionVoxelSize
    ##  Returns the voxel size (resolution); editing the expression value will make @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  results out of date until the analysis or optimization operation is rerun.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ResolutionVoxelSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ResolutionVoxelSize
         Returns the voxel size (resolution); editing the expression value will make @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  results out of date until the analysis or optimization operation is rerun.  
             
         
        """
        pass
    
    ## Getter for property: (int) StudyQuality
    ##  Returns the study quality or the solution balance factor.  
    ##    The value ranges from 1, for High Accuracy, to 9, for High Performance.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def StudyQuality(self) -> int:
        """
        Getter for property: (int) StudyQuality
         Returns the study quality or the solution balance factor.  
           The value ranges from 1, for High Accuracy, to 9, for High Performance.   
         
        """
        pass
    
    ## Getter for property: (@link StudyBuilder.SubcaseSummationOption NXOpen.DesignSimulation.StudyBuilder.SubcaseSummationOption@endlink) SubcaseSummation
    ##  Returns the subcase summation type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return StudyBuilder.SubcaseSummationOption
    @property
    def SubcaseSummation(self) -> StudyBuilder.SubcaseSummationOption:
        """
        Getter for property: (@link StudyBuilder.SubcaseSummationOption NXOpen.DesignSimulation.StudyBuilder.SubcaseSummationOption@endlink) SubcaseSummation
         Returns the subcase summation type   
            
         
        """
        pass
    
    ## Setter for property: (@link StudyBuilder.SubcaseSummationOption NXOpen.DesignSimulation.StudyBuilder.SubcaseSummationOption@endlink) SubcaseSummation

    ##  Returns the subcase summation type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SubcaseSummation.setter
    def SubcaseSummation(self, subcaseSummation: StudyBuilder.SubcaseSummationOption):
        """
        Setter for property: (@link StudyBuilder.SubcaseSummationOption NXOpen.DesignSimulation.StudyBuilder.SubcaseSummationOption@endlink) SubcaseSummation
         Returns the subcase summation type   
            
         
        """
        pass
    
    ##  Terminates the optimization process, if any, for this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  after it was launched using
    ##             @link NXOpen::DesignSimulation::Study::RunOptimization NXOpen::DesignSimulation::Study::RunOptimization@endlink  and before the process completes or errors out. Calling this method
    ##             does not guarantee that the optimization process will indeed terminate; process state is subject to its progress, hardware and software resources,
    ##             the real time elapsed since it was launched, and other factors. Returns TRUE if the process was previously running and indeed stopped by this method.
    ##             Aborting the optimization will NOT produce partial results and the optimization cannot be resumed (restarted) after being terminated.
    ##         
    ##  @return wasAborted (bool): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def AbortOptimizationProcess(self) -> bool:
        """
         Terminates the optimization process, if any, for this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  after it was launched using
                    @link NXOpen::DesignSimulation::Study::RunOptimization NXOpen::DesignSimulation::Study::RunOptimization@endlink  and before the process completes or errors out. Calling this method
                    does not guarantee that the optimization process will indeed terminate; process state is subject to its progress, hardware and software resources,
                    the real time elapsed since it was launched, and other factors. Returns TRUE if the process was previously running and indeed stopped by this method.
                    Aborting the optimization will NOT produce partial results and the optimization cannot be resumed (restarted) after being terminated.
                
         @return wasAborted (bool): .
        """
        pass
    
    ##  Clones (copies) a @link NXOpen::DesignSimulation::AnalysisConstraint NXOpen::DesignSimulation::AnalysisConstraint@endlink  object and returns the cloned (copied) object if successful. 
    ##  @return clonedConstraint (@link AnalysisConstraint NXOpen.DesignSimulation.AnalysisConstraint@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="existingConstraint"> (@link AnalysisConstraint NXOpen.DesignSimulation.AnalysisConstraint@endlink) </param>
    def CloneAnalysisConstraint(self, existingConstraint: AnalysisConstraint) -> AnalysisConstraint:
        """
         Clones (copies) a @link NXOpen::DesignSimulation::AnalysisConstraint NXOpen::DesignSimulation::AnalysisConstraint@endlink  object and returns the cloned (copied) object if successful. 
         @return clonedConstraint (@link AnalysisConstraint NXOpen.DesignSimulation.AnalysisConstraint@endlink): .
        """
        pass
    
    ##  Clones (copies) a @link NXOpen::DesignSimulation::AnalysisLoad NXOpen::DesignSimulation::AnalysisLoad@endlink  object and returns the cloned (copied) object if successful. 
    ##  @return clonedLoad (@link AnalysisLoad NXOpen.DesignSimulation.AnalysisLoad@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="existingload"> (@link AnalysisLoad NXOpen.DesignSimulation.AnalysisLoad@endlink) </param>
    def CloneAnalysisLoad(self, existingload: AnalysisLoad) -> AnalysisLoad:
        """
         Clones (copies) a @link NXOpen::DesignSimulation::AnalysisLoad NXOpen::DesignSimulation::AnalysisLoad@endlink  object and returns the cloned (copied) object if successful. 
         @return clonedLoad (@link AnalysisLoad NXOpen.DesignSimulation.AnalysisLoad@endlink): .
        """
        pass
    
    ##  Clones (copies) a @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink  object and returns the cloned (copied) object if successful. 
    ##  @return clonedStudy (@link Subcase NXOpen.DesignSimulation.Subcase@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="existingSubcase"> (@link Subcase NXOpen.DesignSimulation.Subcase@endlink) </param>
    def CloneSubcase(self, existingSubcase: Subcase) -> Subcase:
        """
         Clones (copies) a @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink  object and returns the cloned (copied) object if successful. 
         @return clonedStudy (@link Subcase NXOpen.DesignSimulation.Subcase@endlink): .
        """
        pass
    
    ##  Resumes the Topology Optimization process, if any, for this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  after it was suspended (paused) using
    ##             @link NXOpen::DesignSimulation::Study::PauseOptimizationProcess NXOpen::DesignSimulation::Study::PauseOptimizationProcess@endlink  and before the process completes or errors out. Returns TRUE if the process was
    ##             previously paused and indeed resumed by this method.
    ##         
    ##  @return wasResumed (bool): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    def ContinueOptimizationProcess(self) -> bool:
        """
         Resumes the Topology Optimization process, if any, for this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  after it was suspended (paused) using
                    @link NXOpen::DesignSimulation::Study::PauseOptimizationProcess NXOpen::DesignSimulation::Study::PauseOptimizationProcess@endlink  and before the process completes or errors out. Returns TRUE if the process was
                    previously paused and indeed resumed by this method.
                
         @return wasResumed (bool): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::AnalysisConstraintBuilder NXOpen::DesignSimulation::AnalysisConstraintBuilder@endlink  
    ##  @return builder (@link AnalysisConstraintBuilder NXOpen.DesignSimulation.AnalysisConstraintBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="constraint"> (@link AnalysisConstraint NXOpen.DesignSimulation.AnalysisConstraint@endlink) </param>
    def CreateAnalysisConstraintBuilder(self, constraint: AnalysisConstraint) -> AnalysisConstraintBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::AnalysisConstraintBuilder NXOpen::DesignSimulation::AnalysisConstraintBuilder@endlink  
         @return builder (@link AnalysisConstraintBuilder NXOpen.DesignSimulation.AnalysisConstraintBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::AnalysisLoadBuilder NXOpen::DesignSimulation::AnalysisLoadBuilder@endlink  
    ##  @return builder (@link AnalysisLoadBuilder NXOpen.DesignSimulation.AnalysisLoadBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="load"> (@link AnalysisLoad NXOpen.DesignSimulation.AnalysisLoad@endlink) </param>
    def CreateAnalysisLoadBuilder(self, load: AnalysisLoad) -> AnalysisLoadBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::AnalysisLoadBuilder NXOpen::DesignSimulation::AnalysisLoadBuilder@endlink  
         @return builder (@link AnalysisLoadBuilder NXOpen.DesignSimulation.AnalysisLoadBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::AnalysisReportBuilder NXOpen::DesignSimulation::AnalysisReportBuilder@endlink . 
    ##  @return reportBuilder (@link AnalysisReportBuilder NXOpen.DesignSimulation.AnalysisReportBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def CreateAnalysisReportBuilder(self) -> AnalysisReportBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::AnalysisReportBuilder NXOpen::DesignSimulation::AnalysisReportBuilder@endlink . 
         @return reportBuilder (@link AnalysisReportBuilder NXOpen.DesignSimulation.AnalysisReportBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::Connection NXOpen::DesignSimulation::Connection@endlink  
    ##  @return builder (@link ConnectionBuilder NXOpen.DesignSimulation.ConnectionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="connection"> (@link Connection NXOpen.DesignSimulation.Connection@endlink) </param>
    def CreateConnectionBuilder(self, connection: Connection) -> ConnectionBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::Connection NXOpen::DesignSimulation::Connection@endlink  
         @return builder (@link ConnectionBuilder NXOpen.DesignSimulation.ConnectionBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::ConstructionBodyBuilder NXOpen::DesignSimulation::ConstructionBodyBuilder@endlink  that can be used to create one or more @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  objects,
    ##         a single @link NXOpen::DesignSimulation::ConstructionBodyCollector NXOpen::DesignSimulation::ConstructionBodyCollector@endlink  object, or to edit a single @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  object. 
    ##  @return builder (@link ConstructionBodyBuilder NXOpen.DesignSimulation.ConstructionBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="topOptConstructionBody"> (@link ConstructionBody NXOpen.DesignSimulation.ConstructionBody@endlink) </param>
    def CreateConstructionBodyBuilder(self, topOptConstructionBody: ConstructionBody) -> ConstructionBodyBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::ConstructionBodyBuilder NXOpen::DesignSimulation::ConstructionBodyBuilder@endlink  that can be used to create one or more @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  objects,
                a single @link NXOpen::DesignSimulation::ConstructionBodyCollector NXOpen::DesignSimulation::ConstructionBodyCollector@endlink  object, or to edit a single @link NXOpen::DesignSimulation::ConstructionBody NXOpen::DesignSimulation::ConstructionBody@endlink  object. 
         @return builder (@link ConstructionBodyBuilder NXOpen.DesignSimulation.ConstructionBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::ConstructionBodyBuilder NXOpen::DesignSimulation::ConstructionBodyBuilder@endlink  that can be used to edit a single @link NXOpen::DesignSimulation::ConstructionBodyByFaces NXOpen::DesignSimulation::ConstructionBodyByFaces@endlink  object. 
    ##  @return builder (@link ConstructionBodyBuilder NXOpen.DesignSimulation.ConstructionBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="constrBodyByFaces"> (@link ConstructionBodyByFaces NXOpen.DesignSimulation.ConstructionBodyByFaces@endlink) </param>
    def CreateConstructionBodyByFacesBuilder(self, constrBodyByFaces: ConstructionBodyByFaces) -> ConstructionBodyBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::ConstructionBodyBuilder NXOpen::DesignSimulation::ConstructionBodyBuilder@endlink  that can be used to edit a single @link NXOpen::DesignSimulation::ConstructionBodyByFaces NXOpen::DesignSimulation::ConstructionBodyByFaces@endlink  object. 
         @return builder (@link ConstructionBodyBuilder NXOpen.DesignSimulation.ConstructionBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::ConstructionBodyBuilder NXOpen::DesignSimulation::ConstructionBodyBuilder@endlink  that can be used to edit a single @link NXOpen::DesignSimulation::ConstructionBodyCollector NXOpen::DesignSimulation::ConstructionBodyCollector@endlink  object. 
    ##  @return builder (@link ConstructionBodyBuilder NXOpen.DesignSimulation.ConstructionBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="constrBodyCollector"> (@link ConstructionBodyCollector NXOpen.DesignSimulation.ConstructionBodyCollector@endlink) </param>
    def CreateConstructionBodyCollectorBuilder(self, constrBodyCollector: ConstructionBodyCollector) -> ConstructionBodyBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::ConstructionBodyBuilder NXOpen::DesignSimulation::ConstructionBodyBuilder@endlink  that can be used to edit a single @link NXOpen::DesignSimulation::ConstructionBodyCollector NXOpen::DesignSimulation::ConstructionBodyCollector@endlink  object. 
         @return builder (@link ConstructionBodyBuilder NXOpen.DesignSimulation.ConstructionBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::DesignSpaceBuilder NXOpen::DesignSimulation::DesignSpaceBuilder@endlink  
    ##  @return builder (@link DesignSpaceBuilder NXOpen.DesignSimulation.DesignSpaceBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="designSpace"> (@link DesignSpace NXOpen.DesignSimulation.DesignSpace@endlink) </param>
    def CreateDesignSpaceBuilder(self, designSpace: DesignSpace) -> DesignSpaceBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::DesignSpaceBuilder NXOpen::DesignSimulation::DesignSpaceBuilder@endlink  
         @return builder (@link DesignSpaceBuilder NXOpen.DesignSimulation.DesignSpaceBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::EnvironmentLoadBuilder NXOpen::DesignSimulation::EnvironmentLoadBuilder@endlink  
    ##  @return builder (@link EnvironmentLoadBuilder NXOpen.DesignSimulation.EnvironmentLoadBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def CreateEnvironmentLoadBuilder(self) -> EnvironmentLoadBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::EnvironmentLoadBuilder NXOpen::DesignSimulation::EnvironmentLoadBuilder@endlink  
         @return builder (@link EnvironmentLoadBuilder NXOpen.DesignSimulation.EnvironmentLoadBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::ExportToCaeBuilder NXOpen::DesignSimulation::ExportToCaeBuilder@endlink  
    ##  @return builder (@link ExportToCaeBuilder NXOpen.DesignSimulation.ExportToCaeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    def CreateExportToCaeBuilder(self) -> ExportToCaeBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::ExportToCaeBuilder NXOpen::DesignSimulation::ExportToCaeBuilder@endlink  
         @return builder (@link ExportToCaeBuilder NXOpen.DesignSimulation.ExportToCaeBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::OptimizationConstraintBuilder NXOpen::DesignSimulation::OptimizationConstraintBuilder@endlink  
    ##  @return builder (@link OptimizationConstraintBuilder NXOpen.DesignSimulation.OptimizationConstraintBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="optConstraint"> (@link OptimizationConstraint NXOpen.DesignSimulation.OptimizationConstraint@endlink) </param>
    def CreateOptimizationConstraintBuilder(self, optConstraint: OptimizationConstraint) -> OptimizationConstraintBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::OptimizationConstraintBuilder NXOpen::DesignSimulation::OptimizationConstraintBuilder@endlink  
         @return builder (@link OptimizationConstraintBuilder NXOpen.DesignSimulation.OptimizationConstraintBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::ResultMeasureBuilder NXOpen::DesignSimulation::ResultMeasureBuilder@endlink  
    ##  @return builder (@link ResultMeasureBuilder NXOpen.DesignSimulation.ResultMeasureBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="resultMeasure"> (@link ResultMeasure NXOpen.DesignSimulation.ResultMeasure@endlink) </param>
    def CreateResultMeasureBuilder(self, resultMeasure: ResultMeasure) -> ResultMeasureBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::ResultMeasureBuilder NXOpen::DesignSimulation::ResultMeasureBuilder@endlink  
         @return builder (@link ResultMeasureBuilder NXOpen.DesignSimulation.ResultMeasureBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::SceneryBody NXOpen::DesignSimulation::SceneryBody@endlink  
    ##  @return builder (@link SceneryBodyBuilder NXOpen.DesignSimulation.SceneryBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="topOptSceneryBody"> (@link SceneryBody NXOpen.DesignSimulation.SceneryBody@endlink) </param>
    def CreateSceneryBodyBuilder(self, topOptSceneryBody: SceneryBody) -> SceneryBodyBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::SceneryBody NXOpen::DesignSimulation::SceneryBody@endlink  
         @return builder (@link SceneryBodyBuilder NXOpen.DesignSimulation.SceneryBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::ShapeConstraint NXOpen::DesignSimulation::ShapeConstraint@endlink  
    ##  @return builder (@link ShapeConstraintBuilder NXOpen.DesignSimulation.ShapeConstraintBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="topOptShapeConstraint"> (@link ShapeConstraint NXOpen.DesignSimulation.ShapeConstraint@endlink) </param>
    def CreateShapeConstraintBuilder(self, topOptShapeConstraint: ShapeConstraint) -> ShapeConstraintBuilder:
        """
         Creates a @link NXOpen::DesignSimulation::ShapeConstraint NXOpen::DesignSimulation::ShapeConstraint@endlink  
         @return builder (@link ShapeConstraintBuilder NXOpen.DesignSimulation.ShapeConstraintBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DesignSimulation::SubcaseManager NXOpen::DesignSimulation::SubcaseManager@endlink  
    ##  @return builder (@link SubcaseManager NXOpen.DesignSimulation.SubcaseManager@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def CreateSubcaseManager(self) -> SubcaseManager:
        """
         Creates a @link NXOpen::DesignSimulation::SubcaseManager NXOpen::DesignSimulation::SubcaseManager@endlink  
         @return builder (@link SubcaseManager NXOpen.DesignSimulation.SubcaseManager@endlink): .
        """
        pass
    
    ##  Discards optimization results and the optimized bodies for this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  if the topology optimization was previous executed. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def DiscardOptimizationResults(self) -> None:
        """
         Discards optimization results and the optimized bodies for this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  if the topology optimization was previous executed. 
        """
        pass
    
    ##  Delete optimization results from a completed optimization process instead of loading them into this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink .
    ##             This method follows @link NXOpen::DesignSimulation::Study::RunOptimization NXOpen::DesignSimulation::Study::RunOptimization@endlink  and will wait for topology optimization process to complete.
    ##             Use @link NXOpen::DesignSimulation::Study::AbortOptimizationProcess NXOpen::DesignSimulation::Study::AbortOptimizationProcess@endlink  to terminate a running optimization process and delete in-process results.
    ##             The owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  should be active (i.e. not suppressed) before calling this method.
    ##         
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def DiscardUnretrievedOptimizationResults(self) -> None:
        """
         Delete optimization results from a completed optimization process instead of loading them into this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink .
                    This method follows @link NXOpen::DesignSimulation::Study::RunOptimization NXOpen::DesignSimulation::Study::RunOptimization@endlink  and will wait for topology optimization process to complete.
                    Use @link NXOpen::DesignSimulation::Study::AbortOptimizationProcess NXOpen::DesignSimulation::Study::AbortOptimizationProcess@endlink  to terminate a running optimization process and delete in-process results.
                    The owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  should be active (i.e. not suppressed) before calling this method.
                
        """
        pass
    
    ##  Stops and finishes the optimization process for this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  after it was launched using
    ##             @link NXOpen::DesignSimulation::Study::RunOptimization NXOpen::DesignSimulation::Study::RunOptimization@endlink  and before the optimization has converged or completed.
    ##             The optimization process will attempt to produce partial results before terminating. The optimization cannot be resumed (restarted) after
    ##             it has been stopped and optimization results have been loaded. Calling this method does not guarantee that the optimization process will
    ##             produce partial results or that the optimization results will comply with optimization and shape constraints or even meet quality expectations.
    ##             Returns TRUE if the process was previously running and stopped by this method to produce partial results.
    ##         
    ##  @return finished (bool): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    def FinishOptimizationProcess(self) -> bool:
        """
         Stops and finishes the optimization process for this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  after it was launched using
                    @link NXOpen::DesignSimulation::Study::RunOptimization NXOpen::DesignSimulation::Study::RunOptimization@endlink  and before the optimization has converged or completed.
                    The optimization process will attempt to produce partial results before terminating. The optimization cannot be resumed (restarted) after
                    it has been stopped and optimization results have been loaded. Calling this method does not guarantee that the optimization process will
                    produce partial results or that the optimization results will comply with optimization and shape constraints or even meet quality expectations.
                    Returns TRUE if the process was previously running and stopped by this method to produce partial results.
                
         @return finished (bool): .
        """
        pass
    
    ##  Gets all @link NXOpen::DesignSimulation::AnalysisBody NXOpen::DesignSimulation::AnalysisBody@endlink  objects from a @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
    ##             These are @link NXOpen::DesignSimulation::DesignSpace NXOpen::DesignSimulation::DesignSpace@endlink  and @link NXOpen::DesignSimulation::SceneryBody NXOpen::DesignSimulation::SceneryBody@endlink  which are
    ##             directly referenced by the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
    ##  @return bodies (@link AnalysisBody List[NXOpen.DesignSimulation.AnalysisBody]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetAllAnalysisBodies(self) -> List[AnalysisBody]:
        """
         Gets all @link NXOpen::DesignSimulation::AnalysisBody NXOpen::DesignSimulation::AnalysisBody@endlink  objects from a @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
                    These are @link NXOpen::DesignSimulation::DesignSpace NXOpen::DesignSimulation::DesignSpace@endlink  and @link NXOpen::DesignSimulation::SceneryBody NXOpen::DesignSimulation::SceneryBody@endlink  which are
                    directly referenced by the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
         @return bodies (@link AnalysisBody List[NXOpen.DesignSimulation.AnalysisBody]@endlink): .
        """
        pass
    
    ##  Gets all @link NXOpen::DesignSimulation::AnalysisConstraint NXOpen::DesignSimulation::AnalysisConstraint@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
    ##  @return analysisConstraints (@link AnalysisConstraint List[NXOpen.DesignSimulation.AnalysisConstraint]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetAllAnalysisConstraints(self) -> List[AnalysisConstraint]:
        """
         Gets all @link NXOpen::DesignSimulation::AnalysisConstraint NXOpen::DesignSimulation::AnalysisConstraint@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
         @return analysisConstraints (@link AnalysisConstraint List[NXOpen.DesignSimulation.AnalysisConstraint]@endlink): .
        """
        pass
    
    ##  Gets all @link NXOpen::DesignSimulation::AnalysisLoad NXOpen::DesignSimulation::AnalysisLoad@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
    ##  @return analysisLoads (@link AnalysisLoad List[NXOpen.DesignSimulation.AnalysisLoad]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetAllAnalysisLoads(self) -> List[AnalysisLoad]:
        """
         Gets all @link NXOpen::DesignSimulation::AnalysisLoad NXOpen::DesignSimulation::AnalysisLoad@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
         @return analysisLoads (@link AnalysisLoad List[NXOpen.DesignSimulation.AnalysisLoad]@endlink): .
        """
        pass
    
    ##  Gets all @link NXOpen::DesignSimulation::Connection NXOpen::DesignSimulation::Connection@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
    ##  @return topOptConnections (@link Connection List[NXOpen.DesignSimulation.Connection]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetAllConnections(self) -> List[Connection]:
        """
         Gets all @link NXOpen::DesignSimulation::Connection NXOpen::DesignSimulation::Connection@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
         @return topOptConnections (@link Connection List[NXOpen.DesignSimulation.Connection]@endlink): .
        """
        pass
    
    ##  Gets all @link NXOpen::DesignSimulation::DesignSpace NXOpen::DesignSimulation::DesignSpace@endlink  objects from the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
    ##  @return designSpaces (@link DesignSpace List[NXOpen.DesignSimulation.DesignSpace]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetAllDesignSpaces(self) -> List[DesignSpace]:
        """
         Gets all @link NXOpen::DesignSimulation::DesignSpace NXOpen::DesignSimulation::DesignSpace@endlink  objects from the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
         @return designSpaces (@link DesignSpace List[NXOpen.DesignSimulation.DesignSpace]@endlink): .
        """
        pass
    
    ##  Gets all environment load objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink .
    ##             @link NXOpen::DesignSimulation::Acceleration NXOpen::DesignSimulation::Acceleration@endlink  as Gravity is the only environment load currently. 
    ##  @return loads (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetAllEnvironmentLoads(self) -> List[NXOpen.NXObject]:
        """
         Gets all environment load objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink .
                    @link NXOpen::DesignSimulation::Acceleration NXOpen::DesignSimulation::Acceleration@endlink  as Gravity is the only environment load currently. 
         @return loads (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  Gets all @link NXOpen::DesignSimulation::OptimizationConstraint NXOpen::DesignSimulation::OptimizationConstraint@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
    ##  @return optimizationConstraints (@link OptimizationConstraint List[NXOpen.DesignSimulation.OptimizationConstraint]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetAllOptimizationConstraints(self) -> List[OptimizationConstraint]:
        """
         Gets all @link NXOpen::DesignSimulation::OptimizationConstraint NXOpen::DesignSimulation::OptimizationConstraint@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
         @return optimizationConstraints (@link OptimizationConstraint List[NXOpen.DesignSimulation.OptimizationConstraint]@endlink): .
        """
        pass
    
    ##  Gets all @link NXOpen::DesignSimulation::ResultMeasure NXOpen::DesignSimulation::ResultMeasure@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
    ##  @return resultMeasures (@link ResultMeasure List[NXOpen.DesignSimulation.ResultMeasure]@endlink): .
    ## 
    ##   <br>  Created in NX2306.3000.0  <br> 

    ## License requirements: None.
    def GetAllResultMeasures(self) -> List[ResultMeasure]:
        """
         Gets all @link NXOpen::DesignSimulation::ResultMeasure NXOpen::DesignSimulation::ResultMeasure@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
         @return resultMeasures (@link ResultMeasure List[NXOpen.DesignSimulation.ResultMeasure]@endlink): .
        """
        pass
    
    ##  Gets all @link NXOpen::DesignSimulation::SceneryBody NXOpen::DesignSimulation::SceneryBody@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink .. 
    ##  @return topOptSceneryBodies (@link SceneryBody List[NXOpen.DesignSimulation.SceneryBody]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetAllSceneryBodies(self) -> List[SceneryBody]:
        """
         Gets all @link NXOpen::DesignSimulation::SceneryBody NXOpen::DesignSimulation::SceneryBody@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink .. 
         @return topOptSceneryBodies (@link SceneryBody List[NXOpen.DesignSimulation.SceneryBody]@endlink): .
        """
        pass
    
    ##  Gets all @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
    ##  @return subcases (@link Subcase List[NXOpen.DesignSimulation.Subcase]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetAllSubcases(self) -> List[Subcase]:
        """
         Gets all @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink  objects from the given @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . 
         @return subcases (@link Subcase List[NXOpen.DesignSimulation.Subcase]@endlink): .
        """
        pass
    
    ##  Get optimized bodies for this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  
    ##  @return bodies (@link NXOpen.Body List[NXOpen.Body]@endlink):  the optimized bodies .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetOptimizedBodies(self) -> List[NXOpen.Body]:
        """
         Get optimized bodies for this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  
         @return bodies (@link NXOpen.Body List[NXOpen.Body]@endlink):  the optimized bodies .
        """
        pass
    
    ##  Suspends (pauses) the Topology Optimization process, if any, for this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  after it was launched using
    ##             @link NXOpen::DesignSimulation::Study::RunOptimization NXOpen::DesignSimulation::Study::RunOptimization@endlink  and before the process completes or errors out. Calling this method does not guarantee that the
    ##             optimization process will indeed be suspended; process state is subject to its progress, hardware and software resources, the real time elapsed since it was launched,
    ##             and other factors. The optimization process can be resumed (restarted) using @link NXOpen::DesignSimulation::Study::ContinueOptimizationProcess NXOpen::DesignSimulation::Study::ContinueOptimizationProcess@endlink .
    ##         
    ##  @return wasPaused (bool): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    def PauseOptimizationProcess(self) -> bool:
        """
         Suspends (pauses) the Topology Optimization process, if any, for this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  after it was launched using
                    @link NXOpen::DesignSimulation::Study::RunOptimization NXOpen::DesignSimulation::Study::RunOptimization@endlink  and before the process completes or errors out. Calling this method does not guarantee that the
                    optimization process will indeed be suspended; process state is subject to its progress, hardware and software resources, the real time elapsed since it was launched,
                    and other factors. The optimization process can be resumed (restarted) using @link NXOpen::DesignSimulation::Study::ContinueOptimizationProcess NXOpen::DesignSimulation::Study::ContinueOptimizationProcess@endlink .
                
         @return wasPaused (bool): .
        """
        pass
    
    ##  Remove the analysis results from this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . Optimized bodies, if applicable, will be kept. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def RemoveAnalysisResults(self) -> None:
        """
         Remove the analysis results from this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink . Optimized bodies, if applicable, will be kept. 
        """
        pass
    
    ##  Loads results and the optimized bodies from the optimization into this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  when the process has completed. 
    ##             This method follows @link NXOpen::DesignSimulation::Study::RunOptimization NXOpen::DesignSimulation::Study::RunOptimization@endlink  and will wait for topology optimization process to complete.
    ##             The owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  should be active (i.e. not suppressed) before calling this method.
    ##         
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def RetrieveOptimizationResults(self) -> None:
        """
         Loads results and the optimized bodies from the optimization into this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  when the process has completed. 
                    This method follows @link NXOpen::DesignSimulation::Study::RunOptimization NXOpen::DesignSimulation::Study::RunOptimization@endlink  and will wait for topology optimization process to complete.
                    The owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  should be active (i.e. not suppressed) before calling this method.
                
        """
        pass
    
    ##  Analyzes this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  if the Performance Predictor analysis is fully setup and ready to analyze.
    ##             The analysis can be executed independent of the owning @link NXOpen::GeometricAnalysis::AnalysisObject NXOpen::GeometricAnalysis::AnalysisObject@endlink  state. The owning
    ##             @link NXOpen::GeometricAnalysis::AnalysisObject NXOpen::GeometricAnalysis::AnalysisObject@endlink  could be inactive or delayed for update. This method completes all stages
    ##             of the CAE analysis in the foreground, i.e. control returns to call only after CAE analysis is done.
    ##         
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    def RunAnalysis(self) -> None:
        """
         Analyzes this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  if the Performance Predictor analysis is fully setup and ready to analyze.
                    The analysis can be executed independent of the owning @link NXOpen::GeometricAnalysis::AnalysisObject NXOpen::GeometricAnalysis::AnalysisObject@endlink  state. The owning
                    @link NXOpen::GeometricAnalysis::AnalysisObject NXOpen::GeometricAnalysis::AnalysisObject@endlink  could be inactive or delayed for update. This method completes all stages
                    of the CAE analysis in the foreground, i.e. control returns to call only after CAE analysis is done.
                
        """
        pass
    
    ##  Optimizes (solves) this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  if the optimization is fully setup and ready to optimize.
    ##             The optimization (solve) can be executed independent of the owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  state.
    ##             The owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  could be suppressed or delayed for update.
    ## 
    ##             This method will return aftering pre-processing and launching the optimization process to run independent of the NX session. In other words, the
    ##             method will not wait for the topology optimization process to complete.
    ## 
    ##             Optimization results from the solve need to be loaded into the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  object by calling
    ##             @link NXOpen::DesignSimulation::Study::RetrieveOptimizationResults NXOpen::DesignSimulation::Study::RetrieveOptimizationResults@endlink .
    ##         
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def RunOptimization(self) -> None:
        """
         Optimizes (solves) this @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  if the optimization is fully setup and ready to optimize.
                    The optimization (solve) can be executed independent of the owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  state.
                    The owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  could be suppressed or delayed for update.
        
                    This method will return aftering pre-processing and launching the optimization process to run independent of the NX session. In other words, the
                    method will not wait for the topology optimization process to complete.
        
                    Optimization results from the solve need to be loaded into the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  object by calling
                    @link NXOpen::DesignSimulation::Study::RetrieveOptimizationResults NXOpen::DesignSimulation::Study::RetrieveOptimizationResults@endlink .
                
        """
        pass
    
    ##  Unlocks the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  if it is read-only. This method can be used to make a @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink 
    ##             editable if optimization results could not be loaded due to errors or due to missing data. Use @link NXOpen::DesignSimulation::Study::AbortOptimizationProcess NXOpen::DesignSimulation::Study::AbortOptimizationProcess@endlink  to
    ##             terminate a running optimization process or @link NXOpen::DesignSimulation::Study::DiscardUnretrievedOptimizationResults NXOpen::DesignSimulation::Study::DiscardUnretrievedOptimizationResults@endlink  to delete results instead of loading them.
    ##             The owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  should be active (i.e. not suppressed) before calling this method.
    ##         
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    def Unlock(self) -> None:
        """
         Unlocks the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  if it is read-only. This method can be used to make a @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink 
                    editable if optimization results could not be loaded due to errors or due to missing data. Use @link NXOpen::DesignSimulation::Study::AbortOptimizationProcess NXOpen::DesignSimulation::Study::AbortOptimizationProcess@endlink  to
                    terminate a running optimization process or @link NXOpen::DesignSimulation::Study::DiscardUnretrievedOptimizationResults NXOpen::DesignSimulation::Study::DiscardUnretrievedOptimizationResults@endlink  to delete results instead of loading them.
                    The owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  should be active (i.e. not suppressed) before calling this method.
                
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class SubcaseItemList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##  Returns the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SubcaseItemList NXOpen.DesignSimulation.SubcaseItemList@endlink) </param>
    ## <param name="objects"> (@link SubcaseItem List[NXOpen.DesignSimulation.SubcaseItem]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[SubcaseItem]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SubcaseItemList NXOpen.DesignSimulation.SubcaseItemList@endlink) </param>
    ## <param name="objectValue"> (@link SubcaseItem NXOpen.DesignSimulation.SubcaseItem@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: SubcaseItem) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SubcaseItemList NXOpen.DesignSimulation.SubcaseItemList@endlink) </param>
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="delete_idx"> (int)  index of item to be deleted </param>
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SubcaseItemList NXOpen.DesignSimulation.SubcaseItemList@endlink) </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the objects when removing them </param>
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SubcaseItemList NXOpen.DesignSimulation.SubcaseItemList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SubcaseItemList NXOpen.DesignSimulation.SubcaseItemList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SubcaseItemList NXOpen.DesignSimulation.SubcaseItemList@endlink) </param>
    ## <param name="obj"> (@link SubcaseItem NXOpen.DesignSimulation.SubcaseItem@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: SubcaseItem) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SubcaseItemList NXOpen.DesignSimulation.SubcaseItemList@endlink) </param>
    ## <param name="obj"> (@link SubcaseItem NXOpen.DesignSimulation.SubcaseItem@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: SubcaseItem, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="obj"> (@link SubcaseItem NXOpen.DesignSimulation.SubcaseItem@endlink)  Object to find index for </param>
    def FindIndex(self, obj: SubcaseItem) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link SubcaseItem NXOpen.DesignSimulation.SubcaseItem@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> SubcaseItem:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link SubcaseItem NXOpen.DesignSimulation.SubcaseItem@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link SubcaseItem List[NXOpen.DesignSimulation.SubcaseItem]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[SubcaseItem]:
        """
         Gets the contents of the entire list 
         @return objects (@link SubcaseItem List[NXOpen.DesignSimulation.SubcaseItem]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link SubcaseItem NXOpen.DesignSimulation.SubcaseItem@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: SubcaseItem) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link SubcaseItem List[NXOpen.DesignSimulation.SubcaseItem]@endlink)  The list contents </param>
    def SetContents(self, objects: List[SubcaseItem]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SubcaseItemList NXOpen.DesignSimulation.SubcaseItemList@endlink) </param>
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SubcaseItemList NXOpen.DesignSimulation.SubcaseItemList@endlink) </param>
    ## <param name="object1"> (@link SubcaseItem NXOpen.DesignSimulation.SubcaseItem@endlink)  first item </param>
    ## <param name="object2"> (@link SubcaseItem NXOpen.DesignSimulation.SubcaseItem@endlink)  second item </param>
    @overload
    def Swap(self, object1: SubcaseItem, object2: SubcaseItem) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::DesignSimulation::SubcaseItem NXOpen::DesignSimulation::SubcaseItem@endlink  list item
##      <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::SubcaseManager::CreateSubcase  NXOpen::DesignSimulation::SubcaseManager::CreateSubcase @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SubcaseItem(NXOpen.TaggedObject): 
    """
    Represents a <ja_class>NXOpen.DesignSimulation.SubcaseItem</ja_class> list item
    """


    ##  Subcase object type definitions 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Load</term><description> 
    ## </description> </item><item><term> 
    ## Constraint</term><description> 
    ## </description> </item></list>
    class ItemType(Enum):
        """
        Members Include: <Load> <Constraint>
        """
        Load: int
        Constraint: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubcaseItem.ItemType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) IncludedInOptimization
    ##  Returns the flag indicating whether a subcase is included in Optimization   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def IncludedInOptimization(self) -> bool:
        """
        Getter for property: (bool) IncludedInOptimization
         Returns the flag indicating whether a subcase is included in Optimization   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludedInOptimization

    ##  Returns the flag indicating whether a subcase is included in Optimization   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @IncludedInOptimization.setter
    def IncludedInOptimization(self, includedInOptimization: bool):
        """
        Setter for property: (bool) IncludedInOptimization
         Returns the flag indicating whether a subcase is included in Optimization   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the current subcase name   
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
         Returns the current subcase name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the current subcase name   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the current subcase name   
            
         
        """
        pass
    
    ##  Enable a Load/constraint
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ## <param name="reference"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def AddReference(self, reference: NXOpen.NXObject) -> None:
        """
         Enable a Load/constraint
        """
        pass
    
    ##  Disable a Load/constraint
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ## <param name="reference"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def RemoveReference(self, reference: NXOpen.NXObject) -> None:
        """
         Disable a Load/constraint
        """
        pass
    
import NXOpen
## 
##     A class which defines the Subcase Manager for Topology Optimization
##      <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::Study::CreateSubcaseManager  NXOpen::DesignSimulation::Study::CreateSubcaseManager @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SubcaseManager(NXOpen.Builder): 
    """
    A class which defines the Subcase Manager for Topology Optimization
    """


    ## Getter for property: (@link SubcaseItemList NXOpen.DesignSimulation.SubcaseItemList@endlink) SubcaseList
    ##  Returns a list of subcases in a specific Topology Optimization Study   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return SubcaseItemList
    @property
    def SubcaseList(self) -> SubcaseItemList:
        """
        Getter for property: (@link SubcaseItemList NXOpen.DesignSimulation.SubcaseItemList@endlink) SubcaseList
         Returns a list of subcases in a specific Topology Optimization Study   
            
         
        """
        pass
    
    ##  Creates a Subcase item builder
    ##  @return item (@link SubcaseItem NXOpen.DesignSimulation.SubcaseItem@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    def CreateSubcase(self) -> SubcaseItem:
        """
         Creates a Subcase item builder
         @return item (@link SubcaseItem NXOpen.DesignSimulation.SubcaseItem@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Design Simulation Subcase  <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::SubcaseManager  NXOpen::DesignSimulation::SubcaseManager @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Subcase(Container): 
    """ Represents a Design Simulation Subcase """


    ##  Subcase use for Optimization 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## TrueValue</term><description> 
    ## </description> </item><item><term> 
    ## FalseValue</term><description> 
    ## </description> </item></list>
    class IncludeInOptimization(Enum):
        """
        Members Include: <TrueValue> <FalseValue>
        """
        TrueValue: int
        FalseValue: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Subcase.IncludeInOptimization:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link Subcase.IncludeInOptimization NXOpen.DesignSimulation.Subcase.IncludeInOptimization@endlink) IsIncludedInOptimization
    ##  Returns the Included in optimization flag  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return Subcase.IncludeInOptimization
    @property
    def IsIncludedInOptimization(self) -> Subcase.IncludeInOptimization:
        """
        Getter for property: (@link Subcase.IncludeInOptimization NXOpen.DesignSimulation.Subcase.IncludeInOptimization@endlink) IsIncludedInOptimization
         Returns the Included in optimization flag  
            
         
        """
        pass
    
    ## Setter for property: (@link Subcase.IncludeInOptimization NXOpen.DesignSimulation.Subcase.IncludeInOptimization@endlink) IsIncludedInOptimization

    ##  Returns the Included in optimization flag  
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @IsIncludedInOptimization.setter
    def IsIncludedInOptimization(self, isIncludedInOptimization: Subcase.IncludeInOptimization):
        """
        Setter for property: (@link Subcase.IncludeInOptimization NXOpen.DesignSimulation.Subcase.IncludeInOptimization@endlink) IsIncludedInOptimization
         Returns the Included in optimization flag  
            
         
        """
        pass
    
    ## Add reference to a @link NXOpen::DesignSimulation::AnalysisLoad NXOpen::DesignSimulation::AnalysisLoad@endlink  or @link NXOpen::DesignSimulation::AnalysisConstraint NXOpen::DesignSimulation::AnalysisConstraint@endlink  to the @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ## <param name="reference"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def AddReference(self, reference: NXOpen.NXObject) -> None:
        """
        Add reference to a @link NXOpen::DesignSimulation::AnalysisLoad NXOpen::DesignSimulation::AnalysisLoad@endlink  or @link NXOpen::DesignSimulation::AnalysisConstraint NXOpen::DesignSimulation::AnalysisConstraint@endlink  to the @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink .
        """
        pass
    
    ##  Get all @link NXOpen::DesignSimulation::AnalysisLoad NXOpen::DesignSimulation::AnalysisLoad@endlink  or @link NXOpen::DesignSimulation::AnalysisConstraint NXOpen::DesignSimulation::AnalysisConstraint@endlink  in this @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink .
    ##  @return references (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING") OR features_modeling ("FEATURES MODELING")
    def GetReferences(self) -> List[NXOpen.NXObject]:
        """
         Get all @link NXOpen::DesignSimulation::AnalysisLoad NXOpen::DesignSimulation::AnalysisLoad@endlink  or @link NXOpen::DesignSimulation::AnalysisConstraint NXOpen::DesignSimulation::AnalysisConstraint@endlink  in this @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink .
         @return references (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ## Remove a @link NXOpen::DesignSimulation::AnalysisLoad NXOpen::DesignSimulation::AnalysisLoad@endlink  or @link NXOpen::DesignSimulation::AnalysisConstraint NXOpen::DesignSimulation::AnalysisConstraint@endlink  from the @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ## <param name="reference"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def RemoveReference(self, reference: NXOpen.NXObject) -> None:
        """
        Remove a @link NXOpen::DesignSimulation::AnalysisLoad NXOpen::DesignSimulation::AnalysisLoad@endlink  or @link NXOpen::DesignSimulation::AnalysisConstraint NXOpen::DesignSimulation::AnalysisConstraint@endlink  from the @link NXOpen::DesignSimulation::Subcase NXOpen::DesignSimulation::Subcase@endlink .
        """
        pass
    
import NXOpen
##  Represents an Temperature type constraint in the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  context.  <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::EnvironmentLoadBuilder  NXOpen::DesignSimulation::EnvironmentLoadBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class Temperature(NXOpen.NXObject): 
    """ Represents an Temperature type constraint in the <ja_class>NXOpen.DesignSimulation.Study</ja_class> context. """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ReferenceTemperature
    ##  Returns the ambient temperature magnitude   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ReferenceTemperature(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ReferenceTemperature
         Returns the ambient temperature magnitude   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a builder to specify contour display settings and plot contours according to the settings
##      <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::PostManager::CreateViewContourBuilder  NXOpen::DesignSimulation::PostManager::CreateViewContourBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ViewContourBuilder(NXOpen.Builder): 
    """
    Represents a builder to specify contour display settings and plot contours according to the settings
    """


    ##  Color style option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Default</term><description> 
    ## </description> </item><item><term> 
    ## Spotlight</term><description> 
    ## </description> </item><item><term> 
    ## MaterialLimit</term><description> 
    ## </description> </item></list>
    class ColorDisplayStyleOption(Enum):
        """
        Members Include: <Default> <Spotlight> <MaterialLimit>
        """
        Default: int
        Spotlight: int
        MaterialLimit: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ViewContourBuilder.ColorDisplayStyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Color scale range option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## PerView</term><description> 
    ## </description> </item><item><term> 
    ## CommonAcrossViews</term><description> 
    ## </description> </item></list>
    class ColorScaleRangeOption(Enum):
        """
        Members Include: <PerView> <CommonAcrossViews>
        """
        PerView: int
        CommonAcrossViews: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ViewContourBuilder.ColorScaleRangeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Contour display style option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Smooth</term><description> 
    ## </description> </item><item><term> 
    ## Banded</term><description> 
    ## </description> </item></list>
    class ContourDisplayStyleOption(Enum):
        """
        Members Include: <Smooth> <Banded>
        """
        Smooth: int
        Banded: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ViewContourBuilder.ContourDisplayStyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Display type option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Single</term><description> 
    ## </description> </item><item><term> 
    ## Comparison</term><description> 
    ## </description> </item></list>
    class DisplayOption(Enum):
        """
        Members Include: <Single> <Comparison>
        """
        Single: int
        Comparison: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ViewContourBuilder.DisplayOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Material option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AnalysisBody</term><description> 
    ## </description> </item><item><term> 
    ## Material</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item></list>
    class MaterialLimitOption(Enum):
        """
        Members Include: <AnalysisBody> <Material> <UserDefined>
        """
        AnalysisBody: int
        Material: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ViewContourBuilder.MaterialLimitOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Result type and component type option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## DisplacementMagnitude</term><description> 
    ## </description> </item><item><term> 
    ## DisplacementWorstInXYZ</term><description> 
    ## </description> </item><item><term> 
    ## DisplacementX</term><description> 
    ## </description> </item><item><term> 
    ## DisplacementY</term><description> 
    ## </description> </item><item><term> 
    ## DisplacementZ</term><description> 
    ## </description> </item><item><term> 
    ## DisplacementAll</term><description> 
    ##  Displacement All includes Worst in XYZ, X, Y and Z</description> </item><item><term> 
    ## StressVonMises</term><description> 
    ## </description> </item><item><term> 
    ## StressWorstPrincipal</term><description> 
    ## </description> </item><item><term> 
    ## SafetyFactor</term><description> 
    ## </description> </item></list>
    class ResultComponentOption(Enum):
        """
        Members Include: <DisplacementMagnitude> <DisplacementWorstInXYZ> <DisplacementX> <DisplacementY> <DisplacementZ> <DisplacementAll> <StressVonMises> <StressWorstPrincipal> <SafetyFactor>
        """
        DisplacementMagnitude: int
        DisplacementWorstInXYZ: int
        DisplacementX: int
        DisplacementY: int
        DisplacementZ: int
        DisplacementAll: int
        StressVonMises: int
        StressWorstPrincipal: int
        SafetyFactor: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ViewContourBuilder.ResultComponentOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ViewContourBuilder.ColorDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ColorDisplayStyleOption@endlink) ColorDisplayStyle
    ##  Returns the color display style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ViewContourBuilder.ColorDisplayStyleOption
    @property
    def ColorDisplayStyle(self) -> ViewContourBuilder.ColorDisplayStyleOption:
        """
        Getter for property: (@link ViewContourBuilder.ColorDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ColorDisplayStyleOption@endlink) ColorDisplayStyle
         Returns the color display style   
            
         
        """
        pass
    
    ## Setter for property: (@link ViewContourBuilder.ColorDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ColorDisplayStyleOption@endlink) ColorDisplayStyle

    ##  Returns the color display style   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ColorDisplayStyle.setter
    def ColorDisplayStyle(self, colorDisplayStyle: ViewContourBuilder.ColorDisplayStyleOption):
        """
        Setter for property: (@link ViewContourBuilder.ColorDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ColorDisplayStyleOption@endlink) ColorDisplayStyle
         Returns the color display style   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewContourBuilder.ColorScaleRangeOption NXOpen.DesignSimulation.ViewContourBuilder.ColorScaleRangeOption@endlink) ColorScaleRangeType
    ##  Returns the color scale range type.  
    ##    This option is only available for multiple contours display like comparison report, single report with specified
    ##         @link  DesignSimulation::ViewContourBuilder::ResultComponentOption::DisplacementAll   DesignSimulation::ViewContourBuilder::ResultComponentOption::DisplacementAll @endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ViewContourBuilder.ColorScaleRangeOption
    @property
    def ColorScaleRangeType(self) -> ViewContourBuilder.ColorScaleRangeOption:
        """
        Getter for property: (@link ViewContourBuilder.ColorScaleRangeOption NXOpen.DesignSimulation.ViewContourBuilder.ColorScaleRangeOption@endlink) ColorScaleRangeType
         Returns the color scale range type.  
           This option is only available for multiple contours display like comparison report, single report with specified
                @link  DesignSimulation::ViewContourBuilder::ResultComponentOption::DisplacementAll   DesignSimulation::ViewContourBuilder::ResultComponentOption::DisplacementAll @endlink    
         
        """
        pass
    
    ## Setter for property: (@link ViewContourBuilder.ColorScaleRangeOption NXOpen.DesignSimulation.ViewContourBuilder.ColorScaleRangeOption@endlink) ColorScaleRangeType

    ##  Returns the color scale range type.  
    ##    This option is only available for multiple contours display like comparison report, single report with specified
    ##         @link  DesignSimulation::ViewContourBuilder::ResultComponentOption::DisplacementAll   DesignSimulation::ViewContourBuilder::ResultComponentOption::DisplacementAll @endlink    
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ColorScaleRangeType.setter
    def ColorScaleRangeType(self, colorScaleRangeOption: ViewContourBuilder.ColorScaleRangeOption):
        """
        Setter for property: (@link ViewContourBuilder.ColorScaleRangeOption NXOpen.DesignSimulation.ViewContourBuilder.ColorScaleRangeOption@endlink) ColorScaleRangeType
         Returns the color scale range type.  
           This option is only available for multiple contours display like comparison report, single report with specified
                @link  DesignSimulation::ViewContourBuilder::ResultComponentOption::DisplacementAll   DesignSimulation::ViewContourBuilder::ResultComponentOption::DisplacementAll @endlink    
         
        """
        pass
    
    ## Getter for property: (@link ViewContourBuilder.ContourDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ContourDisplayStyleOption@endlink) ContourDisplayStyle
    ##  Returns the contour display style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ViewContourBuilder.ContourDisplayStyleOption
    @property
    def ContourDisplayStyle(self) -> ViewContourBuilder.ContourDisplayStyleOption:
        """
        Getter for property: (@link ViewContourBuilder.ContourDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ContourDisplayStyleOption@endlink) ContourDisplayStyle
         Returns the contour display style   
            
         
        """
        pass
    
    ## Setter for property: (@link ViewContourBuilder.ContourDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ContourDisplayStyleOption@endlink) ContourDisplayStyle

    ##  Returns the contour display style   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ContourDisplayStyle.setter
    def ContourDisplayStyle(self, contourDisplayStyle: ViewContourBuilder.ContourDisplayStyleOption):
        """
        Setter for property: (@link ViewContourBuilder.ContourDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ContourDisplayStyleOption@endlink) ContourDisplayStyle
         Returns the contour display style   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewContourBuilder.DisplayOption NXOpen.DesignSimulation.ViewContourBuilder.DisplayOption@endlink) DisplayType
    ##  Returns the display type choice   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ViewContourBuilder.DisplayOption
    @property
    def DisplayType(self) -> ViewContourBuilder.DisplayOption:
        """
        Getter for property: (@link ViewContourBuilder.DisplayOption NXOpen.DesignSimulation.ViewContourBuilder.DisplayOption@endlink) DisplayType
         Returns the display type choice   
            
         
        """
        pass
    
    ## Setter for property: (@link ViewContourBuilder.DisplayOption NXOpen.DesignSimulation.ViewContourBuilder.DisplayOption@endlink) DisplayType

    ##  Returns the display type choice   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DisplayType.setter
    def DisplayType(self, displayType: ViewContourBuilder.DisplayOption):
        """
        Setter for property: (@link ViewContourBuilder.DisplayOption NXOpen.DesignSimulation.ViewContourBuilder.DisplayOption@endlink) DisplayType
         Returns the display type choice   
            
         
        """
        pass
    
    ## Getter for property: (@link Study NXOpen.DesignSimulation.Study@endlink) FirstStudy
    ##  Returns the first study choice   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return Study
    @property
    def FirstStudy(self) -> Study:
        """
        Getter for property: (@link Study NXOpen.DesignSimulation.Study@endlink) FirstStudy
         Returns the first study choice   
            
         
        """
        pass
    
    ## Setter for property: (@link Study NXOpen.DesignSimulation.Study@endlink) FirstStudy

    ##  Returns the first study choice   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @FirstStudy.setter
    def FirstStudy(self, study: Study):
        """
        Setter for property: (@link Study NXOpen.DesignSimulation.Study@endlink) FirstStudy
         Returns the first study choice   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
    ##  Returns the Material used when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material   DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material @endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Material
    @property
    def Material(self) -> NXOpen.Material:
        """
        Getter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
         Returns the Material used when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material   DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material @endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material

    ##  Returns the Material used when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material   DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material @endlink    
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Material.setter
    def Material(self, assignedMaterial: NXOpen.Material):
        """
        Setter for property: (@link NXOpen.Material NXOpen.Material@endlink) Material
         Returns the Material used when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material   DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material @endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link ViewContourBuilder.MaterialLimitOption NXOpen.DesignSimulation.ViewContourBuilder.MaterialLimitOption@endlink) MaterialLimit
    ##  Returns the Material Limit Option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ViewContourBuilder.MaterialLimitOption
    @property
    def MaterialLimit(self) -> ViewContourBuilder.MaterialLimitOption:
        """
        Getter for property: (@link ViewContourBuilder.MaterialLimitOption NXOpen.DesignSimulation.ViewContourBuilder.MaterialLimitOption@endlink) MaterialLimit
         Returns the Material Limit Option   
            
         
        """
        pass
    
    ## Setter for property: (@link ViewContourBuilder.MaterialLimitOption NXOpen.DesignSimulation.ViewContourBuilder.MaterialLimitOption@endlink) MaterialLimit

    ##  Returns the Material Limit Option   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MaterialLimit.setter
    def MaterialLimit(self, materialLimitOption: ViewContourBuilder.MaterialLimitOption):
        """
        Setter for property: (@link ViewContourBuilder.MaterialLimitOption NXOpen.DesignSimulation.ViewContourBuilder.MaterialLimitOption@endlink) MaterialLimit
         Returns the Material Limit Option   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisBody NXOpen.DesignSimulation.AnalysisBody@endlink) MaterialLimitBody
    ##  Returns the Analysis Body used when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody   DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody @endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return AnalysisBody
    @property
    def MaterialLimitBody(self) -> AnalysisBody:
        """
        Getter for property: (@link AnalysisBody NXOpen.DesignSimulation.AnalysisBody@endlink) MaterialLimitBody
         Returns the Analysis Body used when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody   DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody @endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisBody NXOpen.DesignSimulation.AnalysisBody@endlink) MaterialLimitBody

    ##  Returns the Analysis Body used when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody   DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody @endlink    
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MaterialLimitBody.setter
    def MaterialLimitBody(self, body: AnalysisBody):
        """
        Setter for property: (@link AnalysisBody NXOpen.DesignSimulation.AnalysisBody@endlink) MaterialLimitBody
         Returns the Analysis Body used when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody   DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody @endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxStressCompression
    ##  Returns the Max Stress Compression expression used for Stress Worst Principal when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined   DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined @endlink    
    ##     
    ##  
    ## Getter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxStressCompression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxStressCompression
         Returns the Max Stress Compression expression used for Stress Worst Principal when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined   DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined @endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxStressTension
    ##  Returns the Max Stress Tension expression used for Stress Worst Principal when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined   DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined @endlink    
    ##     
    ##  
    ## Getter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxStressTension(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxStressTension
         Returns the Max Stress Tension expression used for Stress Worst Principal when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined   DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined @endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link ViewContourBuilder.ResultComponentOption NXOpen.DesignSimulation.ViewContourBuilder.ResultComponentOption@endlink) ResultComponentType
    ##  Returns the result component type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ViewContourBuilder.ResultComponentOption
    @property
    def ResultComponentType(self) -> ViewContourBuilder.ResultComponentOption:
        """
        Getter for property: (@link ViewContourBuilder.ResultComponentOption NXOpen.DesignSimulation.ViewContourBuilder.ResultComponentOption@endlink) ResultComponentType
         Returns the result component type   
            
         
        """
        pass
    
    ## Setter for property: (@link ViewContourBuilder.ResultComponentOption NXOpen.DesignSimulation.ViewContourBuilder.ResultComponentOption@endlink) ResultComponentType

    ##  Returns the result component type   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ResultComponentType.setter
    def ResultComponentType(self, resultComponentType: ViewContourBuilder.ResultComponentOption):
        """
        Setter for property: (@link ViewContourBuilder.ResultComponentOption NXOpen.DesignSimulation.ViewContourBuilder.ResultComponentOption@endlink) ResultComponentType
         Returns the result component type   
            
         
        """
        pass
    
    ## Getter for property: (@link Study NXOpen.DesignSimulation.Study@endlink) SecondStudy
    ##  Returns the second study choice, this choice is available for study comparison case   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return Study
    @property
    def SecondStudy(self) -> Study:
        """
        Getter for property: (@link Study NXOpen.DesignSimulation.Study@endlink) SecondStudy
         Returns the second study choice, this choice is available for study comparison case   
            
         
        """
        pass
    
    ## Setter for property: (@link Study NXOpen.DesignSimulation.Study@endlink) SecondStudy

    ##  Returns the second study choice, this choice is available for study comparison case   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SecondStudy.setter
    def SecondStudy(self, study: Study):
        """
        Setter for property: (@link Study NXOpen.DesignSimulation.Study@endlink) SecondStudy
         Returns the second study choice, this choice is available for study comparison case   
            
         
        """
        pass
    
    ## Getter for property: (int) SubcaseIndexForFirstStudy
    ##  Returns the subcase index for first study choice   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def SubcaseIndexForFirstStudy(self) -> int:
        """
        Getter for property: (int) SubcaseIndexForFirstStudy
         Returns the subcase index for first study choice   
            
         
        """
        pass
    
    ## Setter for property: (int) SubcaseIndexForFirstStudy

    ##  Returns the subcase index for first study choice   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SubcaseIndexForFirstStudy.setter
    def SubcaseIndexForFirstStudy(self, subcaseIndexForFirstStudy: int):
        """
        Setter for property: (int) SubcaseIndexForFirstStudy
         Returns the subcase index for first study choice   
            
         
        """
        pass
    
    ## Getter for property: (int) SubcaseIndexForSecondStudy
    ##  Returns the subcase index for second study choice, this choice is available for study comparison case   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def SubcaseIndexForSecondStudy(self) -> int:
        """
        Getter for property: (int) SubcaseIndexForSecondStudy
         Returns the subcase index for second study choice, this choice is available for study comparison case   
            
         
        """
        pass
    
    ## Setter for property: (int) SubcaseIndexForSecondStudy

    ##  Returns the subcase index for second study choice, this choice is available for study comparison case   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SubcaseIndexForSecondStudy.setter
    def SubcaseIndexForSecondStudy(self, subcaseIndexForSecondStudy: int):
        """
        Setter for property: (int) SubcaseIndexForSecondStudy
         Returns the subcase index for second study choice, this choice is available for study comparison case   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YieldStrength
    ##  Returns the Yield Strength expression used for Stress Von Mises when Material Limit is set as
    ##         @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined   DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined @endlink    
    ##     
    ##  
    ## Getter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") OR nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YieldStrength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YieldStrength
         Returns the Yield Strength expression used for Stress Von Mises when Material Limit is set as
                @link  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined   DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined @endlink    
            
         
        """
        pass
    
import NXOpen
##  Represents a builder for creating viewport settings for the analysis report settings used to publish an analysis report. <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::AnalysisReportBuilder::CreateViewportSettingsBuilder  NXOpen::DesignSimulation::AnalysisReportBuilder::CreateViewportSettingsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class ViewportSettingsBuilder(ContourSettingsBuilder): 
    """ Represents a builder for creating viewport settings for the analysis report settings used to publish an analysis report."""


    ## Getter for property: (str) Id
    ##  Returns the Viewport Settings Id that uniquely identifies the object in the context of its parent.  
    ##   
    ##             The report writer replaces the text tags having the Viewport Settings Id with an image
    ##             capturing a contour result created with the Viewport Settings attribute: 
    ##             Result Component, Contour Style, Color Style, etc.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the Viewport Settings Id that uniquely identifies the object in the context of its parent.  
          
                    The report writer replaces the text tags having the Viewport Settings Id with an image
                    capturing a contour result created with the Viewport Settings attribute: 
                    Result Component, Contour Style, Color Style, etc.   
         
        """
        pass
    
    ## Setter for property: (str) Id

    ##  Returns the Viewport Settings Id that uniquely identifies the object in the context of its parent.  
    ##   
    ##             The report writer replaces the text tags having the Viewport Settings Id with an image
    ##             capturing a contour result created with the Viewport Settings attribute: 
    ##             Result Component, Contour Style, Color Style, etc.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @Id.setter
    def Id(self, id: str):
        """
        Setter for property: (str) Id
         Returns the Viewport Settings Id that uniquely identifies the object in the context of its parent.  
          
                    The report writer replaces the text tags having the Viewport Settings Id with an image
                    capturing a contour result created with the Viewport Settings attribute: 
                    Result Component, Contour Style, Color Style, etc.   
         
        """
        pass
    
    ## Getter for property: (bool) IsAnimatedGif
    ##  Returns the animated GIF flag  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def IsAnimatedGif(self) -> bool:
        """
        Getter for property: (bool) IsAnimatedGif
         Returns the animated GIF flag  
            
         
        """
        pass
    
    ## Setter for property: (bool) IsAnimatedGif

    ##  Returns the animated GIF flag  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @IsAnimatedGif.setter
    def IsAnimatedGif(self, isAnimatedGif: bool):
        """
        Setter for property: (bool) IsAnimatedGif
         Returns the animated GIF flag  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ModelingView NXOpen.ModelingView@endlink) ModelingView
    ##  Returns the Modeling View  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.ModelingView
    @property
    def ModelingView(self) -> NXOpen.ModelingView:
        """
        Getter for property: (@link NXOpen.ModelingView NXOpen.ModelingView@endlink) ModelingView
         Returns the Modeling View  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.ModelingView NXOpen.ModelingView@endlink) ModelingView

    ##  Returns the Modeling View  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ModelingView.setter
    def ModelingView(self, modelingView: NXOpen.ModelingView):
        """
        Setter for property: (@link NXOpen.ModelingView NXOpen.ModelingView@endlink) ModelingView
         Returns the Modeling View  
            
         
        """
        pass
    
import NXOpen
##  Represents a Viewport Settings for the Analysis Report Settings used to publish an Analysis Report. <br> To create or edit an instance of this class, use @link NXOpen::DesignSimulation::ViewportSettingsBuilder  NXOpen::DesignSimulation::ViewportSettingsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class ViewportSettings(NXOpen.NXObject): 
    """ Represents a Viewport Settings for the Analysis Report Settings used to publish an Analysis Report."""


    ## Getter for property: (@link ContourSettingsBuilder.ColorStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ColorStyleOption@endlink) ColorStyle
    ##  Returns the color style.  
    ##    This option is for different color schema's for highlighting the results ranges.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return ContourSettingsBuilder.ColorStyleOption
    @property
    def ColorStyle(self) -> ContourSettingsBuilder.ColorStyleOption:
        """
        Getter for property: (@link ContourSettingsBuilder.ColorStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ColorStyleOption@endlink) ColorStyle
         Returns the color style.  
           This option is for different color schema's for highlighting the results ranges.  
         
        """
        pass
    
    ## Getter for property: (@link ContourSettingsBuilder.ComponentTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ComponentTypeOption@endlink) ComponentType
    ##  Returns the component type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return ContourSettingsBuilder.ComponentTypeOption
    @property
    def ComponentType(self) -> ContourSettingsBuilder.ComponentTypeOption:
        """
        Getter for property: (@link ContourSettingsBuilder.ComponentTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ComponentTypeOption@endlink) ComponentType
         Returns the component type   
            
         
        """
        pass
    
    ## Getter for property: (@link ContourSettingsBuilder.ContourStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourStyleOption@endlink) ContourStyle
    ##  Returns the contour style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return ContourSettingsBuilder.ContourStyleOption
    @property
    def ContourStyle(self) -> ContourSettingsBuilder.ContourStyleOption:
        """
        Getter for property: (@link ContourSettingsBuilder.ContourStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourStyleOption@endlink) ContourStyle
         Returns the contour style   
            
         
        """
        pass
    
    ## Getter for property: (int) FrequencyIndex
    ##  Returns the index of the Frequency to display for Natural Frequencies analysis type.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def FrequencyIndex(self) -> int:
        """
        Getter for property: (int) FrequencyIndex
         Returns the index of the Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    
    ## Getter for property: (str) Id
    ##  Returns the Viewport Settings Id that uniquely identifies the object in the context of its parent.  
    ##   
    ##             The report writer replaces the text tags having the Viewport Settings Id with an image
    ##             capturing a contour result created with the Viewport Settings attribute: 
    ##             Result Component, Contour Style, Color Style, etc.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the Viewport Settings Id that uniquely identifies the object in the context of its parent.  
          
                    The report writer replaces the text tags having the Viewport Settings Id with an image
                    capturing a contour result created with the Viewport Settings attribute: 
                    Result Component, Contour Style, Color Style, etc.  
         
        """
        pass
    
    ## Getter for property: (bool) IsAnimatedGif
    ##  Returns the animated GIF flag  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def IsAnimatedGif(self) -> bool:
        """
        Getter for property: (bool) IsAnimatedGif
         Returns the animated GIF flag  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ModelingView NXOpen.ModelingView@endlink) ModelingView
    ##  Returns the Modeling View  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.ModelingView
    @property
    def ModelingView(self) -> NXOpen.ModelingView:
        """
        Getter for property: (@link NXOpen.ModelingView NXOpen.ModelingView@endlink) ModelingView
         Returns the Modeling View  
            
         
        """
        pass
    
    ## Getter for property: (@link ContourSettingsBuilder.ResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption@endlink) ResultType
    ##  Returns the result type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return ContourSettingsBuilder.ResultTypeOption
    @property
    def ResultType(self) -> ContourSettingsBuilder.ResultTypeOption:
        """
        Getter for property: (@link ContourSettingsBuilder.ResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption@endlink) ResultType
         Returns the result type   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a builder to specify tabular result contents and list tabular results according to the contents
##      <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::PostManager::CreateViewTabularResultBuilder  NXOpen::DesignSimulation::PostManager::CreateViewTabularResultBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ViewTabularResultBuilder(NXOpen.Builder): 
    """
    Represents a builder to specify tabular result contents and list tabular results according to the contents
    """


    ##  Report contents option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## OptimizationObjective</term><description> 
    ## </description> </item><item><term> 
    ## OptimizationConstraint</term><description> 
    ## </description> </item><item><term> 
    ## All</term><description> 
    ## </description> </item></list>
    class ReportContentOption(Enum):
        """
        Members Include: <OptimizationObjective> <OptimizationConstraint> <All>
        """
        OptimizationObjective: int
        OptimizationConstraint: int
        All: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ViewTabularResultBuilder.ReportContentOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Bodies
    ##  Returns the selected solid bodies for scenery bodies or design spaces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def Bodies(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Bodies
         Returns the selected solid bodies for scenery bodies or design spaces   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewTabularResultBuilder.ReportContentOption NXOpen.DesignSimulation.ViewTabularResultBuilder.ReportContentOption@endlink) ReportContent
    ##  Returns the report content choice   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ViewTabularResultBuilder.ReportContentOption
    @property
    def ReportContent(self) -> ViewTabularResultBuilder.ReportContentOption:
        """
        Getter for property: (@link ViewTabularResultBuilder.ReportContentOption NXOpen.DesignSimulation.ViewTabularResultBuilder.ReportContentOption@endlink) ReportContent
         Returns the report content choice   
            
         
        """
        pass
    
    ## Setter for property: (@link ViewTabularResultBuilder.ReportContentOption NXOpen.DesignSimulation.ViewTabularResultBuilder.ReportContentOption@endlink) ReportContent

    ##  Returns the report content choice   
    ##     
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ReportContent.setter
    def ReportContent(self, reportContent: ViewTabularResultBuilder.ReportContentOption):
        """
        Setter for property: (@link ViewTabularResultBuilder.ReportContentOption NXOpen.DesignSimulation.ViewTabularResultBuilder.ReportContentOption@endlink) ReportContent
         Returns the report content choice   
            
         
        """
        pass
    
    ##  Gets the selected studies. 
    ##  @return studies (@link Study List[NXOpen.DesignSimulation.Study]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetStudies(self) -> List[Study]:
        """
         Gets the selected studies. 
         @return studies (@link Study List[NXOpen.DesignSimulation.Study]@endlink): .
        """
        pass
    
    ##  Sets the selected studies. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ## <param name="studies"> (@link Study List[NXOpen.DesignSimulation.Study]@endlink) </param>
    def SetStudies(self, studies: List[Study]) -> None:
        """
         Sets the selected studies. 
        """
        pass
    
import NXOpen
## 
##     Represents a builder to draw xygraph for optimization objective or optimization constraint
##      <br> To create a new instance of this class, use @link NXOpen::DesignSimulation::PostManager::CreateViewXygraphBuilder  NXOpen::DesignSimulation::PostManager::CreateViewXygraphBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ViewXygraphBuilder(NXOpen.Builder): 
    """
    Represents a builder to draw xygraph for optimization objective or optimization constraint
    """


    ##  Xygraph content option
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## OptimizationObjective</term><description> 
    ## </description> </item><item><term> 
    ## OptimizationConstraint</term><description> 
    ## </description> </item></list>
    class ContentOption(Enum):
        """
        Members Include: <OptimizationObjective> <OptimizationConstraint>
        """
        OptimizationObjective: int
        OptimizationConstraint: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ViewXygraphBuilder.ContentOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link OptimizationConstraint NXOpen.DesignSimulation.OptimizationConstraint@endlink) OptimizationConstraint
    ##  Returns the optimization constraint.  
    ##   
    ##         
    ##         This property needs to be set when @link NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent@endlink 
    ##         is @link NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint@endlink .
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return OptimizationConstraint
    @property
    def OptimizationConstraint(self) -> OptimizationConstraint:
        """
        Getter for property: (@link OptimizationConstraint NXOpen.DesignSimulation.OptimizationConstraint@endlink) OptimizationConstraint
         Returns the optimization constraint.  
          
                
                This property needs to be set when @link NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent@endlink 
                is @link NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint@endlink .
                
                  
         
        """
        pass
    
    ## Setter for property: (@link OptimizationConstraint NXOpen.DesignSimulation.OptimizationConstraint@endlink) OptimizationConstraint

    ##  Returns the optimization constraint.  
    ##   
    ##         
    ##         This property needs to be set when @link NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent@endlink 
    ##         is @link NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint@endlink .
    ##         
    ##           
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @OptimizationConstraint.setter
    def OptimizationConstraint(self, constraint: OptimizationConstraint):
        """
        Setter for property: (@link OptimizationConstraint NXOpen.DesignSimulation.OptimizationConstraint@endlink) OptimizationConstraint
         Returns the optimization constraint.  
          
                
                This property needs to be set when @link NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent@endlink 
                is @link NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint@endlink .
                
                  
         
        """
        pass
    
    ## Getter for property: (@link Study NXOpen.DesignSimulation.Study@endlink) Study
    ##  Returns the target study.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return Study
    @property
    def Study(self) -> Study:
        """
        Getter for property: (@link Study NXOpen.DesignSimulation.Study@endlink) Study
         Returns the target study.  
             
         
        """
        pass
    
    ## Setter for property: (@link Study NXOpen.DesignSimulation.Study@endlink) Study

    ##  Returns the target study.  
    ##      
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Study.setter
    def Study(self, study: Study):
        """
        Setter for property: (@link Study NXOpen.DesignSimulation.Study@endlink) Study
         Returns the target study.  
             
         
        """
        pass
    
    ## Getter for property: (str) SubcaseName
    ##  Returns the corresponding subcase name for optimization constraint.  
    ##   
    ##         
    ##         This property needs to be set when @link NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent@endlink 
    ##         is @link NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint@endlink .
    ##         For following constraints, their iterative results are independent on subcase, the subcase name should be set as empty.
    ##         <ol>
    ##         <li>
    ##         @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMassTarget NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMassTarget@endlink 
    ##         </li>
    ##         <li>
    ##         @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumMassLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumMassLimit@endlink 
    ##         </li>
    ##         <li>
    ##         @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumMassLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumMassLimit@endlink 
    ##         </li>
    ##         <li>
    ##         @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeFirstFlexibleModeTarget NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeFirstFlexibleModeTarget@endlink 
    ##         </li>
    ##         <li>
    ##         @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumFirstFlexibleModeLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumFirstFlexibleModeLimit@endlink 
    ##         </li>
    ##         <li>
    ##         @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumFirstFlexibleModeLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumFirstFlexibleModeLimit@endlink 
    ##         </li>
    ##         </ol>
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def SubcaseName(self) -> str:
        """
        Getter for property: (str) SubcaseName
         Returns the corresponding subcase name for optimization constraint.  
          
                
                This property needs to be set when @link NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent@endlink 
                is @link NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint@endlink .
                For following constraints, their iterative results are independent on subcase, the subcase name should be set as empty.
                <ol>
                <li>
                @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMassTarget NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMassTarget@endlink 
                </li>
                <li>
                @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumMassLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumMassLimit@endlink 
                </li>
                <li>
                @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumMassLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumMassLimit@endlink 
                </li>
                <li>
                @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeFirstFlexibleModeTarget NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeFirstFlexibleModeTarget@endlink 
                </li>
                <li>
                @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumFirstFlexibleModeLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumFirstFlexibleModeLimit@endlink 
                </li>
                <li>
                @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumFirstFlexibleModeLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumFirstFlexibleModeLimit@endlink 
                </li>
                </ol>
                
                  
         
        """
        pass
    
    ## Setter for property: (str) SubcaseName

    ##  Returns the corresponding subcase name for optimization constraint.  
    ##   
    ##         
    ##         This property needs to be set when @link NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent@endlink 
    ##         is @link NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint@endlink .
    ##         For following constraints, their iterative results are independent on subcase, the subcase name should be set as empty.
    ##         <ol>
    ##         <li>
    ##         @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMassTarget NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMassTarget@endlink 
    ##         </li>
    ##         <li>
    ##         @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumMassLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumMassLimit@endlink 
    ##         </li>
    ##         <li>
    ##         @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumMassLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumMassLimit@endlink 
    ##         </li>
    ##         <li>
    ##         @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeFirstFlexibleModeTarget NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeFirstFlexibleModeTarget@endlink 
    ##         </li>
    ##         <li>
    ##         @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumFirstFlexibleModeLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumFirstFlexibleModeLimit@endlink 
    ##         </li>
    ##         <li>
    ##         @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumFirstFlexibleModeLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumFirstFlexibleModeLimit@endlink 
    ##         </li>
    ##         </ol>
    ##         
    ##           
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SubcaseName.setter
    def SubcaseName(self, subcaseName: str):
        """
        Setter for property: (str) SubcaseName
         Returns the corresponding subcase name for optimization constraint.  
          
                
                This property needs to be set when @link NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent@endlink 
                is @link NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint@endlink .
                For following constraints, their iterative results are independent on subcase, the subcase name should be set as empty.
                <ol>
                <li>
                @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMassTarget NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMassTarget@endlink 
                </li>
                <li>
                @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumMassLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumMassLimit@endlink 
                </li>
                <li>
                @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumMassLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumMassLimit@endlink 
                </li>
                <li>
                @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeFirstFlexibleModeTarget NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeFirstFlexibleModeTarget@endlink 
                </li>
                <li>
                @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumFirstFlexibleModeLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumFirstFlexibleModeLimit@endlink 
                </li>
                <li>
                @link NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumFirstFlexibleModeLimit NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumFirstFlexibleModeLimit@endlink 
                </li>
                </ol>
                
                  
         
        """
        pass
    
    ## Getter for property: (int) TargetWindowDevice
    ##  Returns the ID of target window device on which XY graph is displayed.  
    ##   
    ##         
    ##         The window device ID is returned when calling @link NXOpen::CAE::Xyplot::WindowManager::NewWindow NXOpen::CAE::Xyplot::WindowManager::NewWindow@endlink 
    ##         to create a new graphics window. To get existing window device IDs, call @link NXOpen::CAE::Xyplot::WindowManager::GetWindows NXOpen::CAE::Xyplot::WindowManager::GetWindows@endlink .
    ##         
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def TargetWindowDevice(self) -> int:
        """
        Getter for property: (int) TargetWindowDevice
         Returns the ID of target window device on which XY graph is displayed.  
          
                
                The window device ID is returned when calling @link NXOpen::CAE::Xyplot::WindowManager::NewWindow NXOpen::CAE::Xyplot::WindowManager::NewWindow@endlink 
                to create a new graphics window. To get existing window device IDs, call @link NXOpen::CAE::Xyplot::WindowManager::GetWindows NXOpen::CAE::Xyplot::WindowManager::GetWindows@endlink .
                
                  
         
        """
        pass
    
    ## Setter for property: (int) TargetWindowDevice

    ##  Returns the ID of target window device on which XY graph is displayed.  
    ##   
    ##         
    ##         The window device ID is returned when calling @link NXOpen::CAE::Xyplot::WindowManager::NewWindow NXOpen::CAE::Xyplot::WindowManager::NewWindow@endlink 
    ##         to create a new graphics window. To get existing window device IDs, call @link NXOpen::CAE::Xyplot::WindowManager::GetWindows NXOpen::CAE::Xyplot::WindowManager::GetWindows@endlink .
    ##         
    ##           
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @TargetWindowDevice.setter
    def TargetWindowDevice(self, winDevice: int):
        """
        Setter for property: (int) TargetWindowDevice
         Returns the ID of target window device on which XY graph is displayed.  
          
                
                The window device ID is returned when calling @link NXOpen::CAE::Xyplot::WindowManager::NewWindow NXOpen::CAE::Xyplot::WindowManager::NewWindow@endlink 
                to create a new graphics window. To get existing window device IDs, call @link NXOpen::CAE::Xyplot::WindowManager::GetWindows NXOpen::CAE::Xyplot::WindowManager::GetWindows@endlink .
                
                  
         
        """
        pass
    
    ## Getter for property: (@link ViewXygraphBuilder.ContentOption NXOpen.DesignSimulation.ViewXygraphBuilder.ContentOption@endlink) XygraphContent
    ##  Returns the xygraph content.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ViewXygraphBuilder.ContentOption
    @property
    def XygraphContent(self) -> ViewXygraphBuilder.ContentOption:
        """
        Getter for property: (@link ViewXygraphBuilder.ContentOption NXOpen.DesignSimulation.ViewXygraphBuilder.ContentOption@endlink) XygraphContent
         Returns the xygraph content.  
             
         
        """
        pass
    
    ## Setter for property: (@link ViewXygraphBuilder.ContentOption NXOpen.DesignSimulation.ViewXygraphBuilder.ContentOption@endlink) XygraphContent

    ##  Returns the xygraph content.  
    ##      
    ##  
    ## Setter License requirements: des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @XygraphContent.setter
    def XygraphContent(self, xygraphContent: ViewXygraphBuilder.ContentOption):
        """
        Setter for property: (@link ViewXygraphBuilder.ContentOption NXOpen.DesignSimulation.ViewXygraphBuilder.ContentOption@endlink) XygraphContent
         Returns the xygraph content.  
             
         
        """
        pass
    
## @package NXOpen.DesignSimulation
## Classes, Enums and Structs under NXOpen.DesignSimulation namespace

## @link AnalysisBodyResultsFacet_Struct NXOpen.DesignSimulation.AnalysisBodyResultsFacet_Struct@endlink is an alias for @link AnalysisBodyResults.Facet NXOpen.DesignSimulation.AnalysisBodyResults.Facet@endlink.
AnalysisBodyResultsFacet_Struct = AnalysisBodyResults.Facet


##  @link AnalysisBodySubcaseResultsResultType NXOpen.DesignSimulation.AnalysisBodySubcaseResultsResultType @endlink is an alias for @link AnalysisBodySubcaseResults.ResultType NXOpen.DesignSimulation.AnalysisBodySubcaseResults.ResultType@endlink
AnalysisBodySubcaseResultsResultType = AnalysisBodySubcaseResults.ResultType


##  @link AnalysisConstraintBuilderConstraintType NXOpen.DesignSimulation.AnalysisConstraintBuilderConstraintType @endlink is an alias for @link AnalysisConstraintBuilder.ConstraintType NXOpen.DesignSimulation.AnalysisConstraintBuilder.ConstraintType@endlink
AnalysisConstraintBuilderConstraintType = AnalysisConstraintBuilder.ConstraintType


##  @link AnalysisLoadBuilderAnalysisLoadForceType NXOpen.DesignSimulation.AnalysisLoadBuilderAnalysisLoadForceType @endlink is an alias for @link AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadForceType@endlink
AnalysisLoadBuilderAnalysisLoadForceType = AnalysisLoadBuilder.AnalysisLoadForceType


##  @link AnalysisLoadBuilderAnalysisLoadType NXOpen.DesignSimulation.AnalysisLoadBuilderAnalysisLoadType @endlink is an alias for @link AnalysisLoadBuilder.AnalysisLoadType NXOpen.DesignSimulation.AnalysisLoadBuilder.AnalysisLoadType@endlink
AnalysisLoadBuilderAnalysisLoadType = AnalysisLoadBuilder.AnalysisLoadType


##  @link AnalysisLoadBuilderForceDistributionType NXOpen.DesignSimulation.AnalysisLoadBuilderForceDistributionType @endlink is an alias for @link AnalysisLoadBuilder.ForceDistributionType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceDistributionType@endlink
AnalysisLoadBuilderForceDistributionType = AnalysisLoadBuilder.ForceDistributionType


##  @link AnalysisLoadBuilderForceObjectType NXOpen.DesignSimulation.AnalysisLoadBuilderForceObjectType @endlink is an alias for @link AnalysisLoadBuilder.ForceObjectType NXOpen.DesignSimulation.AnalysisLoadBuilder.ForceObjectType@endlink
AnalysisLoadBuilderForceObjectType = AnalysisLoadBuilder.ForceObjectType


##  @link AnalysisLoadBuilderRemoteForceType NXOpen.DesignSimulation.AnalysisLoadBuilderRemoteForceType @endlink is an alias for @link AnalysisLoadBuilder.RemoteForceType NXOpen.DesignSimulation.AnalysisLoadBuilder.RemoteForceType@endlink
AnalysisLoadBuilderRemoteForceType = AnalysisLoadBuilder.RemoteForceType


##  @link AnalysisReportBuilderImageBackgroundOption NXOpen.DesignSimulation.AnalysisReportBuilderImageBackgroundOption @endlink is an alias for @link AnalysisReportBuilder.ImageBackgroundOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageBackgroundOption@endlink
AnalysisReportBuilderImageBackgroundOption = AnalysisReportBuilder.ImageBackgroundOption


##  @link AnalysisReportBuilderImageSizeOption NXOpen.DesignSimulation.AnalysisReportBuilderImageSizeOption @endlink is an alias for @link AnalysisReportBuilder.ImageSizeOption NXOpen.DesignSimulation.AnalysisReportBuilder.ImageSizeOption@endlink
AnalysisReportBuilderImageSizeOption = AnalysisReportBuilder.ImageSizeOption


##  @link AnalysisReportBuilderSaveBehaviorOption NXOpen.DesignSimulation.AnalysisReportBuilderSaveBehaviorOption @endlink is an alias for @link AnalysisReportBuilder.SaveBehaviorOption NXOpen.DesignSimulation.AnalysisReportBuilder.SaveBehaviorOption@endlink
AnalysisReportBuilderSaveBehaviorOption = AnalysisReportBuilder.SaveBehaviorOption


##  @link AnimationControllerState NXOpen.DesignSimulation.AnimationControllerState @endlink is an alias for @link AnimationController.State NXOpen.DesignSimulation.AnimationController.State@endlink
AnimationControllerState = AnimationController.State


##  @link ConnectionBuilderTypes NXOpen.DesignSimulation.ConnectionBuilderTypes @endlink is an alias for @link ConnectionBuilder.Types NXOpen.DesignSimulation.ConnectionBuilder.Types@endlink
ConnectionBuilderTypes = ConnectionBuilder.Types


##  @link ConstructionBodyBuilderConstructionType NXOpen.DesignSimulation.ConstructionBodyBuilderConstructionType @endlink is an alias for @link ConstructionBodyBuilder.ConstructionType NXOpen.DesignSimulation.ConstructionBodyBuilder.ConstructionType@endlink
ConstructionBodyBuilderConstructionType = ConstructionBodyBuilder.ConstructionType


##  @link ConstructionBodyBuilderGroupingType NXOpen.DesignSimulation.ConstructionBodyBuilderGroupingType @endlink is an alias for @link ConstructionBodyBuilder.GroupingType NXOpen.DesignSimulation.ConstructionBodyBuilder.GroupingType@endlink
ConstructionBodyBuilderGroupingType = ConstructionBodyBuilder.GroupingType


##  @link ConstructionBodyBuilderMethodOption NXOpen.DesignSimulation.ConstructionBodyBuilderMethodOption @endlink is an alias for @link ConstructionBodyBuilder.MethodOption NXOpen.DesignSimulation.ConstructionBodyBuilder.MethodOption@endlink
ConstructionBodyBuilderMethodOption = ConstructionBodyBuilder.MethodOption


##  @link ConstructionBodyBuilderOffsetType NXOpen.DesignSimulation.ConstructionBodyBuilderOffsetType @endlink is an alias for @link ConstructionBodyBuilder.OffsetType NXOpen.DesignSimulation.ConstructionBodyBuilder.OffsetType@endlink
ConstructionBodyBuilderOffsetType = ConstructionBodyBuilder.OffsetType


##  @link ContainerReorderType NXOpen.DesignSimulation.ContainerReorderType @endlink is an alias for @link Container.ReorderType NXOpen.DesignSimulation.Container.ReorderType@endlink
ContainerReorderType = Container.ReorderType


##  @link ContourSettingsBuilderColorStyleOption NXOpen.DesignSimulation.ContourSettingsBuilderColorStyleOption @endlink is an alias for @link ContourSettingsBuilder.ColorStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ColorStyleOption@endlink
ContourSettingsBuilderColorStyleOption = ContourSettingsBuilder.ColorStyleOption


##  @link ContourSettingsBuilderComponentTypeOption NXOpen.DesignSimulation.ContourSettingsBuilderComponentTypeOption @endlink is an alias for @link ContourSettingsBuilder.ComponentTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ComponentTypeOption@endlink
ContourSettingsBuilderComponentTypeOption = ContourSettingsBuilder.ComponentTypeOption


##  @link ContourSettingsBuilderContourLimitOption NXOpen.DesignSimulation.ContourSettingsBuilderContourLimitOption @endlink is an alias for @link ContourSettingsBuilder.ContourLimitOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourLimitOption@endlink
ContourSettingsBuilderContourLimitOption = ContourSettingsBuilder.ContourLimitOption


##  @link ContourSettingsBuilderContourStyleOption NXOpen.DesignSimulation.ContourSettingsBuilderContourStyleOption @endlink is an alias for @link ContourSettingsBuilder.ContourStyleOption NXOpen.DesignSimulation.ContourSettingsBuilder.ContourStyleOption@endlink
ContourSettingsBuilderContourStyleOption = ContourSettingsBuilder.ContourStyleOption


##  @link ContourSettingsBuilderResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilderResultTypeOption @endlink is an alias for @link ContourSettingsBuilder.ResultTypeOption NXOpen.DesignSimulation.ContourSettingsBuilder.ResultTypeOption@endlink
ContourSettingsBuilderResultTypeOption = ContourSettingsBuilder.ResultTypeOption


##  @link ExportToCaeBuilderSolverTypeOption NXOpen.DesignSimulation.ExportToCaeBuilderSolverTypeOption @endlink is an alias for @link ExportToCaeBuilder.SolverTypeOption NXOpen.DesignSimulation.ExportToCaeBuilder.SolverTypeOption@endlink
ExportToCaeBuilderSolverTypeOption = ExportToCaeBuilder.SolverTypeOption


##  @link ExportToCaeBuilderUseBodyOption NXOpen.DesignSimulation.ExportToCaeBuilderUseBodyOption @endlink is an alias for @link ExportToCaeBuilder.UseBodyOption NXOpen.DesignSimulation.ExportToCaeBuilder.UseBodyOption@endlink
ExportToCaeBuilderUseBodyOption = ExportToCaeBuilder.UseBodyOption


##  @link OptimizationConstraintBuilderConstraintType NXOpen.DesignSimulation.OptimizationConstraintBuilderConstraintType @endlink is an alias for @link OptimizationConstraintBuilder.ConstraintType NXOpen.DesignSimulation.OptimizationConstraintBuilder.ConstraintType@endlink
OptimizationConstraintBuilderConstraintType = OptimizationConstraintBuilder.ConstraintType


##  @link OptimizationConstraintBuilderDisplacementOption NXOpen.DesignSimulation.OptimizationConstraintBuilderDisplacementOption @endlink is an alias for @link OptimizationConstraintBuilder.DisplacementOption NXOpen.DesignSimulation.OptimizationConstraintBuilder.DisplacementOption@endlink
OptimizationConstraintBuilderDisplacementOption = OptimizationConstraintBuilder.DisplacementOption


##  @link OptimizationConstraintBuilderMaximumStressOption NXOpen.DesignSimulation.OptimizationConstraintBuilderMaximumStressOption @endlink is an alias for @link OptimizationConstraintBuilder.MaximumStressOption NXOpen.DesignSimulation.OptimizationConstraintBuilder.MaximumStressOption@endlink
OptimizationConstraintBuilderMaximumStressOption = OptimizationConstraintBuilder.MaximumStressOption


##  @link ResultMeasureBuilderResultComponentOption NXOpen.DesignSimulation.ResultMeasureBuilderResultComponentOption @endlink is an alias for @link ResultMeasureBuilder.ResultComponentOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultComponentOption@endlink
ResultMeasureBuilderResultComponentOption = ResultMeasureBuilder.ResultComponentOption


##  @link ResultMeasureBuilderResultTypeOption NXOpen.DesignSimulation.ResultMeasureBuilderResultTypeOption @endlink is an alias for @link ResultMeasureBuilder.ResultTypeOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultTypeOption@endlink
ResultMeasureBuilderResultTypeOption = ResultMeasureBuilder.ResultTypeOption


##  @link ResultMeasureBuilderResultValueOption NXOpen.DesignSimulation.ResultMeasureBuilderResultValueOption @endlink is an alias for @link ResultMeasureBuilder.ResultValueOption NXOpen.DesignSimulation.ResultMeasureBuilder.ResultValueOption@endlink
ResultMeasureBuilderResultValueOption = ResultMeasureBuilder.ResultValueOption


##  @link SceneryBodyBuilderMaterialDefinitionType NXOpen.DesignSimulation.SceneryBodyBuilderMaterialDefinitionType @endlink is an alias for @link SceneryBodyBuilder.MaterialDefinitionType NXOpen.DesignSimulation.SceneryBodyBuilder.MaterialDefinitionType@endlink
SceneryBodyBuilderMaterialDefinitionType = SceneryBodyBuilder.MaterialDefinitionType


##  @link ShapeConstraintBuilderCenterOfGravityLocationType NXOpen.DesignSimulation.ShapeConstraintBuilderCenterOfGravityLocationType @endlink is an alias for @link ShapeConstraintBuilder.CenterOfGravityLocationType NXOpen.DesignSimulation.ShapeConstraintBuilder.CenterOfGravityLocationType@endlink
ShapeConstraintBuilderCenterOfGravityLocationType = ShapeConstraintBuilder.CenterOfGravityLocationType


##  @link ShapeConstraintBuilderConstraintType NXOpen.DesignSimulation.ShapeConstraintBuilderConstraintType @endlink is an alias for @link ShapeConstraintBuilder.ConstraintType NXOpen.DesignSimulation.ShapeConstraintBuilder.ConstraintType@endlink
ShapeConstraintBuilderConstraintType = ShapeConstraintBuilder.ConstraintType


##  @link ShapeConstraintBuilderDraftPartingObjectType NXOpen.DesignSimulation.ShapeConstraintBuilderDraftPartingObjectType @endlink is an alias for @link ShapeConstraintBuilder.DraftPartingObjectType NXOpen.DesignSimulation.ShapeConstraintBuilder.DraftPartingObjectType@endlink
ShapeConstraintBuilderDraftPartingObjectType = ShapeConstraintBuilder.DraftPartingObjectType


##  @link ShapeConstraintBuilderFillFromDirectionType NXOpen.DesignSimulation.ShapeConstraintBuilderFillFromDirectionType @endlink is an alias for @link ShapeConstraintBuilder.FillFromDirectionType NXOpen.DesignSimulation.ShapeConstraintBuilder.FillFromDirectionType@endlink
ShapeConstraintBuilderFillFromDirectionType = ShapeConstraintBuilder.FillFromDirectionType


##  @link ShapeConstraintBuilderMaxOverhangAngleValue NXOpen.DesignSimulation.ShapeConstraintBuilderMaxOverhangAngleValue @endlink is an alias for @link ShapeConstraintBuilder.MaxOverhangAngleValue NXOpen.DesignSimulation.ShapeConstraintBuilder.MaxOverhangAngleValue@endlink
ShapeConstraintBuilderMaxOverhangAngleValue = ShapeConstraintBuilder.MaxOverhangAngleValue


##  @link ShapeConstraintBuilderMultiAxisToolingType NXOpen.DesignSimulation.ShapeConstraintBuilderMultiAxisToolingType @endlink is an alias for @link ShapeConstraintBuilder.MultiAxisToolingType NXOpen.DesignSimulation.ShapeConstraintBuilder.MultiAxisToolingType@endlink
ShapeConstraintBuilderMultiAxisToolingType = ShapeConstraintBuilder.MultiAxisToolingType


##  @link ShapeConstraintBuilderPlanarSymmetryInputOption NXOpen.DesignSimulation.ShapeConstraintBuilderPlanarSymmetryInputOption @endlink is an alias for @link ShapeConstraintBuilder.PlanarSymmetryInputOption NXOpen.DesignSimulation.ShapeConstraintBuilder.PlanarSymmetryInputOption@endlink
ShapeConstraintBuilderPlanarSymmetryInputOption = ShapeConstraintBuilder.PlanarSymmetryInputOption


##  @link StudyBuilderAnalysisOption NXOpen.DesignSimulation.StudyBuilderAnalysisOption @endlink is an alias for @link StudyBuilder.AnalysisOption NXOpen.DesignSimulation.StudyBuilder.AnalysisOption@endlink
StudyBuilderAnalysisOption = StudyBuilder.AnalysisOption


##  @link StudyBuilderOptimizationObjectiveOption NXOpen.DesignSimulation.StudyBuilderOptimizationObjectiveOption @endlink is an alias for @link StudyBuilder.OptimizationObjectiveOption NXOpen.DesignSimulation.StudyBuilder.OptimizationObjectiveOption@endlink
StudyBuilderOptimizationObjectiveOption = StudyBuilder.OptimizationObjectiveOption


##  @link StudyBuilderSubcaseSummationOption NXOpen.DesignSimulation.StudyBuilderSubcaseSummationOption @endlink is an alias for @link StudyBuilder.SubcaseSummationOption NXOpen.DesignSimulation.StudyBuilder.SubcaseSummationOption@endlink
StudyBuilderSubcaseSummationOption = StudyBuilder.SubcaseSummationOption


##  @link SubcaseItemItemType NXOpen.DesignSimulation.SubcaseItemItemType @endlink is an alias for @link SubcaseItem.ItemType NXOpen.DesignSimulation.SubcaseItem.ItemType@endlink
SubcaseItemItemType = SubcaseItem.ItemType


##  @link SubcaseIncludeInOptimization NXOpen.DesignSimulation.SubcaseIncludeInOptimization @endlink is an alias for @link Subcase.IncludeInOptimization NXOpen.DesignSimulation.Subcase.IncludeInOptimization@endlink
SubcaseIncludeInOptimization = Subcase.IncludeInOptimization


##  @link ViewContourBuilderColorDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilderColorDisplayStyleOption @endlink is an alias for @link ViewContourBuilder.ColorDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ColorDisplayStyleOption@endlink
ViewContourBuilderColorDisplayStyleOption = ViewContourBuilder.ColorDisplayStyleOption


##  @link ViewContourBuilderColorScaleRangeOption NXOpen.DesignSimulation.ViewContourBuilderColorScaleRangeOption @endlink is an alias for @link ViewContourBuilder.ColorScaleRangeOption NXOpen.DesignSimulation.ViewContourBuilder.ColorScaleRangeOption@endlink
ViewContourBuilderColorScaleRangeOption = ViewContourBuilder.ColorScaleRangeOption


##  @link ViewContourBuilderContourDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilderContourDisplayStyleOption @endlink is an alias for @link ViewContourBuilder.ContourDisplayStyleOption NXOpen.DesignSimulation.ViewContourBuilder.ContourDisplayStyleOption@endlink
ViewContourBuilderContourDisplayStyleOption = ViewContourBuilder.ContourDisplayStyleOption


##  @link ViewContourBuilderDisplayOption NXOpen.DesignSimulation.ViewContourBuilderDisplayOption @endlink is an alias for @link ViewContourBuilder.DisplayOption NXOpen.DesignSimulation.ViewContourBuilder.DisplayOption@endlink
ViewContourBuilderDisplayOption = ViewContourBuilder.DisplayOption


##  @link ViewContourBuilderMaterialLimitOption NXOpen.DesignSimulation.ViewContourBuilderMaterialLimitOption @endlink is an alias for @link ViewContourBuilder.MaterialLimitOption NXOpen.DesignSimulation.ViewContourBuilder.MaterialLimitOption@endlink
ViewContourBuilderMaterialLimitOption = ViewContourBuilder.MaterialLimitOption


##  @link ViewContourBuilderResultComponentOption NXOpen.DesignSimulation.ViewContourBuilderResultComponentOption @endlink is an alias for @link ViewContourBuilder.ResultComponentOption NXOpen.DesignSimulation.ViewContourBuilder.ResultComponentOption@endlink
ViewContourBuilderResultComponentOption = ViewContourBuilder.ResultComponentOption


##  @link ViewTabularResultBuilderReportContentOption NXOpen.DesignSimulation.ViewTabularResultBuilderReportContentOption @endlink is an alias for @link ViewTabularResultBuilder.ReportContentOption NXOpen.DesignSimulation.ViewTabularResultBuilder.ReportContentOption@endlink
ViewTabularResultBuilderReportContentOption = ViewTabularResultBuilder.ReportContentOption


##  @link ViewXygraphBuilderContentOption NXOpen.DesignSimulation.ViewXygraphBuilderContentOption @endlink is an alias for @link ViewXygraphBuilder.ContentOption NXOpen.DesignSimulation.ViewXygraphBuilder.ContentOption@endlink
ViewXygraphBuilderContentOption = ViewXygraphBuilder.ContentOption


