from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
## 
##        Represents a @link NXOpen::Facet::AdjustMinimumRadiusBuilder NXOpen::Facet::AdjustMinimumRadiusBuilder@endlink .
##        It smooths the input bodies such that their minimum radius of curvature is larger than the prescribed radius of curvature.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateFacetAdjustMinimumRadiusBuilder  NXOpen::Facet::FacetModelingCollection::CreateFacetAdjustMinimumRadiusBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class AdjustMinimumRadiusBuilder(NXOpen.Builder): 
    """
       Represents a <ja_class>NXOpen.Facet.AdjustMinimumRadiusBuilder</ja_class>.
       It smooths the input bodies such that their minimum radius of curvature is larger than the prescribed radius of curvature.
    """


    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) Facets
    ##  Returns the input facets.  
    ##    Inputs to this command can be convergent objects.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def Facets(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) Facets
         Returns the input facets.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    
    ## Getter for property: (bool) IsEditCopy
    ##  Returns the flag indicating if the adjust minimum radius is on the copy of the input facet body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the flag indicating if the adjust minimum radius is on the copy of the input facet body.  
             
         
        """
        pass
    
    ## Setter for property: (bool) IsEditCopy

    ##  Returns the flag indicating if the adjust minimum radius is on the copy of the input facet body.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the flag indicating if the adjust minimum radius is on the copy of the input facet body.  
             
         
        """
        pass
    
    ## Getter for property: (float) MinimumRadius
    ##  Returns the minimum radius of curvature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return float
    @property
    def MinimumRadius(self) -> float:
        """
        Getter for property: (float) MinimumRadius
         Returns the minimum radius of curvature   
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumRadius

    ##  Returns the minimum radius of curvature   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @MinimumRadius.setter
    def MinimumRadius(self, radius: float):
        """
        Setter for property: (float) MinimumRadius
         Returns the minimum radius of curvature   
            
         
        """
        pass
    
import NXOpen
##  This class performs the best fit alignment between objects  <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateBestFitAlignBuilder  NXOpen::Facet::FacetedBodyCollection::CreateBestFitAlignBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class BestFitAlignBuilder(NXOpen.Builder): 
    """ This class performs the best fit alignment between objects """


    ##  Represents the constraint options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Free</term><description> 
    ##  No constraint </description> </item><item><term> 
    ## OnlyTranslation</term><description> 
    ##  Only translation </description> </item><item><term> 
    ## TranslationInPlane</term><description> 
    ##  Translation in the plane </description> </item><item><term> 
    ## TranslationAlongDirection</term><description> 
    ##  Translation along direction </description> </item><item><term> 
    ## OnlyRotation</term><description> 
    ##  Only rotation </description> </item><item><term> 
    ## RotationAroundPoint</term><description> 
    ##  Rotation around specific point </description> </item><item><term> 
    ## RotationAroundLine</term><description> 
    ##  Rotation around specific line </description> </item><item><term> 
    ## HoldToPlane</term><description> 
    ##  Moving in the plane </description> </item><item><term> 
    ## HoldToLine</term><description> 
    ##  Moving along the line </description> </item></list>
    class ConstraintOptions(Enum):
        """
        Members Include: <Free> <OnlyTranslation> <TranslationInPlane> <TranslationAlongDirection> <OnlyRotation> <RotationAroundPoint> <RotationAroundLine> <HoldToPlane> <HoldToLine>
        """
        Free: int
        OnlyTranslation: int
        TranslationInPlane: int
        TranslationAlongDirection: int
        OnlyRotation: int
        RotationAroundPoint: int
        RotationAroundLine: int
        HoldToPlane: int
        HoldToLine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BestFitAlignBuilder.ConstraintOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) DestinationObjects
    ##  Returns the destination objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def DestinationObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) DestinationObjects
         Returns the destination objects   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
    ##  Returns the plane or line direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Direction(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
         Returns the plane or line direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction

    ##  Returns the plane or line direction   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Direction.setter
    def Direction(self, direction: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
         Returns the plane or line direction   
            
         
        """
        pass
    
    ## Getter for property: (@link BestFitAlignBuilder.ConstraintOptions NXOpen.Facet.BestFitAlignBuilder.ConstraintOptions@endlink) FitConstraints
    ##  Returns the fit constraint   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return BestFitAlignBuilder.ConstraintOptions
    @property
    def FitConstraints(self) -> BestFitAlignBuilder.ConstraintOptions:
        """
        Getter for property: (@link BestFitAlignBuilder.ConstraintOptions NXOpen.Facet.BestFitAlignBuilder.ConstraintOptions@endlink) FitConstraints
         Returns the fit constraint   
            
         
        """
        pass
    
    ## Setter for property: (@link BestFitAlignBuilder.ConstraintOptions NXOpen.Facet.BestFitAlignBuilder.ConstraintOptions@endlink) FitConstraints

    ##  Returns the fit constraint   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @FitConstraints.setter
    def FitConstraints(self, fitConstraints: BestFitAlignBuilder.ConstraintOptions):
        """
        Setter for property: (@link BestFitAlignBuilder.ConstraintOptions NXOpen.Facet.BestFitAlignBuilder.ConstraintOptions@endlink) FitConstraints
         Returns the fit constraint   
            
         
        """
        pass
    
    ## Getter for property: (bool) GlobalSearch
    ##  Returns a value indicating whether to do a global search   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def GlobalSearch(self) -> bool:
        """
        Getter for property: (bool) GlobalSearch
         Returns a value indicating whether to do a global search   
            
         
        """
        pass
    
    ## Setter for property: (bool) GlobalSearch

    ##  Returns a value indicating whether to do a global search   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @GlobalSearch.setter
    def GlobalSearch(self, globalSearch: bool):
        """
        Setter for property: (bool) GlobalSearch
         Returns a value indicating whether to do a global search   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) MobileObjects
    ##  Returns the mobile objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def MobileObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) MobileObjects
         Returns the mobile objects   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) RotateCenter
    ##  Returns the rotation center   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def RotateCenter(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) RotateCenter
         Returns the rotation center   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) RotateCenter

    ##  Returns the rotation center   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @RotateCenter.setter
    def RotateCenter(self, rotateCenter: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) RotateCenter
         Returns the rotation center   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SourceObjects
    ##  Returns the source objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def SourceObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SourceObjects
         Returns the source objects   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::BridgeFacetBodyBuilder NXOpen::Facet::BridgeFacetBodyBuilder@endlink 
##     It bridges two disjoint NX facet bodies. User need to specify the range for each input facet body.
##     It returns a new megered NX facet Body. The two input bodies can be kept, deleted or hidden.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateBridgeFacetBodyBuilder  NXOpen::Facet::FacetedBodyCollection::CreateBridgeFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## InputStatus </term> <description> 
##  
## Keep </description> </item> 
## 
## <item><term> 
##  
## Smoothness </term> <description> 
##  
## Linear </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class BridgeFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.BridgeFacetBodyBuilder</ja_class>
    It bridges two disjoint NX facet bodies. User need to specify the range for each input facet body.
    It returns a new megered NX facet Body. The two input bodies can be kept, deleted or hidden.
    """


    ##  Represents the option for keeping, deleting or hiding input two facet bodies after builder committing 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Keep</term><description> 
    ##  Keep the input facet body after builder committing </description> </item><item><term> 
    ## Delete</term><description> 
    ##  Delete the input facet body after builder committing </description> </item><item><term> 
    ## Hide</term><description> 
    ##  Hide the input facet body after builder committing </description> </item></list>
    class Input(Enum):
        """
        Members Include: <Keep> <Delete> <Hide>
        """
        Keep: int
        Delete: int
        Hide: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BridgeFacetBodyBuilder.Input:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the smoothness type for the inserted new facets 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  Insert new facets with linear smoothness </description> </item><item><term> 
    ## TangentBased</term><description> 
    ##  Insert new facets with tangent smoothness </description> </item></list>
    class SmoothTypes(Enum):
        """
        Members Include: <Linear> <TangentBased>
        """
        Linear: int
        TangentBased: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BridgeFacetBodyBuilder.SmoothTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DistanceTolerance
    ##  Returns the distance tolerance used in the bridge facet body feature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the bridge facet body feature   
            
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##  Returns the distance tolerance used in the bridge facet body feature   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the bridge facet body feature   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) FacetBodyOne
    ##  Returns the first NX facet body to be bridged   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectFacetedBody
    @property
    def FacetBodyOne(self) -> SelectFacetedBody:
        """
        Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) FacetBodyOne
         Returns the first NX facet body to be bridged   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) FacetBodyTwo
    ##  Returns the second NX facet body to be bridged   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectFacetedBody
    @property
    def FacetBodyTwo(self) -> SelectFacetedBody:
        """
        Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) FacetBodyTwo
         Returns the second NX facet body to be bridged   
            
         
        """
        pass
    
    ## Getter for property: (@link BridgeFacetBodyBuilder.Input NXOpen.Facet.BridgeFacetBodyBuilder.Input@endlink) InputStatus
    ##  Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return BridgeFacetBodyBuilder.Input
    @property
    def InputStatus(self) -> BridgeFacetBodyBuilder.Input:
        """
        Getter for property: (@link BridgeFacetBodyBuilder.Input NXOpen.Facet.BridgeFacetBodyBuilder.Input@endlink) InputStatus
         Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
            
         
        """
        pass
    
    ## Setter for property: (@link BridgeFacetBodyBuilder.Input NXOpen.Facet.BridgeFacetBodyBuilder.Input@endlink) InputStatus

    ##  Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @InputStatus.setter
    def InputStatus(self, inputStatus: BridgeFacetBodyBuilder.Input):
        """
        Setter for property: (@link BridgeFacetBodyBuilder.Input NXOpen.Facet.BridgeFacetBodyBuilder.Input@endlink) InputStatus
         Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
            
         
        """
        pass
    
    ## Getter for property: (@link BridgeFacetBodyBuilder.SmoothTypes NXOpen.Facet.BridgeFacetBodyBuilder.SmoothTypes@endlink) Smoothness
    ##  Returns the inserted facet smooth type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return BridgeFacetBodyBuilder.SmoothTypes
    @property
    def Smoothness(self) -> BridgeFacetBodyBuilder.SmoothTypes:
        """
        Getter for property: (@link BridgeFacetBodyBuilder.SmoothTypes NXOpen.Facet.BridgeFacetBodyBuilder.SmoothTypes@endlink) Smoothness
         Returns the inserted facet smooth type   
            
         
        """
        pass
    
    ## Setter for property: (@link BridgeFacetBodyBuilder.SmoothTypes NXOpen.Facet.BridgeFacetBodyBuilder.SmoothTypes@endlink) Smoothness

    ##  Returns the inserted facet smooth type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Smoothness.setter
    def Smoothness(self, smoothType: BridgeFacetBodyBuilder.SmoothTypes):
        """
        Setter for property: (@link BridgeFacetBodyBuilder.SmoothTypes NXOpen.Facet.BridgeFacetBodyBuilder.SmoothTypes@endlink) Smoothness
         Returns the inserted facet smooth type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1Range1
    ##  Returns the first vertex used to define the range on the the first facet body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Vertex1Range1(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1Range1
         Returns the first vertex used to define the range on the the first facet body   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1Range1

    ##  Returns the first vertex used to define the range on the the first facet body   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Vertex1Range1.setter
    def Vertex1Range1(self, vertex1Range1: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1Range1
         Returns the first vertex used to define the range on the the first facet body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1Range2
    ##  Returns the first vertex used to defind the range on the second facet body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Vertex1Range2(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1Range2
         Returns the first vertex used to defind the range on the second facet body   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1Range2

    ##  Returns the first vertex used to defind the range on the second facet body   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Vertex1Range2.setter
    def Vertex1Range2(self, vertex1Range2: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1Range2
         Returns the first vertex used to defind the range on the second facet body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2Range1
    ##  Returns the second vertex used to define the range on the first facet body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Vertex2Range1(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2Range1
         Returns the second vertex used to define the range on the first facet body   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2Range1

    ##  Returns the second vertex used to define the range on the first facet body   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Vertex2Range1.setter
    def Vertex2Range1(self, vertex2Range1: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2Range1
         Returns the second vertex used to define the range on the first facet body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2Range2
    ##  Returns the second vertex used to defind the range on the second facet body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Vertex2Range2(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2Range2
         Returns the second vertex used to defind the range on the second facet body   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2Range2

    ##  Returns the second vertex used to defind the range on the second facet body   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Vertex2Range2.setter
    def Vertex2Range2(self, vertex2Range2: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2Range2
         Returns the second vertex used to defind the range on the second facet body   
            
         
        """
        pass
    
    ##  Flip the range between the first and second vertex on the first facet body 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def FlipRange1(self) -> None:
        """
         Flip the range between the first and second vertex on the first facet body 
        """
        pass
    
    ##  Flip the range between the first and second vertex on the second facet body 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def FlipRange2(self) -> None:
        """
         Flip the range between the first and second vertex on the second facet body 
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::CleanupFacetBodyBuilder NXOpen::Facet::CleanupFacetBodyBuilder@endlink  builder. 
##     It removes defects that are present in the surfaces of the bodies selected. 
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateCleanupFacetBodyBuilder  NXOpen::Facet::FacetModelingCollection::CreateCleanupFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## FoldedEdges </term> <description> 
##  
## Analyze </description> </item> 
## 
## <item><term> 
##  
## InconsistentNormals </term> <description> 
##  
## Analyze </description> </item> 
## 
## <item><term> 
##  
## LaminarSlits </term> <description> 
##  
## Analyze </description> </item> 
## 
## <item><term> 
##  
## LongFacets </term> <description> 
##  
## Analyze </description> </item> 
## 
## <item><term> 
##  
## MaxRatioLongFacets </term> <description> 
##  
## 10 </description> </item> 
## 
## <item><term> 
##  
## MinAngleFoldedFacets </term> <description> 
##  
## 15 </description> </item> 
## 
## <item><term> 
##  
## OriginalBodyOption </term> <description> 
##  
## Delete </description> </item> 
## 
## <item><term> 
##  
## SelfIntersections </term> <description> 
##  
## Analyze </description> </item> 
## 
## <item><term> 
##  
## ShowInfo </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ThinFacets </term> <description> 
##  
## Analyze </description> </item> 
## 
## <item><term> 
##  
## ToleranceFactor </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class CleanupFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.CleanupFacetBodyBuilder</ja_class> builder. 
    It removes defects that are present in the surfaces of the bodies selected. 
    """


    ##  These represent the options for each facet defect 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  Don't perform Analysis or Repair </description> </item><item><term> 
    ## Analyze</term><description> 
    ##  Perform Analysis </description> </item><item><term> 
    ## Repair</term><description> 
    ##  Perform Repair </description> </item></list>
    class CleanupOptions(Enum):
        """
        Members Include: <NotSet> <Analyze> <Repair>
        """
        NotSet: int
        Analyze: int
        Repair: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CleanupFacetBodyBuilder.CleanupOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  These represent the options for handling the input bodies  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Keep</term><description> 
    ##  Keep original body </description> </item><item><term> 
    ## Hide</term><description> 
    ##  Hide original body </description> </item><item><term> 
    ## Delete</term><description> 
    ##  Delete original body </description> </item></list>
    class OriginalBodyOptions(Enum):
        """
        Members Include: <Keep> <Hide> <Delete>
        """
        Keep: int
        Hide: int
        Delete: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CleanupFacetBodyBuilder.OriginalBodyOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DistanceTolerance
    ##  Returns the tolerance value use to detect the faults in facet body and fix the same.  
    ##   
    ##          <br> 
    ##         This API is now deprecated.
    ##         Please use @link ToleranceFactor ToleranceFactor@endlink  and @link DistanceTolerance DistanceTolerance@endlink  instead.
    ##          <br> 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Please use @link CleanupFacetBodyBuilder::ToleranceFactor CleanupFacetBodyBuilder::ToleranceFactor@endlink  instead @link CleanupFacetBodyBuilder::DistanceTolerance CleanupFacetBodyBuilder::DistanceTolerance@endlink   <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the tolerance value use to detect the faults in facet body and fix the same.  
          
                 <br> 
                This API is now deprecated.
                Please use @link ToleranceFactor ToleranceFactor@endlink  and @link DistanceTolerance DistanceTolerance@endlink  instead.
                 <br> 
                  
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##  Returns the tolerance value use to detect the faults in facet body and fix the same.  
    ##   
    ##          <br> 
    ##         This API is now deprecated.
    ##         Please use @link ToleranceFactor ToleranceFactor@endlink  and @link DistanceTolerance DistanceTolerance@endlink  instead.
    ##          <br> 
    ##           
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Please use @link CleanupFacetBodyBuilder::ToleranceFactor CleanupFacetBodyBuilder::ToleranceFactor@endlink  instead @link CleanupFacetBodyBuilder::DistanceTolerance CleanupFacetBodyBuilder::DistanceTolerance@endlink   <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, disTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the tolerance value use to detect the faults in facet body and fix the same.  
          
                 <br> 
                This API is now deprecated.
                Please use @link ToleranceFactor ToleranceFactor@endlink  and @link DistanceTolerance DistanceTolerance@endlink  instead.
                 <br> 
                  
         
        """
        pass
    
    ## Getter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) FoldedEdges
    ##  Returns the option to identify or repair facets having an angle with adjacent facets less than a specified minimum value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return CleanupFacetBodyBuilder.CleanupOptions
    @property
    def FoldedEdges(self) -> CleanupFacetBodyBuilder.CleanupOptions:
        """
        Getter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) FoldedEdges
         Returns the option to identify or repair facets having an angle with adjacent facets less than a specified minimum value   
            
         
        """
        pass
    
    ## Setter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) FoldedEdges

    ##  Returns the option to identify or repair facets having an angle with adjacent facets less than a specified minimum value   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @FoldedEdges.setter
    def FoldedEdges(self, foldedEdges: CleanupFacetBodyBuilder.CleanupOptions):
        """
        Setter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) FoldedEdges
         Returns the option to identify or repair facets having an angle with adjacent facets less than a specified minimum value   
            
         
        """
        pass
    
    ## Getter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) InconsistentNormals
    ##  Returns the option to identify or repair normals of neighboring facets or vertices that do not have the right orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return CleanupFacetBodyBuilder.CleanupOptions
    @property
    def InconsistentNormals(self) -> CleanupFacetBodyBuilder.CleanupOptions:
        """
        Getter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) InconsistentNormals
         Returns the option to identify or repair normals of neighboring facets or vertices that do not have the right orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) InconsistentNormals

    ##  Returns the option to identify or repair normals of neighboring facets or vertices that do not have the right orientation   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @InconsistentNormals.setter
    def InconsistentNormals(self, inconsistentNormals: CleanupFacetBodyBuilder.CleanupOptions):
        """
        Setter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) InconsistentNormals
         Returns the option to identify or repair normals of neighboring facets or vertices that do not have the right orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) InputBodies
    ##  Returns the input facet bodies to be analyzed or repaired   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def InputBodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) InputBodies
         Returns the input facet bodies to be analyzed or repaired   
            
         
        """
        pass
    
    ## Getter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) LaminarSlits
    ##  Returns the option to identify or repair thin holes or slits in the mesh caused by facets not being aligned   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return CleanupFacetBodyBuilder.CleanupOptions
    @property
    def LaminarSlits(self) -> CleanupFacetBodyBuilder.CleanupOptions:
        """
        Getter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) LaminarSlits
         Returns the option to identify or repair thin holes or slits in the mesh caused by facets not being aligned   
            
         
        """
        pass
    
    ## Setter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) LaminarSlits

    ##  Returns the option to identify or repair thin holes or slits in the mesh caused by facets not being aligned   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LaminarSlits.setter
    def LaminarSlits(self, laminarSlits: CleanupFacetBodyBuilder.CleanupOptions):
        """
        Setter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) LaminarSlits
         Returns the option to identify or repair thin holes or slits in the mesh caused by facets not being aligned   
            
         
        """
        pass
    
    ## Getter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) LongFacets
    ##  Returns the option to identify or repair facets with a ratio of longest to shortest side exceeding a specified value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return CleanupFacetBodyBuilder.CleanupOptions
    @property
    def LongFacets(self) -> CleanupFacetBodyBuilder.CleanupOptions:
        """
        Getter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) LongFacets
         Returns the option to identify or repair facets with a ratio of longest to shortest side exceeding a specified value   
            
         
        """
        pass
    
    ## Setter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) LongFacets

    ##  Returns the option to identify or repair facets with a ratio of longest to shortest side exceeding a specified value   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LongFacets.setter
    def LongFacets(self, longFacets: CleanupFacetBodyBuilder.CleanupOptions):
        """
        Setter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) LongFacets
         Returns the option to identify or repair facets with a ratio of longest to shortest side exceeding a specified value   
            
         
        """
        pass
    
    ## Getter for property: (float) MaxRatioLongFacets
    ##  Returns the specified value used to define long facets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def MaxRatioLongFacets(self) -> float:
        """
        Getter for property: (float) MaxRatioLongFacets
         Returns the specified value used to define long facets   
            
         
        """
        pass
    
    ## Setter for property: (float) MaxRatioLongFacets

    ##  Returns the specified value used to define long facets   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @MaxRatioLongFacets.setter
    def MaxRatioLongFacets(self, maxRatioLongFacets: float):
        """
        Setter for property: (float) MaxRatioLongFacets
         Returns the specified value used to define long facets   
            
         
        """
        pass
    
    ## Getter for property: (float) MinAngleFoldedFacets
    ##  Returns the minimum angle between adjacent facets to define folded facets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def MinAngleFoldedFacets(self) -> float:
        """
        Getter for property: (float) MinAngleFoldedFacets
         Returns the minimum angle between adjacent facets to define folded facets   
            
         
        """
        pass
    
    ## Setter for property: (float) MinAngleFoldedFacets

    ##  Returns the minimum angle between adjacent facets to define folded facets   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @MinAngleFoldedFacets.setter
    def MinAngleFoldedFacets(self, minAngleFoldedFacets: float):
        """
        Setter for property: (float) MinAngleFoldedFacets
         Returns the minimum angle between adjacent facets to define folded facets   
            
         
        """
        pass
    
    ## Getter for property: (int) MinFacetNumberPerBody
    ##  Returns the minimum number of facets per mesh   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return int
    @property
    def MinFacetNumberPerBody(self) -> int:
        """
        Getter for property: (int) MinFacetNumberPerBody
         Returns the minimum number of facets per mesh   
            
         
        """
        pass
    
    ## Setter for property: (int) MinFacetNumberPerBody

    ##  Returns the minimum number of facets per mesh   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @MinFacetNumberPerBody.setter
    def MinFacetNumberPerBody(self, minFacetNumber: int):
        """
        Setter for property: (int) MinFacetNumberPerBody
         Returns the minimum number of facets per mesh   
            
         
        """
        pass
    
    ## Getter for property: (@link CleanupFacetBodyBuilder.OriginalBodyOptions NXOpen.Facet.CleanupFacetBodyBuilder.OriginalBodyOptions@endlink) OriginalBodyOption
    ##  Returns the option for handling the input facet bodies   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return CleanupFacetBodyBuilder.OriginalBodyOptions
    @property
    def OriginalBodyOption(self) -> CleanupFacetBodyBuilder.OriginalBodyOptions:
        """
        Getter for property: (@link CleanupFacetBodyBuilder.OriginalBodyOptions NXOpen.Facet.CleanupFacetBodyBuilder.OriginalBodyOptions@endlink) OriginalBodyOption
         Returns the option for handling the input facet bodies   
            
         
        """
        pass
    
    ## Setter for property: (@link CleanupFacetBodyBuilder.OriginalBodyOptions NXOpen.Facet.CleanupFacetBodyBuilder.OriginalBodyOptions@endlink) OriginalBodyOption

    ##  Returns the option for handling the input facet bodies   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @OriginalBodyOption.setter
    def OriginalBodyOption(self, enumOriginalBodyOption: CleanupFacetBodyBuilder.OriginalBodyOptions):
        """
        Setter for property: (@link CleanupFacetBodyBuilder.OriginalBodyOptions NXOpen.Facet.CleanupFacetBodyBuilder.OriginalBodyOptions@endlink) OriginalBodyOption
         Returns the option for handling the input facet bodies   
            
         
        """
        pass
    
    ## Getter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) SelfIntersections
    ##  Returns the option to identify or repair facets of the same mesh intersecting each other   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return CleanupFacetBodyBuilder.CleanupOptions
    @property
    def SelfIntersections(self) -> CleanupFacetBodyBuilder.CleanupOptions:
        """
        Getter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) SelfIntersections
         Returns the option to identify or repair facets of the same mesh intersecting each other   
            
         
        """
        pass
    
    ## Setter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) SelfIntersections

    ##  Returns the option to identify or repair facets of the same mesh intersecting each other   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @SelfIntersections.setter
    def SelfIntersections(self, selfIntersections: CleanupFacetBodyBuilder.CleanupOptions):
        """
        Setter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) SelfIntersections
         Returns the option to identify or repair facets of the same mesh intersecting each other   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowInfo
    ##  Returns 
    ##         the option to display numbers of various type of defects identified or repaired in the @link  NXOpen::ListingWindow   NXOpen::ListingWindow @endlink .  
    ##   
    ##         If this option is true, but the program is running externally without UI, display would go to
    ##         a standard output devicethe.  The listing window output can be sent to the Information window or to a 
    ##         file, or to both. See @link  NXOpen::ListingWindow::SelectDevice   NXOpen::ListingWindow::SelectDevice @endlink 
    ##         for more information.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ShowInfo(self) -> bool:
        """
        Getter for property: (bool) ShowInfo
         Returns 
                the option to display numbers of various type of defects identified or repaired in the @link  NXOpen::ListingWindow   NXOpen::ListingWindow @endlink .  
          
                If this option is true, but the program is running externally without UI, display would go to
                a standard output devicethe.  The listing window output can be sent to the Information window or to a 
                file, or to both. See @link  NXOpen::ListingWindow::SelectDevice   NXOpen::ListingWindow::SelectDevice @endlink 
                for more information.
                  
         
        """
        pass
    
    ## Setter for property: (bool) ShowInfo

    ##  Returns 
    ##         the option to display numbers of various type of defects identified or repaired in the @link  NXOpen::ListingWindow   NXOpen::ListingWindow @endlink .  
    ##   
    ##         If this option is true, but the program is running externally without UI, display would go to
    ##         a standard output devicethe.  The listing window output can be sent to the Information window or to a 
    ##         file, or to both. See @link  NXOpen::ListingWindow::SelectDevice   NXOpen::ListingWindow::SelectDevice @endlink 
    ##         for more information.
    ##           
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ShowInfo.setter
    def ShowInfo(self, showInfo: bool):
        """
        Setter for property: (bool) ShowInfo
         Returns 
                the option to display numbers of various type of defects identified or repaired in the @link  NXOpen::ListingWindow   NXOpen::ListingWindow @endlink .  
          
                If this option is true, but the program is running externally without UI, display would go to
                a standard output devicethe.  The listing window output can be sent to the Information window or to a 
                file, or to both. See @link  NXOpen::ListingWindow::SelectDevice   NXOpen::ListingWindow::SelectDevice @endlink 
                for more information.
                  
         
        """
        pass
    
    ## Getter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) ThinFacets
    ##  Returns the option to identify or repair facets with with one long edge and two edges with more or the less the same length and a ratio of length to width exceeding a specified value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return CleanupFacetBodyBuilder.CleanupOptions
    @property
    def ThinFacets(self) -> CleanupFacetBodyBuilder.CleanupOptions:
        """
        Getter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) ThinFacets
         Returns the option to identify or repair facets with with one long edge and two edges with more or the less the same length and a ratio of length to width exceeding a specified value   
            
         
        """
        pass
    
    ## Setter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) ThinFacets

    ##  Returns the option to identify or repair facets with with one long edge and two edges with more or the less the same length and a ratio of length to width exceeding a specified value   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ThinFacets.setter
    def ThinFacets(self, thinFacets: CleanupFacetBodyBuilder.CleanupOptions):
        """
        Setter for property: (@link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink) ThinFacets
         Returns the option to identify or repair facets with with one long edge and two edges with more or the less the same length and a ratio of length to width exceeding a specified value   
            
         
        """
        pass
    
    ## Getter for property: (float) ToleranceFactor
    ##  Returns the tolerance factor use to detect the faults in facet body and fix the same   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def ToleranceFactor(self) -> float:
        """
        Getter for property: (float) ToleranceFactor
         Returns the tolerance factor use to detect the faults in facet body and fix the same   
            
         
        """
        pass
    
    ## Setter for property: (float) ToleranceFactor

    ##  Returns the tolerance factor use to detect the faults in facet body and fix the same   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ToleranceFactor.setter
    def ToleranceFactor(self, tolFactor: float):
        """
        Setter for property: (float) ToleranceFactor
         Returns the tolerance factor use to detect the faults in facet body and fix the same   
            
         
        """
        pass
    
    ##  
    ##         Displays the @link  NXOpen::ListingWindow   NXOpen::ListingWindow @endlink  with numbers of various type of defects identified or repaired.
    ##         If we call this method externally without UI, it displays 
    ##         the information on standard output device. The listing 
    ##         window output can be sent to the Information window or to a 
    ##         file, or to both. See @link  NXOpen::ListingWindow::SelectDevice   NXOpen::ListingWindow::SelectDevice @endlink 
    ##         for more information.
    ##         
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def DisplayCleanupReportInListWindow(self) -> None:
        """
         
                Displays the @link  NXOpen::ListingWindow   NXOpen::ListingWindow @endlink  with numbers of various type of defects identified or repaired.
                If we call this method externally without UI, it displays 
                the information on standard output device. The listing 
                window output can be sent to the Information window or to a 
                file, or to both. See @link  NXOpen::ListingWindow::SelectDevice   NXOpen::ListingWindow::SelectDevice @endlink 
                for more information.
                
        """
        pass
    
    ##  Sets all cleanup options to @link Facet::CleanupFacetBodyBuilder::CleanupOptionsAnalyze Facet::CleanupFacetBodyBuilder::CleanupOptionsAnalyze@endlink , which means to identify the defects only for the input bodies 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def SetAllOptionsToAnalyze(self) -> None:
        """
         Sets all cleanup options to @link Facet::CleanupFacetBodyBuilder::CleanupOptionsAnalyze Facet::CleanupFacetBodyBuilder::CleanupOptionsAnalyze@endlink , which means to identify the defects only for the input bodies 
        """
        pass
    
    ##  Sets all cleanup options to @link Facet::CleanupFacetBodyBuilder::CleanupOptionsNone Facet::CleanupFacetBodyBuilder::CleanupOptionsNone@endlink , which means to do nothing 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def SetAllOptionsToNone(self) -> None:
        """
         Sets all cleanup options to @link Facet::CleanupFacetBodyBuilder::CleanupOptionsNone Facet::CleanupFacetBodyBuilder::CleanupOptionsNone@endlink , which means to do nothing 
        """
        pass
    
    ##  Sets all cleanup options to @link Facet::CleanupFacetBodyBuilder::CleanupOptionsRepair Facet::CleanupFacetBodyBuilder::CleanupOptionsRepair@endlink , which means to identify as well as repair the defects for the input bodies 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def SetAllOptionsToRepair(self) -> None:
        """
         Sets all cleanup options to @link Facet::CleanupFacetBodyBuilder::CleanupOptionsRepair Facet::CleanupFacetBodyBuilder::CleanupOptionsRepair@endlink , which means to identify as well as repair the defects for the input bodies 
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::CleanupFacetBodyWizardBuilder NXOpen::Facet::CleanupFacetBodyWizardBuilder@endlink  builder. 
##     It removes defects that are present in the surfaces of the bodies selected. 
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateCleanupFacetBodyWizardBuilder  NXOpen::Facet::FacetModelingCollection::CreateCleanupFacetBodyWizardBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AutomaticFillType </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## CircumferenceRings </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## CleanupFacetBodyBuilder.FoldedEdges </term> <description> 
##  
## Analyze </description> </item> 
## 
## <item><term> 
##  
## CleanupFacetBodyBuilder.InconsistentNormals </term> <description> 
##  
## Analyze </description> </item> 
## 
## <item><term> 
##  
## CleanupFacetBodyBuilder.LaminarSlits </term> <description> 
##  
## Analyze </description> </item> 
## 
## <item><term> 
##  
## CleanupFacetBodyBuilder.LongFacets </term> <description> 
##  
## Analyze </description> </item> 
## 
## <item><term> 
##  
## CleanupFacetBodyBuilder.MaxRatioLongFacets </term> <description> 
##  
## 10 </description> </item> 
## 
## <item><term> 
##  
## CleanupFacetBodyBuilder.MinAngleFoldedFacets </term> <description> 
##  
## 15 </description> </item> 
## 
## <item><term> 
##  
## CleanupFacetBodyBuilder.OriginalBodyOption </term> <description> 
##  
## Delete </description> </item> 
## 
## <item><term> 
##  
## CleanupFacetBodyBuilder.SelfIntersections </term> <description> 
##  
## Analyze </description> </item> 
## 
## <item><term> 
##  
## CleanupFacetBodyBuilder.ShowInfo </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CleanupFacetBodyBuilder.ThinFacets </term> <description> 
##  
## Analyze </description> </item> 
## 
## <item><term> 
##  
## CleanupFacetBodyBuilder.ToleranceFactor </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## FillMesh.EdgeSelectionMethod </term> <description> 
##  
## UserSelected </description> </item> 
## 
## <item><term> 
##  
## FillMesh.EditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## FillMesh.MaxEdges </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## FillMesh.SmoothnessOption </term> <description> 
##  
## Linear </description> </item> 
## 
## <item><term> 
##  
## FoldedEdges </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## InconsistentNormals </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## LaminarSlits </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## MinAngleFoldedFacets </term> <description> 
##  
## 10 </description> </item> 
## 
## <item><term> 
##  
## MinFacetNumberPerBody </term> <description> 
##  
## 100 </description> </item> 
## 
## <item><term> 
##  
## QualityIndex </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RegionRemoveOption </term> <description> 
##  
## ByRegion </description> </item> 
## 
## <item><term> 
##  
## SelfIntersections </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## SnipFacetBodyBuilder.AlongDirection </term> <description> 
##  
## ViewDirection </description> </item> 
## 
## <item><term> 
##  
## SnipFacetBodyBuilder.BoundaryFacetTreatmentType </term> <description> 
##  
## SnipFacets </description> </item> 
## 
## <item><term> 
##  
## SnipFacetBodyBuilder.CanDivide </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SnipFacetBodyBuilder.IsEditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SnipFacetBodyBuilder.IsSnipNearFacets </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SnipFacetBodyBuilder.ProjectBothSides </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SnipFacetBodyBuilder.RegionsOption </term> <description> 
##  
## RemoveSelected </description> </item> 
## 
## <item><term> 
##  
## ThinFacets </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ToleranceFactor </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class CleanupFacetBodyWizardBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.CleanupFacetBodyWizardBuilder</ja_class> builder. 
    It removes defects that are present in the surfaces of the bodies selected. 
    """


    ##  These provide fill type after region removal
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Linear</term><description> 
    ## </description> </item><item><term> 
    ## Refined</term><description> 
    ## </description> </item><item><term> 
    ## TangentBased</term><description> 
    ## </description> </item><item><term> 
    ## CurvatureBased</term><description> 
    ## </description> </item></list>
    class FillType(Enum):
        """
        Members Include: <NotSet> <Linear> <Refined> <TangentBased> <CurvatureBased>
        """
        NotSet: int
        Linear: int
        Refined: int
        TangentBased: int
        CurvatureBased: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CleanupFacetBodyWizardBuilder.FillType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  These represent the options for removing regions
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ByRegion</term><description> 
    ## </description> </item><item><term> 
    ## ByDefectMarkup</term><description> 
    ## </description> </item></list>
    class JaCleanupFacetBodyBuilderRegionremoveoption(Enum):
        """
        Members Include: <ByRegion> <ByDefectMarkup>
        """
        ByRegion: int
        ByDefectMarkup: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CleanupFacetBodyWizardBuilder.FillType NXOpen.Facet.CleanupFacetBodyWizardBuilder.FillType@endlink) AutomaticFillType
    ##  Returns the automatic fill type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return CleanupFacetBodyWizardBuilder.FillType
    @property
    def AutomaticFillType(self) -> CleanupFacetBodyWizardBuilder.FillType:
        """
        Getter for property: (@link CleanupFacetBodyWizardBuilder.FillType NXOpen.Facet.CleanupFacetBodyWizardBuilder.FillType@endlink) AutomaticFillType
         Returns the automatic fill type   
            
         
        """
        pass
    
    ## Setter for property: (@link CleanupFacetBodyWizardBuilder.FillType NXOpen.Facet.CleanupFacetBodyWizardBuilder.FillType@endlink) AutomaticFillType

    ##  Returns the automatic fill type   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AutomaticFillType.setter
    def AutomaticFillType(self, automaticFillType: CleanupFacetBodyWizardBuilder.FillType):
        """
        Setter for property: (@link CleanupFacetBodyWizardBuilder.FillType NXOpen.Facet.CleanupFacetBodyWizardBuilder.FillType@endlink) AutomaticFillType
         Returns the automatic fill type   
            
         
        """
        pass
    
    ## Getter for property: (int) CircumferenceRings
    ##  Returns the circumference rings   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def CircumferenceRings(self) -> int:
        """
        Getter for property: (int) CircumferenceRings
         Returns the circumference rings   
            
         
        """
        pass
    
    ## Setter for property: (int) CircumferenceRings

    ##  Returns the circumference rings   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CircumferenceRings.setter
    def CircumferenceRings(self, circumferenceRings: int):
        """
        Setter for property: (int) CircumferenceRings
         Returns the circumference rings   
            
         
        """
        pass
    
    ## Getter for property: (@link CleanupFacetBodyBuilder NXOpen.Facet.CleanupFacetBodyBuilder@endlink) CleanupFacetBodyBuilder
    ##  Returns the cleanup Facet   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return CleanupFacetBodyBuilder
    @property
    def CleanupFacetBodyBuilder(self) -> CleanupFacetBodyBuilder:
        """
        Getter for property: (@link CleanupFacetBodyBuilder NXOpen.Facet.CleanupFacetBodyBuilder@endlink) CleanupFacetBodyBuilder
         Returns the cleanup Facet   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
    ##  Returns the collector of facets to be remove.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns the collector of facets to be remove.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector

    ##  Returns the collector of facets to be remove.  
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @FacetCollector.setter
    def FacetCollector(self, collector: NXOpen.FacetCollector):
        """
        Setter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns the collector of facets to be remove.  
            
         
        """
        pass
    
    ## Getter for property: (@link FillMeshBuilder NXOpen.Facet.FillMeshBuilder@endlink) FillMesh
    ##  Returns the Fill Mesh   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return FillMeshBuilder
    @property
    def FillMesh(self) -> FillMeshBuilder:
        """
        Getter for property: (@link FillMeshBuilder NXOpen.Facet.FillMeshBuilder@endlink) FillMesh
         Returns the Fill Mesh   
            
         
        """
        pass
    
    ## Getter for property: (bool) FoldedEdges
    ##  Returns the folded edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def FoldedEdges(self) -> bool:
        """
        Getter for property: (bool) FoldedEdges
         Returns the folded edges   
            
         
        """
        pass
    
    ## Setter for property: (bool) FoldedEdges

    ##  Returns the folded edges   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @FoldedEdges.setter
    def FoldedEdges(self, foldedEdges: bool):
        """
        Setter for property: (bool) FoldedEdges
         Returns the folded edges   
            
         
        """
        pass
    
    ## Getter for property: (bool) InconsistentNormals
    ##  Returns the inconsistent normals   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def InconsistentNormals(self) -> bool:
        """
        Getter for property: (bool) InconsistentNormals
         Returns the inconsistent normals   
            
         
        """
        pass
    
    ## Setter for property: (bool) InconsistentNormals

    ##  Returns the inconsistent normals   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @InconsistentNormals.setter
    def InconsistentNormals(self, inconsistentNormals: bool):
        """
        Setter for property: (bool) InconsistentNormals
         Returns the inconsistent normals   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) InputBodies
    ##  Returns the input bodies.  
    ##    For convergent bodies having associative feature can not be edited. Use CreateCopiesToEdit API to create copies   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def InputBodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) InputBodies
         Returns the input bodies.  
           For convergent bodies having associative feature can not be edited. Use CreateCopiesToEdit API to create copies   
         
        """
        pass
    
    ## Getter for property: (bool) LaminarSlits
    ##  Returns the laminar slits   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def LaminarSlits(self) -> bool:
        """
        Getter for property: (bool) LaminarSlits
         Returns the laminar slits   
            
         
        """
        pass
    
    ## Setter for property: (bool) LaminarSlits

    ##  Returns the laminar slits   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LaminarSlits.setter
    def LaminarSlits(self, laminarSlits: bool):
        """
        Setter for property: (bool) LaminarSlits
         Returns the laminar slits   
            
         
        """
        pass
    
    ## Getter for property: (float) MinAngleFoldedFacets
    ##  Returns the min angle folded facets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def MinAngleFoldedFacets(self) -> float:
        """
        Getter for property: (float) MinAngleFoldedFacets
         Returns the min angle folded facets   
            
         
        """
        pass
    
    ## Setter for property: (float) MinAngleFoldedFacets

    ##  Returns the min angle folded facets   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MinAngleFoldedFacets.setter
    def MinAngleFoldedFacets(self, minAngleFoldedFacets: float):
        """
        Setter for property: (float) MinAngleFoldedFacets
         Returns the min angle folded facets   
            
         
        """
        pass
    
    ## Getter for property: (int) MinFacetNumberPerBody
    ##  Returns the min facet number per body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def MinFacetNumberPerBody(self) -> int:
        """
        Getter for property: (int) MinFacetNumberPerBody
         Returns the min facet number per body   
            
         
        """
        pass
    
    ## Setter for property: (int) MinFacetNumberPerBody

    ##  Returns the min facet number per body   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MinFacetNumberPerBody.setter
    def MinFacetNumberPerBody(self, minFacetNumberPerBody: int):
        """
        Setter for property: (int) MinFacetNumberPerBody
         Returns the min facet number per body   
            
         
        """
        pass
    
    ## Getter for property: (bool) QualityIndex
    ##  Returns the quality index   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def QualityIndex(self) -> bool:
        """
        Getter for property: (bool) QualityIndex
         Returns the quality index   
            
         
        """
        pass
    
    ## Setter for property: (bool) QualityIndex

    ##  Returns the quality index   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @QualityIndex.setter
    def QualityIndex(self, qualityIndex: bool):
        """
        Setter for property: (bool) QualityIndex
         Returns the quality index   
            
         
        """
        pass
    
    ## Getter for property: (@link CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption NXOpen.Facet.CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption@endlink) RegionRemoveOption
    ##  Returns the region remove option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption
    @property
    def RegionRemoveOption(self) -> CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption:
        """
        Getter for property: (@link CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption NXOpen.Facet.CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption@endlink) RegionRemoveOption
         Returns the region remove option   
            
         
        """
        pass
    
    ## Setter for property: (@link CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption NXOpen.Facet.CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption@endlink) RegionRemoveOption

    ##  Returns the region remove option   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RegionRemoveOption.setter
    def RegionRemoveOption(self, regionRemoveOption: CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption):
        """
        Setter for property: (@link CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption NXOpen.Facet.CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption@endlink) RegionRemoveOption
         Returns the region remove option   
            
         
        """
        pass
    
    ## Getter for property: (bool) SelfIntersections
    ##  Returns the self intersections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def SelfIntersections(self) -> bool:
        """
        Getter for property: (bool) SelfIntersections
         Returns the self intersections   
            
         
        """
        pass
    
    ## Setter for property: (bool) SelfIntersections

    ##  Returns the self intersections   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SelfIntersections.setter
    def SelfIntersections(self, selfIntersections: bool):
        """
        Setter for property: (bool) SelfIntersections
         Returns the self intersections   
            
         
        """
        pass
    
    ## Getter for property: (@link SnipFacetBodyBuilder NXOpen.Facet.SnipFacetBodyBuilder@endlink) SnipFacetBodyBuilder
    ##  Returns the snip Facet  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return SnipFacetBodyBuilder
    @property
    def SnipFacetBodyBuilder(self) -> SnipFacetBodyBuilder:
        """
        Getter for property: (@link SnipFacetBodyBuilder NXOpen.Facet.SnipFacetBodyBuilder@endlink) SnipFacetBodyBuilder
         Returns the snip Facet  
            
         
        """
        pass
    
    ## Getter for property: (bool) ThinFacets
    ##  Returns the thin facets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ThinFacets(self) -> bool:
        """
        Getter for property: (bool) ThinFacets
         Returns the thin facets   
            
         
        """
        pass
    
    ## Setter for property: (bool) ThinFacets

    ##  Returns the thin facets   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ThinFacets.setter
    def ThinFacets(self, thinFacets: bool):
        """
        Setter for property: (bool) ThinFacets
         Returns the thin facets   
            
         
        """
        pass
    
    ## Getter for property: (float) ToleranceFactor
    ##  Returns the tolerance factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def ToleranceFactor(self) -> float:
        """
        Getter for property: (float) ToleranceFactor
         Returns the tolerance factor   
            
         
        """
        pass
    
    ## Setter for property: (float) ToleranceFactor

    ##  Returns the tolerance factor   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ToleranceFactor.setter
    def ToleranceFactor(self, toleranceFactor: float):
        """
        Setter for property: (float) ToleranceFactor
         Returns the tolerance factor   
            
         
        """
        pass
    
    ##  The analyze 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def Analyze(self) -> None:
        """
         The analyze 
        """
        pass
    
    ##  Create copies of Associative convergent bodies. Return 1 if copies created 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateCopiesToEdit(self) -> None:
        """
         Create copies of Associative convergent bodies. Return 1 if copies created 
        """
        pass
    
    ##  The Fill hole button 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def FillHole(self) -> None:
        """
         The Fill hole button 
        """
        pass
    
    ##  Remove facet 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def RemoveFacets(self) -> None:
        """
         Remove facet 
        """
        pass
    
    ##  The repair 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def Repair(self) -> None:
        """
         The repair 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Facet::CombineFacetBodiesBuilder NXOpen::Facet::CombineFacetBodiesBuilder@endlink 
##         Merges multiple convergent bodies by averaging the meshes in the overlapping zones.  <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateCombineFacetBodiesBuilder  NXOpen::Facet::FacetModelingCollection::CreateCombineFacetBodiesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AnalyzeMeshQuality </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class CombineFacetBodiesBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Facet.CombineFacetBodiesBuilder</ja_class>
        Merges multiple convergent bodies by averaging the meshes in the overlapping zones. """


    ##  The options indicating action to be taken for input bodies after combine operation is performed 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Delete</term><description> 
    ## </description> </item><item><term> 
    ## Keep</term><description> 
    ## </description> </item><item><term> 
    ## Hide</term><description> 
    ## </description> </item></list>
    class InputBodiesOption(Enum):
        """
        Members Include: <Delete> <Keep> <Hide>
        """
        Delete: int
        Keep: int
        Hide: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CombineFacetBodiesBuilder.InputBodiesOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AnalyzeMeshQuality
    ##  Returns the value used to determine if analyzing the quality of the mesh or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def AnalyzeMeshQuality(self) -> bool:
        """
        Getter for property: (bool) AnalyzeMeshQuality
         Returns the value used to determine if analyzing the quality of the mesh or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AnalyzeMeshQuality

    ##  Returns the value used to determine if analyzing the quality of the mesh or not.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AnalyzeMeshQuality.setter
    def AnalyzeMeshQuality(self, analyzeMeshQuality: bool):
        """
        Setter for property: (bool) AnalyzeMeshQuality
         Returns the value used to determine if analyzing the quality of the mesh or not.  
             
         
        """
        pass
    
    ## Getter for property: (float) AverageFacetSize
    ##  Returns the parameter used to control the average size of the output triangulation.  
    ##   
    ##             The value is also used as a threshold to determine overlapping of the two bodies.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def AverageFacetSize(self) -> float:
        """
        Getter for property: (float) AverageFacetSize
         Returns the parameter used to control the average size of the output triangulation.  
          
                    The value is also used as a threshold to determine overlapping of the two bodies.   
         
        """
        pass
    
    ## Setter for property: (float) AverageFacetSize

    ##  Returns the parameter used to control the average size of the output triangulation.  
    ##   
    ##             The value is also used as a threshold to determine overlapping of the two bodies.   
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AverageFacetSize.setter
    def AverageFacetSize(self, averageFacetSize: float):
        """
        Setter for property: (float) AverageFacetSize
         Returns the parameter used to control the average size of the output triangulation.  
          
                    The value is also used as a threshold to determine overlapping of the two bodies.   
         
        """
        pass
    
    ## Getter for property: (@link CombineFacetBodiesBuilder.InputBodiesOption NXOpen.Facet.CombineFacetBodiesBuilder.InputBodiesOption@endlink) InputBodiesOptions
    ##  Returns the option indicating action to be taken for input bodies after combine operation is performed.  
    ##   
    ##         the builder is committed.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return CombineFacetBodiesBuilder.InputBodiesOption
    @property
    def InputBodiesOptions(self) -> CombineFacetBodiesBuilder.InputBodiesOption:
        """
        Getter for property: (@link CombineFacetBodiesBuilder.InputBodiesOption NXOpen.Facet.CombineFacetBodiesBuilder.InputBodiesOption@endlink) InputBodiesOptions
         Returns the option indicating action to be taken for input bodies after combine operation is performed.  
          
                the builder is committed.  
         
        """
        pass
    
    ## Setter for property: (@link CombineFacetBodiesBuilder.InputBodiesOption NXOpen.Facet.CombineFacetBodiesBuilder.InputBodiesOption@endlink) InputBodiesOptions

    ##  Returns the option indicating action to be taken for input bodies after combine operation is performed.  
    ##   
    ##         the builder is committed.  
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @InputBodiesOptions.setter
    def InputBodiesOptions(self, inputBodiesOptions: CombineFacetBodiesBuilder.InputBodiesOption):
        """
        Setter for property: (@link CombineFacetBodiesBuilder.InputBodiesOption NXOpen.Facet.CombineFacetBodiesBuilder.InputBodiesOption@endlink) InputBodiesOptions
         Returns the option indicating action to be taken for input bodies after combine operation is performed.  
          
                the builder is committed.  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) InputFacetBodies
    ##  Returns the input facet bodies.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def InputFacetBodies(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) InputFacetBodies
         Returns the input facet bodies.  
             
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::CombineFacetBodyBuilder NXOpen::Facet::CombineFacetBodyBuilder@endlink  builder. 
##     It combines the facet bodies to one facet body. The original inputs are deleted.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateCombineFacetBodyBuilder  NXOpen::Facet::FacetModelingCollection::CreateCombineFacetBodyBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class CombineFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.CombineFacetBodyBuilder</ja_class> builder. 
    It combines the facet bodies to one facet body. The original inputs are deleted.
    """


    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) FacetedBodiesToCombine
    ##  Returns the faceted bodies to combine   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def FacetedBodiesToCombine(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) FacetedBodiesToCombine
         Returns the faceted bodies to combine   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::ConvertFacetBodyBuilder NXOpen::Facet::ConvertFacetBodyBuilder@endlink  builder. 
##     It converts the selected NX facet bodies to Convergent bodies or JT bodies, and converts JT facet bodies 
##     to Convergent bodies or NX facets bodies. The original inputs can be deleted, kept, or hidden.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateConvertFacetBodyBuilder  NXOpen::Facet::FacetModelingCollection::CreateConvertFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MinimumAngleFoldedFacets </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## MinimumFacetNumber </term> <description> 
##  
## 100 </description> </item> 
## 
## <item><term> 
##  
## OriginalBodyOption </term> <description> 
##  
## Delete </description> </item> 
## 
## <item><term> 
##  
## OutputType </term> <description> 
##  
## ConvergentBody </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class ConvertFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.ConvertFacetBodyBuilder</ja_class> builder. 
    It converts the selected NX facet bodies to Convergent bodies or JT bodies, and converts JT facet bodies 
    to Convergent bodies or NX facets bodies. The original inputs can be deleted, kept, or hidden.
    """


    ##  These represent the options for handling the input facet bodies  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Keep</term><description> 
    ##  Keep original body </description> </item><item><term> 
    ## Hide</term><description> 
    ##  Hide original body </description> </item><item><term> 
    ## Delete</term><description> 
    ##  Delete original body </description> </item></list>
    class OriginalBodyOptions(Enum):
        """
        Members Include: <Keep> <Hide> <Delete>
        """
        Keep: int
        Hide: int
        Delete: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConvertFacetBodyBuilder.OriginalBodyOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  These options represent the type of output facet body 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ConvergentBody</term><description> 
    ##  Convert To Convergent bodies </description> </item><item><term> 
    ## NXFacetBody</term><description> 
    ##  Convert to NX Facet bodies </description> </item><item><term> 
    ## JTFacetBody</term><description> 
    ##  Convert To JT Facet bodies </description> </item></list>
    class OutputTypes(Enum):
        """
        Members Include: <ConvergentBody> <NXFacetBody> <JTFacetBody>
        """
        ConvergentBody: int
        NXFacetBody: int
        JTFacetBody: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConvertFacetBodyBuilder.OutputTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CleanUp
    ##  Returns an option for automatically repairing the converted PSM mesh   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def CleanUp(self) -> bool:
        """
        Getter for property: (bool) CleanUp
         Returns an option for automatically repairing the converted PSM mesh   
            
         
        """
        pass
    
    ## Setter for property: (bool) CleanUp

    ##  Returns an option for automatically repairing the converted PSM mesh   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CleanUp.setter
    def CleanUp(self, cleanUp: bool):
        """
        Setter for property: (bool) CleanUp
         Returns an option for automatically repairing the converted PSM mesh   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) FacetedBodiesToConvert
    ##  Returns the input facet bodies to convert   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def FacetedBodiesToConvert(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) FacetedBodiesToConvert
         Returns the input facet bodies to convert   
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumAngleFoldedFacets
    ##  Returns the minimum angle between adjacent facets to define folded facets.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def MinimumAngleFoldedFacets(self) -> float:
        """
        Getter for property: (float) MinimumAngleFoldedFacets
         Returns the minimum angle between adjacent facets to define folded facets.  
             
         
        """
        pass
    
    ## Setter for property: (float) MinimumAngleFoldedFacets

    ##  Returns the minimum angle between adjacent facets to define folded facets.  
    ##      
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MinimumAngleFoldedFacets.setter
    def MinimumAngleFoldedFacets(self, minimumAngleFoldedFacets: float):
        """
        Setter for property: (float) MinimumAngleFoldedFacets
         Returns the minimum angle between adjacent facets to define folded facets.  
             
         
        """
        pass
    
    ## Getter for property: (int) MinimumFacetNumber
    ##  Returns the minimum number of facets to create output body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return int
    @property
    def MinimumFacetNumber(self) -> int:
        """
        Getter for property: (int) MinimumFacetNumber
         Returns the minimum number of facets to create output body.  
             
         
        """
        pass
    
    ## Setter for property: (int) MinimumFacetNumber

    ##  Returns the minimum number of facets to create output body.  
    ##      
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @MinimumFacetNumber.setter
    def MinimumFacetNumber(self, minimumFacetNumber: int):
        """
        Setter for property: (int) MinimumFacetNumber
         Returns the minimum number of facets to create output body.  
             
         
        """
        pass
    
    ## Getter for property: (@link ConvertFacetBodyBuilder.OriginalBodyOptions NXOpen.Facet.ConvertFacetBodyBuilder.OriginalBodyOptions@endlink) OriginalBodyOption
    ##  Returns the option for handling the input facet bodies   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return ConvertFacetBodyBuilder.OriginalBodyOptions
    @property
    def OriginalBodyOption(self) -> ConvertFacetBodyBuilder.OriginalBodyOptions:
        """
        Getter for property: (@link ConvertFacetBodyBuilder.OriginalBodyOptions NXOpen.Facet.ConvertFacetBodyBuilder.OriginalBodyOptions@endlink) OriginalBodyOption
         Returns the option for handling the input facet bodies   
            
         
        """
        pass
    
    ## Setter for property: (@link ConvertFacetBodyBuilder.OriginalBodyOptions NXOpen.Facet.ConvertFacetBodyBuilder.OriginalBodyOptions@endlink) OriginalBodyOption

    ##  Returns the option for handling the input facet bodies   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @OriginalBodyOption.setter
    def OriginalBodyOption(self, enumOriginalBodyOption: ConvertFacetBodyBuilder.OriginalBodyOptions):
        """
        Setter for property: (@link ConvertFacetBodyBuilder.OriginalBodyOptions NXOpen.Facet.ConvertFacetBodyBuilder.OriginalBodyOptions@endlink) OriginalBodyOption
         Returns the option for handling the input facet bodies   
            
         
        """
        pass
    
    ## Getter for property: (@link ConvertFacetBodyBuilder.OutputTypes NXOpen.Facet.ConvertFacetBodyBuilder.OutputTypes@endlink) OutputType
    ##  Returns the output type of converted facet body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ConvertFacetBodyBuilder.OutputTypes
    @property
    def OutputType(self) -> ConvertFacetBodyBuilder.OutputTypes:
        """
        Getter for property: (@link ConvertFacetBodyBuilder.OutputTypes NXOpen.Facet.ConvertFacetBodyBuilder.OutputTypes@endlink) OutputType
         Returns the output type of converted facet body   
            
         
        """
        pass
    
    ## Setter for property: (@link ConvertFacetBodyBuilder.OutputTypes NXOpen.Facet.ConvertFacetBodyBuilder.OutputTypes@endlink) OutputType

    ##  Returns the output type of converted facet body   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @OutputType.setter
    def OutputType(self, enumOutputType: ConvertFacetBodyBuilder.OutputTypes):
        """
        Setter for property: (@link ConvertFacetBodyBuilder.OutputTypes NXOpen.Facet.ConvertFacetBodyBuilder.OutputTypes@endlink) OutputType
         Returns the output type of converted facet body   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##        Represents a @link NXOpen::Facet::CreateTransitionBuilder NXOpen::Facet::CreateTransitionBuilder@endlink  builder. 
##        This class creates the blend/chamfer of a facet body.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateCreateTransitionBuilder  NXOpen::Facet::FacetModelingCollection::CreateCreateTransitionBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Distance.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## IsClosed </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsEditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Radius.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX12.0.0  <br> 

class CreateTransitionBuilder(NXOpen.Builder): 
    """
       Represents a <ja_class>NXOpen.Facet.CreateTransitionBuilder</ja_class> builder. 
       This class creates the blend/chamfer of a facet body.
    """


    ##  the transition type. The round type creates fillet type transition. The flat type creates chamfer type transition. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Round</term><description> 
    ## </description> </item><item><term> 
    ## Flat</term><description> 
    ## </description> </item></list>
    class Types(Enum):
        """
        Members Include: <Round> <Flat>
        """
        Round: int
        Flat: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CreateTransitionBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Distance
    ##  Returns the distance.  
    ##    This value is for chamfer operation.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Distance
         Returns the distance.  
           This value is for chamfer operation.   
         
        """
        pass
    
    ## Getter for property: (bool) IsClosed
    ##  Returns the is closed.  
    ##    The flag indicate if the edge is closed or not.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsClosed(self) -> bool:
        """
        Getter for property: (bool) IsClosed
         Returns the is closed.  
           The flag indicate if the edge is closed or not.   
         
        """
        pass
    
    ## Setter for property: (bool) IsClosed

    ##  Returns the is closed.  
    ##    The flag indicate if the edge is closed or not.   
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsClosed.setter
    def IsClosed(self, isClosed: bool):
        """
        Setter for property: (bool) IsClosed
         Returns the is closed.  
           The flag indicate if the edge is closed or not.   
         
        """
        pass
    
    ## Getter for property: (bool) IsEditCopy
    ##  Returns the flag indicating if the transition is created on the copy of the input facet body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the flag indicating if the transition is created on the copy of the input facet body.  
             
         
        """
        pass
    
    ## Setter for property: (bool) IsEditCopy

    ##  Returns the flag indicating if the transition is created on the copy of the input facet body.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the flag indicating if the transition is created on the copy of the input facet body.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Radius
    ##  Returns the radius.  
    ##    This value is for blend operation.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Radius
         Returns the radius.  
           This value is for blend operation.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) SelectedBody
    ##  Returns the selected facet body.  
    ##    It could be a convergent object.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.DisplayableObject
    @property
    def SelectedBody(self) -> NXOpen.DisplayableObject:
        """
        Getter for property: (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) SelectedBody
         Returns the selected facet body.  
           It could be a convergent object.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) SelectedBody

    ##  Returns the selected facet body.  
    ##    It could be a convergent object.   
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SelectedBody.setter
    def SelectedBody(self, selectedBody: NXOpen.DisplayableObject):
        """
        Setter for property: (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) SelectedBody
         Returns the selected facet body.  
           It could be a convergent object.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) SelectedPoints
    ##  Returns the selected points.  
    ##    The points will define the edge which needs blend/chamfer.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def SelectedPoints(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) SelectedPoints
         Returns the selected points.  
           The points will define the edge which needs blend/chamfer.   
         
        """
        pass
    
    ## Getter for property: (@link CreateTransitionBuilder.Types NXOpen.Facet.CreateTransitionBuilder.Types@endlink) Type
    ##  Returns the type.  
    ##    This value defines the transition type.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CreateTransitionBuilder.Types
    @property
    def Type(self) -> CreateTransitionBuilder.Types:
        """
        Getter for property: (@link CreateTransitionBuilder.Types NXOpen.Facet.CreateTransitionBuilder.Types@endlink) Type
         Returns the type.  
           This value defines the transition type.   
         
        """
        pass
    
    ## Setter for property: (@link CreateTransitionBuilder.Types NXOpen.Facet.CreateTransitionBuilder.Types@endlink) Type

    ##  Returns the type.  
    ##    This value defines the transition type.   
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Type.setter
    def Type(self, type: CreateTransitionBuilder.Types):
        """
        Setter for property: (@link CreateTransitionBuilder.Types NXOpen.Facet.CreateTransitionBuilder.Types@endlink) Type
         Returns the type.  
           This value defines the transition type.   
         
        """
        pass
    
import NXOpen
## 
##        Represents a @link NXOpen::Facet::CurvatureBuilder NXOpen::Facet::CurvatureBuilder@endlink .
##        It calculates the maximum absolute principal curvature on facet
##        bodies and creates a color map of these values.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateFacetCurvatureBuilder  NXOpen::Facet::FacetedBodyCollection::CreateFacetCurvatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class CurvatureBuilder(NXOpen.Builder): 
    """
       Represents a <ja_class>NXOpen.Facet.CurvatureBuilder</ja_class>.
       It calculates the maximum absolute principal curvature on facet
       bodies and creates a color map of these values.
    """


    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Bodies
    ##  Returns the input facet body list.  
    ##    Inputs to this command can be convergent objects.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Bodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Bodies
         Returns the input facet body list.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    
    ## Getter for property: (float) ConcaveRadius
    ##  Returns the concave radius threshold   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def ConcaveRadius(self) -> float:
        """
        Getter for property: (float) ConcaveRadius
         Returns the concave radius threshold   
            
         
        """
        pass
    
    ## Setter for property: (float) ConcaveRadius

    ##  Returns the concave radius threshold   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ConcaveRadius.setter
    def ConcaveRadius(self, concave_radius: float):
        """
        Setter for property: (float) ConcaveRadius
         Returns the concave radius threshold   
            
         
        """
        pass
    
    ## Getter for property: (float) ConvexRadius
    ##  Returns the convex radius threshold   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def ConvexRadius(self) -> float:
        """
        Getter for property: (float) ConvexRadius
         Returns the convex radius threshold   
            
         
        """
        pass
    
    ## Setter for property: (float) ConvexRadius

    ##  Returns the convex radius threshold   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ConvexRadius.setter
    def ConvexRadius(self, convex_radius: float):
        """
        Setter for property: (float) ConvexRadius
         Returns the convex radius threshold   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) FacetBodies
    ##  Returns the input facet body list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Facet::CurvatureBuilder::Bodies NXOpen::Facet::CurvatureBuilder::Bodies@endlink  instead.  <br> 

    ## @return SelectFacetedBodyList
    @property
    def FacetBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) FacetBodies
         Returns the input facet body list   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsDirectionReversed
    ##  Returns the reverse direction option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def IsDirectionReversed(self) -> bool:
        """
        Getter for property: (bool) IsDirectionReversed
         Returns the reverse direction option   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsDirectionReversed

    ##  Returns the reverse direction option   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @IsDirectionReversed.setter
    def IsDirectionReversed(self, direction_reversed: bool):
        """
        Setter for property: (bool) IsDirectionReversed
         Returns the reverse direction option   
            
         
        """
        pass
    
    ## Getter for property: (float) SmoothingFactor
    ##  Returns the smoothing factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def SmoothingFactor(self) -> float:
        """
        Getter for property: (float) SmoothingFactor
         Returns the smoothing factor   
            
         
        """
        pass
    
    ## Setter for property: (float) SmoothingFactor

    ##  Returns the smoothing factor   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SmoothingFactor.setter
    def SmoothingFactor(self, smoothing_factor: float):
        """
        Setter for property: (float) SmoothingFactor
         Returns the smoothing factor   
            
         
        """
        pass
    
    ##  Deletes the curvature data associated with the input facet bodies.
    ##             Call this method in order to save memory if the curvature data are not needed any more.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def DeleteCurvature(self) -> None:
        """
         Deletes the curvature data associated with the input facet bodies.
                    Call this method in order to save memory if the curvature data are not needed any more.
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Facet::DecimateFacetBodyBuilder NXOpen::Facet::DecimateFacetBodyBuilder@endlink .
##     Decimate Body Builder is a function to facilitate the reduction of data by reducing the density of facets while keeping the general shape in tact.
##     Three different methods are provided to reduce the data.  <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateDecimateFacetBodyBuilder  NXOpen::Facet::FacetedBodyCollection::CreateDecimateFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AngleThreshold </term> <description> 
##  
## 15 </description> </item> 
## 
## <item><term> 
##  
## DecimateMethod </term> <description> 
##  
## ChordalDeviation </description> </item> 
## 
## <item><term> 
##  
## IsEditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsLockBoundary </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## MinimumArea </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Percentage </term> <description> 
##  
## 10 </description> </item> 
## 
## <item><term> 
##  
## Tolerance </term> <description> 
##  
## 0.25 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class DecimateFacetBodyBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Facet.DecimateFacetBodyBuilder</ja_class>.
    Decimate Body Builder is a function to facilitate the reduction of data by reducing the density of facets while keeping the general shape in tact.
    Three different methods are provided to reduce the data. """


    ##  Decimate Method 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ChordalDeviation</term><description> 
    ##  Chordal deviation reduces the number of facets by removing facets which do not effect the overall accuracy of the mesh.</description> </item><item><term> 
    ## SmallestFacet</term><description> 
    ##  Smallest facet removes all facets smaller than the defined area, thus removing facets deemed to be redundant by the designer.</description> </item><item><term> 
    ## Percentage</term><description> 
    ##  Percentage option allows the user to reduce the facet count by overall percentage.</description> </item></list>
    class DecimateMethodType(Enum):
        """
        Members Include: <ChordalDeviation> <SmallestFacet> <Percentage>
        """
        ChordalDeviation: int
        SmallestFacet: int
        Percentage: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DecimateFacetBodyBuilder.DecimateMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) AngleThreshold
    ##  Returns the value indicating maximum angle, where any facets with a larger relative angle are not reduced.  
    ##   
    ##             This allows sharp edges to be retained.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def AngleThreshold(self) -> float:
        """
        Getter for property: (float) AngleThreshold
         Returns the value indicating maximum angle, where any facets with a larger relative angle are not reduced.  
          
                    This allows sharp edges to be retained.   
         
        """
        pass
    
    ## Setter for property: (float) AngleThreshold

    ##  Returns the value indicating maximum angle, where any facets with a larger relative angle are not reduced.  
    ##   
    ##             This allows sharp edges to be retained.   
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @AngleThreshold.setter
    def AngleThreshold(self, angleThreshold: float):
        """
        Setter for property: (float) AngleThreshold
         Returns the value indicating maximum angle, where any facets with a larger relative angle are not reduced.  
          
                    This allows sharp edges to be retained.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Bodies
    ##  Returns the facet bodies to be decimated.  
    ##    Inputs to this command can be convergent objects.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::Facet::SubdivideFacetBodyBuilder::FacetCollector NXOpen::Facet::SubdivideFacetBodyBuilder::FacetCollector@endlink  instead.  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Bodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Bodies
         Returns the facet bodies to be decimated.  
           Inputs to this command can be convergent objects.  
         
        """
        pass
    
    ## Getter for property: (@link DecimateFacetBodyBuilder.DecimateMethodType NXOpen.Facet.DecimateFacetBodyBuilder.DecimateMethodType@endlink) DecimateMethod
    ##  Returns the decimation method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return DecimateFacetBodyBuilder.DecimateMethodType
    @property
    def DecimateMethod(self) -> DecimateFacetBodyBuilder.DecimateMethodType:
        """
        Getter for property: (@link DecimateFacetBodyBuilder.DecimateMethodType NXOpen.Facet.DecimateFacetBodyBuilder.DecimateMethodType@endlink) DecimateMethod
         Returns the decimation method   
            
         
        """
        pass
    
    ## Setter for property: (@link DecimateFacetBodyBuilder.DecimateMethodType NXOpen.Facet.DecimateFacetBodyBuilder.DecimateMethodType@endlink) DecimateMethod

    ##  Returns the decimation method   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @DecimateMethod.setter
    def DecimateMethod(self, decimateMethod: DecimateFacetBodyBuilder.DecimateMethodType):
        """
        Setter for property: (@link DecimateFacetBodyBuilder.DecimateMethodType NXOpen.Facet.DecimateFacetBodyBuilder.DecimateMethodType@endlink) DecimateMethod
         Returns the decimation method   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) FacetBodies
    ##  Returns the facet bodies to be decimated   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Facet::DecimateFacetBodyBuilder::Bodies NXOpen::Facet::DecimateFacetBodyBuilder::Bodies@endlink  instead.  <br> 

    ## @return SelectFacetedBodyList
    @property
    def FacetBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) FacetBodies
         Returns the facet bodies to be decimated   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
    ##  Returns a collector of facets on the facet bodies to be decimated.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns a collector of facets on the facet bodies to be decimated.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector

    ##  Returns a collector of facets on the facet bodies to be decimated.  
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FacetCollector.setter
    def FacetCollector(self, collector: NXOpen.FacetCollector):
        """
        Setter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns a collector of facets on the facet bodies to be decimated.  
            
         
        """
        pass
    
    ## Getter for property: (bool) IsEditCopy
    ##  Returns the value indicating if a copy of the facet body to be decimated without altering the original   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be decimated without altering the original   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsEditCopy

    ##  Returns the value indicating if a copy of the facet body to be decimated without altering the original   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be decimated without altering the original   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsLockBoundary
    ##  Returns the value indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def IsLockBoundary(self) -> bool:
        """
        Getter for property: (bool) IsLockBoundary
         Returns the value indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsLockBoundary

    ##  Returns the value indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @IsLockBoundary.setter
    def IsLockBoundary(self, isLockBoundary: bool):
        """
        Setter for property: (bool) IsLockBoundary
         Returns the value indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact   
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumArea
    ##  Returns the value indicating area of the smallest facet that is to be retained.  
    ##    All the facets
    ##             smaller than the minimum area are removed. This value is used when
    ##             @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType@endlink  is
    ##             @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeSmallestFacet NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeSmallestFacet@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def MinimumArea(self) -> float:
        """
        Getter for property: (float) MinimumArea
         Returns the value indicating area of the smallest facet that is to be retained.  
           All the facets
                    smaller than the minimum area are removed. This value is used when
                    @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType@endlink  is
                    @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeSmallestFacet NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeSmallestFacet@endlink .   
         
        """
        pass
    
    ## Setter for property: (float) MinimumArea

    ##  Returns the value indicating area of the smallest facet that is to be retained.  
    ##    All the facets
    ##             smaller than the minimum area are removed. This value is used when
    ##             @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType@endlink  is
    ##             @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeSmallestFacet NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeSmallestFacet@endlink .   
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @MinimumArea.setter
    def MinimumArea(self, minimumArea: float):
        """
        Setter for property: (float) MinimumArea
         Returns the value indicating area of the smallest facet that is to be retained.  
           All the facets
                    smaller than the minimum area are removed. This value is used when
                    @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType@endlink  is
                    @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeSmallestFacet NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeSmallestFacet@endlink .   
         
        """
        pass
    
    ## Getter for property: (float) Percentage
    ##  Returns the value indicating percentage by which facet count is to be reduced.  
    ##    This value is used when
    ##             @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType@endlink  is
    ##             @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypePercentage NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypePercentage@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def Percentage(self) -> float:
        """
        Getter for property: (float) Percentage
         Returns the value indicating percentage by which facet count is to be reduced.  
           This value is used when
                    @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType@endlink  is
                    @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypePercentage NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypePercentage@endlink .   
         
        """
        pass
    
    ## Setter for property: (float) Percentage

    ##  Returns the value indicating percentage by which facet count is to be reduced.  
    ##    This value is used when
    ##             @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType@endlink  is
    ##             @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypePercentage NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypePercentage@endlink .   
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Percentage.setter
    def Percentage(self, percentage: float):
        """
        Setter for property: (float) Percentage
         Returns the value indicating percentage by which facet count is to be reduced.  
           This value is used when
                    @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType@endlink  is
                    @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypePercentage NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypePercentage@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList@endlink) RegionList
    ##  Returns an optional list of regions on the facet bodies to be decimated.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::Facet::SubdivideFacetBodyBuilder::FacetCollector NXOpen::Facet::SubdivideFacetBodyBuilder::FacetCollector@endlink  instead.  <br> 

    ## @return NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList
    @property
    def RegionList(self) -> NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList@endlink) RegionList
         Returns an optional list of regions on the facet bodies to be decimated.  
             
         
        """
        pass
    
    ## Getter for property: (float) Tolerance
    ##  Returns the value indicating maximum chordal deviation from the original facet body.  
    ##    The value is used
    ##             when @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType@endlink  is
    ##             @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeChordalDeviation NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeChordalDeviation@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def Tolerance(self) -> float:
        """
        Getter for property: (float) Tolerance
         Returns the value indicating maximum chordal deviation from the original facet body.  
           The value is used
                    when @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType@endlink  is
                    @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeChordalDeviation NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeChordalDeviation@endlink .   
         
        """
        pass
    
    ## Setter for property: (float) Tolerance

    ##  Returns the value indicating maximum chordal deviation from the original facet body.  
    ##    The value is used
    ##             when @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType@endlink  is
    ##             @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeChordalDeviation NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeChordalDeviation@endlink .   
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Tolerance.setter
    def Tolerance(self, tolerance: float):
        """
        Setter for property: (float) Tolerance
         Returns the value indicating maximum chordal deviation from the original facet body.  
           The value is used
                    when @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType@endlink  is
                    @link NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeChordalDeviation NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeChordalDeviation@endlink .   
         
        """
        pass
    
import NXOpen
## 
##        This class manages the primitive shape detection for a facet body.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateDetectPrimitivesBuilder  NXOpen::Facet::FacetModelingCollection::CreateDetectPrimitivesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CurvatureSensitivity </term> <description> 
##  
## 20 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class DetectPrimitivesBuilder(NXOpen.Builder): 
    """
       This class manages the primitive shape detection for a facet body.
    """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BlendFactor
    ##  Returns the blend factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BlendFactor(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BlendFactor
         Returns the blend factor   
            
         
        """
        pass
    
    ## Getter for property: (int) CurvatureSensitivity
    ##  Returns the curvature sensitivity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def CurvatureSensitivity(self) -> int:
        """
        Getter for property: (int) CurvatureSensitivity
         Returns the curvature sensitivity   
            
         
        """
        pass
    
    ## Setter for property: (int) CurvatureSensitivity

    ##  Returns the curvature sensitivity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @CurvatureSensitivity.setter
    def CurvatureSensitivity(self, curvatureSensitivity: int):
        """
        Setter for property: (int) CurvatureSensitivity
         Returns the curvature sensitivity   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) FacetSelection
    ##  Returns the facet selection.  
    ##    Inputs to this command can be convergent objects.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def FacetSelection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) FacetSelection
         Returns the facet selection.  
           Inputs to this command can be convergent objects.  
         
        """
        pass
    
    ##  Adjust shape detection result with selectivity angle 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def AdjustShapeBoundary(self) -> None:
        """
         Adjust shape detection result with selectivity angle 
        """
        pass
    
    ##  Returns the blend color 
    ##  @return blendColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetBlendColor(self) -> List[float]:
        """
         Returns the blend color 
         @return blendColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Returns the cone color 
    ##  @return coneColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetConeColor(self) -> List[float]:
        """
         Returns the cone color 
         @return coneColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Returns the cylinder color 
    ##  @return cylinderColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetCylinderColor(self) -> List[float]:
        """
         Returns the cylinder color 
         @return cylinderColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Returns Other type of color. All non-primitive shapes are classfied as Other type 
    ##  @return otherColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetOtherColor(self) -> List[float]:
        """
         Returns Other type of color. All non-primitive shapes are classfied as Other type 
         @return otherColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Returns the plane color 
    ##  @return planeColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetPlaneColor(self) -> List[float]:
        """
         Returns the plane color 
         @return planeColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Returns the sphere color 
    ##  @return sphereColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetSphereColor(self) -> List[float]:
        """
         Returns the sphere color 
         @return sphereColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Sets the blend color 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="blendColor"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetBlendColor(self, blendColor: List[float]) -> None:
        """
         Sets the blend color 
        """
        pass
    
    ##  Sets the cone color 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="coneColor"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetConeColor(self, coneColor: List[float]) -> None:
        """
         Sets the cone color 
        """
        pass
    
    ##  Sets the cylinder color 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="cylinderColor"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetCylinderColor(self, cylinderColor: List[float]) -> None:
        """
         Sets the cylinder color 
        """
        pass
    
    ##  Sets the other color 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="otherColor"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetOtherColor(self, otherColor: List[float]) -> None:
        """
         Sets the other color 
        """
        pass
    
    ##  Sets the plane color 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="planeColor"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetPlaneColor(self, planeColor: List[float]) -> None:
        """
         Sets the plane color 
        """
        pass
    
    ##  Sets the sphere color 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sphereColor"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetSphereColor(self, sphereColor: List[float]) -> None:
        """
         Sets the sphere color 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Facet::DivideFacetFaceBuilder NXOpen::Facet::DivideFacetFaceBuilder@endlink .
##     Divide Facet Face Builder is a function to facilitate dividing of selected facet out of original facet face.  <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateDivideFacetFaceBuilder  NXOpen::Facet::FacetModelingCollection::CreateDivideFacetFaceBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Degree (deprecated) </term> <description> 
##  
## 3 </description> </item> 
## 
## <item><term> 
##  
## IsEditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Segments (deprecated) </term> <description> 
##  
## 50 </description> </item> 
## 
## <item><term> 
##  
## Type </term> <description> 
##  
## ByRegion </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX12.0.0  <br> 

class DivideFacetFaceBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Facet.DivideFacetFaceBuilder</ja_class>.
    Divide Facet Face Builder is a function to facilitate dividing of selected facet out of original facet face. """


    ##  Divide Facet Face type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ByColor</term><description> 
    ##  Divide Facet face based on colored facets </description> </item><item><term> 
    ## ByRegion</term><description> 
    ##  Divide Facet face based on selected regional facets </description> </item><item><term> 
    ## ByCurves</term><description> 
    ##  Divide Facet face based on split curves </description> </item></list>
    class DivideFacetTypes(Enum):
        """
        Members Include: <ByColor> <ByRegion> <ByCurves>
        """
        ByColor: int
        ByRegion: int
        ByCurves: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DivideFacetFaceBuilder.DivideFacetTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) Degree
    ##  Returns the polynomial degree (one unit less than the order).  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::Facet::DivideFacetFaceBuilder::IsSmoothEdge NXOpen::Facet::DivideFacetFaceBuilder::IsSmoothEdge@endlink  instead.  <br> 

    ## @return int
    @property
    def Degree(self) -> int:
        """
        Getter for property: (int) Degree
         Returns the polynomial degree (one unit less than the order).  
            
         
        """
        pass
    
    ## Setter for property: (int) Degree

    ##  Returns the polynomial degree (one unit less than the order).  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::Facet::DivideFacetFaceBuilder::SetSmoothEdge NXOpen::Facet::DivideFacetFaceBuilder::SetSmoothEdge@endlink  instead.  <br> 

    @Degree.setter
    def Degree(self, degree: int):
        """
        Setter for property: (int) Degree
         Returns the polynomial degree (one unit less than the order).  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FacetBodyCollector
    ##  Returns the collector for specifying facet bodies to be divided based on colored regions.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FacetBodyCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FacetBodyCollector
         Returns the collector for specifying facet bodies to be divided based on colored regions.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
    ##  Returns the collector for specifying facet regions  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns the collector for specifying facet regions  
            
         
        """
        pass
    
    ## Getter for property: (bool) IsEditCopy
    ##  Returns the value indicating if a copy of the facet body to be used for Divide facet face without altering the original   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be used for Divide facet face without altering the original   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsEditCopy

    ##  Returns the value indicating if a copy of the facet body to be used for Divide facet face without altering the original   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be used for Divide facet face without altering the original   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsSmoothEdge
    ##  Returns the option to add smoothing to the edge of the divided region    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def IsSmoothEdge(self) -> bool:
        """
        Getter for property: (bool) IsSmoothEdge
         Returns the option to add smoothing to the edge of the divided region    
            
         
        """
        pass
    
    ## Setter for property: (bool) IsSmoothEdge

    ##  Returns the option to add smoothing to the edge of the divided region    
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @IsSmoothEdge.setter
    def IsSmoothEdge(self, isSmoothEdge: bool):
        """
        Setter for property: (bool) IsSmoothEdge
         Returns the option to add smoothing to the edge of the divided region    
            
         
        """
        pass
    
    ## Getter for property: (int) Segments
    ##  Returnsthe number of segments used for advanced fitting  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::Facet::DivideFacetFaceBuilder::IsSmoothEdge NXOpen::Facet::DivideFacetFaceBuilder::IsSmoothEdge@endlink  instead.  <br> 

    ## @return int
    @property
    def Segments(self) -> int:
        """
        Getter for property: (int) Segments
         Returnsthe number of segments used for advanced fitting  
            
         
        """
        pass
    
    ## Setter for property: (int) Segments

    ##  Returnsthe number of segments used for advanced fitting  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::Facet::DivideFacetFaceBuilder::SetSmoothEdge NXOpen::Facet::DivideFacetFaceBuilder::SetSmoothEdge@endlink  instead.  <br> 

    @Segments.setter
    def Segments(self, segments: int):
        """
        Setter for property: (int) Segments
         Returnsthe number of segments used for advanced fitting  
            
         
        """
        pass
    
    ## Getter for property: (@link SplitCurveMethodListDataManager NXOpen.Facet.SplitCurveMethodListDataManager@endlink) SplitCurveMethodListDataManager
    ##  Returns the split curve method list data manager   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return SplitCurveMethodListDataManager
    @property
    def SplitCurveMethodListDataManager(self) -> SplitCurveMethodListDataManager:
        """
        Getter for property: (@link SplitCurveMethodListDataManager NXOpen.Facet.SplitCurveMethodListDataManager@endlink) SplitCurveMethodListDataManager
         Returns the split curve method list data manager   
            
         
        """
        pass
    
    ## Getter for property: (@link DivideFacetFaceBuilder.DivideFacetTypes NXOpen.Facet.DivideFacetFaceBuilder.DivideFacetTypes@endlink) Type
    ##  Returns the type of enum which decides method for dividing facet faces  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return DivideFacetFaceBuilder.DivideFacetTypes
    @property
    def Type(self) -> DivideFacetFaceBuilder.DivideFacetTypes:
        """
        Getter for property: (@link DivideFacetFaceBuilder.DivideFacetTypes NXOpen.Facet.DivideFacetFaceBuilder.DivideFacetTypes@endlink) Type
         Returns the type of enum which decides method for dividing facet faces  
            
         
        """
        pass
    
    ## Setter for property: (@link DivideFacetFaceBuilder.DivideFacetTypes NXOpen.Facet.DivideFacetFaceBuilder.DivideFacetTypes@endlink) Type

    ##  Returns the type of enum which decides method for dividing facet faces  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Type.setter
    def Type(self, type: DivideFacetFaceBuilder.DivideFacetTypes):
        """
        Setter for property: (@link DivideFacetFaceBuilder.DivideFacetTypes NXOpen.Facet.DivideFacetFaceBuilder.DivideFacetTypes@endlink) Type
         Returns the type of enum which decides method for dividing facet faces  
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::ExtrudeFacetBodyBuilder NXOpen::Facet::ExtrudeFacetBodyBuilder@endlink 
##     It extrudes a NX Facet Body. The limit of extrusion can be specified by direction and distance
##     or plane object. It returns the extruded NX Facet Body.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateExtrudeFacetBodyBuilder  NXOpen::Facet::FacetedBodyCollection::CreateExtrudeFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Distance.Value </term> <description> 
##  
## 10 (millimeters part), 1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Offset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Type </term> <description> 
##  
## Distance </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class ExtrudeFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.ExtrudeFacetBodyBuilder</ja_class>
    It extrudes a NX Facet Body. The limit of extrusion can be specified by direction and distance
    or plane object. It returns the extruded NX Facet Body.
    """


    ##  Represents the extrude limit type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Distance</term><description> 
    ##  Specify the limit by direction and distance. Direction and Distance need to be specified. </description> </item><item><term> 
    ## ToPlane</term><description> 
    ##  Specify the limit by plane object. Plane needes to be specified. </description> </item></list>
    class LimitType(Enum):
        """
        Members Include: <Distance> <ToPlane>
        """
        Distance: int
        ToPlane: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExtrudeFacetBodyBuilder.LimitType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
    ##  Returns the direction used when limit type is @link NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Direction(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
         Returns the direction used when limit type is @link NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction

    ##  Returns the direction used when limit type is @link NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance@endlink    
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Direction.setter
    def Direction(self, direction: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
         Returns the direction used when limit type is @link NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Distance
    ##  Returns the distance used when limit type is @link NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Distance
         Returns the distance used when limit type is @link NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance@endlink    
            
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##  Returns the distance tolerance used in the extrude facet body feature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the extrude facet body feature   
            
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##  Returns the distance tolerance used in the extrude facet body feature   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the extrude facet body feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) FacetBody
    ##  Returns the facet/sheet bodies to be extruded   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def FacetBody(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) FacetBody
         Returns the facet/sheet bodies to be extruded   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##  Returns the offset value used to offset the extruded body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
         Returns the offset value used to offset the extruded body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
    ##  Returns the plane used when limit type is @link NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeToPlane NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeToPlane@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the plane used when limit type is @link NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeToPlane NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeToPlane@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane

    ##  Returns the plane used when limit type is @link NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeToPlane NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeToPlane@endlink    
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the plane used when limit type is @link NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeToPlane NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeToPlane@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link ExtrudeFacetBodyBuilder.LimitType NXOpen.Facet.ExtrudeFacetBodyBuilder.LimitType@endlink) Type
    ##  Returns the limit type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ExtrudeFacetBodyBuilder.LimitType
    @property
    def Type(self) -> ExtrudeFacetBodyBuilder.LimitType:
        """
        Getter for property: (@link ExtrudeFacetBodyBuilder.LimitType NXOpen.Facet.ExtrudeFacetBodyBuilder.LimitType@endlink) Type
         Returns the limit type   
            
         
        """
        pass
    
    ## Setter for property: (@link ExtrudeFacetBodyBuilder.LimitType NXOpen.Facet.ExtrudeFacetBodyBuilder.LimitType@endlink) Type

    ##  Returns the limit type   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Type.setter
    def Type(self, type: ExtrudeFacetBodyBuilder.LimitType):
        """
        Setter for property: (@link ExtrudeFacetBodyBuilder.LimitType NXOpen.Facet.ExtrudeFacetBodyBuilder.LimitType@endlink) Type
         Returns the limit type   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::ExtrudeProfileBuilder NXOpen::Facet::ExtrudeProfileBuilder@endlink 
##     It extrudes 3D closed profile between planes. The two planes are defined 
##     by direction and distance. It returns the extruded NX Facet Body.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateExtrudeProfileBuilder  NXOpen::Facet::FacetedBodyCollection::CreateExtrudeProfileBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## FirstDistance.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Offset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## SecondDistance.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Tolerance.Value </term> <description> 
##  
## 0.01 (millimeters part), 0.001 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class ExtrudeProfileBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.ExtrudeProfileBuilder</ja_class>
    It extrudes 3D closed profile between planes. The two planes are defined 
    by direction and distance. It returns the extruded NX Facet Body.
    """


    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
    ##  Returns the extrude direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Direction(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
         Returns the extrude direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction

    ##  Returns the extrude direction   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Direction.setter
    def Direction(self, direction: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
         Returns the extrude direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FirstDistance
    ##  Returns the first distance to extrude   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FirstDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FirstDistance
         Returns the first distance to extrude   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##  Returns the offset used to offset the extruded body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
         Returns the offset used to offset the extruded body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Profile
    ##  Returns the 3D profile to be extruded   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def Profile(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Profile
         Returns the 3D profile to be extruded   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SecondDistance
    ##  Returns the second distance to extrude   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SecondDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SecondDistance
         Returns the second distance to extrude   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Tolerance
    ##  Returns the tolerance used to create the polyline   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Tolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Tolerance
         Returns the tolerance used to create the polyline   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::FacetBodyFromBodyBuilder NXOpen::Facet::FacetBodyFromBodyBuilder@endlink  builder. 
##     It converts the selected analytic bodies to NX convergent bodies bodies. 
##     The original inputs are deleted.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateFacetBodyFromBodyBuilder  NXOpen::Facet::FacetModelingCollection::CreateFacetBodyFromBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Associative </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## MaximumDeviation </term> <description> 
##  
## 0.1 (millimeters part), 0.005 (inches part) </description> </item> 
## 
## <item><term> 
##  
## OriginalBodyOption </term> <description> 
##  
## Hide </description> </item> 
## 
## <item><term> 
##  
## OutputType </term> <description> 
##  
## ConvergentBody </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class FacetBodyFromBodyBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.FacetBodyFromBodyBuilder</ja_class> builder. 
    It converts the selected analytic bodies to NX convergent bodies bodies. 
    The original inputs are deleted.
    """


    ##  These options represent the options for handling original body: Keep, Hide, Delete  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Keep</term><description> 
    ##  Keep original body </description> </item><item><term> 
    ## Hide</term><description> 
    ##  Hide original body </description> </item><item><term> 
    ## Delete</term><description> 
    ##  Delete original body </description> </item></list>
    class OriginalBodyOptions(Enum):
        """
        Members Include: <Keep> <Hide> <Delete>
        """
        Keep: int
        Hide: int
        Delete: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FacetBodyFromBodyBuilder.OriginalBodyOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  These options represent the type of output body 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ConvergentBody</term><description> 
    ##  Convert To Convergent bodies </description> </item><item><term> 
    ## NXFacetBody</term><description> 
    ##  Convert to NX Facet Bodies </description> </item><item><term> 
    ## JTFacetBody</term><description> 
    ##  Convert To JT Facet bodies </description> </item></list>
    class OutputTypes(Enum):
        """
        Members Include: <ConvergentBody> <NXFacetBody> <JTFacetBody>
        """
        ConvergentBody: int
        NXFacetBody: int
        JTFacetBody: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FacetBodyFromBodyBuilder.OutputTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) Associative
    ##  Returns the option that specifies whether the facet body from body operation is associative   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the option that specifies whether the facet body from body operation is associative   
            
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##  Returns the option that specifies whether the facet body from body operation is associative   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the option that specifies whether the facet body from body operation is associative   
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumDeviation
    ##  Returns the maximum deviation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def MaximumDeviation(self) -> float:
        """
        Getter for property: (float) MaximumDeviation
         Returns the maximum deviation   
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumDeviation

    ##  Returns the maximum deviation   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @MaximumDeviation.setter
    def MaximumDeviation(self, maximumDeviation: float):
        """
        Setter for property: (float) MaximumDeviation
         Returns the maximum deviation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) NonFacetedBodiesToConvert
    ##  Returns the input non-faceted bodies to convert   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def NonFacetedBodiesToConvert(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) NonFacetedBodiesToConvert
         Returns the input non-faceted bodies to convert   
            
         
        """
        pass
    
    ## Getter for property: (@link FacetBodyFromBodyBuilder.OriginalBodyOptions NXOpen.Facet.FacetBodyFromBodyBuilder.OriginalBodyOptions@endlink) OriginalBodyOption
    ##  Returns the original body option of enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return FacetBodyFromBodyBuilder.OriginalBodyOptions
    @property
    def OriginalBodyOption(self) -> FacetBodyFromBodyBuilder.OriginalBodyOptions:
        """
        Getter for property: (@link FacetBodyFromBodyBuilder.OriginalBodyOptions NXOpen.Facet.FacetBodyFromBodyBuilder.OriginalBodyOptions@endlink) OriginalBodyOption
         Returns the original body option of enum   
            
         
        """
        pass
    
    ## Setter for property: (@link FacetBodyFromBodyBuilder.OriginalBodyOptions NXOpen.Facet.FacetBodyFromBodyBuilder.OriginalBodyOptions@endlink) OriginalBodyOption

    ##  Returns the original body option of enum   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @OriginalBodyOption.setter
    def OriginalBodyOption(self, enumOriginalBodyOption: FacetBodyFromBodyBuilder.OriginalBodyOptions):
        """
        Setter for property: (@link FacetBodyFromBodyBuilder.OriginalBodyOptions NXOpen.Facet.FacetBodyFromBodyBuilder.OriginalBodyOptions@endlink) OriginalBodyOption
         Returns the original body option of enum   
            
         
        """
        pass
    
    ## Getter for property: (@link FacetBodyFromBodyBuilder.OutputTypes NXOpen.Facet.FacetBodyFromBodyBuilder.OutputTypes@endlink) OutputType
    ##  Returns the output of the type of enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return FacetBodyFromBodyBuilder.OutputTypes
    @property
    def OutputType(self) -> FacetBodyFromBodyBuilder.OutputTypes:
        """
        Getter for property: (@link FacetBodyFromBodyBuilder.OutputTypes NXOpen.Facet.FacetBodyFromBodyBuilder.OutputTypes@endlink) OutputType
         Returns the output of the type of enum   
            
         
        """
        pass
    
    ## Setter for property: (@link FacetBodyFromBodyBuilder.OutputTypes NXOpen.Facet.FacetBodyFromBodyBuilder.OutputTypes@endlink) OutputType

    ##  Returns the output of the type of enum   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @OutputType.setter
    def OutputType(self, enumOutputType: FacetBodyFromBodyBuilder.OutputTypes):
        """
        Setter for property: (@link FacetBodyFromBodyBuilder.OutputTypes NXOpen.Facet.FacetBodyFromBodyBuilder.OutputTypes@endlink) OutputType
         Returns the output of the type of enum   
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of faceted bodies in a part  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class FacetedBodyCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of faceted bodies in a part """


    ##  Specifies the type of facets created when copying or converting faceted bodies 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Nx</term><description> 
    ##  NX facet </description> </item><item><term> 
    ## Jt</term><description> 
    ##  JT facet </description> </item></list>
    class Type(Enum):
        """
        Members Include: <Nx> <Jt>
        """
        Nx: int
        Jt: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FacetedBodyCollection.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Returns the FacetModelingCollection instance belonging to this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @link FacetModelingCollection NXOpen.Facet.FacetModelingCollection@endlink
    @property
    def FacetModelingCollection() -> FacetModelingCollection:
        """
         Returns the FacetModelingCollection instance belonging to this part 
        """
        pass
    
    ##  Converts the internal representation of this faceted body to the specified type. This does not create a new body 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fromBody"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  The faceted body to convert </param>
    ## <param name="toFacetType"> (@link FacetedBodyCollection.Type NXOpen.Facet.FacetedBodyCollection.Type@endlink)  To facet type </param>
    def Convert(self, fromBody: FacetedBody, toFacetType: FacetedBodyCollection.Type) -> None:
        """
         Converts the internal representation of this faceted body to the specified type. This does not create a new body 
        """
        pass
    
    ##  Copies a faceted body and optionally changes the internal representation to the given type
    ##              (This is only valid for JT to NX copy) 
    ##          
    ##  @return copy (@link FacetedBody NXOpen.Facet.FacetedBody@endlink):  New body .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fromBody"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  The faceted body to copy </param>
    ## <param name="toPart"> (@link NXOpen.Part NXOpen.Part@endlink)  Part to create the copy in </param>
    ## <param name="toFacetType"> (@link FacetedBodyCollection.Type NXOpen.Facet.FacetedBodyCollection.Type@endlink)  To facet type </param>
    def Copy(self, fromBody: FacetedBody, toPart: NXOpen.Part, toFacetType: FacetedBodyCollection.Type) -> FacetedBody:
        """
         Copies a faceted body and optionally changes the internal representation to the given type
                     (This is only valid for JT to NX copy) 
                 
         @return copy (@link FacetedBody NXOpen.Facet.FacetedBody@endlink):  New body .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::BestFitAlignBuilder NXOpen::Facet::BestFitAlignBuilder@endlink  
    ##  @return builder (@link BestFitAlignBuilder NXOpen.Facet.BestFitAlignBuilder@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling")
    def CreateBestFitAlignBuilder(self) -> BestFitAlignBuilder:
        """
         Creates a @link NXOpen::Facet::BestFitAlignBuilder NXOpen::Facet::BestFitAlignBuilder@endlink  
         @return builder (@link BestFitAlignBuilder NXOpen.Facet.BestFitAlignBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::BridgeFacetBodyBuilder NXOpen::Facet::BridgeFacetBodyBuilder@endlink  
    ##  @return builder (@link BridgeFacetBodyBuilder NXOpen.Facet.BridgeFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    def CreateBridgeFacetBodyBuilder(self) -> BridgeFacetBodyBuilder:
        """
         Creates a @link NXOpen::Facet::BridgeFacetBodyBuilder NXOpen::Facet::BridgeFacetBodyBuilder@endlink  
         @return builder (@link BridgeFacetBodyBuilder NXOpen.Facet.BridgeFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::DecimateFacetBodyBuilder NXOpen::Facet::DecimateFacetBodyBuilder@endlink  
    ##  @return builder (@link DecimateFacetBodyBuilder NXOpen.Facet.DecimateFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateDecimateFacetBodyBuilder(self) -> DecimateFacetBodyBuilder:
        """
         Creates a @link NXOpen::Facet::DecimateFacetBodyBuilder NXOpen::Facet::DecimateFacetBodyBuilder@endlink  
         @return builder (@link DecimateFacetBodyBuilder NXOpen.Facet.DecimateFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::ExtrudeFacetBodyBuilder NXOpen::Facet::ExtrudeFacetBodyBuilder@endlink  
    ##  @return builder (@link ExtrudeFacetBodyBuilder NXOpen.Facet.ExtrudeFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    def CreateExtrudeFacetBodyBuilder(self) -> ExtrudeFacetBodyBuilder:
        """
         Creates a @link NXOpen::Facet::ExtrudeFacetBodyBuilder NXOpen::Facet::ExtrudeFacetBodyBuilder@endlink  
         @return builder (@link ExtrudeFacetBodyBuilder NXOpen.Facet.ExtrudeFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::ExtrudeProfileBuilder NXOpen::Facet::ExtrudeProfileBuilder@endlink  
    ##  @return builder (@link ExtrudeProfileBuilder NXOpen.Facet.ExtrudeProfileBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    def CreateExtrudeProfileBuilder(self) -> ExtrudeProfileBuilder:
        """
         Creates a @link NXOpen::Facet::ExtrudeProfileBuilder NXOpen::Facet::ExtrudeProfileBuilder@endlink  
         @return builder (@link ExtrudeProfileBuilder NXOpen.Facet.ExtrudeProfileBuilder@endlink): .
        """
        pass
    
    ##  Creates a JT @link NXOpen::Facet::FacetedBody NXOpen::Facet::FacetedBody@endlink  using the default faceting tolerances. 
    ##             The output facetBodies and errorTable arrays are the same size as the input nSolidBodies. 
    ##             The errorTable array provides information about any errors encountered when faceting bodies. 
    ##             Note that it is possible that faceted bodies with 0 facets are created (and returned in the facetBodies parameter). 
    ##             For this case, the errorTable will contain the UF_FACET_err_zero_facets_produced error. 
    ##             If there is an existing facet body it will get refaceted with the previous tolerance used to tessellate it .
    ##             See @link NXOpen::Body::GetFacetedBody NXOpen::Body::GetFacetedBody@endlink  for ways to check for this situation.
    ##         
    ##  @return A tuple consisting of (facetBodies, errorTable). 
    ##  - facetBodies is: @link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink.
    ##  - errorTable is: List[int].

    ## 
    ##   <br>  Created in NX7.5.5  <br> 

    ## License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
    ## 
    ## <param name="solidBodies"> (@link NXOpen.Body List[NXOpen.Body]@endlink) </param>
    def CreateFacetBody(self, solidBodies: List[NXOpen.Body]) -> Tuple[List[FacetedBody], List[int]]:
        """
         Creates a JT @link NXOpen::Facet::FacetedBody NXOpen::Facet::FacetedBody@endlink  using the default faceting tolerances. 
                    The output facetBodies and errorTable arrays are the same size as the input nSolidBodies. 
                    The errorTable array provides information about any errors encountered when faceting bodies. 
                    Note that it is possible that faceted bodies with 0 facets are created (and returned in the facetBodies parameter). 
                    For this case, the errorTable will contain the UF_FACET_err_zero_facets_produced error. 
                    If there is an existing facet body it will get refaceted with the previous tolerance used to tessellate it .
                    See @link NXOpen::Body::GetFacetedBody NXOpen::Body::GetFacetedBody@endlink  for ways to check for this situation.
                
         @return A tuple consisting of (facetBodies, errorTable). 
         - facetBodies is: @link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink.
         - errorTable is: List[int].

        """
        pass
    
    ##  Creates a JT @link NXOpen::Facet::FacetedBody NXOpen::Facet::FacetedBody@endlink  using the default faceting tolerances. 
    ##             The output facetBodies and errorTable arrays are the same size as the input nSolidFaces. 
    ##             The errorTable array provides information about any errors encountered when faceting bodies. 
    ##             Note that it is possible that faceted bodies with 0 facets are created (and returned in the facetBodies parameter). 
    ##             For this case, the errorTable will contain the UF_FACET_err_zero_facets_produced error. 
    ##             If there is an existing facet body it will get refaceted with the previous tolerance used to tessellate it .
    ##             See @link NXOpen::Body::GetFacetedBody NXOpen::Body::GetFacetedBody@endlink  for ways to check for this situation.
    ##         
    ##  @return A tuple consisting of (facetBodies, errorTable). 
    ##  - facetBodies is: @link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink.
    ##  - errorTable is: List[int].

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
    ## 
    ## <param name="solidFaces"> (@link NXOpen.Face List[NXOpen.Face]@endlink) </param>
    def CreateFacetBodyFromFaces(self, solidFaces: List[NXOpen.Face]) -> Tuple[List[FacetedBody], List[int]]:
        """
         Creates a JT @link NXOpen::Facet::FacetedBody NXOpen::Facet::FacetedBody@endlink  using the default faceting tolerances. 
                    The output facetBodies and errorTable arrays are the same size as the input nSolidFaces. 
                    The errorTable array provides information about any errors encountered when faceting bodies. 
                    Note that it is possible that faceted bodies with 0 facets are created (and returned in the facetBodies parameter). 
                    For this case, the errorTable will contain the UF_FACET_err_zero_facets_produced error. 
                    If there is an existing facet body it will get refaceted with the previous tolerance used to tessellate it .
                    See @link NXOpen::Body::GetFacetedBody NXOpen::Body::GetFacetedBody@endlink  for ways to check for this situation.
                
         @return A tuple consisting of (facetBodies, errorTable). 
         - facetBodies is: @link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink.
         - errorTable is: List[int].

        """
        pass
    
    ##  Create a @link NXOpen::Facet::CurvatureBuilder NXOpen::Facet::CurvatureBuilder@endlink  object. 
    ##  @return builder (@link CurvatureBuilder NXOpen.Facet.CurvatureBuilder@endlink): .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def CreateFacetCurvatureBuilder(self) -> CurvatureBuilder:
        """
         Create a @link NXOpen::Facet::CurvatureBuilder NXOpen::Facet::CurvatureBuilder@endlink  object. 
         @return builder (@link CurvatureBuilder NXOpen.Facet.CurvatureBuilder@endlink): .
        """
        pass
    
    ##  Create a @link NXOpen::Facet::FeatureExtractionBuilder NXOpen::Facet::FeatureExtractionBuilder@endlink  object. 
    ##  @return builder (@link FeatureExtractionBuilder NXOpen.Facet.FeatureExtractionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    def CreateFacetFeatureExtractionBuilder(self) -> FeatureExtractionBuilder:
        """
         Create a @link NXOpen::Facet::FeatureExtractionBuilder NXOpen::Facet::FeatureExtractionBuilder@endlink  object. 
         @return builder (@link FeatureExtractionBuilder NXOpen.Facet.FeatureExtractionBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::FillHoleBuilder NXOpen::Facet::FillHoleBuilder@endlink  
    ##  @return builder (@link FillHoleBuilder NXOpen.Facet.FillHoleBuilder@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateFillHoleBuilder(self) -> FillHoleBuilder:
        """
         Creates a @link NXOpen::Facet::FillHoleBuilder NXOpen::Facet::FillHoleBuilder@endlink  
         @return builder (@link FillHoleBuilder NXOpen.Facet.FillHoleBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::MergeFacetBodyBuilder NXOpen::Facet::MergeFacetBodyBuilder@endlink  
    ##  @return builder (@link MergeFacetBodyBuilder NXOpen.Facet.MergeFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  This functionality is no longer supported.  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    def CreateMergeFacetBodyBuilder(self) -> MergeFacetBodyBuilder:
        """
         Creates a @link NXOpen::Facet::MergeFacetBodyBuilder NXOpen::Facet::MergeFacetBodyBuilder@endlink  
         @return builder (@link MergeFacetBodyBuilder NXOpen.Facet.MergeFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::MultiPatchAlignmentBuilder NXOpen::Facet::MultiPatchAlignmentBuilder@endlink  
    ##  @return builder (@link MultiPatchAlignmentBuilder NXOpen.Facet.MultiPatchAlignmentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateMultiPatchAlignmentBuilder(self) -> MultiPatchAlignmentBuilder:
        """
         Creates a @link NXOpen::Facet::MultiPatchAlignmentBuilder NXOpen::Facet::MultiPatchAlignmentBuilder@endlink  
         @return builder (@link MultiPatchAlignmentBuilder NXOpen.Facet.MultiPatchAlignmentBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::STLImportBuilder NXOpen::Facet::STLImportBuilder@endlink  
    ##  @return builder (@link STLImportBuilder NXOpen.Facet.STLImportBuilder@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling") OR nx_masterfem ("Finite Element Modeling")
    def CreateSTLImportBuilder(self) -> STLImportBuilder:
        """
         Creates a @link NXOpen::Facet::STLImportBuilder NXOpen::Facet::STLImportBuilder@endlink  
         @return builder (@link STLImportBuilder NXOpen.Facet.STLImportBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::SewFacetBodyBuilder NXOpen::Facet::SewFacetBodyBuilder@endlink  
    ##  @return builder (@link SewFacetBodyBuilder NXOpen.Facet.SewFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    def CreateSewFacetBodyBuilder(self) -> SewFacetBodyBuilder:
        """
         Creates a @link NXOpen::Facet::SewFacetBodyBuilder NXOpen::Facet::SewFacetBodyBuilder@endlink  
         @return builder (@link SewFacetBodyBuilder NXOpen.Facet.SewFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::SmoothFacetBodyBuilder NXOpen::Facet::SmoothFacetBodyBuilder@endlink  
    ##  @return builder (@link SmoothFacetBodyBuilder NXOpen.Facet.SmoothFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateSmoothFacetBodyBuilder(self) -> SmoothFacetBodyBuilder:
        """
         Creates a @link NXOpen::Facet::SmoothFacetBodyBuilder NXOpen::Facet::SmoothFacetBodyBuilder@endlink  
         @return builder (@link SmoothFacetBodyBuilder NXOpen.Facet.SmoothFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::SnipFacetBodyBuilder NXOpen::Facet::SnipFacetBodyBuilder@endlink  
    ##  @return builder (@link SnipFacetBodyBuilder NXOpen.Facet.SnipFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateSnipFacetBodyBuilder(self) -> SnipFacetBodyBuilder:
        """
         Creates a @link NXOpen::Facet::SnipFacetBodyBuilder NXOpen::Facet::SnipFacetBodyBuilder@endlink  
         @return builder (@link SnipFacetBodyBuilder NXOpen.Facet.SnipFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::SubdivideFacetBodyBuilder NXOpen::Facet::SubdivideFacetBodyBuilder@endlink  
    ##  @return builder (@link SubdivideFacetBodyBuilder NXOpen.Facet.SubdivideFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateSubdivideFacetBodyBuilder(self) -> SubdivideFacetBodyBuilder:
        """
         Creates a @link NXOpen::Facet::SubdivideFacetBodyBuilder NXOpen::Facet::SubdivideFacetBodyBuilder@endlink  
         @return builder (@link SubdivideFacetBodyBuilder NXOpen.Facet.SubdivideFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Delete any temporary faces and edges on faceted bodies that may have been created 
    ##             in the specified part.  Please note that this call will invoke an Update operation.
    ##         
    ## 
    ##   <br>  Created in NX5.0.2  <br> 

    ## License requirements: None.
    def DeleteTemporaryFacesAndEdges(self) -> None:
        """
         Delete any temporary faces and edges on faceted bodies that may have been created 
                    in the specified part.  Please note that this call will invoke an Update operation.
                
        """
        pass
    
    ##  Finds the @link  NXOpen::Facet::FacetedBody   NXOpen::Facet::FacetedBody @endlink  with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link FacetedBody NXOpen.Facet.FacetedBody@endlink):  Faceted body with this identifier .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Identifier of the faceted body you want </param>
    def FindObject(self, journal_identifier: str) -> FacetedBody:
        """
         Finds the @link  NXOpen::Facet::FacetedBody   NXOpen::Facet::FacetedBody @endlink  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
        
                    An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link FacetedBody NXOpen.Facet.FacetedBody@endlink):  Faceted body with this identifier .
        """
        pass
    
    ##  Returns the loaded solid bodies associated with the argument faceted body.
    ##             Also returns the number of unloaded associated faceted bodies.
    ##         
    ##  @return A tuple consisting of (associatedFacetedBodies, numberOfUnloadedFacetedBodies). 
    ##  - associatedFacetedBodies is: @link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink. Array of loaded associated faceted bodies .
    ##  - numberOfUnloadedFacetedBodies is: int. The number of unloaded associated faceted bodies for this solids body .

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="solidBody"> (@link NXOpen.Body NXOpen.Body@endlink)  The body for which to get associated faceted bodies </param>
    def GetAssociatedFacetedBodies(self, solidBody: NXOpen.Body) -> Tuple[List[FacetedBody], int]:
        """
         Returns the loaded solid bodies associated with the argument faceted body.
                    Also returns the number of unloaded associated faceted bodies.
                
         @return A tuple consisting of (associatedFacetedBodies, numberOfUnloadedFacetedBodies). 
         - associatedFacetedBodies is: @link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink. Array of loaded associated faceted bodies .
         - numberOfUnloadedFacetedBodies is: int. The number of unloaded associated faceted bodies for this solids body .

        """
        pass
    
import NXOpen
##  
##     Represents a faceted body. Instances of this class cannot be created directly by the user, but can
##     be created using the methods of FacetedBodyCollection.
##     
## 
##   <br>  Created in NX5.0.0  <br> 

class FacetedBody(NXOpen.DisplayableObject): 
    """ 
    Represents a faceted body. Instances of this class cannot be created directly by the user, but can
    be created using the methods of FacetedBodyCollection.
    """


    ##  Body type
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Undefined</term><description> 
    ##  Undefined body type </description> </item><item><term> 
    ## SolidBody</term><description> 
    ## </description> </item><item><term> 
    ## SheetBody</term><description> 
    ## </description> </item></list>
    class FacetedbodyType(Enum):
        """
        Members Include: <Undefined> <SolidBody> <SheetBody>
        """
        Undefined: int
        SolidBody: int
        SheetBody: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FacetedBody.FacetedbodyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Body NXOpen.Body@endlink) AssociatedBody
    ##  Returns
    ##             the solid body associated with this facet body.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Body
    @property
    def AssociatedBody(self) -> NXOpen.Body:
        """
        Getter for property: (@link NXOpen.Body NXOpen.Body@endlink) AssociatedBody
         Returns
                    the solid body associated with this facet body.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link FacetedBody.FacetedbodyType NXOpen.Facet.FacetedBody.FacetedbodyType@endlink) BodyType
    ##  Returns the type of the body.  
    ##   
    ##             This only works for JT Facets.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## @return FacetedBody.FacetedbodyType
    @property
    def BodyType(self) -> FacetedBody.FacetedbodyType:
        """
        Getter for property: (@link FacetedBody.FacetedbodyType NXOpen.Facet.FacetedBody.FacetedbodyType@endlink) BodyType
         Returns the type of the body.  
          
                    This only works for JT Facets.
                  
         
        """
        pass
    
    ## Getter for property: (bool) IsAssemblyLevel
    ##  Returns
    ##             a flag indicating this is an assembly level representation.  
    ##    That is
    ##             this facet body is associated with an occurrence of a solid body. 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def IsAssemblyLevel(self) -> bool:
        """
        Getter for property: (bool) IsAssemblyLevel
         Returns
                    a flag indicating this is an assembly level representation.  
           That is
                    this facet body is associated with an occurrence of a solid body. 
                  
         
        """
        pass
    
    ## Getter for property: (bool) IsAssociatedBodyLoaded
    ##  Returns
    ##             the load state of the solid body associated with this facet body.  
    ##   
    ##             False if there is no associated body.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def IsAssociatedBodyLoaded(self) -> bool:
        """
        Getter for property: (bool) IsAssociatedBodyLoaded
         Returns
                    the load state of the solid body associated with this facet body.  
          
                    False if there is no associated body.
                  
         
        """
        pass
    
    ## Getter for property: (bool) IsSheetBody
    ##  Returns true if the body is a sheet body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.1.  Use @link NXOpen::Facet::FacetedBody::BodyType NXOpen::Facet::FacetedBody::BodyType@endlink  instead  <br> 

    ## @return bool
    @property
    def IsSheetBody(self) -> bool:
        """
        Getter for property: (bool) IsSheetBody
         Returns true if the body is a sheet body   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsSolidBody
    ##  Returns true if the body is a solid body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.1.  Use @link NXOpen::Facet::FacetedBody::BodyType NXOpen::Facet::FacetedBody::BodyType@endlink  instead.  <br> 

    ## @return bool
    @property
    def IsSolidBody(self) -> bool:
        """
        Getter for property: (bool) IsSolidBody
         Returns true if the body is a solid body   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfFaces
    ##  Returns
    ##             the number of faces in this faceted body in the highest level of detail.  
    ##   
    ##             Typically only useful if the model has been derived from a solid model. 
    ##             For models constructed directly, the output will be number of facets/triangles, since there would be no faces. 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def NumberOfFaces(self) -> int:
        """
        Getter for property: (int) NumberOfFaces
         Returns
                    the number of faces in this faceted body in the highest level of detail.  
          
                    Typically only useful if the model has been derived from a solid model. 
                    For models constructed directly, the output will be number of facets/triangles, since there would be no faces. 
                  
         
        """
        pass
    
    ## Getter for property: (int) NumberOfLevelsOfDetail
    ##  Returns
    ##             the number of levels of detail in this faceted body.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def NumberOfLevelsOfDetail(self) -> int:
        """
        Getter for property: (int) NumberOfLevelsOfDetail
         Returns
                    the number of levels of detail in this faceted body.  
          
                  
         
        """
        pass
    
    ## Getter for property: (float) SurfaceArea
    ##  Returns
    ##             the surface area of the faceted body in part units for its
    ##             highest level of detail.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def SurfaceArea(self) -> float:
        """
        Getter for property: (float) SurfaceArea
         Returns
                    the surface area of the faceted body in part units for its
                    highest level of detail.  
          
                  
         
        """
        pass
    
    ## Getter for property: (float) Volume
    ##  Returns
    ##             the volume of the faceted body in part units for its
    ##             highest level of detail.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def Volume(self) -> float:
        """
        Getter for property: (float) Volume
         Returns
                    the volume of the faceted body in part units for its
                    highest level of detail.  
          
                  
         
        """
        pass
    
    ## 
    ##             Destroys all @link IFacet IFacet@endlink  objects owned by this body.
    ##              
    ##             Please note that this method does not geometrically delete a facet from its surface mesh leaving a hole. 
    ##             It only deletes the tagged object created to represent the individual facet.
    ##             
    ##         
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def DestroyOwnedFacets(self) -> None:
        """
        
                    Destroys all @link IFacet IFacet@endlink  objects owned by this body.
                     
                    Please note that this method does not geometrically delete a facet from its surface mesh leaving a hole. 
                    It only deletes the tagged object created to represent the individual facet.
                    
                
        """
        pass
    
    ##  Returns the edges in the faceted body.
    ##             This only works for JT Facets.
    ##         
    ##  @return edges (@link FacetedEdge List[NXOpen.Facet.FacetedEdge]@endlink):  .
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def GetEdges(self) -> List[FacetedEdge]:
        """
         Returns the edges in the faceted body.
                    This only works for JT Facets.
                
         @return edges (@link FacetedEdge List[NXOpen.Facet.FacetedEdge]@endlink):  .
        """
        pass
    
    ##  Returns the faces in the faceted body.
    ##             This only works for JT Facets.
    ##         
    ##  @return faceted_face (@link FacetedFace List[NXOpen.Facet.FacetedFace]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def GetFaces(self) -> List[FacetedFace]:
        """
         Returns the faces in the faceted body.
                    This only works for JT Facets.
                
         @return faceted_face (@link FacetedFace List[NXOpen.Facet.FacetedFace]@endlink): .
        """
        pass
    
    ##  Returns the number of edges in the faceted body.
    ##             This only works for JT Facets.
    ##         
    ##  @return number_of_edges (int): .
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def GetNumberOfEdges(self) -> int:
        """
         Returns the number of edges in the faceted body.
                    This only works for JT Facets.
                
         @return number_of_edges (int): .
        """
        pass
    
    ## 
    ##             Get the number of facets in the given level of detail.
    ##         
    ##  @return count (int): .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="level_of_detail"> (int)  level of detail to query </param>
    def GetNumberOfFacets(self, level_of_detail: int) -> int:
        """
        
                    Get the number of facets in the given level of detail.
                
         @return count (int): .
        """
        pass
    
    ##  
    ##             Get the faceted body parameters
    ##         
    ##  @return parameters (@link FacetingParameters NXOpen.Facet.FacetingParameters@endlink):  faceting parameters for this body .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetParameters(self) -> FacetingParameters:
        """
         
                    Get the faceted body parameters
                
         @return parameters (@link FacetingParameters NXOpen.Facet.FacetingParameters@endlink):  faceting parameters for this body .
        """
        pass
    
    ##  Returns whether the FACET has analytical information.
    ##             This only works for JT Facets.
    ##         
    ##  @return has_lightweight_analytics (bool): .
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def HasLightWeightAnalytics(self) -> bool:
        """
         Returns whether the FACET has analytical information.
                    This only works for JT Facets.
                
         @return has_lightweight_analytics (bool): .
        """
        pass
    
    ##  Returns whether the FACET has topology information.
    ##             This only works for JT Facets.
    ##         
    ##  @return has_topology_information (bool): .
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def HasTopologyInformation(self) -> bool:
        """
         Returns whether the FACET has topology information.
                    This only works for JT Facets.
                
         @return has_topology_information (bool): .
        """
        pass
    
    ##  
    ##             Set the faceted body parameters, it will retessellate the body with the new parameters
    ##         
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameters"> (@link FacetingParameters NXOpen.Facet.FacetingParameters@endlink)  new facetting faceting parameters to set for this body </param>
    def SetParameters(self, parameters: FacetingParameters) -> None:
        """
         
                    Set the faceted body parameters, it will retessellate the body with the new parameters
                
        """
        pass
    
import NXOpen
##  Represents a faceted edge. Instances of this class may be
##         generated when recording a journal, but they cannot be created
##         directly. 
##     
## 
##   <br>  Created in NX5.0.0  <br> 

class FacetedEdge(NXOpen.DisplayableObject): 
    """ Represents a faceted edge. Instances of this class may be
        generated when recording a journal, but they cannot be created
        directly. 
    """


    ##  Facet Edge type
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Undefined</term><description> 
    ## </description> </item><item><term> 
    ## Linear</term><description> 
    ##  Linear edge </description> </item><item><term> 
    ## Circular</term><description> 
    ##  Circular edge </description> </item><item><term> 
    ## Elliptical</term><description> 
    ##  Elliptical edge </description> </item><item><term> 
    ## Intersection</term><description> 
    ##  Intersection edge </description> </item><item><term> 
    ## Spline</term><description> 
    ##  Spline edge </description> </item></list>
    class FacetededgeType(Enum):
        """
        Members Include: <Undefined> <Linear> <Circular> <Elliptical> <Intersection> <Spline>
        """
        Undefined: int
        Linear: int
        Circular: int
        Elliptical: int
        Intersection: int
        Spline: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FacetedEdge.FacetededgeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FacetedEdge.FacetededgeType NXOpen.Facet.FacetedEdge.FacetededgeType@endlink) EdgeType
    ##  Returns the type of the facet edge   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## @return FacetedEdge.FacetededgeType
    @property
    def EdgeType(self) -> FacetedEdge.FacetededgeType:
        """
        Getter for property: (@link FacetedEdge.FacetededgeType NXOpen.Facet.FacetedEdge.FacetededgeType@endlink) EdgeType
         Returns the type of the facet edge   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsReference
    ##  Returns the reference state of a curve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def IsReference(self) -> bool:
        """
        Getter for property: (bool) IsReference
         Returns the reference state of a curve   
            
         
        """
        pass
    
    ##  Returns the body containing this edge 
    ##  @return faceted_body (@link FacetedBody NXOpen.Facet.FacetedBody@endlink):  .
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def GetBody(self) -> FacetedBody:
        """
         Returns the body containing this edge 
         @return faceted_body (@link FacetedBody NXOpen.Facet.FacetedBody@endlink):  .
        """
        pass
    
    ##  Returns the curve information for the facet edge
    ## 
    ##            Parameter description
    ##            faceted_edge           : The input edge tag for which curve information is required.
    ##            PNT3_p_t position      : Line: Position on Line 
    ##                                     Circle/Ellipse: Center Point
    ##                                     Spline/Intersection-Curve: Start Point of Curve.
    ##            PNT3_p_t dir_or_end_pt : Line : Direction of the Line
    ##                                     Circle: Normal to Plane Axis.
    ##                                     Ellipse: Major Axis
    ##                                     Spline/Intersection-Curve: End Point.
    ##            PNT3_p_t x_axis         : Circle: Axis from Center to Start Point,
    ##                                     Ellipse: Minor Axis
    ##                                     Not valid for other types.
    ##        
    ##            double* radius         : Circle: Radius
    ##                                     Ellipse: Major Radius
    ##                                     Not valid for other types.
    ## 
    ##            double* minor_radius   : Ellipse: Minor Radius
    ##                                     Not valid for other types.
    ## 
    ##         
    ##  @return A tuple consisting of (position, dir_or_end_pt, x_axis, radius, minor_radius). 
    ##  - position is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - dir_or_end_pt is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - x_axis is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - radius is: float.
    ##  - minor_radius is: float.

    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def GetCurveData(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d, NXOpen.Point3d, float, float]:
        """
         Returns the curve information for the facet edge
        
                   Parameter description
                   faceted_edge           : The input edge tag for which curve information is required.
                   PNT3_p_t position      : Line: Position on Line 
                                            Circle/Ellipse: Center Point
                                            Spline/Intersection-Curve: Start Point of Curve.
                   PNT3_p_t dir_or_end_pt : Line : Direction of the Line
                                            Circle: Normal to Plane Axis.
                                            Ellipse: Major Axis
                                            Spline/Intersection-Curve: End Point.
                   PNT3_p_t x_axis         : Circle: Axis from Center to Start Point,
                                            Ellipse: Minor Axis
                                            Not valid for other types.
               
                   double* radius         : Circle: Radius
                                            Ellipse: Major Radius
                                            Not valid for other types.
        
                   double* minor_radius   : Ellipse: Minor Radius
                                            Not valid for other types.
        
                
         @return A tuple consisting of (position, dir_or_end_pt, x_axis, radius, minor_radius). 
         - position is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - dir_or_end_pt is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - x_axis is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - radius is: float.
         - minor_radius is: float.

        """
        pass
    
    ##  Returns the faces connected to the edge 
    ##  @return faces (@link FacetedFace List[NXOpen.Facet.FacetedFace]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def GetFaces(self) -> List[FacetedFace]:
        """
         Returns the faces connected to the edge 
         @return faces (@link FacetedFace List[NXOpen.Facet.FacetedFace]@endlink): .
        """
        pass
    
    ##  Returns the vertices of the edge. If the edge is closed, the second vertex is the same as the first. 
    ##  @return A tuple consisting of (vertex1, vertex2). 
    ##  - vertex1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. First vertex in the edge .
    ##  - vertex2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. Second vertex in the edge .

    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def GetVertices(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
         Returns the vertices of the edge. If the edge is closed, the second vertex is the same as the first. 
         @return A tuple consisting of (vertex1, vertex2). 
         - vertex1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. First vertex in the edge .
         - vertex2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. Second vertex in the edge .

        """
        pass
    
import NXOpen
##  Represents a faceted face. Instances of this class may be
##         generated when recording a journal, but they cannot be created
##         directly. 
##     
## 
##   <br>  Created in NX5.0.0  <br> 

class FacetedFace(NXOpen.DisplayableObject): 
    """ Represents a faceted face. Instances of this class may be
        generated when recording a journal, but they cannot be created
        directly. 
    """


    ##  Facet Face type
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Undefined</term><description> 
    ##  Undefined body type </description> </item><item><term> 
    ## Planar</term><description> 
    ##  Planar face </description> </item><item><term> 
    ## Cylindrical</term><description> 
    ##  Cylindrical face </description> </item><item><term> 
    ## Conical</term><description> 
    ##  Conical face </description> </item><item><term> 
    ## Spherical</term><description> 
    ##  Spherical face </description> </item><item><term> 
    ## Toroidal</term><description> 
    ##  Face from toroid </description> </item><item><term> 
    ## Parametric</term><description> 
    ##  Parametric face </description> </item></list>
    class FacetedfaceType(Enum):
        """
        Members Include: <Undefined> <Planar> <Cylindrical> <Conical> <Spherical> <Toroidal> <Parametric>
        """
        Undefined: int
        Planar: int
        Cylindrical: int
        Conical: int
        Spherical: int
        Toroidal: int
        Parametric: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FacetedFace.FacetedfaceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FacetedFace.FacetedfaceType NXOpen.Facet.FacetedFace.FacetedfaceType@endlink) FaceType
    ##  Returns the type of the face   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## @return FacetedFace.FacetedfaceType
    @property
    def FaceType(self) -> FacetedFace.FacetedfaceType:
        """
        Getter for property: (@link FacetedFace.FacetedfaceType NXOpen.Facet.FacetedFace.FacetedfaceType@endlink) FaceType
         Returns the type of the face   
            
         
        """
        pass
    
    ##  Returns the facet body containing this facet face 
    ##  @return faceted_body (@link FacetedBody NXOpen.Facet.FacetedBody@endlink): .
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def GetBody(self) -> FacetedBody:
        """
         Returns the facet body containing this facet face 
         @return faceted_body (@link FacetedBody NXOpen.Facet.FacetedBody@endlink): .
        """
        pass
    
    ##  Returns the edges connected to the face 
    ##  @return faceted_edges (@link FacetedEdge List[NXOpen.Facet.FacetedEdge]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def GetEdges(self) -> List[FacetedEdge]:
        """
         Returns the edges connected to the face 
         @return faceted_edges (@link FacetedEdge List[NXOpen.Facet.FacetedEdge]@endlink): .
        """
        pass
    
    ##  Returns the number of edges in the faceted face 
    ##  @return number_of_edges (int): .
    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def GetNumberOfEdges(self) -> int:
        """
         Returns the number of edges in the faceted face 
         @return number_of_edges (int): .
        """
        pass
    
    ##  Returns the surface information for this face 
    ##        
    ##             tag_t    faceted_face     : The input edge tag for which face information is required.
    ##             PNT3_p_t position         : Plane: Position on Plane
    ##                                         Origin for other
    ##             PNT3_p_t dir              : Plane: Normal direction
    ##                                         Axis for others.
    ##             double   *radius          : Not applicable for planes
    ##                                         Cylinder: Radius of Cylinder, 
    ##                                         Sphere: Radius of Sphere
    ##                                         Cone: Radius of Circle on the cone and in the plane passing through the position.
    ##             double   *radius_or_angle : Cone: Half Angle. 
    ##             logical  *sense           : Indicates the sense of normal
    ##         
    ##  @return A tuple consisting of (position, dir, radius, radius_or_angle, sense). 
    ##  - position is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - dir is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - radius is: float.
    ##  - radius_or_angle is: float.
    ##  - sense is: bool.

    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    def GetSurfaceData(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d, float, float, bool]:
        """
         Returns the surface information for this face 
               
                    tag_t    faceted_face     : The input edge tag for which face information is required.
                    PNT3_p_t position         : Plane: Position on Plane
                                                Origin for other
                    PNT3_p_t dir              : Plane: Normal direction
                                                Axis for others.
                    double   *radius          : Not applicable for planes
                                                Cylinder: Radius of Cylinder, 
                                                Sphere: Radius of Sphere
                                                Cone: Radius of Circle on the cone and in the plane passing through the position.
                    double   *radius_or_angle : Cone: Half Angle. 
                    logical  *sense           : Indicates the sense of normal
                
         @return A tuple consisting of (position, dir, radius, radius_or_angle, sense). 
         - position is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - dir is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - radius is: float.
         - radius_or_angle is: float.
         - sense is: bool.

        """
        pass
    
##  The structure of JA faceting parameters 
class FacetingParameters:
    """
     The structure of JA faceting parameters 
    """
    ## Getter for property :(int) MaximumFacetEdges
    ## The maximum number of edges allowed                                               in the facets that are to be generated                                                (this does not apply to JT).
    ## @return int
    @property
    def MaximumFacetEdges(self) -> int:
        """
        Getter for property MaximumFacetEdges
        The maximum number of edges allowed                                               in the facets that are to be generated                                                (this does not apply to JT).

        """
        pass
    
    ## Setter for property :(int) MaximumFacetEdges
    @MaximumFacetEdges.setter
    def MaximumFacetEdges(self, value: int):
        """
        Getter for property MaximumFacetEdges
        The maximum number of edges allowed                                               in the facets that are to be generated                                                (this does not apply to JT).
        Setter for property MaximumFacetEdges
        The maximum number of edges allowed                                               in the facets that are to be generated                                                (this does not apply to JT).

        """
        pass
    
    ## Getter for property :(bool) SpecifySurfaceTolerance
    ## If this value is true, then                                               values must be specified for                                               surfaceDistanceTolerance                                               and surfaceAngularTolerance.
    ## @return bool
    @property
    def SpecifySurfaceTolerance(self) -> bool:
        """
        Getter for property SpecifySurfaceTolerance
        If this value is true, then                                               values must be specified for                                               surfaceDistanceTolerance                                               and surfaceAngularTolerance.

        """
        pass
    
    ## Setter for property :(bool) SpecifySurfaceTolerance
    @SpecifySurfaceTolerance.setter
    def SpecifySurfaceTolerance(self, value: bool):
        """
        Getter for property SpecifySurfaceTolerance
        If this value is true, then                                               values must be specified for                                               surfaceDistanceTolerance                                               and surfaceAngularTolerance.
        Setter for property SpecifySurfaceTolerance
        If this value is true, then                                               values must be specified for                                               surfaceDistanceTolerance                                               and surfaceAngularTolerance.

        """
        pass
    
    ## Getter for property :(float) SurfaceDistanceTolerance
    ## This is the maximum distance from                                               the surface to the facet.
    ## @return float
    @property
    def SurfaceDistanceTolerance(self) -> float:
        """
        Getter for property SurfaceDistanceTolerance
        This is the maximum distance from                                               the surface to the facet.

        """
        pass
    
    ## Setter for property :(float) SurfaceDistanceTolerance
    @SurfaceDistanceTolerance.setter
    def SurfaceDistanceTolerance(self, value: float):
        """
        Getter for property SurfaceDistanceTolerance
        This is the maximum distance from                                               the surface to the facet.
        Setter for property SurfaceDistanceTolerance
        This is the maximum distance from                                               the surface to the facet.

        """
        pass
    
    ## Getter for property :(float) SurfaceAngularTolerance
    ## This is the maximum angular variation                                               in radians of the surface normal                                               over the facet.
    ## @return float
    @property
    def SurfaceAngularTolerance(self) -> float:
        """
        Getter for property SurfaceAngularTolerance
        This is the maximum angular variation                                               in radians of the surface normal                                               over the facet.

        """
        pass
    
    ## Setter for property :(float) SurfaceAngularTolerance
    @SurfaceAngularTolerance.setter
    def SurfaceAngularTolerance(self, value: float):
        """
        Getter for property SurfaceAngularTolerance
        This is the maximum angular variation                                               in radians of the surface normal                                               over the facet.
        Setter for property SurfaceAngularTolerance
        This is the maximum angular variation                                               in radians of the surface normal                                               over the facet.

        """
        pass
    
    ## Getter for property :(bool) SpecifyCurveTolerance
    ## This indicates that values are to be                                               specified for curveDistanceTolerance                                               and curveAngularTolerance and                                               curve_max_length.
    ## @return bool
    @property
    def SpecifyCurveTolerance(self) -> bool:
        """
        Getter for property SpecifyCurveTolerance
        This indicates that values are to be                                               specified for curveDistanceTolerance                                               and curveAngularTolerance and                                               curve_max_length.

        """
        pass
    
    ## Setter for property :(bool) SpecifyCurveTolerance
    @SpecifyCurveTolerance.setter
    def SpecifyCurveTolerance(self, value: bool):
        """
        Getter for property SpecifyCurveTolerance
        This indicates that values are to be                                               specified for curveDistanceTolerance                                               and curveAngularTolerance and                                               curve_max_length.
        Setter for property SpecifyCurveTolerance
        This indicates that values are to be                                               specified for curveDistanceTolerance                                               and curveAngularTolerance and                                               curve_max_length.

        """
        pass
    
    ## Getter for property :(float) CurveDistanceTolerance
    ## This is the maximum distance between                                               the facet edge and the curve segment                                               represented by the facet edge.
    ## @return float
    @property
    def CurveDistanceTolerance(self) -> float:
        """
        Getter for property CurveDistanceTolerance
        This is the maximum distance between                                               the facet edge and the curve segment                                               represented by the facet edge.

        """
        pass
    
    ## Setter for property :(float) CurveDistanceTolerance
    @CurveDistanceTolerance.setter
    def CurveDistanceTolerance(self, value: float):
        """
        Getter for property CurveDistanceTolerance
        This is the maximum distance between                                               the facet edge and the curve segment                                               represented by the facet edge.
        Setter for property CurveDistanceTolerance
        This is the maximum distance between                                               the facet edge and the curve segment                                               represented by the facet edge.

        """
        pass
    
    ## Getter for property :(float) CurveAngularTolerance
    ## This is the maximum angular variation                                               in radians of the curve tangent along                                               the curve segment represented by the                                               facet edge.
    ## @return float
    @property
    def CurveAngularTolerance(self) -> float:
        """
        Getter for property CurveAngularTolerance
        This is the maximum angular variation                                               in radians of the curve tangent along                                               the curve segment represented by the                                               facet edge.

        """
        pass
    
    ## Setter for property :(float) CurveAngularTolerance
    @CurveAngularTolerance.setter
    def CurveAngularTolerance(self, value: float):
        """
        Getter for property CurveAngularTolerance
        This is the maximum angular variation                                               in radians of the curve tangent along                                               the curve segment represented by the                                               facet edge.
        Setter for property CurveAngularTolerance
        This is the maximum angular variation                                               in radians of the curve tangent along                                               the curve segment represented by the                                               facet edge.

        """
        pass
    
    ## Getter for property :(float) CurveMaximumLength
    ## The maximum length of a curve, default is 1000.
    ## @return float
    @property
    def CurveMaximumLength(self) -> float:
        """
        Getter for property CurveMaximumLength
        The maximum length of a curve, default is 1000.

        """
        pass
    
    ## Setter for property :(float) CurveMaximumLength
    @CurveMaximumLength.setter
    def CurveMaximumLength(self, value: float):
        """
        Getter for property CurveMaximumLength
        The maximum length of a curve, default is 1000.
        Setter for property CurveMaximumLength
        The maximum length of a curve, default is 1000.

        """
        pass
    
    ## Getter for property :(bool) SpecifyConvexFacets
    ## This indicates that the facets                                               generated by the faceter should all be                                               convex (this does not apply to JT).
    ## @return bool
    @property
    def SpecifyConvexFacets(self) -> bool:
        """
        Getter for property SpecifyConvexFacets
        This indicates that the facets                                               generated by the faceter should all be                                               convex (this does not apply to JT).

        """
        pass
    
    ## Setter for property :(bool) SpecifyConvexFacets
    @SpecifyConvexFacets.setter
    def SpecifyConvexFacets(self, value: bool):
        """
        Getter for property SpecifyConvexFacets
        This indicates that the facets                                               generated by the faceter should all be                                               convex (this does not apply to JT).
        Setter for property SpecifyConvexFacets
        This indicates that the facets                                               generated by the faceter should all be                                               convex (this does not apply to JT).

        """
        pass
    
    ## Getter for property :(bool) SpecifyMaximumFacetSize
    ## This indicates that a maximum width of                                               facet is to be specified using                                               maximumFacetSize.
    ## @return bool
    @property
    def SpecifyMaximumFacetSize(self) -> bool:
        """
        Getter for property SpecifyMaximumFacetSize
        This indicates that a maximum width of                                               facet is to be specified using                                               maximumFacetSize.

        """
        pass
    
    ## Setter for property :(bool) SpecifyMaximumFacetSize
    @SpecifyMaximumFacetSize.setter
    def SpecifyMaximumFacetSize(self, value: bool):
        """
        Getter for property SpecifyMaximumFacetSize
        This indicates that a maximum width of                                               facet is to be specified using                                               maximumFacetSize.
        Setter for property SpecifyMaximumFacetSize
        This indicates that a maximum width of                                               facet is to be specified using                                               maximumFacetSize.

        """
        pass
    
    ## Getter for property :(float) MaximumFacetSize
    ## This is the maximum width of a facet.
    ## @return float
    @property
    def MaximumFacetSize(self) -> float:
        """
        Getter for property MaximumFacetSize
        This is the maximum width of a facet.

        """
        pass
    
    ## Setter for property :(float) MaximumFacetSize
    @MaximumFacetSize.setter
    def MaximumFacetSize(self, value: float):
        """
        Getter for property MaximumFacetSize
        This is the maximum width of a facet.
        Setter for property MaximumFacetSize
        This is the maximum width of a facet.

        """
        pass
    
    ## Getter for property :(bool) SpecifyParameters
    ## This indicates that the model will be                                               created with the parametric information                                               for each vertex.
    ## @return bool
    @property
    def SpecifyParameters(self) -> bool:
        """
        Getter for property SpecifyParameters
        This indicates that the model will be                                               created with the parametric information                                               for each vertex.

        """
        pass
    
    ## Setter for property :(bool) SpecifyParameters
    @SpecifyParameters.setter
    def SpecifyParameters(self, value: bool):
        """
        Getter for property SpecifyParameters
        This indicates that the model will be                                               created with the parametric information                                               for each vertex.
        Setter for property SpecifyParameters
        This indicates that the model will be                                               created with the parametric information                                               for each vertex.

        """
        pass
    
    ## Getter for property :(int) NumberStorageType
    ## This indicates whether the real                                               numbers for facet vertices and facet                                               normals should be stored as floats                                               (UF_FACET_TYPE_FLOAT) or as doubles                                               (UF_FACET_TYPE_DOUBLE).
    ## @return int
    @property
    def NumberStorageType(self) -> int:
        """
        Getter for property NumberStorageType
        This indicates whether the real                                               numbers for facet vertices and facet                                               normals should be stored as floats                                               (UF_FACET_TYPE_FLOAT) or as doubles                                               (UF_FACET_TYPE_DOUBLE).

        """
        pass
    
    ## Setter for property :(int) NumberStorageType
    @NumberStorageType.setter
    def NumberStorageType(self, value: int):
        """
        Getter for property NumberStorageType
        This indicates whether the real                                               numbers for facet vertices and facet                                               normals should be stored as floats                                               (UF_FACET_TYPE_FLOAT) or as doubles                                               (UF_FACET_TYPE_DOUBLE).
        Setter for property NumberStorageType
        This indicates whether the real                                               numbers for facet vertices and facet                                               normals should be stored as floats                                               (UF_FACET_TYPE_FLOAT) or as doubles                                               (UF_FACET_TYPE_DOUBLE).

        """
        pass
    
    ## Getter for property :(bool) SpecifyViewDirection
    ## Should we use a viewing direction                                               for denser faceting around                                               silhouettes.
    ## @return bool
    @property
    def SpecifyViewDirection(self) -> bool:
        """
        Getter for property SpecifyViewDirection
        Should we use a viewing direction                                               for denser faceting around                                               silhouettes.

        """
        pass
    
    ## Setter for property :(bool) SpecifyViewDirection
    @SpecifyViewDirection.setter
    def SpecifyViewDirection(self, value: bool):
        """
        Getter for property SpecifyViewDirection
        Should we use a viewing direction                                               for denser faceting around                                               silhouettes.
        Setter for property SpecifyViewDirection
        Should we use a viewing direction                                               for denser faceting around                                               silhouettes.

        """
        pass
    
    ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) SilhouetteViewDirection
    ## If specifyViewDirection is specified,                                               then this is the view direction to use                                               (this does not apply to JT).
    ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
    @property
    def SilhouetteViewDirection(self) -> NXOpen.Vector3d:
        """
        Getter for property SilhouetteViewDirection
        If specifyViewDirection is specified,                                               then this is the view direction to use                                               (this does not apply to JT).

        """
        pass
    
    ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) SilhouetteViewDirection
    @SilhouetteViewDirection.setter
    def SilhouetteViewDirection(self, value: NXOpen.Vector3d):
        """
        Getter for property SilhouetteViewDirection
        If specifyViewDirection is specified,                                               then this is the view direction to use                                               (this does not apply to JT).
        Setter for property SilhouetteViewDirection
        If specifyViewDirection is specified,                                               then this is the view direction to use                                               (this does not apply to JT).

        """
        pass
    
    ## Getter for property :(float) SilhouetteChordTolerance
    ## If specifyViewDirection is specified                                               then this is the tolerance which will be                                               used as a tighter surface tolerance                                               in the silhouette area specified                                               by the view direction (this does not apply to JT).
    ## @return float
    @property
    def SilhouetteChordTolerance(self) -> float:
        """
        Getter for property SilhouetteChordTolerance
        If specifyViewDirection is specified                                               then this is the tolerance which will be                                               used as a tighter surface tolerance                                               in the silhouette area specified                                               by the view direction (this does not apply to JT).

        """
        pass
    
    ## Setter for property :(float) SilhouetteChordTolerance
    @SilhouetteChordTolerance.setter
    def SilhouetteChordTolerance(self, value: float):
        """
        Getter for property SilhouetteChordTolerance
        If specifyViewDirection is specified                                               then this is the tolerance which will be                                               used as a tighter surface tolerance                                               in the silhouette area specified                                               by the view direction (this does not apply to JT).
        Setter for property SilhouetteChordTolerance
        If specifyViewDirection is specified                                               then this is the tolerance which will be                                               used as a tighter surface tolerance                                               in the silhouette area specified                                               by the view direction (this does not apply to JT).

        """
        pass
    
    ## Getter for property :(bool) StoreFaceTag
    ## Should this FACET body record face tags or not                                                (this does not apply to JT).
    ## @return bool
    @property
    def StoreFaceTag(self) -> bool:
        """
        Getter for property StoreFaceTag
        Should this FACET body record face tags or not                                                (this does not apply to JT).

        """
        pass
    
    ## Setter for property :(bool) StoreFaceTag
    @StoreFaceTag.setter
    def StoreFaceTag(self, value: bool):
        """
        Getter for property StoreFaceTag
        Should this FACET body record face tags or not                                                (this does not apply to JT).
        Setter for property StoreFaceTag
        Should this FACET body record face tags or not                                                (this does not apply to JT).

        """
        pass
    
    ## Getter for property :(bool) WithLODS
    ## When creating a JT facet body whether to create LODs or not                                                (this does not apply to NX).
    ## @return bool
    @property
    def WithLODS(self) -> bool:
        """
        Getter for property WithLODS
        When creating a JT facet body whether to create LODs or not                                                (this does not apply to NX).

        """
        pass
    
    ## Setter for property :(bool) WithLODS
    @WithLODS.setter
    def WithLODS(self, value: bool):
        """
        Getter for property WithLODS
        When creating a JT facet body whether to create LODs or not                                                (this does not apply to NX).
        Setter for property WithLODS
        When creating a JT facet body whether to create LODs or not                                                (this does not apply to NX).

        """
        pass
    


import NXOpen
import NXOpen.Features
##  Collection of freeform facet operations.  <br> To obtain an instance of this class, refer to @link NXOpen::Facet::FacetedBodyCollection  NXOpen::Facet::FacetedBodyCollection @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class FacetModelingCollection(NXOpen.Object): 
    """ Collection of freeform facet operations. """


    ##  Creates a @link NXOpen::Facet::CleanupFacetBodyBuilder NXOpen::Facet::CleanupFacetBodyBuilder@endlink  
    ##  @return builder (@link CleanupFacetBodyBuilder NXOpen.Facet.CleanupFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateCleanupFacetBodyBuilder(self) -> CleanupFacetBodyBuilder:
        """
         Creates a @link NXOpen::Facet::CleanupFacetBodyBuilder NXOpen::Facet::CleanupFacetBodyBuilder@endlink  
         @return builder (@link CleanupFacetBodyBuilder NXOpen.Facet.CleanupFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::CleanupFacetBodyWizardBuilder NXOpen::Facet::CleanupFacetBodyWizardBuilder@endlink  
    ##  @return builder (@link CleanupFacetBodyWizardBuilder NXOpen.Facet.CleanupFacetBodyWizardBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateCleanupFacetBodyWizardBuilder(self) -> CleanupFacetBodyWizardBuilder:
        """
         Creates a @link NXOpen::Facet::CleanupFacetBodyWizardBuilder NXOpen::Facet::CleanupFacetBodyWizardBuilder@endlink  
         @return builder (@link CleanupFacetBodyWizardBuilder NXOpen.Facet.CleanupFacetBodyWizardBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::CombineFacetBodiesBuilder NXOpen::Facet::CombineFacetBodiesBuilder@endlink  
    ##  @return builder (@link CombineFacetBodiesBuilder NXOpen.Facet.CombineFacetBodiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreateCombineFacetBodiesBuilder(self) -> CombineFacetBodiesBuilder:
        """
         Creates a @link NXOpen::Facet::CombineFacetBodiesBuilder NXOpen::Facet::CombineFacetBodiesBuilder@endlink  
         @return builder (@link CombineFacetBodiesBuilder NXOpen.Facet.CombineFacetBodiesBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::CombineFacetBodyBuilder NXOpen::Facet::CombineFacetBodyBuilder@endlink  
    ##  @return builder (@link CombineFacetBodyBuilder NXOpen.Facet.CombineFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateCombineFacetBodyBuilder(self) -> CombineFacetBodyBuilder:
        """
         Creates a @link NXOpen::Facet::CombineFacetBodyBuilder NXOpen::Facet::CombineFacetBodyBuilder@endlink  
         @return builder (@link CombineFacetBodyBuilder NXOpen.Facet.CombineFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::ConvertFacetBodyBuilder NXOpen::Facet::ConvertFacetBodyBuilder@endlink  
    ##  @return builder (@link ConvertFacetBodyBuilder NXOpen.Facet.ConvertFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    def CreateConvertFacetBodyBuilder(self) -> ConvertFacetBodyBuilder:
        """
         Creates a @link NXOpen::Facet::ConvertFacetBodyBuilder NXOpen::Facet::ConvertFacetBodyBuilder@endlink  
         @return builder (@link ConvertFacetBodyBuilder NXOpen.Facet.ConvertFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::CreateTransitionBuilder NXOpen::Facet::CreateTransitionBuilder@endlink  object 
    ##  @return builder (@link CreateTransitionBuilder NXOpen.Facet.CreateTransitionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreateCreateTransitionBuilder(self) -> CreateTransitionBuilder:
        """
         Creates a @link NXOpen::Facet::CreateTransitionBuilder NXOpen::Facet::CreateTransitionBuilder@endlink  object 
         @return builder (@link CreateTransitionBuilder NXOpen.Facet.CreateTransitionBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::DetectPrimitivesBuilder NXOpen::Facet::DetectPrimitivesBuilder@endlink  object. 
    ##  @return builder (@link DetectPrimitivesBuilder NXOpen.Facet.DetectPrimitivesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateDetectPrimitivesBuilder(self) -> DetectPrimitivesBuilder:
        """
         Creates a @link NXOpen::Facet::DetectPrimitivesBuilder NXOpen::Facet::DetectPrimitivesBuilder@endlink  object. 
         @return builder (@link DetectPrimitivesBuilder NXOpen.Facet.DetectPrimitivesBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::DivideFacetFaceBuilder NXOpen::Facet::DivideFacetFaceBuilder@endlink  
    ##  @return builder (@link DivideFacetFaceBuilder NXOpen.Facet.DivideFacetFaceBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreateDivideFacetFaceBuilder(self) -> DivideFacetFaceBuilder:
        """
         Creates a @link NXOpen::Facet::DivideFacetFaceBuilder NXOpen::Facet::DivideFacetFaceBuilder@endlink  
         @return builder (@link DivideFacetFaceBuilder NXOpen.Facet.DivideFacetFaceBuilder@endlink): .
        """
        pass
    
    ##  Create a @link NXOpen::Facet::AdjustMinimumRadiusBuilder NXOpen::Facet::AdjustMinimumRadiusBuilder@endlink  object. 
    ##  @return builder (@link AdjustMinimumRadiusBuilder NXOpen.Facet.AdjustMinimumRadiusBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def CreateFacetAdjustMinimumRadiusBuilder(self) -> AdjustMinimumRadiusBuilder:
        """
         Create a @link NXOpen::Facet::AdjustMinimumRadiusBuilder NXOpen::Facet::AdjustMinimumRadiusBuilder@endlink  object. 
         @return builder (@link AdjustMinimumRadiusBuilder NXOpen.Facet.AdjustMinimumRadiusBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::FacetBodyFromBodyBuilder NXOpen::Facet::FacetBodyFromBodyBuilder@endlink  
    ##  @return builder (@link FacetBodyFromBodyBuilder NXOpen.Facet.FacetBodyFromBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateFacetBodyFromBodyBuilder(self) -> FacetBodyFromBodyBuilder:
        """
         Creates a @link NXOpen::Facet::FacetBodyFromBodyBuilder NXOpen::Facet::FacetBodyFromBodyBuilder@endlink  
         @return builder (@link FacetBodyFromBodyBuilder NXOpen.Facet.FacetBodyFromBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::FillMeshBuilder NXOpen::Facet::FillMeshBuilder@endlink  
    ##  @return builder (@link FillMeshBuilder NXOpen.Facet.FillMeshBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreateFillMeshBuilder(self) -> FillMeshBuilder:
        """
         Creates a @link NXOpen::Facet::FillMeshBuilder NXOpen::Facet::FillMeshBuilder@endlink  
         @return builder (@link FillMeshBuilder NXOpen.Facet.FillMeshBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Facet::LocalOffsetBuilder Facet::LocalOffsetBuilder@endlink  
    ##  @return builder (@link LocalOffsetBuilder NXOpen.Facet.LocalOffsetBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreateLocalOffsetBuilder(self) -> LocalOffsetBuilder:
        """
         Creates a @link Facet::LocalOffsetBuilder Facet::LocalOffsetBuilder@endlink  
         @return builder (@link LocalOffsetBuilder NXOpen.Facet.LocalOffsetBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::MergeFacetFacesBuilder NXOpen::Facet::MergeFacetFacesBuilder@endlink  
    ##  @return builder (@link MergeFacetFacesBuilder NXOpen.Facet.MergeFacetFacesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreateMergeFacetFacesBuilder(self) -> MergeFacetFacesBuilder:
        """
         Creates a @link NXOpen::Facet::MergeFacetFacesBuilder NXOpen::Facet::MergeFacetFacesBuilder@endlink  
         @return builder (@link MergeFacetFacesBuilder NXOpen.Facet.MergeFacetFacesBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::MeshFromCloudBuilder NXOpen::Facet::MeshFromCloudBuilder@endlink  
    ##  @return builder (@link MeshFromCloudBuilder NXOpen.Facet.MeshFromCloudBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreateMeshFromCloudBuilder(self) -> MeshFromCloudBuilder:
        """
         Creates a @link NXOpen::Facet::MeshFromCloudBuilder NXOpen::Facet::MeshFromCloudBuilder@endlink  
         @return builder (@link MeshFromCloudBuilder NXOpen.Facet.MeshFromCloudBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::PaintBrushBuilder NXOpen::Facet::PaintBrushBuilder@endlink  object. 
    ##  @return builder (@link PaintBrushBuilder NXOpen.Facet.PaintBrushBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreatePaintBrushBuilder(self) -> PaintBrushBuilder:
        """
         Creates a @link NXOpen::Facet::PaintBrushBuilder NXOpen::Facet::PaintBrushBuilder@endlink  object. 
         @return builder (@link PaintBrushBuilder NXOpen.Facet.PaintBrushBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::PaintFacetBodyBuilder NXOpen::Facet::PaintFacetBodyBuilder@endlink  object. 
    ##  @return builder (@link PaintFacetBodyBuilder NXOpen.Facet.PaintFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def CreatePaintFacetBodyBuilder(self) -> PaintFacetBodyBuilder:
        """
         Creates a @link NXOpen::Facet::PaintFacetBodyBuilder NXOpen::Facet::PaintFacetBodyBuilder@endlink  object. 
         @return builder (@link PaintFacetBodyBuilder NXOpen.Facet.PaintFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::PlugLeakageBuilder NXOpen::Facet::PlugLeakageBuilder@endlink  
    ##  @return builder (@link PlugLeakageBuilder NXOpen.Facet.PlugLeakageBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreatePlugLeakageBuilder(self) -> PlugLeakageBuilder:
        """
         Creates a @link NXOpen::Facet::PlugLeakageBuilder NXOpen::Facet::PlugLeakageBuilder@endlink  
         @return builder (@link PlugLeakageBuilder NXOpen.Facet.PlugLeakageBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::PolygonModelingBuilder NXOpen::Facet::PolygonModelingBuilder@endlink  
    ##  @return builder (@link PolygonModelingBuilder NXOpen.Facet.PolygonModelingBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreatePolygonModelingBuilder(self) -> PolygonModelingBuilder:
        """
         Creates a @link NXOpen::Facet::PolygonModelingBuilder NXOpen::Facet::PolygonModelingBuilder@endlink  
         @return builder (@link PolygonModelingBuilder NXOpen.Facet.PolygonModelingBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Facet::RemeshFacetBodyBuilder Facet::RemeshFacetBodyBuilder@endlink  
    ##  @return builder (@link RemeshFacetBodyBuilder NXOpen.Facet.RemeshFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreateRemeshFacetBodyBuilder(self) -> RemeshFacetBodyBuilder:
        """
         Creates a @link Facet::RemeshFacetBodyBuilder Facet::RemeshFacetBodyBuilder@endlink  
         @return builder (@link RemeshFacetBodyBuilder NXOpen.Facet.RemeshFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Facet::ReplaceMeshWithFaceBuilder Facet::ReplaceMeshWithFaceBuilder@endlink  
    ##  @return builder (@link ReplaceMeshWithFaceBuilder NXOpen.Facet.ReplaceMeshWithFaceBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreateReplaceMeshWithFaceBuilder(self) -> ReplaceMeshWithFaceBuilder:
        """
         Creates a @link Facet::ReplaceMeshWithFaceBuilder Facet::ReplaceMeshWithFaceBuilder@endlink  
         @return builder (@link ReplaceMeshWithFaceBuilder NXOpen.Facet.ReplaceMeshWithFaceBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::SculptMeshBuilder NXOpen::Facet::SculptMeshBuilder@endlink  
    ##  @return builder (@link SculptMeshBuilder NXOpen.Facet.SculptMeshBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreateSculptMeshBuilder(self) -> SculptMeshBuilder:
        """
         Creates a @link NXOpen::Facet::SculptMeshBuilder NXOpen::Facet::SculptMeshBuilder@endlink  
         @return builder (@link SculptMeshBuilder NXOpen.Facet.SculptMeshBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::SplitCurveMethodBuilder NXOpen::Facet::SplitCurveMethodBuilder@endlink  
    ##  @return builder (@link SplitCurveMethodBuilder NXOpen.Facet.SplitCurveMethodBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreateSplitCurveMethodBuilder(self) -> SplitCurveMethodBuilder:
        """
         Creates a @link NXOpen::Facet::SplitCurveMethodBuilder NXOpen::Facet::SplitCurveMethodBuilder@endlink  
         @return builder (@link SplitCurveMethodBuilder NXOpen.Facet.SplitCurveMethodBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::SplitCurveMethodListDataManager NXOpen::Facet::SplitCurveMethodListDataManager@endlink  
    ##  @return dataManager (@link SplitCurveMethodListDataManager NXOpen.Facet.SplitCurveMethodListDataManager@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreateSplitCurveMethodListDataManager(self) -> SplitCurveMethodListDataManager:
        """
         Creates a @link NXOpen::Facet::SplitCurveMethodListDataManager NXOpen::Facet::SplitCurveMethodListDataManager@endlink  
         @return dataManager (@link SplitCurveMethodListDataManager NXOpen.Facet.SplitCurveMethodListDataManager@endlink): .
        """
        pass
    
    ##  Creates a @link Features::TubeLatticeBuilder Features::TubeLatticeBuilder@endlink  
    ##  @return builder (@link NXOpen.Features.TubeLatticeBuilder NXOpen.Features.TubeLatticeBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ## <param name="tube_lattice"> (@link NXOpen.Features.TubeLattice NXOpen.Features.TubeLattice@endlink)  @link NXOpen::Features::TubeLattice NXOpen::Features::TubeLattice@endlink  to be edited </param>
    def CreateTubeLatticeBuilder(self, tube_lattice: NXOpen.Features.TubeLattice) -> NXOpen.Features.TubeLatticeBuilder:
        """
         Creates a @link Features::TubeLatticeBuilder Features::TubeLatticeBuilder@endlink  
         @return builder (@link NXOpen.Features.TubeLatticeBuilder NXOpen.Features.TubeLatticeBuilder@endlink):  .
        """
        pass
    
    ##  Creates a @link NXOpen::Facet::WrapMeshBuilder NXOpen::Facet::WrapMeshBuilder@endlink  
    ##  @return builder (@link WrapMeshBuilder NXOpen.Facet.WrapMeshBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreateWrapMeshBuilder(self) -> WrapMeshBuilder:
        """
         Creates a @link NXOpen::Facet::WrapMeshBuilder NXOpen::Facet::WrapMeshBuilder@endlink  
         @return builder (@link WrapMeshBuilder NXOpen.Facet.WrapMeshBuilder@endlink): .
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::FeatureExtractionBuilder NXOpen::Facet::FeatureExtractionBuilder@endlink 
##     It extracts feature lines or separates regions of different curvature
##     from a facet body based on the curvature map.
##     For facet body curvature, please see @link NXOpen::Facet::CurvatureBuilder NXOpen::Facet::CurvatureBuilder@endlink .
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateFacetFeatureExtractionBuilder  NXOpen::Facet::FacetedBodyCollection::CreateFacetFeatureExtractionBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class FeatureExtractionBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.FeatureExtractionBuilder</ja_class>
    It extracts feature lines or separates regions of different curvature
    from a facet body based on the curvature map.
    For facet body curvature, please see <ja_class>NXOpen.Facet.CurvatureBuilder</ja_class>.
    """


    ##  Specifies how to handle the input facet bodies. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Blank</term><description> 
    ##  Blank the input facet bodies </description> </item><item><term> 
    ## Retain</term><description> 
    ##  Retain the input facet bodies </description> </item><item><term> 
    ## Delete</term><description> 
    ##  Delete the input facet bodies </description> </item></list>
    class InputActions(Enum):
        """
        Members Include: <Blank> <Retain> <Delete>
        """
        Blank: int
        Retain: int
        Delete: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FeatureExtractionBuilder.InputActions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AreBordersEnabled
    ##  Returns the extracting borders option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def AreBordersEnabled(self) -> bool:
        """
        Getter for property: (bool) AreBordersEnabled
         Returns the extracting borders option   
            
         
        """
        pass
    
    ## Setter for property: (bool) AreBordersEnabled

    ##  Returns the extracting borders option   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @AreBordersEnabled.setter
    def AreBordersEnabled(self, bordersEnabled: bool):
        """
        Setter for property: (bool) AreBordersEnabled
         Returns the extracting borders option   
            
         
        """
        pass
    
    ## Getter for property: (bool) AreRegionsEnabled
    ##  Returns  the extracting regions option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def AreRegionsEnabled(self) -> bool:
        """
        Getter for property: (bool) AreRegionsEnabled
         Returns  the extracting regions option   
            
         
        """
        pass
    
    ## Setter for property: (bool) AreRegionsEnabled

    ##  Returns  the extracting regions option   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @AreRegionsEnabled.setter
    def AreRegionsEnabled(self, regionsEnabled: bool):
        """
        Setter for property: (bool) AreRegionsEnabled
         Returns  the extracting regions option   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) FacetBodies
    ##  Returns the input facet body selection list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return SelectFacetedBodyList
    @property
    def FacetBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) FacetBodies
         Returns the input facet body selection list   
            
         
        """
        pass
    
    ## Getter for property: (@link FeatureExtractionBuilder.InputActions NXOpen.Facet.FeatureExtractionBuilder.InputActions@endlink) InputAction
    ##  Returns the input facet body action   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FeatureExtractionBuilder.InputActions
    @property
    def InputAction(self) -> FeatureExtractionBuilder.InputActions:
        """
        Getter for property: (@link FeatureExtractionBuilder.InputActions NXOpen.Facet.FeatureExtractionBuilder.InputActions@endlink) InputAction
         Returns the input facet body action   
            
         
        """
        pass
    
    ## Setter for property: (@link FeatureExtractionBuilder.InputActions NXOpen.Facet.FeatureExtractionBuilder.InputActions@endlink) InputAction

    ##  Returns the input facet body action   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @InputAction.setter
    def InputAction(self, inputAction: FeatureExtractionBuilder.InputActions):
        """
        Setter for property: (@link FeatureExtractionBuilder.InputActions NXOpen.Facet.FeatureExtractionBuilder.InputActions@endlink) InputAction
         Returns the input facet body action   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsSmoothingEnabled
    ##  Returns the smoothing option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def IsSmoothingEnabled(self) -> bool:
        """
        Getter for property: (bool) IsSmoothingEnabled
         Returns the smoothing option   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsSmoothingEnabled

    ##  Returns the smoothing option   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @IsSmoothingEnabled.setter
    def IsSmoothingEnabled(self, smoothingEnabled: bool):
        """
        Setter for property: (bool) IsSmoothingEnabled
         Returns the smoothing option   
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumBorderLength
    ##  Returns the minimum border length   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MinimumBorderLength(self) -> float:
        """
        Getter for property: (float) MinimumBorderLength
         Returns the minimum border length   
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumBorderLength

    ##  Returns the minimum border length   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MinimumBorderLength.setter
    def MinimumBorderLength(self, minimumBorderLength: float):
        """
        Setter for property: (float) MinimumBorderLength
         Returns the minimum border length   
            
         
        """
        pass
    
    ## Getter for property: (float) SmoothingFactor
    ##  Returns the smoothing factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def SmoothingFactor(self) -> float:
        """
        Getter for property: (float) SmoothingFactor
         Returns the smoothing factor   
            
         
        """
        pass
    
    ## Setter for property: (float) SmoothingFactor

    ##  Returns the smoothing factor   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SmoothingFactor.setter
    def SmoothingFactor(self, smoothingFactor: float):
        """
        Setter for property: (float) SmoothingFactor
         Returns the smoothing factor   
            
         
        """
        pass
    
    ##  Gets the extracted curves. Call @link Builder::Commit Builder::Commit@endlink  before calling this method. 
    ##  @return borders (@link NXOpen.Spline List[NXOpen.Spline]@endlink):  The extracted curves.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def GetExtractedBorders(self) -> List[NXOpen.Spline]:
        """
         Gets the extracted curves. Call @link Builder::Commit Builder::Commit@endlink  before calling this method. 
         @return borders (@link NXOpen.Spline List[NXOpen.Spline]@endlink):  The extracted curves.
        """
        pass
    
    ##  Gets the extracted facet bodies. Call @link Builder::Commit Builder::Commit@endlink  before calling this method. 
    ##  @return regions (@link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink):  The extracted facet bodies .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def GetExtractedRegions(self) -> List[FacetedBody]:
        """
         Gets the extracted facet bodies. Call @link Builder::Commit Builder::Commit@endlink  before calling this method. 
         @return regions (@link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink):  The extracted facet bodies .
        """
        pass
    
import NXOpen
##  This class finds and fills holes to a prescribed boundary smoothness condition.
##         Inputs to this class can be convergent objects.  <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateFillHoleBuilder  NXOpen::Facet::FacetedBodyCollection::CreateFillHoleBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## IsEditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## MaxEdges </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SmoothType </term> <description> 
##  
## Linear </description> </item> 
## 
## <item><term> 
##  
## TargetType </term> <description> 
##  
## UserDefined </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX6.0.0  <br> 

class FillHoleBuilder(NXOpen.Builder): 
    """ This class finds and fills holes to a prescribed boundary smoothness condition.
        Inputs to this class can be convergent objects. """


    ##  Smoothness and boundary continuity options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  Linear (triangulated) fill. </description> </item><item><term> 
    ## Refined</term><description> 
    ##  Smooth internal fill. </description> </item><item><term> 
    ## TangentBased</term><description> 
    ##  Smooth fill, boundary is based on facet body tangent. </description> </item><item><term> 
    ## CurvatureBased</term><description> 
    ##  Smooth fill, boundary is based on facet body curvature. </description> </item></list>
    class SmoothTypes(Enum):
        """
        Members Include: <Linear> <Refined> <TangentBased> <CurvatureBased>
        """
        Linear: int
        Refined: int
        TangentBased: int
        CurvatureBased: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FillHoleBuilder.SmoothTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Options defining how to target holes for filling. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## UserDefined</term><description> 
    ##  Fills user-defined target holes. </description> </item><item><term> 
    ## ByNumberOfEdges</term><description> 
    ##  Automatically target holes based on number of edges. </description> </item></list>
    class TargetTypes(Enum):
        """
        Members Include: <UserDefined> <ByNumberOfEdges>
        """
        UserDefined: int
        ByNumberOfEdges: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FillHoleBuilder.TargetTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Hole filling type options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FillHole</term><description> 
    ##  Fills individual hole(s). </description> </item><item><term> 
    ## FillIsland</term><description> 
    ##  Fills a hole defined by inner island and outer facet body. </description> </item><item><term> 
    ## BridgeGap</term><description> 
    ##  Bridges some open boundary edges with a linear fill. </description> </item></list>
    class Types(Enum):
        """
        Members Include: <FillHole> <FillIsland> <BridgeGap>
        """
        FillHole: int
        FillIsland: int
        BridgeGap: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FillHoleBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectICurveList NXOpen.SelectICurveList@endlink) BridgeEdges1
    ##  Returns the first list of edges when bridging holes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectICurveList
    @property
    def BridgeEdges1(self) -> NXOpen.SelectICurveList:
        """
        Getter for property: (@link NXOpen.SelectICurveList NXOpen.SelectICurveList@endlink) BridgeEdges1
         Returns the first list of edges when bridging holes.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectICurveList NXOpen.SelectICurveList@endlink) BridgeEdges2
    ##  Returns the second list of edges when bridging holes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectICurveList
    @property
    def BridgeEdges2(self) -> NXOpen.SelectICurveList:
        """
        Getter for property: (@link NXOpen.SelectICurveList NXOpen.SelectICurveList@endlink) BridgeEdges2
         Returns the second list of edges when bridging holes.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectICurveList NXOpen.SelectICurveList@endlink) InnerHole
    ##  Returns the Inner Hole in island filling.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectICurveList
    @property
    def InnerHole(self) -> NXOpen.SelectICurveList:
        """
        Getter for property: (@link NXOpen.SelectICurveList NXOpen.SelectICurveList@endlink) InnerHole
         Returns the Inner Hole in island filling.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsEditCopy
    ##  Returns the flag indicating if the hole filling is on the copy of the input facet body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the flag indicating if the hole filling is on the copy of the input facet body.  
             
         
        """
        pass
    
    ## Setter for property: (bool) IsEditCopy

    ##  Returns the flag indicating if the hole filling is on the copy of the input facet body.  
    ##      
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the flag indicating if the hole filling is on the copy of the input facet body.  
             
         
        """
        pass
    
    ## Getter for property: (int) MaxEdges
    ##  Returns the maximum number of edges that a targeted hole can have.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def MaxEdges(self) -> int:
        """
        Getter for property: (int) MaxEdges
         Returns the maximum number of edges that a targeted hole can have.  
             
         
        """
        pass
    
    ## Setter for property: (int) MaxEdges

    ##  Returns the maximum number of edges that a targeted hole can have.  
    ##      
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MaxEdges.setter
    def MaxEdges(self, max_edges: int):
        """
        Setter for property: (int) MaxEdges
         Returns the maximum number of edges that a targeted hole can have.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectICurveList NXOpen.SelectICurveList@endlink) OuterHole
    ##  Returns the Outer Hole in island filling.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectICurveList
    @property
    def OuterHole(self) -> NXOpen.SelectICurveList:
        """
        Getter for property: (@link NXOpen.SelectICurveList NXOpen.SelectICurveList@endlink) OuterHole
         Returns the Outer Hole in island filling.  
             
         
        """
        pass
    
    ## Getter for property: (@link FillHoleBuilder.SmoothTypes NXOpen.Facet.FillHoleBuilder.SmoothTypes@endlink) SmoothType
    ##  Returns the boundary smoothness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return FillHoleBuilder.SmoothTypes
    @property
    def SmoothType(self) -> FillHoleBuilder.SmoothTypes:
        """
        Getter for property: (@link FillHoleBuilder.SmoothTypes NXOpen.Facet.FillHoleBuilder.SmoothTypes@endlink) SmoothType
         Returns the boundary smoothness.  
             
         
        """
        pass
    
    ## Setter for property: (@link FillHoleBuilder.SmoothTypes NXOpen.Facet.FillHoleBuilder.SmoothTypes@endlink) SmoothType

    ##  Returns the boundary smoothness.  
    ##      
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @SmoothType.setter
    def SmoothType(self, smooth_type: FillHoleBuilder.SmoothTypes):
        """
        Setter for property: (@link FillHoleBuilder.SmoothTypes NXOpen.Facet.FillHoleBuilder.SmoothTypes@endlink) SmoothType
         Returns the boundary smoothness.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) TargetBody
    ##  Returns the facet body we will be filling.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def TargetBody(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) TargetBody
         Returns the facet body we will be filling.  
             
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) TargetFacetBody
    ##  Returns the facet body we will be filling.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Facet::FillHoleBuilder::TargetBody NXOpen::Facet::FillHoleBuilder::TargetBody@endlink  instead.  <br> 

    ## @return SelectFacetedBody
    @property
    def TargetFacetBody(self) -> SelectFacetedBody:
        """
        Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) TargetFacetBody
         Returns the facet body we will be filling.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectICurveList NXOpen.SelectICurveList@endlink) TargetHole
    ##  Returns the hole curves using Fill Hole, User Defined.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectICurveList
    @property
    def TargetHole(self) -> NXOpen.SelectICurveList:
        """
        Getter for property: (@link NXOpen.SelectICurveList NXOpen.SelectICurveList@endlink) TargetHole
         Returns the hole curves using Fill Hole, User Defined.  
             
         
        """
        pass
    
    ## Getter for property: (@link FillHoleBuilder.TargetTypes NXOpen.Facet.FillHoleBuilder.TargetTypes@endlink) TargetType
    ##  Returns the hole target type when filling holes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return FillHoleBuilder.TargetTypes
    @property
    def TargetType(self) -> FillHoleBuilder.TargetTypes:
        """
        Getter for property: (@link FillHoleBuilder.TargetTypes NXOpen.Facet.FillHoleBuilder.TargetTypes@endlink) TargetType
         Returns the hole target type when filling holes.  
             
         
        """
        pass
    
    ## Setter for property: (@link FillHoleBuilder.TargetTypes NXOpen.Facet.FillHoleBuilder.TargetTypes@endlink) TargetType

    ##  Returns the hole target type when filling holes.  
    ##      
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @TargetType.setter
    def TargetType(self, target_type: FillHoleBuilder.TargetTypes):
        """
        Setter for property: (@link FillHoleBuilder.TargetTypes NXOpen.Facet.FillHoleBuilder.TargetTypes@endlink) TargetType
         Returns the hole target type when filling holes.  
             
         
        """
        pass
    
    ## Getter for property: (@link FillHoleBuilder.Types NXOpen.Facet.FillHoleBuilder.Types@endlink) Type
    ##  Returns the hole filling type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return FillHoleBuilder.Types
    @property
    def Type(self) -> FillHoleBuilder.Types:
        """
        Getter for property: (@link FillHoleBuilder.Types NXOpen.Facet.FillHoleBuilder.Types@endlink) Type
         Returns the hole filling type.  
             
         
        """
        pass
    
    ## Setter for property: (@link FillHoleBuilder.Types NXOpen.Facet.FillHoleBuilder.Types@endlink) Type

    ##  Returns the hole filling type.  
    ##      
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Type.setter
    def Type(self, type: FillHoleBuilder.Types):
        """
        Setter for property: (@link FillHoleBuilder.Types NXOpen.Facet.FillHoleBuilder.Types@endlink) Type
         Returns the hole filling type.  
             
         
        """
        pass
    
    ##  Cleans up local meshes associated with each fill. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def ClearHoleFills(self) -> None:
        """
         Cleans up local meshes associated with each fill. 
        """
        pass
    
    ##  Removes all holes, deletes associated hole polylines. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def ClearHoles(self) -> None:
        """
         Removes all holes, deletes associated hole polylines. 
        """
        pass
    
    ##  Fills targeted holes. 
    ##  @return newFacetBody (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink):  updated input facet body .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="globalUpdate"> (bool)  If true, update the entire input facet body.  If
    ##                                   false, GetHoleFillsOnly() may be used to get a facet body
    ##                                   that contains only the new facets of the filled holes. </param>
    def FillHoles(self, globalUpdate: bool) -> NXOpen.DisplayableObject:
        """
         Fills targeted holes. 
         @return newFacetBody (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink):  updated input facet body .
        """
        pass
    
    ##  Locates holes in the mesh and creates polylines around them. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def FindHoles(self) -> None:
        """
         Locates holes in the mesh and creates polylines around them. 
        """
        pass
    
    ##  Gets a list of all holes (represented by polylines). 
    ##  @return holeCurveTags (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink):  Hole polylines. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetAllHoles(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets a list of all holes (represented by polylines). 
         @return holeCurveTags (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink):  Hole polylines. .
        """
        pass
    
    ##  Gets a hole given an index into the list of holes. 
    ##  @return holeAtIndex (@link NXOpen.ICurve NXOpen.ICurve@endlink):  Equals NULL if not found .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  Index into the list of all holes </param>
    def GetHoleByIndex(self, index: int) -> NXOpen.ICurve:
        """
         Gets a hole given an index into the list of holes. 
         @return holeAtIndex (@link NXOpen.ICurve NXOpen.ICurve@endlink):  Equals NULL if not found .
        """
        pass
    
    ##  Builds a facet body that contains only the facets of the filled holes.
    ##  @return facetBodyResult (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink):  the fill facet body .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetHoleFillsOnly(self) -> NXOpen.DisplayableObject:
        """
         Builds a facet body that contains only the facets of the filled holes.
         @return facetBodyResult (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink):  the fill facet body .
        """
        pass
    
    ##  Gets the number of holes in the target facet body. 
    ##  @return numberOfHoles (int): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetNumberOfHoles(self) -> int:
        """
         Gets the number of holes in the target facet body. 
         @return numberOfHoles (int): .
        """
        pass
    
    ##  Gets a list of targeted holes (represented by polylines) based on number of edges. 
    ##  @return holeCurveTags (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink):  Hole polylines. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="numMaxEdges"> (int)  Targets polylines that have this many edges or less. </param>
    def GetTargetHolesByEdgeNumber(self, numMaxEdges: int) -> List[NXOpen.DisplayableObject]:
        """
         Gets a list of targeted holes (represented by polylines) based on number of edges. 
         @return holeCurveTags (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink):  Hole polylines. .
        """
        pass
    
    ##  Switches boundary edge mapping based on the filling type (holes, island, bridge)
    ##             When filling holes or islands, each hole is defined by a polyline.  When bridging holes,
    ##             each individual open edge has its own polyline.
    ##         
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def SwitchHoleFillType(self) -> None:
        """
         Switches boundary edge mapping based on the filling type (holes, island, bridge)
                    When filling holes or islands, each hole is defined by a polyline.  When bridging holes,
                    each individual open edge has its own polyline.
                
        """
        pass
    
import NXOpen
##  This function fills one or more holes in the selected facet bodies to make convergent bodies solid   <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateFillMeshBuilder  NXOpen::Facet::FacetModelingCollection::CreateFillMeshBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## EdgeSelectionMethod </term> <description> 
##  
## UserSelected </description> </item> 
## 
## <item><term> 
##  
## EditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## MaxEdges </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SmoothnessOption </term> <description> 
##  
## Linear </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1872.0.0  <br> 

class FillMeshBuilder(NXOpen.Builder): 
    """ This function fills one or more holes in the selected facet bodies to make convergent bodies solid  """


    ##  Different ways to select an edge 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## UserSelected</term><description> 
    ## </description> </item><item><term> 
    ## ByNumberofEdges</term><description> 
    ## </description> </item></list>
    class EdgeOptionMenu(Enum):
        """
        Members Include: <All> <UserSelected> <ByNumberofEdges>
        """
        All: int
        UserSelected: int
        ByNumberofEdges: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FillMeshBuilder.EdgeOptionMenu:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Smoothness options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ## </description> </item><item><term> 
    ## Refined</term><description> 
    ## </description> </item><item><term> 
    ## TangentBased</term><description> 
    ## </description> </item><item><term> 
    ## CurvatureBased</term><description> 
    ## </description> </item></list>
    class SmoothnessOptionMenu(Enum):
        """
        Members Include: <Linear> <Refined> <TangentBased> <CurvatureBased>
        """
        Linear: int
        Refined: int
        TangentBased: int
        CurvatureBased: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FillMeshBuilder.SmoothnessOptionMenu:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Different types of hole filling are available 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FillHole</term><description> 
    ## </description> </item><item><term> 
    ## CloseNotch</term><description> 
    ## </description> </item><item><term> 
    ## FillIsland</term><description> 
    ## </description> </item><item><term> 
    ## ConnectHoles</term><description> 
    ## </description> </item><item><term> 
    ## BridgeGap</term><description> 
    ## </description> </item></list>
    class Types(Enum):
        """
        Members Include: <FillHole> <CloseNotch> <FillIsland> <ConnectHoles> <BridgeGap>
        """
        FillHole: int
        CloseNotch: int
        FillIsland: int
        ConnectHoles: int
        BridgeGap: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FillMeshBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Contains facet vertex information. 
    ## @link FillMeshBuilderFacetVertexData_Struct NXOpen.Facet.FillMeshBuilderFacetVertexData_Struct@endlink is an alias for @link FillMeshBuilder.FacetVertexData NXOpen.Facet.FillMeshBuilder.FacetVertexData@endlink.
    class FacetVertexData:
        """
         Contains facet vertex information. 
        @link FillMeshBuilderFacetVertexData_Struct NXOpen.Facet.FillMeshBuilderFacetVertexData_Struct@endlink is an alias for @link FillMeshBuilder.FacetVertexData NXOpen.Facet.FillMeshBuilder.FacetVertexData@endlink.
        """
        ## Getter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) Face
        ## The face that facet belongs to.
        ## @return @link NXOpen.NXObject NXOpen.NXObject@endlink
        @property
        def Face(self) -> NXOpen.NXObject:
            """
            Getter for property Face
            The face that facet belongs to.

            """
            pass
        
        ## Setter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) Face
        @Face.setter
        def Face(self, value: NXOpen.NXObject):
            """
            Getter for property Face
            The face that facet belongs to.
            Setter for property Face
            The face that facet belongs to.

            """
            pass
        
        ## Getter for property :(int) NxFacetIndex
        ## The facet index for NX facet body.
        ## @return int
        @property
        def NxFacetIndex(self) -> int:
            """
            Getter for property NxFacetIndex
            The facet index for NX facet body.

            """
            pass
        
        ## Setter for property :(int) NxFacetIndex
        @NxFacetIndex.setter
        def NxFacetIndex(self, value: int):
            """
            Getter for property NxFacetIndex
            The facet index for NX facet body.
            Setter for property NxFacetIndex
            The facet index for NX facet body.

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) PointCoord
        ## The 3d point location on the facet body.
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def PointCoord(self) -> NXOpen.Point3d:
            """
            Getter for property PointCoord
            The 3d point location on the facet body.

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) PointCoord
        @PointCoord.setter
        def PointCoord(self, value: NXOpen.Point3d):
            """
            Getter for property PointCoord
            The 3d point location on the facet body.
            Setter for property PointCoord
            The 3d point location on the facet body.

            """
            pass
        
    
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) EdgeHole
    ##  Returns the edge hole   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def EdgeHole(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) EdgeHole
         Returns the edge hole   
            
         
        """
        pass
    
    ## Getter for property: (@link FillMeshBuilder.EdgeOptionMenu NXOpen.Facet.FillMeshBuilder.EdgeOptionMenu@endlink) EdgeSelectionMethod
    ##  Returns the edge selection method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return FillMeshBuilder.EdgeOptionMenu
    @property
    def EdgeSelectionMethod(self) -> FillMeshBuilder.EdgeOptionMenu:
        """
        Getter for property: (@link FillMeshBuilder.EdgeOptionMenu NXOpen.Facet.FillMeshBuilder.EdgeOptionMenu@endlink) EdgeSelectionMethod
         Returns the edge selection method   
            
         
        """
        pass
    
    ## Setter for property: (@link FillMeshBuilder.EdgeOptionMenu NXOpen.Facet.FillMeshBuilder.EdgeOptionMenu@endlink) EdgeSelectionMethod

    ##  Returns the edge selection method   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @EdgeSelectionMethod.setter
    def EdgeSelectionMethod(self, edgeSelectionMethod: FillMeshBuilder.EdgeOptionMenu):
        """
        Setter for property: (@link FillMeshBuilder.EdgeOptionMenu NXOpen.Facet.FillMeshBuilder.EdgeOptionMenu@endlink) EdgeSelectionMethod
         Returns the edge selection method   
            
         
        """
        pass
    
    ## Getter for property: (bool) EditCopy
    ##  Returns the edit copy   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def EditCopy(self) -> bool:
        """
        Getter for property: (bool) EditCopy
         Returns the edit copy   
            
         
        """
        pass
    
    ## Setter for property: (bool) EditCopy

    ##  Returns the edit copy   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @EditCopy.setter
    def EditCopy(self, editCopy: bool):
        """
        Setter for property: (bool) EditCopy
         Returns the edit copy   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) EndEdgeVertex1
    ##  Returns the end edge vertex1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def EndEdgeVertex1(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) EndEdgeVertex1
         Returns the end edge vertex1   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) EndEdgeVertex1

    ##  Returns the end edge vertex1   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @EndEdgeVertex1.setter
    def EndEdgeVertex1(self, endEdgeVertex1: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) EndEdgeVertex1
         Returns the end edge vertex1   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) EndEdgeVertex2
    ##  Returns the end edge vertex2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def EndEdgeVertex2(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) EndEdgeVertex2
         Returns the end edge vertex2   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) EndEdgeVertex2

    ##  Returns the end edge vertex2   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @EndEdgeVertex2.setter
    def EndEdgeVertex2(self, endEdgeVertex2: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) EndEdgeVertex2
         Returns the end edge vertex2   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) EndHole
    ##  Returns the end hole   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def EndHole(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) EndHole
         Returns the end hole   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) FacetBodies
    ##  Returns the facet body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def FacetBodies(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) FacetBodies
         Returns the facet body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) InnerHole
    ##  Returns the inner hole   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def InnerHole(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) InnerHole
         Returns the inner hole   
            
         
        """
        pass
    
    ## Getter for property: (int) MaxEdges
    ##  Returns the max edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return int
    @property
    def MaxEdges(self) -> int:
        """
        Getter for property: (int) MaxEdges
         Returns the max edges   
            
         
        """
        pass
    
    ## Setter for property: (int) MaxEdges

    ##  Returns the max edges   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @MaxEdges.setter
    def MaxEdges(self, maxEdges: int):
        """
        Setter for property: (int) MaxEdges
         Returns the max edges   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) OuterHole
    ##  Returns the outer hole   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def OuterHole(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) OuterHole
         Returns the outer hole   
            
         
        """
        pass
    
    ## Getter for property: (@link FillMeshBuilder.SmoothnessOptionMenu NXOpen.Facet.FillMeshBuilder.SmoothnessOptionMenu@endlink) SmoothnessOption
    ##  Returns the smoothness option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return FillMeshBuilder.SmoothnessOptionMenu
    @property
    def SmoothnessOption(self) -> FillMeshBuilder.SmoothnessOptionMenu:
        """
        Getter for property: (@link FillMeshBuilder.SmoothnessOptionMenu NXOpen.Facet.FillMeshBuilder.SmoothnessOptionMenu@endlink) SmoothnessOption
         Returns the smoothness option   
            
         
        """
        pass
    
    ## Setter for property: (@link FillMeshBuilder.SmoothnessOptionMenu NXOpen.Facet.FillMeshBuilder.SmoothnessOptionMenu@endlink) SmoothnessOption

    ##  Returns the smoothness option   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @SmoothnessOption.setter
    def SmoothnessOption(self, smoothnessOption: FillMeshBuilder.SmoothnessOptionMenu):
        """
        Setter for property: (@link FillMeshBuilder.SmoothnessOptionMenu NXOpen.Facet.FillMeshBuilder.SmoothnessOptionMenu@endlink) SmoothnessOption
         Returns the smoothness option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartEdgeVertex1
    ##  Returns the start edge vertex1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def StartEdgeVertex1(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartEdgeVertex1
         Returns the start edge vertex1   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartEdgeVertex1

    ##  Returns the start edge vertex1   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @StartEdgeVertex1.setter
    def StartEdgeVertex1(self, startEdgeVertex1: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartEdgeVertex1
         Returns the start edge vertex1   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartEdgeVertex2
    ##  Returns the start edge vertex2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def StartEdgeVertex2(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartEdgeVertex2
         Returns the start edge vertex2   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartEdgeVertex2

    ##  Returns the start edge vertex2   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @StartEdgeVertex2.setter
    def StartEdgeVertex2(self, startEdgeVertex2: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartEdgeVertex2
         Returns the start edge vertex2   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) StartHole
    ##  Returns the start hole   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def StartHole(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) StartHole
         Returns the start hole   
            
         
        """
        pass
    
    ## Getter for property: (@link FillMeshBuilder.Types NXOpen.Facet.FillMeshBuilder.Types@endlink) Type
    ##  Returns the type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return FillMeshBuilder.Types
    @property
    def Type(self) -> FillMeshBuilder.Types:
        """
        Getter for property: (@link FillMeshBuilder.Types NXOpen.Facet.FillMeshBuilder.Types@endlink) Type
         Returns the type   
            
         
        """
        pass
    
    ## Setter for property: (@link FillMeshBuilder.Types NXOpen.Facet.FillMeshBuilder.Types@endlink) Type

    ##  Returns the type   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @Type.setter
    def Type(self, type: FillMeshBuilder.Types):
        """
        Setter for property: (@link FillMeshBuilder.Types NXOpen.Facet.FillMeshBuilder.Types@endlink) Type
         Returns the type   
            
         
        """
        pass
    
    ## Getter for property: (@link FillMeshBuilder.Types NXOpen.Facet.FillMeshBuilder.Types@endlink) TypeOfHole
    ##  Returns the type of Hole   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return FillMeshBuilder.Types
    @property
    def TypeOfHole(self) -> FillMeshBuilder.Types:
        """
        Getter for property: (@link FillMeshBuilder.Types NXOpen.Facet.FillMeshBuilder.Types@endlink) TypeOfHole
         Returns the type of Hole   
            
         
        """
        pass
    
    ## Setter for property: (@link FillMeshBuilder.Types NXOpen.Facet.FillMeshBuilder.Types@endlink) TypeOfHole

    ##  Returns the type of Hole   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @TypeOfHole.setter
    def TypeOfHole(self, type: FillMeshBuilder.Types):
        """
        Setter for property: (@link FillMeshBuilder.Types NXOpen.Facet.FillMeshBuilder.Types@endlink) TypeOfHole
         Returns the type of Hole   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1
    ##  Returns the vertex1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Vertex1(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1
         Returns the vertex1   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1

    ##  Returns the vertex1   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @Vertex1.setter
    def Vertex1(self, vertex1: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1
         Returns the vertex1   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2
    ##  Returns the vertex2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Vertex2(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2
         Returns the vertex2   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2

    ##  Returns the vertex2   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @Vertex2.setter
    def Vertex2(self, vertex2: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2
         Returns the vertex2   
            
         
        """
        pass
    
    ##  Flips the end edge range 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def FlipRangeEnd(self) -> None:
        """
         Flips the end edge range 
        """
        pass
    
    ##  Flips the start edge range 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def FlipRangeStart(self) -> None:
        """
         Flips the start edge range 
        """
        pass
    
    ##  Sets first end edge vertex to bridge the gap. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ## <param name="facetVertexData"> (@link FillMeshBuilder.FacetVertexData NXOpen.Facet.FillMeshBuilder.FacetVertexData@endlink) picked facet vertex info </param>
    def SetBridgeGapEndEdgeVertex1(self, facetVertexData: FillMeshBuilder.FacetVertexData) -> None:
        """
         Sets first end edge vertex to bridge the gap. 
        """
        pass
    
    ##  Sets second end edge vertex to bridge the gap. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ## <param name="facetVertexData"> (@link FillMeshBuilder.FacetVertexData NXOpen.Facet.FillMeshBuilder.FacetVertexData@endlink) picked facet vertex info </param>
    def SetBridgeGapEndEdgeVertex2(self, facetVertexData: FillMeshBuilder.FacetVertexData) -> None:
        """
         Sets second end edge vertex to bridge the gap. 
        """
        pass
    
    ##  Sets first start edge vertex to bridge the gap. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ## <param name="facetVertexData"> (@link FillMeshBuilder.FacetVertexData NXOpen.Facet.FillMeshBuilder.FacetVertexData@endlink) picked facet vertex info </param>
    def SetBridgeGapStartEdgeVertex1(self, facetVertexData: FillMeshBuilder.FacetVertexData) -> None:
        """
         Sets first start edge vertex to bridge the gap. 
        """
        pass
    
    ##  Sets second start edge vertex to bridge the gap. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ## <param name="facetVertexData"> (@link FillMeshBuilder.FacetVertexData NXOpen.Facet.FillMeshBuilder.FacetVertexData@endlink) picked facet vertex info </param>
    def SetBridgeGapStartEdgeVertex2(self, facetVertexData: FillMeshBuilder.FacetVertexData) -> None:
        """
         Sets second start edge vertex to bridge the gap. 
        """
        pass
    
    ##  Sets first vertex to close the notch. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ## <param name="facetVertexData"> (@link FillMeshBuilder.FacetVertexData NXOpen.Facet.FillMeshBuilder.FacetVertexData@endlink) picked facet vertex info </param>
    def SetCloseNotchVertex1(self, facetVertexData: FillMeshBuilder.FacetVertexData) -> None:
        """
         Sets first vertex to close the notch. 
        """
        pass
    
    ##  Sets second vertex to close the notch. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ## <param name="facetVertexData"> (@link FillMeshBuilder.FacetVertexData NXOpen.Facet.FillMeshBuilder.FacetVertexData@endlink) picked facet vertex info </param>
    def SetCloseNotchVertex2(self, facetVertexData: FillMeshBuilder.FacetVertexData) -> None:
        """
         Sets second vertex to close the notch. 
        """
        pass
    
    ##  Update all the holes of the selected facet bodies. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: studio_free_form ("STUDIO FREE FORM")
    def UpdateHoles(self) -> None:
        """
         Update all the holes of the selected facet bodies. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Facet::LocalOffsetBuilder NXOpen::Facet::LocalOffsetBuilder@endlink .
##         This class adds or removes material on facet bodies by creating local offsets. <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateLocalOffsetBuilder  NXOpen::Facet::FacetModelingCollection::CreateLocalOffsetBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## IsEditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsSmoothEdge </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## OffsetDistance.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RegionDistance.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ShapeMethod </term> <description> 
##  
## Smooth </description> </item> 
## 
## <item><term> 
##  
## TransitionMethod </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX12.0.0  <br> 

class LocalOffsetBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Facet.LocalOffsetBuilder</ja_class>.
        This class adds or removes material on facet bodies by creating local offsets."""


    ##  Continuity Method 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Sharp</term><description> 
    ##  Sharp specifies a transition region without smoothing.</description> </item><item><term> 
    ## Smooth</term><description> 
    ##  Smooth specifies a transition region with smoothing.</description> </item></list>
    class ShapeMethodType(Enum):
        """
        Members Include: <Sharp> <Smooth>
        """
        Sharp: int
        Smooth: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> LocalOffsetBuilder.ShapeMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Transition Region Definition 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None creates an offset without a transition region.</description> </item><item><term> 
    ## ByConstantOffset</term><description> 
    ##  Constant offset creates a transition region of constant distance.</description> </item><item><term> 
    ## ByRegionSelection</term><description> 
    ##  Region selection allows the user to select transtion regions.</description> </item></list>
    class TransitionMethodType(Enum):
        """
        Members Include: <NotSet> <ByConstantOffset> <ByRegionSelection>
        """
        NotSet: int
        ByConstantOffset: int
        ByRegionSelection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> LocalOffsetBuilder.TransitionMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetRegion
    ##  Returns the facets to be offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetRegion(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetRegion
         Returns the facets to be offset   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetTransitionRegions
    ##  Returns the user-selected transition regions   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetTransitionRegions(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetTransitionRegions
         Returns the user-selected transition regions   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsEditCopy
    ##  Returns the option to create a non-associative copy of the selected body and edit that copy   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the option to create a non-associative copy of the selected body and edit that copy   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsEditCopy

    ##  Returns the option to create a non-associative copy of the selected body and edit that copy   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the option to create a non-associative copy of the selected body and edit that copy   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsRegenerateOffsetMesh
    ##  Returns the option to rebuild the mesh structure of the offset output   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsRegenerateOffsetMesh(self) -> bool:
        """
        Getter for property: (bool) IsRegenerateOffsetMesh
         Returns the option to rebuild the mesh structure of the offset output   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsRegenerateOffsetMesh

    ##  Returns the option to rebuild the mesh structure of the offset output   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsRegenerateOffsetMesh.setter
    def IsRegenerateOffsetMesh(self, isRegenerateOffsetMesh: bool):
        """
        Setter for property: (bool) IsRegenerateOffsetMesh
         Returns the option to rebuild the mesh structure of the offset output   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsReverseDirection
    ##  Returns the method to reverse the direction of the offset.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsReverseDirection(self) -> bool:
        """
        Getter for property: (bool) IsReverseDirection
         Returns the method to reverse the direction of the offset.  
             
         
        """
        pass
    
    ## Setter for property: (bool) IsReverseDirection

    ##  Returns the method to reverse the direction of the offset.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsReverseDirection.setter
    def IsReverseDirection(self, isReverseDirection: bool):
        """
        Setter for property: (bool) IsReverseDirection
         Returns the method to reverse the direction of the offset.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsSmoothEdge
    ##  Returns the option to add smoothing to the edge of the offset region   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsSmoothEdge(self) -> bool:
        """
        Getter for property: (bool) IsSmoothEdge
         Returns the option to add smoothing to the edge of the offset region   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsSmoothEdge

    ##  Returns the option to add smoothing to the edge of the offset region   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsSmoothEdge.setter
    def IsSmoothEdge(self, isSmoothEdge: bool):
        """
        Setter for property: (bool) IsSmoothEdge
         Returns the option to add smoothing to the edge of the offset region   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
    ##  Returns the linear distance of the created local offset, which may be a positive or negative distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
         Returns the linear distance of the created local offset, which may be a positive or negative distance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RegionDistance
    ##  Returns the distance of the transition region with the constant offset option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RegionDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RegionDistance
         Returns the distance of the transition region with the constant offset option   
            
         
        """
        pass
    
    ## Getter for property: (@link LocalOffsetBuilder.ShapeMethodType NXOpen.Facet.LocalOffsetBuilder.ShapeMethodType@endlink) ShapeMethod
    ##  Returns the method to define the shape of the transition region   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return LocalOffsetBuilder.ShapeMethodType
    @property
    def ShapeMethod(self) -> LocalOffsetBuilder.ShapeMethodType:
        """
        Getter for property: (@link LocalOffsetBuilder.ShapeMethodType NXOpen.Facet.LocalOffsetBuilder.ShapeMethodType@endlink) ShapeMethod
         Returns the method to define the shape of the transition region   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalOffsetBuilder.ShapeMethodType NXOpen.Facet.LocalOffsetBuilder.ShapeMethodType@endlink) ShapeMethod

    ##  Returns the method to define the shape of the transition region   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShapeMethod.setter
    def ShapeMethod(self, shapeMethod: LocalOffsetBuilder.ShapeMethodType):
        """
        Setter for property: (@link LocalOffsetBuilder.ShapeMethodType NXOpen.Facet.LocalOffsetBuilder.ShapeMethodType@endlink) ShapeMethod
         Returns the method to define the shape of the transition region   
            
         
        """
        pass
    
    ## Getter for property: (@link LocalOffsetBuilder.TransitionMethodType NXOpen.Facet.LocalOffsetBuilder.TransitionMethodType@endlink) TransitionMethod
    ##  Returns the type of transition region   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return LocalOffsetBuilder.TransitionMethodType
    @property
    def TransitionMethod(self) -> LocalOffsetBuilder.TransitionMethodType:
        """
        Getter for property: (@link LocalOffsetBuilder.TransitionMethodType NXOpen.Facet.LocalOffsetBuilder.TransitionMethodType@endlink) TransitionMethod
         Returns the type of transition region   
            
         
        """
        pass
    
    ## Setter for property: (@link LocalOffsetBuilder.TransitionMethodType NXOpen.Facet.LocalOffsetBuilder.TransitionMethodType@endlink) TransitionMethod

    ##  Returns the type of transition region   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @TransitionMethod.setter
    def TransitionMethod(self, transitionMethod: LocalOffsetBuilder.TransitionMethodType):
        """
        Setter for property: (@link LocalOffsetBuilder.TransitionMethodType NXOpen.Facet.LocalOffsetBuilder.TransitionMethodType@endlink) TransitionMethod
         Returns the type of transition region   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::MergeFacetBodyBuilder NXOpen::Facet::MergeFacetBodyBuilder@endlink 
##     It merges two overlapping NX facet bodies. It returns a new mergered NX facet body. The two input bodies
##     can be kept, deleted or hidden.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateMergeFacetBodyBuilder  NXOpen::Facet::FacetedBodyCollection::CreateMergeFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ChordHeight.Value (deprecated) </term> <description> 
##  
## 0.05 (millimeters part), 0.005 (inches part) </description> </item> 
## 
## <item><term> 
##  
## EdgeLength.Value (deprecated) </term> <description> 
##  
## 1 (millimeters part), 0.1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## InputStatus (deprecated) </term> <description> 
##  
## Keep </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX2206.0.0.  This functionality is no longer supported.  <br> 

class MergeFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.MergeFacetBodyBuilder</ja_class>
    It merges two overlapping NX facet bodies. It returns a new mergered NX facet body. The two input bodies
    can be kept, deleted or hidden.
    """


    ##  Represents the option for keeping, deleting or hiding input two facet bodies after builder committing 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Keep</term><description> 
    ##  Keep the input facet body after builder committing </description> </item><item><term> 
    ## Delete</term><description> 
    ##  Delete the input facet body after builder committing </description> </item><item><term> 
    ## Hide</term><description> 
    ##  Hide the input facet body after builder committing </description> </item></list>
    class Input(Enum):
        """
        Members Include: <Keep> <Delete> <Hide>
        """
        Keep: int
        Delete: int
        Hide: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MergeFacetBodyBuilder.Input:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) AngleTolerance
    ##  Returns the angle tolerance used in the merge facet body feature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  This functionality is no longer supported.  <br> 

    ## @return float
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance used in the merge facet body feature   
            
         
        """
        pass
    
    ## Setter for property: (float) AngleTolerance

    ##  Returns the angle tolerance used in the merge facet body feature   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  This functionality is no longer supported.  <br> 

    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance used in the merge facet body feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ChordHeight
    ##  Returns the chord height to control the size of new facets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  This functionality is no longer supported.  <br> 

    ## @return NXOpen.Expression
    @property
    def ChordHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ChordHeight
         Returns the chord height to control the size of new facets   
            
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##  Returns the distance tolerance used in the merge facet body feature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  This functionality is no longer supported.  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the merge facet body feature   
            
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##  Returns the distance tolerance used in the merge facet body feature   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  This functionality is no longer supported.  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the merge facet body feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EdgeLength
    ##  Returns the edge length to control the size of new facets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  This functionality is no longer supported.  <br> 

    ## @return NXOpen.Expression
    @property
    def EdgeLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EdgeLength
         Returns the edge length to control the size of new facets   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) FacetBodyOne
    ##  Returns the first NX facet body to be merged   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  This functionality is no longer supported.  <br> 

    ## @return SelectFacetedBody
    @property
    def FacetBodyOne(self) -> SelectFacetedBody:
        """
        Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) FacetBodyOne
         Returns the first NX facet body to be merged   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) FacetBodyTwo
    ##  Returns the second NX facet body to be merged   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  This functionality is no longer supported.  <br> 

    ## @return SelectFacetedBody
    @property
    def FacetBodyTwo(self) -> SelectFacetedBody:
        """
        Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) FacetBodyTwo
         Returns the second NX facet body to be merged   
            
         
        """
        pass
    
    ## Getter for property: (@link MergeFacetBodyBuilder.Input NXOpen.Facet.MergeFacetBodyBuilder.Input@endlink) InputStatus
    ##  Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  This functionality is no longer supported.  <br> 

    ## @return MergeFacetBodyBuilder.Input
    @property
    def InputStatus(self) -> MergeFacetBodyBuilder.Input:
        """
        Getter for property: (@link MergeFacetBodyBuilder.Input NXOpen.Facet.MergeFacetBodyBuilder.Input@endlink) InputStatus
         Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
            
         
        """
        pass
    
    ## Setter for property: (@link MergeFacetBodyBuilder.Input NXOpen.Facet.MergeFacetBodyBuilder.Input@endlink) InputStatus

    ##  Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  This functionality is no longer supported.  <br> 

    @InputStatus.setter
    def InputStatus(self, inputStatus: MergeFacetBodyBuilder.Input):
        """
        Setter for property: (@link MergeFacetBodyBuilder.Input NXOpen.Facet.MergeFacetBodyBuilder.Input@endlink) InputStatus
         Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link Facet::MergeFacetFacesBuilder Facet::MergeFacetFacesBuilder@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateMergeFacetFacesBuilder  NXOpen::Facet::FacetModelingCollection::CreateMergeFacetFacesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## IsEditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX12.0.0  <br> 

class MergeFacetFacesBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>Facet.MergeFacetFacesBuilder</ja_class> builder
    """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector
    ##  Returns the face collector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector
         Returns the face collector   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsEditCopy
    ##  Returns the value indicating if a copy of the facet body to be used for Merge facet faces without altering the original   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be used for Merge facet faces without altering the original   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsEditCopy

    ##  Returns the value indicating if a copy of the facet body to be used for Merge facet faces without altering the original   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be used for Merge facet faces without altering the original   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::MeshFromCloudBuilder NXOpen::Facet::MeshFromCloudBuilder@endlink 
##     Creates a convergent body from point clouds. The point cloud data source
##     can be either a file or existing points within the part file.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateMeshFromCloudBuilder  NXOpen::Facet::FacetModelingCollection::CreateMeshFromCloudBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AnalyzeMeshQuality </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ModeOptions </term> <description> 
##  
## KeepAllPoints </description> </item> 
## 
## <item><term> 
##  
## NeighborhoodSize </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## SmoothingFactor </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SourceOptions </term> <description> 
##  
## FromFile </description> </item> 
## 
## <item><term> 
##  
## TargetVertexNumber </term> <description> 
##  
## 100000 </description> </item> 
## 
## <item><term> 
##  
## TessellationPercentage </term> <description> 
##  
## 100 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class MeshFromCloudBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.MeshFromCloudBuilder</ja_class>
    Creates a convergent body from point clouds. The point cloud data source
    can be either a file or existing points within the part file.
    """


    ##  The options controlling distribution of vertices in the output convergent body.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## UniformDensity</term><description> 
    ##  Uniform vertex density. </description> </item><item><term> 
    ## VariableDensity</term><description> 
    ##  uniform vertex density in planar areas with increased density in curvy areas. </description> </item><item><term> 
    ## KeepAllPoints</term><description> 
    ##  Preserve input points to create corresponding vertices. </description> </item></list>
    class ModeOption(Enum):
        """
        Members Include: <UniformDensity> <VariableDensity> <KeepAllPoints>
        """
        UniformDensity: int
        VariableDensity: int
        KeepAllPoints: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MeshFromCloudBuilder.ModeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The options indicating the source of point cloud. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FromFile</term><description> 
    ## </description> </item><item><term> 
    ## ExistingPoints</term><description> 
    ## </description> </item></list>
    class SourceOption(Enum):
        """
        Members Include: <FromFile> <ExistingPoints>
        """
        FromFile: int
        ExistingPoints: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MeshFromCloudBuilder.SourceOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AnalyzeMeshQuality
    ##  Returns the value used to determine if analyzing the quality of the mesh or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def AnalyzeMeshQuality(self) -> bool:
        """
        Getter for property: (bool) AnalyzeMeshQuality
         Returns the value used to determine if analyzing the quality of the mesh or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AnalyzeMeshQuality

    ##  Returns the value used to determine if analyzing the quality of the mesh or not.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AnalyzeMeshQuality.setter
    def AnalyzeMeshQuality(self, analyzeMeshQuality: bool):
        """
        Setter for property: (bool) AnalyzeMeshQuality
         Returns the value used to determine if analyzing the quality of the mesh or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link MeshFromCloudBuilder.ModeOption NXOpen.Facet.MeshFromCloudBuilder.ModeOption@endlink) ModeOptions
    ##  Returns the option controlling distribution of vertices in the output convergent body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return MeshFromCloudBuilder.ModeOption
    @property
    def ModeOptions(self) -> MeshFromCloudBuilder.ModeOption:
        """
        Getter for property: (@link MeshFromCloudBuilder.ModeOption NXOpen.Facet.MeshFromCloudBuilder.ModeOption@endlink) ModeOptions
         Returns the option controlling distribution of vertices in the output convergent body.  
             
         
        """
        pass
    
    ## Setter for property: (@link MeshFromCloudBuilder.ModeOption NXOpen.Facet.MeshFromCloudBuilder.ModeOption@endlink) ModeOptions

    ##  Returns the option controlling distribution of vertices in the output convergent body.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ModeOptions.setter
    def ModeOptions(self, modeOptions: MeshFromCloudBuilder.ModeOption):
        """
        Setter for property: (@link MeshFromCloudBuilder.ModeOption NXOpen.Facet.MeshFromCloudBuilder.ModeOption@endlink) ModeOptions
         Returns the option controlling distribution of vertices in the output convergent body.  
             
         
        """
        pass
    
    ## Getter for property: (float) NeighborhoodSize
    ##  Returns the value used to determine neighboring points when creating a body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def NeighborhoodSize(self) -> float:
        """
        Getter for property: (float) NeighborhoodSize
         Returns the value used to determine neighboring points when creating a body.  
             
         
        """
        pass
    
    ## Setter for property: (float) NeighborhoodSize

    ##  Returns the value used to determine neighboring points when creating a body.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @NeighborhoodSize.setter
    def NeighborhoodSize(self, neighborhoodSize: float):
        """
        Setter for property: (float) NeighborhoodSize
         Returns the value used to determine neighboring points when creating a body.  
             
         
        """
        pass
    
    ## Getter for property: (str) PointFile
    ##  Returns the point cloud file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def PointFile(self) -> str:
        """
        Getter for property: (str) PointFile
         Returns the point cloud file.  
             
         
        """
        pass
    
    ## Setter for property: (str) PointFile

    ##  Returns the point cloud file.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PointFile.setter
    def PointFile(self, filename: str):
        """
        Setter for property: (str) PointFile
         Returns the point cloud file.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) SelectPoints
    ##  Returns the point cloud.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.SelectPointList
    @property
    def SelectPoints(self) -> NXOpen.SelectPointList:
        """
        Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) SelectPoints
         Returns the point cloud.  
             
         
        """
        pass
    
    ## Getter for property: (int) SmoothingFactor
    ##  Returns the value indicating smoothing factor.  
    ##    The value can be between 0 and 100, with high value indicating higher smoothing.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def SmoothingFactor(self) -> int:
        """
        Getter for property: (int) SmoothingFactor
         Returns the value indicating smoothing factor.  
           The value can be between 0 and 100, with high value indicating higher smoothing.   
         
        """
        pass
    
    ## Setter for property: (int) SmoothingFactor

    ##  Returns the value indicating smoothing factor.  
    ##    The value can be between 0 and 100, with high value indicating higher smoothing.   
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @SmoothingFactor.setter
    def SmoothingFactor(self, smoothingFactor: int):
        """
        Setter for property: (int) SmoothingFactor
         Returns the value indicating smoothing factor.  
           The value can be between 0 and 100, with high value indicating higher smoothing.   
         
        """
        pass
    
    ## Getter for property: (@link MeshFromCloudBuilder.SourceOption NXOpen.Facet.MeshFromCloudBuilder.SourceOption@endlink) SourceOptions
    ##  Returns the option indicating the source of point cloud.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return MeshFromCloudBuilder.SourceOption
    @property
    def SourceOptions(self) -> MeshFromCloudBuilder.SourceOption:
        """
        Getter for property: (@link MeshFromCloudBuilder.SourceOption NXOpen.Facet.MeshFromCloudBuilder.SourceOption@endlink) SourceOptions
         Returns the option indicating the source of point cloud.  
             
         
        """
        pass
    
    ## Setter for property: (@link MeshFromCloudBuilder.SourceOption NXOpen.Facet.MeshFromCloudBuilder.SourceOption@endlink) SourceOptions

    ##  Returns the option indicating the source of point cloud.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @SourceOptions.setter
    def SourceOptions(self, sourceOptions: MeshFromCloudBuilder.SourceOption):
        """
        Setter for property: (@link MeshFromCloudBuilder.SourceOption NXOpen.Facet.MeshFromCloudBuilder.SourceOption@endlink) SourceOptions
         Returns the option indicating the source of point cloud.  
             
         
        """
        pass
    
    ## Getter for property: (int) TargetVertexNumber
    ##  Returns the value indicating the desired number of vertices in the output body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def TargetVertexNumber(self) -> int:
        """
        Getter for property: (int) TargetVertexNumber
         Returns the value indicating the desired number of vertices in the output body.  
             
         
        """
        pass
    
    ## Setter for property: (int) TargetVertexNumber

    ##  Returns the value indicating the desired number of vertices in the output body.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @TargetVertexNumber.setter
    def TargetVertexNumber(self, targetVertexNumber: int):
        """
        Setter for property: (int) TargetVertexNumber
         Returns the value indicating the desired number of vertices in the output body.  
             
         
        """
        pass
    
    ## Getter for property: (float) TessellationPercentage
    ##  Returns the value as a percentage ratio of number of output vertices to the number of input points.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def TessellationPercentage(self) -> float:
        """
        Getter for property: (float) TessellationPercentage
         Returns the value as a percentage ratio of number of output vertices to the number of input points.  
             
         
        """
        pass
    
    ## Setter for property: (float) TessellationPercentage

    ##  Returns the value as a percentage ratio of number of output vertices to the number of input points.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @TessellationPercentage.setter
    def TessellationPercentage(self, tessellationPercentage: float):
        """
        Setter for property: (float) TessellationPercentage
         Returns the value as a percentage ratio of number of output vertices to the number of input points.  
             
         
        """
        pass
    
    ##  Determines @link NXOpen::Facet::MeshFromCloudBuilder::NeighborhoodSize NXOpen::Facet::MeshFromCloudBuilder::NeighborhoodSize@endlink  for a given point cloud data. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def SuggestNeighborhoodSize(self) -> None:
        """
         Determines @link NXOpen::Facet::MeshFromCloudBuilder::NeighborhoodSize NXOpen::Facet::MeshFromCloudBuilder::NeighborhoodSize@endlink  for a given point cloud data. 
        """
        pass
    
import NXOpen
##  Aligns multiple facet bodies to one another without using reference points.  <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateMultiPatchAlignmentBuilder  NXOpen::Facet::FacetedBodyCollection::CreateMultiPatchAlignmentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Iteration </term> <description> 
##  
## 10 </description> </item> 
## 
## <item><term> 
##  
## MaximumCheckingDistance </term> <description> 
##  
## 10.0 (millimeters part), 0.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Resolution </term> <description> 
##  
## High </description> </item> 
## 
## <item><term> 
##  
## Tolerance </term> <description> 
##  
## 0.01 (millimeters part), 0.005 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class MultiPatchAlignmentBuilder(NXOpen.Builder): 
    """ Aligns multiple facet bodies to one another without using reference points. """


    ##  Determines the number of facets used in the alignment. 
    ##             If you are importing an .AC file with image information, this option will 
    ##             control how many image pixels are used in the alignment. If the imported 
    ##             facet data does not have image information, the number of points being used 
    ##             for the alignment will be controlled. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## High</term><description> 
    ##  Uses a high number of facets for the alignment. </description> </item><item><term> 
    ## Medium</term><description> 
    ##  Uses a medium number of facets for the alignment. </description> </item><item><term> 
    ## Low</term><description> 
    ##  Uses a low number of facets for the alignment. </description> </item></list>
    class ResolutionType(Enum):
        """
        Members Include: <High> <Medium> <Low>
        """
        High: int
        Medium: int
        Low: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MultiPatchAlignmentBuilder.ResolutionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) AlignFacetPatches
    ##  Returns the facet bodies to be aligned.  
    ##    Inputs to this command can be convergent objects.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def AlignFacetPatches(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) AlignFacetPatches
         Returns the facet bodies to be aligned.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) AlignmentBodies
    ##  Returns the facet bodies to be aligned.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1847.0.0.  Use @link NXOpen::Facet::MultiPatchAlignmentBuilder::AlignFacetPatches NXOpen::Facet::MultiPatchAlignmentBuilder::AlignFacetPatches@endlink  instead.  <br> 

    ## @return SelectFacetedBodyList
    @property
    def AlignmentBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) AlignmentBodies
         Returns the facet bodies to be aligned.  
             
         
        """
        pass
    
    ## Getter for property: (int) Iteration
    ##  Returns the value indicating the number of times the alignment algorithm is applied.  
    ##    
    ##             Many iterations improve alignment accuracy but take longer.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return int
    @property
    def Iteration(self) -> int:
        """
        Getter for property: (int) Iteration
         Returns the value indicating the number of times the alignment algorithm is applied.  
           
                    Many iterations improve alignment accuracy but take longer.   
         
        """
        pass
    
    ## Setter for property: (int) Iteration

    ##  Returns the value indicating the number of times the alignment algorithm is applied.  
    ##    
    ##             Many iterations improve alignment accuracy but take longer.   
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Iteration.setter
    def Iteration(self, iteration: int):
        """
        Setter for property: (int) Iteration
         Returns the value indicating the number of times the alignment algorithm is applied.  
           
                    Many iterations improve alignment accuracy but take longer.   
         
        """
        pass
    
    ## Getter for property: (float) MaximumCheckingDistance
    ##  Returns the distance facets may be from one another in order to be used 
    ##             in the alignment.  
    ##    Larger numbers slow the alignment process.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def MaximumCheckingDistance(self) -> float:
        """
        Getter for property: (float) MaximumCheckingDistance
         Returns the distance facets may be from one another in order to be used 
                    in the alignment.  
           Larger numbers slow the alignment process.   
         
        """
        pass
    
    ## Setter for property: (float) MaximumCheckingDistance

    ##  Returns the distance facets may be from one another in order to be used 
    ##             in the alignment.  
    ##    Larger numbers slow the alignment process.   
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @MaximumCheckingDistance.setter
    def MaximumCheckingDistance(self, maximumCheckingDistance: float):
        """
        Setter for property: (float) MaximumCheckingDistance
         Returns the distance facets may be from one another in order to be used 
                    in the alignment.  
           Larger numbers slow the alignment process.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ReferenceFacetPatches
    ##  Returns an optional reference facet body.  
    ##    Inputs to this command can be convergent objects.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def ReferenceFacetPatches(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ReferenceFacetPatches
         Returns an optional reference facet body.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) ReferencePatches
    ##  Returns an optional reference facet body with a location and orientation that will 
    ##             remain fixed, causing all of the other selected facet bodies to align with 
    ##             it.  
    ##    If you do not select a reference body, all of the selected facet bodies 
    ##             will align to each other, without a fixed location.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1847.0.0.  Use @link NXOpen::Facet::MultiPatchAlignmentBuilder::ReferenceFacetPatches NXOpen::Facet::MultiPatchAlignmentBuilder::ReferenceFacetPatches@endlink  instead.  <br> 

    ## @return SelectFacetedBodyList
    @property
    def ReferencePatches(self) -> SelectFacetedBodyList:
        """
        Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) ReferencePatches
         Returns an optional reference facet body with a location and orientation that will 
                    remain fixed, causing all of the other selected facet bodies to align with 
                    it.  
           If you do not select a reference body, all of the selected facet bodies 
                    will align to each other, without a fixed location.   
         
        """
        pass
    
    ## Getter for property: (@link MultiPatchAlignmentBuilder.ResolutionType NXOpen.Facet.MultiPatchAlignmentBuilder.ResolutionType@endlink) Resolution
    ##  Returns the type indicating number of facets to be used  in the alignment.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return MultiPatchAlignmentBuilder.ResolutionType
    @property
    def Resolution(self) -> MultiPatchAlignmentBuilder.ResolutionType:
        """
        Getter for property: (@link MultiPatchAlignmentBuilder.ResolutionType NXOpen.Facet.MultiPatchAlignmentBuilder.ResolutionType@endlink) Resolution
         Returns the type indicating number of facets to be used  in the alignment.  
             
         
        """
        pass
    
    ## Setter for property: (@link MultiPatchAlignmentBuilder.ResolutionType NXOpen.Facet.MultiPatchAlignmentBuilder.ResolutionType@endlink) Resolution

    ##  Returns the type indicating number of facets to be used  in the alignment.  
    ##      
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Resolution.setter
    def Resolution(self, resolution: MultiPatchAlignmentBuilder.ResolutionType):
        """
        Setter for property: (@link MultiPatchAlignmentBuilder.ResolutionType NXOpen.Facet.MultiPatchAlignmentBuilder.ResolutionType@endlink) Resolution
         Returns the type indicating number of facets to be used  in the alignment.  
             
         
        """
        pass
    
    ## Getter for property: (float) Tolerance
    ##  Returns the precision of the alignment.  
    ##   
    ##             Alignment will complete when tolerance is met or the number of iterations has been reached.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def Tolerance(self) -> float:
        """
        Getter for property: (float) Tolerance
         Returns the precision of the alignment.  
          
                    Alignment will complete when tolerance is met or the number of iterations has been reached.   
         
        """
        pass
    
    ## Setter for property: (float) Tolerance

    ##  Returns the precision of the alignment.  
    ##   
    ##             Alignment will complete when tolerance is met or the number of iterations has been reached.   
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Tolerance.setter
    def Tolerance(self, tolerance: float):
        """
        Setter for property: (float) Tolerance
         Returns the precision of the alignment.  
          
                    Alignment will complete when tolerance is met or the number of iterations has been reached.   
         
        """
        pass
    
import NXOpen
## 
##        This class manages the paint brush utility for a facet body.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreatePaintBrushBuilder  NXOpen::Facet::FacetModelingCollection::CreatePaintBrushBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class PaintBrushBuilder(NXOpen.Builder): 
    """
       This class manages the paint brush utility for a facet body.
    """


    ##  Clears the paint path 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def ClearThePaintPath(self) -> None:
        """
         Clears the paint path 
        """
        pass
    
    ##  Returns the paint brush color 
    ##  @return paintBrushColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetPaintBrushColor(self) -> List[float]:
        """
         Returns the paint brush color 
         @return paintBrushColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Paints facet body vertex color 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  No replacement for this api.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="position"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Vertex position </param>
    def PaintVertexColor(self, position: NXOpen.Point3d) -> None:
        """
         Paints facet body vertex color 
        """
        pass
    
    ##  Sets facet body being painted. Inputs to this command can be convergent objects. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="body"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  Body being painted. </param>
    def SetBodyBeingPainted(self, body: NXOpen.DisplayableObject) -> None:
        """
         Sets facet body being painted. Inputs to this command can be convergent objects. 
        """
        pass
    
    ##  Sets facet body being painted. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Facet::PaintBrushBuilder::SetBodyBeingPainted NXOpen::Facet::PaintBrushBuilder::SetBodyBeingPainted@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="facet"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  Facet body being painted. </param>
    def SetFacetBeingPainted(self, facet: FacetedBody) -> None:
        """
         Sets facet body being painted. 
        """
        pass
    
    ##  Sets the paint brush color 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="paintBrushColor"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetPaintBrushColor(self, paintBrushColor: List[float]) -> None:
        """
         Sets the paint brush color 
        """
        pass
    
    ##  Flag to use temporary facet display 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="tempDisplay"> (bool)  Temporary display flag </param>
    def SetTemporaryFacetDisplay(self, tempDisplay: bool) -> None:
        """
         Flag to use temporary facet display 
        """
        pass
    
    ##  Setup the paint facet body 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def SetupPaintFacetBody(self) -> None:
        """
         Setup the paint facet body 
        """
        pass
    
import NXOpen
## 
##        This class manages the color painting on a facet body.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreatePaintFacetBodyBuilder  NXOpen::Facet::FacetModelingCollection::CreatePaintFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## PaintBrushSize.Value (deprecated) </term> <description> 
##  
## 20.0 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class PaintFacetBodyBuilder(NXOpen.Builder): 
    """
       This class manages the color painting on a facet body.
    """


    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
    ##  Returns a collector of facets on the facet bodies to be to be tested.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns a collector of facets on the facet bodies to be to be tested.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) InheritBodyColorPick
    ##  Returns the inherit color pick.  
    ##    Inputs to this command can be convergent objects.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def InheritBodyColorPick(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) InheritBodyColorPick
         Returns the inherit color pick.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) InheritColorPick
    ##  Returns the inherit color pick   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Facet::PaintFacetBodyBuilder::InheritBodyColorPick NXOpen::Facet::PaintFacetBodyBuilder::InheritBodyColorPick@endlink  instead.  <br> 

    ## @return SelectFacetedBody
    @property
    def InheritColorPick(self) -> SelectFacetedBody:
        """
        Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) InheritColorPick
         Returns the inherit color pick   
            
         
        """
        pass
    
    ## Getter for property: (@link PaintBrushBuilder NXOpen.Facet.PaintBrushBuilder@endlink) PaintBrush
    ##  Returns the paint brush   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::Facet::PaintFacetBodyBuilder::FacetCollector NXOpen::Facet::PaintFacetBodyBuilder::FacetCollector@endlink  instead.  <br> 

    ## @return PaintBrushBuilder
    @property
    def PaintBrush(self) -> PaintBrushBuilder:
        """
        Getter for property: (@link PaintBrushBuilder NXOpen.Facet.PaintBrushBuilder@endlink) PaintBrush
         Returns the paint brush   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PaintBrushSize
    ##  Returns the paint brush size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::Facet::PaintFacetBodyBuilder::FacetCollector NXOpen::Facet::PaintFacetBodyBuilder::FacetCollector@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def PaintBrushSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PaintBrushSize
         Returns the paint brush size   
            
         
        """
        pass
    
    ##  Returns the paint brush color 
    ##  @return paintBrushColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetPaintBrushColor(self) -> List[float]:
        """
         Returns the paint brush color 
         @return paintBrushColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Paints facets background color. Inputs to this command can be convergent objects.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="bodies"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink)  Bodies to be painted with background color </param>
    def PaintBodiesBackgroundColor(self, bodies: List[NXOpen.DisplayableObject]) -> None:
        """
         Paints facets background color. Inputs to this command can be convergent objects.
        """
        pass
    
    ##  Paints facets background color 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Facet::PaintFacetBodyBuilder::PaintBodiesBackgroundColor NXOpen::Facet::PaintFacetBodyBuilder::PaintBodiesBackgroundColor@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="facets"> (@link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink)  Facets to be painted with background color </param>
    def PaintFacetsBackGroundColor(self, facets: List[FacetedBody]) -> None:
        """
         Paints facets background color 
        """
        pass
    
    ##  Paints selected facets. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def PaintSelectedFacets(self) -> None:
        """
         Paints selected facets. 
        """
        pass
    
    ##  Sets the paint brush color 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="paintBrushColor"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetPaintBrushColor(self, paintBrushColor: List[float]) -> None:
        """
         Sets the paint brush color 
        """
        pass
    
    ##  Setup color data. Inputs to this command can be convergent objects. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="bodies"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink)  Bodies that need color data for edit </param>
    def SetupBodyColorData(self, bodies: List[NXOpen.DisplayableObject]) -> None:
        """
         Setup color data. Inputs to this command can be convergent objects. 
        """
        pass
    
    ##  Setup color data 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Facet::PaintFacetBodyBuilder::SetupBodyColorData NXOpen::Facet::PaintFacetBodyBuilder::SetupBodyColorData@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="facets"> (@link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink)  Facets that need color data for edit </param>
    def SetupColorData(self, facets: List[FacetedBody]) -> None:
        """
         Setup color data 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Facet::PlugLeakageBuilder NXOpen::Facet::PlugLeakageBuilder@endlink 
##         that identifies holes in facet bodies and covers the holes with newly created facet bodies. <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreatePlugLeakageBuilder  NXOpen::Facet::FacetModelingCollection::CreatePlugLeakageBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## HoleMinimumSize.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class PlugLeakageBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Facet.PlugLeakageBuilder</ja_class>
        that identifies holes in facet bodies and covers the holes with newly created facet bodies."""


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleMinimumSize
    ##  Returns the minimum size of hole to be detected  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HoleMinimumSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleMinimumSize
         Returns the minimum size of hole to be detected  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) InnerPoint
    ##  Returnsthe inner point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def InnerPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) InnerPoint
         Returnsthe inner point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) InnerPoint

    ##  Returnsthe inner point   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @InnerPoint.setter
    def InnerPoint(self, innerPoint: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) InnerPoint
         Returnsthe inner point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) InputBodyCollector
    ##  Returns the input body collector  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def InputBodyCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) InputBodyCollector
         Returns the input body collector  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) OuterPoint
    ##  Returnsthe outer point  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def OuterPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) OuterPoint
         Returnsthe outer point  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) OuterPoint

    ##  Returnsthe outer point  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OuterPoint.setter
    def OuterPoint(self, outerPoint: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) OuterPoint
         Returnsthe outer point  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList@endlink) RegionList
    ##  Returnsthe boundaries that are defined to patch the holes.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList
    @property
    def RegionList(self) -> NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList@endlink) RegionList
         Returnsthe boundaries that are defined to patch the holes.  
            
         
        """
        pass
    
    ## Creates a patch defined by the boundary.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def CreatePatch(self) -> None:
        """
        Creates a patch defined by the boundary.
        """
        pass
    
    ##  Finds the path that goes through the holes, starting from 
    ##         @link NXOpen::Facet::PlugLeakageBuilder::InnerPoint NXOpen::Facet::PlugLeakageBuilder::InnerPoint@endlink  and ending at 
    ##         @link NXOpen::Facet::PlugLeakageBuilder::OuterPoint NXOpen::Facet::PlugLeakageBuilder::OuterPoint@endlink .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def FindPath(self) -> None:
        """
         Finds the path that goes through the holes, starting from 
                @link NXOpen::Facet::PlugLeakageBuilder::InnerPoint NXOpen::Facet::PlugLeakageBuilder::InnerPoint@endlink  and ending at 
                @link NXOpen::Facet::PlugLeakageBuilder::OuterPoint NXOpen::Facet::PlugLeakageBuilder::OuterPoint@endlink .
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::PolygonModelingBuilder NXOpen::Facet::PolygonModelingBuilder@endlink  builder. 
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreatePolygonModelingBuilder  NXOpen::Facet::FacetModelingCollection::CreatePolygonModelingBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ConvertType </term> <description> 
##  
## Convergent </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX12.0.0  <br> 

class PolygonModelingBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.PolygonModelingBuilder</ja_class> builder. 
    """


    ##  the conversion type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Convergent</term><description> 
    ## </description> </item><item><term> 
    ## Facet</term><description> 
    ## </description> </item></list>
    class ConvertTypes(Enum):
        """
        Members Include: <Convergent> <Facet>
        """
        Convergent: int
        Facet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PolygonModelingBuilder.ConvertTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link PolygonModelingBuilder.ConvertTypes NXOpen.Facet.PolygonModelingBuilder.ConvertTypes@endlink) ConvertType
    ##  Returns the convert type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return PolygonModelingBuilder.ConvertTypes
    @property
    def ConvertType(self) -> PolygonModelingBuilder.ConvertTypes:
        """
        Getter for property: (@link PolygonModelingBuilder.ConvertTypes NXOpen.Facet.PolygonModelingBuilder.ConvertTypes@endlink) ConvertType
         Returns the convert type   
            
         
        """
        pass
    
    ## Setter for property: (@link PolygonModelingBuilder.ConvertTypes NXOpen.Facet.PolygonModelingBuilder.ConvertTypes@endlink) ConvertType

    ##  Returns the convert type   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ConvertType.setter
    def ConvertType(self, convertType: PolygonModelingBuilder.ConvertTypes):
        """
        Setter for property: (@link PolygonModelingBuilder.ConvertTypes NXOpen.Facet.PolygonModelingBuilder.ConvertTypes@endlink) ConvertType
         Returns the convert type   
            
         
        """
        pass
    
    ## Getter for property: (bool) EditCopy
    ##  Returns the option to create a non-associative copy of the selected body and edit that copy   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def EditCopy(self) -> bool:
        """
        Getter for property: (bool) EditCopy
         Returns the option to create a non-associative copy of the selected body and edit that copy   
            
         
        """
        pass
    
    ## Setter for property: (bool) EditCopy

    ##  Returns the option to create a non-associative copy of the selected body and edit that copy   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @EditCopy.setter
    def EditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) EditCopy
         Returns the option to create a non-associative copy of the selected body and edit that copy   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectFacetBodies
    ##  Returns the selected bodies   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def SelectFacetBodies(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectFacetBodies
         Returns the selected bodies   
            
         
        """
        pass
    
    ##  Merges all faces of the input body
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ## <param name="bodyTag"> (@link NXOpen.Body NXOpen.Body@endlink) </param>
    def MergeAllFaces(self, bodyTag: NXOpen.Body) -> None:
        """
         Merges all faces of the input body
        """
        pass
    
    ##  Removes the parameters of the input body
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ## <param name="bodyTag"> (@link NXOpen.Body NXOpen.Body@endlink) </param>
    def RemoveParameterOfBody(self, bodyTag: NXOpen.Body) -> None:
        """
         Removes the parameters of the input body
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Facet::RemeshFacetBodyBuilder NXOpen::Facet::RemeshFacetBodyBuilder@endlink .
##         This class remeshes selected facet regions to specified density. <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateRemeshFacetBodyBuilder  NXOpen::Facet::FacetModelingCollection::CreateRemeshFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AngularThreshold </term> <description> 
##  
## 30 </description> </item> 
## 
## <item><term> 
##  
## AverageSize.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ChordalTolerance </term> <description> 
##  
## 0.1 (millimeters part), 0.004 (inches part) </description> </item> 
## 
## <item><term> 
##  
## IsEditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsLockBoundary </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsShowDeviationPlot </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## MaximumSize.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RemeshMode </term> <description> 
##  
## Constant </description> </item> 
## 
## <item><term> 
##  
## SharpEdgesLockOption </term> <description> 
##  
## NoLock </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1847.0.0  <br> 

class RemeshFacetBodyBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Facet.RemeshFacetBodyBuilder</ja_class>.
        This class remeshes selected facet regions to specified density."""


    ##   Remesh mode definitions 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Constant</term><description> 
    ## </description> </item><item><term> 
    ## Variable</term><description> 
    ## </description> </item></list>
    class RemeshModeType(Enum):
        """
        Members Include: <Constant> <Variable>
        """
        Constant: int
        Variable: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RemeshFacetBodyBuilder.RemeshModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   Sharp Edges lock definitions 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoLock</term><description> 
    ## </description> </item><item><term> 
    ## SoftLock</term><description> 
    ## </description> </item><item><term> 
    ## HardLock</term><description> 
    ## </description> </item></list>
    class SharpEdgesLockType(Enum):
        """
        Members Include: <NoLock> <SoftLock> <HardLock>
        """
        NoLock: int
        SoftLock: int
        HardLock: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RemeshFacetBodyBuilder.SharpEdgesLockType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) AngularThreshold
    ##  Returns the AngularThreshold for remesh  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def AngularThreshold(self) -> float:
        """
        Getter for property: (float) AngularThreshold
         Returns the AngularThreshold for remesh  
            
         
        """
        pass
    
    ## Setter for property: (float) AngularThreshold

    ##  Returns the AngularThreshold for remesh  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @AngularThreshold.setter
    def AngularThreshold(self, angularThreshold: float):
        """
        Setter for property: (float) AngularThreshold
         Returns the AngularThreshold for remesh  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AverageSize
    ##  Returns the AverageSize for remesh  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AverageSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AverageSize
         Returns the AverageSize for remesh  
            
         
        """
        pass
    
    ## Getter for property: (float) ChordalTolerance
    ##  Returns the ChordalTolerance for remesh  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def ChordalTolerance(self) -> float:
        """
        Getter for property: (float) ChordalTolerance
         Returns the ChordalTolerance for remesh  
            
         
        """
        pass
    
    ## Setter for property: (float) ChordalTolerance

    ##  Returns the ChordalTolerance for remesh  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ChordalTolerance.setter
    def ChordalTolerance(self, chordalTolerance: float):
        """
        Setter for property: (float) ChordalTolerance
         Returns the ChordalTolerance for remesh  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetRegion
    ##  Returns the facets to be remeshed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetRegion(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetRegion
         Returns the facets to be remeshed   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsEditCopy
    ##  Returns the option to create a non-associative copy of the selected body and edit that copy   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the option to create a non-associative copy of the selected body and edit that copy   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsEditCopy

    ##  Returns the option to create a non-associative copy of the selected body and edit that copy   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the option to create a non-associative copy of the selected body and edit that copy   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsLockBoundary
    ##  Returns the option to lock boundary of remesh regions   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def IsLockBoundary(self) -> bool:
        """
        Getter for property: (bool) IsLockBoundary
         Returns the option to lock boundary of remesh regions   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsLockBoundary

    ##  Returns the option to lock boundary of remesh regions   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @IsLockBoundary.setter
    def IsLockBoundary(self, isLockBoundary: bool):
        """
        Setter for property: (bool) IsLockBoundary
         Returns the option to lock boundary of remesh regions   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsShowDeviationPlot
    ##  Returns the option to show deviation plot   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def IsShowDeviationPlot(self) -> bool:
        """
        Getter for property: (bool) IsShowDeviationPlot
         Returns the option to show deviation plot   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsShowDeviationPlot

    ##  Returns the option to show deviation plot   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @IsShowDeviationPlot.setter
    def IsShowDeviationPlot(self, isShowDeviationPlot: bool):
        """
        Setter for property: (bool) IsShowDeviationPlot
         Returns the option to show deviation plot   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumSize
    ##  Returns the MaximumSize for remesh  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumSize
         Returns the MaximumSize for remesh  
            
         
        """
        pass
    
    ## Getter for property: (@link RemeshFacetBodyBuilder.RemeshModeType NXOpen.Facet.RemeshFacetBodyBuilder.RemeshModeType@endlink) RemeshMode
    ##  Returns the Mode for remesh  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return RemeshFacetBodyBuilder.RemeshModeType
    @property
    def RemeshMode(self) -> RemeshFacetBodyBuilder.RemeshModeType:
        """
        Getter for property: (@link RemeshFacetBodyBuilder.RemeshModeType NXOpen.Facet.RemeshFacetBodyBuilder.RemeshModeType@endlink) RemeshMode
         Returns the Mode for remesh  
            
         
        """
        pass
    
    ## Setter for property: (@link RemeshFacetBodyBuilder.RemeshModeType NXOpen.Facet.RemeshFacetBodyBuilder.RemeshModeType@endlink) RemeshMode

    ##  Returns the Mode for remesh  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RemeshMode.setter
    def RemeshMode(self, remeshMode: RemeshFacetBodyBuilder.RemeshModeType):
        """
        Setter for property: (@link RemeshFacetBodyBuilder.RemeshModeType NXOpen.Facet.RemeshFacetBodyBuilder.RemeshModeType@endlink) RemeshMode
         Returns the Mode for remesh  
            
         
        """
        pass
    
    ## Getter for property: (@link RemeshFacetBodyBuilder.SharpEdgesLockType NXOpen.Facet.RemeshFacetBodyBuilder.SharpEdgesLockType@endlink) SharpEdgesLockOption
    ##  Returns the Option for sharp edges lock type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return RemeshFacetBodyBuilder.SharpEdgesLockType
    @property
    def SharpEdgesLockOption(self) -> RemeshFacetBodyBuilder.SharpEdgesLockType:
        """
        Getter for property: (@link RemeshFacetBodyBuilder.SharpEdgesLockType NXOpen.Facet.RemeshFacetBodyBuilder.SharpEdgesLockType@endlink) SharpEdgesLockOption
         Returns the Option for sharp edges lock type  
            
         
        """
        pass
    
    ## Setter for property: (@link RemeshFacetBodyBuilder.SharpEdgesLockType NXOpen.Facet.RemeshFacetBodyBuilder.SharpEdgesLockType@endlink) SharpEdgesLockOption

    ##  Returns the Option for sharp edges lock type  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @SharpEdgesLockOption.setter
    def SharpEdgesLockOption(self, sharpEdgesLockType: RemeshFacetBodyBuilder.SharpEdgesLockType):
        """
        Setter for property: (@link RemeshFacetBodyBuilder.SharpEdgesLockType NXOpen.Facet.RemeshFacetBodyBuilder.SharpEdgesLockType@endlink) SharpEdgesLockOption
         Returns the Option for sharp edges lock type  
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Facet::ReplaceMeshWithFaceBuilder NXOpen::Facet::ReplaceMeshWithFaceBuilder@endlink .
##     Replace Mesh With Face Builder is a function to facilitate the creation of prismatic faces 
##     through selected facet regions and replace that facet region with the analytic face.  <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateReplaceMeshWithFaceBuilder  NXOpen::Facet::FacetModelingCollection::CreateReplaceMeshWithFaceBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ConeAverageConstrainToDirectionToggle </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ConeConstraintTypes </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## ConeHalfAngle.Value </term> <description> 
##  
## 45 </description> </item> 
## 
## <item><term> 
##  
## CylinderAverageConstrainToDirectionToggle </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CylinderConstraintTypes </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## CylinderOrSphereRadius.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## HalfAngleToggle </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## MaxDeviation.Value </term> <description> 
##  
## 0.5 (millimeters part), 0.02 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MinimumFacetNumber </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## PlaneAverageConstrainToNormalToggle </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## PlaneConstraintTypes </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## RadiusToggle </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ReplaceMeshOn </term> <description> 
##  
## OriginalBody </description> </item> 
## 
## <item><term> 
##  
## SphereConstraintTypes </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class ReplaceMeshWithFaceBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Facet.ReplaceMeshWithFaceBuilder</ja_class>.
    Replace Mesh With Face Builder is a function to facilitate the creation of prismatic faces 
    through selected facet regions and replace that facet region with the analytic face. """


    ##  Constraints for cone 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None constraint for cone </description> </item><item><term> 
    ## Parallel</term><description> 
    ##  Parallel constraint for cone </description> </item><item><term> 
    ## Colinear</term><description> 
    ##  Colinear constraint for cone </description> </item><item><term> 
    ## AverageParallel</term><description> 
    ##  AverageParallel constraint for cone </description> </item><item><term> 
    ## AverageColinear</term><description> 
    ##  AverageColinear constraint for cone </description> </item></list>
    class ConeConstraint(Enum):
        """
        Members Include: <NotSet> <Parallel> <Colinear> <AverageParallel> <AverageColinear>
        """
        NotSet: int
        Parallel: int
        Colinear: int
        AverageParallel: int
        AverageColinear: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReplaceMeshWithFaceBuilder.ConeConstraint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Constraints for cylinder 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None constraint for cylinder </description> </item><item><term> 
    ## Parallel</term><description> 
    ##  Parallel constraint for cylinder </description> </item><item><term> 
    ## Colinear</term><description> 
    ##  Colinear constraint for cylinder </description> </item><item><term> 
    ## AverageParallel</term><description> 
    ##  AverageParallel constraint for cylinder </description> </item><item><term> 
    ## AverageColinear</term><description> 
    ##  AverageColinear constraint for cylinder </description> </item></list>
    class CylinderConstraint(Enum):
        """
        Members Include: <NotSet> <Parallel> <Colinear> <AverageParallel> <AverageColinear>
        """
        NotSet: int
        Parallel: int
        Colinear: int
        AverageParallel: int
        AverageColinear: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReplaceMeshWithFaceBuilder.CylinderConstraint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Constraints for plane 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None constraint for plane </description> </item><item><term> 
    ## Orthogonal</term><description> 
    ##  Orthogonal constraint for plane </description> </item><item><term> 
    ## Parallel</term><description> 
    ##  Parallel constraint for plane </description> </item><item><term> 
    ## Coplanar</term><description> 
    ##  Coplanar constraint for plane </description> </item><item><term> 
    ## AverageParallel</term><description> 
    ##  AverageParallel constraint for plane </description> </item><item><term> 
    ## AverageCoplanar</term><description> 
    ##  AverageCoplanar constraint for plane </description> </item></list>
    class PlaneConstraint(Enum):
        """
        Members Include: <NotSet> <Orthogonal> <Parallel> <Coplanar> <AverageParallel> <AverageCoplanar>
        """
        NotSet: int
        Orthogonal: int
        Parallel: int
        Coplanar: int
        AverageParallel: int
        AverageCoplanar: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReplaceMeshWithFaceBuilder.PlaneConstraint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Replace mesh on enum
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## OriginalBody</term><description> 
    ##  Replace mesh on original body</description> </item><item><term> 
    ## NewBody</term><description> 
    ##  Replace mesh on new body </description> </item></list>
    class ReplaceMeshOnOption(Enum):
        """
        Members Include: <OriginalBody> <NewBody>
        """
        OriginalBody: int
        NewBody: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Constraints for sphere 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None constraint for sphere </description> </item><item><term> 
    ## Concentric</term><description> 
    ##  Concentric constraint for sphere </description> </item><item><term> 
    ## AverageConcentric</term><description> 
    ##  AverageConcentric constraint for sphere </description> </item></list>
    class SphereConstraint(Enum):
        """
        Members Include: <NotSet> <Concentric> <AverageConcentric>
        """
        NotSet: int
        Concentric: int
        AverageConcentric: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReplaceMeshWithFaceBuilder.SphereConstraint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Primitive types to divide facet face 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Plane</term><description> 
    ##  Divide facet face to fit the plane </description> </item><item><term> 
    ## Cylinder</term><description> 
    ##  Divide facet face to fit the cylinder </description> </item><item><term> 
    ## Cone</term><description> 
    ##  Divide facet face to fit the cone </description> </item><item><term> 
    ## Sphere</term><description> 
    ##  Divide facet face to fit the sphere </description> </item></list>
    class Types(Enum):
        """
        Members Include: <Plane> <Cylinder> <Cone> <Sphere>
        """
        Plane: int
        Cylinder: int
        Cone: int
        Sphere: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReplaceMeshWithFaceBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) ConeAverageConstrainToDirectionToggle
    ##  Returns the cone average constrain to direction toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def ConeAverageConstrainToDirectionToggle(self) -> bool:
        """
        Getter for property: (bool) ConeAverageConstrainToDirectionToggle
         Returns the cone average constrain to direction toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ConeAverageConstrainToDirectionToggle

    ##  Returns the cone average constrain to direction toggle   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ConeAverageConstrainToDirectionToggle.setter
    def ConeAverageConstrainToDirectionToggle(self, coneAverageConstrainToDirectionToggle: bool):
        """
        Setter for property: (bool) ConeAverageConstrainToDirectionToggle
         Returns the cone average constrain to direction toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConeAverageConstrainToDirectionVector
    ##  Returns the cone average constrain to direction vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ConeAverageConstrainToDirectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConeAverageConstrainToDirectionVector
         Returns the cone average constrain to direction vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConeAverageConstrainToDirectionVector

    ##  Returns the cone average constrain to direction vector   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ConeAverageConstrainToDirectionVector.setter
    def ConeAverageConstrainToDirectionVector(self, coneAverageConstrainToDirectionVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConeAverageConstrainToDirectionVector
         Returns the cone average constrain to direction vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) ConeColinearConstraintAxis
    ##  Returns the cone colinear constraint axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Axis
    @property
    def ConeColinearConstraintAxis(self) -> NXOpen.Axis:
        """
        Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) ConeColinearConstraintAxis
         Returns the cone colinear constraint axis   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) ConeColinearConstraintAxis

    ##  Returns the cone colinear constraint axis   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ConeColinearConstraintAxis.setter
    def ConeColinearConstraintAxis(self, coneColinearConstraintAxis: NXOpen.Axis):
        """
        Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) ConeColinearConstraintAxis
         Returns the cone colinear constraint axis   
            
         
        """
        pass
    
    ## Getter for property: (@link ReplaceMeshWithFaceBuilder.ConeConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.ConeConstraint@endlink) ConeConstraintTypes
    ##  Returns the cone constraint types   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ReplaceMeshWithFaceBuilder.ConeConstraint
    @property
    def ConeConstraintTypes(self) -> ReplaceMeshWithFaceBuilder.ConeConstraint:
        """
        Getter for property: (@link ReplaceMeshWithFaceBuilder.ConeConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.ConeConstraint@endlink) ConeConstraintTypes
         Returns the cone constraint types   
            
         
        """
        pass
    
    ## Setter for property: (@link ReplaceMeshWithFaceBuilder.ConeConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.ConeConstraint@endlink) ConeConstraintTypes

    ##  Returns the cone constraint types   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ConeConstraintTypes.setter
    def ConeConstraintTypes(self, coneConstraintTypes: ReplaceMeshWithFaceBuilder.ConeConstraint):
        """
        Setter for property: (@link ReplaceMeshWithFaceBuilder.ConeConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.ConeConstraint@endlink) ConeConstraintTypes
         Returns the cone constraint types   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ConeHalfAngle
    ##  Returns the cone half angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ConeHalfAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ConeHalfAngle
         Returns the cone half angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConeParallelConstraintVector
    ##  Returns the cone parallel constraint vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ConeParallelConstraintVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConeParallelConstraintVector
         Returns the cone parallel constraint vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConeParallelConstraintVector

    ##  Returns the cone parallel constraint vector   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ConeParallelConstraintVector.setter
    def ConeParallelConstraintVector(self, coneParallelConstraintVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConeParallelConstraintVector
         Returns the cone parallel constraint vector   
            
         
        """
        pass
    
    ## Getter for property: (bool) CylinderAverageConstrainToDirectionToggle
    ##  Returns the cylinder average constrain to direction toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def CylinderAverageConstrainToDirectionToggle(self) -> bool:
        """
        Getter for property: (bool) CylinderAverageConstrainToDirectionToggle
         Returns the cylinder average constrain to direction toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) CylinderAverageConstrainToDirectionToggle

    ##  Returns the cylinder average constrain to direction toggle   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CylinderAverageConstrainToDirectionToggle.setter
    def CylinderAverageConstrainToDirectionToggle(self, cylinderAverageConstrainToDirectionToggle: bool):
        """
        Setter for property: (bool) CylinderAverageConstrainToDirectionToggle
         Returns the cylinder average constrain to direction toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) CylinderAverageConstrainToDirectionVector
    ##  Returns the cylinder average constrain to direction vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def CylinderAverageConstrainToDirectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) CylinderAverageConstrainToDirectionVector
         Returns the cylinder average constrain to direction vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) CylinderAverageConstrainToDirectionVector

    ##  Returns the cylinder average constrain to direction vector   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CylinderAverageConstrainToDirectionVector.setter
    def CylinderAverageConstrainToDirectionVector(self, cylinderAverageConstrainToDirectionVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) CylinderAverageConstrainToDirectionVector
         Returns the cylinder average constrain to direction vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) CylinderColinearConstraintAxis
    ##  Returns the cylinder colinear constraint axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Axis
    @property
    def CylinderColinearConstraintAxis(self) -> NXOpen.Axis:
        """
        Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) CylinderColinearConstraintAxis
         Returns the cylinder colinear constraint axis   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) CylinderColinearConstraintAxis

    ##  Returns the cylinder colinear constraint axis   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CylinderColinearConstraintAxis.setter
    def CylinderColinearConstraintAxis(self, cylinderColinearConstraintAxis: NXOpen.Axis):
        """
        Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) CylinderColinearConstraintAxis
         Returns the cylinder colinear constraint axis   
            
         
        """
        pass
    
    ## Getter for property: (@link ReplaceMeshWithFaceBuilder.CylinderConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.CylinderConstraint@endlink) CylinderConstraintTypes
    ##  Returns the cylinder constraint types   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ReplaceMeshWithFaceBuilder.CylinderConstraint
    @property
    def CylinderConstraintTypes(self) -> ReplaceMeshWithFaceBuilder.CylinderConstraint:
        """
        Getter for property: (@link ReplaceMeshWithFaceBuilder.CylinderConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.CylinderConstraint@endlink) CylinderConstraintTypes
         Returns the cylinder constraint types   
            
         
        """
        pass
    
    ## Setter for property: (@link ReplaceMeshWithFaceBuilder.CylinderConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.CylinderConstraint@endlink) CylinderConstraintTypes

    ##  Returns the cylinder constraint types   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CylinderConstraintTypes.setter
    def CylinderConstraintTypes(self, cylinderConstraintTypes: ReplaceMeshWithFaceBuilder.CylinderConstraint):
        """
        Setter for property: (@link ReplaceMeshWithFaceBuilder.CylinderConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.CylinderConstraint@endlink) CylinderConstraintTypes
         Returns the cylinder constraint types   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CylinderOrSphereRadius
    ##  Returns the cylinder or sphere radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def CylinderOrSphereRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CylinderOrSphereRadius
         Returns the cylinder or sphere radius   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) CylinderParallelConstraintVector
    ##  Returns the cylinder parallel constraint vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def CylinderParallelConstraintVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) CylinderParallelConstraintVector
         Returns the cylinder parallel constraint vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) CylinderParallelConstraintVector

    ##  Returns the cylinder parallel constraint vector   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CylinderParallelConstraintVector.setter
    def CylinderParallelConstraintVector(self, cylinderParallelConstraintVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) CylinderParallelConstraintVector
         Returns the cylinder parallel constraint vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
    ##  Returns the face collector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns the face collector   
            
         
        """
        pass
    
    ## Getter for property: (bool) HalfAngleToggle
    ##  Returns the half angle toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def HalfAngleToggle(self) -> bool:
        """
        Getter for property: (bool) HalfAngleToggle
         Returns the half angle toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) HalfAngleToggle

    ##  Returns the half angle toggle   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @HalfAngleToggle.setter
    def HalfAngleToggle(self, halfAngleToggle: bool):
        """
        Setter for property: (bool) HalfAngleToggle
         Returns the half angle toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDeviation
    ##  Returns the max deviation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxDeviation(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxDeviation
         Returns the max deviation   
            
         
        """
        pass
    
    ## Getter for property: (int) MinimumFacetNumber
    ##  Returns the minimum facet number   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return int
    @property
    def MinimumFacetNumber(self) -> int:
        """
        Getter for property: (int) MinimumFacetNumber
         Returns the minimum facet number   
            
         
        """
        pass
    
    ## Setter for property: (int) MinimumFacetNumber

    ##  Returns the minimum facet number   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @MinimumFacetNumber.setter
    def MinimumFacetNumber(self, minimumFacetNumber: int):
        """
        Setter for property: (int) MinimumFacetNumber
         Returns the minimum facet number   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) OrthogonalOrCoplanarConstraintPlane
    ##  Returns the orthogonal or coplanar constraint plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def OrthogonalOrCoplanarConstraintPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) OrthogonalOrCoplanarConstraintPlane
         Returns the orthogonal or coplanar constraint plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) OrthogonalOrCoplanarConstraintPlane

    ##  Returns the orthogonal or coplanar constraint plane   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @OrthogonalOrCoplanarConstraintPlane.setter
    def OrthogonalOrCoplanarConstraintPlane(self, orthogonalOrCoplanarConstraintPlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) OrthogonalOrCoplanarConstraintPlane
         Returns the orthogonal or coplanar constraint plane   
            
         
        """
        pass
    
    ## Getter for property: (bool) PlaneAverageConstrainToNormalToggle
    ##  Returns the plane average constrain to normal toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def PlaneAverageConstrainToNormalToggle(self) -> bool:
        """
        Getter for property: (bool) PlaneAverageConstrainToNormalToggle
         Returns the plane average constrain to normal toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) PlaneAverageConstrainToNormalToggle

    ##  Returns the plane average constrain to normal toggle   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @PlaneAverageConstrainToNormalToggle.setter
    def PlaneAverageConstrainToNormalToggle(self, planeAverageConstrainToNormalToggle: bool):
        """
        Setter for property: (bool) PlaneAverageConstrainToNormalToggle
         Returns the plane average constrain to normal toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) PlaneAverageConstrainToNormalVector
    ##  Returns the plane average constrain to normal vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def PlaneAverageConstrainToNormalVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) PlaneAverageConstrainToNormalVector
         Returns the plane average constrain to normal vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) PlaneAverageConstrainToNormalVector

    ##  Returns the plane average constrain to normal vector   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @PlaneAverageConstrainToNormalVector.setter
    def PlaneAverageConstrainToNormalVector(self, planeAverageConstrainToNormalVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) PlaneAverageConstrainToNormalVector
         Returns the plane average constrain to normal vector   
            
         
        """
        pass
    
    ## Getter for property: (@link ReplaceMeshWithFaceBuilder.PlaneConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.PlaneConstraint@endlink) PlaneConstraintTypes
    ##  Returns the plane constraint types   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ReplaceMeshWithFaceBuilder.PlaneConstraint
    @property
    def PlaneConstraintTypes(self) -> ReplaceMeshWithFaceBuilder.PlaneConstraint:
        """
        Getter for property: (@link ReplaceMeshWithFaceBuilder.PlaneConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.PlaneConstraint@endlink) PlaneConstraintTypes
         Returns the plane constraint types   
            
         
        """
        pass
    
    ## Setter for property: (@link ReplaceMeshWithFaceBuilder.PlaneConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.PlaneConstraint@endlink) PlaneConstraintTypes

    ##  Returns the plane constraint types   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @PlaneConstraintTypes.setter
    def PlaneConstraintTypes(self, planeConstraintTypes: ReplaceMeshWithFaceBuilder.PlaneConstraint):
        """
        Setter for property: (@link ReplaceMeshWithFaceBuilder.PlaneConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.PlaneConstraint@endlink) PlaneConstraintTypes
         Returns the plane constraint types   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) PlaneParallelConstraintNormal
    ##  Returns the plane parallel constraint normal   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def PlaneParallelConstraintNormal(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) PlaneParallelConstraintNormal
         Returns the plane parallel constraint normal   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) PlaneParallelConstraintNormal

    ##  Returns the plane parallel constraint normal   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @PlaneParallelConstraintNormal.setter
    def PlaneParallelConstraintNormal(self, planeParallelConstraintNormal: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) PlaneParallelConstraintNormal
         Returns the plane parallel constraint normal   
            
         
        """
        pass
    
    ## Getter for property: (bool) RadiusToggle
    ##  Returns the radius toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def RadiusToggle(self) -> bool:
        """
        Getter for property: (bool) RadiusToggle
         Returns the radius toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) RadiusToggle

    ##  Returns the radius toggle   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RadiusToggle.setter
    def RadiusToggle(self, radiusToggle: bool):
        """
        Setter for property: (bool) RadiusToggle
         Returns the radius toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption NXOpen.Facet.ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption@endlink) ReplaceMeshOn
    ##  Returns the replace mesh on enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption
    @property
    def ReplaceMeshOn(self) -> ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption:
        """
        Getter for property: (@link ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption NXOpen.Facet.ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption@endlink) ReplaceMeshOn
         Returns the replace mesh on enum   
            
         
        """
        pass
    
    ## Setter for property: (@link ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption NXOpen.Facet.ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption@endlink) ReplaceMeshOn

    ##  Returns the replace mesh on enum   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ReplaceMeshOn.setter
    def ReplaceMeshOn(self, replaceMeshOn: ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption):
        """
        Setter for property: (@link ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption NXOpen.Facet.ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption@endlink) ReplaceMeshOn
         Returns the replace mesh on enum   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SphereConcentricConstraintPoint
    ##  Returns the sphere concentric constraint point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def SphereConcentricConstraintPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SphereConcentricConstraintPoint
         Returns the sphere concentric constraint point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SphereConcentricConstraintPoint

    ##  Returns the sphere concentric constraint point   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SphereConcentricConstraintPoint.setter
    def SphereConcentricConstraintPoint(self, sphereConcentricConstraintPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SphereConcentricConstraintPoint
         Returns the sphere concentric constraint point   
            
         
        """
        pass
    
    ## Getter for property: (@link ReplaceMeshWithFaceBuilder.SphereConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.SphereConstraint@endlink) SphereConstraintTypes
    ##  Returns the sphere constraint types   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ReplaceMeshWithFaceBuilder.SphereConstraint
    @property
    def SphereConstraintTypes(self) -> ReplaceMeshWithFaceBuilder.SphereConstraint:
        """
        Getter for property: (@link ReplaceMeshWithFaceBuilder.SphereConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.SphereConstraint@endlink) SphereConstraintTypes
         Returns the sphere constraint types   
            
         
        """
        pass
    
    ## Setter for property: (@link ReplaceMeshWithFaceBuilder.SphereConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.SphereConstraint@endlink) SphereConstraintTypes

    ##  Returns the sphere constraint types   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SphereConstraintTypes.setter
    def SphereConstraintTypes(self, sphereConstraintTypes: ReplaceMeshWithFaceBuilder.SphereConstraint):
        """
        Setter for property: (@link ReplaceMeshWithFaceBuilder.SphereConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.SphereConstraint@endlink) SphereConstraintTypes
         Returns the sphere constraint types   
            
         
        """
        pass
    
    ## Getter for property: (@link ReplaceMeshWithFaceBuilder.Types NXOpen.Facet.ReplaceMeshWithFaceBuilder.Types@endlink) Type
    ##  Returns the type of enum which decides method for dividing facet faces  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return ReplaceMeshWithFaceBuilder.Types
    @property
    def Type(self) -> ReplaceMeshWithFaceBuilder.Types:
        """
        Getter for property: (@link ReplaceMeshWithFaceBuilder.Types NXOpen.Facet.ReplaceMeshWithFaceBuilder.Types@endlink) Type
         Returns the type of enum which decides method for dividing facet faces  
            
         
        """
        pass
    
    ## Setter for property: (@link ReplaceMeshWithFaceBuilder.Types NXOpen.Facet.ReplaceMeshWithFaceBuilder.Types@endlink) Type

    ##  Returns the type of enum which decides method for dividing facet faces  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Type.setter
    def Type(self, type: ReplaceMeshWithFaceBuilder.Types):
        """
        Setter for property: (@link ReplaceMeshWithFaceBuilder.Types NXOpen.Facet.ReplaceMeshWithFaceBuilder.Types@endlink) Type
         Returns the type of enum which decides method for dividing facet faces  
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Facet::SculptMeshBuilder NXOpen::Facet::SculptMeshBuilder@endlink .
##         This class provides the ability to sculpt the shape of a facet body by pushing or pulling facets within a locally defined area. <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateSculptMeshBuilder  NXOpen::Facet::FacetModelingCollection::CreateSculptMeshBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## EditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## FallOffFactor </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## MaximumOffset.Value </term> <description> 
##  
## 1 (millimeters part), 0.05 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Width.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2212.0.0  <br> 

class SculptMeshBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Facet.SculptMeshBuilder</ja_class>.
        This class provides the ability to sculpt the shape of a facet body by pushing or pulling facets within a locally defined area."""


    ## Getter for property: (bool) EditCopy
    ##  Returns the edit copy   
    ##     
    ##  
    ## Getter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def EditCopy(self) -> bool:
        """
        Getter for property: (bool) EditCopy
         Returns the edit copy   
            
         
        """
        pass
    
    ## Setter for property: (bool) EditCopy

    ##  Returns the edit copy   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @EditCopy.setter
    def EditCopy(self, editCopy: bool):
        """
        Setter for property: (bool) EditCopy
         Returns the edit copy   
            
         
        """
        pass
    
    ## Getter for property: (float) FallOffFactor
    ##  Returns the falloff factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def FallOffFactor(self) -> float:
        """
        Getter for property: (float) FallOffFactor
         Returns the falloff factor   
            
         
        """
        pass
    
    ## Setter for property: (float) FallOffFactor

    ##  Returns the falloff factor   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @FallOffFactor.setter
    def FallOffFactor(self, fallOffFactor: float):
        """
        Setter for property: (float) FallOffFactor
         Returns the falloff factor   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumOffset
    ##  Returns the maximum offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumOffset
         Returns the maximum offset   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) TargetFacetBody
    ##  Returns the target body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return SelectFacetedBodyList
    @property
    def TargetFacetBody(self) -> SelectFacetedBodyList:
        """
        Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) TargetFacetBody
         Returns the target body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.StrokeGestureData NXOpen.GeometricUtilities.StrokeGestureData@endlink) Tool
    ##  Returns the sculpting tool   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.StrokeGestureData
    @property
    def Tool(self) -> NXOpen.GeometricUtilities.StrokeGestureData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.StrokeGestureData NXOpen.GeometricUtilities.StrokeGestureData@endlink) Tool
         Returns the sculpting tool   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
    ##  Returns the width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
         Returns the width   
            
         
        """
        pass
    
    ##  Reset falloff factor to medium 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def ResetToMedium(self) -> None:
        """
         Reset falloff factor to medium 
        """
        pass
    
    ##   Sculpts the mesh based on the sculpting tool parameters and trajectory. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    def SculptMesh(self) -> None:
        """
          Sculpts the mesh based on the sculpting tool parameters and trajectory. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a list of objects on a selection list.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectFacetedBodyList(NXOpen.TaggedObject): 
    """ Represents a list of objects on a selection list.
"""


    ## Getter for property: (bool) DuplicatesAllowed
    ##  Returns whether duplicate objects are allowed in the selection list.  
    ##   
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def DuplicatesAllowed(self) -> bool:
        """
        Getter for property: (bool) DuplicatesAllowed
         Returns whether duplicate objects are allowed in the selection list.  
          
              
         
        """
        pass
    
    ## Getter for property: (int) Size
    ##  Returns the number of objects in the list.  
    ##   
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
         Returns the number of objects in the list.  
          
              
         
        """
        pass
    
    ##  Adds an object to the list
    ##     
    ##  @return added (bool):  True if successfully added to list;
    ##                                   False if the object was already a member
    ##                                   of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) </param>
    ## <param name="objectValue"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  object to add </param>
    @overload
    def Add(self, objectValue: FacetedBody) -> bool:
        """
         Adds an object to the list
            
         @return added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds a set of objects with views to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink)  objects to add </param>
    ## <param name="views"> (@link NXOpen.View List[NXOpen.View]@endlink)  views for the objects </param>
    def AddWithViews(self, objects: List[FacetedBody], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds a set of objects to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) </param>
    ## <param name="objects"> (@link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink)  objects to add </param>
    @overload
    def Add(self, objects: List[FacetedBody]) -> bool:
        """
         Adds a set of objects to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds the objects from a SelectionMethod to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) </param>
    ## <param name="input_selection_method"> (@link NXOpen.SelectionMethod NXOpen.SelectionMethod@endlink)  selection method containing objects to add </param>
    @overload
    def Add(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Adds the objects from a SelectionMethod to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds the object with the objects view and objects point
    ##     
    ##  @return added (bool):  True if successfully added to list;
    ##                                   False if the object was already a member
    ##                                   of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) </param>
    ## <param name="selection"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  selected object </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  selected object view</param>
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  selected object point</param>
    @overload
    def Add(self, selection: FacetedBody, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         @return added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) first  selected object point</param>
    ## <param name="selection2"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink) second  selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: FacetedBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: FacetedBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObjectList::Add NXOpen::SelectObjectList::Add@endlink .  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) </param>
    ## <param name="selection"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  selected object </param>
    ## <param name="cae_sub_type"> (@link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink)  CAE set object sub type</param>
    ## <param name="cae_sub_id"> (int)  CAE set object sub id</param>
    @overload
    def Add(self, selection: FacetedBody, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
        """
         The object being selected with CAE set object information.
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Removes all items from the list.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Clear(self) -> None:
        """
         Removes all items from the list.
            
        """
        pass
    
    ##  Returns whether the specified object is already in the list or not.
    ##     
    ##  @return list_contains (bool):  true if object is in the list, false otherwise .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectValue"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  object to check </param>
    def Contains(self, objectValue: FacetedBody) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         @return list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    
    ##  Returns the list of objects in the selection list.
    ##     
    ##  @return objects (@link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetArray(self) -> List[FacetedBody]:
        """
         Returns the list of objects in the selection list.
            
         @return objects (@link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink):  items in list .
        """
        pass
    
    ##  Returns the list of SelectObjects in the selection list.
    ##     
    ##  @return objects (@link NXOpen.SelectObject List[NXOpen.SelectObject]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         @return objects (@link NXOpen.SelectObject List[NXOpen.SelectObject]@endlink):  items in list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) </param>
    ## <param name="objectValue"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  Object to remove </param>
    @overload
    def Remove(self, objectValue: FacetedBody) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Remove specified objects from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink)  Objects to remove </param>
    def RemoveArray(self, objects: List[FacetedBody]) -> bool:
        """
         Remove specified objects from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object / view was not a member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) </param>
    ## <param name="objectValue"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  Object to remove </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  with this view</param>
    @overload
    def Remove(self, objectValue: FacetedBody, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object / view was not a member of the list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) first  selected object point</param>
    ## <param name="selection2"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink) second  selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: FacetedBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: FacetedBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Removes the objects from a SelectionMethod from the list
    ##     
    ##  @return removed (bool):  True if successfully removed all objects from the list;
    ##                                     False if there was at least one object that was not a
    ##                                     member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) </param>
    ## <param name="input_selection_method"> (@link NXOpen.SelectionMethod NXOpen.SelectionMethod@endlink)  selection method containing objects to add </param>
    @overload
    def Remove(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Removes the objects from a SelectionMethod from the list
            
         @return removed (bool):  True if successfully removed all objects from the list;
                                            False if there was at least one object that was not a
                                            member of the list .
        """
        pass
    
    ##  Sets the list of objects in the selection list. This will clear any existing
    ##     items in the list.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link FacetedBody List[NXOpen.Facet.FacetedBody]@endlink)  items to put in the list</param>
    def SetArray(self, objects: List[FacetedBody]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a single object selection.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectFacetedBody(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""


    ## Getter for property: (@link FacetedBody NXOpen.Facet.FacetedBody@endlink) Value
    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return FacetedBody
    @property
    def Value(self) -> FacetedBody:
        """
        Getter for property: (@link FacetedBody NXOpen.Facet.FacetedBody@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ## Setter for property: (@link FacetedBody NXOpen.Facet.FacetedBody@endlink) Value

    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Value.setter
    def Value(self, selection: FacetedBody):
        """
        Setter for property: (@link FacetedBody NXOpen.Facet.FacetedBody@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ##  The object being selected with the object's view and point.
    ##     
    ##  @return A tuple consisting of (selection, view, point). 
    ##  - selection is: @link FacetedBody NXOpen.Facet.FacetedBody@endlink. selected object .
    ##  - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
    ##  - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[FacetedBody, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         @return A tuple consisting of (selection, view, point). 
         - selection is: @link FacetedBody NXOpen.Facet.FacetedBody@endlink. selected object .
         - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
         - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

        """
        pass
    
    ##  The object being selected with the objects view and point and snap information.
    ##     
    ##  @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
    ##  - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
    ##  - selection1 is: @link FacetedBody NXOpen.Facet.FacetedBody@endlink. first selected object .
    ##  - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
    ##  - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
    ##  - selection2 is: @link FacetedBody NXOpen.Facet.FacetedBody@endlink. second selected object .
    ##  - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
    ##  - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, FacetedBody, NXOpen.View, NXOpen.Point3d, FacetedBody, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
         - selection1 is: @link FacetedBody NXOpen.Facet.FacetedBody@endlink. first selected object .
         - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
         - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
         - selection2 is: @link FacetedBody NXOpen.Facet.FacetedBody@endlink. second selected object .
         - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
         - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
    ##  - selection is: @link FacetedBody NXOpen.Facet.FacetedBody@endlink. selected object .
    ##  - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
    ##  - cae_sub_id is: int. CAE set object sub id.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObject::GetValue NXOpen::SelectObject::GetValue@endlink .  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[FacetedBody, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is: @link FacetedBody NXOpen.Facet.FacetedBody@endlink. selected object .
         - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    
    ##  The object being selected with the object's view and object's point
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) </param>
    ## <param name="selection"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  selected object </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  selected object view</param>
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  selected object point</param>
    @overload
    def SetValue(self, selection: FacetedBody, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  first selected object point</param>
    ## <param name="selection2"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink)  second selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: FacetedBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: FacetedBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObject::SetValue NXOpen::SelectObject::SetValue@endlink .  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) </param>
    ## <param name="selection"> (@link FacetedBody NXOpen.Facet.FacetedBody@endlink)  selected object </param>
    ## <param name="cae_sub_type"> (@link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink)  CAE set object sub type</param>
    ## <param name="cae_sub_id"> (int)  CAE set object sub id</param>
    @overload
    def SetValue(self, selection: FacetedBody, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Facet::SewFacetBodyBuilder NXOpen::Facet::SewFacetBodyBuilder@endlink 
##     It sews two touching NX facet bodies. User need to specify the range on one of input body.
##     The range on the other body is calculated automatically by choosing the closest vertex.
##     It retruns a new mergered NX facet body. The two input bodies can be kept, deleted or hidden.
##      <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateSewFacetBodyBuilder  NXOpen::Facet::FacetedBodyCollection::CreateSewFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DeformDistance.Value </term> <description> 
##  
## 0.5 (millimeters part), 0.05 (inches part) </description> </item> 
## 
## <item><term> 
##  
## InputStatus </term> <description> 
##  
## Keep </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class SewFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Facet.SewFacetBodyBuilder</ja_class>
    It sews two touching NX facet bodies. User need to specify the range on one of input body.
    The range on the other body is calculated automatically by choosing the closest vertex.
    It retruns a new mergered NX facet body. The two input bodies can be kept, deleted or hidden.
    """


    ##  Represents the option for keeping, deleting or hiding input two facet bodies after builder committing 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Keep</term><description> 
    ##  Keep the input facet body after builder committing </description> </item><item><term> 
    ## Delete</term><description> 
    ##  Delete the input facet body after builder committing </description> </item><item><term> 
    ## Hide</term><description> 
    ##  Hide the input facet body after builder committing </description> </item></list>
    class Input(Enum):
        """
        Members Include: <Keep> <Delete> <Hide>
        """
        Keep: int
        Delete: int
        Hide: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SewFacetBodyBuilder.Input:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Index of the vertex 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## First</term><description> 
    ##  Index of the first vertex </description> </item><item><term> 
    ## Second</term><description> 
    ##  Index of the second vertex </description> </item></list>
    class VertexIndex(Enum):
        """
        Members Include: <First> <Second>
        """
        First: int
        Second: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SewFacetBodyBuilder.VertexIndex:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) DeformBody
    ##  Returns the deform body to be sewed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectFacetedBody
    @property
    def DeformBody(self) -> SelectFacetedBody:
        """
        Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) DeformBody
         Returns the deform body to be sewed   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeformDistance
    ##  Returns the distance to control the deform area on the deform body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DeformDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeformDistance
         Returns the distance to control the deform area on the deform body   
            
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##  Returns the distance tolerance used in the merge touching facet body feature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the merge touching facet body feature   
            
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##  Returns the distance tolerance used in the merge touching facet body feature   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the merge touching facet body feature   
            
         
        """
        pass
    
    ## Getter for property: (@link SewFacetBodyBuilder.Input NXOpen.Facet.SewFacetBodyBuilder.Input@endlink) InputStatus
    ##  Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SewFacetBodyBuilder.Input
    @property
    def InputStatus(self) -> SewFacetBodyBuilder.Input:
        """
        Getter for property: (@link SewFacetBodyBuilder.Input NXOpen.Facet.SewFacetBodyBuilder.Input@endlink) InputStatus
         Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
            
         
        """
        pass
    
    ## Setter for property: (@link SewFacetBodyBuilder.Input NXOpen.Facet.SewFacetBodyBuilder.Input@endlink) InputStatus

    ##  Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @InputStatus.setter
    def InputStatus(self, inputStatus: SewFacetBodyBuilder.Input):
        """
        Setter for property: (@link SewFacetBodyBuilder.Input NXOpen.Facet.SewFacetBodyBuilder.Input@endlink) InputStatus
         Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) TargetBody
    ##  Returns the target body to be sewed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectFacetedBody
    @property
    def TargetBody(self) -> SelectFacetedBody:
        """
        Getter for property: (@link SelectFacetedBody NXOpen.Facet.SelectFacetedBody@endlink) TargetBody
         Returns the target body to be sewed   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1
    ##  Returns the first vertex used to define the range   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Vertex1(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1
         Returns the first vertex used to define the range   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1

    ##  Returns the first vertex used to define the range   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Vertex1.setter
    def Vertex1(self, vertexPoint1: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex1
         Returns the first vertex used to define the range   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2
    ##  Returns the second vertex used to define the range   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Vertex2(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2
         Returns the second vertex used to define the range   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2

    ##  Returns the second vertex used to define the range   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Vertex2.setter
    def Vertex2(self, vertexPoint2: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Vertex2
         Returns the second vertex used to define the range   
            
         
        """
        pass
    
    ##  Flip the range between the first and second vertex 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def FlipRange(self) -> None:
        """
         Flip the range between the first and second vertex 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Facet::SmoothFacetBodyBuilder NXOpen::Facet::SmoothFacetBodyBuilder@endlink .
##     Smooth Facet Body Builder is a function to facilitate the removal of noise from facet bodies while keeping the general shape in tact.  <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateSmoothFacetBodyBuilder  NXOpen::Facet::FacetedBodyCollection::CreateSmoothFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## IsEditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsLockBoundary </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsSmoothOverEdges </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## NumberOfIterations </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## SmoothFactor </term> <description> 
##  
## 10 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class SmoothFacetBodyBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Facet.SmoothFacetBodyBuilder</ja_class>.
    Smooth Facet Body Builder is a function to facilitate the removal of noise from facet bodies while keeping the general shape in tact. """


    ##  Smooth Options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Mesh</term><description> 
    ## </description> </item><item><term> 
    ## Edge</term><description> 
    ## </description> </item></list>
    class Types(Enum):
        """
        Members Include: <Mesh> <Edge>
        """
        Mesh: int
        Edge: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmoothFacetBodyBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Bodies
    ##  Returns the facet bodies to be smoothed.  
    ##    Inputs to this command can be convergent objects.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::Facet::SmoothFacetBodyBuilder::FacetCollector NXOpen::Facet::SmoothFacetBodyBuilder::FacetCollector@endlink  instead.  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Bodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Bodies
         Returns the facet bodies to be smoothed.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) FaceEdge
    ##  Returns the option indicating if a copy of the facet body will be smoothed without altering the original   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def FaceEdge(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) FaceEdge
         Returns the option indicating if a copy of the facet body will be smoothed without altering the original   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) FacetBodies
    ##  Returns the facet bodies to be smoothed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Facet::SmoothFacetBodyBuilder::Bodies NXOpen::Facet::SmoothFacetBodyBuilder::Bodies@endlink  instead.  <br> 

    ## @return SelectFacetedBodyList
    @property
    def FacetBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) FacetBodies
         Returns the facet bodies to be smoothed   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
    ##  Returns a collector of facets on the facet bodies to be to be smoothed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns a collector of facets on the facet bodies to be to be smoothed.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector

    ##  Returns a collector of facets on the facet bodies to be to be smoothed.  
    ##      
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FacetCollector.setter
    def FacetCollector(self, collector: NXOpen.FacetCollector):
        """
        Setter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns a collector of facets on the facet bodies to be to be smoothed.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsEditCopy
    ##  Returns the option indicating if a copy of the facet body will be smoothed without altering the original   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the option indicating if a copy of the facet body will be smoothed without altering the original   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsEditCopy

    ##  Returns the option indicating if a copy of the facet body will be smoothed without altering the original   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the option indicating if a copy of the facet body will be smoothed without altering the original   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsLockBoundary
    ##  Returns the option indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def IsLockBoundary(self) -> bool:
        """
        Getter for property: (bool) IsLockBoundary
         Returns the option indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsLockBoundary

    ##  Returns the option indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @IsLockBoundary.setter
    def IsLockBoundary(self, isLockBoundary: bool):
        """
        Setter for property: (bool) IsLockBoundary
         Returns the option indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsSmoothOverEdges
    ##  Returns an option to apply the smooth operator across face edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return bool
    @property
    def IsSmoothOverEdges(self) -> bool:
        """
        Getter for property: (bool) IsSmoothOverEdges
         Returns an option to apply the smooth operator across face edges   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsSmoothOverEdges

    ##  Returns an option to apply the smooth operator across face edges   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @IsSmoothOverEdges.setter
    def IsSmoothOverEdges(self, isSmoothOverEdges: bool):
        """
        Setter for property: (bool) IsSmoothOverEdges
         Returns an option to apply the smooth operator across face edges   
            
         
        """
        pass
    
    ## Getter for property: (int) ModifyPercent
    ##  Returns the modification percentage   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.2.  This attribute is not very effective, hence this has been deprecated.  <br> 

    ## @return int
    @property
    def ModifyPercent(self) -> int:
        """
        Getter for property: (int) ModifyPercent
         Returns the modification percentage   
            
         
        """
        pass
    
    ## Setter for property: (int) ModifyPercent

    ##  Returns the modification percentage   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.2.  This attribute is not very effective, hence this has been deprecated.  <br> 

    @ModifyPercent.setter
    def ModifyPercent(self, modifyPercent: int):
        """
        Setter for property: (int) ModifyPercent
         Returns the modification percentage   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfIterations
    ##  Returns the number of iterations   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return int
    @property
    def NumberOfIterations(self) -> int:
        """
        Getter for property: (int) NumberOfIterations
         Returns the number of iterations   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfIterations

    ##  Returns the number of iterations   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @NumberOfIterations.setter
    def NumberOfIterations(self, numberOfIterations: int):
        """
        Setter for property: (int) NumberOfIterations
         Returns the number of iterations   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList@endlink) RegionList
    ##  Returns an optional list of regions on the facet bodies to be smoothed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::Facet::SmoothFacetBodyBuilder::FacetCollector NXOpen::Facet::SmoothFacetBodyBuilder::FacetCollector@endlink  instead.  <br> 

    ## @return NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList
    @property
    def RegionList(self) -> NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList@endlink) RegionList
         Returns an optional list of regions on the facet bodies to be smoothed   
            
         
        """
        pass
    
    ## Getter for property: (int) SmoothFactor
    ##  Returns the smoothing factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return int
    @property
    def SmoothFactor(self) -> int:
        """
        Getter for property: (int) SmoothFactor
         Returns the smoothing factor   
            
         
        """
        pass
    
    ## Setter for property: (int) SmoothFactor

    ##  Returns the smoothing factor   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @SmoothFactor.setter
    def SmoothFactor(self, smoothFactor: int):
        """
        Setter for property: (int) SmoothFactor
         Returns the smoothing factor   
            
         
        """
        pass
    
    ## Getter for property: (@link SmoothFacetBodyBuilder.Types NXOpen.Facet.SmoothFacetBodyBuilder.Types@endlink) Type
    ##  Returns the type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return SmoothFacetBodyBuilder.Types
    @property
    def Type(self) -> SmoothFacetBodyBuilder.Types:
        """
        Getter for property: (@link SmoothFacetBodyBuilder.Types NXOpen.Facet.SmoothFacetBodyBuilder.Types@endlink) Type
         Returns the type   
            
         
        """
        pass
    
    ## Setter for property: (@link SmoothFacetBodyBuilder.Types NXOpen.Facet.SmoothFacetBodyBuilder.Types@endlink) Type

    ##  Returns the type   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @Type.setter
    def Type(self, type: SmoothFacetBodyBuilder.Types):
        """
        Setter for property: (@link SmoothFacetBodyBuilder.Types NXOpen.Facet.SmoothFacetBodyBuilder.Types@endlink) Type
         Returns the type   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a SnipFacetBody builder  <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateSnipFacetBodyBuilder  NXOpen::Facet::FacetedBodyCollection::CreateSnipFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AlongDirection </term> <description> 
##  
## ViewDirection </description> </item> 
## 
## <item><term> 
##  
## BoundaryFacetTreatmentType </term> <description> 
##  
## SnipFacets </description> </item> 
## 
## <item><term> 
##  
## CanDivide </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsEditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsSnipNearFacets </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ProjectBothSides </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RegionsOption </term> <description> 
##  
## RemoveSelected </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class SnipFacetBodyBuilder(NXOpen.Builder): 
    """ Represents a SnipFacetBody builder """


    ##  Smoothness and boundary continuity options for automatic fill 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None (do not fill) </description> </item><item><term> 
    ## Linear</term><description> 
    ##  Linear (triangulated) fill. </description> </item><item><term> 
    ## Refined</term><description> 
    ##  Smooth internal fill. </description> </item><item><term> 
    ## TangentBased</term><description> 
    ##  Smooth fill, boundary is based on facet body tangent. </description> </item><item><term> 
    ## CurvatureBased</term><description> 
    ##  Smooth fill, boundary is based on facet body curvature. </description> </item></list>
    class AutomaticFillTypes(Enum):
        """
        Members Include: <NotSet> <Linear> <Refined> <TangentBased> <CurvatureBased>
        """
        NotSet: int
        Linear: int
        Refined: int
        TangentBased: int
        CurvatureBased: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SnipFacetBodyBuilder.AutomaticFillTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Boundary facet treatment type: 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SnipFacets</term><description> 
    ##  Snip scarred facets by the border </description> </item><item><term> 
    ## RemoveFacets</term><description> 
    ##  Remove scarred facets </description> </item></list>
    class BoundaryFacetTreatmentMethod(Enum):
        """
        Members Include: <SnipFacets> <RemoveFacets>
        """
        SnipFacets: int
        RemoveFacets: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Snipping direction when snipping type "by profiles"  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ViewDirection</term><description> 
    ##  Snip along view direction </description> </item><item><term> 
    ## FacetNormal</term><description> 
    ##  Snip along facet normal </description> </item><item><term> 
    ## AlongVector</term><description> 
    ##  Snip along specified vector </description> </item></list>
    class DirectionType(Enum):
        """
        Members Include: <ViewDirection> <FacetNormal> <AlongVector>
        """
        ViewDirection: int
        FacetNormal: int
        AlongVector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SnipFacetBodyBuilder.DirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  These options represent if selected portions will be: Remove Selected, Keep Selected, Divide  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## RemoveSelected</term><description> 
    ##  Remove Selected </description> </item><item><term> 
    ## KeepSelected</term><description> 
    ##  Keep Selected </description> </item><item><term> 
    ## Divide</term><description> 
    ##  Divide </description> </item></list>
    class RegionsOptionType(Enum):
        """
        Members Include: <RemoveSelected> <KeepSelected> <Divide>
        """
        RemoveSelected: int
        KeepSelected: int
        Divide: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SnipFacetBodyBuilder.RegionsOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Snip method 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SnipByBoundary</term><description> 
    ##  Snip by boundary </description> </item><item><term> 
    ## SnipByRegion</term><description> 
    ##  Snip by region </description> </item><item><term> 
    ## SnipWithCurves</term><description> 
    ##  Snip with curves </description> </item><item><term> 
    ## SnipAtPlane</term><description> 
    ##  Snip at plane </description> </item></list>
    class Types(Enum):
        """
        Members Include: <SnipByBoundary> <SnipByRegion> <SnipWithCurves> <SnipAtPlane>
        """
        SnipByBoundary: int
        SnipByRegion: int
        SnipWithCurves: int
        SnipAtPlane: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SnipFacetBodyBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SnipFacetBodyBuilder.DirectionType NXOpen.Facet.SnipFacetBodyBuilder.DirectionType@endlink) AlongDirection
    ##  Returns the direction in which snipping profiles are projected on the facet bodies    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return SnipFacetBodyBuilder.DirectionType
    @property
    def AlongDirection(self) -> SnipFacetBodyBuilder.DirectionType:
        """
        Getter for property: (@link SnipFacetBodyBuilder.DirectionType NXOpen.Facet.SnipFacetBodyBuilder.DirectionType@endlink) AlongDirection
         Returns the direction in which snipping profiles are projected on the facet bodies    
            
         
        """
        pass
    
    ## Setter for property: (@link SnipFacetBodyBuilder.DirectionType NXOpen.Facet.SnipFacetBodyBuilder.DirectionType@endlink) AlongDirection

    ##  Returns the direction in which snipping profiles are projected on the facet bodies    
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @AlongDirection.setter
    def AlongDirection(self, alongDirection: SnipFacetBodyBuilder.DirectionType):
        """
        Setter for property: (@link SnipFacetBodyBuilder.DirectionType NXOpen.Facet.SnipFacetBodyBuilder.DirectionType@endlink) AlongDirection
         Returns the direction in which snipping profiles are projected on the facet bodies    
            
         
        """
        pass
    
    ## Getter for property: (@link SnipFacetBodyBuilder.AutomaticFillTypes NXOpen.Facet.SnipFacetBodyBuilder.AutomaticFillTypes@endlink) AutomaticFillType
    ##  Returns the boundary smoothness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SnipFacetBodyBuilder.AutomaticFillTypes
    @property
    def AutomaticFillType(self) -> SnipFacetBodyBuilder.AutomaticFillTypes:
        """
        Getter for property: (@link SnipFacetBodyBuilder.AutomaticFillTypes NXOpen.Facet.SnipFacetBodyBuilder.AutomaticFillTypes@endlink) AutomaticFillType
         Returns the boundary smoothness   
            
         
        """
        pass
    
    ## Setter for property: (@link SnipFacetBodyBuilder.AutomaticFillTypes NXOpen.Facet.SnipFacetBodyBuilder.AutomaticFillTypes@endlink) AutomaticFillType

    ##  Returns the boundary smoothness   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AutomaticFillType.setter
    def AutomaticFillType(self, smooth_type: SnipFacetBodyBuilder.AutomaticFillTypes):
        """
        Setter for property: (@link SnipFacetBodyBuilder.AutomaticFillTypes NXOpen.Facet.SnipFacetBodyBuilder.AutomaticFillTypes@endlink) AutomaticFillType
         Returns the boundary smoothness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Bodies
    ##  Returns the facet bodies to snip.  
    ##    Inputs to this command can be convergent objects.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Bodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Bodies
         Returns the facet bodies to snip.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    
    ## Getter for property: (@link SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod NXOpen.Facet.SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod@endlink) BoundaryFacetTreatmentType
    ##  Returns the boundary facet treatment type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod
    @property
    def BoundaryFacetTreatmentType(self) -> SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod:
        """
        Getter for property: (@link SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod NXOpen.Facet.SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod@endlink) BoundaryFacetTreatmentType
         Returns the boundary facet treatment type   
            
         
        """
        pass
    
    ## Setter for property: (@link SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod NXOpen.Facet.SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod@endlink) BoundaryFacetTreatmentType

    ##  Returns the boundary facet treatment type   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @BoundaryFacetTreatmentType.setter
    def BoundaryFacetTreatmentType(self, boundaryFacetTreatmentType: SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod):
        """
        Setter for property: (@link SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod NXOpen.Facet.SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod@endlink) BoundaryFacetTreatmentType
         Returns the boundary facet treatment type   
            
         
        """
        pass
    
    ## Getter for property: (bool) CanDivide
    ##  Returns the value indicating if facet body is to be divided   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def CanDivide(self) -> bool:
        """
        Getter for property: (bool) CanDivide
         Returns the value indicating if facet body is to be divided   
            
         
        """
        pass
    
    ## Setter for property: (bool) CanDivide

    ##  Returns the value indicating if facet body is to be divided   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @CanDivide.setter
    def CanDivide(self, canDivide: bool):
        """
        Setter for property: (bool) CanDivide
         Returns the value indicating if facet body is to be divided   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) FacetBodies
    ##  Returns the facet bodies to snip   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Facet::SnipFacetBodyBuilder::Bodies NXOpen::Facet::SnipFacetBodyBuilder::Bodies@endlink  instead.  <br> 

    ## @return SelectFacetedBodyList
    @property
    def FacetBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) FacetBodies
         Returns the facet bodies to snip   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
    ##  Returns the collector of facets to be snipped.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns the collector of facets to be snipped.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector

    ##  Returns the collector of facets to be snipped.  
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FacetCollector.setter
    def FacetCollector(self, collector: NXOpen.FacetCollector):
        """
        Setter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns the collector of facets to be snipped.  
            
         
        """
        pass
    
    ## Getter for property: (bool) IsEditCopy
    ##  Returns the value indicating if a copy of the facet body to be snipped without altering the original   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be snipped without altering the original   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsEditCopy

    ##  Returns the value indicating if a copy of the facet body to be snipped without altering the original   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be snipped without altering the original   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsSnipNearFacets
    ##  Returns the value indicating if only facets near to the viewer to be snipped   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def IsSnipNearFacets(self) -> bool:
        """
        Getter for property: (bool) IsSnipNearFacets
         Returns the value indicating if only facets near to the viewer to be snipped   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsSnipNearFacets

    ##  Returns the value indicating if only facets near to the viewer to be snipped   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @IsSnipNearFacets.setter
    def IsSnipNearFacets(self, isSnipNearFacets: bool):
        """
        Setter for property: (bool) IsSnipNearFacets
         Returns the value indicating if only facets near to the viewer to be snipped   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
    ##  Returns the snipping plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Plane
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the snipping plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane

    ##  Returns the snipping plane   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the snipping plane   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SectionList NXOpen.SectionList@endlink) ProfileList
    ##  Returns the list of snipping profiles   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.SectionList
    @property
    def ProfileList(self) -> NXOpen.SectionList:
        """
        Getter for property: (@link NXOpen.SectionList NXOpen.SectionList@endlink) ProfileList
         Returns the list of snipping profiles   
            
         
        """
        pass
    
    ## Getter for property: (bool) ProjectBothSides
    ##  Returns the value indicating if project both sides in snip with curves along specified vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ProjectBothSides(self) -> bool:
        """
        Getter for property: (bool) ProjectBothSides
         Returns the value indicating if project both sides in snip with curves along specified vector.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ProjectBothSides

    ##  Returns the value indicating if project both sides in snip with curves along specified vector.  
    ##      
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ProjectBothSides.setter
    def ProjectBothSides(self, projectBothSides: bool):
        """
        Setter for property: (bool) ProjectBothSides
         Returns the value indicating if project both sides in snip with curves along specified vector.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionVector
    ##  Returns the projection vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ProjectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionVector
         Returns the projection vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionVector

    ##  Returns the projection vector   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ProjectionVector.setter
    def ProjectionVector(self, projectionVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionVector
         Returns the projection vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList@endlink) RegionList
    ##  Returns the list of regions to snip   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList
    @property
    def RegionList(self) -> NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList@endlink) RegionList
         Returns the list of regions to snip   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) RegionPoint
    ##  Returns the point indicating the portion of the facet body with respect to specified region to be snipped.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.SelectPointList
    @property
    def RegionPoint(self) -> NXOpen.SelectPointList:
        """
        Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) RegionPoint
         Returns the point indicating the portion of the facet body with respect to specified region to be snipped.  
             
         
        """
        pass
    
    ## Getter for property: (@link SnipFacetBodyBuilder.RegionsOptionType NXOpen.Facet.SnipFacetBodyBuilder.RegionsOptionType@endlink) RegionsOption
    ##  Returns the regions option of enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return SnipFacetBodyBuilder.RegionsOptionType
    @property
    def RegionsOption(self) -> SnipFacetBodyBuilder.RegionsOptionType:
        """
        Getter for property: (@link SnipFacetBodyBuilder.RegionsOptionType NXOpen.Facet.SnipFacetBodyBuilder.RegionsOptionType@endlink) RegionsOption
         Returns the regions option of enum   
            
         
        """
        pass
    
    ## Setter for property: (@link SnipFacetBodyBuilder.RegionsOptionType NXOpen.Facet.SnipFacetBodyBuilder.RegionsOptionType@endlink) RegionsOption

    ##  Returns the regions option of enum   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @RegionsOption.setter
    def RegionsOption(self, regionsOption: SnipFacetBodyBuilder.RegionsOptionType):
        """
        Setter for property: (@link SnipFacetBodyBuilder.RegionsOptionType NXOpen.Facet.SnipFacetBodyBuilder.RegionsOptionType@endlink) RegionsOption
         Returns the regions option of enum   
            
         
        """
        pass
    
    ## Getter for property: (@link SnipFacetBodyBuilder.Types NXOpen.Facet.SnipFacetBodyBuilder.Types@endlink) Type
    ##  Returns the snipping method accessor  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return SnipFacetBodyBuilder.Types
    @property
    def Type(self) -> SnipFacetBodyBuilder.Types:
        """
        Getter for property: (@link SnipFacetBodyBuilder.Types NXOpen.Facet.SnipFacetBodyBuilder.Types@endlink) Type
         Returns the snipping method accessor  
            
         
        """
        pass
    
    ## Setter for property: (@link SnipFacetBodyBuilder.Types NXOpen.Facet.SnipFacetBodyBuilder.Types@endlink) Type

    ##  Returns the snipping method accessor  
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Type.setter
    def Type(self, type: SnipFacetBodyBuilder.Types):
        """
        Setter for property: (@link SnipFacetBodyBuilder.Types NXOpen.Facet.SnipFacetBodyBuilder.Types@endlink) Type
         Returns the snipping method accessor  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ViewDirection
    ##  Returns the view direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def ViewDirection(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ViewDirection
         Returns the view direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ViewDirection

    ##  Returns the view direction   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ViewDirection.setter
    def ViewDirection(self, viewDirection: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ViewDirection
         Returns the view direction   
            
         
        """
        pass
    
    ##  Switch the region to be snipped indicated by the region point. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def SwitchRegion(self) -> None:
        """
         Switch the region to be snipped indicated by the region point. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Facet::SplitCurveMethodBuilder NXOpen::Facet::SplitCurveMethodBuilder@endlink .
##    Split Curve Method Builder is a class to provide a curve to divide the facet faces.  <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateSplitCurveMethodBuilder  NXOpen::Facet::FacetModelingCollection::CreateSplitCurveMethodBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class SplitCurveMethodBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Facet.SplitCurveMethodBuilder</ja_class>.
   Split Curve Method Builder is a class to provide a curve to divide the facet faces. """


    ##  the project option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NormalToFace</term><description> 
    ##  project normal to face </description> </item><item><term> 
    ## AlongVector</term><description> 
    ##  project along vector </description> </item></list>
    class ProjectOption(Enum):
        """
        Members Include: <NormalToFace> <AlongVector>
        """
        NormalToFace: int
        AlongVector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SplitCurveMethodBuilder.ProjectOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) ExistingCurves
    ##  Returns the existing curves to be used to divide facet body  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Section
    @property
    def ExistingCurves(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) ExistingCurves
         Returns the existing curves to be used to divide facet body  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectDirection
    ##  Returns the projection direction   
    ##     
    ##  
    ## Getter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.GeometricUtilities.ProjectionOptions
    @property
    def ProjectDirection(self) -> NXOpen.GeometricUtilities.ProjectionOptions:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectDirection
         Returns the projection direction   
            
         
        """
        pass
    
    ##  Set the list of curves on bodies 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ## <param name="bodyArray"> (@link NXOpen.Body List[NXOpen.Body]@endlink) </param>
    def AddCurveOnBodies(self, bodyArray: List[NXOpen.Body]) -> None:
        """
         Set the list of curves on bodies 
        """
        pass
    
    ##  Create split curve with use existing method
    ##  @return curves (@link NXOpen.Spline List[NXOpen.Spline]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def CreateSplitCurveWithUseExisting(self) -> List[NXOpen.Spline]:
        """
         Create split curve with use existing method
         @return curves (@link NXOpen.Spline List[NXOpen.Spline]@endlink): .
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Facet::SplitCurveMethodListDataManager NXOpen::Facet::SplitCurveMethodListDataManager@endlink .
##     Split Curve Method List Data Manager is a class to provide list of split curve methods used in facet body.  <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateSplitCurveMethodListDataManager  NXOpen::Facet::FacetModelingCollection::CreateSplitCurveMethodListDataManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class SplitCurveMethodListDataManager(NXOpen.TaggedObject): 
    """ Represents a <ja_class>NXOpen.Facet.SplitCurveMethodListDataManager</ja_class>.
    Split Curve Method List Data Manager is a class to provide list of split curve methods used in facet body. """


    ## Getter for property: (@link NXOpen.TaggedObjectList NXOpen.TaggedObjectList@endlink) SplitCurveMethodList
    ##  Returns the split curve list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.TaggedObjectList
    @property
    def SplitCurveMethodList(self) -> NXOpen.TaggedObjectList:
        """
        Getter for property: (@link NXOpen.TaggedObjectList NXOpen.TaggedObjectList@endlink) SplitCurveMethodList
         Returns the split curve list   
            
         
        """
        pass
    
import NXOpen
##  The STL file import builder. Inputs to this class can be convergent objects. <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateSTLImportBuilder  NXOpen::Facet::FacetedBodyCollection::CreateSTLImportBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AngularTolerance </term> <description> 
##  
## Medium </description> </item> 
## 
## <item><term> 
##  
## FacetBodyType </term> <description> 
##  
## Psm </description> </item> 
## 
## <item><term> 
##  
## HideSmoothEdges </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## MinimumAngleFoldedFacets </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## MinimumFacetNumber </term> <description> 
##  
## 100 </description> </item> 
## 
## <item><term> 
##  
## STLFileUnits </term> <description> 
##  
## Millimeters </description> </item> 
## 
## <item><term> 
##  
## ShowInformationWindow </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX6.0.0  <br> 

class STLImportBuilder(NXOpen.Builder): 
    """ The STL file import builder. Inputs to this class can be convergent objects."""


    ##  The angular tolerance types
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Coarse</term><description> 
    ##  </description> </item><item><term> 
    ## Medium</term><description> 
    ##  </description> </item><item><term> 
    ## Fine</term><description> 
    ##  </description> </item></list>
    class AngularToleranceTypes(Enum):
        """
        Members Include: <Coarse> <Medium> <Fine>
        """
        Coarse: int
        Medium: int
        Fine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> STLImportBuilder.AngularToleranceTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  These represent the type of body that will get created on importing the STL file 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Psm</term><description> 
    ##  Import to Facet Brep format</description> </item><item><term> 
    ## Nx</term><description> 
    ##  Import To NX Facet Format </description> </item><item><term> 
    ## Jt</term><description> 
    ##  Import to JT format</description> </item></list>
    class FacetBodyTypes(Enum):
        """
        Members Include: <Psm> <Nx> <Jt>
        """
        Psm: int
        Nx: int
        Jt: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> STLImportBuilder.FacetBodyTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The STL file units types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Meters</term><description> 
    ##  </description> </item><item><term> 
    ## Millimeters</term><description> 
    ##  </description> </item><item><term> 
    ## Inches</term><description> 
    ##  </description> </item></list>
    class STLFileUnitsTypes(Enum):
        """
        Members Include: <Meters> <Millimeters> <Inches>
        """
        Meters: int
        Millimeters: int
        Inches: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> STLImportBuilder.STLFileUnitsTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link STLImportBuilder.AngularToleranceTypes NXOpen.Facet.STLImportBuilder.AngularToleranceTypes@endlink) AngularTolerance
    ##  Returns the angular tolerance   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return STLImportBuilder.AngularToleranceTypes
    @property
    def AngularTolerance(self) -> STLImportBuilder.AngularToleranceTypes:
        """
        Getter for property: (@link STLImportBuilder.AngularToleranceTypes NXOpen.Facet.STLImportBuilder.AngularToleranceTypes@endlink) AngularTolerance
         Returns the angular tolerance   
            
         
        """
        pass
    
    ## Setter for property: (@link STLImportBuilder.AngularToleranceTypes NXOpen.Facet.STLImportBuilder.AngularToleranceTypes@endlink) AngularTolerance

    ##  Returns the angular tolerance   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @AngularTolerance.setter
    def AngularTolerance(self, angularTolerance: STLImportBuilder.AngularToleranceTypes):
        """
        Setter for property: (@link STLImportBuilder.AngularToleranceTypes NXOpen.Facet.STLImportBuilder.AngularToleranceTypes@endlink) AngularTolerance
         Returns the angular tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) CleanUp
    ##  Returns the option to clean up all mesh defects on import   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def CleanUp(self) -> bool:
        """
        Getter for property: (bool) CleanUp
         Returns the option to clean up all mesh defects on import   
            
         
        """
        pass
    
    ## Setter for property: (bool) CleanUp

    ##  Returns the option to clean up all mesh defects on import   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @CleanUp.setter
    def CleanUp(self, cleanUp: bool):
        """
        Setter for property: (bool) CleanUp
         Returns the option to clean up all mesh defects on import   
            
         
        """
        pass
    
    ## Getter for property: (@link STLImportBuilder.FacetBodyTypes NXOpen.Facet.STLImportBuilder.FacetBodyTypes@endlink) FacetBodyType
    ##  Returns the facet body type   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return STLImportBuilder.FacetBodyTypes
    @property
    def FacetBodyType(self) -> STLImportBuilder.FacetBodyTypes:
        """
        Getter for property: (@link STLImportBuilder.FacetBodyTypes NXOpen.Facet.STLImportBuilder.FacetBodyTypes@endlink) FacetBodyType
         Returns the facet body type   
            
         
        """
        pass
    
    ## Setter for property: (@link STLImportBuilder.FacetBodyTypes NXOpen.Facet.STLImportBuilder.FacetBodyTypes@endlink) FacetBodyType

    ##  Returns the facet body type   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @FacetBodyType.setter
    def FacetBodyType(self, facetBodyType: STLImportBuilder.FacetBodyTypes):
        """
        Setter for property: (@link STLImportBuilder.FacetBodyTypes NXOpen.Facet.STLImportBuilder.FacetBodyTypes@endlink) FacetBodyType
         Returns the facet body type   
            
         
        """
        pass
    
    ## Getter for property: (str) File
    ##  Returns the STL file    
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return str
    @property
    def File(self) -> str:
        """
        Getter for property: (str) File
         Returns the STL file    
            
         
        """
        pass
    
    ## Setter for property: (str) File

    ##  Returns the STL file    
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING") OR nx_freeform_1 ("basic freeform modeling") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @File.setter
    def File(self, filename: str):
        """
        Setter for property: (str) File
         Returns the STL file    
            
         
        """
        pass
    
    ## Getter for property: (bool) HideSmoothEdges
    ##  Returns the indicator for whether to hide smooth edges   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def HideSmoothEdges(self) -> bool:
        """
        Getter for property: (bool) HideSmoothEdges
         Returns the indicator for whether to hide smooth edges   
            
         
        """
        pass
    
    ## Setter for property: (bool) HideSmoothEdges

    ##  Returns the indicator for whether to hide smooth edges   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @HideSmoothEdges.setter
    def HideSmoothEdges(self, hideSmoothEdges: bool):
        """
        Setter for property: (bool) HideSmoothEdges
         Returns the indicator for whether to hide smooth edges   
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumAngleFoldedFacets
    ##  Returns the value for minimum angle between adjacent facets to define folded facets.  
    ##      
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def MinimumAngleFoldedFacets(self) -> float:
        """
        Getter for property: (float) MinimumAngleFoldedFacets
         Returns the value for minimum angle between adjacent facets to define folded facets.  
             
         
        """
        pass
    
    ## Setter for property: (float) MinimumAngleFoldedFacets

    ##  Returns the value for minimum angle between adjacent facets to define folded facets.  
    ##      
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MinimumAngleFoldedFacets.setter
    def MinimumAngleFoldedFacets(self, minimumAngleFoldedFacets: float):
        """
        Setter for property: (float) MinimumAngleFoldedFacets
         Returns the value for minimum angle between adjacent facets to define folded facets.  
             
         
        """
        pass
    
    ## Getter for property: (int) MinimumFacetNumber
    ##  Returns the value for minimum number of facets for a STL file to be imported   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def MinimumFacetNumber(self) -> int:
        """
        Getter for property: (int) MinimumFacetNumber
         Returns the value for minimum number of facets for a STL file to be imported   
            
         
        """
        pass
    
    ## Setter for property: (int) MinimumFacetNumber

    ##  Returns the value for minimum number of facets for a STL file to be imported   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MinimumFacetNumber.setter
    def MinimumFacetNumber(self, minimumFacetNumber: int):
        """
        Setter for property: (int) MinimumFacetNumber
         Returns the value for minimum number of facets for a STL file to be imported   
            
         
        """
        pass
    
    ## Getter for property: (@link STLImportBuilder.STLFileUnitsTypes NXOpen.Facet.STLImportBuilder.STLFileUnitsTypes@endlink) STLFileUnits
    ##  Returns the STL file units   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return STLImportBuilder.STLFileUnitsTypes
    @property
    def STLFileUnits(self) -> STLImportBuilder.STLFileUnitsTypes:
        """
        Getter for property: (@link STLImportBuilder.STLFileUnitsTypes NXOpen.Facet.STLImportBuilder.STLFileUnitsTypes@endlink) STLFileUnits
         Returns the STL file units   
            
         
        """
        pass
    
    ## Setter for property: (@link STLImportBuilder.STLFileUnitsTypes NXOpen.Facet.STLImportBuilder.STLFileUnitsTypes@endlink) STLFileUnits

    ##  Returns the STL file units   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @STLFileUnits.setter
    def STLFileUnits(self, stlFileUnits: STLImportBuilder.STLFileUnitsTypes):
        """
        Setter for property: (@link STLImportBuilder.STLFileUnitsTypes NXOpen.Facet.STLImportBuilder.STLFileUnitsTypes@endlink) STLFileUnits
         Returns the STL file units   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowInformationWindow
    ##  Returns the indicator for whether to show information window   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def ShowInformationWindow(self) -> bool:
        """
        Getter for property: (bool) ShowInformationWindow
         Returns the indicator for whether to show information window   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowInformationWindow

    ##  Returns the indicator for whether to show information window   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ShowInformationWindow.setter
    def ShowInformationWindow(self, showInformationWindow: bool):
        """
        Setter for property: (bool) ShowInformationWindow
         Returns the indicator for whether to show information window   
            
         
        """
        pass
    
    ##   The imported bodies after STL file import 
    ##  @return topology (@link NXOpen.Part List[NXOpen.Part]@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") OR nx_masterfem ("Finite Element Modeling")
    def GetTopology(self) -> List[NXOpen.Part]:
        """
          The imported bodies after STL file import 
         @return topology (@link NXOpen.Part List[NXOpen.Part]@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  This class provides functionality to subdivide the polygons to increase the density of the facet bodies.
##     Subdividing Polygons creates a smoother representation. <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateSubdivideFacetBodyBuilder  NXOpen::Facet::FacetedBodyCollection::CreateSubdivideFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AngleThreshold </term> <description> 
##  
## 30 </description> </item> 
## 
## <item><term> 
##  
## EdgeLength </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## InterpolationMethod </term> <description> 
##  
## Cubic </description> </item> 
## 
## <item><term> 
##  
## IsEditCopy </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsOptimize </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SubdivisionMethod </term> <description> 
##  
## SubdivideIntoFour </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class SubdivideFacetBodyBuilder(NXOpen.Builder): 
    """ This class provides functionality to subdivide the polygons to increase the density of the facet bodies.
    Subdividing Polygons creates a smoother representation."""


    ##  Subdivision interpolation methods 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  In the linear option the sub-triangles are coplanar to the original triangle. Shape resolution remains untouched. </description> </item><item><term> 
    ## Cubic</term><description> 
    ##  In the cubic option the sub-triangles are fitted cubic to the surrounding triangles. Shape resolution increases. </description> </item></list>
    class InterpolationMethodType(Enum):
        """
        Members Include: <Linear> <Cubic>
        """
        Linear: int
        Cubic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivideFacetBodyBuilder.InterpolationMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Subdivision methods 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SubdivideIntoFour</term><description> 
    ##  Subdivides the polygons into four sub triangles. The original mesh structure remains.</description> </item><item><term> 
    ## SubdividebyEdgeLength</term><description> 
    ##  Subdivides the polygons to a specified edge length. The original mesh structure disappears. </description> </item></list>
    class SubdivisionMethodType(Enum):
        """
        Members Include: <SubdivideIntoFour> <SubdividebyEdgeLength>
        """
        SubdivideIntoFour: int
        SubdividebyEdgeLength: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivideFacetBodyBuilder.SubdivisionMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) AngleThreshold
    ##  Returns the angular tolerance to detect sharp edges to be kept.  
    ##    Cubic interpolation can not interpolate over an edge of two triangles whose normals differ more than the specified value. Same applies to re-meshing.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def AngleThreshold(self) -> float:
        """
        Getter for property: (float) AngleThreshold
         Returns the angular tolerance to detect sharp edges to be kept.  
           Cubic interpolation can not interpolate over an edge of two triangles whose normals differ more than the specified value. Same applies to re-meshing.   
         
        """
        pass
    
    ## Setter for property: (float) AngleThreshold

    ##  Returns the angular tolerance to detect sharp edges to be kept.  
    ##    Cubic interpolation can not interpolate over an edge of two triangles whose normals differ more than the specified value. Same applies to re-meshing.   
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @AngleThreshold.setter
    def AngleThreshold(self, angleThreshold: float):
        """
        Setter for property: (float) AngleThreshold
         Returns the angular tolerance to detect sharp edges to be kept.  
           Cubic interpolation can not interpolate over an edge of two triangles whose normals differ more than the specified value. Same applies to re-meshing.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Bodies
    ##  Returns the facet bodies to be subdivided.  
    ##    Inputs to this command can be convergent objects.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::Facet::SubdivideFacetBodyBuilder::FacetCollector NXOpen::Facet::SubdivideFacetBodyBuilder::FacetCollector@endlink  instead.  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Bodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Bodies
         Returns the facet bodies to be subdivided.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    
    ## Getter for property: (float) EdgeLength
    ##  Returns the value indicating length of the edge of the polygons to be subdivided.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def EdgeLength(self) -> float:
        """
        Getter for property: (float) EdgeLength
         Returns the value indicating length of the edge of the polygons to be subdivided.  
            
         
        """
        pass
    
    ## Setter for property: (float) EdgeLength

    ##  Returns the value indicating length of the edge of the polygons to be subdivided.  
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @EdgeLength.setter
    def EdgeLength(self, edgeLength: float):
        """
        Setter for property: (float) EdgeLength
         Returns the value indicating length of the edge of the polygons to be subdivided.  
            
         
        """
        pass
    
    ## Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) FacetBodies
    ##  Returns the facet bodies to be subdivided  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Facet::SubdivideFacetBodyBuilder::Bodies NXOpen::Facet::SubdivideFacetBodyBuilder::Bodies@endlink  instead.  <br> 

    ## @return SelectFacetedBodyList
    @property
    def FacetBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: (@link SelectFacetedBodyList NXOpen.Facet.SelectFacetedBodyList@endlink) FacetBodies
         Returns the facet bodies to be subdivided  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
    ##  Returns a collector of facets on the facet bodies to be subdivided.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns a collector of facets on the facet bodies to be subdivided.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector

    ##  Returns a collector of facets on the facet bodies to be subdivided.  
    ##      
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FacetCollector.setter
    def FacetCollector(self, collector: NXOpen.FacetCollector):
        """
        Setter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns a collector of facets on the facet bodies to be subdivided.  
             
         
        """
        pass
    
    ## Getter for property: (@link SubdivideFacetBodyBuilder.InterpolationMethodType NXOpen.Facet.SubdivideFacetBodyBuilder.InterpolationMethodType@endlink) InterpolationMethod
    ##  Returns the interpolation method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return SubdivideFacetBodyBuilder.InterpolationMethodType
    @property
    def InterpolationMethod(self) -> SubdivideFacetBodyBuilder.InterpolationMethodType:
        """
        Getter for property: (@link SubdivideFacetBodyBuilder.InterpolationMethodType NXOpen.Facet.SubdivideFacetBodyBuilder.InterpolationMethodType@endlink) InterpolationMethod
         Returns the interpolation method   
            
         
        """
        pass
    
    ## Setter for property: (@link SubdivideFacetBodyBuilder.InterpolationMethodType NXOpen.Facet.SubdivideFacetBodyBuilder.InterpolationMethodType@endlink) InterpolationMethod

    ##  Returns the interpolation method   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @InterpolationMethod.setter
    def InterpolationMethod(self, interpolationMethod: SubdivideFacetBodyBuilder.InterpolationMethodType):
        """
        Setter for property: (@link SubdivideFacetBodyBuilder.InterpolationMethodType NXOpen.Facet.SubdivideFacetBodyBuilder.InterpolationMethodType@endlink) InterpolationMethod
         Returns the interpolation method   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsEditCopy
    ##  Returns the value indicating if a copy of the facet body to be subdivided without altering the original.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be subdivided without altering the original.  
             
         
        """
        pass
    
    ## Setter for property: (bool) IsEditCopy

    ##  Returns the value indicating if a copy of the facet body to be subdivided without altering the original.  
    ##      
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be subdivided without altering the original.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsOptimize
    ##  Returns the value indicating whether to perform a decimation step after the subdivision.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def IsOptimize(self) -> bool:
        """
        Getter for property: (bool) IsOptimize
         Returns the value indicating whether to perform a decimation step after the subdivision.  
            
         
        """
        pass
    
    ## Setter for property: (bool) IsOptimize

    ##  Returns the value indicating whether to perform a decimation step after the subdivision.  
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @IsOptimize.setter
    def IsOptimize(self, isOptimize: bool):
        """
        Setter for property: (bool) IsOptimize
         Returns the value indicating whether to perform a decimation step after the subdivision.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList@endlink) RegionList
    ##  Returns an optional list of regions on the facet bodies to be subdivided.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::Facet::SubdivideFacetBodyBuilder::FacetCollector NXOpen::Facet::SubdivideFacetBodyBuilder::FacetCollector@endlink  instead.  <br> 

    ## @return NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList
    @property
    def RegionList(self) -> NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList@endlink) RegionList
         Returns an optional list of regions on the facet bodies to be subdivided.  
             
         
        """
        pass
    
    ## Getter for property: (@link SubdivideFacetBodyBuilder.SubdivisionMethodType NXOpen.Facet.SubdivideFacetBodyBuilder.SubdivisionMethodType@endlink) SubdivisionMethod
    ##  Returns the subdivision method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return SubdivideFacetBodyBuilder.SubdivisionMethodType
    @property
    def SubdivisionMethod(self) -> SubdivideFacetBodyBuilder.SubdivisionMethodType:
        """
        Getter for property: (@link SubdivideFacetBodyBuilder.SubdivisionMethodType NXOpen.Facet.SubdivideFacetBodyBuilder.SubdivisionMethodType@endlink) SubdivisionMethod
         Returns the subdivision method   
            
         
        """
        pass
    
    ## Setter for property: (@link SubdivideFacetBodyBuilder.SubdivisionMethodType NXOpen.Facet.SubdivideFacetBodyBuilder.SubdivisionMethodType@endlink) SubdivisionMethod

    ##  Returns the subdivision method   
    ##     
    ##  
    ## Setter License requirements: studio_free_form ("STUDIO FREE FORM")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @SubdivisionMethod.setter
    def SubdivisionMethod(self, subdivisionMethod: SubdivideFacetBodyBuilder.SubdivisionMethodType):
        """
        Setter for property: (@link SubdivideFacetBodyBuilder.SubdivisionMethodType NXOpen.Facet.SubdivideFacetBodyBuilder.SubdivisionMethodType@endlink) SubdivisionMethod
         Returns the subdivision method   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Facet::WrapMeshBuilder NXOpen::Facet::WrapMeshBuilder@endlink .
##         This class wraps a facet body around one or more bodies. <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateWrapMeshBuilder  NXOpen::Facet::FacetModelingCollection::CreateWrapMeshBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AngleThreshold </term> <description> 
##  
## 50 </description> </item> 
## 
## <item><term> 
##  
## AverageSize.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ChordalTolerance </term> <description> 
##  
## 0.1 (millimeters part), 0.004 (inches part) </description> </item> 
## 
## <item><term> 
##  
## FacetsInGap </term> <description> 
##  
## 3 </description> </item> 
## 
## <item><term> 
##  
## InputBodyOption </term> <description> 
##  
## Hide </description> </item> 
## 
## <item><term> 
##  
## KeepSharpEdges </term> <description> 
##  
## True </description> </item> 
## 
## <item><term> 
##  
## MaxGapSize.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MaximumSize.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ProximityRefinement </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## SearchDistance.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class WrapMeshBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Facet.WrapMeshBuilder</ja_class>.
        This class wraps a facet body around one or more bodies."""


    ##  Input body visibility options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Keep</term><description> 
    ## </description> </item><item><term> 
    ## Hide</term><description> 
    ## </description> </item></list>
    class KeepInputBodyType(Enum):
        """
        Members Include: <Keep> <Hide>
        """
        Keep: int
        Hide: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> WrapMeshBuilder.KeepInputBodyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Methods based on wrapped volume. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## External</term><description> 
    ## </description> </item><item><term> 
    ## LargestInternal</term><description> 
    ## </description> </item><item><term> 
    ## InternalBySeedPoint</term><description> 
    ## </description> </item></list>
    class MethodType(Enum):
        """
        Members Include: <External> <LargestInternal> <InternalBySeedPoint>
        """
        External: int
        LargestInternal: int
        InternalBySeedPoint: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> WrapMeshBuilder.MethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Mesh wrapping modes. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Constant</term><description> 
    ## </description> </item><item><term> 
    ## Variable</term><description> 
    ## </description> </item></list>
    class WrapMeshModeType(Enum):
        """
        Members Include: <Constant> <Variable>
        """
        Constant: int
        Variable: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> WrapMeshBuilder.WrapMeshModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) AngleThreshold
    ##  Returns the angle threshold  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def AngleThreshold(self) -> float:
        """
        Getter for property: (float) AngleThreshold
         Returns the angle threshold  
            
         
        """
        pass
    
    ## Setter for property: (float) AngleThreshold

    ##  Returns the angle threshold  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AngleThreshold.setter
    def AngleThreshold(self, angleThreshold: float):
        """
        Setter for property: (float) AngleThreshold
         Returns the angle threshold  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AverageSize
    ##  Returns the average size for wrap mesh  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AverageSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AverageSize
         Returns the average size for wrap mesh  
            
         
        """
        pass
    
    ## Getter for property: (float) ChordalTolerance
    ##  Returns the chordal tolerance for wrap mesh  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def ChordalTolerance(self) -> float:
        """
        Getter for property: (float) ChordalTolerance
         Returns the chordal tolerance for wrap mesh  
            
         
        """
        pass
    
    ## Setter for property: (float) ChordalTolerance

    ##  Returns the chordal tolerance for wrap mesh  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ChordalTolerance.setter
    def ChordalTolerance(self, chordalTolerance: float):
        """
        Setter for property: (float) ChordalTolerance
         Returns the chordal tolerance for wrap mesh  
            
         
        """
        pass
    
    ## Getter for property: (int) FacetsInGap
    ##  Returns the facets in gap   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def FacetsInGap(self) -> int:
        """
        Getter for property: (int) FacetsInGap
         Returns the facets in gap   
            
         
        """
        pass
    
    ## Setter for property: (int) FacetsInGap

    ##  Returns the facets in gap   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @FacetsInGap.setter
    def FacetsInGap(self, facetsInGap: int):
        """
        Setter for property: (int) FacetsInGap
         Returns the facets in gap   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) GapFaces
    ##  Returns the select gap faces  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def GapFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) GapFaces
         Returns the select gap faces  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) InputBodyCollector
    ##  Returns the input body collector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def InputBodyCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) InputBodyCollector
         Returns the input body collector   
            
         
        """
        pass
    
    ## Getter for property: (@link WrapMeshBuilder.KeepInputBodyType NXOpen.Facet.WrapMeshBuilder.KeepInputBodyType@endlink) InputBodyOption
    ##  Returns the input body visibility option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return WrapMeshBuilder.KeepInputBodyType
    @property
    def InputBodyOption(self) -> WrapMeshBuilder.KeepInputBodyType:
        """
        Getter for property: (@link WrapMeshBuilder.KeepInputBodyType NXOpen.Facet.WrapMeshBuilder.KeepInputBodyType@endlink) InputBodyOption
         Returns the input body visibility option.  
             
         
        """
        pass
    
    ## Setter for property: (@link WrapMeshBuilder.KeepInputBodyType NXOpen.Facet.WrapMeshBuilder.KeepInputBodyType@endlink) InputBodyOption

    ##  Returns the input body visibility option.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @InputBodyOption.setter
    def InputBodyOption(self, inputBodyOption: WrapMeshBuilder.KeepInputBodyType):
        """
        Setter for property: (@link WrapMeshBuilder.KeepInputBodyType NXOpen.Facet.WrapMeshBuilder.KeepInputBodyType@endlink) InputBodyOption
         Returns the input body visibility option.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) IntendedGapSize
    ##  Returns the intended gap size  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def IntendedGapSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) IntendedGapSize
         Returns the intended gap size  
            
         
        """
        pass
    
    ## Getter for property: (bool) KeepSharpEdges
    ##  Returns the flag indicating if sharp edges should be kept.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def KeepSharpEdges(self) -> bool:
        """
        Getter for property: (bool) KeepSharpEdges
         Returns the flag indicating if sharp edges should be kept.  
             
         
        """
        pass
    
    ## Setter for property: (bool) KeepSharpEdges

    ##  Returns the flag indicating if sharp edges should be kept.  
    ##      
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @KeepSharpEdges.setter
    def KeepSharpEdges(self, keepSharpEdges: bool):
        """
        Setter for property: (bool) KeepSharpEdges
         Returns the flag indicating if sharp edges should be kept.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxGapSize
    ##  Returns the maximum gap size  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxGapSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxGapSize
         Returns the maximum gap size  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumSize
    ##  Returns the maximum size for wrap mesh  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumSize
         Returns the maximum size for wrap mesh  
            
         
        """
        pass
    
    ## Getter for property: (@link WrapMeshBuilder.MethodType NXOpen.Facet.WrapMeshBuilder.MethodType@endlink) Method
    ##  Returns the method for selected volume  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return WrapMeshBuilder.MethodType
    @property
    def Method(self) -> WrapMeshBuilder.MethodType:
        """
        Getter for property: (@link WrapMeshBuilder.MethodType NXOpen.Facet.WrapMeshBuilder.MethodType@endlink) Method
         Returns the method for selected volume  
            
         
        """
        pass
    
    ## Setter for property: (@link WrapMeshBuilder.MethodType NXOpen.Facet.WrapMeshBuilder.MethodType@endlink) Method

    ##  Returns the method for selected volume  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Method.setter
    def Method(self, method: WrapMeshBuilder.MethodType):
        """
        Setter for property: (@link WrapMeshBuilder.MethodType NXOpen.Facet.WrapMeshBuilder.MethodType@endlink) Method
         Returns the method for selected volume  
            
         
        """
        pass
    
    ## Getter for property: (bool) ProximityRefinement
    ##  Returns the proximity refinement   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ProximityRefinement(self) -> bool:
        """
        Getter for property: (bool) ProximityRefinement
         Returns the proximity refinement   
            
         
        """
        pass
    
    ## Setter for property: (bool) ProximityRefinement

    ##  Returns the proximity refinement   
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ProximityRefinement.setter
    def ProximityRefinement(self, proximityRefinement: bool):
        """
        Setter for property: (bool) ProximityRefinement
         Returns the proximity refinement   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchDistance
    ##  Returns the search distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SearchDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SearchDistance
         Returns the search distance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SeedPoint
    ##  Returns the seed point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SeedPoint(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SeedPoint
         Returns the seed point   
            
         
        """
        pass
    
    ## Getter for property: (@link WrapMeshBuilder.WrapMeshModeType NXOpen.Facet.WrapMeshBuilder.WrapMeshModeType@endlink) WrapMeshMode
    ##  Returns the mode for wrap mesh  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return WrapMeshBuilder.WrapMeshModeType
    @property
    def WrapMeshMode(self) -> WrapMeshBuilder.WrapMeshModeType:
        """
        Getter for property: (@link WrapMeshBuilder.WrapMeshModeType NXOpen.Facet.WrapMeshBuilder.WrapMeshModeType@endlink) WrapMeshMode
         Returns the mode for wrap mesh  
            
         
        """
        pass
    
    ## Setter for property: (@link WrapMeshBuilder.WrapMeshModeType NXOpen.Facet.WrapMeshBuilder.WrapMeshModeType@endlink) WrapMeshMode

    ##  Returns the mode for wrap mesh  
    ##     
    ##  
    ## Setter License requirements: nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @WrapMeshMode.setter
    def WrapMeshMode(self, wrapMeshMode: WrapMeshBuilder.WrapMeshModeType):
        """
        Setter for property: (@link WrapMeshBuilder.WrapMeshModeType NXOpen.Facet.WrapMeshBuilder.WrapMeshModeType@endlink) WrapMeshMode
         Returns the mode for wrap mesh  
            
         
        """
        pass
    
## @package NXOpen.Facet
## Classes, Enums and Structs under NXOpen.Facet namespace

##  @link BestFitAlignBuilderConstraintOptions NXOpen.Facet.BestFitAlignBuilderConstraintOptions @endlink is an alias for @link BestFitAlignBuilder.ConstraintOptions NXOpen.Facet.BestFitAlignBuilder.ConstraintOptions@endlink
BestFitAlignBuilderConstraintOptions = BestFitAlignBuilder.ConstraintOptions


##  @link BridgeFacetBodyBuilderInput NXOpen.Facet.BridgeFacetBodyBuilderInput @endlink is an alias for @link BridgeFacetBodyBuilder.Input NXOpen.Facet.BridgeFacetBodyBuilder.Input@endlink
BridgeFacetBodyBuilderInput = BridgeFacetBodyBuilder.Input


##  @link BridgeFacetBodyBuilderSmoothTypes NXOpen.Facet.BridgeFacetBodyBuilderSmoothTypes @endlink is an alias for @link BridgeFacetBodyBuilder.SmoothTypes NXOpen.Facet.BridgeFacetBodyBuilder.SmoothTypes@endlink
BridgeFacetBodyBuilderSmoothTypes = BridgeFacetBodyBuilder.SmoothTypes


##  @link CleanupFacetBodyBuilderCleanupOptions NXOpen.Facet.CleanupFacetBodyBuilderCleanupOptions @endlink is an alias for @link CleanupFacetBodyBuilder.CleanupOptions NXOpen.Facet.CleanupFacetBodyBuilder.CleanupOptions@endlink
CleanupFacetBodyBuilderCleanupOptions = CleanupFacetBodyBuilder.CleanupOptions


##  @link CleanupFacetBodyBuilderOriginalBodyOptions NXOpen.Facet.CleanupFacetBodyBuilderOriginalBodyOptions @endlink is an alias for @link CleanupFacetBodyBuilder.OriginalBodyOptions NXOpen.Facet.CleanupFacetBodyBuilder.OriginalBodyOptions@endlink
CleanupFacetBodyBuilderOriginalBodyOptions = CleanupFacetBodyBuilder.OriginalBodyOptions


##  @link CleanupFacetBodyWizardBuilderFillType NXOpen.Facet.CleanupFacetBodyWizardBuilderFillType @endlink is an alias for @link CleanupFacetBodyWizardBuilder.FillType NXOpen.Facet.CleanupFacetBodyWizardBuilder.FillType@endlink
CleanupFacetBodyWizardBuilderFillType = CleanupFacetBodyWizardBuilder.FillType


##  @link CleanupFacetBodyWizardBuilderJaCleanupFacetBodyBuilderRegionremoveoption NXOpen.Facet.CleanupFacetBodyWizardBuilderJaCleanupFacetBodyBuilderRegionremoveoption @endlink is an alias for @link CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption NXOpen.Facet.CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption@endlink
CleanupFacetBodyWizardBuilderJaCleanupFacetBodyBuilderRegionremoveoption = CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption


##  @link CombineFacetBodiesBuilderInputBodiesOption NXOpen.Facet.CombineFacetBodiesBuilderInputBodiesOption @endlink is an alias for @link CombineFacetBodiesBuilder.InputBodiesOption NXOpen.Facet.CombineFacetBodiesBuilder.InputBodiesOption@endlink
CombineFacetBodiesBuilderInputBodiesOption = CombineFacetBodiesBuilder.InputBodiesOption


##  @link ConvertFacetBodyBuilderOriginalBodyOptions NXOpen.Facet.ConvertFacetBodyBuilderOriginalBodyOptions @endlink is an alias for @link ConvertFacetBodyBuilder.OriginalBodyOptions NXOpen.Facet.ConvertFacetBodyBuilder.OriginalBodyOptions@endlink
ConvertFacetBodyBuilderOriginalBodyOptions = ConvertFacetBodyBuilder.OriginalBodyOptions


##  @link ConvertFacetBodyBuilderOutputTypes NXOpen.Facet.ConvertFacetBodyBuilderOutputTypes @endlink is an alias for @link ConvertFacetBodyBuilder.OutputTypes NXOpen.Facet.ConvertFacetBodyBuilder.OutputTypes@endlink
ConvertFacetBodyBuilderOutputTypes = ConvertFacetBodyBuilder.OutputTypes


##  @link CreateTransitionBuilderTypes NXOpen.Facet.CreateTransitionBuilderTypes @endlink is an alias for @link CreateTransitionBuilder.Types NXOpen.Facet.CreateTransitionBuilder.Types@endlink
CreateTransitionBuilderTypes = CreateTransitionBuilder.Types


##  @link DecimateFacetBodyBuilderDecimateMethodType NXOpen.Facet.DecimateFacetBodyBuilderDecimateMethodType @endlink is an alias for @link DecimateFacetBodyBuilder.DecimateMethodType NXOpen.Facet.DecimateFacetBodyBuilder.DecimateMethodType@endlink
DecimateFacetBodyBuilderDecimateMethodType = DecimateFacetBodyBuilder.DecimateMethodType


##  @link DivideFacetFaceBuilderDivideFacetTypes NXOpen.Facet.DivideFacetFaceBuilderDivideFacetTypes @endlink is an alias for @link DivideFacetFaceBuilder.DivideFacetTypes NXOpen.Facet.DivideFacetFaceBuilder.DivideFacetTypes@endlink
DivideFacetFaceBuilderDivideFacetTypes = DivideFacetFaceBuilder.DivideFacetTypes


##  @link ExtrudeFacetBodyBuilderLimitType NXOpen.Facet.ExtrudeFacetBodyBuilderLimitType @endlink is an alias for @link ExtrudeFacetBodyBuilder.LimitType NXOpen.Facet.ExtrudeFacetBodyBuilder.LimitType@endlink
ExtrudeFacetBodyBuilderLimitType = ExtrudeFacetBodyBuilder.LimitType


##  @link FacetBodyFromBodyBuilderOriginalBodyOptions NXOpen.Facet.FacetBodyFromBodyBuilderOriginalBodyOptions @endlink is an alias for @link FacetBodyFromBodyBuilder.OriginalBodyOptions NXOpen.Facet.FacetBodyFromBodyBuilder.OriginalBodyOptions@endlink
FacetBodyFromBodyBuilderOriginalBodyOptions = FacetBodyFromBodyBuilder.OriginalBodyOptions


##  @link FacetBodyFromBodyBuilderOutputTypes NXOpen.Facet.FacetBodyFromBodyBuilderOutputTypes @endlink is an alias for @link FacetBodyFromBodyBuilder.OutputTypes NXOpen.Facet.FacetBodyFromBodyBuilder.OutputTypes@endlink
FacetBodyFromBodyBuilderOutputTypes = FacetBodyFromBodyBuilder.OutputTypes


##  @link FacetedBodyCollectionType NXOpen.Facet.FacetedBodyCollectionType @endlink is an alias for @link FacetedBodyCollection.Type NXOpen.Facet.FacetedBodyCollection.Type@endlink
FacetedBodyCollectionType = FacetedBodyCollection.Type


##  @link FacetedBodyFacetedbodyType NXOpen.Facet.FacetedBodyFacetedbodyType @endlink is an alias for @link FacetedBody.FacetedbodyType NXOpen.Facet.FacetedBody.FacetedbodyType@endlink
FacetedBodyFacetedbodyType = FacetedBody.FacetedbodyType


##  @link FacetedEdgeFacetededgeType NXOpen.Facet.FacetedEdgeFacetededgeType @endlink is an alias for @link FacetedEdge.FacetededgeType NXOpen.Facet.FacetedEdge.FacetededgeType@endlink
FacetedEdgeFacetededgeType = FacetedEdge.FacetededgeType


##  @link FacetedFaceFacetedfaceType NXOpen.Facet.FacetedFaceFacetedfaceType @endlink is an alias for @link FacetedFace.FacetedfaceType NXOpen.Facet.FacetedFace.FacetedfaceType@endlink
FacetedFaceFacetedfaceType = FacetedFace.FacetedfaceType


##  @link FeatureExtractionBuilderInputActions NXOpen.Facet.FeatureExtractionBuilderInputActions @endlink is an alias for @link FeatureExtractionBuilder.InputActions NXOpen.Facet.FeatureExtractionBuilder.InputActions@endlink
FeatureExtractionBuilderInputActions = FeatureExtractionBuilder.InputActions


##  @link FillHoleBuilderSmoothTypes NXOpen.Facet.FillHoleBuilderSmoothTypes @endlink is an alias for @link FillHoleBuilder.SmoothTypes NXOpen.Facet.FillHoleBuilder.SmoothTypes@endlink
FillHoleBuilderSmoothTypes = FillHoleBuilder.SmoothTypes


##  @link FillHoleBuilderTargetTypes NXOpen.Facet.FillHoleBuilderTargetTypes @endlink is an alias for @link FillHoleBuilder.TargetTypes NXOpen.Facet.FillHoleBuilder.TargetTypes@endlink
FillHoleBuilderTargetTypes = FillHoleBuilder.TargetTypes


##  @link FillHoleBuilderTypes NXOpen.Facet.FillHoleBuilderTypes @endlink is an alias for @link FillHoleBuilder.Types NXOpen.Facet.FillHoleBuilder.Types@endlink
FillHoleBuilderTypes = FillHoleBuilder.Types


##  @link FillMeshBuilderEdgeOptionMenu NXOpen.Facet.FillMeshBuilderEdgeOptionMenu @endlink is an alias for @link FillMeshBuilder.EdgeOptionMenu NXOpen.Facet.FillMeshBuilder.EdgeOptionMenu@endlink
FillMeshBuilderEdgeOptionMenu = FillMeshBuilder.EdgeOptionMenu


## @link FillMeshBuilderFacetVertexData_Struct NXOpen.Facet.FillMeshBuilderFacetVertexData_Struct@endlink is an alias for @link FillMeshBuilder.FacetVertexData NXOpen.Facet.FillMeshBuilder.FacetVertexData@endlink.
FillMeshBuilderFacetVertexData_Struct = FillMeshBuilder.FacetVertexData


##  @link FillMeshBuilderSmoothnessOptionMenu NXOpen.Facet.FillMeshBuilderSmoothnessOptionMenu @endlink is an alias for @link FillMeshBuilder.SmoothnessOptionMenu NXOpen.Facet.FillMeshBuilder.SmoothnessOptionMenu@endlink
FillMeshBuilderSmoothnessOptionMenu = FillMeshBuilder.SmoothnessOptionMenu


##  @link FillMeshBuilderTypes NXOpen.Facet.FillMeshBuilderTypes @endlink is an alias for @link FillMeshBuilder.Types NXOpen.Facet.FillMeshBuilder.Types@endlink
FillMeshBuilderTypes = FillMeshBuilder.Types


##  @link LocalOffsetBuilderShapeMethodType NXOpen.Facet.LocalOffsetBuilderShapeMethodType @endlink is an alias for @link LocalOffsetBuilder.ShapeMethodType NXOpen.Facet.LocalOffsetBuilder.ShapeMethodType@endlink
LocalOffsetBuilderShapeMethodType = LocalOffsetBuilder.ShapeMethodType


##  @link LocalOffsetBuilderTransitionMethodType NXOpen.Facet.LocalOffsetBuilderTransitionMethodType @endlink is an alias for @link LocalOffsetBuilder.TransitionMethodType NXOpen.Facet.LocalOffsetBuilder.TransitionMethodType@endlink
LocalOffsetBuilderTransitionMethodType = LocalOffsetBuilder.TransitionMethodType


##  @link MergeFacetBodyBuilderInput NXOpen.Facet.MergeFacetBodyBuilderInput @endlink is an alias for @link MergeFacetBodyBuilder.Input NXOpen.Facet.MergeFacetBodyBuilder.Input@endlink
MergeFacetBodyBuilderInput = MergeFacetBodyBuilder.Input


##  @link MeshFromCloudBuilderModeOption NXOpen.Facet.MeshFromCloudBuilderModeOption @endlink is an alias for @link MeshFromCloudBuilder.ModeOption NXOpen.Facet.MeshFromCloudBuilder.ModeOption@endlink
MeshFromCloudBuilderModeOption = MeshFromCloudBuilder.ModeOption


##  @link MeshFromCloudBuilderSourceOption NXOpen.Facet.MeshFromCloudBuilderSourceOption @endlink is an alias for @link MeshFromCloudBuilder.SourceOption NXOpen.Facet.MeshFromCloudBuilder.SourceOption@endlink
MeshFromCloudBuilderSourceOption = MeshFromCloudBuilder.SourceOption


##  @link MultiPatchAlignmentBuilderResolutionType NXOpen.Facet.MultiPatchAlignmentBuilderResolutionType @endlink is an alias for @link MultiPatchAlignmentBuilder.ResolutionType NXOpen.Facet.MultiPatchAlignmentBuilder.ResolutionType@endlink
MultiPatchAlignmentBuilderResolutionType = MultiPatchAlignmentBuilder.ResolutionType


##  @link PolygonModelingBuilderConvertTypes NXOpen.Facet.PolygonModelingBuilderConvertTypes @endlink is an alias for @link PolygonModelingBuilder.ConvertTypes NXOpen.Facet.PolygonModelingBuilder.ConvertTypes@endlink
PolygonModelingBuilderConvertTypes = PolygonModelingBuilder.ConvertTypes


##  @link RemeshFacetBodyBuilderRemeshModeType NXOpen.Facet.RemeshFacetBodyBuilderRemeshModeType @endlink is an alias for @link RemeshFacetBodyBuilder.RemeshModeType NXOpen.Facet.RemeshFacetBodyBuilder.RemeshModeType@endlink
RemeshFacetBodyBuilderRemeshModeType = RemeshFacetBodyBuilder.RemeshModeType


##  @link RemeshFacetBodyBuilderSharpEdgesLockType NXOpen.Facet.RemeshFacetBodyBuilderSharpEdgesLockType @endlink is an alias for @link RemeshFacetBodyBuilder.SharpEdgesLockType NXOpen.Facet.RemeshFacetBodyBuilder.SharpEdgesLockType@endlink
RemeshFacetBodyBuilderSharpEdgesLockType = RemeshFacetBodyBuilder.SharpEdgesLockType


##  @link ReplaceMeshWithFaceBuilderConeConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilderConeConstraint @endlink is an alias for @link ReplaceMeshWithFaceBuilder.ConeConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.ConeConstraint@endlink
ReplaceMeshWithFaceBuilderConeConstraint = ReplaceMeshWithFaceBuilder.ConeConstraint


##  @link ReplaceMeshWithFaceBuilderCylinderConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilderCylinderConstraint @endlink is an alias for @link ReplaceMeshWithFaceBuilder.CylinderConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.CylinderConstraint@endlink
ReplaceMeshWithFaceBuilderCylinderConstraint = ReplaceMeshWithFaceBuilder.CylinderConstraint


##  @link ReplaceMeshWithFaceBuilderPlaneConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilderPlaneConstraint @endlink is an alias for @link ReplaceMeshWithFaceBuilder.PlaneConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.PlaneConstraint@endlink
ReplaceMeshWithFaceBuilderPlaneConstraint = ReplaceMeshWithFaceBuilder.PlaneConstraint


##  @link ReplaceMeshWithFaceBuilderReplaceMeshOnOption NXOpen.Facet.ReplaceMeshWithFaceBuilderReplaceMeshOnOption @endlink is an alias for @link ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption NXOpen.Facet.ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption@endlink
ReplaceMeshWithFaceBuilderReplaceMeshOnOption = ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption


##  @link ReplaceMeshWithFaceBuilderSphereConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilderSphereConstraint @endlink is an alias for @link ReplaceMeshWithFaceBuilder.SphereConstraint NXOpen.Facet.ReplaceMeshWithFaceBuilder.SphereConstraint@endlink
ReplaceMeshWithFaceBuilderSphereConstraint = ReplaceMeshWithFaceBuilder.SphereConstraint


##  @link ReplaceMeshWithFaceBuilderTypes NXOpen.Facet.ReplaceMeshWithFaceBuilderTypes @endlink is an alias for @link ReplaceMeshWithFaceBuilder.Types NXOpen.Facet.ReplaceMeshWithFaceBuilder.Types@endlink
ReplaceMeshWithFaceBuilderTypes = ReplaceMeshWithFaceBuilder.Types


##  @link SewFacetBodyBuilderInput NXOpen.Facet.SewFacetBodyBuilderInput @endlink is an alias for @link SewFacetBodyBuilder.Input NXOpen.Facet.SewFacetBodyBuilder.Input@endlink
SewFacetBodyBuilderInput = SewFacetBodyBuilder.Input


##  @link SewFacetBodyBuilderVertexIndex NXOpen.Facet.SewFacetBodyBuilderVertexIndex @endlink is an alias for @link SewFacetBodyBuilder.VertexIndex NXOpen.Facet.SewFacetBodyBuilder.VertexIndex@endlink
SewFacetBodyBuilderVertexIndex = SewFacetBodyBuilder.VertexIndex


##  @link SmoothFacetBodyBuilderTypes NXOpen.Facet.SmoothFacetBodyBuilderTypes @endlink is an alias for @link SmoothFacetBodyBuilder.Types NXOpen.Facet.SmoothFacetBodyBuilder.Types@endlink
SmoothFacetBodyBuilderTypes = SmoothFacetBodyBuilder.Types


##  @link SnipFacetBodyBuilderAutomaticFillTypes NXOpen.Facet.SnipFacetBodyBuilderAutomaticFillTypes @endlink is an alias for @link SnipFacetBodyBuilder.AutomaticFillTypes NXOpen.Facet.SnipFacetBodyBuilder.AutomaticFillTypes@endlink
SnipFacetBodyBuilderAutomaticFillTypes = SnipFacetBodyBuilder.AutomaticFillTypes


##  @link SnipFacetBodyBuilderBoundaryFacetTreatmentMethod NXOpen.Facet.SnipFacetBodyBuilderBoundaryFacetTreatmentMethod @endlink is an alias for @link SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod NXOpen.Facet.SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod@endlink
SnipFacetBodyBuilderBoundaryFacetTreatmentMethod = SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod


##  @link SnipFacetBodyBuilderDirectionType NXOpen.Facet.SnipFacetBodyBuilderDirectionType @endlink is an alias for @link SnipFacetBodyBuilder.DirectionType NXOpen.Facet.SnipFacetBodyBuilder.DirectionType@endlink
SnipFacetBodyBuilderDirectionType = SnipFacetBodyBuilder.DirectionType


##  @link SnipFacetBodyBuilderRegionsOptionType NXOpen.Facet.SnipFacetBodyBuilderRegionsOptionType @endlink is an alias for @link SnipFacetBodyBuilder.RegionsOptionType NXOpen.Facet.SnipFacetBodyBuilder.RegionsOptionType@endlink
SnipFacetBodyBuilderRegionsOptionType = SnipFacetBodyBuilder.RegionsOptionType


##  @link SnipFacetBodyBuilderTypes NXOpen.Facet.SnipFacetBodyBuilderTypes @endlink is an alias for @link SnipFacetBodyBuilder.Types NXOpen.Facet.SnipFacetBodyBuilder.Types@endlink
SnipFacetBodyBuilderTypes = SnipFacetBodyBuilder.Types


##  @link SplitCurveMethodBuilderProjectOption NXOpen.Facet.SplitCurveMethodBuilderProjectOption @endlink is an alias for @link SplitCurveMethodBuilder.ProjectOption NXOpen.Facet.SplitCurveMethodBuilder.ProjectOption@endlink
SplitCurveMethodBuilderProjectOption = SplitCurveMethodBuilder.ProjectOption


##  @link STLImportBuilderAngularToleranceTypes NXOpen.Facet.STLImportBuilderAngularToleranceTypes @endlink is an alias for @link STLImportBuilder.AngularToleranceTypes NXOpen.Facet.STLImportBuilder.AngularToleranceTypes@endlink
STLImportBuilderAngularToleranceTypes = STLImportBuilder.AngularToleranceTypes


##  @link STLImportBuilderFacetBodyTypes NXOpen.Facet.STLImportBuilderFacetBodyTypes @endlink is an alias for @link STLImportBuilder.FacetBodyTypes NXOpen.Facet.STLImportBuilder.FacetBodyTypes@endlink
STLImportBuilderFacetBodyTypes = STLImportBuilder.FacetBodyTypes


##  @link STLImportBuilderSTLFileUnitsTypes NXOpen.Facet.STLImportBuilderSTLFileUnitsTypes @endlink is an alias for @link STLImportBuilder.STLFileUnitsTypes NXOpen.Facet.STLImportBuilder.STLFileUnitsTypes@endlink
STLImportBuilderSTLFileUnitsTypes = STLImportBuilder.STLFileUnitsTypes


##  @link SubdivideFacetBodyBuilderInterpolationMethodType NXOpen.Facet.SubdivideFacetBodyBuilderInterpolationMethodType @endlink is an alias for @link SubdivideFacetBodyBuilder.InterpolationMethodType NXOpen.Facet.SubdivideFacetBodyBuilder.InterpolationMethodType@endlink
SubdivideFacetBodyBuilderInterpolationMethodType = SubdivideFacetBodyBuilder.InterpolationMethodType


##  @link SubdivideFacetBodyBuilderSubdivisionMethodType NXOpen.Facet.SubdivideFacetBodyBuilderSubdivisionMethodType @endlink is an alias for @link SubdivideFacetBodyBuilder.SubdivisionMethodType NXOpen.Facet.SubdivideFacetBodyBuilder.SubdivisionMethodType@endlink
SubdivideFacetBodyBuilderSubdivisionMethodType = SubdivideFacetBodyBuilder.SubdivisionMethodType


##  @link WrapMeshBuilderKeepInputBodyType NXOpen.Facet.WrapMeshBuilderKeepInputBodyType @endlink is an alias for @link WrapMeshBuilder.KeepInputBodyType NXOpen.Facet.WrapMeshBuilder.KeepInputBodyType@endlink
WrapMeshBuilderKeepInputBodyType = WrapMeshBuilder.KeepInputBodyType


##  @link WrapMeshBuilderMethodType NXOpen.Facet.WrapMeshBuilderMethodType @endlink is an alias for @link WrapMeshBuilder.MethodType NXOpen.Facet.WrapMeshBuilder.MethodType@endlink
WrapMeshBuilderMethodType = WrapMeshBuilder.MethodType


##  @link WrapMeshBuilderWrapMeshModeType NXOpen.Facet.WrapMeshBuilderWrapMeshModeType @endlink is an alias for @link WrapMeshBuilder.WrapMeshModeType NXOpen.Facet.WrapMeshBuilder.WrapMeshModeType@endlink
WrapMeshBuilderWrapMeshModeType = WrapMeshBuilder.WrapMeshModeType


