from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ImportKinematicsBuilder(NXOpen.Builder): 
    """Import Kinematics to part file using PLMXML"""
    @property
    def KinFileBrowser(self) -> str:
        """
        Getter for property: (str) KinFileBrowser
         Returns the kin PLMXML file browser   
            
         
        """
        pass
    @KinFileBrowser.setter
    def KinFileBrowser(self, filename: str):
        """
        Setter for property: (str) KinFileBrowser
         Returns the kin PLMXML file browser   
            
         
        """
        pass
import NXOpen
class JointJogBuilder(NXOpen.Builder): 
    """  """
    @property
    def LastSelectedDevice(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) LastSelectedDevice
         Returns the last selected device   
            
         
        """
        pass
    @LastSelectedDevice.setter
    def LastSelectedDevice(self, lastDeviceSelectedTag: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) LastSelectedDevice
         Returns the last selected device   
            
         
        """
        pass
    @property
    def PoseName(self) -> str:
        """
        Getter for property: (str) PoseName
         Returns the poseName returned  
            
         
        """
        pass
    @PoseName.setter
    def PoseName(self, poseName: str):
        """
        Setter for property: (str) PoseName
         Returns the poseName returned  
            
         
        """
        pass
    @property
    def SelectDevice(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) SelectDevice
         Returns the select device   
            
         
        """
        pass
    def AddJointToMap(self, nxkJoint: NXOpen.TaggedObject, distance: float) -> None:
        """
         Add JointToMap
        """
        pass
    def ApplyJoints(self) -> None:
        """
         Apply Joints 
        """
        pass
    def ApplyPose(self, selectedPartOccTag: NXOpen.NXObject) -> None:
        """
         Apply Pose 
        """
        pass
    def ClearJointValuePairVector(self) -> None:
        """
         Clear m_jointValuePairVector
        """
        pass
    def DryApplyPoseForPartOcc(self, partOccTag: NXOpen.TaggedObject) -> None:
        """
         Dry apply pose for part occ
        """
        pass
    def GetLastJoggedDevice(self) -> NXOpen.NXObject:
        """
         Get the last jogged device in case of multi devices jogging
         Returns lastDeviceJoggedDevice ( NXOpen.NXObject):  .
        """
        pass
    def RemoveAllJointMap(self) -> None:
        """
         Remove JointToMap
        """
        pass
    def SetJointJogBehaviour(self, sDlgTitle: str, eDlgState: int, sPoseName: str, tDeviceTag: NXOpen.NXObject) -> None:
        """
         Set Joint Jog dialog behaviour data 
        """
        pass
    def SetLastJoggedDevice(self, lastDeviceJoggedDevice: NXOpen.NXObject) -> None:
        """
         Set the last jogged device in case of multi devices jogging
        """
        pass
    def UpdateJointToMap(self, nxkJoint: NXOpen.TaggedObject, newValue: float) -> None:
        """
         Update JointToMap
        """
        pass
    def UpdateJointValuePairVector(self, nxkJoint: NXOpen.TaggedObject, newValue: float) -> None:
        """
         Update m_jointValuePairVector 
        """
        pass
    def UpdatePartOccToJointVectorMapPtr(self, partOccTag: NXOpen.TaggedObject, nxkJointTag: NXOpen.TaggedObject) -> None:
        """
         Update m_partOccToJointVectorMapPtr
        """
        pass
import NXOpen
class PoseEditorBuilder(NXOpen.Builder): 
    """  """
    @property
    def PoseName(self) -> str:
        """
        Getter for property: (str) PoseName
         Returns the poseName returned  
            
         
        """
        pass
    @PoseName.setter
    def PoseName(self, poseName: str):
        """
        Setter for property: (str) PoseName
         Returns the poseName returned  
            
         
        """
        pass
    @property
    def SelectDevice(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) SelectDevice
         Returns the select device   
            
         
        """
        pass
    def AddPoseButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def CreateHomePose(self, tDeviceTag: NXOpen.NXObject) -> None:
        """
         Create Home Pose 
        """
        pass
    def DeletePoseButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def EditPoseButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def JumpPoseButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def LoadInstancePoseInMinimalLoad(self, displayObj: NXOpen.NXObject) -> None:
        """
         Load Instance Poses for selected object or current work part in minimal load
        """
        pass
    def ResetHomePoseValues(self, tDeviceTag: NXOpen.NXObject) -> None:
        """
         Reset Home Pose Values
        """
        pass
import NXOpen
class RigidGroupBuilder(NXOpen.Builder): 
    """  """
    @property
    def RigidGroupName(self) -> str:
        """
        Getter for property: (str) RigidGroupName
         Returns the rigid group name   
            
         
        """
        pass
    @RigidGroupName.setter
    def RigidGroupName(self, rigidGroupName: str):
        """
        Setter for property: (str) RigidGroupName
         Returns the rigid group name   
            
         
        """
        pass
    @property
    def SelectObject(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectObject
         Returns the select device   
            
         
        """
        pass
