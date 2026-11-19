from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Features.Industry
##  Represents the interface for navigator node classes <br> Use the @link NXOpen::AECDesign::AECDesignNavigatorView NXOpen::AECDesign::AECDesignNavigatorView@endlink  class to create a navigator node  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class AECDesignNavigatorNode(NXOpen.Features.Industry.IndustryNavigatorNode): 
    """ Represents the interface for navigator node classes"""


    ##  Changes node show and hide state. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="status"> (int) </param>
    def ChangeNodeState(node: AECDesignNavigatorNode, status: int) -> None:
        """
         Changes node show and hide state. 
        """
        pass
    
    ##  The objects represented by the node. 
    ##  @return nodeObjects (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def GetNodeObjects(node: AECDesignNavigatorNode) -> List[NXOpen.TaggedObject]:
        """
         The objects represented by the node. 
         @return nodeObjects (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
        """
        pass
    
    ##  Sets the objects represented by the node. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="nodeObjects"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    def SetNodeObjects(node: AECDesignNavigatorNode, nodeObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the objects represented by the node. 
        """
        pass
    
import NXOpen
##  Represents the interface for AEC design navigator root classes.  <br> An instance of this class can be obtained from @link NXOpen::AECDesign::AECDesignSession::GetAECDesignNavigatorRoot NXOpen::AECDesign::AECDesignSession::GetAECDesignNavigatorRoot@endlink   <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class AECDesignNavigatorRoot(NXOpen.NXObject): 
    """ Represents the interface for AEC design navigator root classes. """
    pass


import NXOpen
##  Represents the interface for navigator view classe <br> Use the @link NXOpen::AECDesign::AECDesignNavigator NXOpen::AECDesign::AECDesignNavigator@endlink  class to get a navigator view  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class AECDesignNavigatorView(NXOpen.NXObject): 
    """ Represents the interface for navigator view classe"""


    ##  Adds a root object to the navigator to represent the object. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="name"> (str) </param>
    ## <param name="nodeObjects"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    def AddRootNode(selfView: AECDesignNavigatorView, name: str, nodeObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Adds a root object to the navigator to represent the object. 
        """
        pass
    
    ##  Gets root node. 
    ##  @return rootNode (@link AECDesignNavigator NXOpen.AECDesign.AECDesignNavigator@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def GetRootNode(selfView: AECDesignNavigatorView) -> AECDesignNavigator:
        """
         Gets root node. 
         @return rootNode (@link AECDesignNavigator NXOpen.AECDesign.AECDesignNavigator@endlink): .
        """
        pass
    
    ##  Gets selected nodes. 
    ##  @return selectedNodes (@link AECDesignNavigator List[NXOpen.AECDesign.AECDesignNavigator]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def GetSelectedNodes(view: AECDesignNavigatorView) -> List[AECDesignNavigator]:
        """
         Gets selected nodes. 
         @return selectedNodes (@link AECDesignNavigator List[NXOpen.AECDesign.AECDesignNavigator]@endlink): .
        """
        pass
    
    ##  Removes root node. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def RemoveRootNode(selfView: AECDesignNavigatorView) -> None:
        """
         Removes root node. 
        """
        pass
    
    ##  Sets selected nodes. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="selectedNodes"> (@link AECDesignNavigator List[NXOpen.AECDesign.AECDesignNavigator]@endlink) </param>
    def SetSelectedNodes(view: AECDesignNavigatorView, selectedNodes: List[AECDesignNavigator]) -> None:
        """
         Sets selected nodes. 
        """
        pass
    
import NXOpen
##  Represents the interface for navigator action classes <br> Can be create automatically by the data structures  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class AECDesignNavigator(NXOpen.NXObject): 
    """ Represents the interface for navigator action classes"""


    ##  Hides a navigator. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def Hide(selfNavigator: AECDesignNavigator) -> None:
        """
         Hides a navigator. 
        """
        pass
    
    ##  Hides a navigator view. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="viewIndex"> (int) </param>
    def HideView(selfNavigator: AECDesignNavigator, viewIndex: int) -> None:
        """
         Hides a navigator view. 
        """
        pass
    
    ##  Shows a navigator view. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="viewIndex"> (int) </param>
    def ShowView(selfNavigator: AECDesignNavigator, viewIndex: int) -> None:
        """
         Shows a navigator view. 
        """
        pass
    
import NXOpen
import NXOpen.Annotations
import NXOpen.Features.AECDesign
##  Represents AECDesign session  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class AECDesignSession(NXOpen.Object): 
    """ Represents AECDesign session """


    ## Getter for property: (str) ActiveLevelName
    ##   the active level name  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def ActiveLevelName(self) -> str:
        """
        Getter for property: (str) ActiveLevelName
          the active level name  
            
         
        """
        pass
    
    ## Setter for property: (str) ActiveLevelName

    ##   the active level name  
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ActiveLevelName.setter
    def ActiveLevelName(self, activeLevel: str):
        """
        Setter for property: (str) ActiveLevelName
          the active level name  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) LevelContainer
    ##   the level container  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Part
    @property
    def LevelContainer(self) -> NXOpen.Part:
        """
        Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) LevelContainer
          the level container  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) LevelContainer

    ##   the level container  
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @LevelContainer.setter
    def LevelContainer(self, levelContainer: NXOpen.Part):
        """
        Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) LevelContainer
          the level container  
            
         
        """
        pass
    
    ## Getter for property: (@link PlanElevationViewManager NXOpen.AECDesign.PlanElevationViewManager@endlink) PlanElevationViewManager
    ##   the plan elevation view manager  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return PlanElevationViewManager
    @property
    def PlanElevationViewManager(self) -> PlanElevationViewManager:
        """
        Getter for property: (@link PlanElevationViewManager NXOpen.AECDesign.PlanElevationViewManager@endlink) PlanElevationViewManager
          the plan elevation view manager  
            
         
        """
        pass
    
    ##  Add Curves to grid line 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="tgSketch"> (@link NXOpen.Sketch NXOpen.Sketch@endlink) </param>
    ## <param name="curves"> (@link NXOpen.Curve List[NXOpen.Curve]@endlink) </param>
    def AddCurvesToGridLine(tgSketch: NXOpen.Sketch, curves: List[NXOpen.Curve]) -> None:
        """
         Add Curves to grid line 
        """
        pass
    
    ##  Changes the state of AEC line format toggle
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="tgToggle"> (@link NXOpen.Annotations.Annotation NXOpen.Annotations.Annotation@endlink) </param>
    @staticmethod
    def ChangeLineEndToggleState(tgToggle: NXOpen.Annotations.Annotation) -> None:
        """
         Changes the state of AEC line format toggle
        """
        pass
    
    ##  Starts grid creation 
    ##  @return pTgGirdFrec (@link NXOpen.Features.AECDesign.Grid NXOpen.Features.AECDesign.Grid@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    def CreateGrid() -> NXOpen.Features.AECDesign.Grid:
        """
         Starts grid creation 
         @return pTgGirdFrec (@link NXOpen.Features.AECDesign.Grid NXOpen.Features.AECDesign.Grid@endlink): .
        """
        pass
    
    ##  Deletes objects for grid or level 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ##  Objects to be deleted 
    def DeleteObjectsForGridLevel(tgSketch: NXOpen.Sketch, objects: List[NXOpen.NXObject]) -> None:
        """
         Deletes objects for grid or level 
        """
        pass
    
    ##  Enables AEC line format elbow
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="tgElbow"> (@link NXOpen.Annotations.Annotation NXOpen.Annotations.Annotation@endlink) </param>
    @staticmethod
    def EnableAECLineElbow(tgElbow: NXOpen.Annotations.Annotation) -> None:
        """
         Enables AEC line format elbow
        """
        pass
    
    ##  Finishes grid task 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="tgGridFrec"> (@link NXOpen.Features.AECDesign.Grid NXOpen.Features.AECDesign.Grid@endlink) </param>
    @staticmethod
    def FinishGridTask(tgGridFrec: NXOpen.Features.AECDesign.Grid) -> None:
        """
         Finishes grid task 
        """
        pass
    
    ##  Finishes the last AEC line format
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def FinishLastAECLineFormat() -> None:
        """
         Finishes the last AEC line format
        """
        pass
    
    ##  Finishes level creation 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="level"> (@link NXOpen.Features.AECDesign.Level NXOpen.Features.AECDesign.Level@endlink) </param>
    @staticmethod
    def FinishLevelCreation(level: NXOpen.Features.AECDesign.Level) -> None:
        """
         Finishes level creation 
        """
        pass
    
    ##  Establish aec design navigator root 
    ##  @return navRoot (@link AECDesignNavigatorRoot NXOpen.AECDesign.AECDesignNavigatorRoot@endlink):  .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def GetAECDesignNavigatorRoot() -> AECDesignNavigatorRoot:
        """
         Establish aec design navigator root 
         @return navRoot (@link AECDesignNavigatorRoot NXOpen.AECDesign.AECDesignNavigatorRoot@endlink):  .
        """
        pass
    
    ##  Gets the position and height of active level
    ##  @return A tuple consisting of (levelPosition, levelHeight). 
    ##  - levelPosition is: float.
    ##  - levelHeight is: float.

    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def GetActiveLevelPositionAndHeight() -> Tuple[float, float]:
        """
         Gets the position and height of active level
         @return A tuple consisting of (levelPosition, levelHeight). 
         - levelPosition is: float.
         - levelHeight is: float.

        """
        pass
    
    ##  Get names for all the levels
    ##  @return levelNames (List[str]): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLevelNames() -> List[str]:
        """
         Get names for all the levels
         @return levelNames (List[str]): .
        """
        pass
    
    ##  Exits the Sketch environment. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def LevelSketchEnd() -> None:
        """
         Exits the Sketch environment. 
        """
        pass
    
    ##  On exiting the BIM Design application
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def OnExitApplication() -> None:
        """
         On exiting the BIM Design application
        """
        pass
    
    ##  Set Curves to last saved curves in grid task 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="tgSketch"> (@link NXOpen.Sketch NXOpen.Sketch@endlink) </param>
    ## <param name="curves"> (@link NXOpen.Curve List[NXOpen.Curve]@endlink) </param>
    def SetLastSavedCurvesInGridTask(tgSketch: NXOpen.Sketch, curves: List[NXOpen.Curve]) -> None:
        """
         Set Curves to last saved curves in grid task 
        """
        pass
    
    ##  Sets entites as the last saved entites in the grid task. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="tgSketch"> (@link NXOpen.Sketch NXOpen.Sketch@endlink) </param>
    ## <param name="entites"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def SetLastSavedEntitesInGridTask(tgSketch: NXOpen.Sketch, entites: List[NXOpen.NXObject]) -> None:
        """
         Sets entites as the last saved entites in the grid task. 
        """
        pass
    
    ##  Set multi-segment toggle off 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def SetMultiSegmentToggleOff() -> None:
        """
         Set multi-segment toggle off 
        """
        pass
    
    ##  Set multi-segment toggle on 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def SetMultiSegmentToggleOn() -> None:
        """
         Set multi-segment toggle on 
        """
        pass
    
    ##  Sets the origin for the BIM line. It will not move the BIM line.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="tgBaseLine"> (@link NXOpen.Annotations.AECDesignBaseLine NXOpen.Annotations.AECDesignBaseLine@endlink) </param>
    ## <param name="x"> (float) </param>
    ## <param name="y"> (float) </param>
    ## <param name="z"> (float) </param>
    def SetOnlySelfOriginBaseLine(tgBaseLine: NXOpen.Annotations.AECDesignBaseLine, x: float, y: float, z: float) -> None:
        """
         Sets the origin for the BIM line. It will not move the BIM line.
        """
        pass
    
    ##  Sets the state of in the level update.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="bInLevelUpdate"> (bool) </param>
    @staticmethod
    def SetStateOfInLevelUpdate(bInLevelUpdate: bool) -> None:
        """
         Sets the state of in the level update.
        """
        pass
    
    ##  Starts to edit AEC line format
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="tgAECLine"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def StartEditAECLineFormat(tgAECLine: NXOpen.NXObject) -> None:
        """
         Starts to edit AEC line format
        """
        pass
    
    ##  Starts grid task 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="tgGridFrec"> (@link NXOpen.Features.AECDesign.Grid NXOpen.Features.AECDesign.Grid@endlink) </param>
    @staticmethod
    def StartGridTask(tgGridFrec: NXOpen.Features.AECDesign.Grid) -> None:
        """
         Starts grid task 
        """
        pass
    
    ##  Starts level creation 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="level"> (@link NXOpen.Features.AECDesign.Level NXOpen.Features.AECDesign.Level@endlink) </param>
    @staticmethod
    def StartLevelCreation(level: NXOpen.Features.AECDesign.Level) -> None:
        """
         Starts level creation 
        """
        pass
    
    ##  Updates and regenerates all symbols for base line.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="tgBaseLine"> (@link NXOpen.Annotations.AECDesignBaseLine NXOpen.Annotations.AECDesignBaseLine@endlink) </param>
    @staticmethod
    def UpdateAndRegenAllSymbolsForBaseLine(tgBaseLine: NXOpen.Annotations.AECDesignBaseLine) -> None:
        """
         Updates and regenerates all symbols for base line.
        """
        pass
    
    ##  Updates dimensions of BIM curves 
    ##  @return bHaveDimension (bool): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## <param name="tgSketch"> (@link NXOpen.Sketch NXOpen.Sketch@endlink) </param>
    ## <param name="baseCurves"> (@link NXOpen.Annotations.AECDesignBaseLine List[NXOpen.Annotations.AECDesignBaseLine]@endlink) </param>
    def UpdateDimensionsOfBIMCurves(tgSketch: NXOpen.Sketch, baseCurves: List[NXOpen.Annotations.AECDesignBaseLine]) -> bool:
        """
         Updates dimensions of BIM curves 
         @return bHaveDimension (bool): .
        """
        pass
    
##  Represents the center segment type of grid line. 
##  The CFW of center segment is same with the end segment
class AecGridCenterSegmentType(Enum):
    """
    Members Include: <Continuous> <NotSet> <Custom>
    """
    Continuous: int
    NotSet: int
    Custom: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AecGridCenterSegmentType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the AEC line drag point type. 
##  The drag point in the end point of AEC line
class AecLineFormatDragPointType(Enum):
    """
    Members Include: <EndPoint> <GapPoint> <ElbowFirst> <ElbowSecond>
    """
    EndPoint: int
    GapPoint: int
    ElbowFirst: int
    ElbowSecond: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AecLineFormatDragPointType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the AEC line format type. 
##  AEC line format of elbow
class AecLineFormatType(Enum):
    """
    Members Include: <Elbow> <EndSymbolToggle> <DragPoint>
    """
    Elbow: int
    EndSymbolToggle: int
    DragPoint: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AecLineFormatType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the AEC Line type. 
##  unknow AEC Line type
class AecLineType(Enum):
    """
    Members Include: <Unknown> <GridLine> <LevelLine> <Level3dLine>
    """
    Unknown: int
    GridLine: int
    LevelLine: int
    Level3dLine: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AecLineType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the AECSymbol type. 
##  unknow AECSymbol type
class AecSymbolType(Enum):
    """
    Members Include: <Unknown> <GridEndNote> <LevelEndNote>
    """
    Unknown: int
    GridEndNote: int
    LevelEndNote: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AecSymbolType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the AEC task enviroment type. 
##  not in AEC task enviroment
class AecTaskEnvType(Enum):
    """
    Members Include: <NotSet> <Grid> <Level>
    """
    NotSet: int
    Grid: int
    Level: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AecTaskEnvType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the index in the level symbol. 
##  height index in the level symbol
class LevelSymbolIndex(Enum):
    """
    Members Include: <Height> <LevelName>
    """
    Height: int
    LevelName: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> LevelSymbolIndex:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents AECDesign Plan Elevation View Manager  <br> This class is sub-object of AECDesignSession, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class PlanElevationViewManager(NXOpen.NXObject): 
    """ Represents AECDesign Plan Elevation View Manager """


    ##  Represent view types of the level view.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FloorView</term><description> 
    ## </description> </item><item><term> 
    ## CeilingView</term><description> 
    ## </description> </item></list>
    class LevelViewType(Enum):
        """
        Members Include: <FloorView> <CeilingView>
        """
        FloorView: int
        CeilingView: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlanElevationViewManager.LevelViewType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Gets the front elevation view.
    ##  @return frontElevationView (@link PlanElevationView NXOpen.AECDesign.PlanElevationView@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def GetFrontElevationView(manager: PlanElevationViewManager) -> PlanElevationView:
        """
         Gets the front elevation view.
         @return frontElevationView (@link PlanElevationView NXOpen.AECDesign.PlanElevationView@endlink): .
        """
        pass
    
    ##  Gets the left elevation view. 
    ##  @return leftElevationView (@link PlanElevationView NXOpen.AECDesign.PlanElevationView@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def GetLeftElevationView(manager: PlanElevationViewManager) -> PlanElevationView:
        """
         Gets the left elevation view. 
         @return leftElevationView (@link PlanElevationView NXOpen.AECDesign.PlanElevationView@endlink): .
        """
        pass
    
    ##  Gets the level view. 
    ##  @return levelView (@link PlanElevationView NXOpen.AECDesign.PlanElevationView@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="levelName"> (str) </param>
    ## <param name="viewType"> (@link PlanElevationViewManager.LevelViewType NXOpen.AECDesign.PlanElevationViewManager.LevelViewType@endlink) </param>
    def GetLevelView(manager: PlanElevationViewManager, levelName: str, viewType: PlanElevationViewManager.LevelViewType) -> PlanElevationView:
        """
         Gets the level view. 
         @return levelView (@link PlanElevationView NXOpen.AECDesign.PlanElevationView@endlink): .
        """
        pass
    
    ##  Gets the near elevation view. 
    ##  @return nearElevationView (@link PlanElevationView NXOpen.AECDesign.PlanElevationView@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def GetNearElevationView(manager: PlanElevationViewManager) -> PlanElevationView:
        """
         Gets the near elevation view. 
         @return nearElevationView (@link PlanElevationView NXOpen.AECDesign.PlanElevationView@endlink): .
        """
        pass
    
    ##  Gets the plan view. 
    ##  @return planView (@link PlanElevationView NXOpen.AECDesign.PlanElevationView@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def GetPlanView(manager: PlanElevationViewManager) -> PlanElevationView:
        """
         Gets the plan view. 
         @return planView (@link PlanElevationView NXOpen.AECDesign.PlanElevationView@endlink): .
        """
        pass
    
    ##  Gets the right elevation view. 
    ##  @return rightElevationView (@link PlanElevationView NXOpen.AECDesign.PlanElevationView@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def GetRightElevationView(manager: PlanElevationViewManager) -> PlanElevationView:
        """
         Gets the right elevation view. 
         @return rightElevationView (@link PlanElevationView NXOpen.AECDesign.PlanElevationView@endlink): .
        """
        pass
    
    ##  Updates the section views of all levels. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def UpdateSectionViews(manager: PlanElevationViewManager) -> None:
        """
         Updates the section views of all levels. 
        """
        pass
    
import NXOpen
##  Represents AECDesign Plan Elevation View  <br> This class is sub-object of PlanElevationViewManager, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class PlanElevationView(NXOpen.NXObject): 
    """ Represents AECDesign Plan Elevation View """


    ## Getter for property: (bool) Clip
    ##   the flag to indicate whether or not to clip the view.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def Clip(self) -> bool:
        """
        Getter for property: (bool) Clip
          the flag to indicate whether or not to clip the view.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Clip

    ##   the flag to indicate whether or not to clip the view.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Clip.setter
    def Clip(self, clip: bool):
        """
        Setter for property: (bool) Clip
          the flag to indicate whether or not to clip the view.  
             
         
        """
        pass
    
    ## Getter for property: (bool) LockDirection
    ##   the flag to indicate whether or not to lock the view direction.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def LockDirection(self) -> bool:
        """
        Getter for property: (bool) LockDirection
          the flag to indicate whether or not to lock the view direction.  
            
         
        """
        pass
    
    ## Setter for property: (bool) LockDirection

    ##   the flag to indicate whether or not to lock the view direction.  
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @LockDirection.setter
    def LockDirection(self, lockDirection: bool):
        """
        Setter for property: (bool) LockDirection
          the flag to indicate whether or not to lock the view direction.  
            
         
        """
        pass
    
    ## Getter for property: (float) Scale
    ##   the scale of the view.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
          the scale of the view.  
             
         
        """
        pass
    
    ## Setter for property: (float) Scale

    ##   the scale of the view.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
          the scale of the view.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowCrossHatching
    ##   the flag to indicate whether or not to show cross hatching.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ShowCrossHatching(self) -> bool:
        """
        Getter for property: (bool) ShowCrossHatching
          the flag to indicate whether or not to show cross hatching.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowCrossHatching

    ##   the flag to indicate whether or not to show cross hatching.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ShowCrossHatching.setter
    def ShowCrossHatching(self, showCrossHatching: bool):
        """
        Setter for property: (bool) ShowCrossHatching
          the flag to indicate whether or not to show cross hatching.  
             
         
        """
        pass
    
    ## Getter for property: (str) ViewName
    ##   the view name  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def ViewName(self) -> str:
        """
        Getter for property: (str) ViewName
          the view name  
            
         
        """
        pass
    
    ## Setter for property: (str) ViewName

    ##   the view name  
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ViewName.setter
    def ViewName(self, viewName: str):
        """
        Setter for property: (str) ViewName
          the view name  
            
         
        """
        pass
    
    ##  Makes the view active. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def MakeActive(planElevationView: PlanElevationView) -> None:
        """
         Makes the view active. 
        """
        pass
    
    ##  Resets the orientation of the view
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def ResetOrientation(planElevationView: PlanElevationView) -> None:
        """
         Resets the orientation of the view
        """
        pass
    
## @package NXOpen.AECDesign
## Classes, Enums and Structs under NXOpen.AECDesign namespace

##  @link PlanElevationViewManagerLevelViewType NXOpen.AECDesign.PlanElevationViewManagerLevelViewType @endlink is an alias for @link PlanElevationViewManager.LevelViewType NXOpen.AECDesign.PlanElevationViewManager.LevelViewType@endlink
PlanElevationViewManagerLevelViewType = PlanElevationViewManager.LevelViewType


