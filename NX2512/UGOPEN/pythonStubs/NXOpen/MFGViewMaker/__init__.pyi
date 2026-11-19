from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class CloneModelViewsBuilder(NXOpen.Builder): 
    """ Clone Model Views """
    @property
    def CloneWithTrace(self) -> bool:
        """
        Getter for property: (bool) CloneWithTrace
         Returns the Keep reference to source   
            
         
        """
        pass
    @CloneWithTrace.setter
    def CloneWithTrace(self, cloneWithTrace: bool):
        """
        Setter for property: (bool) CloneWithTrace
         Returns the Keep reference to source   
            
         
        """
        pass
    @property
    def SelectedModelViews(self) -> NXOpen.ModelingViewList:
        """
        Getter for property: ( NXOpen.ModelingViewList) SelectedModelViews
         Returns the selected model views   
            
         
        """
        pass
    @property
    def SourcePart(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) SourcePart
         Returns a Source Part   
            
         
        """
        pass
    @SourcePart.setter
    def SourcePart(self, sourcePart: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) SourcePart
         Returns a Source Part   
            
         
        """
        pass
    @property
    def TargetPart(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) TargetPart
         Returns a Target Part   
            
         
        """
        pass
    @TargetPart.setter
    def TargetPart(self, targetPart: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) TargetPart
         Returns a Target Part   
            
         
        """
        pass
    def AddModelViewToSelection(self, modelView: NXOpen.ModelingView) -> None:
        """
         Add model view to selected model view list 
        """
        pass
    def AddModelViewsToSelection(self, modelView: List[NXOpen.ModelingView]) -> None:
        """
         Add model views to selected model view list  
        """
        pass
    def ClearSelectedModelViews(self) -> None:
        """
         Clears the seleced model views list  
        """
        pass
    def GetModelViewsOfSourcePart(self) -> Tuple[List[NXOpen.ModelingView], List[str]]:
        """
         Returns the non-predefined model views of the source part  
         Returns A tuple consisting of (modelViews, viewNames). 
         - modelViews is:  NXOpen.ModelingView Li.
         - viewNames is: List[str].

        """
        pass
import NXOpen
class MFGViewMakerApplicationBuilder(NXOpen.NXObject): 
    """
    Represents a class to create enter and exit the MFGViewMaker application
    """
    def Enter(self) -> None:
        """
          Enter the MFGViewMaker application 
        """
        pass
    def Exit(self) -> None:
        """
          Exit the MFGViewMaker application this call will destroy the builder
        """
        pass
import NXOpen
class MFGViewMakerManager(NXOpen.Object): 
    """ Represents a manager of MFGViewMaker builders """
    def CreateApplicationBuilder(part: NXOpen.Part) -> MFGViewMakerApplicationBuilder:
        """
         Creates the application builder 
         Returns builder ( MFGViewMakerApplicationBuilder NXOpen.MF):  .
        """
        pass
    def CreateCloneModelViewsBuilder(part: NXOpen.Part) -> CloneModelViewsBuilder:
        """
         Creates a clone model views dialog builder 
         Returns builder ( CloneModelViewsBuilder NXOpen.MF): .
        """
        pass
    def GetApplicationBuilder() -> MFGViewMakerApplicationBuilder:
        """
         Return the application builder 
         Returns builder ( MFGViewMakerApplicationBuilder NXOpen.MF): .
        """
        pass
