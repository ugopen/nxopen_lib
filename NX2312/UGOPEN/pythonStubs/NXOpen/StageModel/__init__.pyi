from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents the Stage Model CAD Manager class. <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class CadManager(NXOpen.Object): 
    """ Represents the Stage Model CAD Manager class."""
    pass


import NXOpen.Tooling
##  Represents a @link StageModel::Stage StageModel::Stage@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::StageModel::Manager::CreateDeriveStockBuilder  NXOpen::StageModel::Manager::CreateDeriveStockBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Associative </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Clearance.Value </term> <description> 
##  
## 3.0 (millimeters part), 0.125 (inches part) </description> </item> 
## 
## <item><term> 
##  
## InputSymmetricValue </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsClearanceAutoSet </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ReferenceCsysType </term> <description> 
##  
## Wcs </description> </item> 
## 
## <item><term> 
##  
## ShowDiameterSymbol </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## SizePrecision </term> <description> 
##  
## 3 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class DeriveStockBuilder(NXOpen.Tooling.StockSizeBuilder): 
    """ Represents a <ja_class>StageModel.Stage</ja_class> builder """


    ## Getter for property: (@link StockStageDetailsBuilder NXOpen.StageModel.StockStageDetailsBuilder@endlink) StockStageDetails
    ##   the Stock Stage Detaild Builder as @link StageModel::StockStageDetailsBuilder StageModel::StockStageDetailsBuilder@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return StockStageDetailsBuilder
    @property
    def StockStageDetails(self) -> StockStageDetailsBuilder:
        """
        Getter for property: (@link StockStageDetailsBuilder NXOpen.StageModel.StockStageDetailsBuilder@endlink) StockStageDetails
          the Stock Stage Detaild Builder as @link StageModel::StockStageDetailsBuilder StageModel::StockStageDetailsBuilder@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link StockStageDetailsBuilder NXOpen.StageModel.StockStageDetailsBuilder@endlink) StockStageDetails

    ##   the Stock Stage Detaild Builder as @link StageModel::StockStageDetailsBuilder StageModel::StockStageDetailsBuilder@endlink    
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @StockStageDetails.setter
    def StockStageDetails(self, stageDetails: StockStageDetailsBuilder):
        """
        Setter for property: (@link StockStageDetailsBuilder NXOpen.StageModel.StockStageDetailsBuilder@endlink) StockStageDetails
          the Stock Stage Detaild Builder as @link StageModel::StockStageDetailsBuilder StageModel::StockStageDetailsBuilder@endlink    
            
         
        """
        pass
    
import NXOpen
##  Represents the Stage Model Manager class. <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class Manager(NXOpen.Object): 
    """ Represents the Stage Model Manager class."""


    ##  Returns the @link NXOpen::StageModel::ObjectUpdateStateManager NXOpen::StageModel::ObjectUpdateStateManager@endlink  belonging to this manager 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @link ObjectUpdateStateManager NXOpen.StageModel.ObjectUpdateStateManager@endlink
    @property
    def ObjectUpdateStateManager() -> ObjectUpdateStateManager:
        """
         Returns the @link NXOpen::StageModel::ObjectUpdateStateManager NXOpen::StageModel::ObjectUpdateStateManager@endlink  belonging to this manager 
        """
        pass
    
    ##  Creates a @link StageModel::DeriveStockBuilder StageModel::DeriveStockBuilder@endlink  
    ##  @return builder (@link DeriveStockBuilder NXOpen.StageModel.DeriveStockBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="stage"> (@link Stage NXOpen.StageModel.Stage@endlink) </param>
    def CreateDeriveStockBuilder(part: NXOpen.Part, stage: Stage) -> DeriveStockBuilder:
        """
         Creates a @link StageModel::DeriveStockBuilder StageModel::DeriveStockBuilder@endlink  
         @return builder (@link DeriveStockBuilder NXOpen.StageModel.DeriveStockBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link StageModel::ReferenceStockBuilder StageModel::ReferenceStockBuilder@endlink  
    ##  @return builder (@link ReferenceStockBuilder NXOpen.StageModel.ReferenceStockBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="stage"> (@link Stage NXOpen.StageModel.Stage@endlink) </param>
    ## <param name="sourceFileName"> (str) </param>
    def CreateReferenceStockBuilder(part: NXOpen.Part, stage: Stage, sourceFileName: str) -> ReferenceStockBuilder:
        """
         Creates a @link StageModel::ReferenceStockBuilder StageModel::ReferenceStockBuilder@endlink  
         @return builder (@link ReferenceStockBuilder NXOpen.StageModel.ReferenceStockBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link StageModel::ReplacePartBuilder StageModel::ReplacePartBuilder@endlink  
    ##  @return builder (@link ReplacePartBuilder NXOpen.StageModel.ReplacePartBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateReplacePartBuilder(part: NXOpen.Part) -> ReplacePartBuilder:
        """
         Creates a @link StageModel::ReplacePartBuilder StageModel::ReplacePartBuilder@endlink  
         @return builder (@link ReplacePartBuilder NXOpen.StageModel.ReplacePartBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link StageModel::StageBuilder StageModel::StageBuilder@endlink  
    ##  @return builder (@link StageBuilder NXOpen.StageModel.StageBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="stage"> (@link Stage NXOpen.StageModel.Stage@endlink) </param>
    def CreateStageBuilder(part: NXOpen.Part, stage: Stage) -> StageBuilder:
        """
         Creates a @link StageModel::StageBuilder StageModel::StageBuilder@endlink  
         @return builder (@link StageBuilder NXOpen.StageModel.StageBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link StageModel::StageSetBuilder StageModel::StageSetBuilder@endlink  
    ##  @return builder (@link StageSetBuilder NXOpen.StageModel.StageSetBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="stageSet"> (@link StageSet NXOpen.StageModel.StageSet@endlink) </param>
    def CreateStageSetBuilder(part: NXOpen.Part, stageSet: StageSet) -> StageSetBuilder:
        """
         Creates a @link StageModel::StageSetBuilder StageModel::StageSetBuilder@endlink  
         @return builder (@link StageSetBuilder NXOpen.StageModel.StageSetBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link StageModel::StandardStockBuilder StageModel::StandardStockBuilder@endlink  
    ##  @return builder (@link StandardStockBuilder NXOpen.StageModel.StandardStockBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="stage"> (@link Stage NXOpen.StageModel.Stage@endlink) </param>
    ## <param name="surceFileName"> (str) </param>
    def CreateStandardStockBuilder(part: NXOpen.Part, stage: Stage, surceFileName: str) -> StandardStockBuilder:
        """
         Creates a @link StageModel::StandardStockBuilder StageModel::StandardStockBuilder@endlink  
         @return builder (@link StandardStockBuilder NXOpen.StageModel.StandardStockBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link StageModel::StockStageDetailsBuilder StageModel::StockStageDetailsBuilder@endlink  
    ##  @return builder (@link StockStageDetailsBuilder NXOpen.StageModel.StockStageDetailsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="stagedetails"> (@link StockStageDetails NXOpen.StageModel.StockStageDetails@endlink) </param>
    def CreateStockStageDetailsBuilder(part: NXOpen.Part, stagedetails: StockStageDetails) -> StockStageDetailsBuilder:
        """
         Creates a @link StageModel::StockStageDetailsBuilder StageModel::StockStageDetailsBuilder@endlink  
         @return builder (@link StockStageDetailsBuilder NXOpen.StageModel.StockStageDetailsBuilder@endlink): .
        """
        pass
    
    ##  Get the active stage 
    ##  @return activeStage (@link Stage NXOpen.StageModel.Stage@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetActiveStage() -> Stage:
        """
         Get the active stage 
         @return activeStage (@link Stage NXOpen.StageModel.Stage@endlink): .
        """
        pass
    
    ##  Get the active stage set 
    ##  @return activeStageSet (@link StageSet NXOpen.StageModel.StageSet@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetActiveStageSet() -> StageSet:
        """
         Get the active stage set 
         @return activeStageSet (@link StageSet NXOpen.StageModel.StageSet@endlink): .
        """
        pass
    
    ##  Get loaded stage sets 
    ##  @return stageSets (@link StageSet List[NXOpen.StageModel.StageSet]@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLoadedStageSets() -> List[StageSet]:
        """
         Get loaded stage sets 
         @return stageSets (@link StageSet List[NXOpen.StageModel.StageSet]@endlink): .
        """
        pass
    
import NXOpen
##  Provides interface for objtects up to date status.  <br> To obtain an instance of this class, refer to @link NXOpen::StageModel::Manager  NXOpen::StageModel::Manager @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class ObjectUpdateStateManager(NXOpen.Object): 
    """ Provides interface for objtects up to date status. """


    ##  Defines allowed Up to date status. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## InvalidUpToDate</term><description> 
    ## </description> </item><item><term> 
    ## UpToDate</term><description> 
    ## </description> </item><item><term> 
    ## UpToDateToOodParent</term><description> 
    ## </description> </item><item><term> 
    ## OutOfDateCannotUpdate</term><description> 
    ## </description> </item><item><term> 
    ## Failed</term><description> 
    ## </description> </item><item><term> 
    ## OutOfDateCanUpdate</term><description> 
    ## </description> </item><item><term> 
    ## NoState</term><description> 
    ## </description> </item><item><term> 
    ## UpdateFrozen</term><description> 
    ## </description> </item><item><term> 
    ## ParentNotLoaded</term><description> 
    ## </description> </item><item><term> 
    ## InterPartAssoBroken</term><description> 
    ## </description> </item></list>
    class Status(Enum):
        """
        Members Include: <InvalidUpToDate> <UpToDate> <UpToDateToOodParent> <OutOfDateCannotUpdate> <Failed> <OutOfDateCanUpdate> <NoState> <UpdateFrozen> <ParentNotLoaded> <InterPartAssoBroken>
        """
        InvalidUpToDate: int
        UpToDate: int
        UpToDateToOodParent: int
        OutOfDateCannotUpdate: int
        Failed: int
        OutOfDateCanUpdate: int
        NoState: int
        UpdateFrozen: int
        ParentNotLoaded: int
        InterPartAssoBroken: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ObjectUpdateStateManager.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Get up to date status of the object.
    ##  @return upTodateStatus (@link ObjectUpdateStateManager.Status NXOpen.StageModel.ObjectUpdateStateManager.Status@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="objectValue"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    @staticmethod
    def GetStatus(objectValue: NXOpen.TaggedObject) -> ObjectUpdateStateManager.Status:
        """
         Get up to date status of the object.
         @return upTodateStatus (@link ObjectUpdateStateManager.Status NXOpen.StageModel.ObjectUpdateStateManager.Status@endlink): .
        """
        pass
    
    ##  Updates all given out-of-date objects to make them up to date 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ##  The objects to be made up to date 
    def MakeUpToDate(objects: List[NXOpen.TaggedObject], undoMarkId: int) -> None:
        """
         Updates all given out-of-date objects to make them up to date 
        """
        pass
    
import NXOpen
##  Represents the Stage Model PMI Manager class. <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class PmiManager(NXOpen.Object): 
    """ Represents the Stage Model PMI Manager class."""


    ##  Creates a @link StageModel::ReusePmiBuilder StageModel::ReusePmiBuilder@endlink  
    ##  @return builder (@link ReusePmiBuilder NXOpen.StageModel.ReusePmiBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="stage"> (@link Stage NXOpen.StageModel.Stage@endlink) </param>
    def CreateReusePmiBuilder(stage: Stage) -> ReusePmiBuilder:
        """
         Creates a @link StageModel::ReusePmiBuilder StageModel::ReusePmiBuilder@endlink  
         @return builder (@link ReusePmiBuilder NXOpen.StageModel.ReusePmiBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link StageModel::ReuseViewBuilder StageModel::ReuseViewBuilder@endlink  
    ##  @return builder (@link ReuseViewBuilder NXOpen.StageModel.ReuseViewBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="stage"> (@link Stage NXOpen.StageModel.Stage@endlink) </param>
    def CreateReuseViewBuilder(stage: Stage) -> ReuseViewBuilder:
        """
         Creates a @link StageModel::ReuseViewBuilder StageModel::ReuseViewBuilder@endlink  
         @return builder (@link ReuseViewBuilder NXOpen.StageModel.ReuseViewBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents a @link StageModel::Stage StageModel::Stage@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::StageModel::Manager::CreateReferenceStockBuilder  NXOpen::StageModel::Manager::CreateReferenceStockBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ReferenceStockBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>StageModel.Stage</ja_class> builder """


    ## Getter for property: (str) ReferencePart
    ##   the reference part   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def ReferencePart(self) -> str:
        """
        Getter for property: (str) ReferencePart
          the reference part   
            
         
        """
        pass
    
    ## Setter for property: (str) ReferencePart

    ##   the reference part   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ReferencePart.setter
    def ReferencePart(self, referencePart: str):
        """
        Setter for property: (str) ReferencePart
          the reference part   
            
         
        """
        pass
    
    ## Getter for property: (@link StockStageDetailsBuilder NXOpen.StageModel.StockStageDetailsBuilder@endlink) StockStageDetails
    ##   the Stock Stage Details Builder as @link StageModel::StockStageDetailsBuilder StageModel::StockStageDetailsBuilder@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return StockStageDetailsBuilder
    @property
    def StockStageDetails(self) -> StockStageDetailsBuilder:
        """
        Getter for property: (@link StockStageDetailsBuilder NXOpen.StageModel.StockStageDetailsBuilder@endlink) StockStageDetails
          the Stock Stage Details Builder as @link StageModel::StockStageDetailsBuilder StageModel::StockStageDetailsBuilder@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link StockStageDetailsBuilder NXOpen.StageModel.StockStageDetailsBuilder@endlink) StockStageDetails

    ##   the Stock Stage Details Builder as @link StageModel::StockStageDetailsBuilder StageModel::StockStageDetailsBuilder@endlink    
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @StockStageDetails.setter
    def StockStageDetails(self, stageDetails: StockStageDetailsBuilder):
        """
        Setter for property: (@link StockStageDetailsBuilder NXOpen.StageModel.StockStageDetailsBuilder@endlink) StockStageDetails
          the Stock Stage Details Builder as @link StageModel::StockStageDetailsBuilder StageModel::StockStageDetailsBuilder@endlink    
            
         
        """
        pass
    
import NXOpen
##  Represents a @link StageModel::ReplacePartBuilder StageModel::ReplacePartBuilder@endlink . <br> To create a new instance of this class, use @link NXOpen::StageModel::Manager::CreateReplacePartBuilder  NXOpen::StageModel::Manager::CreateReplacePartBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## EnumDesignReference </term> <description> 
##  
## DesignPart </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1980.0.0  <br> 

class ReplacePartBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>StageModel.ReplacePartBuilder</ja_class>."""


    ##  Represents the two options the user can have. Either replacing the Design Part or another referenced part by the StageSet
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## DesignPart</term><description> 
    ## </description> </item><item><term> 
    ## ReferencePart</term><description> 
    ## </description> </item></list>
    class DesignPartTypes(Enum):
        """
        Members Include: <DesignPart> <ReferencePart>
        """
        DesignPart: int
        ReferencePart: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReplacePartBuilder.DesignPartTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ReplacePartBuilder.DesignPartTypes NXOpen.StageModel.ReplacePartBuilder.DesignPartTypes@endlink) EnumDesignReference
    ##   the enum design reference   
    ##     
    ##  
    ## Getter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return ReplacePartBuilder.DesignPartTypes
    @property
    def EnumDesignReference(self) -> ReplacePartBuilder.DesignPartTypes:
        """
        Getter for property: (@link ReplacePartBuilder.DesignPartTypes NXOpen.StageModel.ReplacePartBuilder.DesignPartTypes@endlink) EnumDesignReference
          the enum design reference   
            
         
        """
        pass
    
    ## Setter for property: (@link ReplacePartBuilder.DesignPartTypes NXOpen.StageModel.ReplacePartBuilder.DesignPartTypes@endlink) EnumDesignReference

    ##   the enum design reference   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @EnumDesignReference.setter
    def EnumDesignReference(self, enumDesignReference: ReplacePartBuilder.DesignPartTypes):
        """
        Setter for property: (@link ReplacePartBuilder.DesignPartTypes NXOpen.StageModel.ReplacePartBuilder.DesignPartTypes@endlink) EnumDesignReference
          the enum design reference   
            
         
        """
        pass
    
    ##  Set reference part. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="reference"> (str) </param>
    def SetReferencePart(builder: ReplacePartBuilder, reference: str) -> None:
        """
         Set reference part. 
        """
        pass
    
    ##  Set replacement part. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="replacementPart"> (str) </param>
    def SetReplacementPart(builder: ReplacePartBuilder, replacementPart: str) -> None:
        """
         Set replacement part. 
        """
        pass
    
import NXOpen
import NXOpen.Annotations
##  Represents a @link  NXOpen::StageModel::ReusePmiBuilder  NXOpen::StageModel::ReusePmiBuilder@endlink . <br> To create a new instance of this class, use @link NXOpen::StageModel::PmiManager::CreateReusePmiBuilder  NXOpen::StageModel::PmiManager::CreateReusePmiBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ReusePmiBuilder(NXOpen.Builder): 
    """ Represents a <ja_class> NXOpen.StageModel.ReusePmiBuilder</ja_class>."""


    ## Getter for property: (bool) Associative
    ##   the associative setting   
    ##     
    ##  
    ## Getter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
          the associative setting   
            
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##   the associative setting   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
          the associative setting   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) DestinationStage
    ##   the destination stage   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def DestinationStage(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) DestinationStage
          the destination stage   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) DestinationStage

    ##   the destination stage   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DestinationStage.setter
    def DestinationStage(self, destinationStage: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) DestinationStage
          the destination stage   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.PmiInterpartSelectionBuilder NXOpen.Annotations.PmiInterpartSelectionBuilder@endlink) ReusePMI
    ##   the list of selected PMI to be re-used   
    ##     
    ##  
    ## Getter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Annotations.PmiInterpartSelectionBuilder
    @property
    def ReusePMI(self) -> NXOpen.Annotations.PmiInterpartSelectionBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.PmiInterpartSelectionBuilder NXOpen.Annotations.PmiInterpartSelectionBuilder@endlink) ReusePMI
          the list of selected PMI to be re-used   
            
         
        """
        pass
    
    ##  The parent of a reused PMI 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="child"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def GetPmiParent(builder: ReusePmiBuilder, child: NXOpen.TaggedObject) -> None:
        """
         The parent of a reused PMI 
        """
        pass
    
import NXOpen
##  Represents a @link  NXOpen::StageModel::ReuseViewBuilder  NXOpen::StageModel::ReuseViewBuilder@endlink . <br> To create a new instance of this class, use @link NXOpen::StageModel::PmiManager::CreateReuseViewBuilder  NXOpen::StageModel::PmiManager::CreateReuseViewBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class ReuseViewBuilder(NXOpen.Builder): 
    """ Represents a <ja_class> NXOpen.StageModel.ReuseViewBuilder</ja_class>."""


    ## Getter for property: (bool) Associative
    ##   the associative setting   
    ##     
    ##  
    ## Getter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
          the associative setting   
            
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##   the associative setting   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
          the associative setting   
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludePmi
    ##   the include pmi setting   
    ##     
    ##  
    ## Getter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def IncludePmi(self) -> bool:
        """
        Getter for property: (bool) IncludePmi
          the include pmi setting   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludePmi

    ##   the include pmi setting   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @IncludePmi.setter
    def IncludePmi(self, includePmi: bool):
        """
        Setter for property: (bool) IncludePmi
          the include pmi setting   
            
         
        """
        pass
    
    ##  The selected views 
    ##  @return selectedViews (@link NXOpen.View List[NXOpen.View]@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    @staticmethod
    def GetSelectedViews(builder: ReuseViewBuilder) -> List[NXOpen.View]:
        """
         The selected views 
         @return selectedViews (@link NXOpen.View List[NXOpen.View]@endlink): .
        """
        pass
    
    ##  The selected views 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="selectedViews"> (@link NXOpen.View List[NXOpen.View]@endlink) </param>
    def SetSelectedViews(builder: ReuseViewBuilder, selectedViews: List[NXOpen.View]) -> None:
        """
         The selected views 
        """
        pass
    
import NXOpen
import NXOpen.ModlUtils
import NXOpen.PDM
##  Represents a @link StageModel::StageBuilder StageModel::StageBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::StageModel::Manager::CreateStageBuilder  NXOpen::StageModel::Manager::CreateStageBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class StageBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>StageModel.StageBuilder</ja_class>. """


    ##  Create a new stage in the specified staged model set and append it to the stage before, or in front of the staged model set list if no stage before is given
    ##  @return createdStage (@link Stage NXOpen.StageModel.Stage@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="stageSet"> (@link StageSet NXOpen.StageModel.StageSet@endlink) </param>
    ## <param name="stageBefore"> (@link Stage NXOpen.StageModel.Stage@endlink) </param>
    ## <param name="stageName"> (str) </param>
    ## <param name="stageDescription"> (str) </param>
    def CreateStage(builder: StageBuilder, stageSet: StageSet, stageBefore: Stage, stageName: str, stageDescription: str) -> Stage:
        """
         Create a new stage in the specified staged model set and append it to the stage before, or in front of the staged model set list if no stage before is given
         @return createdStage (@link Stage NXOpen.StageModel.Stage@endlink): .
        """
        pass
    
    ##  Edit builder stage's description 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="stageDescription"> (str) </param>
    def EditStageDescription(builder: StageBuilder, stageDescription: str) -> None:
        """
         Edit builder stage's description 
        """
        pass
    
    ##  Edit builder stage's name
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="stageName"> (str) </param>
    def EditStageName(builder: StageBuilder, stageName: str) -> None:
        """
         Edit builder stage's name
        """
        pass
    
    ##  Registers the import template part object 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="templateBuilder"> (@link NXOpen.ModlUtils.ImportTemplatePartBuilder NXOpen.ModlUtils.ImportTemplatePartBuilder@endlink) </param>
    def RegisterImportTemplatePartObject(builder: StageBuilder, templateBuilder: NXOpen.ModlUtils.ImportTemplatePartBuilder) -> None:
        """
         Registers the import template part object 
        """
        pass
    
    ##  Place the builder stage behind the stage before, or in front of the staged model set list if no stage before is given
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="stageBefore"> (@link Stage NXOpen.StageModel.Stage@endlink) </param>
    def ReorderStage(builder: StageBuilder, stageBefore: Stage) -> None:
        """
         Place the builder stage behind the stage before, or in front of the staged model set list if no stage before is given
        """
        pass
    
    ##  Update the name of the Object from the template 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="stageSetName"> (str) </param>
    def SetNameOnPartOperationBuilder(builder: StageBuilder, stageSetName: str) -> None:
        """
         Update the name of the Object from the template 
        """
        pass
    
    ##  Set the @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="createBuilder"> (@link NXOpen.PDM.PartOperationCreateBuilder NXOpen.PDM.PartOperationCreateBuilder@endlink) </param>
    def SetPartOperationCreateBuilder(builder: StageBuilder, createBuilder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
         Set the @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  
        """
        pass
    
import NXOpen
import NXOpen.ModlUtils
import NXOpen.PDM
##  Represents a @link StageModel::StageSetBuilder StageModel::StageSetBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::StageModel::Manager::CreateStageSetBuilder  NXOpen::StageModel::Manager::CreateStageSetBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class StageSetBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>StageModel.StageSetBuilder</ja_class> """


    ## Getter for property: (str) Name
    ##   the stage set name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the stage set name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the stage set name   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the stage set name   
            
         
        """
        pass
    
    ##  Create a managed staged model set with the specified name and number of stages at the specified location
    ##  @return createdStageSet (@link StageSet NXOpen.StageModel.StageSet@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="designPart"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="stageSetName"> (str) </param>
    ## <param name="stageSetLocation"> (str) </param>
    ## <param name="numOfStages"> (int) </param>
    def CreateManagedStageSet(builder: StageSetBuilder, designPart: NXOpen.Part, stageSetName: str, stageSetLocation: str, numOfStages: int) -> StageSet:
        """
         Create a managed staged model set with the specified name and number of stages at the specified location
         @return createdStageSet (@link StageSet NXOpen.StageModel.StageSet@endlink): .
        """
        pass
    
    ##  Create a native staged model set with the specified name and number of stages in the directory of the design part
    ##  @return createdStageSet (@link StageSet NXOpen.StageModel.StageSet@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="designPart"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="stageSetName"> (str) </param>
    ## <param name="numOfStages"> (int) </param>
    def CreateNativeStageSet(builder: StageSetBuilder, designPart: NXOpen.Part, stageSetName: str, numOfStages: int) -> StageSet:
        """
         Create a native staged model set with the specified name and number of stages in the directory of the design part
         @return createdStageSet (@link StageSet NXOpen.StageModel.StageSet@endlink): .
        """
        pass
    
    ##  Edit builder staged model set's name
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="stageSetName"> (str) </param>
    def EditStageSetName(builder: StageSetBuilder, stageSetName: str) -> None:
        """
         Edit builder staged model set's name
        """
        pass
    
    ##  Registers the import template part object 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="templateBuilder"> (@link NXOpen.ModlUtils.ImportTemplatePartBuilder NXOpen.ModlUtils.ImportTemplatePartBuilder@endlink) </param>
    def RegisterImportTemplatePartObject(builder: StageSetBuilder, templateBuilder: NXOpen.ModlUtils.ImportTemplatePartBuilder) -> None:
        """
         Registers the import template part object 
        """
        pass
    
    ##  Registers the import template part object 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="designPart"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def SetDesingPart(builder: StageSetBuilder, designPart: NXOpen.Part) -> None:
        """
         Registers the import template part object 
        """
        pass
    
    ##  Update the name of the Object from the template 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="stageSetName"> (str) </param>
    def SetNameOnPartOperationBuilder(builder: StageSetBuilder, stageSetName: str) -> None:
        """
         Update the name of the Object from the template 
        """
        pass
    
    ##  Set the @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="createBuilder"> (@link NXOpen.PDM.PartOperationCreateBuilder NXOpen.PDM.PartOperationCreateBuilder@endlink) </param>
    def SetPartOperationCreateBuilder(builder: StageSetBuilder, createBuilder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
         Set the @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  
        """
        pass
    
import NXOpen
##  Represents a @link StageModel::StageSet StageModel::StageSet@endlink  object.  <br> To create or edit an instance of this class, use @link NXOpen::StageModel::StageSetBuilder  NXOpen::StageModel::StageSetBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class StageSet(NXOpen.TaggedObject): 
    """ Represents a <ja_class>StageModel.StageSet</ja_class> object. """


    ## Getter for property: (str) Name
    ##   the name of the staged model set   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name of the staged model set   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name of the staged model set   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name of the staged model set   
            
         
        """
        pass
    
    ##  Load and activate the design part of the stage set 
    ##  @return designPart (@link NXOpen.Part NXOpen.Part@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="displayInNewWindow"> (bool) </param>
    def ActivateDesignPart(stageSet: StageSet, displayInNewWindow: bool) -> NXOpen.Part:
        """
         Load and activate the design part of the stage set 
         @return designPart (@link NXOpen.Part NXOpen.Part@endlink): .
        """
        pass
    
    ##  Delete the stages from this staged model set
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="stagesToDelete"> (@link Stage List[NXOpen.StageModel.Stage]@endlink) </param>
    def DeleteStages(stageSet: StageSet, stagesToDelete: List[Stage]) -> None:
        """
         Delete the stages from this staged model set
        """
        pass
    
    ##  Get the stage with the specified name in the staged model set if the stage exists 
    ##  @return stage (@link Stage NXOpen.StageModel.Stage@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="stageName"> (str) </param>
    def GetStageWithName(stageSet: StageSet, stageName: str) -> Stage:
        """
         Get the stage with the specified name in the staged model set if the stage exists 
         @return stage (@link Stage NXOpen.StageModel.Stage@endlink): .
        """
        pass
    
    ##  Get the list of stages in the staged model set 
    ##  @return stages (@link Stage List[NXOpen.StageModel.Stage]@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="includeStockStage"> (bool) </param>
    def GetStages(stageSet: StageSet, includeStockStage: bool) -> List[Stage]:
        """
         Get the list of stages in the staged model set 
         @return stages (@link Stage List[NXOpen.StageModel.Stage]@endlink): .
        """
        pass
    
    ##  Get the stock stage of the stage set 
    ##  @return stockStage (@link Stage NXOpen.StageModel.Stage@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStockStage(stageSet: StageSet) -> Stage:
        """
         Get the stock stage of the stage set 
         @return stockStage (@link Stage NXOpen.StageModel.Stage@endlink): .
        """
        pass
    
    ##  Save as to save an open stage model set as a new stage model set with a new name in native stage model environment. 
    ##  @return newStageSet (@link StageSet NXOpen.StageModel.StageSet@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="name"> (str) </param>
    def NativeSaveAs(stageSet: StageSet, name: str) -> StageSet:
        """
         Save as to save an open stage model set as a new stage model set with a new name in native stage model environment. 
         @return newStageSet (@link StageSet NXOpen.StageModel.StageSet@endlink): .
        """
        pass
    
    ##  Replace the design part of the stage set 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="replacementPart"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def ReplaceDesignPart(stageSet: StageSet, replacementPart: NXOpen.Part) -> None:
        """
         Replace the design part of the stage set 
        """
        pass
    
    ##  Save changes made to the staged model set, including all changes made to its stages 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    @staticmethod
    def SaveStageSet(stageSet: StageSet) -> None:
        """
         Save changes made to the staged model set, including all changes made to its stages 
        """
        pass
    
import NXOpen
##  Represents a @link StageModel::Stage StageModel::Stage@endlink  object. <br> To create or edit an instance of this class, use @link NXOpen::StageModel::StageBuilder  NXOpen::StageModel::StageBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Stage(NXOpen.TaggedObject): 
    """ Represents a <ja_class>StageModel.Stage</ja_class> object."""


    ## Getter for property: (str) Description
    ##   the description of the stage   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the description of the stage   
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the description of the stage   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
          the description of the stage   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name of the stage   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name of the stage   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name of the stage   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name of the stage   
            
         
        """
        pass
    
    ##  Activate the stage 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="displayInNewWindow"> (bool) </param>
    def Activate(stage: Stage, displayInNewWindow: bool) -> None:
        """
         Activate the stage 
        """
        pass
    
    ##  Whether the stage is active or not 
    ##  @return isActive (bool): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def IsActive(stage: Stage) -> bool:
        """
         Whether the stage is active or not 
         @return isActive (bool): .
        """
        pass
    
    ##  Place this stage behind the stage before, or in front of the staged model set list if no stage before is given
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="stageBefore"> (@link Stage NXOpen.StageModel.Stage@endlink) </param>
    def Reorder(stage: Stage, stageBefore: Stage) -> None:
        """
         Place this stage behind the stage before, or in front of the staged model set list if no stage before is given
        """
        pass
    
    ##  Save changes made to the staged model set of this stage, including all changes made to this stage 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    @staticmethod
    def SaveStageSetOfStage(stage: Stage) -> None:
        """
         Save changes made to the staged model set of this stage, including all changes made to this stage 
        """
        pass
    
##  Represents a @link StageModel::Stage StageModel::Stage@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::StageModel::Manager::CreateStandardStockBuilder  NXOpen::StageModel::Manager::CreateStandardStockBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class StandardStockBuilder(StockStageDetailsBuilder): 
    """ Represents a <ja_class>StageModel.Stage</ja_class> builder """
    pass


import NXOpen
import NXOpen.PDM
##  Represents a @link StageModel::StockStageDetailsBuilder StageModel::StockStageDetailsBuilder@endlink . <br> To create a new instance of this class, use @link NXOpen::StageModel::Manager::CreateStockStageDetailsBuilder  NXOpen::StageModel::Manager::CreateStockStageDetailsBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class StockStageDetailsBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>StageModel.StockStageDetailsBuilder</ja_class>."""


    ## Getter for property: (str) StockStageName
    ##   the stage name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def StockStageName(self) -> str:
        """
        Getter for property: (str) StockStageName
          the stage name   
            
         
        """
        pass
    
    ## Setter for property: (str) StockStageName

    ##   the stage name   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @StockStageName.setter
    def StockStageName(self, stageName: str):
        """
        Setter for property: (str) StockStageName
          the stage name   
            
         
        """
        pass
    
    ##  Returns the stage description 
    ##  @return stageDescription (List[str]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def GetStockStageDescription(self) -> List[str]:
        """
         Returns the stage description 
         @return stageDescription (List[str]): .
        """
        pass
    
    ##  Returns @link StageModel::StockStageDetails StageModel::StockStageDetails@endlink  object 
    ##  @return stagedetails (@link StockStageDetails NXOpen.StageModel.StockStageDetails@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def GetStockStageDetails(self) -> StockStageDetails:
        """
         Returns @link StageModel::StockStageDetails StageModel::StockStageDetails@endlink  object 
         @return stagedetails (@link StockStageDetails NXOpen.StageModel.StockStageDetails@endlink): .
        """
        pass
    
    ##  Set the @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="createBuilder"> (@link NXOpen.PDM.PartOperationCreateBuilder NXOpen.PDM.PartOperationCreateBuilder@endlink) </param>
    def SetPartOperationCreateBuilder(builder: StockStageDetailsBuilder, createBuilder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
         Set the @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  
        """
        pass
    
    ##  Sets the stage description 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ##  
    def SetStockStageDescription(self, stageDescription: List[str]) -> None:
        """
         Sets the stage description 
        """
        pass
    
import NXOpen
##  Represents the Stage details class  <br> To create or edit an instance of this class, use @link NXOpen::StageModel::StockStageDetailsBuilder  NXOpen::StageModel::StockStageDetailsBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class StockStageDetails(NXOpen.TaggedObject): 
    """ Represents the Stage details class """
    pass


## @package NXOpen.StageModel
## Classes, Enums and Structs under NXOpen.StageModel namespace

##  @link ObjectUpdateStateManagerStatus NXOpen.StageModel.ObjectUpdateStateManagerStatus @endlink is an alias for @link ObjectUpdateStateManager.Status NXOpen.StageModel.ObjectUpdateStateManager.Status@endlink
ObjectUpdateStateManagerStatus = ObjectUpdateStateManager.Status


##  @link ReplacePartBuilderDesignPartTypes NXOpen.StageModel.ReplacePartBuilderDesignPartTypes @endlink is an alias for @link ReplacePartBuilder.DesignPartTypes NXOpen.StageModel.ReplacePartBuilder.DesignPartTypes@endlink
ReplacePartBuilderDesignPartTypes = ReplacePartBuilder.DesignPartTypes


