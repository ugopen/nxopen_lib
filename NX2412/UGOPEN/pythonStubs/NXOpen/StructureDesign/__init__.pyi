from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Assemblies
import NXOpen.ShipDesign
class ContextMenu(NXOpen.Object): 
    """ Represents the interface for Context Menu """
    class DisplayColorType(Enum):
        """
        Members Include: 
         |ShowStock|  show stock color 
         |ShowWeld|  show weld color 

        """
        ShowStock: int
        ShowWeld: int
        @staticmethod
        def ValueOf(value: int) -> ContextMenu.DisplayColorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def DeleteWeldmentNode(tWeldmentNode: NXOpen.ShipDesign.NavigatorNode, index: int) -> None:
        """
         Deletes weldment node under consolidate list. 
        """
        pass
    def PackMemberNodes(tgNodes: List[NXOpen.ShipDesign.NavigatorNode], tgStructurePart: NXOpen.Assemblies.Component) -> None:
        """
         Packs members in navigator for structure design 
        """
        pass
    def RemoveConsolidateList(consolidateListNodeTag: NXOpen.ShipDesign.NavigatorNode) -> None:
        """
         Remove consolidate list components and navigator node 
        """
        pass
    def RemoveFeaturesInsideBoltedConnectionComponents(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes bolted Connection feature inside the components. 
        """
        pass
    def RemoveFeaturesInsideEndCapComponents(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes End Cap feature inside the components. 
        """
        pass
    def RemoveFeaturesInsideMemberComponents(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes Member feature inside the components. 
        """
        pass
    def RemoveFeaturesInsideMountingFeetComponents(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes Mounting Feet feature inside the components. 
        """
        pass
    def RemoveFeaturesInsidePadComponents(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes pad feature inside the components. 
        """
        pass
    def RemoveFeaturesInsideStiffenerComponents(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes stiffener feature inside the components. 
        """
        pass
    def RemoveFromConsolidateList(tgNodes: List[NXOpen.ShipDesign.NavigatorNode]) -> None:
        """
         Remove external component from consolidate list. 
        """
        pass
    def ReparentPartNodes(index: int, tgTargetNode: NXOpen.ShipDesign.NavigatorNode, tgNodes: List[NXOpen.ShipDesign.NavigatorNode]) -> None:
        """
         Reparents part node under consolidate list. 
        """
        pass
    def UnpackMemberNodes(tgNodes: List[NXOpen.ShipDesign.NavigatorNode], tgStructurePart: NXOpen.Assemblies.Component) -> None:
        """
         Unpacks members in navigator for structure design 
        """
        pass
    def UpdateDisplayColorType(displayType: ContextMenu.DisplayColorType) -> None:
        """
        Show or clear physics color.  
        """
        pass
    def UpdateStructure(curves: List[NXOpen.NXObject]) -> None:
        """
          Updates attributes on the structure curves or edges. 
        """
        pass
import NXOpen
class EditDimensionValueBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.StructureDesign.EditDimensionValueBuilder """
    @property
    def ActiveHandleIndex(self) -> int:
        """
        Getter for property: (int) ActiveHandleIndex
         Returns the active handle index   
            
         
        """
        pass
    @ActiveHandleIndex.setter
    def ActiveHandleIndex(self, handleIndex: int):
        """
        Setter for property: (int) ActiveHandleIndex
         Returns the active handle index   
            
         
        """
        pass
    @property
    def DimValue(self) -> float:
        """
        Getter for property: (float) DimValue
         Returns the dimension value   
            
         
        """
        pass
    @DimValue.setter
    def DimValue(self, dimValue: float):
        """
        Setter for property: (float) DimValue
         Returns the dimension value   
            
         
        """
        pass
    @property
    def InDragging(self) -> bool:
        """
        Getter for property: (bool) InDragging
         Returns the dragging mode.  
             
         
        """
        pass
    @InDragging.setter
    def InDragging(self, isInDragging: bool):
        """
        Setter for property: (bool) InDragging
         Returns the dragging mode.  
             
         
        """
        pass
    @property
    def InPreview(self) -> bool:
        """
        Getter for property: (bool) InPreview
         Returns the preview mode.  
             
         
        """
        pass
    @InPreview.setter
    def InPreview(self, isInPreview: bool):
        """
        Setter for property: (bool) InPreview
         Returns the preview mode.  
             
         
        """
        pass
    def ApplyEdit(self) -> None:
        """
         Applys dimension editing. 
        """
        pass
import NXOpen
import NXOpen.Features.StructureDesign
class Frame3DManager(NXOpen.Object): 
    """
        Represents the Frame3D context manager associated with a session.
    """
    class CommandTypes(Enum):
        """
        Members Include: 
         |NotSet| 
         |Frame3D| 
         |Line| 
         |Rectangle| 
         |Box| 
         |Plane| 
         |StructureBasic| 
         |StructureSupport| 
         |StructureLevels| 
         |Member| 

        """
        NotSet: int
        Frame3D: int
        Line: int
        Rectangle: int
        Box: int
        Plane: int
        StructureBasic: int
        StructureSupport: int
        StructureLevels: int
        Member: int
        @staticmethod
        def ValueOf(value: int) -> Frame3DManager.CommandTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActiveCommand(self) -> Frame3DManager.CommandTypes:
        """
        Getter for property: ( Frame3DManager.CommandTypes NXOpen.Str) ActiveCommand
         Returns the active Frame3D command.  
             
         
        """
        pass
    @ActiveCommand.setter
    def ActiveCommand(self, type: Frame3DManager.CommandTypes):
        """
        Setter for property: ( Frame3DManager.CommandTypes NXOpen.Str) ActiveCommand
         Returns the active Frame3D command.  
             
         
        """
        pass
    @property
    def ActiveFeature(self) -> NXOpen.Features.StructureDesign.IFrame:
        """
        Getter for property: ( NXOpen.Features.StructureDesign.IFrame) ActiveFeature
         Returns the active Frame3D feature.  
             
         
        """
        pass
    @ActiveFeature.setter
    def ActiveFeature(self, feature: NXOpen.Features.StructureDesign.IFrame):
        """
        Setter for property: ( NXOpen.Features.StructureDesign.IFrame) ActiveFeature
         Returns the active Frame3D feature.  
             
         
        """
        pass
    @property
    def FrameVertexCollection() -> FrameVertexCollection:
        """
         FrameVertex collection 
        """
        pass
    def ClearCachedGeometry() -> None:
        """
         Clears cached geometry. 
        """
        pass
    def Edit(feature: NXOpen.Features.StructureDesign.IFrame) -> None:
        """
         Sets the frame to be edited and marks the feature to be in edit mode. 
        """
        pass
    def Enter() -> None:
        """
         Starts the Frame3D command.
                    This method should not be called if already in the Frame3D command.
                
        """
        pass
    def Exit() -> None:
        """
         Ends the Frame3D state.
                
        """
        pass
    def ResizeFrameDimension() -> None:
        """
         Resizes frame dimensions. 
        """
        pass
    def SetCancelled() -> None:
        """
         Marks the command to be cancelled such that during Frame3DManager.Exit
                    command is undone and all the changes are discarded.
                
        """
        pass
    def ShowFrameMember(bCreateMember: bool, bUpdateFeature: bool) -> None:
        """
         Shows frame members in solid. 
        """
        pass
import NXOpen.Annotations
class FrameRapidDimensionBuilder(NXOpen.Annotations.BaseRapidDimensionBuilder): 
    """ Represents a NXOpen.StructureDesign.FrameRapidDimensionBuilder """
    @property
    def Driving(self) -> NXOpen.Annotations.DrivingValueBuilder:
        """
        Getter for property: ( NXOpen.Annotations.DrivingValueBuilder) Driving
         Returns the driving   
            
         
        """
        pass
    @property
    def ForeshorteningSymbol(self) -> NXOpen.Annotations.ForeshorteningSymbolBuilder:
        """
        Getter for property: ( NXOpen.Annotations.ForeshorteningSymbolBuilder) ForeshorteningSymbol
         Returns the foreshortening symbol builder   
            
         
        """
        pass
import NXOpen
import NXOpen.Features.StructureDesign
class FrameTaskEnvironment(NXOpen.Object): 
    """
        Represents the Frame task environment associated with a session.
    """
    @property
    def ActiveFeature(self) -> NXOpen.Features.StructureDesign.SuperFrame:
        """
        Getter for property: ( NXOpen.Features.StructureDesign.SuperFrame) ActiveFeature
         Returns the active SuperFrame feature.  
             
         
        """
        pass
    @ActiveFeature.setter
    def ActiveFeature(self, feature: NXOpen.Features.StructureDesign.SuperFrame):
        """
        Setter for property: ( NXOpen.Features.StructureDesign.SuperFrame) ActiveFeature
         Returns the active SuperFrame feature.  
             
         
        """
        pass
    @property
    def BaseType(self) -> NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes:
        """
        Getter for property: ( NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes) BaseType
         Returns the active base type for the Frame command.  
             
         
        """
        pass
    @BaseType.setter
    def BaseType(self, type: NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes):
        """
        Setter for property: ( NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes) BaseType
         Returns the active base type for the Frame command.  
             
         
        """
        pass
    @property
    def TransformType(self) -> NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes:
        """
        Getter for property: ( NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes) TransformType
         Returns the active transform type for the MoveCopy Curve commands.  
             
         
        """
        pass
    @TransformType.setter
    def TransformType(self, type: NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes):
        """
        Setter for property: ( NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes) TransformType
         Returns the active transform type for the MoveCopy Curve commands.  
             
         
        """
        pass
    def Edit(feature: NXOpen.Features.StructureDesign.SuperFrame) -> None:
        """
         Sets the frame to be edited and marks the task to be in edit mode. 
        """
        pass
    def Enter() -> None:
        """
         Starts the Frame task environment.
                    This method should not be called if already in the Frame task environment.
                
        """
        pass
    def Exit() -> None:
        """
         Ends the Frame task environment.
                
        """
        pass
    def SetCancelled() -> None:
        """
         Marks the task to be cancelled such that during FrameTaskEnvironment.Exit
                    task is undone and all the changes are discarded.
                
        """
        pass
import NXOpen
class FrameVertexCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of FrameVertex """
    def FindObject(self, sid: str) -> FrameVertex:
        """
         Finds the NXOpen.StructureDesign.FrameVertex object with the given sid. 
         Returns found ( FrameVertex NXOpen.Str):  NXOpen.StructureDesign.FrameVertex object with this sid. .
        """
        pass
import NXOpen
class FrameVertex(NXOpen.NXObject): 
    """
        Represents the Frame vertex associated with a Frame curve.
    """
    class CurvePlacementType(Enum):
        """
        Members Include: 
         |NotSet|  Vertex not on a curve  
         |Start|  Vertex at start of curve 
         |End|  Vertex at end of curve 

        """
        NotSet: int
        Start: int
        End: int
        @staticmethod
        def ValueOf(value: int) -> FrameVertex.CurvePlacementType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
import NXOpen
class StructureDesignNavigatorRoot(NXOpen.NXObject): 
    """ Represents the interface for structure design navigator root classes. """
    pass
import NXOpen
import NXOpen.Features.StructureDesign
class StructureDesignSession(NXOpen.Object): 
    """ Represents StructureDesign session """
    @property
    def ContextMenu() -> ContextMenu:
        """
         Returns the  NXOpen::StructureDesign::ContextMenu  belonging to this session 
        """
        pass
    def AskCornerObjects(memberBody: NXOpen.Body) -> List[NXOpen.Features.StructureDesign.Corner]:
        """
         Get related corner objects from a member body
         Returns corners ( NXOpen.Features.StructureDesign.Corner Li): .
        """
        pass
    def AskMembers(corner: NXOpen.Features.StructureDesign.Corner) -> List[NXOpen.Body]:
        """
         Get related member bodies from a corner object
         Returns members ( NXOpen.Body Li): .
        """
        pass
    def GetStructureDesignNavigatorRoot() -> StructureDesignNavigatorRoot:
        """
         Establish structure design navigator root 
         Returns navRoot ( StructureDesignNavigatorRoot NXOpen.Str):  .
        """
        pass
