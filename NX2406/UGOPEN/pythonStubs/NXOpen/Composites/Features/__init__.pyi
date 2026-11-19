from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
##  Creates or edits a @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  object  <br> To create a new instance of this class, use @link NXOpen::Composites::Features::Manager::CreateLayupSurfaceBuilder  NXOpen::Composites::Features::Manager::CreateLayupSurfaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class LayupSurfaceBuilder(NXOpen.Features.FeatureBuilder): 
    """ Creates or edits a <ja_class>Composites.Features.LayupSurface</ja_class> object """


    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) BoundaryObjects
    ##  Returns the boundary objects that define the boundaries of the regions of the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink    
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def BoundaryObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) BoundaryObjects
         Returns the boundary objects that define the boundaries of the regions of the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink    
            
         
        """
        pass
    
    ## Getter for property: (bool) NormalFlipped
    ##  Returns the logical value which defines whether the input sheet body normal should be flipped    
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def NormalFlipped(self) -> bool:
        """
        Getter for property: (bool) NormalFlipped
         Returns the logical value which defines whether the input sheet body normal should be flipped    
            
         
        """
        pass
    
    ## Setter for property: (bool) NormalFlipped

    ##  Returns the logical value which defines whether the input sheet body normal should be flipped    
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @NormalFlipped.setter
    def NormalFlipped(self, isNormalFlipped: bool):
        """
        Setter for property: (bool) NormalFlipped
         Returns the logical value which defines whether the input sheet body normal should be flipped    
            
         
        """
        pass
    
    ## Getter for property: (bool) ProjectRegionPoints
    ##  Returns whether the input region points will be projected to the sheet body  
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ProjectRegionPoints(self) -> bool:
        """
        Getter for property: (bool) ProjectRegionPoints
         Returns whether the input region points will be projected to the sheet body  
            
         
        """
        pass
    
    ## Setter for property: (bool) ProjectRegionPoints

    ##  Returns whether the input region points will be projected to the sheet body  
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ProjectRegionPoints.setter
    def ProjectRegionPoints(self, projectRegionPoints: bool):
        """
        Setter for property: (bool) ProjectRegionPoints
         Returns whether the input region points will be projected to the sheet body  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectionDirection
    ##  Returns the projection direction object to project boundary objects to the selected sheet body   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.ProjectionOptions
    @property
    def ProjectionDirection(self) -> NXOpen.GeometricUtilities.ProjectionOptions:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectionDirection
         Returns the projection direction object to project boundary objects to the selected sheet body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.RegionPointList NXOpen.RegionPointList@endlink) Regions
    ##  Returns the region list that defines the extents of the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink    
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.RegionPointList
    @property
    def Regions(self) -> NXOpen.RegionPointList:
        """
        Getter for property: (@link NXOpen.RegionPointList NXOpen.RegionPointList@endlink) Regions
         Returns the region list that defines the extents of the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Body NXOpen.Body@endlink) SheetBody
    ##  Returns the sheet body that the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  is defined on   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Body
    @property
    def SheetBody(self) -> NXOpen.Body:
        """
        Getter for property: (@link NXOpen.Body NXOpen.Body@endlink) SheetBody
         Returns the sheet body that the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  is defined on   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Body NXOpen.Body@endlink) SheetBody

    ##  Returns the sheet body that the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  is defined on   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SheetBody.setter
    def SheetBody(self, sheetBody: NXOpen.Body):
        """
        Setter for property: (@link NXOpen.Body NXOpen.Body@endlink) SheetBody
         Returns the sheet body that the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  is defined on   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a layup surface feature that defines a surface that a @link Composites::Laminate Composites::Laminate@endlink  can be built upon  <br> To create or edit an instance of this class, use @link NXOpen::Composites::Features::LayupSurfaceBuilder  NXOpen::Composites::Features::LayupSurfaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class LayupSurface(NXOpen.Features.Feature): 
    """ Represents a layup surface feature that defines a surface that a <ja_class>Composites.Laminate</ja_class> can be built upon """
    pass


import NXOpen
##  Manager of builders and common functionality of Composites features <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Manager(NXOpen.Object): 
    """ Manager of builders and common functionality of Composites features"""


    ##  Creates a @link Composites::Features::LayupSurfaceBuilder Composites::Features::LayupSurfaceBuilder@endlink  to create or edit a @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  
    ##  @return builder_p (@link LayupSurfaceBuilder NXOpen.Composites.Features.LayupSurfaceBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="layupSurfaceTag"> (@link LayupSurface NXOpen.Composites.Features.LayupSurface@endlink) </param>
    def CreateLayupSurfaceBuilder(part: NXOpen.Part, layupSurfaceTag: LayupSurface) -> LayupSurfaceBuilder:
        """
         Creates a @link Composites::Features::LayupSurfaceBuilder Composites::Features::LayupSurfaceBuilder@endlink  to create or edit a @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  
         @return builder_p (@link LayupSurfaceBuilder NXOpen.Composites.Features.LayupSurfaceBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::Features::RegionBuilder Composites::Features::RegionBuilder@endlink  to create or edit a @link Composites::Features::Region Composites::Features::Region@endlink  
    ##  @return builder_p (@link RegionBuilder NXOpen.Composites.Features.RegionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="regionTag"> (@link Region NXOpen.Composites.Features.Region@endlink) </param>
    def CreateRegionBuilder(part: NXOpen.Part, regionTag: Region) -> RegionBuilder:
        """
         Creates a @link Composites::Features::RegionBuilder Composites::Features::RegionBuilder@endlink  to create or edit a @link Composites::Features::Region Composites::Features::Region@endlink  
         @return builder_p (@link RegionBuilder NXOpen.Composites.Features.RegionBuilder@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
##  Creates or edits a @link Composites::Features::Region Composites::Features::Region@endlink  object  <br> To create a new instance of this class, use @link NXOpen::Composites::Features::Manager::CreateRegionBuilder  NXOpen::Composites::Features::Manager::CreateRegionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class RegionBuilder(NXOpen.Features.FeatureBuilder): 
    """ Creates or edits a <ja_class>Composites.Features.Region</ja_class> object """


    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) BoundaryObjects
    ##  Returns the boundary objects that define the boundaries of the regions of the @link Composites::Features::Region Composites::Features::Region@endlink    
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def BoundaryObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) BoundaryObjects
         Returns the boundary objects that define the boundaries of the regions of the @link Composites::Features::Region Composites::Features::Region@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) ParentLayupSurface
    ##  Returns the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  that the @link Composites::Features::Region Composites::Features::Region@endlink  is defined on   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Features.Feature
    @property
    def ParentLayupSurface(self) -> NXOpen.Features.Feature:
        """
        Getter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) ParentLayupSurface
         Returns the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  that the @link Composites::Features::Region Composites::Features::Region@endlink  is defined on   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) ParentLayupSurface

    ##  Returns the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  that the @link Composites::Features::Region Composites::Features::Region@endlink  is defined on   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ParentLayupSurface.setter
    def ParentLayupSurface(self, parentFeature: NXOpen.Features.Feature):
        """
        Setter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) ParentLayupSurface
         Returns the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  that the @link Composites::Features::Region Composites::Features::Region@endlink  is defined on   
            
         
        """
        pass
    
    ## Getter for property: (bool) ProjectRegionPoints
    ##  Returns whether the input region points should be projected to the parent @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ProjectRegionPoints(self) -> bool:
        """
        Getter for property: (bool) ProjectRegionPoints
         Returns whether the input region points should be projected to the parent @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink   
            
         
        """
        pass
    
    ## Setter for property: (bool) ProjectRegionPoints

    ##  Returns whether the input region points should be projected to the parent @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ProjectRegionPoints.setter
    def ProjectRegionPoints(self, projectRegionPoints: bool):
        """
        Setter for property: (bool) ProjectRegionPoints
         Returns whether the input region points should be projected to the parent @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectionDirection
    ##  Returns the projection direction object to project boundary objects to the selected sheet body   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.ProjectionOptions
    @property
    def ProjectionDirection(self) -> NXOpen.GeometricUtilities.ProjectionOptions:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectionDirection
         Returns the projection direction object to project boundary objects to the selected sheet body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.RegionPointList NXOpen.RegionPointList@endlink) Regions
    ##  Returns the region list that defines the extents of the @link Composites::Features::Region Composites::Features::Region@endlink    
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.RegionPointList
    @property
    def Regions(self) -> NXOpen.RegionPointList:
        """
        Getter for property: (@link NXOpen.RegionPointList NXOpen.RegionPointList@endlink) Regions
         Returns the region list that defines the extents of the @link Composites::Features::Region Composites::Features::Region@endlink    
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a composites region feature defining the coverage of composites objects, such as @link Composites::Ply Composites::Ply@endlink   <br> To create or edit an instance of this class, use @link NXOpen::Composites::Features::RegionBuilder  NXOpen::Composites::Features::RegionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Region(NXOpen.Features.Feature): 
    """ Represents a composites region feature defining the coverage of composites objects, such as <ja_class>Composites.Ply</ja_class> """
    pass


## @package NXOpen.Composites.Features
## Classes, Enums and Structs under NXOpen.Composites.Features namespace

