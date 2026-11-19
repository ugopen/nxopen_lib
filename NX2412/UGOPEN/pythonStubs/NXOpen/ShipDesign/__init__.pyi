from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ApplicationUtils(NXOpen.Object): 
    """ Represents Generator which wrap the ship api for china """
    def RegisterApplicationForModlFeatureEdit(appName: str) -> None:
        """
         Register button in other application 
        """
        pass
    def RegisterApplicationSensitivityOnApplicationChange(appName: str, appsWhereToLive: List[str]) -> None:
        """
         Register application sensitivity when the application is changed 
        """
        pass
    def RegisterButtonApplication(appId: int, buttonName: str) -> None:
        """
         Register button in other application 
        """
        pass
    def RegisterLastApplication(part: NXOpen.Part, appName: str) -> None:
        """
         Register the last application of the part 
        """
        pass
import NXOpen
class GeneralArrangementManager(NXOpen.Object): 
    """ Represents the interface for General Arrangement classes """
    def CreateSkecthRectangle(sketch: NXOpen.Sketch) -> None:
        """
         Creates the rectangle for Deck Plan sketch. 
        """
        pass
    def CreateWaveLinkPlane(srPlane: NXOpen.TaggedObject) -> NXOpen.TaggedObject:
        """
         Creates the wave plane for src plane . 
         Returns dstPlane ( NXOpen.TaggedObject): .
        """
        pass
    def EditRoomCallBack() -> None:
        """
         Add callback EditRoomCallBack 
        """
        pass
    def GASketchEnd() -> None:
        """
         Exits the Sketch environment under General Arrangement application. 
        """
        pass
    def MakeContainerPart(part: NXOpen.Part) -> None:
        """
         Makes the part to be Ship Container. 
        """
        pass
    def ReloadMaterialData(bShip: bool) -> None:
        """
        Reload the material data.
        """
        pass
    def RemoveSketchFromMoldRefSet(sketch: NXOpen.TaggedObject) -> None:
        """
         Remove the sketch objects from the model reference set 
        """
        pass
    def RemoveUnusedExpression() -> None:
        """
        Removes all unused expressions in the general arrangement deck reference part.
        """
        pass
    def ResizeGrid() -> None:
        """
         Resizes the ship grid datum. 
        """
        pass
    def WaveLinkFrameBarToDeckRefPart() -> None:
        """
         WaveLinkFrameBarToDeckRefPart. 
        """
        pass
import NXOpen
class Generator(NXOpen.Object): 
    """ Represents Generator which wrap the ship api for china """
    class ClashType(Enum):
        """
        Members Include: 
         |NotSet|  There is no clash between two bodies. 
         |AInB|  Body a is completly in body b, without abut. 
         |BInA|  Body b is completly in body a, without abut. 
         |Exists| Clash exists; only this is requested. 
         |AbutNoClass|  Bounding topologies abut, inoutside unknown. 
         |AbutBInA|  Bounding b topology abuts bounding a topology on the inside. 
         |AbutBOutA|  Bounding b topology abuts bounding a topology on the outside. 
         |Interfere|  Bounding topologies interfere. 

        """
        NotSet: int
        AInB: int
        BInA: int
        Exists: int
        AbutNoClass: int
        AbutBInA: int
        AbutBOutA: int
        Interfere: int
        @staticmethod
        def ValueOf(value: int) -> Generator.ClashType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AdvanceProgress(stepNumber: int) -> None:
        """
         Advances the progress bar. 
        """
        pass
    def AskIntersectionPlates(plate: NXOpen.TaggedObject, inSheets: List[NXOpen.TaggedObject], tolerence: float) -> List[NXOpen.TaggedObject]:
        """
         Gets all intersected plates with the given plates. 
         Returns outElements ( NXOpen.TaggedObject Li): .
        """
        pass
    def AskPlatesSpatialRelations(hull: NXOpen.TaggedObject, inSheets: List[NXOpen.TaggedObject], tolerence: float) -> Tuple[List[int], List[NXOpen.TaggedObject]]:
        """
         Gets the spatial relations of the plates based on its positions. 
         Returns A tuple consisting of (elementIndex, outElements). 
         - elementIndex is: List[int].
         - outElements is:  NXOpen.TaggedObject Li.

        """
        pass
    def CheckAssemblyCircularReferences() -> None:
        """
         Check assembly circular references. 
        """
        pass
    def CheckBodyClash(body_a: NXOpen.DisplayableObject, body_b: NXOpen.DisplayableObject) -> Generator.ClashType:
        """
         Check the clash between two bodys. 
         Returns clash_status ( Generator.ClashType NXOpen.S):  O: clash status for body a and body b .
        """
        pass
    def CreateCargo(inSheets: List[NXOpen.TaggedObject], tolerence: float) -> List[NXOpen.TaggedObject]:
        """
         Creates the ship cargo body based on the input boundary sheets. 
         Returns outElements ( NXOpen.TaggedObject Li): .
        """
        pass
    def CreateProgress(numSteps: int, operationName: str) -> None:
        """
         Creates a progress bar with given title and number of total steps. 
        """
        pass
    def DeleteProgress() -> None:
        """
         Deletes the progress bar. 
        """
        pass
    def GetOutlineSheetbody(bodies: List[NXOpen.Body], datum_plane: NXOpen.DatumPlane) -> NXOpen.Body:
        """
         Get the outline sheet body of input bodies. 
         Returns outline_body ( NXOpen.Body):  O: output outline sheet body .
        """
        pass
    def GetSheetsEdgesLaidOnTargetSheet(outSheet: NXOpen.TaggedObject, inSheets: List[NXOpen.TaggedObject], tolerence: float) -> List[NXOpen.TaggedObject]:
        """
         Gets the edges of tool sheet bodies which are laid on a target sheet body 
         Returns outElements ( NXOpen.TaggedObject Li): .
        """
        pass
    ShipCustomerEnterApplication = Callable[[], None]
    ShipCustomerExitApplication = Callable[[], None]
    def RegisterApplicationCallback(name: str, enterCallback: Generator.ShipCustomerEnterApplication, exitCallback: Generator.ShipCustomerExitApplication) -> None:
        """
         Register application callback when application is entered or exited. It is specific for ship customers. 
        """
        pass
import NXOpen
import NXOpen.Features
class NavigatorCollection(NXOpen.Object): 
    """ Represents the interface for navigator action classes"""
    def ActiveNavigator(index: int) -> None:
        """
         Actives ship navigator. 
        """
        pass
    def ChangeNodeState(tgTargetNode: NavigatorNode, status: int) -> None:
        """
         Change node state. 
        """
        pass
    def ChangeNodesState(tgNodes: List[NavigatorNode], status: int) -> None:
        """
         Change nodes state. 
        """
        pass
    def CopyNode(index: int, tgNodes: List[NavigatorNode]) -> None:
        """
         Copy navigator node. 
        """
        pass
    def CreateShipNavigatorNodeBuilder(isEdit: bool, tgNode: NavigatorNode) -> ShipNavigatorNodeBuilder:
        """
         Creates a NXOpen.ShipDesign.ShipNavigatorNodeBuilder. 
         Returns builder ( ShipNavigatorNodeBuilder NXOpen.S): .
        """
        pass
    def CutNode(index: int, tgNodes: List[NavigatorNode]) -> None:
        """
         Cut navigator node. 
        """
        pass
    def DecrementIgnoreNavigatorViewUpdateEventsLevel(index: int) -> None:
        """
         Decrease ignore navigator view update events level and update navigator views
        """
        pass
    def EditFeature(tgFeat: NXOpen.Features.Feature) -> None:
        """
         Edit feature. 
        """
        pass
    def EnterSketchEnvironment(sketch_feature: NXOpen.Features.SketchFeature) -> None:
        """
         Enter sketch environment by edit 
        """
        pass
    def GetNavigator(index: int) -> Navigator:
        """
         Gets ship navigator. 
         Returns navigator ( Navigator NXOpen.S): .
        """
        pass
    def GetNavigatorCount() -> int:
        """
         Gets navigator count. 
         Returns count (int): .
        """
        pass
    def GetReferencingNodes(tgReferencedObject: NXOpen.TaggedObject) -> List[NavigatorNode]:
        """
         Gets all referencing navigator nodes. 
         Returns referencingNodes ( NavigatorNode List[NXOpen): .
        """
        pass
    def GetShipNavigatorRoot() -> ShipNavigatorRoot:
        """
         Establish ship navigator root 
         Returns navRoot ( ShipNavigatorRoot NXOpen.S):  .
        """
        pass
    def IncrementIgnoreNavigatorViewUpdateEventsLevel(index: int) -> None:
        """
         Increase ignore navigator view update events level 
        """
        pass
    def IsNavigatorRegistered(index: int) -> bool:
        """
         Checks if ship navigator is registered. 
         Returns isNavigatorRegistered (bool): .
        """
        pass
    def PasteNode(index: int, tgTargetNode: NavigatorNode) -> None:
        """
         Paste navigator node. 
        """
        pass
    def PopulateAndPrintShipNavigator(displayPart: NXOpen.BasePart) -> None:
        """
         Populates and prints data for each navigator found. 
        """
        pass
    def RefreshNavigator(index: int) -> None:
        """
         Loads navigator models. 
        """
        pass
    def RegisterNavigator(index: int, bitmap: str, tooltip: str, name: str) -> None:
        """
         Registers the navigator. 
        """
        pass
    def RemoveNodes(index: int, tgNodes: List[NavigatorNode]) -> None:
        """
         Remove navigator nodes. 
        """
        pass
    def ReparentNode(index: int, tgTargetNode: NavigatorNode, tgSourceNode: NavigatorNode) -> None:
        """
         Reparent navigator node. 
        """
        pass
    def ReparentNodes(index: int, tgTargetNode: NavigatorNode, tgNodes: List[NavigatorNode]) -> None:
        """
         Reparent navigator nodes. 
        """
        pass
    def ReparentNodesWithoutPersistentData(index: int, tgTargetNode: NavigatorNode, tgNodes: List[NavigatorNode]) -> None:
        """
         Reparent navigator nodes transiently. 
        """
        pass
    def SaveConfigureFile(index: int) -> None:
        """
         Saves the configure file. 
        """
        pass
    def SendToSubView(index: int, tgTargetNode: NavigatorNode) -> None:
        """
         Send node to sub view. 
        """
        pass
    def SetActiveNode(index: int, tgTargetNode: NavigatorNode) -> None:
        """
         Set selected node as active node. 
        """
        pass
    def SetNodeName(tgTargetNode: NavigatorNode, name: str) -> None:
        """
         Set node name. 
        """
        pass
    def ShowNavigator(index: int, bitmap: str, tooltip: str, name: str) -> Navigator:
        """
         Shows the navigator. 
         Returns navigator ( Navigator NXOpen.S): .
        """
        pass
    def UnloadPartAndItsChildren(partTag: NXOpen.BasePart) -> None:
        """
         Unloads part and its children. 
        """
        pass
    def UnregisterNavigator(index: int) -> None:
        """
         Unregisters the navigator. 
        """
        pass
import NXOpen
import NXOpen.Features.Industry
class NavigatorNode(NXOpen.Features.Industry.IndustryNavigatorNode): 
    """ Represents the interface for navigator view classes"""
    @property
    def CheckStatus(self) -> bool:
        """
        Getter for property: (bool) CheckStatus
         Returns the node check status.  
             
         
        """
        pass
    @CheckStatus.setter
    def CheckStatus(self, checkStatus: bool):
        """
        Setter for property: (bool) CheckStatus
         Returns the node check status.  
             
         
        """
        pass
    @property
    def Modifiable(self) -> bool:
        """
        Getter for property: (bool) Modifiable
         Returns the node modifiable property.  
             
         
        """
        pass
    @Modifiable.setter
    def Modifiable(self, modifiable: bool):
        """
        Setter for property: (bool) Modifiable
         Returns the node modifiable property.  
             
         
        """
        pass
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the node title.  
             
         
        """
        pass
    @Title.setter
    def Title(self, title: str):
        """
        Setter for property: (str) Title
         Returns the node title.  
             
         
        """
        pass
    def AddChild(self, name: str, nodeObjects: List[NXOpen.TaggedObject], createPersistentData: bool) -> NavigatorNode:
        """
         Adds a child node. 
         Returns childNode ( NavigatorNode NXOpen.S): .
        """
        pass
    def GetChildren(self) -> List[NavigatorNode]:
        """
         Gets children nodes. 
         Returns childNodes ( NavigatorNode List[NXOpen): .
        """
        pass
    def GetNextNode(self) -> NavigatorNode:
        """
         Get next node. If this node has some child nodes, the next node is the first child.
                    Otherwise return next sibling of this node, or its parent node, or its grandparent node...  
         Returns nextNode ( NavigatorNode NXOpen.S): .
        """
        pass
    def GetNextSiblingNode(self) -> NavigatorNode:
        """
         Gets next sibling node. 
         Returns nextSiblingNode ( NavigatorNode NXOpen.S): .
        """
        pass
    def GetNodeObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the objects represented by the node. 
         Returns nodeObjects ( NXOpen.TaggedObject Li): .
        """
        pass
    def GetParent(self) -> NavigatorNode:
        """
         Gets parent node. 
         Returns parentNode ( NavigatorNode NXOpen.S): .
        """
        pass
    def GetPreviousNode(self) -> NavigatorNode:
        """
         Get previous node. If this node has no prior siblings, the previous node is its parent node if it has. 
                     If this node has a prior sibling, the previous node is the last descendant node of this previous sibling. 
         Returns previousNode ( NavigatorNode NXOpen.S): .
        """
        pass
    def GetPreviousSiblingNode(self) -> NavigatorNode:
        """
         Gets previous sibling node. 
         Returns previousSiblingNode ( NavigatorNode NXOpen.S): .
        """
        pass
    def GetProperty(self, propertyName: str) -> str:
        """
         Gets the node property. 
         Returns propertyValue (str): .
        """
        pass
    def RemoveChild(self, childNode: NavigatorNode) -> None:
        """
         Removes a child node. 
        """
        pass
    def SetDraggable(self, draggable: bool) -> None:
        """
         Sets the node draggable attribute. 
        """
        pass
    def SetIcon(self, icon: str) -> None:
        """
         Sets the node icon. 
        """
        pass
    def SetNodeObjects(self, nodeObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the objects represented by the node. 
        """
        pass
    def UpdateProperty(self, propertyName: str, propertyValue: str) -> None:
        """
         Sets the node property. 
        """
        pass
import NXOpen
class NavigatorView(NXOpen.NXObject): 
    """ Represents the interface for navigator view classes"""
    def AddRootNode(self, name: str, nodeObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Adds a root object to the navigator to represent the object. 
        """
        pass
    def GetLastSelectedNode(self) -> NavigatorNode:
        """
         Gets last selected node. 
         Returns selectedNode ( NavigatorNode NXOpen.S): .
        """
        pass
    def GetRootNode(self) -> NavigatorNode:
        """
         Gets root node. 
         Returns rootNode ( NavigatorNode NXOpen.S): .
        """
        pass
    def GetSelectedNodes(self) -> List[NavigatorNode]:
        """
         Gets selected nodes. 
         Returns selectedNodes ( NavigatorNode List[NXOpen): .
        """
        pass
    def RemoveRootNode(self) -> None:
        """
         Removes root node. 
        """
        pass
    def SetLastSelectedNode(self, selectedNode: NavigatorNode) -> None:
        """
         Sets last selected node. 
        """
        pass
    def SetSelectedNodes(self, selectedNodes: List[NavigatorNode]) -> None:
        """
         Sets selected nodes. 
        """
        pass
import NXOpen
class Navigator(NXOpen.NXObject): 
    """ Represents the interface for navigator action classes"""
    def GetRootPart(self) -> NXOpen.BasePart:
        """
         Gets root part to load navigator model. 
         Returns rootPart ( NXOpen.BasePart): .
        """
        pass
    def GetView(self, viewIndex: int) -> NavigatorView:
        """
         Gets navigator view. 
         Returns view ( NavigatorView NXOpen.S): .
        """
        pass
    def GetViewCount(self) -> int:
        """
         Gets navigator view count. 
         Returns viewCount (int): .
        """
        pass
    @overload
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
    @overload
    def Hide(self, hideNavigator: bool) -> None:
        """
         Hides a navigator. 
        """
        pass
    NodeCheckCallback = Callable[[NavigatorNode], None]
    NodeContextMenuItemActionCallback = Callable[[NavigatorNode], None]
    NodeContextMenuItemDefaultMenuItemCallback = Callable[[NavigatorNode], None]
    NodeContextMenuItemVisibilityCallback = Callable[[NavigatorNode], None]
    NodeDeselectedCallback = Callable[[NavigatorNode], None]
    NodePropertyCompareCallback = Callable[[NavigatorNode, NavigatorNode, str], None]
    NodeSelectedCallback = Callable[[NavigatorNode], None]
    NodesContextMenuItemActionCallback = Callable[[List[NavigatorNode]], None]
    NodesContextMenuItemDefaultMenuItemCallback = Callable[[List[NavigatorNode]], None]
    NodesContextMenuItemVisibilityCallback = Callable[[List[NavigatorNode]], None]
    def RegisterNodeContextMenuItem(self, title: str, icon: str, actionCB: Navigator.NodeContextMenuItemActionCallback, visibilityCB: Navigator.NodeContextMenuItemVisibilityCallback, isDefaultCB: Navigator.NodeContextMenuItemDefaultMenuItemCallback) -> None:
        """
         Registers node context menu. 
        """
        pass
    def RegisterNodesContextMenuItem(self, title: str, icon: str, actionCB: Navigator.NodesContextMenuItemActionCallback, visibilityCB: Navigator.NodesContextMenuItemVisibilityCallback, isDefaultCB: Navigator.NodesContextMenuItemDefaultMenuItemCallback) -> None:
        """
         Registers multiple nodes context menu. 
        """
        pass
    ViewContextMenuItemActionCallback = Callable[[NavigatorView], None]
    ViewContextMenuItemVisibilityCallback = Callable[[NavigatorView], None]
    def RegisterViewContextMenuItem(self, title: str, icon: str, actionCB: Navigator.ViewContextMenuItemActionCallback, visibilityCB: Navigator.ViewContextMenuItemVisibilityCallback) -> None:
        """
         Registers view context menu. 
        """
        pass
    def SetNodeCheckCallback(self, checkCB: Navigator.NodeCheckCallback) -> None:
        """
         Sets node check callback. 
        """
        pass
    def SetNodeDeselectedCallback(self, deselectedCB: Navigator.NodeDeselectedCallback) -> None:
        """
         Sets node deselected callback. 
        """
        pass
    def SetNodePropertyCompareCallback(self, checkCB: Navigator.NodePropertyCompareCallback) -> None:
        """
         Sets node property compare callback. 
        """
        pass
    def SetNodeSelectedCallback(self, selectedCB: Navigator.NodeSelectedCallback) -> None:
        """
         Sets node selected callback. 
        """
        pass
    def SetRootPart(self, rootPart: NXOpen.BasePart) -> None:
        """
         Sets root part to load navigator model. 
        """
        pass
    def ShowView(self, viewIndex: int) -> None:
        """
         Shows a navigator view. 
        """
        pass
import NXOpen
class PaintParametersData(NXOpen.TransientObject): 
    """
        Represents the paint parameter data which stored in ship design feature parms.        
     """
    class JaShipPaintParametersStatus(Enum):
        """
        Members Include: 
         |Selected|  User select paint to target in UI 

        """
        Selected: int
        @staticmethod
        def ValueOf(value: int) -> PaintParametersData.JaShipPaintParametersStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def ClearCatogoryToKruDataPtrMap(self) -> None:
        """
         Clear the catogory of spreadsheet parameter. 
        """
        pass
    def Dispose(self) -> None:
        """
         Dispose the paint parameter data object 
        """
        pass
    def EditParameter(self, parameterName: str, parameterValue: str) -> None:
        """
         Modify the paint parameter data parameter. 
        """
        pass
    def EditPrimaryParameter(self, parameterName: str, parameterValue: str) -> None:
        """
         Modify the paint parameter primary data parameter. 
        """
        pass
    def GetCheckedParameters(self) -> List[PaintParametersParameterValue]:
        """
         Get checked parameters. 
         Returns checkedPara ( PaintParametersParameterValue List[NXOpen): .
        """
        pass
    def RefreshParentParameter(self) -> None:
        """
         Refresh and reset parent parameter. 
        """
        pass
    def SetPaintParameterStatus(self, parameterName: str, parameterStatus: int, isAdd: bool) -> None:
        """
         Sets the LockHide or other status of additional paint parameter data parameter. 
        """
        pass
    def SetParameterStatus(self, parameterName: str, parameterStatus: int, isAdd: bool) -> None:
        """
         Sets the LockHide or other status of paint parameter data parameter. 
        """
        pass
import NXOpen
class PaintParametersParameterValue(NXOpen.TransientObject): 
    """
        Represents the Paint Parameters Parameter Value which stored in ship design feature parms.        
     """
    def Dispose(self) -> None:
        """
         Dispose the paint parameters parameter value object 
        """
        pass
import NXOpen
import NXOpen.Features
class ShipNavigatorNodeBuilder(NXOpen.Builder): 
    """ Represents the ship navigator node builder to add or edit ship navigator node. """
    class NodeTypes(Enum):
        """
        Members Include: 
         |Object|  The object node type. 
         |Part|  The part node type. 
         |Container|  The container node type. 

        """
        Object: int
        Part: int
        Container: int
        @staticmethod
        def ValueOf(value: int) -> ShipNavigatorNodeBuilder.NodeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExpandChildNodes(self) -> bool:
        """
        Getter for property: (bool) ExpandChildNodes
         Returns the setting indicates if the node we create or edit will expand its children in ship navigator.  
             
         
        """
        pass
    @ExpandChildNodes.setter
    def ExpandChildNodes(self, expandNode: bool):
        """
        Setter for property: (bool) ExpandChildNodes
         Returns the setting indicates if the node we create or edit will expand its children in ship navigator.  
             
         
        """
        pass
    @property
    def NodeName(self) -> str:
        """
        Getter for property: (str) NodeName
         Returns the ship navigator node name.  
             
         
        """
        pass
    @NodeName.setter
    def NodeName(self, nodeName: str):
        """
        Setter for property: (str) NodeName
         Returns the ship navigator node name.  
             
         
        """
        pass
    @property
    def NodeType(self) -> ShipNavigatorNodeBuilder.NodeTypes:
        """
        Getter for property: ( ShipNavigatorNodeBuilder.NodeTypes NXOpen.S) NodeType
         Returns the ship navigator node type, which can be object, part or container.  
             
         
        """
        pass
    @NodeType.setter
    def NodeType(self, type: ShipNavigatorNodeBuilder.NodeTypes):
        """
        Setter for property: ( ShipNavigatorNodeBuilder.NodeTypes NXOpen.S) NodeType
         Returns the ship navigator node type, which can be object, part or container.  
             
         
        """
        pass
    @property
    def SourceFeatures(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) SourceFeatures
         Returns the list of features used to create ship navigator object node.  
             
         
        """
        pass
    @property
    def SourceParts(self) -> SelectComponentList:
        """
        Getter for property: ( SelectComponentList NXOpen.A) SourceParts
         Returns the list of parts used to create ship navigator part nodes.  
             
         
        """
        pass
import NXOpen
class ShipNavigatorRoot(NXOpen.NXObject): 
    """ Represents the interface for ship navigator root classes. """
    pass
import NXOpen
class ShipSession(NXOpen.Object): 
    """ Represents Ship session """
    @property
    def Navigators() -> NavigatorCollection:
        """
         Returns the  NXOpen::ShipDesign::NavigatorCollection  belonging to this session 
        """
        pass
    @property
    def Generator() -> Generator:
        """
         Returns the  NXOpen::ShipDesign::Generator  belonging to this session 
        """
        pass
    @property
    def GeneralArrangement() -> GeneralArrangementManager:
        """
         Returns the  NXOpen::ShipDesign::GeneralArrangementManager  belonging to this session 
        """
        pass
    @property
    def ApplicationUtils() -> ApplicationUtils:
        """
         Returns the  NXOpen::ShipDesign::ApplicationUtils  belonging to this session 
        """
        pass
