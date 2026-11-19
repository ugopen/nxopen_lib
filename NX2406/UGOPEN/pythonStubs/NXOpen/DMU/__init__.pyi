from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents an object that manages DMU application specific objects and preferences.
##       <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class DMUManager(NXOpen.Object): 
    """ Represents an object that manages DMU application specific objects and preferences.
     """


    ##  Creates the @link NXOpen::DMU::SnapshotCollection NXOpen::DMU::SnapshotCollection@endlink  in the part.
    ##             At max only one instance of @link NXOpen::DMU::SnapshotCollection NXOpen::DMU::SnapshotCollection@endlink 
    ##             can be created in a part.
    ##         
    ##  @return collection (@link SnapshotCollection NXOpen.DMU.SnapshotCollection@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateSnapshotCollection(part: NXOpen.Part) -> SnapshotCollection:
        """
         Creates the @link NXOpen::DMU::SnapshotCollection NXOpen::DMU::SnapshotCollection@endlink  in the part.
                    At max only one instance of @link NXOpen::DMU::SnapshotCollection NXOpen::DMU::SnapshotCollection@endlink 
                    can be created in a part.
                
         @return collection (@link SnapshotCollection NXOpen.DMU.SnapshotCollection@endlink): .
        """
        pass
    
    ##  Returns the @link NXOpen::DMU::SnapshotCollection NXOpen::DMU::SnapshotCollection@endlink  in the part. 
    ##  @return collection (@link SnapshotCollection NXOpen.DMU.SnapshotCollection@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def GetSnapshotCollection(part: NXOpen.Part) -> SnapshotCollection:
        """
         Returns the @link NXOpen::DMU::SnapshotCollection NXOpen::DMU::SnapshotCollection@endlink  in the part. 
         @return collection (@link SnapshotCollection NXOpen.DMU.SnapshotCollection@endlink): .
        """
        pass
    
    ##  Resets the changes made to the part, related to the assets which can be captured in the 
    ##             @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink .
    ##         
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink)  Part that will get reset to design state</param>
    def ResetToDesignState(part: NXOpen.Part) -> None:
        """
         Resets the changes made to the part, related to the assets which can be captured in the 
                    @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink .
                
        """
        pass
    
    ##  Enables and disables the selective snapshot capture properties.
    ##         This will overwrite the customer default settings for specified properties. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="propertiesToBeEnabled"> (List[str])  the ids of the properties to be enabled </param>
    ## <param name="propertiesToBeDisabled"> (List[str])  the ids of the properties to be disabled </param>
    def SetPreferences(part: NXOpen.Part, propertiesToBeEnabled: List[str], propertiesToBeDisabled: List[str]) -> None:
        """
         Enables and disables the selective snapshot capture properties.
                This will overwrite the customer default settings for specified properties. 
        """
        pass
    
import NXOpen
##   Represents the @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  object.
##     
## 
##   <br>  Created in NX12.0.0  <br> 

class ISnapshot(NXOpen.INXObject): 
    """  Represents the <ja_class>NXOpen.DMU.ISnapshot</ja_class> object.
    """


    ##  Applies a @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  on current model.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def Apply(self) -> None:
        """
         Applies a @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  on current model.
        """
        pass
    
    ##  Applies selected properties of @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  on current model.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="propertiesToBeApplied"> (List[str])  the ids of the properties to be applied </param>
    @abstractmethod
    def ApplyProperties(self, propertiesToBeApplied: List[str]) -> None:
        """
         Applies selected properties of @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  on current model.
        """
        pass
    
    ##  Deletes a @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  object.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    @abstractmethod
    def Delete(self) -> None:
        """
         Deletes a @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  object.
        """
        pass
    
    ##  Replaces a @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  object with current state of model.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    @abstractmethod
    def Replace(self) -> None:
        """
         Replaces a @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  object with current state of model.
        """
        pass
    
    ##  Captures and removes selective assets to @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink .
    ##         If the asset already exists while capture, then it will get over-written.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="assetsToBeCaptured"> (List[str])  the ids of the assets to be captured </param>
    ## <param name="assetsToBeRemoved"> (List[str])  the ids of the assets to be removed </param>
    @abstractmethod
    def UpdateAssets(self, assetsToBeCaptured: List[str], assetsToBeRemoved: List[str]) -> None:
        """
         Captures and removes selective assets to @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink .
                If the asset already exists while capture, then it will get over-written.
        """
        pass
    
import NXOpen
##  Represents the collection object for all snapshot in a part. <br> No KF support.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SnapshotCollection(NXOpen.NXObject): 
    """ Represents the collection object for all snapshot in a part."""


    ##  Creates a @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  in the collection.
    ##  @return snapshot (@link ISnapshot NXOpen.DMU.ISnapshot@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    def CreateSnapshot(self) -> ISnapshot:
        """
         Creates a @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  in the collection.
         @return snapshot (@link ISnapshot NXOpen.DMU.ISnapshot@endlink): .
        """
        pass
    
    ##  Creates and inserts a @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  in the collection before the target @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink .
    ##  @return insertedSnapshot (@link ISnapshot NXOpen.DMU.ISnapshot@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::DMU::SnapshotCollection::CreateSnapshot NXOpen::DMU::SnapshotCollection::CreateSnapshot@endlink  and @link NXOpen::DMU::SnapshotCollection::MoveSnapshotsBefore NXOpen::DMU::SnapshotCollection::MoveSnapshotsBefore@endlink .  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="targetSnapshot"> (@link ISnapshot NXOpen.DMU.ISnapshot@endlink) </param>
    def InsertSnapshot(self, targetSnapshot: ISnapshot) -> ISnapshot:
        """
         Creates and inserts a @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  in the collection before the target @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink .
         @return insertedSnapshot (@link ISnapshot NXOpen.DMU.ISnapshot@endlink): .
        """
        pass
    
    ##  Moves sourceSnapshots @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  in the collection after the targetSnapshot @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="targetSnapshot"> (@link ISnapshot NXOpen.DMU.ISnapshot@endlink) </param>
    ## <param name="sourceSnapshots"> (@link ISnapshot List[NXOpen.DMU.ISnapshot]@endlink) </param>
    def MoveSnapshotsAfter(self, targetSnapshot: ISnapshot, sourceSnapshots: List[ISnapshot]) -> None:
        """
         Moves sourceSnapshots @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  in the collection after the targetSnapshot @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink .
        """
        pass
    
    ##  Moves sourceSnapshots @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  in the collection before the targetSnapshot @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="targetSnapshot"> (@link ISnapshot NXOpen.DMU.ISnapshot@endlink) </param>
    ## <param name="sourceSnapshots"> (@link ISnapshot List[NXOpen.DMU.ISnapshot]@endlink) </param>
    def MoveSnapshotsBefore(self, targetSnapshot: ISnapshot, sourceSnapshots: List[ISnapshot]) -> None:
        """
         Moves sourceSnapshots @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink  in the collection before the targetSnapshot @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink .
        """
        pass
    
import NXOpen
##   Represents the @link NXOpen::DMU::Snapshot NXOpen::DMU::Snapshot@endlink  object. 
##          To create a new instance of this class, use the @link NXOpen::DMU::SnapshotCollection NXOpen::DMU::SnapshotCollection@endlink  class. 
##      <br> Instances of this class can be created through DMU.SnapshotCollection object  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Snapshot(NXOpen.NXObject): 
    """  Represents the <ja_class>NXOpen.DMU.Snapshot</ja_class> object. 
         To create a new instance of this class, use the <ja_class>NXOpen.DMU.SnapshotCollection</ja_class> class. 
    """
    pass


## @package NXOpen.DMU
## Classes, Enums and Structs under NXOpen.DMU namespace

