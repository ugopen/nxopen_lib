from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
## Import Kinematics to part file using PLMXML <br> To create a new instance of this class, use @link NXOpen::CLDKin::CldKinematicsManager::CreateImportKinematicsBuilder  NXOpen::CLDKin::CldKinematicsManager::CreateImportKinematicsBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class ImportKinematicsBuilder(NXOpen.Builder): 
    """Import Kinematics to part file using PLMXML"""


    ## Getter for property: (str) KinFileBrowser
    ##  Returns the kin PLMXML file browser   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def KinFileBrowser(self) -> str:
        """
        Getter for property: (str) KinFileBrowser
         Returns the kin PLMXML file browser   
            
         
        """
        pass
    
    ## Setter for property: (str) KinFileBrowser

    ##  Returns the kin PLMXML file browser   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @KinFileBrowser.setter
    def KinFileBrowser(self, filename: str):
        """
        Setter for property: (str) KinFileBrowser
         Returns the kin PLMXML file browser   
            
         
        """
        pass
    
import NXOpen
##    <br> To create a new instance of this class, use @link NXOpen::CLDKin::CldKinematicsManager::CreateJointJogBuilderBuilder  NXOpen::CLDKin::CldKinematicsManager::CreateJointJogBuilderBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class JointJogBuilder(NXOpen.Builder): 
    """  """


    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) LastSelectedDevice
    ##  Returns the last selected device   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.NXObject
    @property
    def LastSelectedDevice(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) LastSelectedDevice
         Returns the last selected device   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) LastSelectedDevice

    ##  Returns the last selected device   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @LastSelectedDevice.setter
    def LastSelectedDevice(self, lastDeviceSelectedTag: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) LastSelectedDevice
         Returns the last selected device   
            
         
        """
        pass
    
    ## Getter for property: (str) PoseName
    ##  Returns the poseName returned  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return str
    @property
    def PoseName(self) -> str:
        """
        Getter for property: (str) PoseName
         Returns the poseName returned  
            
         
        """
        pass
    
    ## Setter for property: (str) PoseName

    ##  Returns the poseName returned  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @PoseName.setter
    def PoseName(self, poseName: str):
        """
        Setter for property: (str) PoseName
         Returns the poseName returned  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectDevice
    ##  Returns the select device   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def SelectDevice(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectDevice
         Returns the select device   
            
         
        """
        pass
    
    ##  Add JointToMap
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nxkJoint"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="distance"> (float) </param>
    def AddJointToMap(self, nxkJoint: NXOpen.TaggedObject, distance: float) -> None:
        """
         Add JointToMap
        """
        pass
    
    ##  Apply Joints 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: None.
    def ApplyJoints(self) -> None:
        """
         Apply Joints 
        """
        pass
    
    ##  Apply Pose 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedPartOccTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  </param>
    def ApplyPose(self, selectedPartOccTag: NXOpen.NXObject) -> None:
        """
         Apply Pose 
        """
        pass
    
    ##  Clear m_jointValuePairVector
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def ClearJointValuePairVector(self) -> None:
        """
         Clear m_jointValuePairVector
        """
        pass
    
    ##  Dry apply pose for part occ
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="partOccTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def DryApplyPoseForPartOcc(self, partOccTag: NXOpen.TaggedObject) -> None:
        """
         Dry apply pose for part occ
        """
        pass
    
    ##  Get the last jogged device in case of multi devices jogging
    ##  @return lastDeviceJoggedDevice (@link NXOpen.NXObject NXOpen.NXObject@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetLastJoggedDevice(self) -> NXOpen.NXObject:
        """
         Get the last jogged device in case of multi devices jogging
         @return lastDeviceJoggedDevice (@link NXOpen.NXObject NXOpen.NXObject@endlink):  .
        """
        pass
    
    ##  Remove JointToMap
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: None.
    def RemoveAllJointMap(self) -> None:
        """
         Remove JointToMap
        """
        pass
    
    ##  Set Joint Jog dialog behaviour data 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sDlgTitle"> (str) </param>
    ## <param name="eDlgState"> (int) </param>
    ## <param name="sPoseName"> (str) </param>
    ## <param name="tDeviceTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def SetJointJogBehaviour(self, sDlgTitle: str, eDlgState: int, sPoseName: str, tDeviceTag: NXOpen.NXObject) -> None:
        """
         Set Joint Jog dialog behaviour data 
        """
        pass
    
    ##  Set the last jogged device in case of multi devices jogging
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="lastDeviceJoggedDevice"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  </param>
    def SetLastJoggedDevice(self, lastDeviceJoggedDevice: NXOpen.NXObject) -> None:
        """
         Set the last jogged device in case of multi devices jogging
        """
        pass
    
    ##  Update JointToMap
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nxkJoint"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="newValue"> (float) </param>
    def UpdateJointToMap(self, nxkJoint: NXOpen.TaggedObject, newValue: float) -> None:
        """
         Update JointToMap
        """
        pass
    
    ##  Update m_jointValuePairVector 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nxkJoint"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="newValue"> (float) </param>
    def UpdateJointValuePairVector(self, nxkJoint: NXOpen.TaggedObject, newValue: float) -> None:
        """
         Update m_jointValuePairVector 
        """
        pass
    
    ##  Update m_partOccToJointVectorMapPtr
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="partOccTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="nxkJointTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def UpdatePartOccToJointVectorMapPtr(self, partOccTag: NXOpen.TaggedObject, nxkJointTag: NXOpen.TaggedObject) -> None:
        """
         Update m_partOccToJointVectorMapPtr
        """
        pass
    
import NXOpen
##    <br> To create a new instance of this class, use @link NXOpen::CLDKin::CldKinematicsManager::CreatePoseEditorBuilder  NXOpen::CLDKin::CldKinematicsManager::CreatePoseEditorBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class PoseEditorBuilder(NXOpen.Builder): 
    """  """


    ## Getter for property: (str) PoseName
    ##  Returns the poseName returned  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return str
    @property
    def PoseName(self) -> str:
        """
        Getter for property: (str) PoseName
         Returns the poseName returned  
            
         
        """
        pass
    
    ## Setter for property: (str) PoseName

    ##  Returns the poseName returned  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @PoseName.setter
    def PoseName(self, poseName: str):
        """
        Setter for property: (str) PoseName
         Returns the poseName returned  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectDevice
    ##  Returns the select device   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def SelectDevice(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectDevice
         Returns the select device   
            
         
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def AddPoseButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
    ##  Create Home Pose 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="tDeviceTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateHomePose(self, tDeviceTag: NXOpen.NXObject) -> None:
        """
         Create Home Pose 
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def DeletePoseButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def EditPoseButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def JumpPoseButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
    ##  Load Instance Poses for selected object or current work part in minimal load
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="displayObj"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def LoadInstancePoseInMinimalLoad(self, displayObj: NXOpen.NXObject) -> None:
        """
         Load Instance Poses for selected object or current work part in minimal load
        """
        pass
    
    ##  Reset Home Pose Values
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="tDeviceTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def ResetHomePoseValues(self, tDeviceTag: NXOpen.NXObject) -> None:
        """
         Reset Home Pose Values
        """
        pass
    
import NXOpen
##    <br> To create a new instance of this class, use @link NXOpen::CLDKin::CldKinematicsManager::CreateRigidGroupBuilder  NXOpen::CLDKin::CldKinematicsManager::CreateRigidGroupBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class RigidGroupBuilder(NXOpen.Builder): 
    """  """


    ## Getter for property: (str) RigidGroupName
    ##  Returns the rigid group name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def RigidGroupName(self) -> str:
        """
        Getter for property: (str) RigidGroupName
         Returns the rigid group name   
            
         
        """
        pass
    
    ## Setter for property: (str) RigidGroupName

    ##  Returns the rigid group name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RigidGroupName.setter
    def RigidGroupName(self, rigidGroupName: str):
        """
        Setter for property: (str) RigidGroupName
         Returns the rigid group name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectObject
    ##  Returns the select device   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectObject(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectObject
         Returns the select device   
            
         
        """
        pass
    
## @package NXOpen.CLDKin
## Classes, Enums and Structs under NXOpen.CLDKin namespace

