from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Clone Model Views  <br> To create a new instance of this class, use @link NXOpen::MFGViewMaker::MFGViewMakerManager::CreateCloneModelViewsBuilder  NXOpen::MFGViewMaker::MFGViewMakerManager::CreateCloneModelViewsBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CloneWithTrace </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.1  <br> 

class CloneModelViewsBuilder(NXOpen.Builder): 
    """ Clone Model Views """


    ## Getter for property: (bool) CloneWithTrace
    ##   the Keep reference to source   
    ##     
    ##  
    ## Getter License requirements: geometric_tol ("GDT")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def CloneWithTrace(self) -> bool:
        """
        Getter for property: (bool) CloneWithTrace
          the Keep reference to source   
            
         
        """
        pass
    
    ## Setter for property: (bool) CloneWithTrace

    ##   the Keep reference to source   
    ##     
    ##  
    ## Setter License requirements: geometric_tol ("GDT")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CloneWithTrace.setter
    def CloneWithTrace(self, cloneWithTrace: bool):
        """
        Setter for property: (bool) CloneWithTrace
          the Keep reference to source   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ModelingViewList NXOpen.ModelingViewList@endlink) SelectedModelViews
    ##   the selected model views   
    ##     
    ##  
    ## Getter License requirements: geometric_tol ("GDT")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.ModelingViewList
    @property
    def SelectedModelViews(self) -> NXOpen.ModelingViewList:
        """
        Getter for property: (@link NXOpen.ModelingViewList NXOpen.ModelingViewList@endlink) SelectedModelViews
          the selected model views   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SourcePart
    ##   a Source Part   
    ##     
    ##  
    ## Getter License requirements: geometric_tol ("GDT")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def SourcePart(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SourcePart
          a Source Part   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SourcePart

    ##   a Source Part   
    ##     
    ##  
    ## Setter License requirements: geometric_tol ("GDT")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @SourcePart.setter
    def SourcePart(self, sourcePart: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SourcePart
          a Source Part   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetPart
    ##   a Target Part   
    ##     
    ##  
    ## Getter License requirements: geometric_tol ("GDT")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def TargetPart(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetPart
          a Target Part   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetPart

    ##   a Target Part   
    ##     
    ##  
    ## Setter License requirements: geometric_tol ("GDT")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @TargetPart.setter
    def TargetPart(self, targetPart: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) TargetPart
          a Target Part   
            
         
        """
        pass
    
    ##  Add model view to selected model view list 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: geometric_tol ("GDT")
    ## 
    ## <param name="modelView"> (@link NXOpen.ModelingView NXOpen.ModelingView@endlink) </param>
    def AddModelViewToSelection(builder: CloneModelViewsBuilder, modelView: NXOpen.ModelingView) -> None:
        """
         Add model view to selected model view list 
        """
        pass
    
    ##  Add model views to selected model view list  
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: geometric_tol ("GDT")
    ## 
    ## <param name="modelView"> (@link NXOpen.ModelingView List[NXOpen.ModelingView]@endlink) </param>
    def AddModelViewsToSelection(builder: CloneModelViewsBuilder, modelView: List[NXOpen.ModelingView]) -> None:
        """
         Add model views to selected model view list  
        """
        pass
    
    ##  Clears the seleced model views list  
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: geometric_tol ("GDT")
    @staticmethod
    def ClearSelectedModelViews(builder: CloneModelViewsBuilder) -> None:
        """
         Clears the seleced model views list  
        """
        pass
    
    ##  Returns the non-predefined model views of the source part  
    ##  @return A tuple consisting of (modelViews, viewNames). 
    ##  - modelViews is: @link NXOpen.ModelingView List[NXOpen.ModelingView]@endlink.
    ##  - viewNames is: List[str].

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: geometric_tol ("GDT")
    @staticmethod
    def GetModelViewsOfSourcePart(builder: CloneModelViewsBuilder) -> Tuple[List[NXOpen.ModelingView], List[str]]:
        """
         Returns the non-predefined model views of the source part  
         @return A tuple consisting of (modelViews, viewNames). 
         - modelViews is: @link NXOpen.ModelingView List[NXOpen.ModelingView]@endlink.
         - viewNames is: List[str].

        """
        pass
    
import NXOpen
## 
##     Represents a class to create enter and exit the MFGViewMaker application
##     
## 
##   <br>  Created in NX11.0.1  <br> 

class MFGViewMakerApplicationBuilder(NXOpen.NXObject): 
    """
    Represents a class to create enter and exit the MFGViewMaker application
    """


    ##   Enter the MFGViewMaker application 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: geometric_tol ("GDT")
    @staticmethod
    def Enter(builder: MFGViewMakerApplicationBuilder) -> None:
        """
          Enter the MFGViewMaker application 
        """
        pass
    
    ##   Exit the MFGViewMaker application this call will destroy the builder
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: geometric_tol ("GDT")
    @staticmethod
    def Exit(builder: MFGViewMakerApplicationBuilder) -> None:
        """
          Exit the MFGViewMaker application this call will destroy the builder
        """
        pass
    
import NXOpen
##  Represents a manager of MFGViewMaker builders  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class MFGViewMakerManager(NXOpen.Object): 
    """ Represents a manager of MFGViewMaker builders """


    ##  Creates the application builder 
    ##  @return builder (@link MFGViewMakerApplicationBuilder NXOpen.MFGViewMaker.MFGViewMakerApplicationBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: geometric_tol ("GDT")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateApplicationBuilder(part: NXOpen.Part) -> MFGViewMakerApplicationBuilder:
        """
         Creates the application builder 
         @return builder (@link MFGViewMakerApplicationBuilder NXOpen.MFGViewMaker.MFGViewMakerApplicationBuilder@endlink):  .
        """
        pass
    
    ##  Creates a clone model views dialog builder 
    ##  @return builder (@link CloneModelViewsBuilder NXOpen.MFGViewMaker.CloneModelViewsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: geometric_tol ("GDT")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateCloneModelViewsBuilder(part: NXOpen.Part) -> CloneModelViewsBuilder:
        """
         Creates a clone model views dialog builder 
         @return builder (@link CloneModelViewsBuilder NXOpen.MFGViewMaker.CloneModelViewsBuilder@endlink): .
        """
        pass
    
    ##  Return the application builder 
    ##  @return builder (@link MFGViewMakerApplicationBuilder NXOpen.MFGViewMaker.MFGViewMakerApplicationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: geometric_tol ("GDT")
    @staticmethod
    def GetApplicationBuilder() -> MFGViewMakerApplicationBuilder:
        """
         Return the application builder 
         @return builder (@link MFGViewMakerApplicationBuilder NXOpen.MFGViewMaker.MFGViewMakerApplicationBuilder@endlink): .
        """
        pass
    
## @package NXOpen.MFGViewMaker
## Classes, Enums and Structs under NXOpen.MFGViewMaker namespace

