from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class LayupSurfaceBuilder(NXOpen.Features.FeatureBuilder): 
    """ Creates or edits a Composites.Features.LayupSurface object """
    @property
    def BoundaryObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) BoundaryObjects
         Returns the boundary objects that define the boundaries of the regions of the  Composites::Features::LayupSurface    
            
         
        """
        pass
    @property
    def NormalFlipped(self) -> bool:
        """
        Getter for property: (bool) NormalFlipped
         Returns the logical value which defines whether the input sheet body normal should be flipped    
            
         
        """
        pass
    @NormalFlipped.setter
    def NormalFlipped(self, isNormalFlipped: bool):
        """
        Setter for property: (bool) NormalFlipped
         Returns the logical value which defines whether the input sheet body normal should be flipped    
            
         
        """
        pass
    @property
    def ProjectRegionPoints(self) -> bool:
        """
        Getter for property: (bool) ProjectRegionPoints
         Returns whether the input region points will be projected to the sheet body  
            
         
        """
        pass
    @ProjectRegionPoints.setter
    def ProjectRegionPoints(self, projectRegionPoints: bool):
        """
        Setter for property: (bool) ProjectRegionPoints
         Returns whether the input region points will be projected to the sheet body  
            
         
        """
        pass
    @property
    def ProjectionDirection(self) -> NXOpen.GeometricUtilities.ProjectionOptions:
        """
        Getter for property: ( NXOpen.GeometricUtilities.ProjectionOptions) ProjectionDirection
         Returns the projection direction object to project boundary objects to the selected sheet body   
            
         
        """
        pass
    @property
    def Regions(self) -> NXOpen.RegionPointList:
        """
        Getter for property: ( NXOpen.RegionPointList) Regions
         Returns the region list that defines the extents of the  Composites::Features::LayupSurface    
            
         
        """
        pass
    @property
    def SheetBody(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) SheetBody
         Returns the sheet body that the  Composites::Features::LayupSurface  is defined on   
            
         
        """
        pass
    @SheetBody.setter
    def SheetBody(self, sheetBody: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) SheetBody
         Returns the sheet body that the  Composites::Features::LayupSurface  is defined on   
            
         
        """
        pass
import NXOpen.Features
class LayupSurface(NXOpen.Features.Feature): 
    """ Represents a layup surface feature that defines a surface that a Composites.Laminate can be built upon """
    pass
import NXOpen
class Manager(NXOpen.Object): 
    """ Manager of builders and common functionality of Composites features"""
    def CreateLayupSurfaceBuilder(part: NXOpen.Part, layupSurfaceTag: LayupSurface) -> LayupSurfaceBuilder:
        """
         Creates a Composites.Features.LayupSurfaceBuilder to create or edit a Composites.Features.LayupSurface 
         Returns builder_p ( LayupSurfaceBuilder NXOpen.Compo): .
        """
        pass
    def CreateRegionBuilder(part: NXOpen.Part, regionTag: Region) -> RegionBuilder:
        """
         Creates a Composites.Features.RegionBuilder to create or edit a Composites.Features.Region 
         Returns builder_p ( RegionBuilder NXOpen.Compo): .
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class RegionBuilder(NXOpen.Features.FeatureBuilder): 
    """ Creates or edits a Composites.Features.Region object """
    @property
    def BoundaryObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) BoundaryObjects
         Returns the boundary objects that define the boundaries of the regions of the  Composites::Features::Region    
            
         
        """
        pass
    @property
    def ParentLayupSurface(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) ParentLayupSurface
         Returns the  Composites::Features::LayupSurface  that the  Composites::Features::Region  is defined on   
            
         
        """
        pass
    @ParentLayupSurface.setter
    def ParentLayupSurface(self, parentFeature: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) ParentLayupSurface
         Returns the  Composites::Features::LayupSurface  that the  Composites::Features::Region  is defined on   
            
         
        """
        pass
    @property
    def ProjectRegionPoints(self) -> bool:
        """
        Getter for property: (bool) ProjectRegionPoints
         Returns whether the input region points should be projected to the parent  Composites::Features::LayupSurface   
            
         
        """
        pass
    @ProjectRegionPoints.setter
    def ProjectRegionPoints(self, projectRegionPoints: bool):
        """
        Setter for property: (bool) ProjectRegionPoints
         Returns whether the input region points should be projected to the parent  Composites::Features::LayupSurface   
            
         
        """
        pass
    @property
    def ProjectionDirection(self) -> NXOpen.GeometricUtilities.ProjectionOptions:
        """
        Getter for property: ( NXOpen.GeometricUtilities.ProjectionOptions) ProjectionDirection
         Returns the projection direction object to project boundary objects to the selected sheet body   
            
         
        """
        pass
    @property
    def Regions(self) -> NXOpen.RegionPointList:
        """
        Getter for property: ( NXOpen.RegionPointList) Regions
         Returns the region list that defines the extents of the  Composites::Features::Region    
            
         
        """
        pass
import NXOpen.Features
class Region(NXOpen.Features.Feature): 
    """ Represents a composites region feature defining the coverage of composites objects, such as Composites.Ply """
    pass
