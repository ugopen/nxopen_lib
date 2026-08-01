from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class DMUManager(NXOpen.Object): 
    """ Represents an object that manages DMU application specific objects and preferences.
     """
    def CreateSnapshotCollection(part: NXOpen.Part) -> SnapshotCollection:
        """
         Creates the NXOpen.DMU.SnapshotCollection in the part.
                    At max only one instance of NXOpen.DMU.SnapshotCollection
                    can be created in a part.
                
         Returns collection ( SnapshotCollection NXOp): .
        """
        pass
    def GetSnapshotCollection(part: NXOpen.Part) -> SnapshotCollection:
        """
         Returns the NXOpen.DMU.SnapshotCollection in the part. 
         Returns collection ( SnapshotCollection NXOp): .
        """
        pass
    def ResetToDesignState(part: NXOpen.Part) -> None:
        """
         Resets the changes made to the part, related to the assets which can be captured in the 
                    NXOpen.DMU.ISnapshot.
                
        """
        pass
    def SetPreferences(part: NXOpen.Part, propertiesToBeEnabled: List[str], propertiesToBeDisabled: List[str]) -> None:
        """
         Enables and disables the selective snapshot capture properties.
                This will overwrite the customer default settings for specified properties. 
        """
        pass
import NXOpen
class ISnapshot(NXOpen.INXObject): 
    """  Represents the NXOpen.DMU.ISnapshot object.
    """
    @abstractmethod
    def Apply(self) -> None:
        """
         Applies a NXOpen.DMU.ISnapshot on current model.
        """
        pass
    @abstractmethod
    def ApplyProperties(self, propertiesToBeApplied: List[str]) -> None:
        """
         Applies selected properties of NXOpen.DMU.ISnapshot on current model.
        """
        pass
    @abstractmethod
    def Delete(self) -> None:
        """
         Deletes a NXOpen.DMU.ISnapshot object.
        """
        pass
    @abstractmethod
    def Replace(self) -> None:
        """
         Replaces a NXOpen.DMU.ISnapshot object with current state of model.
        """
        pass
    @abstractmethod
    def UpdateAssets(self, assetsToBeCaptured: List[str], assetsToBeRemoved: List[str]) -> None:
        """
         Captures and removes selective assets to NXOpen.DMU.ISnapshot.
                If the asset already exists while capture, then it will get over-written.
        """
        pass
import NXOpen
class SnapshotCollection(NXOpen.NXObject): 
    """ Represents the collection object for all snapshot in a part."""
    def CreateSnapshot(self) -> ISnapshot:
        """
         Creates a NXOpen.DMU.ISnapshot in the collection.
         Returns snapshot ( ISnapshot NXOp): .
        """
        pass
    def InsertSnapshot(self, targetSnapshot: ISnapshot) -> ISnapshot:
        """
         Creates and inserts a NXOpen.DMU.ISnapshot in the collection before the target NXOpen.DMU.ISnapshot.
         Returns insertedSnapshot ( ISnapshot NXOp): .
        """
        pass
    def MoveSnapshotsAfter(self, targetSnapshot: ISnapshot, sourceSnapshots: List[ISnapshot]) -> None:
        """
         Moves sourceSnapshots NXOpen.DMU.ISnapshot in the collection after the targetSnapshot NXOpen.DMU.ISnapshot.
        """
        pass
    def MoveSnapshotsBefore(self, targetSnapshot: ISnapshot, sourceSnapshots: List[ISnapshot]) -> None:
        """
         Moves sourceSnapshots NXOpen.DMU.ISnapshot in the collection before the targetSnapshot NXOpen.DMU.ISnapshot.
        """
        pass
import NXOpen
class Snapshot(NXOpen.NXObject): 
    """  Represents the NXOpen.DMU.Snapshot object. 
         To create a new instance of this class, use the NXOpen.DMU.SnapshotCollection class. 
    """
    pass
