from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Assemblies
import NXOpen.ShipDesign
##  Represents the interface for Context Menu  <br> To obtain an instance of this class, refer to @link NXOpen::StructureDesign::StructureDesignSession  NXOpen::StructureDesign::StructureDesignSession @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ContextMenu(NXOpen.Object): 
    """ Represents the interface for Context Menu """


    ##  Represents display color type. 
    ##  show stock color 
    class DisplayColorType(Enum):
        """
        Members Include: <ShowStock> <ShowWeld>
        """
        ShowStock: int
        ShowWeld: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ContextMenu.DisplayColorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Deletes weldment node under consolidate list. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ##  ship navigator id 
    def DeleteWeldmentNode(tWeldmentNode: NXOpen.ShipDesign.NavigatorNode, index: int) -> None:
        """
         Deletes weldment node under consolidate list. 
        """
        pass
    
    ##  Packs members in navigator for structure design 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## <param name="tgNodes"> (@link NXOpen.ShipDesign.NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink) </param>
    ## <param name="tgStructurePart"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) </param>
    def PackMemberNodes(tgNodes: List[NXOpen.ShipDesign.NavigatorNode], tgStructurePart: NXOpen.Assemblies.Component) -> None:
        """
         Packs members in navigator for structure design 
        """
        pass
    
    ##  Remove consolidate list components and navigator node 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## <param name="consolidateListNodeTag"> (@link NXOpen.ShipDesign.NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink) </param>
    @staticmethod
    def RemoveConsolidateList(consolidateListNodeTag: NXOpen.ShipDesign.NavigatorNode) -> None:
        """
         Remove consolidate list components and navigator node 
        """
        pass
    
    ##  Removes bolted Connection feature inside the components. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## <param name="components"> (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink) </param>
    @staticmethod
    def RemoveFeaturesInsideBoltedConnectionComponents(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes bolted Connection feature inside the components. 
        """
        pass
    
    ##  Removes End Cap feature inside the components. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## <param name="components"> (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink) </param>
    @staticmethod
    def RemoveFeaturesInsideEndCapComponents(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes End Cap feature inside the components. 
        """
        pass
    
    ##  Removes Member feature inside the components. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## <param name="components"> (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink) </param>
    @staticmethod
    def RemoveFeaturesInsideMemberComponents(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes Member feature inside the components. 
        """
        pass
    
    ##  Removes Mounting Feet feature inside the components. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## <param name="components"> (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink) </param>
    @staticmethod
    def RemoveFeaturesInsideMountingFeetComponents(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes Mounting Feet feature inside the components. 
        """
        pass
    
    ##  Removes stiffener feature inside the components. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## <param name="components"> (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink) </param>
    @staticmethod
    def RemoveFeaturesInsideStiffenerComponents(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes stiffener feature inside the components. 
        """
        pass
    
    ##  Remove external component from consolidate list. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## <param name="tgNodes"> (@link NXOpen.ShipDesign.NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink) </param>
    @staticmethod
    def RemoveFromConsolidateList(tgNodes: List[NXOpen.ShipDesign.NavigatorNode]) -> None:
        """
         Remove external component from consolidate list. 
        """
        pass
    
    ##  Reparents part node under consolidate list. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ##  ship navigator id 
    def ReparentPartNodes(index: int, tgTargetNode: NXOpen.ShipDesign.NavigatorNode, tgNodes: List[NXOpen.ShipDesign.NavigatorNode]) -> None:
        """
         Reparents part node under consolidate list. 
        """
        pass
    
    ##  Unpacks members in navigator for structure design 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## <param name="tgNodes"> (@link NXOpen.ShipDesign.NavigatorNode List[NXOpen.ShipDesign.NavigatorNode]@endlink) </param>
    ## <param name="tgStructurePart"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) </param>
    def UnpackMemberNodes(tgNodes: List[NXOpen.ShipDesign.NavigatorNode], tgStructurePart: NXOpen.Assemblies.Component) -> None:
        """
         Unpacks members in navigator for structure design 
        """
        pass
    
    ## Show or clear physics color.  
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="displayType"> (@link ContextMenu.DisplayColorType NXOpen.StructureDesign.ContextMenu.DisplayColorType@endlink) </param>
    @staticmethod
    def UpdateDisplayColorType(displayType: ContextMenu.DisplayColorType) -> None:
        """
        Show or clear physics color.  
        """
        pass
    
    ##   Updates attributes on the structure curves or edges. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ##  curve or edge
    @staticmethod
    def UpdateStructure(curves: List[NXOpen.NXObject]) -> None:
        """
          Updates attributes on the structure curves or edges. 
        """
        pass
    
import NXOpen
import NXOpen.Features.StructureDesign
## 
##         Represents the Frame task environment associated with a session.
##      <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class FrameTaskEnvironment(NXOpen.Object): 
    """
        Represents the Frame task environment associated with a session.
    """


    ## Getter for property: (@link NXOpen.Features.StructureDesign.SuperFrame NXOpen.Features.StructureDesign.SuperFrame@endlink) ActiveFeature
    ##   the active SuperFrame feature.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Features.StructureDesign.SuperFrame
    @property
    def ActiveFeature(self) -> NXOpen.Features.StructureDesign.SuperFrame:
        """
        Getter for property: (@link NXOpen.Features.StructureDesign.SuperFrame NXOpen.Features.StructureDesign.SuperFrame@endlink) ActiveFeature
          the active SuperFrame feature.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Features.StructureDesign.SuperFrame NXOpen.Features.StructureDesign.SuperFrame@endlink) ActiveFeature

    ##   the active SuperFrame feature.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ActiveFeature.setter
    def ActiveFeature(self, feature: NXOpen.Features.StructureDesign.SuperFrame):
        """
        Setter for property: (@link NXOpen.Features.StructureDesign.SuperFrame NXOpen.Features.StructureDesign.SuperFrame@endlink) ActiveFeature
          the active SuperFrame feature.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes@endlink) BaseType
    ##   the active base type for the Frame command.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes
    @property
    def BaseType(self) -> NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes:
        """
        Getter for property: (@link NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes@endlink) BaseType
          the active base type for the Frame command.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes@endlink) BaseType

    ##   the active base type for the Frame command.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @BaseType.setter
    def BaseType(self, type: NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes):
        """
        Setter for property: (@link NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes@endlink) BaseType
          the active base type for the Frame command.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes@endlink) TransformType
    ##   the active transform type for the Move/Copy Curve commands.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes
    @property
    def TransformType(self) -> NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes:
        """
        Getter for property: (@link NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes@endlink) TransformType
          the active transform type for the Move/Copy Curve commands.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes@endlink) TransformType

    ##   the active transform type for the Move/Copy Curve commands.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @TransformType.setter
    def TransformType(self, type: NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes):
        """
        Setter for property: (@link NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes@endlink) TransformType
          the active transform type for the Move/Copy Curve commands.  
             
         
        """
        pass
    
    ##  Sets the frame to be edited and marks the task to be in edit mode. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## <param name="feature"> (@link NXOpen.Features.StructureDesign.SuperFrame NXOpen.Features.StructureDesign.SuperFrame@endlink) </param>
    @staticmethod
    def Edit(feature: NXOpen.Features.StructureDesign.SuperFrame) -> None:
        """
         Sets the frame to be edited and marks the task to be in edit mode. 
        """
        pass
    
    ##  Starts the Frame task environment.
    ##             This method should not be called if already in the Frame task environment.
    ##         
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def Enter() -> None:
        """
         Starts the Frame task environment.
                    This method should not be called if already in the Frame task environment.
                
        """
        pass
    
    ##  Ends the Frame task environment.
    ##         
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def Exit() -> None:
        """
         Ends the Frame task environment.
                
        """
        pass
    
    ##  Marks the task to be cancelled such that during @link FrameTaskEnvironment::Exit FrameTaskEnvironment::Exit@endlink 
    ##             task is undone and all the changes are discarded.
    ##         
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def SetCancelled() -> None:
        """
         Marks the task to be cancelled such that during @link FrameTaskEnvironment::Exit FrameTaskEnvironment::Exit@endlink 
                    task is undone and all the changes are discarded.
                
        """
        pass
    
import NXOpen
##  Represents the interface for structure design navigator root classes.  <br> An instance of this class can be obtained from @link NXOpen::StructureDesign::StructureDesignSession::GetStructureDesignNavigatorRoot NXOpen::StructureDesign::StructureDesignSession::GetStructureDesignNavigatorRoot@endlink   <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class StructureDesignNavigatorRoot(NXOpen.NXObject): 
    """ Represents the interface for structure design navigator root classes. """
    pass


import NXOpen
import NXOpen.Features.StructureDesign
##  Represents StructureDesign session  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class StructureDesignSession(NXOpen.Object): 
    """ Represents StructureDesign session """


    ##  Returns the @link NXOpen::StructureDesign::ContextMenu NXOpen::StructureDesign::ContextMenu@endlink  belonging to this session 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @link ContextMenu NXOpen.StructureDesign.ContextMenu@endlink
    @property
    def ContextMenu() -> ContextMenu:
        """
         Returns the @link NXOpen::StructureDesign::ContextMenu NXOpen::StructureDesign::ContextMenu@endlink  belonging to this session 
        """
        pass
    
    ##  Get related corner objects from a member body
    ##  @return corners (@link NXOpen.Features.StructureDesign.Corner List[NXOpen.Features.StructureDesign.Corner]@endlink): .
    ## 
    ##   <br>  Created in NX2306.7000.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## <param name="memberBody"> (@link NXOpen.Body NXOpen.Body@endlink) </param>
    @staticmethod
    def AskCornerObjects(memberBody: NXOpen.Body) -> List[NXOpen.Features.StructureDesign.Corner]:
        """
         Get related corner objects from a member body
         @return corners (@link NXOpen.Features.StructureDesign.Corner List[NXOpen.Features.StructureDesign.Corner]@endlink): .
        """
        pass
    
    ##  Get related member bodies from a corner object
    ##  @return members (@link NXOpen.Body List[NXOpen.Body]@endlink): .
    ## 
    ##   <br>  Created in NX2306.7000.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## <param name="corner"> (@link NXOpen.Features.StructureDesign.Corner NXOpen.Features.StructureDesign.Corner@endlink) </param>
    @staticmethod
    def AskMembers(corner: NXOpen.Features.StructureDesign.Corner) -> List[NXOpen.Body]:
        """
         Get related member bodies from a corner object
         @return members (@link NXOpen.Body List[NXOpen.Body]@endlink): .
        """
        pass
    
    ##  Establish structure design navigator root 
    ##  @return navRoot (@link StructureDesignNavigatorRoot NXOpen.StructureDesign.StructureDesignNavigatorRoot@endlink):  .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def GetStructureDesignNavigatorRoot() -> StructureDesignNavigatorRoot:
        """
         Establish structure design navigator root 
         @return navRoot (@link StructureDesignNavigatorRoot NXOpen.StructureDesign.StructureDesignNavigatorRoot@endlink):  .
        """
        pass
    
## @package NXOpen.StructureDesign
## Classes, Enums and Structs under NXOpen.StructureDesign namespace

##  @link ContextMenuDisplayColorType NXOpen.StructureDesign.ContextMenuDisplayColorType @endlink is an alias for @link ContextMenu.DisplayColorType NXOpen.StructureDesign.ContextMenu.DisplayColorType@endlink
ContextMenuDisplayColorType = ContextMenu.DisplayColorType


