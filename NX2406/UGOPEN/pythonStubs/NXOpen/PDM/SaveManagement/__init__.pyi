from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.PDM
##  JA interface for SaveCallbackData object  <br> This cannot be created  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class SaveCallbackData(NXOpen.TaggedObject): 
    """ JA interface for SaveCallbackData object """


    ##  Gets the @link NXOpen::PDM::SmartSaveObject NXOpen::PDM::SmartSaveObject@endlink  for NX Objects participating in save operation 
    ##  @return saveObjects (@link NXOpen.PDM.SmartSaveObject List[NXOpen.PDM.SmartSaveObject]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetSaveObjects(self) -> List[NXOpen.PDM.SmartSaveObject]:
        """
         Gets the @link NXOpen::PDM::SmartSaveObject NXOpen::PDM::SmartSaveObject@endlink  for NX Objects participating in save operation 
         @return saveObjects (@link NXOpen.PDM.SmartSaveObject List[NXOpen.PDM.SmartSaveObject]@endlink): .
        """
        pass
    
import NXOpen
##  This class is responsible for invoking registered callbacks at different stages in the save operation.  <br> To obtain an instance of this class, refer to @link NXOpen::PDM::PdmSession  NXOpen::PDM::PdmSession @endlink  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class SaveObserver(NXOpen.TaggedObjectCollection): 
    """ This class is responsible for invoking registered callbacks at different stages in the save operation. """


    ##  User defined AutoAssign callback that is called before auto-assigning attributes 
    ## A callback definition with the following input arguments: 
    ##  - @link SaveCallbackData NXOpen.PDM.SaveManagement.SaveCallbackData@endlink
    ##  and no return type
    AutoassignCb = Callable[[SaveCallbackData], None]
    
    
    ##  Registers a user defined AutoAssign callback that is called before auto-assigning attributes 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="autoassign_cb"> (@link SaveObserver.AutoassignCb NXOpen.PDM.SaveManagement.SaveObserver.AutoassignCb@endlink)  method to register </param>
    def AddAutoassignCallback(autoassign_cb: SaveObserver.AutoassignCb) -> int:
        """
         Registers a user defined AutoAssign callback that is called before auto-assigning attributes 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  User defined Initialize callback that is called during initialization of the save objects. 
    ## A callback definition with the following input arguments: 
    ##  - @link SaveCallbackData NXOpen.PDM.SaveManagement.SaveCallbackData@endlink
    ##  and no return type
    InitializeCb = Callable[[SaveCallbackData], None]
    
    
    ##  Registers a user defined Initialize callback that is called during initialization of save objects. 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="initialize_cb"> (@link SaveObserver.InitializeCb NXOpen.PDM.SaveManagement.SaveObserver.InitializeCb@endlink)  method to register </param>
    def AddInitializeCallback(initialize_cb: SaveObserver.InitializeCb) -> int:
        """
         Registers a user defined Initialize callback that is called during initialization of save objects. 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  Unregisters the user defined AutoAssign callback 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemoveAutoassignCallback(id: int) -> None:
        """
         Unregisters the user defined AutoAssign callback 
        """
        pass
    
    ##  Unregisters the user defined Initialize callback 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemoveInitializeCallback(id: int) -> None:
        """
         Unregisters the user defined Initialize callback 
        """
        pass
    
## @package NXOpen.PDM.SaveManagement
## Classes, Enums and Structs under NXOpen.PDM.SaveManagement namespace

