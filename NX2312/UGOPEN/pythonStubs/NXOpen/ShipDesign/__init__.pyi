from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents Generator which wrap the ship api for china  <br> To obtain an instance of this class, refer to @link NXOpen::ShipDesign::ShipSession  NXOpen::ShipDesign::ShipSession @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ApplicationUtils(NXOpen.Object): 
    """ Represents Generator which wrap the ship api for china """


    ##  Register button in other application 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  The name of the application. 
    @staticmethod
    def RegisterApplicationForModlFeatureEdit(appName: str) -> None:
        """
         Register button in other application 
        """
        pass
    
    ##  Register application sensitivity when the application is changed 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  The name of the master application. 
    def RegisterApplicationSensitivityOnApplicationChange(appName: str, appsWhereToLive: List[str]) -> None:
        """
         Register application sensitivity when the application is changed 
        """
        pass
    
    ##  Register button in other application 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  The id of the application. 
    def RegisterButtonApplication(appId: int, buttonName: str) -> None:
        """
         Register button in other application 
        """
        pass
    
    ##  Register the last application of the part 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  The name of the application. 
    def RegisterLastApplication(part: NXOpen.Part, appName: str) -> None:
        """
         Register the last application of the part 
        """
        pass
    
import NXOpen
##  Represents the interface for General Arrangement classes  <br> To obtain an instance of this class, refer to @link NXOpen::ShipDesign::ShipSession  NXOpen::ShipDesign::ShipSession @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class GeneralArrangementManager(NXOpen.Object): 
    """ Represents the interface for General Arrangement classes """


    ##  Creates the rectangle for Deck Plan sketch. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  the sketch 
    def CreateSkecthRectangle(sketch: NXOpen.Sketch) -> None:
        """
         Creates the rectangle for Deck Plan sketch. 
        """
        pass
    
    ##  Creates the wave plane for src plane . 
    ##  @return dstPlane (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ## <param name="srPlane"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreateWaveLinkPlane(srPlane: NXOpen.TaggedObject) -> NXOpen.TaggedObject:
        """
         Creates the wave plane for src plane . 
         @return dstPlane (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
        """
        pass
    
    ##  Add callback EditRoomCallBack 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    @staticmethod
    def EditRoomCallBack() -> None:
        """
         Add callback EditRoomCallBack 
        """
        pass
    
    ##  Exits the Sketch environment under General Arrangement application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    @staticmethod
    def GASketchEnd() -> None:
        """
         Exits the Sketch environment under General Arrangement application. 
        """
        pass
    
    ##  Makes the part to be Ship Container. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  the container part 
    @staticmethod
    def MakeContainerPart(part: NXOpen.Part) -> None:
        """
         Makes the part to be Ship Container. 
        """
        pass
    
    ## Reload the material data.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_concept ("Ship Concept")
    ## <param name="bShip"> (bool) </param>
    @staticmethod
    def ReloadMaterialData(bShip: bool) -> None:
        """
        Reload the material data.
        """
        pass
    
    ##  Remove the sketch objects from the model reference set 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ## <param name="sketch"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    @staticmethod
    def RemoveSketchFromMoldRefSet(sketch: NXOpen.TaggedObject) -> None:
        """
         Remove the sketch objects from the model reference set 
        """
        pass
    
    ## Removes all unused expressions in the general arrangement deck reference part.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    @staticmethod
    def RemoveUnusedExpression() -> None:
        """
        Removes all unused expressions in the general arrangement deck reference part.
        """
        pass
    
    ##  Resizes the ship grid datum. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    @staticmethod
    def ResizeGrid() -> None:
        """
         Resizes the ship grid datum. 
        """
        pass
    
    ##  WaveLinkFrameBarToDeckRefPart. 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    @staticmethod
    def WaveLinkFrameBarToDeckRefPart() -> None:
        """
         WaveLinkFrameBarToDeckRefPart. 
        """
        pass
    
import NXOpen
##  Represents Generator which wrap the ship api for china  <br> To obtain an instance of this class, refer to @link NXOpen::ShipDesign::ShipSession  NXOpen::ShipDesign::ShipSession @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class Generator(NXOpen.Object): 
    """ Represents Generator which wrap the ship api for china """


    ##  Clash status to indicate to show space position relation between two bodies
    ##         1.Clashes in entities of the same dimension
    ##         Clash_interfere        Two solid bodies interfere if they share a common volume
    ##                                             Two faces interfere if they share a common area, or they intersect.
    ##                                             Two edges interfere if they share a common length, or they intersect.
    ## 
    ##         Clash_abut_no_class    Two solid bodies abut when they touch, but do not share a common volume.
    ##                                             Two faces abut when they share a common curve or point in space which lies on the bounding topology of at least one of the faces.
    ##                                             Two edges abut when they share a common point in space which lies on the bounding topology of at least one of the edges.
    ## 
    ##         Clash_a_in_b
    ##         Clash_b_in_a           For solids, faces, and edges, one entity is contained when it lies entirely inside the other entity, 
    ##                                             and their bounding topologies do not touch.
    ##         2.Clashes in bodies of different dimensions 
    ##         Clash_interfere        If there is a common point in space that lies within the bounding topology of the two bodies,
    ##                                             then the bodies are said to interfere.
    ##         Clash_abut_no_class    If no common point exists, but the bounding topologies of the two bodies touch,
    ##                                             then the bodies are said to abut.
    ##         Clash_a_in_b           
    ##         Clash_b_in_a           If one body lies entirely within the bounding topology of the other, and the bounding topology 
    ##                                             of the two bodies do not touch then the entity is contained.
    ##         
    ##  There is no clash between two bodies. 
    class ClashType(Enum):
        """
        Members Include: <NotSet> <AInB> <BInA> <Exists> <AbutNoClass> <AbutBInA> <AbutBOutA> <Interfere>
        """
        NotSet: int
        AInB: int
        BInA: int
        Exists: int
        AbutNoClass: int
        AbutBInA: int
        AbutBOutA: int
        Interfere: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Generator.ClashType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Advances the progress bar. 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ## <param name="stepNumber"> (int) </param>
    @staticmethod
    def AdvanceProgress(stepNumber: int) -> None:
        """
         Advances the progress bar. 
        """
        pass
    
    ##  Gets all intersected plates with the given plates. 
    ##  @return outElements (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ## <param name="plate"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="inSheets"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    ## <param name="tolerence"> (float) </param>
    def AskIntersectionPlates(plate: NXOpen.TaggedObject, inSheets: List[NXOpen.TaggedObject], tolerence: float) -> List[NXOpen.TaggedObject]:
        """
         Gets all intersected plates with the given plates. 
         @return outElements (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
        """
        pass
    
    ##  Gets the spatial relations of the plates based on its positions. 
    ##  @return A tuple consisting of (elementIndex, outElements). 
    ##  - elementIndex is: List[int].
    ##  - outElements is: @link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink.

    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ## <param name="hull"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="inSheets"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    ## <param name="tolerence"> (float) </param>
    @staticmethod
    def AskPlatesSpatialRelations(hull: NXOpen.TaggedObject, inSheets: List[NXOpen.TaggedObject], tolerence: float) -> Tuple[List[int], List[NXOpen.TaggedObject]]:
        """
         Gets the spatial relations of the plates based on its positions. 
         @return A tuple consisting of (elementIndex, outElements). 
         - elementIndex is: List[int].
         - outElements is: @link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink.

        """
        pass
    
    ##  Check assembly circular references. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_mfg_prep ("Ship Manufacturing")
    @staticmethod
    def CheckAssemblyCircularReferences() -> None:
        """
         Check assembly circular references. 
        """
        pass
    
    ##  Check the clash between two bodys. 
    ##  @return clash_status (@link Generator.ClashType NXOpen.ShipDesign.Generator.ClashType@endlink):  O: clash status for body a and body b .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ## <param name="body_a"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    ## <param name="body_b"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def CheckBodyClash(body_a: NXOpen.DisplayableObject, body_b: NXOpen.DisplayableObject) -> Generator.ClashType:
        """
         Check the clash between two bodys. 
         @return clash_status (@link Generator.ClashType NXOpen.ShipDesign.Generator.ClashType@endlink):  O: clash status for body a and body b .
        """
        pass
    
    ##  Creates the ship cargo body based on the input boundary sheets. 
    ##  @return outElements (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ## <param name="inSheets"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    ## <param name="tolerence"> (float) </param>
    def CreateCargo(inSheets: List[NXOpen.TaggedObject], tolerence: float) -> List[NXOpen.TaggedObject]:
        """
         Creates the ship cargo body based on the input boundary sheets. 
         @return outElements (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
        """
        pass
    
    ##  Creates a progress bar with given title and number of total steps. 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ## <param name="numSteps"> (int) </param>
    ## <param name="operationName"> (str) </param>
    def CreateProgress(numSteps: int, operationName: str) -> None:
        """
         Creates a progress bar with given title and number of total steps. 
        """
        pass
    
    ##  Deletes the progress bar. 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    @staticmethod
    def DeleteProgress() -> None:
        """
         Deletes the progress bar. 
        """
        pass
    
    ##  Get the outline sheet body of input bodies. 
    ##  @return outline_body (@link NXOpen.Body NXOpen.Body@endlink):  O: output outline sheet body .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ## <param name="bodies"> (@link NXOpen.Body List[NXOpen.Body]@endlink) </param>
    ## <param name="datum_plane"> (@link NXOpen.DatumPlane NXOpen.DatumPlane@endlink) </param>
    def GetOutlineSheetbody(bodies: List[NXOpen.Body], datum_plane: NXOpen.DatumPlane) -> NXOpen.Body:
        """
         Get the outline sheet body of input bodies. 
         @return outline_body (@link NXOpen.Body NXOpen.Body@endlink):  O: output outline sheet body .
        """
        pass
    
    ##  Gets the edges of tool sheet bodies which are laid on a target sheet body 
    ##  @return outElements (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ## <param name="outSheet"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="inSheets"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    ## <param name="tolerence"> (float) </param>
    def GetSheetsEdgesLaidOnTargetSheet(outSheet: NXOpen.TaggedObject, inSheets: List[NXOpen.TaggedObject], tolerence: float) -> List[NXOpen.TaggedObject]:
        """
         Gets the edges of tool sheet bodies which are laid on a target sheet body 
         @return outElements (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
        """
        pass
    
    ##  Defines the callback function whenever an NX application is entered. 
    ## A callback definition with no input arguments and no return type
    ShipCustomerEnterApplication = Callable[[], None]
    
    
    ##  Defines the callback function whenever an NX application is exited. 
    ## A callback definition with no input arguments and no return type
    ShipCustomerExitApplication = Callable[[], None]
    
    
    ##  Register application callback when application is entered or exited. It is specific for ship customers. 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  The name of the application. 
    def RegisterApplicationCallback(name: str, enterCallback: Generator.ShipCustomerEnterApplication, exitCallback: Generator.ShipCustomerExitApplication) -> None:
        """
         Register application callback when application is entered or exited. It is specific for ship customers. 
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents the interface for navigator action classes <br> To obtain an instance of this class, refer to @link NXOpen::ShipDesign::ShipSession  NXOpen::ShipDesign::ShipSession @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class NavigatorCollection(NXOpen.Object): 
    """ Represents the interface for navigator action classes"""


    ##  Actives ship navigator. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  ship navigator id 
    @staticmethod
    def ActiveNavigator(index: int) -> None:
        """
         Actives ship navigator. 
        """
        pass
    
    ##  Change node state. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## <param name="tgTargetNode"> (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink) </param>
    ## <param name="status"> (int) </param>
    def ChangeNodeState(tgTargetNode: NavigatorNode, status: int) -> None:
        """
         Change node state. 
        """
        pass
    
    ##  Change nodes state. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ## <param name="tgNodes"> (@link NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink) </param>
    ## <param name="status"> (int) </param>
    def ChangeNodesState(tgNodes: List[NavigatorNode], status: int) -> None:
        """
         Change nodes state. 
        """
        pass
    
    ##  Copy navigator node. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  ship navigator id 
    def CopyNode(index: int, tgNodes: List[NavigatorNode]) -> None:
        """
         Copy navigator node. 
        """
        pass
    
    ##  Creates a @link NXOpen::ShipDesign::ShipNavigatorNodeBuilder NXOpen::ShipDesign::ShipNavigatorNodeBuilder@endlink . 
    ##  @return builder (@link ShipNavigatorNodeBuilder NXOpen.ShipDesign.ShipNavigatorNodeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## <param name="isEdit"> (bool) </param>
    ## <param name="tgNode"> (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink) </param>
    def CreateShipNavigatorNodeBuilder(isEdit: bool, tgNode: NavigatorNode) -> ShipNavigatorNodeBuilder:
        """
         Creates a @link NXOpen::ShipDesign::ShipNavigatorNodeBuilder NXOpen::ShipDesign::ShipNavigatorNodeBuilder@endlink . 
         @return builder (@link ShipNavigatorNodeBuilder NXOpen.ShipDesign.ShipNavigatorNodeBuilder@endlink): .
        """
        pass
    
    ##  Cut navigator node. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  ship navigator id 
    def CutNode(index: int, tgNodes: List[NavigatorNode]) -> None:
        """
         Cut navigator node. 
        """
        pass
    
    ##  Decrease ignore navigator view update events level and update navigator views
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  ship navigator id 
    @staticmethod
    def DecrementIgnoreNavigatorViewUpdateEventsLevel(index: int) -> None:
        """
         Decrease ignore navigator view update events level and update navigator views
        """
        pass
    
    ##  Edit feature. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  @link NXOpen::Features::Feature NXOpen::Features::Feature@endlink  to be edited 
    @staticmethod
    def EditFeature(tgFeat: NXOpen.Features.Feature) -> None:
        """
         Edit feature. 
        """
        pass
    
    ##  Enter sketch environment by edit 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  The Sketch to edit 
    @staticmethod
    def EnterSketchEnvironment(sketch_feature: NXOpen.Features.SketchFeature) -> None:
        """
         Enter sketch environment by edit 
        """
        pass
    
    ##  Gets ship navigator. 
    ##  @return navigator (@link Navigator NXOpen.ShipDesign.Navigator@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  ship navigator id 
    @staticmethod
    def GetNavigator(index: int) -> Navigator:
        """
         Gets ship navigator. 
         @return navigator (@link Navigator NXOpen.ShipDesign.Navigator@endlink): .
        """
        pass
    
    ##  Gets navigator count. 
    ##  @return count (int): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetNavigatorCount() -> int:
        """
         Gets navigator count. 
         @return count (int): .
        """
        pass
    
    ##  Gets all referencing navigator nodes. 
    ##  @return referencingNodes (@link NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## <param name="tgReferencedObject"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    @staticmethod
    def GetReferencingNodes(tgReferencedObject: NXOpen.TaggedObject) -> List[NavigatorNode]:
        """
         Gets all referencing navigator nodes. 
         @return referencingNodes (@link NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink): .
        """
        pass
    
    ##  Establish ship navigator root 
    ##  @return navRoot (@link ShipNavigatorRoot NXOpen.ShipDesign.ShipNavigatorRoot@endlink):  .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetShipNavigatorRoot() -> ShipNavigatorRoot:
        """
         Establish ship navigator root 
         @return navRoot (@link ShipNavigatorRoot NXOpen.ShipDesign.ShipNavigatorRoot@endlink):  .
        """
        pass
    
    ##  Increase ignore navigator view update events level 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  ship navigator id 
    @staticmethod
    def IncrementIgnoreNavigatorViewUpdateEventsLevel(index: int) -> None:
        """
         Increase ignore navigator view update events level 
        """
        pass
    
    ##  Checks if ship navigator is registered. 
    ##  @return isNavigatorRegistered (bool): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## <param name="index"> (int) </param>
    @staticmethod
    def IsNavigatorRegistered(index: int) -> bool:
        """
         Checks if ship navigator is registered. 
         @return isNavigatorRegistered (bool): .
        """
        pass
    
    ##  Paste navigator node. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  ship navigator id 
    def PasteNode(index: int, tgTargetNode: NavigatorNode) -> None:
        """
         Paste navigator node. 
        """
        pass
    
    ##  Populates and prints data for each navigator found. 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    ##  part being validated 
    @staticmethod
    def PopulateAndPrintShipNavigator(displayPart: NXOpen.BasePart) -> None:
        """
         Populates and prints data for each navigator found. 
        """
        pass
    
    ##  Loads navigator models. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  ship navigator id 
    @staticmethod
    def RefreshNavigator(index: int) -> None:
        """
         Loads navigator models. 
        """
        pass
    
    ##  Registers the navigator. 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## <param name="index"> (int) </param>
    ## <param name="bitmap"> (str) </param>
    ## <param name="tooltip"> (str) </param>
    ## <param name="name"> (str) </param>
    def RegisterNavigator(index: int, bitmap: str, tooltip: str, name: str) -> None:
        """
         Registers the navigator. 
        """
        pass
    
    ##  Remove navigator nodes. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  ship navigator id 
    def RemoveNodes(index: int, tgNodes: List[NavigatorNode]) -> None:
        """
         Remove navigator nodes. 
        """
        pass
    
    ##  Reparent navigator node. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  ship navigator id 
    def ReparentNode(index: int, tgTargetNode: NavigatorNode, tgSourceNode: NavigatorNode) -> None:
        """
         Reparent navigator node. 
        """
        pass
    
    ##  Reparent navigator nodes. 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  ship navigator id 
    def ReparentNodes(index: int, tgTargetNode: NavigatorNode, tgNodes: List[NavigatorNode]) -> None:
        """
         Reparent navigator nodes. 
        """
        pass
    
    ##  Reparent navigator nodes transiently. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  ship navigator id 
    def ReparentNodesWithoutPersistentData(index: int, tgTargetNode: NavigatorNode, tgNodes: List[NavigatorNode]) -> None:
        """
         Reparent navigator nodes transiently. 
        """
        pass
    
    ##  Saves the configure file. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  ship navigator id 
    @staticmethod
    def SaveConfigureFile(index: int) -> None:
        """
         Saves the configure file. 
        """
        pass
    
    ##  Send node to sub view. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  ship navigator id 
    def SendToSubView(index: int, tgTargetNode: NavigatorNode) -> None:
        """
         Send node to sub view. 
        """
        pass
    
    ##  Set selected node as active node. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ##  ship navigator id 
    def SetActiveNode(index: int, tgTargetNode: NavigatorNode) -> None:
        """
         Set selected node as active node. 
        """
        pass
    
    ##  Set node name. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## <param name="tgTargetNode"> (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink) </param>
    ## <param name="name"> (str) </param>
    def SetNodeName(tgTargetNode: NavigatorNode, name: str) -> None:
        """
         Set node name. 
        """
        pass
    
    ##  Shows the navigator. 
    ##  @return navigator (@link Navigator NXOpen.ShipDesign.Navigator@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## <param name="index"> (int) </param>
    ## <param name="bitmap"> (str) </param>
    ## <param name="tooltip"> (str) </param>
    ## <param name="name"> (str) </param>
    def ShowNavigator(index: int, bitmap: str, tooltip: str, name: str) -> Navigator:
        """
         Shows the navigator. 
         @return navigator (@link Navigator NXOpen.ShipDesign.Navigator@endlink): .
        """
        pass
    
    ##  Unloads part and its children. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## <param name="partTag"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    @staticmethod
    def UnloadPartAndItsChildren(partTag: NXOpen.BasePart) -> None:
        """
         Unloads part and its children. 
        """
        pass
    
    ##  Unregisters the navigator. 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## <param name="index"> (int) </param>
    @staticmethod
    def UnregisterNavigator(index: int) -> None:
        """
         Unregisters the navigator. 
        """
        pass
    
import NXOpen
import NXOpen.Features.Industry
##  Represents the interface for navigator view classes <br> Use the @link NXOpen::ShipDesign::NavigatorView NXOpen::ShipDesign::NavigatorView@endlink  class to create a navigator node  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class NavigatorNode(NXOpen.Features.Industry.IndustryNavigatorNode): 
    """ Represents the interface for navigator view classes"""


    ## Getter for property: (bool) CheckStatus
    ##   the node check status.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def CheckStatus(self) -> bool:
        """
        Getter for property: (bool) CheckStatus
          the node check status.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CheckStatus

    ##   the node check status.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CheckStatus.setter
    def CheckStatus(self, checkStatus: bool):
        """
        Setter for property: (bool) CheckStatus
          the node check status.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Modifiable
    ##   the node modifiable property.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return bool
    @property
    def Modifiable(self) -> bool:
        """
        Getter for property: (bool) Modifiable
          the node modifiable property.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Modifiable

    ##   the node modifiable property.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    @Modifiable.setter
    def Modifiable(self, modifiable: bool):
        """
        Setter for property: (bool) Modifiable
          the node modifiable property.  
             
         
        """
        pass
    
    ## Getter for property: (str) Title
    ##   the node title.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
          the node title.  
             
         
        """
        pass
    
    ## Setter for property: (str) Title

    ##   the node title.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @Title.setter
    def Title(self, title: str):
        """
        Setter for property: (str) Title
          the node title.  
             
         
        """
        pass
    
    ##  Adds a child node. 
    ##  @return childNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="name"> (str) </param>
    ## <param name="nodeObjects"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    ## <param name="createPersistentData"> (bool) </param>
    def AddChild(node: NavigatorNode, name: str, nodeObjects: List[NXOpen.TaggedObject], createPersistentData: bool) -> NavigatorNode:
        """
         Adds a child node. 
         @return childNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
        """
        pass
    
    ##  Gets children nodes. 
    ##  @return childNodes (@link NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetChildren(node: NavigatorNode) -> List[NavigatorNode]:
        """
         Gets children nodes. 
         @return childNodes (@link NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink): .
        """
        pass
    
    ##  Get next node. If this node has some child nodes, the next node is the first child.
    ##             Otherwise return next sibling of this node, or its parent node, or its grandparent node...  
    ##  @return nextNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetNextNode(node: NavigatorNode) -> NavigatorNode:
        """
         Get next node. If this node has some child nodes, the next node is the first child.
                    Otherwise return next sibling of this node, or its parent node, or its grandparent node...  
         @return nextNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
        """
        pass
    
    ##  Gets next sibling node. 
    ##  @return nextSiblingNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetNextSiblingNode(node: NavigatorNode) -> NavigatorNode:
        """
         Gets next sibling node. 
         @return nextSiblingNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
        """
        pass
    
    ##  Gets the objects represented by the node. 
    ##  @return nodeObjects (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetNodeObjects(node: NavigatorNode) -> List[NXOpen.TaggedObject]:
        """
         Gets the objects represented by the node. 
         @return nodeObjects (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
        """
        pass
    
    ##  Gets parent node. 
    ##  @return parentNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetParent(node: NavigatorNode) -> NavigatorNode:
        """
         Gets parent node. 
         @return parentNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
        """
        pass
    
    ##  Get previous node. If this node has no prior siblings, the previous node is its parent node if it has. 
    ##              If this node has a prior sibling, the previous node is the last descendant node of this previous sibling. 
    ##  @return previousNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetPreviousNode(node: NavigatorNode) -> NavigatorNode:
        """
         Get previous node. If this node has no prior siblings, the previous node is its parent node if it has. 
                     If this node has a prior sibling, the previous node is the last descendant node of this previous sibling. 
         @return previousNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
        """
        pass
    
    ##  Gets previous sibling node. 
    ##  @return previousSiblingNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetPreviousSiblingNode(node: NavigatorNode) -> NavigatorNode:
        """
         Gets previous sibling node. 
         @return previousSiblingNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
        """
        pass
    
    ##  Gets the node property. 
    ##  @return propertyValue (str): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="propertyName"> (str) </param>
    def GetProperty(node: NavigatorNode, propertyName: str) -> str:
        """
         Gets the node property. 
         @return propertyValue (str): .
        """
        pass
    
    ##  Removes a child node. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="childNode"> (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink) </param>
    def RemoveChild(node: NavigatorNode, childNode: NavigatorNode) -> None:
        """
         Removes a child node. 
        """
        pass
    
    ##  Sets the node draggable attribute. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="draggable"> (bool) </param>
    def SetDraggable(node: NavigatorNode, draggable: bool) -> None:
        """
         Sets the node draggable attribute. 
        """
        pass
    
    ##  Sets the node icon. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="icon"> (str) </param>
    def SetIcon(node: NavigatorNode, icon: str) -> None:
        """
         Sets the node icon. 
        """
        pass
    
    ##  Sets the objects represented by the node. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="nodeObjects"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    def SetNodeObjects(node: NavigatorNode, nodeObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the objects represented by the node. 
        """
        pass
    
    ##  Sets the node property. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="propertyName"> (str) </param>
    ## <param name="propertyValue"> (str) </param>
    def UpdateProperty(node: NavigatorNode, propertyName: str, propertyValue: str) -> None:
        """
         Sets the node property. 
        """
        pass
    
import NXOpen
##  Represents the interface for navigator view classes <br> Use the @link NXOpen::ShipDesign::Navigator NXOpen::ShipDesign::Navigator@endlink  class to get a navigator view  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class NavigatorView(NXOpen.NXObject): 
    """ Represents the interface for navigator view classes"""


    ##  Adds a root object to the navigator to represent the object. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="name"> (str) </param>
    ## <param name="nodeObjects"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    def AddRootNode(selfView: NavigatorView, name: str, nodeObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Adds a root object to the navigator to represent the object. 
        """
        pass
    
    ##  Gets last selected node. 
    ##  @return selectedNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetLastSelectedNode(view: NavigatorView) -> NavigatorNode:
        """
         Gets last selected node. 
         @return selectedNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
        """
        pass
    
    ##  Gets root node. 
    ##  @return rootNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetRootNode(selfView: NavigatorView) -> NavigatorNode:
        """
         Gets root node. 
         @return rootNode (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink): .
        """
        pass
    
    ##  Gets selected nodes. 
    ##  @return selectedNodes (@link NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetSelectedNodes(view: NavigatorView) -> List[NavigatorNode]:
        """
         Gets selected nodes. 
         @return selectedNodes (@link NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink): .
        """
        pass
    
    ##  Removes root node. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def RemoveRootNode(selfView: NavigatorView) -> None:
        """
         Removes root node. 
        """
        pass
    
    ##  Sets last selected node. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="selectedNode"> (@link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink) </param>
    def SetLastSelectedNode(view: NavigatorView, selectedNode: NavigatorNode) -> None:
        """
         Sets last selected node. 
        """
        pass
    
    ##  Sets selected nodes. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="selectedNodes"> (@link NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink) </param>
    def SetSelectedNodes(view: NavigatorView, selectedNodes: List[NavigatorNode]) -> None:
        """
         Sets selected nodes. 
        """
        pass
    
import NXOpen
##  Represents the interface for navigator action classes <br> Use the @link NXOpen::ShipDesign::NavigatorCollection NXOpen::ShipDesign::NavigatorCollection@endlink  class to get a navigator  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Navigator(NXOpen.NXObject): 
    """ Represents the interface for navigator action classes"""


    ##  Gets root part to load navigator model. 
    ##  @return rootPart (@link NXOpen.BasePart NXOpen.BasePart@endlink): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetRootPart(selfNavigator: Navigator) -> NXOpen.BasePart:
        """
         Gets root part to load navigator model. 
         @return rootPart (@link NXOpen.BasePart NXOpen.BasePart@endlink): .
        """
        pass
    
    ##  Gets navigator view. 
    ##  @return view (@link NavigatorView NXOpen.ShipDesign.NavigatorView@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="viewIndex"> (int) </param>
    def GetView(selfNavigator: Navigator, viewIndex: int) -> NavigatorView:
        """
         Gets navigator view. 
         @return view (@link NavigatorView NXOpen.ShipDesign.NavigatorView@endlink): .
        """
        pass
    
    ##  Gets navigator view count. 
    ##  @return viewCount (int): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def GetViewCount(selfNavigator: Navigator) -> int:
        """
         Gets navigator view count. 
         @return viewCount (int): .
        """
        pass
    
    ##  Hides a navigator. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    @staticmethod
    def Hide(selfNavigator: Navigator) -> None:
        """
         Hides a navigator. 
        """
        pass
    
    ##  Hides a navigator view. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="viewIndex"> (int) </param>
    def HideView(selfNavigator: Navigator, viewIndex: int) -> None:
        """
         Hides a navigator view. 
        """
        pass
    
    ##  Hides a navigator. 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="hideNavigator"> (bool) </param>
    def Hide(selfNavigator: Navigator, hideNavigator: bool) -> None:
        """
         Hides a navigator. 
        """
        pass
    
    ##  Navigator node check callback. 
    ## A callback definition with the following input arguments: 
    ##  - @link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink
    ##  and no return type
    NodeCheckCallback = Callable[[NavigatorNode], None]
    
    
    ##  Navigator node context menu item callback. 
    ## A callback definition with the following input arguments: 
    ##  - @link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink
    ##  and no return type
    NodeContextMenuItemActionCallback = Callable[[NavigatorNode], None]
    
    
    ##  Navigator node context menu item default callback. 
    ## A callback definition with the following input arguments: 
    ##  - @link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink
    ##  and no return type
    NodeContextMenuItemDefaultMenuItemCallback = Callable[[NavigatorNode], None]
    
    
    ##  Navigator node context menu item visibility callback. 
    ## A callback definition with the following input arguments: 
    ##  - @link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink
    ##  and no return type
    NodeContextMenuItemVisibilityCallback = Callable[[NavigatorNode], None]
    
    
    ##  Navigator node deselected callback. 
    ## A callback definition with the following input arguments: 
    ##  - @link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink
    ##  and no return type
    NodeDeselectedCallback = Callable[[NavigatorNode], None]
    
    
    ##  Navigator node property compare callback. 
    ## A callback definition with the following input arguments: 
    ##  - @link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink
    ##  - @link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink
    ##  - str
    ##  and no return type
    NodePropertyCompareCallback = Callable[[NavigatorNode, NavigatorNode, str], None]
    
    
    ##  Navigator node selected callback. 
    ## A callback definition with the following input arguments: 
    ##  - @link NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink
    ##  and no return type
    NodeSelectedCallback = Callable[[NavigatorNode], None]
    
    
    ##  Multiple navigator node context menu item callback. 
    ## A callback definition with the following input arguments: 
    ##  - @link NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink
    ##  and no return type
    NodesContextMenuItemActionCallback = Callable[[List[NavigatorNode]], None]
    
    
    ##  Multiple navigator node context menu item default callback. 
    ## A callback definition with the following input arguments: 
    ##  - @link NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink
    ##  and no return type
    NodesContextMenuItemDefaultMenuItemCallback = Callable[[List[NavigatorNode]], None]
    
    
    ##  Multiple navigator node context menu item visibility callback. 
    ## A callback definition with the following input arguments: 
    ##  - @link NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink
    ##  and no return type
    NodesContextMenuItemVisibilityCallback = Callable[[List[NavigatorNode]], None]
    
    
    ##  Registers node context menu. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="title"> (str) </param>
    ## <param name="icon"> (str) </param>
    ## <param name="actionCB"> (@link Navigator.NodeContextMenuItemActionCallback NXOpen.ShipDesign.Navigator.NodeContextMenuItemActionCallback@endlink) </param>
    ## <param name="visibilityCB"> (@link Navigator.NodeContextMenuItemVisibilityCallback NXOpen.ShipDesign.Navigator.NodeContextMenuItemVisibilityCallback@endlink) </param>
    ## <param name="isDefaultCB"> (@link Navigator.NodeContextMenuItemDefaultMenuItemCallback NXOpen.ShipDesign.Navigator.NodeContextMenuItemDefaultMenuItemCallback@endlink) </param>
    def RegisterNodeContextMenuItem(selfNavigator: Navigator, title: str, icon: str, actionCB: Navigator.NodeContextMenuItemActionCallback, visibilityCB: Navigator.NodeContextMenuItemVisibilityCallback, isDefaultCB: Navigator.NodeContextMenuItemDefaultMenuItemCallback) -> None:
        """
         Registers node context menu. 
        """
        pass
    
    ##  Registers multiple nodes context menu. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="title"> (str) </param>
    ## <param name="icon"> (str) </param>
    ## <param name="actionCB"> (@link Navigator.NodesContextMenuItemActionCallback NXOpen.ShipDesign.Navigator.NodesContextMenuItemActionCallback@endlink) </param>
    ## <param name="visibilityCB"> (@link Navigator.NodesContextMenuItemVisibilityCallback NXOpen.ShipDesign.Navigator.NodesContextMenuItemVisibilityCallback@endlink) </param>
    ## <param name="isDefaultCB"> (@link Navigator.NodesContextMenuItemDefaultMenuItemCallback NXOpen.ShipDesign.Navigator.NodesContextMenuItemDefaultMenuItemCallback@endlink) </param>
    def RegisterNodesContextMenuItem(selfNavigator: Navigator, title: str, icon: str, actionCB: Navigator.NodesContextMenuItemActionCallback, visibilityCB: Navigator.NodesContextMenuItemVisibilityCallback, isDefaultCB: Navigator.NodesContextMenuItemDefaultMenuItemCallback) -> None:
        """
         Registers multiple nodes context menu. 
        """
        pass
    
    ##  Navigator view context menu item callback. 
    ## A callback definition with the following input arguments: 
    ##  - @link NavigatorView NXOpen.ShipDesign.NavigatorView@endlink
    ##  and no return type
    ViewContextMenuItemActionCallback = Callable[[NavigatorView], None]
    
    
    ##  Navigator iew context menu item visibility callback. 
    ## A callback definition with the following input arguments: 
    ##  - @link NavigatorView NXOpen.ShipDesign.NavigatorView@endlink
    ##  and no return type
    ViewContextMenuItemVisibilityCallback = Callable[[NavigatorView], None]
    
    
    ##  Registers view context menu. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="title"> (str) </param>
    ## <param name="icon"> (str) </param>
    ## <param name="actionCB"> (@link Navigator.ViewContextMenuItemActionCallback NXOpen.ShipDesign.Navigator.ViewContextMenuItemActionCallback@endlink) </param>
    ## <param name="visibilityCB"> (@link Navigator.ViewContextMenuItemVisibilityCallback NXOpen.ShipDesign.Navigator.ViewContextMenuItemVisibilityCallback@endlink) </param>
    def RegisterViewContextMenuItem(selfNavigator: Navigator, title: str, icon: str, actionCB: Navigator.ViewContextMenuItemActionCallback, visibilityCB: Navigator.ViewContextMenuItemVisibilityCallback) -> None:
        """
         Registers view context menu. 
        """
        pass
    
    ##  Sets node check callback. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="checkCB"> (@link Navigator.NodeCheckCallback NXOpen.ShipDesign.Navigator.NodeCheckCallback@endlink) </param>
    def SetNodeCheckCallback(selfNavigator: Navigator, checkCB: Navigator.NodeCheckCallback) -> None:
        """
         Sets node check callback. 
        """
        pass
    
    ##  Sets node deselected callback. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="deselectedCB"> (@link Navigator.NodeDeselectedCallback NXOpen.ShipDesign.Navigator.NodeDeselectedCallback@endlink) </param>
    def SetNodeDeselectedCallback(selfNavigator: Navigator, deselectedCB: Navigator.NodeDeselectedCallback) -> None:
        """
         Sets node deselected callback. 
        """
        pass
    
    ##  Sets node property compare callback. 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="checkCB"> (@link Navigator.NodePropertyCompareCallback NXOpen.ShipDesign.Navigator.NodePropertyCompareCallback@endlink) </param>
    def SetNodePropertyCompareCallback(selfNavigator: Navigator, checkCB: Navigator.NodePropertyCompareCallback) -> None:
        """
         Sets node property compare callback. 
        """
        pass
    
    ##  Sets node selected callback. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="selectedCB"> (@link Navigator.NodeSelectedCallback NXOpen.ShipDesign.Navigator.NodeSelectedCallback@endlink) </param>
    def SetNodeSelectedCallback(selfNavigator: Navigator, selectedCB: Navigator.NodeSelectedCallback) -> None:
        """
         Sets node selected callback. 
        """
        pass
    
    ##  Sets root part to load navigator model. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="rootPart"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    def SetRootPart(selfNavigator: Navigator, rootPart: NXOpen.BasePart) -> None:
        """
         Sets root part to load navigator model. 
        """
        pass
    
    ##  Shows a navigator view. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design")
    ## 
    ## <param name="viewIndex"> (int) </param>
    def ShowView(selfNavigator: Navigator, viewIndex: int) -> None:
        """
         Shows a navigator view. 
        """
        pass
    
import NXOpen
## 
##         Represents the paint parameter data which stored in ship design feature parms.        
##      
## 
##   <br>  Created in NX1980.0.0  <br> 

class PaintParametersData(NXOpen.TransientObject): 
    """
        Represents the paint parameter data which stored in ship design feature parms.        
     """


    ##  Represents the different spreadsheet parameter status 
    ##  User select paint to target in UI 
    class JaShipPaintParametersStatus(Enum):
        """
        Members Include: <Selected>
        """
        Selected: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PaintParametersData.JaShipPaintParametersStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Clear the catogory of spreadsheet parameter. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    @staticmethod
    def ClearCatogoryToKruDataPtrMap(spreadsheetData: PaintParametersData) -> None:
        """
         Clear the catogory of spreadsheet parameter. 
        """
        pass
    
    ##  Dispose the paint parameter data object 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(spreadsheetData: PaintParametersData) -> None:
        """
         Dispose the paint parameter data object 
        """
        pass
    
    ##  Modify the paint parameter data parameter. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  the parameter name 
    def EditParameter(spreadsheetData: PaintParametersData, parameterName: str, parameterValue: str) -> None:
        """
         Modify the paint parameter data parameter. 
        """
        pass
    
    ##  Modify the paint parameter primary data parameter. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  the parameter name 
    def EditPrimaryParameter(spreadsheetData: PaintParametersData, parameterName: str, parameterValue: str) -> None:
        """
         Modify the paint parameter primary data parameter. 
        """
        pass
    
    ##  Get checked parameters. 
    ##  @return checkedPara (@link PaintParametersParameterValue List[NXOpen.ShipDesign.PaintParametersParameterValue]@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCheckedParameters(spreadsheetData: PaintParametersData) -> List[PaintParametersParameterValue]:
        """
         Get checked parameters. 
         @return checkedPara (@link PaintParametersParameterValue List[NXOpen.ShipDesign.PaintParametersParameterValue]@endlink): .
        """
        pass
    
    ##  Refresh and reset parent parameter. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    @staticmethod
    def RefreshParentParameter(spreadsheetData: PaintParametersData) -> None:
        """
         Refresh and reset parent parameter. 
        """
        pass
    
    ##  Sets the Lock/Hide or other status of additional paint parameter data parameter. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  the parameter name 
    def SetPaintParameterStatus(spreadsheetData: PaintParametersData, parameterName: str, parameterStatus: int, isAdd: bool) -> None:
        """
         Sets the Lock/Hide or other status of additional paint parameter data parameter. 
        """
        pass
    
    ##  Sets the Lock/Hide or other status of paint parameter data parameter. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
    ##  the parameter name 
    def SetParameterStatus(spreadsheetData: PaintParametersData, parameterName: str, parameterStatus: int, isAdd: bool) -> None:
        """
         Sets the Lock/Hide or other status of paint parameter data parameter. 
        """
        pass
    
import NXOpen
## 
##         Represents the Paint Parameters Parameter Value which stored in ship design feature parms.        
##      
## 
##   <br>  Created in NX1980.0.0  <br> 

class PaintParametersParameterValue(NXOpen.TransientObject): 
    """
        Represents the Paint Parameters Parameter Value which stored in ship design feature parms.        
     """


    ##  Dispose the paint parameters parameter value object 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(parameterValue: PaintParametersParameterValue) -> None:
        """
         Dispose the paint parameters parameter value object 
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents the ship navigator node builder to add or edit ship navigator node.  <br> To create a new instance of this class, use @link NXOpen::ShipDesign::NavigatorCollection::CreateShipNavigatorNodeBuilder  NXOpen::ShipDesign::NavigatorCollection::CreateShipNavigatorNodeBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class ShipNavigatorNodeBuilder(NXOpen.Builder): 
    """ Represents the ship navigator node builder to add or edit ship navigator node. """


    ##  Settings to indicate the type of ship navigator node.  
    ##  The object node type. 
    class NodeTypes(Enum):
        """
        Members Include: <Object> <Part> <Container>
        """
        Object: int
        Part: int
        Container: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ShipNavigatorNodeBuilder.NodeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) ExpandChildNodes
    ##   the setting indicates if the node we create or edit will expand its children in ship navigator.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def ExpandChildNodes(self) -> bool:
        """
        Getter for property: (bool) ExpandChildNodes
          the setting indicates if the node we create or edit will expand its children in ship navigator.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ExpandChildNodes

    ##   the setting indicates if the node we create or edit will expand its children in ship navigator.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ExpandChildNodes.setter
    def ExpandChildNodes(self, expandNode: bool):
        """
        Setter for property: (bool) ExpandChildNodes
          the setting indicates if the node we create or edit will expand its children in ship navigator.  
             
         
        """
        pass
    
    ## Getter for property: (str) NodeName
    ##   the ship navigator node name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def NodeName(self) -> str:
        """
        Getter for property: (str) NodeName
          the ship navigator node name.  
             
         
        """
        pass
    
    ## Setter for property: (str) NodeName

    ##   the ship navigator node name.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @NodeName.setter
    def NodeName(self, nodeName: str):
        """
        Setter for property: (str) NodeName
          the ship navigator node name.  
             
         
        """
        pass
    
    ## Getter for property: (@link ShipNavigatorNodeBuilder.NodeTypes NXOpen.ShipDesign.ShipNavigatorNodeBuilder.NodeTypes@endlink) NodeType
    ##   the ship navigator node type, which can be object, part or container.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return ShipNavigatorNodeBuilder.NodeTypes
    @property
    def NodeType(self) -> ShipNavigatorNodeBuilder.NodeTypes:
        """
        Getter for property: (@link ShipNavigatorNodeBuilder.NodeTypes NXOpen.ShipDesign.ShipNavigatorNodeBuilder.NodeTypes@endlink) NodeType
          the ship navigator node type, which can be object, part or container.  
             
         
        """
        pass
    
    ## Setter for property: (@link ShipNavigatorNodeBuilder.NodeTypes NXOpen.ShipDesign.ShipNavigatorNodeBuilder.NodeTypes@endlink) NodeType

    ##   the ship navigator node type, which can be object, part or container.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @NodeType.setter
    def NodeType(self, type: ShipNavigatorNodeBuilder.NodeTypes):
        """
        Setter for property: (@link ShipNavigatorNodeBuilder.NodeTypes NXOpen.ShipDesign.ShipNavigatorNodeBuilder.NodeTypes@endlink) NodeType
          the ship navigator node type, which can be object, part or container.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) SourceFeatures
    ##   the list of features used to create ship navigator object node.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Features.SelectFeatureList
    @property
    def SourceFeatures(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) SourceFeatures
          the list of features used to create ship navigator object node.  
             
         
        """
        pass
    
    ## Getter for property: (@link SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) SourceParts
    ##   the list of parts used to create ship navigator part nodes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return SelectComponentList
    @property
    def SourceParts(self) -> SelectComponentList:
        """
        Getter for property: (@link SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) SourceParts
          the list of parts used to create ship navigator part nodes.  
             
         
        """
        pass
    
import NXOpen
##  Represents the interface for ship navigator root classes.  <br> An instance of this class can be obtained from @link NXOpen::ShipDesign::NavigatorCollection::GetShipNavigatorRoot NXOpen::ShipDesign::NavigatorCollection::GetShipNavigatorRoot@endlink   <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class ShipNavigatorRoot(NXOpen.NXObject): 
    """ Represents the interface for ship navigator root classes. """
    pass


import NXOpen
##  Represents Ship session  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ShipSession(NXOpen.Object): 
    """ Represents Ship session """


    ##  Returns the @link NXOpen::ShipDesign::NavigatorCollection NXOpen::ShipDesign::NavigatorCollection@endlink  belonging to this session 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @link NavigatorCollection NXOpen.ShipDesign.NavigatorCollection@endlink
    @property
    def Navigators() -> NavigatorCollection:
        """
         Returns the @link NXOpen::ShipDesign::NavigatorCollection NXOpen::ShipDesign::NavigatorCollection@endlink  belonging to this session 
        """
        pass
    
    ##  Returns the @link NXOpen::ShipDesign::Generator NXOpen::ShipDesign::Generator@endlink  belonging to this session 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @link Generator NXOpen.ShipDesign.Generator@endlink
    @property
    def Generator() -> Generator:
        """
         Returns the @link NXOpen::ShipDesign::Generator NXOpen::ShipDesign::Generator@endlink  belonging to this session 
        """
        pass
    
    ##  Returns the @link NXOpen::ShipDesign::GeneralArrangementManager NXOpen::ShipDesign::GeneralArrangementManager@endlink  belonging to this session 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link GeneralArrangementManager NXOpen.ShipDesign.GeneralArrangementManager@endlink
    @property
    def GeneralArrangement() -> GeneralArrangementManager:
        """
         Returns the @link NXOpen::ShipDesign::GeneralArrangementManager NXOpen::ShipDesign::GeneralArrangementManager@endlink  belonging to this session 
        """
        pass
    
    ##  Returns the @link NXOpen::ShipDesign::ApplicationUtils NXOpen::ShipDesign::ApplicationUtils@endlink  belonging to this session 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @link ApplicationUtils NXOpen.ShipDesign.ApplicationUtils@endlink
    @property
    def ApplicationUtils() -> ApplicationUtils:
        """
         Returns the @link NXOpen::ShipDesign::ApplicationUtils NXOpen::ShipDesign::ApplicationUtils@endlink  belonging to this session 
        """
        pass
    
## @package NXOpen.ShipDesign
## Classes, Enums and Structs under NXOpen.ShipDesign namespace

##  @link GeneratorClashType NXOpen.ShipDesign.GeneratorClashType @endlink is an alias for @link Generator.ClashType NXOpen.ShipDesign.Generator.ClashType@endlink
GeneratorClashType = Generator.ClashType


##  @link PaintParametersDataJaShipPaintParametersStatus NXOpen.ShipDesign.PaintParametersDataJaShipPaintParametersStatus @endlink is an alias for @link PaintParametersData.JaShipPaintParametersStatus NXOpen.ShipDesign.PaintParametersData.JaShipPaintParametersStatus@endlink
PaintParametersDataJaShipPaintParametersStatus = PaintParametersData.JaShipPaintParametersStatus


##  @link ShipNavigatorNodeBuilderNodeTypes NXOpen.ShipDesign.ShipNavigatorNodeBuilderNodeTypes @endlink is an alias for @link ShipNavigatorNodeBuilder.NodeTypes NXOpen.ShipDesign.ShipNavigatorNodeBuilder.NodeTypes@endlink
ShipNavigatorNodeBuilderNodeTypes = ShipNavigatorNodeBuilder.NodeTypes


