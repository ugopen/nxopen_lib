from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Features.Industry
class AECDesignNavigatorNode(NXOpen.Features.Industry.IndustryNavigatorNode): 
    """ Represents the interface for navigator node classes"""
    def ChangeNodeState(self, status: int) -> None:
        """
         Changes node show and hide state. 
        """
        pass
    def GetNodeObjects(self) -> List[NXOpen.TaggedObject]:
        """
         The objects represented by the node. 
         Returns nodeObjects ( NXOpen.TaggedObject Li): .
        """
        pass
    def SetNodeObjects(self, nodeObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the objects represented by the node. 
        """
        pass
import NXOpen
class AECDesignNavigatorRoot(NXOpen.NXObject): 
    """ Represents the interface for AEC design navigator root classes. """
    pass
import NXOpen
class AECDesignNavigatorView(NXOpen.NXObject): 
    """ Represents the interface for navigator view classe"""
    def AddRootNode(self, name: str, nodeObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Adds a root object to the navigator to represent the object. 
        """
        pass
    def GetRootNode(self) -> AECDesignNavigator:
        """
         Gets root node. 
         Returns rootNode ( AECDesignNavigator NXOpen.): .
        """
        pass
    def GetSelectedNodes(self) -> List[AECDesignNavigator]:
        """
         Gets selected nodes. 
         Returns selectedNodes ( AECDesignNavigator List[NXOpe): .
        """
        pass
    def RemoveRootNode(self) -> None:
        """
         Removes root node. 
        """
        pass
    def SetSelectedNodes(self, selectedNodes: List[AECDesignNavigator]) -> None:
        """
         Sets selected nodes. 
        """
        pass
import NXOpen
class AECDesignNavigator(NXOpen.NXObject): 
    """ Represents the interface for navigator action classes"""
    def Hide(self) -> None:
        """
         Hides a navigator. 
        """
        pass
    def HideView(self, viewIndex: int) -> None:
        """
         Hides a navigator view. 
        """
        pass
    def ShowView(self, viewIndex: int) -> None:
        """
         Shows a navigator view. 
        """
        pass
import NXOpen
import NXOpen.Annotations
import NXOpen.Features.AECDesign
class AECDesignSession(NXOpen.Object): 
    """ Represents AECDesign session """
    @property
    def ActiveLevelName(self) -> str:
        """
        Getter for property: (str) ActiveLevelName
         Returns the active level name  
            
         
        """
        pass
    @ActiveLevelName.setter
    def ActiveLevelName(self, activeLevel: str):
        """
        Setter for property: (str) ActiveLevelName
         Returns the active level name  
            
         
        """
        pass
    @property
    def LevelContainer(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) LevelContainer
         Returns the level container  
            
         
        """
        pass
    @LevelContainer.setter
    def LevelContainer(self, levelContainer: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) LevelContainer
         Returns the level container  
            
         
        """
        pass
    @property
    def PlanElevationViewManager(self) -> PlanElevationViewManager:
        """
        Getter for property: ( PlanElevationViewManager NXOpen.) PlanElevationViewManager
         Returns the plan elevation view manager  
            
         
        """
        pass
    def AddCurvesToGridLine(tgSketch: NXOpen.Sketch, curves: List[NXOpen.Curve]) -> None:
        """
         Add Curves to grid line 
        """
        pass
    def ChangeLineEndToggleState(tgToggle: NXOpen.Annotations.Annotation) -> None:
        """
         Changes the state of AEC line format toggle
        """
        pass
    def CreateGrid() -> NXOpen.Features.AECDesign.Grid:
        """
         Starts grid creation 
         Returns pTgGirdFrec ( NXOpen.Features.AECDesign.Grid): .
        """
        pass
    def DeleteObjectsForGridLevel(tgSketch: NXOpen.Sketch, objects: List[NXOpen.NXObject]) -> None:
        """
         Deletes objects for grid or level 
        """
        pass
    def EnableAECLineElbow(tgElbow: NXOpen.Annotations.Annotation) -> None:
        """
         Enables AEC line format elbow
        """
        pass
    def FinishGridTask(tgGridFrec: NXOpen.Features.AECDesign.Grid) -> None:
        """
         Finishes grid task 
        """
        pass
    def FinishLastAECLineFormat() -> None:
        """
         Finishes the last AEC line format
        """
        pass
    def FinishLevelCreation(level: NXOpen.Features.AECDesign.Level) -> None:
        """
         Finishes level creation 
        """
        pass
    def GetAECDesignNavigatorRoot() -> AECDesignNavigatorRoot:
        """
         Establish aec design navigator root 
         Returns navRoot ( AECDesignNavigatorRoot NXOpen.):  .
        """
        pass
    def GetActiveLevelPositionAndHeight() -> Tuple[float, float]:
        """
         Gets the position and height of active level
         Returns A tuple consisting of (levelPosition, levelHeight). 
         - levelPosition is: float.
         - levelHeight is: float.

        """
        pass
    def GetLevelNames() -> List[str]:
        """
         Get names for all the levels
         Returns levelNames (List[str]): .
        """
        pass
    def LevelSketchEnd() -> None:
        """
         Exits the Sketch environment. 
        """
        pass
    def OnExitApplication() -> None:
        """
         On exiting the BIM Design application
        """
        pass
    def SetLastSavedCurvesInGridTask(tgSketch: NXOpen.Sketch, curves: List[NXOpen.Curve]) -> None:
        """
         Set Curves to last saved curves in grid task 
        """
        pass
    def SetLastSavedEntitesInGridTask(tgSketch: NXOpen.Sketch, entites: List[NXOpen.NXObject]) -> None:
        """
         Sets entites as the last saved entites in the grid task. 
        """
        pass
    def SetMultiSegmentToggleOff() -> None:
        """
         Set multi-segment toggle off 
        """
        pass
    def SetMultiSegmentToggleOn() -> None:
        """
         Set multi-segment toggle on 
        """
        pass
    def SetOnlySelfOriginBaseLine(tgBaseLine: NXOpen.Annotations.AECDesignBaseLine, x: float, y: float, z: float) -> None:
        """
         Sets the origin for the BIM line. It will not move the BIM line.
        """
        pass
    def SetStateOfInLevelUpdate(bInLevelUpdate: bool) -> None:
        """
         Sets the state of in the level update.
        """
        pass
    def StartEditAECLineFormat(tgAECLine: NXOpen.NXObject) -> None:
        """
         Starts to edit AEC line format
        """
        pass
    def StartGridTask(tgGridFrec: NXOpen.Features.AECDesign.Grid) -> None:
        """
         Starts grid task 
        """
        pass
    def StartLevelCreation(level: NXOpen.Features.AECDesign.Level) -> None:
        """
         Starts level creation 
        """
        pass
    def UpdateAndRegenAllSymbolsForBaseLine(tgBaseLine: NXOpen.Annotations.AECDesignBaseLine) -> None:
        """
         Updates and regenerates all symbols for base line.
        """
        pass
    def UpdateDimensionsOfBIMCurves(tgSketch: NXOpen.Sketch, baseCurves: List[NXOpen.Annotations.AECDesignBaseLine]) -> bool:
        """
         Updates dimensions of BIM curves 
         Returns bHaveDimension (bool): .
        """
        pass
class AecGridCenterSegmentType(Enum):
    """
    Members Include: 
     |Continuous|  The CFW of center segment is same with the end segment
     |NotSet|  Hide the center segment
     |Custom|  The center segment have its own Color Font and Width

    """
    Continuous: int
    NotSet: int
    Custom: int
    @staticmethod
    def ValueOf(value: int) -> AecGridCenterSegmentType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AecLineFormatDragPointType(Enum):
    """
    Members Include: 
     |EndPoint|  The drag point in the end point of AEC line
     |GapPoint|  The drag point in the AEC line
     |ElbowFirst|  The drag point in end point of the first elbow segments
     |ElbowSecond|  The drag point in the point of the second elbow segments

    """
    EndPoint: int
    GapPoint: int
    ElbowFirst: int
    ElbowSecond: int
    @staticmethod
    def ValueOf(value: int) -> AecLineFormatDragPointType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AecLineFormatType(Enum):
    """
    Members Include: 
     |Elbow|  AEC line format of elbow
     |EndSymbolToggle|  AEC line format of end symbol toggle
     |DragPoint|  AEC line format of drag point

    """
    Elbow: int
    EndSymbolToggle: int
    DragPoint: int
    @staticmethod
    def ValueOf(value: int) -> AecLineFormatType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AecLineType(Enum):
    """
    Members Include: 
     |Unknown|  unknow AEC Line type
     |GridLine|  grid line
     |LevelLine|  level line
     |Level3dLine|  level 3D line

    """
    Unknown: int
    GridLine: int
    LevelLine: int
    Level3dLine: int
    @staticmethod
    def ValueOf(value: int) -> AecLineType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AecSymbolType(Enum):
    """
    Members Include: 
     |Unknown|  unknow AECSymbol type
     |GridEndNote|  grid end note type AECSymbol
     |LevelEndNote|  level end note type AECSymbol

    """
    Unknown: int
    GridEndNote: int
    LevelEndNote: int
    @staticmethod
    def ValueOf(value: int) -> AecSymbolType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AecTaskEnvType(Enum):
    """
    Members Include: 
     |NotSet|  not in AEC task enviroment
     |Grid|  AEC grid task enviroment
     |Level|  AEC level task enviroment

    """
    NotSet: int
    Grid: int
    Level: int
    @staticmethod
    def ValueOf(value: int) -> AecTaskEnvType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class LevelSymbolIndex(Enum):
    """
    Members Include: 
     |Height|  height index in the level symbol
     |LevelName|  level name index in the level symbol

    """
    Height: int
    LevelName: int
    @staticmethod
    def ValueOf(value: int) -> LevelSymbolIndex:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class PlanElevationViewManager(NXOpen.NXObject): 
    """ Represents AECDesign Plan Elevation View Manager """
    class LevelViewType(Enum):
        """
        Members Include: 
         |FloorView| 
         |CeilingView| 

        """
        FloorView: int
        CeilingView: int
        @staticmethod
        def ValueOf(value: int) -> PlanElevationViewManager.LevelViewType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetFrontElevationView(self) -> PlanElevationView:
        """
         Gets the front elevation view.
         Returns frontElevationView ( PlanElevationView NXOpen.): .
        """
        pass
    def GetLeftElevationView(self) -> PlanElevationView:
        """
         Gets the left elevation view. 
         Returns leftElevationView ( PlanElevationView NXOpen.): .
        """
        pass
    def GetLevelView(self, levelName: str, viewType: PlanElevationViewManager.LevelViewType) -> PlanElevationView:
        """
         Gets the level view. 
         Returns levelView ( PlanElevationView NXOpen.): .
        """
        pass
    def GetNearElevationView(self) -> PlanElevationView:
        """
         Gets the near elevation view. 
         Returns nearElevationView ( PlanElevationView NXOpen.): .
        """
        pass
    def GetPlanView(self) -> PlanElevationView:
        """
         Gets the plan view. 
         Returns planView ( PlanElevationView NXOpen.): .
        """
        pass
    def GetRightElevationView(self) -> PlanElevationView:
        """
         Gets the right elevation view. 
         Returns rightElevationView ( PlanElevationView NXOpen.): .
        """
        pass
    def UpdateSectionViews(self) -> None:
        """
         Updates the section views of all levels. 
        """
        pass
import NXOpen
class PlanElevationView(NXOpen.NXObject): 
    """ Represents AECDesign Plan Elevation View """
    @property
    def Clip(self) -> bool:
        """
        Getter for property: (bool) Clip
         Returns the flag to indicate whether or not to clip the view.  
             
         
        """
        pass
    @Clip.setter
    def Clip(self, clip: bool):
        """
        Setter for property: (bool) Clip
         Returns the flag to indicate whether or not to clip the view.  
             
         
        """
        pass
    @property
    def LockDirection(self) -> bool:
        """
        Getter for property: (bool) LockDirection
         Returns the flag to indicate whether or not to lock the view direction.  
            
         
        """
        pass
    @LockDirection.setter
    def LockDirection(self, lockDirection: bool):
        """
        Setter for property: (bool) LockDirection
         Returns the flag to indicate whether or not to lock the view direction.  
            
         
        """
        pass
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the scale of the view.  
             
         
        """
        pass
    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the scale of the view.  
             
         
        """
        pass
    @property
    def ShowCrossHatching(self) -> bool:
        """
        Getter for property: (bool) ShowCrossHatching
         Returns the flag to indicate whether or not to show cross hatching.  
             
         
        """
        pass
    @ShowCrossHatching.setter
    def ShowCrossHatching(self, showCrossHatching: bool):
        """
        Setter for property: (bool) ShowCrossHatching
         Returns the flag to indicate whether or not to show cross hatching.  
             
         
        """
        pass
    @property
    def ViewName(self) -> str:
        """
        Getter for property: (str) ViewName
         Returns the view name  
            
         
        """
        pass
    @ViewName.setter
    def ViewName(self, viewName: str):
        """
        Setter for property: (str) ViewName
         Returns the view name  
            
         
        """
        pass
    def MakeActive(self) -> None:
        """
         Makes the view active. 
        """
        pass
    def ResetOrientation(self) -> None:
        """
         Resets the orientation of the view
        """
        pass
