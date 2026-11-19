from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.PDM
class SaveCallbackData(NXOpen.TaggedObject): 
    """ JA interface for SaveCallbackData object """
    def GetSaveObjects(self) -> List[NXOpen.PDM.SmartSaveObject]:
        """
         Gets the NXOpen.PDM.SmartSaveObject for NX Objects participating in save operation 
         Returns saveObjects ( NXOpen.PDM.SmartSaveObject Li): .
        """
        pass
import NXOpen
class SaveObserver(NXOpen.TaggedObjectCollection): 
    """ This class is responsible for invoking registered callbacks at different stages in the save operation. """
    AutoassignCb = Callable[[SaveCallbackData], None]
    def AddAutoassignCallback(autoassign_cb: SaveObserver.AutoassignCb) -> int:
        """
         Registers a user defined AutoAssign callback that is called before auto-assigning attributes 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    InitializeCb = Callable[[SaveCallbackData], None]
    def AddInitializeCallback(initialize_cb: SaveObserver.InitializeCb) -> int:
        """
         Registers a user defined Initialize callback that is called during initialization of save objects. 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    def RemoveAutoassignCallback(id: int) -> None:
        """
         Unregisters the user defined AutoAssign callback 
        """
        pass
    def RemoveInitializeCallback(id: int) -> None:
        """
         Unregisters the user defined Initialize callback 
        """
        pass
