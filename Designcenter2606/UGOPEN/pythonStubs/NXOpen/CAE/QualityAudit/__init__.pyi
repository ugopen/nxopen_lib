from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ActionList(NXOpen.NXObject): 
    """  The Quality Audit ActionList class offers means to select, deselect, obtain NXOpen.CAE.QualityAudit.Action instances. """
    def Deselect(self, pAction: Action) -> None:
        """
         Deselect the specified action to avoid using it in the quality audit.
                     
        """
        pass
    def DeselectAll(self) -> None:
        """
         Deselect all available actions.
                     
        """
        pass
    def GetAction(self, id: Action.Id) -> Action:
        """
         Get the action by id. See NXOpen.CAE.QualityAudit.Action.Id for full the list of actions.
                     
         Returns action ( Action NXOpen.CAE.):  Corresponding action .
        """
        pass
    def GetSelectedActions(self) -> List[Action]:
        """
         Returns an array of all selected actions.
                     
         Returns pActions ( Action List[NXOpen.CA):  The selected actions .
        """
        pass
    def IsSelected(self, pAction: Action) -> bool:
        """
         Tells if the action is to be used in the quality audit.
                     
         Returns pSelected (bool):  .
        """
        pass
    def LoadActionSettings(self, actionConfigFile: str) -> None:
        """
         Import action settings from file
                     
        """
        pass
    def SaveActionSettings(self, actionConfigFile: str) -> None:
        """
         Export action settings to file
                     
        """
        pass
    def Select(self, pAction: Action) -> None:
        """
         Select the specified action to be used in the quality audit.
                     
        """
        pass
    def SelectAll(self) -> None:
        """
         Select all the actions available.
                     
        """
        pass
import NXOpen
import NXOpen.CAE.Connections
class ActionSettings(NXOpen.NXObject): 
    """  The Quality Audit ActionSettings is the base class for NXOpen.CAE.QualityAudit.Action settings. It provides basic functionality. """
    @property
    def Action(self) -> Action:
        """
        Getter for property: ( Action NXOpen.CAE.) Action
         Returns the action using these settings   
            
         
        """
        pass
    def AllowOverride(self, connectionType: NXOpen.CAE.Connections.ConnectionType, allowOverride: bool) -> None:
        """
         Sets the override flag of settings for the specified connection type.
        """
        pass
    def CanOverride(self, connectionType: NXOpen.CAE.Connections.ConnectionType) -> bool:
        """
         Tells if overriding is allowed for the specified connection type.
         Returns canOverride (bool): .
        """
        pass
    def GetSupportedConnectionTypes(self) -> List[NXOpen.CAE.Connections.ConnectionType]:
        """
         The supported connection types using the settings 
         Returns supportedConnections ( NXOpen.CAE.Connections.ConnectionType Li): .
        """
        pass
    def ResetToDefaults(self) -> None:
        """
         Reset the action settings to default values 
        """
        pass
import NXOpen
class Action(NXOpen.NXObject): 
    """  The Quality Audit Action is a base class that performs actions on a list of objects. Results of the action are also stored here. """
    class Id(Enum):
        """
        Members Include: 
         |AllConnectionsList|  the action that lists all connections 
         |NonModeledConnectionsList|  the action that list all non modeled connections 
         |SubAssemblyComponentCheck|  the action that list groups of connected components before meshing 
         |SubAssemblyMeshCheck|  the action that list groups of connected meshes after meshing 
         |ObjectLevelProjectionCheck|  the action listing projection errors at object level 
         |MeshLevelProjectionCheck|  the action listing projection errors at mesh level 
         |DistanceBetweenConnectionPointsCheck|  the action verifying distance between the points of the same connection 
         |DistanceBetweenConnectionsCheck|  the action checking the distance between connections 
         |FreeEdgeDistanceCheck|  the action checking for near edge connections 
         |TargetSequenceCheck|  the action verifying the support order 
         |ObjectLevelLengthCheck|  the action checking connections for which the distance is lower or higher than a threshold value 
         |MeshLevelLengthCheck|  the action checking connections for which the distance is lower or higher than a threshold value 
         |ObjectLevelLengthRatioCheck|  the action checking connections for which the distance between the projection points on the supports divided by the sum of half the support thickness is lower or higher than a threshold value 
         |MeshLevelLengthRatioCheck|  the action checking connections for which the distance between the projection points on the supports divided by the sum of half the support thickness is lower or higher than a threshold value 
         |ObjectLevelConnectionAngleCheck|  the action checking connections for which the angle is higher than a threshold value 
         |MeshLevelConnectionAngleCheck|  the action checking connections for which the angle is higher than a threshold value
         |ObjectLevelFlatnessCheck|  the action checking spot welds for which the height is higher than a threshold value 
         |MeshLevelFlatnessCheck|  the action checking spot welds for which the height is higher than a threshold value 
         |ConnectionSynthesis|  the action displaying information about the connections grouped by characteristics 

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
        @staticmethod
        def ValueOf(value: int) -> Action.Id:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActionId(self) -> Action.Id:
        """
        Getter for property: ( Action.Id NXOpen.CAE.) ActionId
         Returns the action id
                       
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the action description
                       
            
         
        """
        pass
    @property
    def Settings(self) -> ActionSettings:
        """
        Getter for property: ( ActionSettings NXOpen.CAE.) Settings
         Returns the action settings
                       
            
         
        """
        pass
    def ExportResults(self, resultsFIle: str) -> None:
        """
         Export results to file
        """
        pass
    def GetResults(self) -> List[Result]:
        """
         Get the CAE.QualityAudit.Result list obtained from the latest check
                     
         Returns pResults ( Result List[NXOpen.CA): .
        """
        pass
    def Perform(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Performs the action on the given object list.
                     
        """
        pass
class ComponentConnectivity(Action): 
    """  This action has as result groups of connected components. """
    pass
import NXOpen.Assemblies
class ComponentSubResult(Result): 
    """  This result a group of connected components. """
    def GetComponent(self) -> NXOpen.Assemblies.Component:
        """
         Gets the component of this sub-result 
         Returns component ( NXOpen.Assemblies.Component): .
        """
        pass
class ConnectedComponentsGroupResult(Result): 
    """  This result a group of connected components. """
    pass
class ConnectedMeshesGroupResult(Result): 
    """  This result a group of connected meshes. """
    pass
class ConnectionDistanceCheck(Action): 
    """  This action checks the distance between connections. """
    pass
import NXOpen
import NXOpen.CAE.Connections
class ConnectionDistanceResult(Result): 
    """  The Quality Audit ConnectionPointsDistanceResult is a class containing information about failed distance between connection distance checks on universal connections. """
    @property
    def Connection1(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection1
         Returns the first connection.  
            
         
        """
        pass
    @property
    def Connection2(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection2
         Returns the second connection.  
            
         
        """
        pass
    @property
    def CoordinateIndex1(self) -> int:
        """
        Getter for property: (int) CoordinateIndex1
         Returns the coordinate index of the first point.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def CoordinateIndex2(self) -> int:
        """
        Getter for property: (int) CoordinateIndex2
         Returns the coordinate index of the second point.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def Coordinates1(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Coordinates1
         Returns the coordinates of the first point.  
             
         
        """
        pass
    @property
    def Coordinates2(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Coordinates2
         Returns the coordinates of the second point.  
             
         
        """
        pass
    @property
    def DefinitionIndex1(self) -> int:
        """
        Getter for property: (int) DefinitionIndex1
         Returns the definition index of the first point.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def DefinitionIndex2(self) -> int:
        """
        Getter for property: (int) DefinitionIndex2
         Returns the definition index of the second point.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
         Returns the distance between the two connections.  
              
         
        """
        pass
    @property
    def LocationIndex1(self) -> int:
        """
        Getter for property: (int) LocationIndex1
         Returns the location index of the first point.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
    @property
    def LocationIndex2(self) -> int:
        """
        Getter for property: (int) LocationIndex2
         Returns the location index of the second point.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
class ConnectionPointsDistanceCheck(Action): 
    """  This action checks the distance between connection's definition points. """
    pass
import NXOpen.CAE.Connections
class ConnectionPointsDistanceResult(Result): 
    """  The Quality Audit ConnectionPointsDistanceResult is a class containing information about failed distance between connection points checks on universal connections. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection.  
             
         
        """
        pass
    @property
    def CoordinateIndex1(self) -> int:
        """
        Getter for property: (int) CoordinateIndex1
         Returns the coordinate index of the first point in the first location.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def CoordinateIndex2(self) -> int:
        """
        Getter for property: (int) CoordinateIndex2
         Returns the coordinate index of the second point in the second location.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex1(self) -> int:
        """
        Getter for property: (int) DefinitionIndex1
         Returns the definition index of the first point.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def DefinitionIndex2(self) -> int:
        """
        Getter for property: (int) DefinitionIndex2
         Returns the definition index of the second point.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
         Returns the distance between the two points.  
              
         
        """
        pass
    @property
    def LocationIndex1(self) -> int:
        """
        Getter for property: (int) LocationIndex1
         Returns the location index of the first point.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
    @property
    def LocationIndex2(self) -> int:
        """
        Getter for property: (int) LocationIndex2
         Returns the location index of the second point.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
import NXOpen
import NXOpen.CAE
class ConnectionResult(Result): 
    """  The ConnectionResult is a class containing information about connections found when performing the NXOpen.CAE.QualityAudit.ListConnections action. """
    @property
    def Connection(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) Connection
         Returns the connection.  
             
         
        """
        pass
    @property
    def Femodel(self) -> NXOpen.CAE.FEModelOccurrence:
        """
        Getter for property: ( NXOpen.CAE.FEModelOccurrence) Femodel
         Returns the Fe Model of the connection when we're dealing with a non-occurrenceable connection.  
             
         
        """
        pass
class ConnectionSynthesis(Action): 
    """  This action has as result the list of all connections from the specified model. """
    pass
class ConnectionWithComponentsResult(ConnectionResult): 
    """  This result contains information about connection and the components it connects. It is the result of the NXOpen.CAE.QualityAudit.ComponentConnectivity action. """
    pass
class ConnectionWithMeshesResult(ConnectionResult): 
    """  This result contains information about connection and the meshes it connects. It is the result of the NXOpen.CAE.QualityAudit.MeshConnectivity action. """
    pass
import NXOpen
class FlatnessSettings(ActionSettings): 
    """  This class contains the flatness settings available for the following actions: 
        NXOpen.CAE.QualityAudit.ObjectLevelFlatnessCheck
        NXOpen.CAE.QualityAudit.MeshLevelFlatnessCheck
        . """
    @property
    def ClosestPointFlag(self) -> bool:
        """
        Getter for property: (bool) ClosestPointFlag
         Returns the closest point flag.  
           If this flag is false it returns one of the points else it returns the closest point  
         
        """
        pass
    @ClosestPointFlag.setter
    def ClosestPointFlag(self, closestPointFlag: bool):
        """
        Setter for property: (bool) ClosestPointFlag
         Returns the closest point flag.  
           If this flag is false it returns one of the points else it returns the closest point  
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height required.  
           For a greater height an error is reported   
         
        """
        pass
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Radius
         Returns the radius required.  
             
         
        """
        pass
class FreeEdgeDistanceCheck(Action): 
    """  This action checks if there are connections that are too close to the edge based on a configurable tolerance. """
    pass
import NXOpen
import NXOpen.CAE
import NXOpen.CAE.Connections
class FreeEdgeDistanceResult(Result): 
    """  The Quality Audit FreeEdgeDistanceResult contains information about problematic places where distance between connection points and free edges is less than a given value. """
    @property
    def CaeEdge(self) -> NXOpen.CAE.CAEEdge:
        """
        Getter for property: ( NXOpen.CAE.CAEEdge) CaeEdge
         Returns the CAE edge (if present).  
             
         
        """
        pass
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection with points close to the edge   
            
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index of the close to the edge point in the location.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index of the point close to edge.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
         Returns the distance.  
           See  NXOpen::CAE::Connections::IFlangesContainer  for details    
         
        """
        pass
    @property
    def EdgePoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) EdgePoint
         Returns the edge point.  
             
         
        """
        pass
    @property
    def FeElementEdge(self) -> NXOpen.CAE.FEElemEdge:
        """
        Getter for property: ( NXOpen.CAE.FEElemEdge) FeElementEdge
         Returns the FE edge (if present).  
             
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index of the close to the edge point.  
           See  NXOpen::CAE::Connections::IFlangesContainer  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index of the point close to edge.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
    def GetClosestConnectionPoint(self) -> NXOpen.Point3d:
        """
         The closest connection point. 
         Returns pointPosition ( NXOpen.Point3d):  Closest connection point in ABS coordinates .
        """
        pass
import NXOpen
import NXOpen.Assemblies
class IConnectedComponents(NXOpen.INXObject): 
    """  This is an interface to obtain the connected components. """
    @abstractmethod
    def GetComponents(self) -> List[NXOpen.Assemblies.Component]:
        """
         Gets the connected components from a result 
         Returns components ( NXOpen.Assemblies.Component Li): .
        """
        pass
import NXOpen
import NXOpen.CAE
class IConnectedMeshes(NXOpen.INXObject): 
    """  This is an interface to obtain the connected meshes. """
    @abstractmethod
    def GetMeshes(self) -> List[NXOpen.CAE.Mesh]:
        """
         Gets the connected meshes from a result 
         Returns meshes ( NXOpen.CAE.Mesh Li): .
        """
        pass
import NXOpen
class InputList(NXOpen.NXObject): 
    """  The Quality Audit InputList class offers means to select, deselect, obtain the objects to be used by CAE.QualityAudit.Action instances. """
    def Deselect(self, obj: NXOpen.NXObject) -> None:
        """
         Mark the specified object to be excluded from the quality audit actions.
                     
        """
        pass
    def DeselectAll(self) -> None:
        """
         Deselect all input from the CAE.QualityAudit.InputList.
                     
        """
        pass
    def GetAllObjects(self) -> List[NXOpen.NXObject]:
        """
         Return all the objects available as input for the quality audit actions.
                     
         Returns pObjects ( NXOpen.NXObject Li):  Array of selected objects .
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.NXObject]:
        """
         Return all the selected objects available as input to the quality audit actions.
                     
         Returns pObjects ( NXOpen.NXObject Li):  Array of selected objects .
        """
        pass
    def IsSelected(self, obj: NXOpen.NXObject) -> bool:
        """
         Tells if the specified object is included in the quality audit actions.
                     
         Returns pIsSelected (bool): .
        """
        pass
    def Select(self, obj: NXOpen.NXObject) -> None:
        """
         Mark the specified object to be included in the quality audit actions.
                     
        """
        pass
    def SelectAll(self) -> None:
        """
         Select all input from the CAE.QualityAudit.InputList.
                     
        """
        pass
import NXOpen
import NXOpen.CAE.Connections
class LengthRangeSettings(ActionSettings): 
    """  This class contains the length range settings available for the following actions: 
        NXOpen.CAE.QualityAudit.ObjectLevelLengthRangeCheck
        . """
    @property
    def MaximumDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumDistance
         Returns the maximum length required.  
           For a greater distance an error is reported   
         
        """
        pass
    @property
    def MinimumDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumDistance
         Returns the minimum length required.  
           For a lower distance an error is reported   
         
        """
        pass
    def GetMaximumDistanceByConnectionType(self, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The maximum length required for the specified connection type. For a greater distance an error is reported 
         Returns maximumDistance ( NXOpen.Expression): .
        """
        pass
    def GetMinimumDistanceByConnectionType(self, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The minimum length required for the specified connection type. For a lower distance an error is reported 
         Returns minimumDistance ( NXOpen.Expression): .
        """
        pass
import NXOpen
import NXOpen.CAE.Connections
class LengthRatioRangeSettings(ActionSettings): 
    """  This class contains the length ratio range settings available for the following actions: 
        NXOpen.CAE.QualityAudit.ObjectLevelLengthRatioRangeCheck
        NXOpen.CAE.QualityAudit.MeshLevelLengthRatioRangeCheck
        . """
    @property
    def MaximumRatio(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumRatio
         Returns the maximum length ratio range required.  
           For a greater ratio an error is reported   
         
        """
        pass
    @property
    def MinimumRatio(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumRatio
         Returns the minimum length ratio required.  
           For lower ratio an error is reported   
         
        """
        pass
    def GetMaximumRatioByConnectionType(self, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The maximum ratio required for the specified connection type. For a greater ratio an error is reported 
         Returns maximumRatio ( NXOpen.Expression): .
        """
        pass
    def GetMinimumRatioByConnectionType(self, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The minimum ratio required for the specified connection type. For lower ratio an error is reported 
         Returns minimumRatio ( NXOpen.Expression): .
        """
        pass
class ListConnections(Action): 
    """  This action has as result the list of all connections from the specified model. """
    pass
class ListNonModeledConnections(Action): 
    """  This action's output is a list of connections that are not realized. """
    pass
import NXOpen
class Manager(NXOpen.Object): 
    """  The Quality Audit Manager class offers means to check for errors at assembly level  """
    @property
    def ActionList(self) -> ActionList:
        """
        Getter for property: ( ActionList NXOpen.CAE.) ActionList
         Returns the quality audit action list.  
          
                       
         
        """
        pass
    @property
    def InputList(self) -> InputList:
        """
        Getter for property: ( InputList NXOpen.CAE.) InputList
         Returns the quality audit input list.  
          
                       
         
        """
        pass
    @property
    def UseInputListForSynthesis(self) -> bool:
        """
        Getter for property: (bool) UseInputListForSynthesis
         Returns the option to use the input list for the connections used in Connection Synthesis check
                       
            
         
        """
        pass
    @UseInputListForSynthesis.setter
    def UseInputListForSynthesis(self, useInputList: bool):
        """
        Setter for property: (bool) UseInputListForSynthesis
         Returns the option to use the input list for the connections used in Connection Synthesis check
                       
            
         
        """
        pass
    def ExportResults(actionsToExport: List[Action], resultsFIle: str) -> None:
        """
         Export results to file
        """
        pass
    def FindObject(journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the  NXOpen.INXObject  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( NXOpen.INXObject):  An object matching the journal identifier .
        """
        pass
    def PerformActions(inputActions: List[Action], pObjects: List[NXOpen.NXObject]) -> None:
        """
         This method performs checks on the selected objects. 
        """
        pass
import NXOpen.CAE
class ManualElementsResult(Result): 
    """  The Quality Audit ManualElementsResult is a class containing information about nodes connecting components. They are obtained by the NXOpen.CAE.QualityAudit.ListConnections action. """
    def GetElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Returns the manual elements. 
         Returns pElems ( NXOpen.CAE.FEElement Li): .
        """
        pass
class ManualElementsWithComponentsResult(ManualElementsResult): 
    """  This class contains information about elements connecting components and the connected components. It is obtained from the NXOpen.CAE.QualityAudit.ComponentConnectivity action. """
    pass
class ManualElementsWithMeshesResult(ManualElementsResult): 
    """  This class contains information about elements connecting meshes and the connected meshes. It is obtained from the NXOpen.CAE.QualityAudit.MeshConnectivity action. """
    pass
import NXOpen
import NXOpen.CAE.Connections
class MaximumAngleSettings(ActionSettings): 
    """  This class contains the maximum angle settings available for the following actions: 
        NXOpen.CAE.QualityAudit.MeshLevelConnectionAngleCheck
        NXOpen.CAE.QualityAudit.ObjectLevelConnectionAngleCheck
        . """
    @property
    def MaximumAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumAngle
         Returns the maximum angle allowed.  
           For a greater angle an error is reported   
         
        """
        pass
    def GetMaximumAngleByConnectionType(self, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The maximum angle allowed for the specified connection type. For a greater angle an error is reported 
         Returns maximumAngle ( NXOpen.Expression): .
        """
        pass
import NXOpen.CAE
class MergedNodesResult(Result): 
    """  The Quality Audit MergedNodesResult is a class containing information about nodes connecting components. They are obtained by the NXOpen.CAE.QualityAudit.ListConnections action. """
    def GetNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Returns the merged nodes. 
         Returns pElems ( NXOpen.CAE.FENode Li): .
        """
        pass
class MergedNodesWithComponentsResult(MergedNodesResult): 
    """  This class contains information about nodes connecting components and these components. It is the result of the NXOpen.CAE.QualityAudit.ComponentConnectivity action. """
    pass
class MergedNodesWithMeshesResult(MergedNodesResult): 
    """  This class contains information about nodes connecting meshes and these meshes. It is the result of the NXOpen.CAE.QualityAudit.MeshConnectivity action. """
    pass
class MeshConnectivity(Action): 
    """  This action has as result groups of connected meshes. """
    pass
class MeshLevelConnectionAngleCheck(Action): 
    """  This action checks the angle between the normal directions at the projection points on the supports after meshing. """
    pass
import NXOpen.CAE.Connections
class MeshLevelConnectionAngleResult(Result): 
    """  The Quality Audit MeshLevelConnectionAngleResult is a class containing information about failed connection angle check on universal connections at mesh level. """
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the angle.  
              
         
        """
        pass
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection.  
             
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index .  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
import NXOpen.CAE.Connections
class MeshLevelFailedElementCreationResult(Result): 
    """  The Quality Audit MeshLevelFailedElementCreationResult is a class containing information about failed element creations on universal connections. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection with the failed element creation   
            
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index of the failing element creation in the location.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index of the failing element creation.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index of the failing element creation.  
           See  NXOpen::CAE::Connections::IFlangesContainer  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index of the failing element creation.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
import NXOpen.CAE.Connections
class MeshLevelFailedProjectionResult(Result): 
    """  The Quality Audit MeshLevelFailedProjectionResult is a class containing information about failed projections on universal connections. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection with the failed mesh projection   
            
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index of the failing projection in the location.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index of the failing projection.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index of the failing mesh projection.  
           See  NXOpen::CAE::Connections::IFlangesContainer  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index of the failing projection.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
import NXOpen.CAE.Connections
class MeshLevelFailedProjectionToleranceResult(Result): 
    """ The Quality Audit MeshLevelFailedProjectionToleranceResult is a class containing information about mesh projections 
        that failed the tolerance criteria. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection with the failed mesh tolerance projection  
            
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index of the tolerance failing mesh projection in the location.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index of the tolerance failing mesh projection.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index of the tolerance failing mesh projection.  
           See  NXOpen::CAE::Connections::IFlangesContainer  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index of the tolerance failing mesh projection.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
    @property
    def OffendingDistance(self) -> float:
        """
        Getter for property: (float) OffendingDistance
         Returns the offending distance of the failing mesh projection.  
              
         
        """
        pass
class MeshLevelFlatnessCheck(Action): 
    """  This action checks the flatness around the spot weld after meshing. """
    pass
import NXOpen
import NXOpen.CAE.Connections
class MeshLevelFlatnessResult(Result): 
    """  The Quality Audit MeshLevelFlatnessResult is a class containing information about failed flatness check on universal connections at mesh level. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection.  
             
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index .  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
         Returns the distance.  
              
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index of the first point.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Point
         Returns the result point.  
              
         
        """
        pass
    @property
    def ResultEntity(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ResultEntity
         Returns the result object.  
              
         
        """
        pass
class MeshLevelLengthRangeCheck(Action): 
    """  This action checks the distance between two consecutive supports after meshing. """
    pass
import NXOpen.CAE.Connections
class MeshLevelLengthRangeResult(Result): 
    """  The Quality Audit MeshLevelLengthRangeResult is a class containing information about failed length range check on universal connections at mesh level. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection.  
             
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index .  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length.  
              
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
class MeshLevelLengthRatioRangeCheck(Action): 
    """  This action checks the ratio between two consecutive supports after meshing. """
    pass
import NXOpen.CAE.Connections
class MeshLevelLengthRatioRangeResult(Result): 
    """  The Quality Audit MeshLevelLengthRatioRangeResult is a class containing information about failed length ratio range check on universal connections at mesh level. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection.  
             
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index .  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
    @property
    def Ratio(self) -> float:
        """
        Getter for property: (float) Ratio
         Returns the ratio.  
              
         
        """
        pass
    @property
    def Thickness1(self) -> float:
        """
        Getter for property: (float) Thickness1
         Returns the thickness of the first flange.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def Thickness2(self) -> float:
        """
        Getter for property: (float) Thickness2
         Returns the thickness of the second flange.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
class MeshLevelProjectionCheck(Action): 
    """  This action has as output the list of failed projections of the universal connections at mesh level. """
    pass
import NXOpen.CAE
class MeshSubResult(Result): 
    """  This result a group of connected meshes. """
    def GetMesh(self) -> NXOpen.CAE.Mesh:
        """
         Gets the mesh of this sub-result 
         Returns mesh ( NXOpen.CAE.Mesh): .
        """
        pass
import NXOpen
import NXOpen.CAE.Connections
class MinimumDistanceSettings(ActionSettings): 
    """  This class contains the minimum distance settings available for the following actions: 
        NXOpen.CAE.QualityAudit.FreeEdgeDistanceCheck
        NXOpen.CAE.QualityAudit.ConnectionDistanceCheck
        NXOpen.CAE.QualityAudit.ConnectionPointsDistanceCheck
         """
    @property
    def MinimumDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumDistance
         Returns the minimum distance required.  
           For a smaller distance an error is reported   
         
        """
        pass
    def GetMinimumDistanceByConnectionType(self, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The minimum distance required for the specified connection type. For a smaller distance an error is reported 
         Returns minimumDistance ( NXOpen.Expression): .
        """
        pass
import NXOpen.CAE.Connections
class NonModeledConnectionResult(Result): 
    """  This is a class containing information about the non modeled universal connections. It is in the results of NXOpen.CAE.QualityAudit.ListNonModeledConnections """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection not being modeled   
            
         
        """
        pass
class ObjectLevelConnectionAngleCheck(Action): 
    """ This action checks the angle between the normal directions at the projection points on the supports before meshing. """
    pass
import NXOpen.CAE.Connections
class ObjectLevelConnectionAngleResult(Result): 
    """  The Quality Audit ObjectLevelConnectionAngleResult is a class containing information about failed connection angle check on universal connections at object level. """
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the angle.  
              
         
        """
        pass
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection.  
             
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index .  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
import NXOpen.CAE.Connections
class ObjectLevelCorrectedProjectionResult(Result): 
    """  The Quality Audit ObjectLevelCorrectedProjectionResult is a class containing information about corrected projections on universal connections. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection with the corrected projection   
            
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index of the corrected projection in the location.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index of the corrected projection.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index of the corrected projection.  
           See  NXOpen::CAE::Connections::IFlangesContainer  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index of the corrected projection.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
import NXOpen.CAE.Connections
class ObjectLevelFailedProjectionResult(Result): 
    """  The Quality Audit ObjectLevelFailedProjectionResult is a class containing information about failed projections on universal connections. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection with the failed projection   
            
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index of the failing projection in the location.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index of the failing projection.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index of the failing projection.  
           See  NXOpen::CAE::Connections::IFlangesContainer  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index of the failing projection.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
import NXOpen.CAE.Connections
class ObjectLevelFailedProjectionToleranceResult(Result): 
    """ The Quality Audit ObjectLevelFailedProjectionToleranceResult is a class containing information about projections 
        that failed the tolerance criteria although the projection itself was successful. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection with the failed tolerance projection   
            
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index of the tolerance failing projection in the location.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index of the tolerance failing projection.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index of the tolerance failing projection.  
           See  NXOpen::CAE::Connections::IFlangesContainer  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index of the tolerance failing projection.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
    @property
    def OffendingDistance(self) -> float:
        """
        Getter for property: (float) OffendingDistance
         Returns the offending distance of the failing mesh projection.  
              
         
        """
        pass
class ObjectLevelFlatnessCheck(Action): 
    """  This action checks the flatness around the spot weld before meshing. """
    pass
import NXOpen
import NXOpen.CAE.Connections
class ObjectLevelFlatnessResult(Result): 
    """  The Quality Audit ObjectLevelFlatnessResult is a class containing information about failed flatness check on universal connections at object level. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection.  
             
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index .  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
         Returns the distance.  
              
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index of the first point.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Point
         Returns the result point.  
              
         
        """
        pass
    @property
    def ResultEntity(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ResultEntity
         Returns the result object.  
              
         
        """
        pass
class ObjectLevelLengthRangeCheck(Action): 
    """  This action checks the distance between two consecutive supports before meshing. """
    pass
import NXOpen.CAE.Connections
class ObjectLevelLengthRangeResult(Result): 
    """  The Quality Audit ObjectLevelLengthRangeResult is a class containing information about failed length range check on universal connections at object level. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection.  
             
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index .  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the ratio.  
              
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
class ObjectLevelLengthRatioRangeCheck(Action): 
    """  This action checks the ratio between two consecutive supports before meshing. """
    pass
import NXOpen.CAE.Connections
class ObjectLevelLengthRatioRangeResult(Result): 
    """  The Quality Audit ObjectLevelLengthRatioRangeResult is a class containing information about failed length ratio range check on universal connections at object level. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection.  
             
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index .  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def FlangeIndex(self) -> int:
        """
        Getter for property: (int) FlangeIndex
         Returns the flange index.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
    @property
    def Ratio(self) -> float:
        """
        Getter for property: (float) Ratio
         Returns the ratio.  
              
         
        """
        pass
    @property
    def Thickness1(self) -> float:
        """
        Getter for property: (float) Thickness1
         Returns the thickness of the first flange.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def Thickness2(self) -> float:
        """
        Getter for property: (float) Thickness2
         Returns the thickness of the second flange.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
class ObjectLevelProjectionCheck(Action): 
    """  This action has as output the list of failed projections of the universal connections at object level. """
    pass
import NXOpen
import NXOpen.CAE.Connections
class ProjectionCheckSettings(ActionSettings): 
    """  This class contains settings used by the projection checks. """
    @property
    def Threshold(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Threshold
         Returns the threshold distance from definition point to projection point.  
           Once this is surpassed an error is reported   
         
        """
        pass
    def GetThresholdByConnectionType(self, connectionType: NXOpen.CAE.Connections.ConnectionType) -> NXOpen.Expression:
        """
         The threshold distance from definition point to projection point for the specified connection type. Once this is surpassed an error is reported 
         Returns threshold ( NXOpen.Expression): .
        """
        pass
import NXOpen
class Result(NXOpen.NXObject): 
    """  The Quality Audit Result class offers means to access information about specific problems found while performing specific quality audit checks. """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the text description of this result    
            
         
        """
        pass
    @property
    def Outdated(self) -> bool:
        """
        Getter for property: (bool) Outdated
         Returns the outdated flag of this result    
            
         
        """
        pass
    @property
    def OwningAction(self) -> Action:
        """
        Getter for property: ( Action NXOpen.CAE.) OwningAction
         Returns the owning action that provides this result   
            
         
        """
        pass
    def GetSubResults(self) -> List[Result]:
        """
         Get the sub results, if any 
         Returns subResults ( Result List[NXOpen.CA): .
        """
        pass
class SupportSequenceCheck(Action): 
    """  This action's output is the list of connections having more than 2 supports with wrong order (e.g. first support between the second and third). """
    pass
import NXOpen.CAE.Connections
class UniversalConnectionSynthesisResult(Result): 
    """ This result represents a group of universal connections having the same property. """
    @property
    def Characteristic(self) -> str:
        """
        Getter for property: (str) Characteristic
         Returns the characteristic   
            
         
        """
        pass
    @property
    def Count(self) -> int:
        """
        Getter for property: (int) Count
         Returns the count of the different type   
            
         
        """
        pass
    def GetRepresentedConnections(self) -> List[NXOpen.CAE.Connections.IConnection]:
        """
         Get the connections having the same properties 
         Returns connections ( NXOpen.CAE.Connections.IConnection Li): .
        """
        pass
import NXOpen.CAE.Connections
class WrongSupportSequenceResult(Result): 
    """  The Quality Audit WrongSupportSequenceResult is a class containing information about universal connections whose support sequence order is wrong. """
    @property
    def Connection(self) -> NXOpen.CAE.Connections.IConnection:
        """
        Getter for property: ( NXOpen.CAE.Connections.IConnection) Connection
         Returns the connection with the failed support sequence   
            
         
        """
        pass
    @property
    def CoordinateIndex(self) -> int:
        """
        Getter for property: (int) CoordinateIndex
         Returns the coordinate index in the location where the support sequence is wrong.  
           See  NXOpen::CAE::Connections::Location  for details    
         
        """
        pass
    @property
    def DefinitionIndex(self) -> int:
        """
        Getter for property: (int) DefinitionIndex
         Returns the definition index for the wrong support sequence.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details   
         
        """
        pass
    @property
    def LocationIndex(self) -> int:
        """
        Getter for property: (int) LocationIndex
         Returns the location index for the wrong support sequence.  
           See  NXOpen::CAE::Connections::ILocationsContainer  for details    
         
        """
        pass
