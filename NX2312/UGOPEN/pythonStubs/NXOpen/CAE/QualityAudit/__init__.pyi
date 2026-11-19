from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##   @brief  The Quality Audit ActionList class offers means to select, deselect, obtain @link NXOpen::CAE::QualityAudit::Action NXOpen::CAE::QualityAudit::Action@endlink  instances. 
## 
##    <br> To obtain the instance of this class access @link CAE::QualityAudit::Manager::ActionList CAE::QualityAudit::Manager::ActionList@endlink  of  @link CAE::QualityAudit::Manager CAE::QualityAudit::Manager@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ActionList(NXOpen.NXObject): 
    """ <summary> The Quality Audit ActionList class offers means to select, deselect, obtain <ja_class>NXOpen.CAE.QualityAudit.Action</ja_class> instances.</summary> """


    ##  Deselect the specified action to avoid using it in the quality audit.
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  The action to be deselected 
    def Deselect(pSelfActionList: ActionList, pAction: Action) -> None:
        """
         Deselect the specified action to avoid using it in the quality audit.
                     
        """
        pass
    
    ##  Deselect all available actions.
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def DeselectAll(pSelfActionList: ActionList) -> None:
        """
         Deselect all available actions.
                     
        """
        pass
    
    ##  Get the action by id. See @link NXOpen::CAE::QualityAudit::Action::Id NXOpen::CAE::QualityAudit::Action::Id@endlink  for full the list of actions.
    ##              
    ##  @return action (@link Action NXOpen.CAE.QualityAudit.Action@endlink):  Corresponding action .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Action id. See @link NXOpen::CAE::QualityAudit::Action::Id NXOpen::CAE::QualityAudit::Action::Id@endlink  
    def GetAction(pSelfActionList: ActionList, id: Action.Id) -> Action:
        """
         Get the action by id. See @link NXOpen::CAE::QualityAudit::Action::Id NXOpen::CAE::QualityAudit::Action::Id@endlink  for full the list of actions.
                     
         @return action (@link Action NXOpen.CAE.QualityAudit.Action@endlink):  Corresponding action .
        """
        pass
    
    ##  Returns an array of all selected actions.
    ##              
    ##  @return pActions (@link Action List[NXOpen.CAE.QualityAudit.Action]@endlink):  The selected actions .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedActions(pSelfActionList: ActionList) -> List[Action]:
        """
         Returns an array of all selected actions.
                     
         @return pActions (@link Action List[NXOpen.CAE.QualityAudit.Action]@endlink):  The selected actions .
        """
        pass
    
    ##  Tells if the action is to be used in the quality audit.
    ##              
    ##  @return pSelected (bool):  .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  The action to be checked if selected or not 
    def IsSelected(pSelfActionList: ActionList, pAction: Action) -> bool:
        """
         Tells if the action is to be used in the quality audit.
                     
         @return pSelected (bool):  .
        """
        pass
    
    ##  Import action settings from file
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="actionConfigFile"> (str) </param>
    def LoadActionSettings(pSelfActionList: ActionList, actionConfigFile: str) -> None:
        """
         Import action settings from file
                     
        """
        pass
    
    ##  Export action settings to file
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="actionConfigFile"> (str) </param>
    def SaveActionSettings(pSelfActionList: ActionList, actionConfigFile: str) -> None:
        """
         Export action settings to file
                     
        """
        pass
    
    ##  Select the specified action to be used in the quality audit.
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  The action to be selected 
    def Select(pSelfActionList: ActionList, pAction: Action) -> None:
        """
         Select the specified action to be used in the quality audit.
                     
        """
        pass
    
    ##  Select all the actions available.
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SelectAll(pSelfActionList: ActionList) -> None:
        """
         Select all the actions available.
                     
        """
        pass
    
import NXOpen
import NXOpen.CAE.Connections
##   @brief  The Quality Audit ActionSettings is the base class for @link NXOpen::CAE::QualityAudit::Action NXOpen::CAE::QualityAudit::Action@endlink  settings. It provides basic functionality. 
## 
##    <br> Settings instances can be obtained via @link NXOpen::CAE::QualityAudit::Action::Settings NXOpen::CAE::QualityAudit::Action::Settings@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ActionSettings(NXOpen.NXObject): 
    """ <summary> The Quality Audit ActionSettings is the base class for <ja_class>NXOpen.CAE.QualityAudit.Action</ja_class> settings. It provides basic functionality.</summary> """


    ## Getter for property: (@link Action NXOpen.CAE.QualityAudit.Action@endlink) Action
    ##   the action using these settings   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return Action
    @property
    def Action(self) -> Action:
        """
        Getter for property: (@link Action NXOpen.CAE.QualityAudit.Action@endlink) Action
          the action using these settings   
            
         
        """
        pass
    
    ##  Sets the override flag of settings for the specified connection type.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connectionType"> (@link NXOpen.CAE.Connections.ConnectionType NXOpen.CAE.Connections.ConnectionType@endlink) </param>
    ## <param name="allowOverride"> (bool) </param>
    def AllowOverride(pSettings: ActionSettings, connectionType: NXOpen.CAE.Connections.ConnectionType, allowOverride: bool) -> None:
        """
         Sets the override flag of settings for the specified connection type.
        """
        pass
    
    ##  Tells if overriding is allowed for the specified connection type.
    ##  @return canOverride (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connectionType"> (@link NXOpen.CAE.Connections.ConnectionType NXOpen.CAE.Connections.ConnectionType@endlink) </param>
    def CanOverride(pSettings: ActionSettings, connectionType: NXOpen.CAE.Connections.ConnectionType) -> bool:
        """
         Tells if overriding is allowed for the specified connection type.
         @return canOverride (bool): .
        """
        pass
    
    ##  The supported connection types using the settings 
    ##  @return supportedConnections (@link NXOpen.CAE.Connections.ConnectionType List[NXOpen.CAE.Connections.ConnectionType]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSupportedConnectionTypes(pSettings: ActionSettings) -> List[NXOpen.CAE.Connections.ConnectionType]:
        """
         The supported connection types using the settings 
         @return supportedConnections (@link NXOpen.CAE.Connections.ConnectionType List[NXOpen.CAE.Connections.ConnectionType]@endlink): .
        """
        pass
    
    ##  Reset the action settings to default values 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def ResetToDefaults(pSettings: ActionSettings) -> None:
        """
         Reset the action settings to default values 
        """
        pass
    
import NXOpen
##   @brief  The Quality Audit Action is a base class that performs actions on a list of objects. Results of the action are also stored here. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Action(NXOpen.NXObject): 
    """ <summary> The Quality Audit Action is a base class that performs actions on a list of objects. Results of the action are also stored here.</summary> """


    ##  Action ids. Each action can be identified through an unique id. 
    ##  the action that lists all connections 
    class Id(Enum):
        """
        Members Include: <AllConnectionsList> <NonModeledConnectionsList> <SubAssemblyComponentCheck> <SubAssemblyMeshCheck> <ObjectLevelProjectionCheck> <MeshLevelProjectionCheck> <DistanceBetweenConnectionPointsCheck> <DistanceBetweenConnectionsCheck> <FreeEdgeDistanceCheck> <TargetSequenceCheck> <ObjectLevelLengthCheck> <MeshLevelLengthCheck> <ObjectLevelLengthRatioCheck> <MeshLevelLengthRatioCheck> <ObjectLevelConnectionAngleCheck> <MeshLevelConnectionAngleCheck> <ObjectLevelFlatnessCheck> <MeshLevelFlatnessCheck> <ConnectionSynthesis>
        """
        AllConnectionsList: int
        NonModeledConnectionsList: int
        SubAssemblyComponentCheck: int
        SubAssemblyMeshCheck: int
        ObjectLevelProjectionCheck: int
        MeshLevelProjectionCheck: int
        DistanceBetweenConnectionPointsCheck: int
        DistanceBetweenConnectionsCheck: int
        FreeEdgeDistanceCheck: int
        TargetSequenceCheck: int
        ObjectLevelLengthCheck: int
        MeshLevelLengthCheck: int
        ObjectLevelLengthRatioCheck: int
        MeshLevelLengthRatioCheck: int
        ObjectLevelConnectionAngleCheck: int
        MeshLevelConnectionAngleCheck: int
        ObjectLevelFlatnessCheck: int
        MeshLevelFlatnessCheck: int
        ConnectionSynthesis: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Action.Id:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link Action.Id NXOpen.CAE.QualityAudit.Action.Id@endlink) ActionId
    ##   the action id
    ##                
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return Action.Id
    @property
    def ActionId(self) -> Action.Id:
        """
        Getter for property: (@link Action.Id NXOpen.CAE.QualityAudit.Action.Id@endlink) ActionId
          the action id
                       
            
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##   the action description
    ##                
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the action description
                       
            
         
        """
        pass
    
    ## Getter for property: (@link ActionSettings NXOpen.CAE.QualityAudit.ActionSettings@endlink) Settings
    ##   the action settings
    ##                
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ActionSettings
    @property
    def Settings(self) -> ActionSettings:
        """
        Getter for property: (@link ActionSettings NXOpen.CAE.QualityAudit.ActionSettings@endlink) Settings
          the action settings
                       
            
         
        """
        pass
    
    ##  Export results to file
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultsFIle"> (str) </param>
    def ExportResults(pSelfAction: Action, resultsFIle: str) -> None:
        """
         Export results to file
        """
        pass
    
    ##  Get the @link CAE::QualityAudit::Result CAE::QualityAudit::Result@endlink  list obtained from the latest check
    ##              
    ##  @return pResults (@link Result List[NXOpen.CAE.QualityAudit.Result]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetResults(pSelfAction: Action) -> List[Result]:
        """
         Get the @link CAE::QualityAudit::Result CAE::QualityAudit::Result@endlink  list obtained from the latest check
                     
         @return pResults (@link Result List[NXOpen.CAE.QualityAudit.Result]@endlink): .
        """
        pass
    
    ##  Performs the action on the given object list.
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def Perform(pSelfAction: Action, objects: List[NXOpen.NXObject]) -> None:
        """
         Performs the action on the given object list.
                     
        """
        pass
    
##   @brief  This action has as result groups of connected components. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ComponentConnectivity(Action): 
    """ <summary> This action has as result groups of connected components.</summary> """
    pass


import NXOpen.Assemblies
##   @brief  This result a group of connected components. 
## 
##    <br> To obtain this result see @link CAE::QualityAudit::ComponentConnectivity CAE::QualityAudit::ComponentConnectivity@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ComponentSubResult(Result): 
    """ <summary> This result a group of connected components.</summary> """


    ##  Gets the component of this sub-result 
    ##  @return component (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetComponent(pThis: ComponentSubResult) -> NXOpen.Assemblies.Component:
        """
         Gets the component of this sub-result 
         @return component (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink): .
        """
        pass
    
##   @brief  This result a group of connected components. 
## 
##    <br> To obtain this result see @link CAE::QualityAudit::ComponentConnectivity CAE::QualityAudit::ComponentConnectivity@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ConnectedComponentsGroupResult(Result): 
    """ <summary> This result a group of connected components.</summary> """
    pass


##   @brief  This result a group of connected meshes. 
## 
##    <br> To obtain this result see @link CAE::QualityAudit::MeshConnectivity CAE::QualityAudit::MeshConnectivity@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ConnectedMeshesGroupResult(Result): 
    """ <summary> This result a group of connected meshes.</summary> """
    pass


##   @brief  This action checks the distance between connections. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ConnectionDistanceCheck(Action): 
    """ <summary> This action checks the distance between connections.</summary> """
    pass


import NXOpen
import NXOpen.CAE.Connections
##   @brief  The Quality Audit ConnectionPointsDistanceResult is a class containing information about failed distance between connection distance checks on universal connections. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ConnectionDistanceCheck CAE::QualityAudit::ConnectionDistanceCheck@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ConnectionDistanceResult(Result): 
    """ <summary> The Quality Audit ConnectionPointsDistanceResult is a class containing information about failed distance between connection distance checks on universal connections.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection1
    ##   the first connection.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection1(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection1
          the first connection.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection2
    ##   the second connection.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection2(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection2
          the second connection.  
            
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex1
    ##   the coordinate index of the first point.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex1(self) -> int:
        """
        Getter for property: (int) CoordinateIndex1
          the coordinate index of the first point.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex2
    ##   the coordinate index of the second point.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex2(self) -> int:
        """
        Getter for property: (int) CoordinateIndex2
          the coordinate index of the second point.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Coordinates1
    ##   the coordinates of the first point.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Coordinates1(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Coordinates1
          the coordinates of the first point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Coordinates2
    ##   the coordinates of the second point.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Coordinates2(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Coordinates2
          the coordinates of the second point.  
             
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex1
    ##   the definition index of the first point.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex1(self) -> int:
        """
        Getter for property: (int) DefinitionIndex1
          the definition index of the first point.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex2
    ##   the definition index of the second point.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex2(self) -> int:
        """
        Getter for property: (int) DefinitionIndex2
          the definition index of the second point.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (float) Distance
    ##   the distance between the two connections.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
          the distance between the two connections.  
              
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex1
    ##   the location index of the first point.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def LocationIndex1(self) -> int:
        """
        Getter for property: (int) LocationIndex1
          the location index of the first point.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex2
    ##   the location index of the second point.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def LocationIndex2(self) -> int:
        """
        Getter for property: (int) LocationIndex2
          the location index of the second point.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
##   @brief  This action checks the distance between connection's definition points. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ConnectionPointsDistanceCheck(Action): 
    """ <summary> This action checks the distance between connection's definition points.</summary> """
    pass


import NXOpen.CAE.Connections
##   @brief  The Quality Audit ConnectionPointsDistanceResult is a class containing information about failed distance between connection points checks on universal connections. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ConnectionPointsDistanceCheck CAE::QualityAudit::ConnectionPointsDistanceCheck@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ConnectionPointsDistanceResult(Result): 
    """ <summary> The Quality Audit ConnectionPointsDistanceResult is a class containing information about failed distance between connection points checks on universal connections.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection.  
             
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex1
    ##   the coordinate index of the first point in the first location.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex1(self) -> int:
        """
        Getter for property: (int) CoordinateIndex1
          the coordinate index of the first point in the first location.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex2
    ##   the coordinate index of the second point in the second location.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex2(self) -> int:
        """
        Getter for property: (int) CoordinateIndex2
          the coordinate index of the second point in the second location.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex1
    ##   the definition index of the first point.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex1(self) -> int:
        """
        Getter for property: (int) DefinitionIndex1
          the definition index of the first point.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex2
    ##   the definition index of the second point.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex2(self) -> int:
        """
        Getter for property: (int) DefinitionIndex2
          the definition index of the second point.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (float) Distance
    ##   the distance between the two points.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
          the distance between the two points.  
              
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex1
    ##   the location index of the first point.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def LocationIndex1(self) -> int:
        """
        Getter for property: (int) LocationIndex1
          the location index of the first point.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex2
    ##   the location index of the second point.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def LocationIndex2(self) -> int:
        """
        Getter for property: (int) LocationIndex2
          the location index of the second point.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  The ConnectionResult is a class containing information about connections found when performing the @link NXOpen::CAE::QualityAudit::ListConnections NXOpen::CAE::QualityAudit::ListConnections@endlink  action. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ListConnections CAE::QualityAudit::ListConnections@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ConnectionResult(Result): 
    """ <summary> The ConnectionResult is a class containing information about connections found when performing the <ja_class>NXOpen.CAE.QualityAudit.ListConnections</ja_class> action.</summary> """


    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Connection
    ##   the connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def Connection(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Connection
          the connection.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.FEModelOccurrence NXOpen.CAE.FEModelOccurrence@endlink) Femodel
    ##   the Fe Model of the connection when we're dealing with a non-occurrenceable connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.FEModelOccurrence
    @property
    def Femodel(self) -> NXOpen.CAE.FEModelOccurrence:
        """
        Getter for property: (@link NXOpen.CAE.FEModelOccurrence NXOpen.CAE.FEModelOccurrence@endlink) Femodel
          the Fe Model of the connection when we're dealing with a non-occurrenceable connection.  
             
         
        """
        pass
    
##   @brief  This action has as result the list of all connections from the specified model. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ConnectionSynthesis(Action): 
    """ <summary> This action has as result the list of all connections from the specified model.</summary> """
    pass


##   @brief  This result contains information about connection and the components it connects. It is the result of the @link NXOpen::CAE::QualityAudit::ComponentConnectivity NXOpen::CAE::QualityAudit::ComponentConnectivity@endlink  action. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ComponentConnectivity CAE::QualityAudit::ComponentConnectivity@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ConnectionWithComponentsResult(ConnectionResult): 
    """ <summary> This result contains information about connection and the components it connects. It is the result of the <ja_class>NXOpen.CAE.QualityAudit.ComponentConnectivity</ja_class> action.</summary> """
    pass


##   @brief  This result contains information about connection and the meshes it connects. It is the result of the @link NXOpen::CAE::QualityAudit::MeshConnectivity NXOpen::CAE::QualityAudit::MeshConnectivity@endlink  action. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::MeshConnectivity CAE::QualityAudit::MeshConnectivity@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ConnectionWithMeshesResult(ConnectionResult): 
    """ <summary> This result contains information about connection and the meshes it connects. It is the result of the <ja_class>NXOpen.CAE.QualityAudit.MeshConnectivity</ja_class> action.</summary> """
    pass


import NXOpen
##   @brief  This class contains the flatness settings available for the following actions: 
##         @link NXOpen::CAE::QualityAudit::ObjectLevelFlatnessCheck NXOpen::CAE::QualityAudit::ObjectLevelFlatnessCheck@endlink 
##         @link NXOpen::CAE::QualityAudit::MeshLevelFlatnessCheck NXOpen::CAE::QualityAudit::MeshLevelFlatnessCheck@endlink 
##         . 
## 
##    <br> To obtain an instance of this class get the @link NXOpen::CAE::QualityAudit::Action::Settings NXOpen::CAE::QualityAudit::Action::Settings@endlink  of classed using it.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class FlatnessSettings(ActionSettings): 
    """ <summary> This class contains the flatness settings available for the following actions: 
        <ja_class>NXOpen.CAE.QualityAudit.ObjectLevelFlatnessCheck</ja_class>
        <ja_class>NXOpen.CAE.QualityAudit.MeshLevelFlatnessCheck</ja_class>
        .</summary> """


    ## Getter for property: (bool) ClosestPointFlag
    ##   the closest point flag.  
    ##    If this flag is false it returns one of the points else it returns the closest point  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def ClosestPointFlag(self) -> bool:
        """
        Getter for property: (bool) ClosestPointFlag
          the closest point flag.  
           If this flag is false it returns one of the points else it returns the closest point  
         
        """
        pass
    
    ## Setter for property: (bool) ClosestPointFlag

    ##   the closest point flag.  
    ##    If this flag is false it returns one of the points else it returns the closest point  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ClosestPointFlag.setter
    def ClosestPointFlag(self, closestPointFlag: bool):
        """
        Setter for property: (bool) ClosestPointFlag
          the closest point flag.  
           If this flag is false it returns one of the points else it returns the closest point  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height required.  
    ##    For a greater height an error is reported   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height required.  
           For a greater height an error is reported   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Radius
    ##   the radius required.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Radius
          the radius required.  
             
         
        """
        pass
    
##   @brief  This action checks if there are connections that are too close to the edge based on a configurable tolerance. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class FreeEdgeDistanceCheck(Action): 
    """ <summary> This action checks if there are connections that are too close to the edge based on a configurable tolerance.</summary> """
    pass


import NXOpen
import NXOpen.CAE
import NXOpen.CAE.Connections
##   @brief  The Quality Audit FreeEdgeDistanceResult contains information about problematic places where distance between connection points and free edges is less than a given value. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::FreeEdgeDistanceCheck CAE::QualityAudit::FreeEdgeDistanceCheck@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class FreeEdgeDistanceResult(Result): 
    """ <summary> The Quality Audit FreeEdgeDistanceResult contains information about problematic places where distance between connection points and free edges is less than a given value.</summary> """


    ## Getter for property: (@link NXOpen.CAE.CAEEdge NXOpen.CAE.CAEEdge@endlink) CaeEdge
    ##   the CAE edge (if present).  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.CAEEdge
    @property
    def CaeEdge(self) -> NXOpen.CAE.CAEEdge:
        """
        Getter for property: (@link NXOpen.CAE.CAEEdge NXOpen.CAE.CAEEdge@endlink) CaeEdge
          the CAE edge (if present).  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection with points close to the edge   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection with points close to the edge   
            
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index of the close to the edge point in the location.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index of the close to the edge point in the location.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index of the point close to edge.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index of the point close to edge.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (float) Distance
    ##   the distance.  
    ##    See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
          the distance.  
           See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) EdgePoint
    ##   the edge point.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def EdgePoint(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) EdgePoint
          the edge point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.FEElemEdge NXOpen.CAE.FEElemEdge@endlink) FeElementEdge
    ##   the FE edge (if present).  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.FEElemEdge
    @property
    def FeElementEdge(self) -> NXOpen.CAE.FEElemEdge:
        """
        Getter for property: (@link NXOpen.CAE.FEElemEdge NXOpen.CAE.FEElemEdge@endlink) FeElementEdge
          the FE edge (if present).  
             
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index of the close to the edge point.  
    ##    See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index of the close to the edge point.  
           See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index of the point close to edge.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index of the point close to edge.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
    ##  The closest connection point. 
    ##  @return pointPosition (@link NXOpen.Point3d NXOpen.Point3d@endlink):  Closest connection point in ABS coordinates .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetClosestConnectionPoint(pResult: FreeEdgeDistanceResult) -> NXOpen.Point3d:
        """
         The closest connection point. 
         @return pointPosition (@link NXOpen.Point3d NXOpen.Point3d@endlink):  Closest connection point in ABS coordinates .
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##   @brief  This is an interface to obtain the connected components. 
## 
##   
## 
##   <br>  Created in NX1847.0.0  <br> 

class IConnectedComponents(NXOpen.INXObject): 
    """ <summary> This is an interface to obtain the connected components.</summary> """


    ##  Gets the connected components from a result 
    ##  @return components (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetComponents(result: IConnectedComponents) -> List[NXOpen.Assemblies.Component]:
        """
         Gets the connected components from a result 
         @return components (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  This is an interface to obtain the connected meshes. 
## 
##   
## 
##   <br>  Created in NX1847.0.0  <br> 

class IConnectedMeshes(NXOpen.INXObject): 
    """ <summary> This is an interface to obtain the connected meshes.</summary> """


    ##  Gets the connected meshes from a result 
    ##  @return meshes (@link NXOpen.CAE.Mesh List[NXOpen.CAE.Mesh]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetMeshes(result: IConnectedMeshes) -> List[NXOpen.CAE.Mesh]:
        """
         Gets the connected meshes from a result 
         @return meshes (@link NXOpen.CAE.Mesh List[NXOpen.CAE.Mesh]@endlink): .
        """
        pass
    
import NXOpen
##   @brief  The Quality Audit InputList class offers means to select, deselect, obtain the objects to be used by @link CAE::QualityAudit::Action CAE::QualityAudit::Action@endlink  instances. 
## 
##    <br> To obtain the instance of this class use @link CAE::QualityAudit::Manager::InputList CAE::QualityAudit::Manager::InputList@endlink  of  @link CAE::QualityAudit::Manager CAE::QualityAudit::Manager@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class InputList(NXOpen.NXObject): 
    """ <summary> The Quality Audit InputList class offers means to select, deselect, obtain the objects to be used by <ja_class>CAE.QualityAudit.Action</ja_class> instances.</summary> """


    ##  Mark the specified object to be excluded from the quality audit actions.
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="obj"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def Deselect(pSelfInputList: InputList, obj: NXOpen.NXObject) -> None:
        """
         Mark the specified object to be excluded from the quality audit actions.
                     
        """
        pass
    
    ##  Deselect all input from the @link CAE::QualityAudit::InputList CAE::QualityAudit::InputList@endlink .
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def DeselectAll(pSelfInputList: InputList) -> None:
        """
         Deselect all input from the @link CAE::QualityAudit::InputList CAE::QualityAudit::InputList@endlink .
                     
        """
        pass
    
    ##  Return all the objects available as input for the quality audit actions.
    ##              
    ##  @return pObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  Array of selected objects .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAllObjects(pSelfInputList: InputList) -> List[NXOpen.NXObject]:
        """
         Return all the objects available as input for the quality audit actions.
                     
         @return pObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  Array of selected objects .
        """
        pass
    
    ##  Return all the selected objects available as input to the quality audit actions.
    ##              
    ##  @return pObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  Array of selected objects .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def GetSelectedObjects(pSelfInputList: InputList) -> List[NXOpen.NXObject]:
        """
         Return all the selected objects available as input to the quality audit actions.
                     
         @return pObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  Array of selected objects .
        """
        pass
    
    ##  Tells if the specified object is included in the quality audit actions.
    ##              
    ##  @return pIsSelected (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="obj"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def IsSelected(pSelfInputList: InputList, obj: NXOpen.NXObject) -> bool:
        """
         Tells if the specified object is included in the quality audit actions.
                     
         @return pIsSelected (bool): .
        """
        pass
    
    ##  Mark the specified object to be included in the quality audit actions.
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="obj"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def Select(pSelfInputList: InputList, obj: NXOpen.NXObject) -> None:
        """
         Mark the specified object to be included in the quality audit actions.
                     
        """
        pass
    
    ##  Select all input from the @link CAE::QualityAudit::InputList CAE::QualityAudit::InputList@endlink .
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def SelectAll(pSelfInputList: InputList) -> None:
        """
         Select all input from the @link CAE::QualityAudit::InputList CAE::QualityAudit::InputList@endlink .
                     
        """
        pass
    
import NXOpen
import NXOpen.CAE.Connections
##   @brief  This class contains the length range settings available for the following actions: 
##         @link NXOpen::CAE::QualityAudit::ObjectLevelLengthRangeCheck NXOpen::CAE::QualityAudit::ObjectLevelLengthRangeCheck@endlink 
##         . 
## 
##    <br> To obtain an instance of this class get the @link NXOpen::CAE::QualityAudit::Action::Settings NXOpen::CAE::QualityAudit::Action::Settings@endlink  of classed using it.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LengthRangeSettings(ActionSettings): 
    """ <summary> This class contains the length range settings available for the following actions: 
        <ja_class>NXOpen.CAE.QualityAudit.ObjectLevelLengthRangeCheck</ja_class>
        .</summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumDistance
    ##   the maximum length required.  
    ##    For a greater distance an error is reported   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumDistance
          the maximum length required.  
           For a greater distance an error is reported   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumDistance
    ##   the minimum length required.  
    ##    For a lower distance an error is reported   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinimumDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumDistance
          the minimum length required.  
           For a lower distance an error is reported   
         
        """
        pass
    
    ##  The maximum length required for the specified connection type. For a greater distance an error is reported 
    ##  @return maximumDistance (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connectionType"> (@link NXOpen.CAE.Connections.ConnectionType NXOpen.CAE.Connections.ConnectionType@endlink) </param>
    def GetMaximumDistanceByConnectionType(pSelfAction: LengthRangeSettings, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The maximum length required for the specified connection type. For a greater distance an error is reported 
         @return maximumDistance (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  The minimum length required for the specified connection type. For a lower distance an error is reported 
    ##  @return minimumDistance (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connectionType"> (@link NXOpen.CAE.Connections.ConnectionType NXOpen.CAE.Connections.ConnectionType@endlink) </param>
    def GetMinimumDistanceByConnectionType(pSelfAction: LengthRangeSettings, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The minimum length required for the specified connection type. For a lower distance an error is reported 
         @return minimumDistance (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.CAE.Connections
##   @brief  This class contains the length ratio range settings available for the following actions: 
##         @link NXOpen::CAE::QualityAudit::ObjectLevelLengthRatioRangeCheck NXOpen::CAE::QualityAudit::ObjectLevelLengthRatioRangeCheck@endlink 
##         @link NXOpen::CAE::QualityAudit::MeshLevelLengthRatioRangeCheck NXOpen::CAE::QualityAudit::MeshLevelLengthRatioRangeCheck@endlink 
##         . 
## 
##    <br> To obtain an instance of this class get the @link NXOpen::CAE::QualityAudit::Action::Settings NXOpen::CAE::QualityAudit::Action::Settings@endlink  of classes using it.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class LengthRatioRangeSettings(ActionSettings): 
    """ <summary> This class contains the length ratio range settings available for the following actions: 
        <ja_class>NXOpen.CAE.QualityAudit.ObjectLevelLengthRatioRangeCheck</ja_class>
        <ja_class>NXOpen.CAE.QualityAudit.MeshLevelLengthRatioRangeCheck</ja_class>
        .</summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumRatio
    ##   the maximum length ratio range required.  
    ##    For a greater ratio an error is reported   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumRatio(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumRatio
          the maximum length ratio range required.  
           For a greater ratio an error is reported   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumRatio
    ##   the minimum length ratio required.  
    ##    For lower ratio an error is reported   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinimumRatio(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumRatio
          the minimum length ratio required.  
           For lower ratio an error is reported   
         
        """
        pass
    
    ##  The maximum ratio required for the specified connection type. For a greater ratio an error is reported 
    ##  @return maximumRatio (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connectionType"> (@link NXOpen.CAE.Connections.ConnectionType NXOpen.CAE.Connections.ConnectionType@endlink) </param>
    def GetMaximumRatioByConnectionType(pSelfAction: LengthRatioRangeSettings, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The maximum ratio required for the specified connection type. For a greater ratio an error is reported 
         @return maximumRatio (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
    ##  The minimum ratio required for the specified connection type. For lower ratio an error is reported 
    ##  @return minimumRatio (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connectionType"> (@link NXOpen.CAE.Connections.ConnectionType NXOpen.CAE.Connections.ConnectionType@endlink) </param>
    def GetMinimumRatioByConnectionType(pSelfAction: LengthRatioRangeSettings, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The minimum ratio required for the specified connection type. For lower ratio an error is reported 
         @return minimumRatio (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
##   @brief  This action has as result the list of all connections from the specified model. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ListConnections(Action): 
    """ <summary> This action has as result the list of all connections from the specified model.</summary> """
    pass


##   @brief  This action's output is a list of connections that are not realized. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ListNonModeledConnections(Action): 
    """ <summary> This action's output is a list of connections that are not realized.</summary> """
    pass


import NXOpen
##   @brief  The Quality Audit Manager class offers means to check for errors at assembly level  
## 
##    <br> To obtain an instance of this class use @link NXOpen::CAE::CaeSession::QualityAuditManager NXOpen::CAE::CaeSession::QualityAuditManager@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Manager(NXOpen.Object): 
    """ <summary> The Quality Audit Manager class offers means to check for errors at assembly level </summary> """


    ## Getter for property: (@link ActionList NXOpen.CAE.QualityAudit.ActionList@endlink) ActionList
    ##   the quality audit action list.  
    ##   
    ##                
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ActionList
    @property
    def ActionList(self) -> ActionList:
        """
        Getter for property: (@link ActionList NXOpen.CAE.QualityAudit.ActionList@endlink) ActionList
          the quality audit action list.  
          
                       
         
        """
        pass
    
    ## Getter for property: (@link InputList NXOpen.CAE.QualityAudit.InputList@endlink) InputList
    ##   the quality audit input list.  
    ##   
    ##                
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return InputList
    @property
    def InputList(self) -> InputList:
        """
        Getter for property: (@link InputList NXOpen.CAE.QualityAudit.InputList@endlink) InputList
          the quality audit input list.  
          
                       
         
        """
        pass
    
    ## Getter for property: (bool) UseInputListForSynthesis
    ##   the option to use the input list for the connections used in Connection Synthesis check
    ##                
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return bool
    @property
    def UseInputListForSynthesis(self) -> bool:
        """
        Getter for property: (bool) UseInputListForSynthesis
          the option to use the input list for the connections used in Connection Synthesis check
                       
            
         
        """
        pass
    
    ## Setter for property: (bool) UseInputListForSynthesis

    ##   the option to use the input list for the connections used in Connection Synthesis check
    ##                
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @UseInputListForSynthesis.setter
    def UseInputListForSynthesis(self, useInputList: bool):
        """
        Setter for property: (bool) UseInputListForSynthesis
          the option to use the input list for the connections used in Connection Synthesis check
                       
            
         
        """
        pass
    
    ##  Export results to file
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="actionsToExport"> (@link Action List[NXOpen.CAE.QualityAudit.Action]@endlink) </param>
    ## <param name="resultsFIle"> (str) </param>
    def ExportResults(actionsToExport: List[Action], resultsFIle: str) -> None:
        """
         Export results to file
        """
        pass
    
    ##  Finds the @link  NXOpen::INXObject   NXOpen::INXObject @endlink  with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  An object matching the journal identifier .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Journal identifier of the object 
    @staticmethod
    def FindObject(journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the @link  NXOpen::INXObject   NXOpen::INXObject @endlink  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
        
                    An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  An object matching the journal identifier .
        """
        pass
    
    ##  This method performs checks on the selected objects. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ##  The @link CAE::QualityAudit::Action CAE::QualityAudit::Action@endlink  array of actions to be performed. 
    def PerformActions(inputActions: List[Action], pObjects: List[NXOpen.NXObject]) -> None:
        """
         This method performs checks on the selected objects. 
        """
        pass
    
import NXOpen.CAE
##   @brief  The Quality Audit ManualElementsResult is a class containing information about nodes connecting components. They are obtained by the @link NXOpen::CAE::QualityAudit::ListConnections NXOpen::CAE::QualityAudit::ListConnections@endlink  action. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ListConnections CAE::QualityAudit::ListConnections@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ManualElementsResult(Result): 
    """ <summary> The Quality Audit ManualElementsResult is a class containing information about nodes connecting components. They are obtained by the <ja_class>NXOpen.CAE.QualityAudit.ListConnections</ja_class> action.</summary> """


    ##  Returns the manual elements. 
    ##  @return pElems (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetElements(pResult: ManualElementsResult) -> List[NXOpen.CAE.FEElement]:
        """
         Returns the manual elements. 
         @return pElems (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink): .
        """
        pass
    
##   @brief  This class contains information about elements connecting components and the connected components. It is obtained from the @link NXOpen::CAE::QualityAudit::ComponentConnectivity NXOpen::CAE::QualityAudit::ComponentConnectivity@endlink  action. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ComponentConnectivity CAE::QualityAudit::ComponentConnectivity@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ManualElementsWithComponentsResult(ManualElementsResult): 
    """ <summary> This class contains information about elements connecting components and the connected components. It is obtained from the <ja_class>NXOpen.CAE.QualityAudit.ComponentConnectivity</ja_class> action.</summary> """
    pass


##   @brief  This class contains information about elements connecting meshes and the connected meshes. It is obtained from the @link NXOpen::CAE::QualityAudit::MeshConnectivity NXOpen::CAE::QualityAudit::MeshConnectivity@endlink  action. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::MeshConnectivity CAE::QualityAudit::MeshConnectivity@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ManualElementsWithMeshesResult(ManualElementsResult): 
    """ <summary> This class contains information about elements connecting meshes and the connected meshes. It is obtained from the <ja_class>NXOpen.CAE.QualityAudit.MeshConnectivity</ja_class> action.</summary> """
    pass


import NXOpen
import NXOpen.CAE.Connections
##   @brief  This class contains the maximum angle settings available for the following actions: 
##         @link NXOpen::CAE::QualityAudit::MeshLevelConnectionAngleCheck NXOpen::CAE::QualityAudit::MeshLevelConnectionAngleCheck@endlink 
##         @link NXOpen::CAE::QualityAudit::ObjectLevelConnectionAngleCheck NXOpen::CAE::QualityAudit::ObjectLevelConnectionAngleCheck@endlink 
##         . 
## 
##    <br> To obtain an instance of this class get the @link NXOpen::CAE::QualityAudit::Action::Settings NXOpen::CAE::QualityAudit::Action::Settings@endlink  of classed using it.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MaximumAngleSettings(ActionSettings): 
    """ <summary> This class contains the maximum angle settings available for the following actions: 
        <ja_class>NXOpen.CAE.QualityAudit.MeshLevelConnectionAngleCheck</ja_class>
        <ja_class>NXOpen.CAE.QualityAudit.ObjectLevelConnectionAngleCheck</ja_class>
        .</summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumAngle
    ##   the maximum angle allowed.  
    ##    For a greater angle an error is reported   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumAngle
          the maximum angle allowed.  
           For a greater angle an error is reported   
         
        """
        pass
    
    ##  The maximum angle allowed for the specified connection type. For a greater angle an error is reported 
    ##  @return maximumAngle (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connectionType"> (@link NXOpen.CAE.Connections.ConnectionType NXOpen.CAE.Connections.ConnectionType@endlink) </param>
    def GetMaximumAngleByConnectionType(pSelfAction: MaximumAngleSettings, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The maximum angle allowed for the specified connection type. For a greater angle an error is reported 
         @return maximumAngle (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
import NXOpen.CAE
##   @brief  The Quality Audit MergedNodesResult is a class containing information about nodes connecting components. They are obtained by the @link NXOpen::CAE::QualityAudit::ListConnections NXOpen::CAE::QualityAudit::ListConnections@endlink  action. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ListConnections CAE::QualityAudit::ListConnections@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MergedNodesResult(Result): 
    """ <summary> The Quality Audit MergedNodesResult is a class containing information about nodes connecting components. They are obtained by the <ja_class>NXOpen.CAE.QualityAudit.ListConnections</ja_class> action.</summary> """


    ##  Returns the merged nodes. 
    ##  @return pElems (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNodes(pResult: MergedNodesResult) -> List[NXOpen.CAE.FENode]:
        """
         Returns the merged nodes. 
         @return pElems (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink): .
        """
        pass
    
##   @brief  This class contains information about nodes connecting components and these components. It is the result of the @link NXOpen::CAE::QualityAudit::ComponentConnectivity NXOpen::CAE::QualityAudit::ComponentConnectivity@endlink  action. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ComponentConnectivity CAE::QualityAudit::ComponentConnectivity@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MergedNodesWithComponentsResult(MergedNodesResult): 
    """ <summary> This class contains information about nodes connecting components and these components. It is the result of the <ja_class>NXOpen.CAE.QualityAudit.ComponentConnectivity</ja_class> action.</summary> """
    pass


##   @brief  This class contains information about nodes connecting meshes and these meshes. It is the result of the @link NXOpen::CAE::QualityAudit::MeshConnectivity NXOpen::CAE::QualityAudit::MeshConnectivity@endlink  action. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::MeshConnectivity CAE::QualityAudit::MeshConnectivity@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MergedNodesWithMeshesResult(MergedNodesResult): 
    """ <summary> This class contains information about nodes connecting meshes and these meshes. It is the result of the <ja_class>NXOpen.CAE.QualityAudit.MeshConnectivity</ja_class> action.</summary> """
    pass


##   @brief  This action has as result groups of connected meshes. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MeshConnectivity(Action): 
    """ <summary> This action has as result groups of connected meshes.</summary> """
    pass


##   @brief  This action checks the angle between the normal directions at the projection points on the supports after meshing. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MeshLevelConnectionAngleCheck(Action): 
    """ <summary> This action checks the angle between the normal directions at the projection points on the supports after meshing.</summary> """
    pass


import NXOpen.CAE.Connections
##   @brief  The Quality Audit MeshLevelConnectionAngleResult is a class containing information about failed connection angle check on universal connections at mesh level. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::MeshLevelConnectionAngleCheck CAE::QualityAudit::MeshLevelConnectionAngleCheck@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MeshLevelConnectionAngleResult(Result): 
    """ <summary> The Quality Audit MeshLevelConnectionAngleResult is a class containing information about failed connection angle check on universal connections at mesh level.</summary> """


    ## Getter for property: (float) Angle
    ##   the angle.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
          the angle.  
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection.  
             
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index .  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index .  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
import NXOpen.CAE.Connections
##   @brief  The Quality Audit MeshLevelFailedElementCreationResult is a class containing information about failed element creations on universal connections. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::MeshLevelProjectionCheck CAE::QualityAudit::MeshLevelProjectionCheck@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MeshLevelFailedElementCreationResult(Result): 
    """ <summary> The Quality Audit MeshLevelFailedElementCreationResult is a class containing information about failed element creations on universal connections.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection with the failed element creation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection with the failed element creation   
            
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index of the failing element creation in the location.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index of the failing element creation in the location.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index of the failing element creation.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index of the failing element creation.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index of the failing element creation.  
    ##    See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index of the failing element creation.  
           See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index of the failing element creation.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index of the failing element creation.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
import NXOpen.CAE.Connections
##   @brief  The Quality Audit MeshLevelFailedProjectionResult is a class containing information about failed projections on universal connections. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::MeshLevelProjectionCheck CAE::QualityAudit::MeshLevelProjectionCheck@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MeshLevelFailedProjectionResult(Result): 
    """ <summary> The Quality Audit MeshLevelFailedProjectionResult is a class containing information about failed projections on universal connections.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection with the failed mesh projection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection with the failed mesh projection   
            
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index of the failing projection in the location.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index of the failing projection in the location.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index of the failing projection.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index of the failing projection.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index of the failing mesh projection.  
    ##    See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index of the failing mesh projection.  
           See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index of the failing projection.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index of the failing projection.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
import NXOpen.CAE.Connections
##   @brief The Quality Audit MeshLevelFailedProjectionToleranceResult is a class containing information about mesh projections 
##         that failed the tolerance criteria. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::MeshLevelProjectionCheck CAE::QualityAudit::MeshLevelProjectionCheck@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MeshLevelFailedProjectionToleranceResult(Result): 
    """ <summary>The Quality Audit MeshLevelFailedProjectionToleranceResult is a class containing information about mesh projections 
        that failed the tolerance criteria.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection with the failed mesh tolerance projection  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection with the failed mesh tolerance projection  
            
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index of the tolerance failing mesh projection in the location.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index of the tolerance failing mesh projection in the location.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index of the tolerance failing mesh projection.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index of the tolerance failing mesh projection.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index of the tolerance failing mesh projection.  
    ##    See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index of the tolerance failing mesh projection.  
           See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index of the tolerance failing mesh projection.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index of the tolerance failing mesh projection.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (float) OffendingDistance
    ##   the offending distance of the failing mesh projection.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def OffendingDistance(self) -> float:
        """
        Getter for property: (float) OffendingDistance
          the offending distance of the failing mesh projection.  
              
         
        """
        pass
    
##   @brief  This action checks the flatness around the spot weld after meshing. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MeshLevelFlatnessCheck(Action): 
    """ <summary> This action checks the flatness around the spot weld after meshing.</summary> """
    pass


import NXOpen
import NXOpen.CAE.Connections
##   @brief  The Quality Audit MeshLevelFlatnessResult is a class containing information about failed flatness check on universal connections at mesh level. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::MeshLevelConnectionAngleCheck CAE::QualityAudit::MeshLevelConnectionAngleCheck@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MeshLevelFlatnessResult(Result): 
    """ <summary> The Quality Audit MeshLevelFlatnessResult is a class containing information about failed flatness check on universal connections at mesh level.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection.  
             
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index .  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index .  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (float) Distance
    ##   the distance.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
          the distance.  
              
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index of the first point.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index of the first point.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Point
    ##   the result point.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Point(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Point
          the result point.  
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ResultEntity
    ##   the result object.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def ResultEntity(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ResultEntity
          the result object.  
              
         
        """
        pass
    
##   @brief  This action checks the distance between two consecutive supports after meshing. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MeshLevelLengthRangeCheck(Action): 
    """ <summary> This action checks the distance between two consecutive supports after meshing.</summary> """
    pass


import NXOpen.CAE.Connections
##   @brief  The Quality Audit MeshLevelLengthRangeResult is a class containing information about failed length range check on universal connections at mesh level. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::MeshLevelLengthRangeCheck CAE::QualityAudit::MeshLevelLengthRangeCheck@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MeshLevelLengthRangeResult(Result): 
    """ <summary> The Quality Audit MeshLevelLengthRangeResult is a class containing information about failed length range check on universal connections at mesh level.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection.  
             
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index .  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index .  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (float) Length
    ##   the length.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
          the length.  
              
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
##   @brief  This action checks the ratio between two consecutive supports after meshing. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MeshLevelLengthRatioRangeCheck(Action): 
    """ <summary> This action checks the ratio between two consecutive supports after meshing.</summary> """
    pass


import NXOpen.CAE.Connections
##   @brief  The Quality Audit MeshLevelLengthRatioRangeResult is a class containing information about failed length ratio range check on universal connections at mesh level. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::MeshLevelLengthRatioRangeCheck CAE::QualityAudit::MeshLevelLengthRatioRangeCheck@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MeshLevelLengthRatioRangeResult(Result): 
    """ <summary> The Quality Audit MeshLevelLengthRatioRangeResult is a class containing information about failed length ratio range check on universal connections at mesh level.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection.  
             
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index .  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index .  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (float) Ratio
    ##   the ratio.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Ratio(self) -> float:
        """
        Getter for property: (float) Ratio
          the ratio.  
              
         
        """
        pass
    
    ## Getter for property: (float) Thickness1
    ##   the thickness of the first flange.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Thickness1(self) -> float:
        """
        Getter for property: (float) Thickness1
          the thickness of the first flange.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (float) Thickness2
    ##   the thickness of the second flange.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Thickness2(self) -> float:
        """
        Getter for property: (float) Thickness2
          the thickness of the second flange.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
##   @brief  This action has as output the list of failed projections of the universal connections at mesh level. 
## 
##    <br> To obtain this action see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MeshLevelProjectionCheck(Action): 
    """ <summary> This action has as output the list of failed projections of the universal connections at mesh level.</summary> """
    pass


import NXOpen.CAE
##   @brief  This result a group of connected meshes. 
## 
##    <br> To obtain this result see @link CAE::QualityAudit::MeshConnectivity CAE::QualityAudit::MeshConnectivity@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MeshSubResult(Result): 
    """ <summary> This result a group of connected meshes.</summary> """


    ##  Gets the mesh of this sub-result 
    ##  @return mesh (@link NXOpen.CAE.Mesh NXOpen.CAE.Mesh@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMesh(pThis: MeshSubResult) -> NXOpen.CAE.Mesh:
        """
         Gets the mesh of this sub-result 
         @return mesh (@link NXOpen.CAE.Mesh NXOpen.CAE.Mesh@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.CAE.Connections
##   @brief  This class contains the minimum distance settings available for the following actions: 
##         @link NXOpen::CAE::QualityAudit::FreeEdgeDistanceCheck NXOpen::CAE::QualityAudit::FreeEdgeDistanceCheck@endlink 
##         @link NXOpen::CAE::QualityAudit::ConnectionDistanceCheck NXOpen::CAE::QualityAudit::ConnectionDistanceCheck@endlink 
##         @link NXOpen::CAE::QualityAudit::ConnectionPointsDistanceCheck NXOpen::CAE::QualityAudit::ConnectionPointsDistanceCheck@endlink 
##          
## 
##    <br> To obtain an instance of this class get the @link NXOpen::CAE::QualityAudit::Action::Settings NXOpen::CAE::QualityAudit::Action::Settings@endlink  of classed using it.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MinimumDistanceSettings(ActionSettings): 
    """ <summary> This class contains the minimum distance settings available for the following actions: 
        <ja_class>NXOpen.CAE.QualityAudit.FreeEdgeDistanceCheck</ja_class>
        <ja_class>NXOpen.CAE.QualityAudit.ConnectionDistanceCheck</ja_class>
        <ja_class>NXOpen.CAE.QualityAudit.ConnectionPointsDistanceCheck</ja_class>
        </summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumDistance
    ##   the minimum distance required.  
    ##    For a smaller distance an error is reported   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinimumDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumDistance
          the minimum distance required.  
           For a smaller distance an error is reported   
         
        """
        pass
    
    ##  The minimum distance required for the specified connection type. For a smaller distance an error is reported 
    ##  @return minimumDistance (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connectionType"> (@link NXOpen.CAE.Connections.ConnectionType NXOpen.CAE.Connections.ConnectionType@endlink) </param>
    def GetMinimumDistanceByConnectionType(pSelfAction: MinimumDistanceSettings, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The minimum distance required for the specified connection type. For a smaller distance an error is reported 
         @return minimumDistance (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
import NXOpen.CAE.Connections
##   @brief  This is a class containing information about the non modeled universal connections. It is in the results of @link NXOpen::CAE::QualityAudit::ListNonModeledConnections NXOpen::CAE::QualityAudit::ListNonModeledConnections@endlink  
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ListNonModeledConnections CAE::QualityAudit::ListNonModeledConnections@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class NonModeledConnectionResult(Result): 
    """ <summary> This is a class containing information about the non modeled universal connections. It is in the results of <ja_class>NXOpen.CAE.QualityAudit.ListNonModeledConnections</ja_class></summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection not being modeled   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection not being modeled   
            
         
        """
        pass
    
##   @brief This action checks the angle between the normal directions at the projection points on the supports before meshing. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ObjectLevelConnectionAngleCheck(Action): 
    """ <summary>This action checks the angle between the normal directions at the projection points on the supports before meshing.</summary> """
    pass


import NXOpen.CAE.Connections
##   @brief  The Quality Audit ObjectLevelConnectionAngleResult is a class containing information about failed connection angle check on universal connections at object level. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ObjectLevelConnectionAngleCheck CAE::QualityAudit::ObjectLevelConnectionAngleCheck@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ObjectLevelConnectionAngleResult(Result): 
    """ <summary> The Quality Audit ObjectLevelConnectionAngleResult is a class containing information about failed connection angle check on universal connections at object level.</summary> """


    ## Getter for property: (float) Angle
    ##   the angle.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
          the angle.  
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection.  
             
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index .  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index .  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
import NXOpen.CAE.Connections
##   @brief  The Quality Audit ObjectLevelCorrectedProjectionResult is a class containing information about corrected projections on universal connections. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ObjectLevelProjectionCheck CAE::QualityAudit::ObjectLevelProjectionCheck@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ObjectLevelCorrectedProjectionResult(Result): 
    """ <summary> The Quality Audit ObjectLevelCorrectedProjectionResult is a class containing information about corrected projections on universal connections.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection with the corrected projection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection with the corrected projection   
            
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index of the corrected projection in the location.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index of the corrected projection in the location.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index of the corrected projection.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index of the corrected projection.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index of the corrected projection.  
    ##    See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index of the corrected projection.  
           See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index of the corrected projection.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index of the corrected projection.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
import NXOpen.CAE.Connections
##   @brief  The Quality Audit ObjectLevelFailedProjectionResult is a class containing information about failed projections on universal connections. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ObjectLevelProjectionCheck CAE::QualityAudit::ObjectLevelProjectionCheck@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ObjectLevelFailedProjectionResult(Result): 
    """ <summary> The Quality Audit ObjectLevelFailedProjectionResult is a class containing information about failed projections on universal connections.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection with the failed projection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection with the failed projection   
            
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index of the failing projection in the location.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index of the failing projection in the location.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index of the failing projection.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index of the failing projection.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index of the failing projection.  
    ##    See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index of the failing projection.  
           See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index of the failing projection.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index of the failing projection.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
import NXOpen.CAE.Connections
##   @brief The Quality Audit ObjectLevelFailedProjectionToleranceResult is a class containing information about projections 
##         that failed the tolerance criteria although the projection itself was successful. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ObjectLevelProjectionCheck CAE::QualityAudit::ObjectLevelProjectionCheck@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ObjectLevelFailedProjectionToleranceResult(Result): 
    """ <summary>The Quality Audit ObjectLevelFailedProjectionToleranceResult is a class containing information about projections 
        that failed the tolerance criteria although the projection itself was successful.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection with the failed tolerance projection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection with the failed tolerance projection   
            
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index of the tolerance failing projection in the location.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index of the tolerance failing projection in the location.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index of the tolerance failing projection.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index of the tolerance failing projection.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index of the tolerance failing projection.  
    ##    See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index of the tolerance failing projection.  
           See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index of the tolerance failing projection.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index of the tolerance failing projection.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (float) OffendingDistance
    ##   the offending distance of the failing mesh projection.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def OffendingDistance(self) -> float:
        """
        Getter for property: (float) OffendingDistance
          the offending distance of the failing mesh projection.  
              
         
        """
        pass
    
##   @brief  This action checks the flatness around the spot weld before meshing. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ObjectLevelFlatnessCheck(Action): 
    """ <summary> This action checks the flatness around the spot weld before meshing.</summary> """
    pass


import NXOpen
import NXOpen.CAE.Connections
##   @brief  The Quality Audit ObjectLevelFlatnessResult is a class containing information about failed flatness check on universal connections at object level. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ObjectLevelFlatnessCheck CAE::QualityAudit::ObjectLevelFlatnessCheck@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ObjectLevelFlatnessResult(Result): 
    """ <summary> The Quality Audit ObjectLevelFlatnessResult is a class containing information about failed flatness check on universal connections at object level.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection.  
             
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index .  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index .  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (float) Distance
    ##   the distance.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
          the distance.  
              
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index of the first point.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index of the first point.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Point
    ##   the result point.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Point(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Point
          the result point.  
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ResultEntity
    ##   the result object.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def ResultEntity(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ResultEntity
          the result object.  
              
         
        """
        pass
    
##   @brief  This action checks the distance between two consecutive supports before meshing. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ObjectLevelLengthRangeCheck(Action): 
    """ <summary> This action checks the distance between two consecutive supports before meshing.</summary> """
    pass


import NXOpen.CAE.Connections
##   @brief  The Quality Audit ObjectLevelLengthRangeResult is a class containing information about failed length range check on universal connections at object level. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ObjectLevelLengthRangeCheck CAE::QualityAudit::ObjectLevelLengthRangeCheck@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ObjectLevelLengthRangeResult(Result): 
    """ <summary> The Quality Audit ObjectLevelLengthRangeResult is a class containing information about failed length range check on universal connections at object level.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection.  
             
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index .  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index .  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (float) Length
    ##   the ratio.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
          the ratio.  
              
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
##   @brief  This action checks the ratio between two consecutive supports before meshing. 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ObjectLevelLengthRatioRangeCheck(Action): 
    """ <summary> This action checks the ratio between two consecutive supports before meshing.</summary> """
    pass


import NXOpen.CAE.Connections
##   @brief  The Quality Audit ObjectLevelLengthRatioRangeResult is a class containing information about failed length ratio range check on universal connections at object level. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ObjectLevelLengthRatioRangeCheck CAE::QualityAudit::ObjectLevelLengthRatioRangeCheck@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ObjectLevelLengthRatioRangeResult(Result): 
    """ <summary> The Quality Audit ObjectLevelLengthRatioRangeResult is a class containing information about failed length ratio range check on universal connections at object level.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection.  
             
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index .  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index .  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) FlangeIndex
    ##   the flange index.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
          the flange index.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (float) Ratio
    ##   the ratio.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Ratio(self) -> float:
        """
        Getter for property: (float) Ratio
          the ratio.  
              
         
        """
        pass
    
    ## Getter for property: (float) Thickness1
    ##   the thickness of the first flange.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Thickness1(self) -> float:
        """
        Getter for property: (float) Thickness1
          the thickness of the first flange.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (float) Thickness2
    ##   the thickness of the second flange.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Thickness2(self) -> float:
        """
        Getter for property: (float) Thickness2
          the thickness of the second flange.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
##   @brief  This action has as output the list of failed projections of the universal connections at object level. 
## 
##    <br> To obtain this action see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ObjectLevelProjectionCheck(Action): 
    """ <summary> This action has as output the list of failed projections of the universal connections at object level.</summary> """
    pass


import NXOpen
import NXOpen.CAE.Connections
##   @brief  This class contains settings used by the projection checks. 
## 
##    <br> To obtain an instance of this class see @link CAE::QualityAudit::MeshLevelProjectionCheck CAE::QualityAudit::MeshLevelProjectionCheck@endlink  or @link CAE::QualityAudit::ObjectLevelProjectionCheck CAE::QualityAudit::ObjectLevelProjectionCheck@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ProjectionCheckSettings(ActionSettings): 
    """ <summary> This class contains settings used by the projection checks.</summary> """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Threshold
    ##   the threshold distance from definition point to projection point.  
    ##    Once this is surpassed an error is reported   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Threshold(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Threshold
          the threshold distance from definition point to projection point.  
           Once this is surpassed an error is reported   
         
        """
        pass
    
    ##  The threshold distance from definition point to projection point for the specified connection type. Once this is surpassed an error is reported 
    ##  @return threshold (@link NXOpen.Expression NXOpen.Expression@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connectionType"> (@link NXOpen.CAE.Connections.ConnectionType NXOpen.CAE.Connections.ConnectionType@endlink) </param>
    def GetThresholdByConnectionType(pSelfAction: ProjectionCheckSettings, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The threshold distance from definition point to projection point for the specified connection type. Once this is surpassed an error is reported 
         @return threshold (@link NXOpen.Expression NXOpen.Expression@endlink): .
        """
        pass
    
import NXOpen
##   @brief  The Quality Audit Result class offers means to access information about specific problems found while performing specific quality audit checks. 
## 
##    <br> Results can be obtained from @link CAE::QualityAudit::Action CAE::QualityAudit::Action@endlink  after checks have been performed via @link NXOpen::CAE::QualityAudit::Action::GetResults NXOpen::CAE::QualityAudit::Action::GetResults@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Result(NXOpen.NXObject): 
    """ <summary> The Quality Audit Result class offers means to access information about specific problems found while performing specific quality audit checks.</summary> """


    ## Getter for property: (str) Description
    ##   the text description of this result    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the text description of this result    
            
         
        """
        pass
    
    ## Getter for property: (bool) Outdated
    ##   the outdated flag of this result    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def Outdated(self) -> bool:
        """
        Getter for property: (bool) Outdated
          the outdated flag of this result    
            
         
        """
        pass
    
    ## Getter for property: (@link Action NXOpen.CAE.QualityAudit.Action@endlink) OwningAction
    ##   the owning action that provides this result   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return Action
    @property
    def OwningAction(self) -> Action:
        """
        Getter for property: (@link Action NXOpen.CAE.QualityAudit.Action@endlink) OwningAction
          the owning action that provides this result   
            
         
        """
        pass
    
    ##  Get the sub results, if any 
    ##  @return subResults (@link Result List[NXOpen.CAE.QualityAudit.Result]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSubResults(pResult: Result) -> List[Result]:
        """
         Get the sub results, if any 
         @return subResults (@link Result List[NXOpen.CAE.QualityAudit.Result]@endlink): .
        """
        pass
    
##   @brief  This action's output is the list of connections having more than 2 supports with wrong order (e.g. first support between the second and third). 
## 
##    <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SupportSequenceCheck(Action): 
    """ <summary> This action's output is the list of connections having more than 2 supports with wrong order (e.g. first support between the second and third).</summary> """
    pass


import NXOpen.CAE.Connections
##   @brief This result represents a group of universal connections having the same property. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::ConnectionSynthesis CAE::QualityAudit::ConnectionSynthesis@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class UniversalConnectionSynthesisResult(Result): 
    """ <summary>This result represents a group of universal connections having the same property.</summary> """


    ## Getter for property: (str) Characteristic
    ##   the characteristic   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Characteristic(self) -> str:
        """
        Getter for property: (str) Characteristic
          the characteristic   
            
         
        """
        pass
    
    ## Getter for property: (int) Count
    ##   the count of the different type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def Count(self) -> int:
        """
        Getter for property: (int) Count
          the count of the different type   
            
         
        """
        pass
    
    ##  Get the connections having the same properties 
    ##  @return connections (@link NXOpen.CAE.Connections.IConnection List[NXOpen.CAE.Connections.IConnection]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRepresentedConnections(pResult: UniversalConnectionSynthesisResult) -> List[NXOpen.CAE.Connections.IConnection]:
        """
         Get the connections having the same properties 
         @return connections (@link NXOpen.CAE.Connections.IConnection List[NXOpen.CAE.Connections.IConnection]@endlink): .
        """
        pass
    
import NXOpen.CAE.Connections
##   @brief  The Quality Audit WrongSupportSequenceResult is a class containing information about universal connections whose support sequence order is wrong. 
## 
##    <br> To obtain this type of results see @link CAE::QualityAudit::SupportSequenceCheck CAE::QualityAudit::SupportSequenceCheck@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class WrongSupportSequenceResult(Result): 
    """ <summary> The Quality Audit WrongSupportSequenceResult is a class containing information about universal connections whose support sequence order is wrong.</summary> """


    ## Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
    ##   the connection with the failed support sequence   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.Connections.IConnection
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: (@link NXOpen.CAE.Connections.IConnection NXOpen.CAE.Connections.IConnection@endlink) Connection
          the connection with the failed support sequence   
            
         
        """
        pass
    
    ## Getter for property: (int) CoordinateIndex
    ##   the coordinate index in the location where the support sequence is wrong.  
    ##    See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
          the coordinate index in the location where the support sequence is wrong.  
           See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details    
         
        """
        pass
    
    ## Getter for property: (int) DefinitionIndex
    ##   the definition index for the wrong support sequence.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
          the definition index for the wrong support sequence.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details   
         
        """
        pass
    
    ## Getter for property: (int) LocationIndex
    ##   the location index for the wrong support sequence.  
    ##    See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
          the location index for the wrong support sequence.  
           See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details    
         
        """
        pass
    
## @package NXOpen.CAE.QualityAudit
## Classes, Enums and Structs under NXOpen.CAE.QualityAudit namespace

##  @link ActionId NXOpen.CAE.QualityAudit.ActionId @endlink is an alias for @link Action.Id NXOpen.CAE.QualityAudit.Action.Id@endlink
ActionId = Action.Id


