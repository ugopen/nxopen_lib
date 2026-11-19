from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
## 
##     Represents a @link NXOpen::Join::AttachedHardware NXOpen::Join::AttachedHardware@endlink  builder.
##      <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateAttachedHardwareBuilder  NXOpen::Join::JoinManager::CreateAttachedHardwareBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class AttachedHardwareBuilder(PointJoinBuilder): 
    """
    Represents a <ja_class>NXOpen.Join.AttachedHardware</ja_class> builder.
    """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) MatingFace
    ##  Returns the selected mating face   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def MatingFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) MatingFace
         Returns the selected mating face   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a attached hardware feature  <br> To create or edit an instance of this class, use @link NXOpen::Join::AttachedHardwareBuilder  NXOpen::Join::AttachedHardwareBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class AttachedHardware(NXOpen.Features.Feature): 
    """ Represents a attached hardware feature """
    pass


import NXOpen
##  Represents a @link NXOpen::Join::AttachmentHardware NXOpen::Join::AttachmentHardware@endlink .
##     
## 
##   <br>  Created in NX2007.0.0  <br> 

class AttachmentHardware(PointJoinHardware): 
    """ Represents a <ja_class>NXOpen.Join.AttachmentHardware</ja_class>.
    """


    ## Getter for property: (str) Alignment
    ##  Returns the alignment of the attachment hardware part.  
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def Alignment(self) -> str:
        """
        Getter for property: (str) Alignment
         Returns the alignment of the attachment hardware part.  
            
         
        """
        pass
    
    ## Setter for property: (str) Alignment

    ##  Returns the alignment of the attachment hardware part.  
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Alignment.setter
    def Alignment(self, alignment: str):
        """
        Setter for property: (str) Alignment
         Returns the alignment of the attachment hardware part.  
            
         
        """
        pass
    
    ##  The bolt points of attachment hardware part
    ##  @return bolts (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetBoltPoint(self) -> List[NXOpen.Point3d]:
        """
         The bolt points of attachment hardware part
         @return bolts (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink): .
        """
        pass
    
    ##  The connections points of attachment hardware part
    ##  @return connections (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetConnectionPoint(self) -> List[NXOpen.Point3d]:
        """
         The connections points of attachment hardware part
         @return connections (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink): .
        """
        pass
    
    ##  The bolt points of attachment hardware part
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="bolts"> (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink) </param>
    def SetBoltPoint(self, bolts: List[NXOpen.Point3d]) -> None:
        """
         The bolt points of attachment hardware part
        """
        pass
    
    ##  The connections points of attachment hardware part
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="connections"> (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink) </param>
    def SetConnectionPoint(self, connections: List[NXOpen.Point3d]) -> None:
        """
         The connections points of attachment hardware part
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Represents a @link NXOpen::Join::AutoPointBuilder NXOpen::Join::AutoPointBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateAutoPointBuilder  NXOpen::Join::JoinManager::CreateAutoPointBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CreateFeaturesOnOk </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## DistanceFromEnds </term> <description> 
##  
## 10.0 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## FaceGapDistance </term> <description> 
##  
## 1.5 (millimeters part), 0.06 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MaximumBendRadius </term> <description> 
##  
## 50 (millimeters part), 2.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MaximumCenterlineWidth </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MaximumSingleThickness </term> <description> 
##  
## 2 (millimeters part), 0.08 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MaximumSpacingBetweenPoints </term> <description> 
##  
## 50 (millimeters part), 2.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MinimumFlangeWidth </term> <description> 
##  
## 6.0 (millimeters part), 0.25 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MinimumNumberPointsOnOverlap </term> <description> 
##  
## 3 </description> </item> 
## 
## <item><term> 
##  
## MinimumSpacingBetweenPoints </term> <description> 
##  
## 25 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MoveReferenceSheetToConstructionLayer </term> <description> 
##  
## True </description> </item> 
## 
## <item><term> 
##  
## OffsetDistanceFromEdge </term> <description> 
##  
## 6.25 (millimeters part), 0.25 (inches part) </description> </item> 
## 
## <item><term> 
##  
## UniformSpacingTolerance </term> <description> 
##  
## 4 (millimeters part), 0.16 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2306.0.0  <br> 

class AutoPointBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Join.AutoPointBuilder</ja_class> builder """


    ##  Settings to indicate whether an interference is near an existing weld point. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoWeldsNearBodies</term><description> 
    ##  Indicates no existing weld points are in this interference area </description> </item><item><term> 
    ## Same</term><description> 
    ##  Indicates weld points exist and part name are the same. </description> </item><item><term> 
    ## Added</term><description> 
    ##  deprecated. </description> </item><item><term> 
    ## Deleted</term><description> 
    ##  deprecated. </description> </item></list>
    class InterferenceDetails(Enum):
        """
        Members Include: <NoWeldsNearBodies> <Same> <Added> <Deleted>
        """
        NoWeldsNearBodies: int
        Same: int
        Added: int
        Deleted: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AutoPointBuilder.InterferenceDetails:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) ComponentsToJoin
    ##  Returns the components that should be joined together.  
    ##    This can be one component, or many.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Assemblies.SelectComponentList
    @property
    def ComponentsToJoin(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) ComponentsToJoin
         Returns the components that should be joined together.  
           This can be one component, or many.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) ComponentsTreatAsUnit
    ##  Returns the components to treat as unit.  
    ##    No features will be created within unit components. Components must be a subset of components to join.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Assemblies.SelectComponentList
    @property
    def ComponentsTreatAsUnit(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) ComponentsTreatAsUnit
         Returns the components to treat as unit.  
           No features will be created within unit components. Components must be a subset of components to join.   
         
        """
        pass
    
    ## Getter for property: (bool) CreateFeaturesOnOk
    ##  Returns the value to indicate if features should be created on ok, or if the Point Join dialog should be launched instead.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def CreateFeaturesOnOk(self) -> bool:
        """
        Getter for property: (bool) CreateFeaturesOnOk
         Returns the value to indicate if features should be created on ok, or if the Point Join dialog should be launched instead.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateFeaturesOnOk

    ##  Returns the value to indicate if features should be created on ok, or if the Point Join dialog should be launched instead.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @CreateFeaturesOnOk.setter
    def CreateFeaturesOnOk(self, create_features_on_ok: bool):
        """
        Setter for property: (bool) CreateFeaturesOnOk
         Returns the value to indicate if features should be created on ok, or if the Point Join dialog should be launched instead.  
             
         
        """
        pass
    
    ## Getter for property: (float) DistanceFromEnds
    ##  Returns the distance from the ends to start creating weld points   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DistanceFromEnds(self) -> float:
        """
        Getter for property: (float) DistanceFromEnds
         Returns the distance from the ends to start creating weld points   
            
         
        """
        pass
    
    ## Setter for property: (float) DistanceFromEnds

    ##  Returns the distance from the ends to start creating weld points   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DistanceFromEnds.setter
    def DistanceFromEnds(self, distanceFromEnds: float):
        """
        Setter for property: (float) DistanceFromEnds
         Returns the distance from the ends to start creating weld points   
            
         
        """
        pass
    
    ## Getter for property: (float) FaceGapDistance
    ##  Returns the face gap distance.  
    ##    This will be used to find interferences between bodies.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def FaceGapDistance(self) -> float:
        """
        Getter for property: (float) FaceGapDistance
         Returns the face gap distance.  
           This will be used to find interferences between bodies.   
         
        """
        pass
    
    ## Setter for property: (float) FaceGapDistance

    ##  Returns the face gap distance.  
    ##    This will be used to find interferences between bodies.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @FaceGapDistance.setter
    def FaceGapDistance(self, faceGapDistance: float):
        """
        Setter for property: (float) FaceGapDistance
         Returns the face gap distance.  
           This will be used to find interferences between bodies.   
         
        """
        pass
    
    ## Getter for property: (float) MaximumBendRadius
    ##  Returns the bend radius of a flange.  
    ##     Points will not be put on faces with a 
    ##             radius smaller than this value.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def MaximumBendRadius(self) -> float:
        """
        Getter for property: (float) MaximumBendRadius
         Returns the bend radius of a flange.  
            Points will not be put on faces with a 
                    radius smaller than this value.   
         
        """
        pass
    
    ## Setter for property: (float) MaximumBendRadius

    ##  Returns the bend radius of a flange.  
    ##     Points will not be put on faces with a 
    ##             radius smaller than this value.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MaximumBendRadius.setter
    def MaximumBendRadius(self, maximumBendRadius: float):
        """
        Setter for property: (float) MaximumBendRadius
         Returns the bend radius of a flange.  
            Points will not be put on faces with a 
                    radius smaller than this value.   
         
        """
        pass
    
    ## Getter for property: (float) MaximumCenterlineWidth
    ##  Returns the maximum centerline width.  
    ##    Points will be created using the centerline method
    ##             if the smallest width is less than this value. If greater, points will be
    ##             created using the offset from edge method.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def MaximumCenterlineWidth(self) -> float:
        """
        Getter for property: (float) MaximumCenterlineWidth
         Returns the maximum centerline width.  
           Points will be created using the centerline method
                    if the smallest width is less than this value. If greater, points will be
                    created using the offset from edge method.   
         
        """
        pass
    
    ## Setter for property: (float) MaximumCenterlineWidth

    ##  Returns the maximum centerline width.  
    ##    Points will be created using the centerline method
    ##             if the smallest width is less than this value. If greater, points will be
    ##             created using the offset from edge method.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MaximumCenterlineWidth.setter
    def MaximumCenterlineWidth(self, maximumCenterlineWidth: float):
        """
        Setter for property: (float) MaximumCenterlineWidth
         Returns the maximum centerline width.  
           Points will be created using the centerline method
                    if the smallest width is less than this value. If greater, points will be
                    created using the offset from edge method.   
         
        """
        pass
    
    ## Getter for property: (float) MaximumSingleThickness
    ##  Returns the maximum single metal thickness for all the selected components.  
    ##   
    ##             If the distance between top faces of two panels (or sheets) is greater
    ##             than single thickness plus face gap distance, a point will not be created
    ##             at that location.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def MaximumSingleThickness(self) -> float:
        """
        Getter for property: (float) MaximumSingleThickness
         Returns the maximum single metal thickness for all the selected components.  
          
                    If the distance between top faces of two panels (or sheets) is greater
                    than single thickness plus face gap distance, a point will not be created
                    at that location.   
         
        """
        pass
    
    ## Setter for property: (float) MaximumSingleThickness

    ##  Returns the maximum single metal thickness for all the selected components.  
    ##   
    ##             If the distance between top faces of two panels (or sheets) is greater
    ##             than single thickness plus face gap distance, a point will not be created
    ##             at that location.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MaximumSingleThickness.setter
    def MaximumSingleThickness(self, maximumSingleThickness: float):
        """
        Setter for property: (float) MaximumSingleThickness
         Returns the maximum single metal thickness for all the selected components.  
          
                    If the distance between top faces of two panels (or sheets) is greater
                    than single thickness plus face gap distance, a point will not be created
                    at that location.   
         
        """
        pass
    
    ## Getter for property: (float) MaximumSpacingBetweenPoints
    ##  Returns the maximum spacing between points   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def MaximumSpacingBetweenPoints(self) -> float:
        """
        Getter for property: (float) MaximumSpacingBetweenPoints
         Returns the maximum spacing between points   
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumSpacingBetweenPoints

    ##  Returns the maximum spacing between points   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MaximumSpacingBetweenPoints.setter
    def MaximumSpacingBetweenPoints(self, maximumSpacingBetweenPoints: float):
        """
        Setter for property: (float) MaximumSpacingBetweenPoints
         Returns the maximum spacing between points   
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumFlangeWidth
    ##  Returns the minimum flange width.  
    ##    If opposite sides of a flange are smaller than
    ##             minimum flange width, it will be ignored.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def MinimumFlangeWidth(self) -> float:
        """
        Getter for property: (float) MinimumFlangeWidth
         Returns the minimum flange width.  
           If opposite sides of a flange are smaller than
                    minimum flange width, it will be ignored.   
         
        """
        pass
    
    ## Setter for property: (float) MinimumFlangeWidth

    ##  Returns the minimum flange width.  
    ##    If opposite sides of a flange are smaller than
    ##             minimum flange width, it will be ignored.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MinimumFlangeWidth.setter
    def MinimumFlangeWidth(self, minimumFlangeWidth: float):
        """
        Setter for property: (float) MinimumFlangeWidth
         Returns the minimum flange width.  
           If opposite sides of a flange are smaller than
                    minimum flange width, it will be ignored.   
         
        """
        pass
    
    ## Getter for property: (int) MinimumNumberPointsOnOverlap
    ##  Returns the mimimum number points to create on an overlap sheet   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return int
    @property
    def MinimumNumberPointsOnOverlap(self) -> int:
        """
        Getter for property: (int) MinimumNumberPointsOnOverlap
         Returns the mimimum number points to create on an overlap sheet   
            
         
        """
        pass
    
    ## Setter for property: (int) MinimumNumberPointsOnOverlap

    ##  Returns the mimimum number points to create on an overlap sheet   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MinimumNumberPointsOnOverlap.setter
    def MinimumNumberPointsOnOverlap(self, minimumNumberPointsOnOverlap: int):
        """
        Setter for property: (int) MinimumNumberPointsOnOverlap
         Returns the mimimum number points to create on an overlap sheet   
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumSpacingBetweenPoints
    ##  Returns the minimum spacing between points   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def MinimumSpacingBetweenPoints(self) -> float:
        """
        Getter for property: (float) MinimumSpacingBetweenPoints
         Returns the minimum spacing between points   
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumSpacingBetweenPoints

    ##  Returns the minimum spacing between points   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MinimumSpacingBetweenPoints.setter
    def MinimumSpacingBetweenPoints(self, minimumSpacingBetweenPoints: float):
        """
        Setter for property: (float) MinimumSpacingBetweenPoints
         Returns the minimum spacing between points   
            
         
        """
        pass
    
    ## Getter for property: (bool) MoveReferenceSheetToConstructionLayer
    ##  Returns the value to indidate if the output sheet bodies of this feature should be moved to the construction layer.  
    ##    Use @link NXOpen::Join::JoinPreferences::SetConstructionLayer NXOpen::Join::JoinPreferences::SetConstructionLayer@endlink  to change the default layer.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def MoveReferenceSheetToConstructionLayer(self) -> bool:
        """
        Getter for property: (bool) MoveReferenceSheetToConstructionLayer
         Returns the value to indidate if the output sheet bodies of this feature should be moved to the construction layer.  
           Use @link NXOpen::Join::JoinPreferences::SetConstructionLayer NXOpen::Join::JoinPreferences::SetConstructionLayer@endlink  to change the default layer.   
         
        """
        pass
    
    ## Setter for property: (bool) MoveReferenceSheetToConstructionLayer

    ##  Returns the value to indidate if the output sheet bodies of this feature should be moved to the construction layer.  
    ##    Use @link NXOpen::Join::JoinPreferences::SetConstructionLayer NXOpen::Join::JoinPreferences::SetConstructionLayer@endlink  to change the default layer.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MoveReferenceSheetToConstructionLayer.setter
    def MoveReferenceSheetToConstructionLayer(self, moveReferenceSheetToConstructionLayer: bool):
        """
        Setter for property: (bool) MoveReferenceSheetToConstructionLayer
         Returns the value to indidate if the output sheet bodies of this feature should be moved to the construction layer.  
           Use @link NXOpen::Join::JoinPreferences::SetConstructionLayer NXOpen::Join::JoinPreferences::SetConstructionLayer@endlink  to change the default layer.   
         
        """
        pass
    
    ## Getter for property: (float) OffsetDistanceFromEdge
    ##  Returns the offset distance from edge   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def OffsetDistanceFromEdge(self) -> float:
        """
        Getter for property: (float) OffsetDistanceFromEdge
         Returns the offset distance from edge   
            
         
        """
        pass
    
    ## Setter for property: (float) OffsetDistanceFromEdge

    ##  Returns the offset distance from edge   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @OffsetDistanceFromEdge.setter
    def OffsetDistanceFromEdge(self, offsetDistanceFromEdge: float):
        """
        Setter for property: (float) OffsetDistanceFromEdge
         Returns the offset distance from edge   
            
         
        """
        pass
    
    ## Getter for property: (str) Subtype
    ##  Returns the Subtype   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def Subtype(self) -> str:
        """
        Getter for property: (str) Subtype
         Returns the Subtype   
            
         
        """
        pass
    
    ## Setter for property: (str) Subtype

    ##  Returns the Subtype   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Subtype.setter
    def Subtype(self, type: str):
        """
        Setter for property: (str) Subtype
         Returns the Subtype   
            
         
        """
        pass
    
    ## Getter for property: (float) UniformSpacingTolerance
    ##  Returns the distance that maximum spacing can be exceeded to achieve uniform spacing   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def UniformSpacingTolerance(self) -> float:
        """
        Getter for property: (float) UniformSpacingTolerance
         Returns the distance that maximum spacing can be exceeded to achieve uniform spacing   
            
         
        """
        pass
    
    ## Setter for property: (float) UniformSpacingTolerance

    ##  Returns the distance that maximum spacing can be exceeded to achieve uniform spacing   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @UniformSpacingTolerance.setter
    def UniformSpacingTolerance(self, uniformSpacingTolerance: float):
        """
        Setter for property: (float) UniformSpacingTolerance
         Returns the distance that maximum spacing can be exceeded to achieve uniform spacing   
            
         
        """
        pass
    
    ##  Ask the connected bodies at a specific point. The point must be from @link NXOpen::Join::AutoPointBuilder::GetPoints NXOpen::Join::AutoPointBuilder::GetPoints@endlink . 
    ##  @return bodies (@link NXOpen.Body List[NXOpen.Body]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="refPoint"> (@link NXOpen.Point NXOpen.Point@endlink) </param>
    def AskConnectedBodiesAtPoint(self, refPoint: NXOpen.Point) -> List[NXOpen.Body]:
        """
         Ask the connected bodies at a specific point. The point must be from @link NXOpen::Join::AutoPointBuilder::GetPoints NXOpen::Join::AutoPointBuilder::GetPoints@endlink . 
         @return bodies (@link NXOpen.Body List[NXOpen.Body]@endlink): .
        """
        pass
    
    ##  Creates a feature set containing weld points for a given interference. 
    ##  @return featureSetTag (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="interferenceIndex"> (int)   Index to the desired interference </param>
    def CreateFeatureSet(self, interferenceIndex: int) -> NXOpen.NXObject:
        """
         Creates a feature set containing weld points for a given interference. 
         @return featureSetTag (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  Returns the number of interference areas between the selected components. This
    ##             method must be invoked or no weld points will be created. The output numInterferences
    ##             variable can be used to get the status of each interference. 
    ##  @return numInterferences (int): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def FindNumberOfInterferenceRegions(self) -> int:
        """
         Returns the number of interference areas between the selected components. This
                    method must be invoked or no weld points will be created. The output numInterferences
                    variable can be used to get the status of each interference. 
         @return numInterferences (int): .
        """
        pass
    
    ##  The status indicating if the interference has existing weld points touching it. The
    ##             index for this function is described in @link NXOpen::Join::AutoPointBuilder::FindNumberOfInterferenceRegions NXOpen::Join::AutoPointBuilder::FindNumberOfInterferenceRegions@endlink . 
    ##  @return interferenceDetails (@link AutoPointBuilder.InterferenceDetails NXOpen.Join.AutoPointBuilder.InterferenceDetails@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="interferenceIndex"> (int)   Index to the desired interference </param>
    def GetInterferenceDetails(self, interferenceIndex: int) -> AutoPointBuilder.InterferenceDetails:
        """
         The status indicating if the interference has existing weld points touching it. The
                    index for this function is described in @link NXOpen::Join::AutoPointBuilder::FindNumberOfInterferenceRegions NXOpen::Join::AutoPointBuilder::FindNumberOfInterferenceRegions@endlink . 
         @return interferenceDetails (@link AutoPointBuilder.InterferenceDetails NXOpen.Join.AutoPointBuilder.InterferenceDetails@endlink): .
        """
        pass
    
    ##  Output reference points for which features have not been created. 
    ##  @return points (@link NXOpen.Point List[NXOpen.Point]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetPoints(self) -> List[NXOpen.Point]:
        """
         Output reference points for which features have not been created. 
         @return points (@link NXOpen.Point List[NXOpen.Point]@endlink): .
        """
        pass
    
    ##  Indicates the display mode. The created feature output can be shown as a solid or point. 
    ##  @return showSolids (bool): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetShowSolids(self) -> bool:
        """
         Indicates the display mode. The created feature output can be shown as a solid or point. 
         @return showSolids (bool): .
        """
        pass
    
    ##  Indicates whether the output point should show thru on creation 
    ##  @return showThruState (bool): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetShowThruState(self) -> bool:
        """
         Indicates whether the output point should show thru on creation 
         @return showThruState (bool): .
        """
        pass
    
    ##  Visible bodies from the selected components. 
    ##  @return bodies (@link NXOpen.Body List[NXOpen.Body]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetVisibleBodies(self) -> List[NXOpen.Body]:
        """
         Visible bodies from the selected components. 
         @return bodies (@link NXOpen.Body List[NXOpen.Body]@endlink): .
        """
        pass
    
    ##  Indicates the display mode. The created feature output can be shown as a solid or point. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="showSolids"> (bool) </param>
    def SetShowSolids(self, showSolids: bool) -> None:
        """
         Indicates the display mode. The created feature output can be shown as a solid or point. 
        """
        pass
    
    ##  Indicates whether the output point should show thru on creation 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="showThruState"> (bool) </param>
    def SetShowThruState(self, showThruState: bool) -> None:
        """
         Indicates whether the output point should show thru on creation 
        """
        pass
    
import NXOpen.Features
## 
##     Represents a @link NXOpen::Join::CompoundJoinWeld NXOpen::Join::CompoundJoinWeld@endlink  builder.
##      <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateCompoundJoinWeldBuilder  NXOpen::Join::JoinManager::CreateCompoundJoinWeldBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Staggered </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2212.0.0  <br> 

class CompoundJoinWeldBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a <ja_class>NXOpen.Join.CompoundJoinWeld</ja_class> builder.
    """


    ## Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) ArrowSideJoinWelds
    ##  Returns the join weld features defining the arrow side of the compound join weld.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Features.SelectFeatureList
    @property
    def ArrowSideJoinWelds(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) ArrowSideJoinWelds
         Returns the join weld features defining the arrow side of the compound join weld.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) OtherSideJoinWelds
    ##  Returns the join weld features defining the other side of the compound join weld.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Features.SelectFeatureList
    @property
    def OtherSideJoinWelds(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) OtherSideJoinWelds
         Returns the join weld features defining the other side of the compound join weld.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Staggered
    ##  Returns the value to control if the weld symbol created from this compound weld should have the staggered indication.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def Staggered(self) -> bool:
        """
        Getter for property: (bool) Staggered
         Returns the value to control if the weld symbol created from this compound weld should have the staggered indication.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Staggered

    ##  Returns the value to control if the weld symbol created from this compound weld should have the staggered indication.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Staggered.setter
    def Staggered(self, bStaggered: bool):
        """
        Setter for property: (bool) Staggered
         Returns the value to control if the weld symbol created from this compound weld should have the staggered indication.  
             
         
        """
        pass
    
import NXOpen.Features
##  Represents a compound join weld feature.  <br> To create or edit an instance of this class, use @link NXOpen::Join::CompoundJoinWeldBuilder  NXOpen::Join::CompoundJoinWeldBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class CompoundJoinWeld(NXOpen.Features.Feature): 
    """ Represents a compound join weld feature. """


    ##  Get the join feature tags, if any, from the arrow side of a compound join weld feature.
    ##  @return arrowSideWelds (@link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetArrowSideWelds(self) -> List[NXOpen.Features.Feature]:
        """
         Get the join feature tags, if any, from the arrow side of a compound join weld feature.
         @return arrowSideWelds (@link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink): .
        """
        pass
    
    ##  Get the weld feature tags, if any, from the Other Side of a weld feature. 
    ##  @return otherSideWelds (@link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetOtherSideWelds(self) -> List[NXOpen.Features.Feature]:
        """
         Get the weld feature tags, if any, from the Other Side of a weld feature. 
         @return otherSideWelds (@link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink): .
        """
        pass
    
    ##  Get a list of @link NXOpen::Join::CompoundJoinWeld NXOpen::Join::CompoundJoinWeld@endlink  from a compound join weld feature.
    ##  @return compoundJoinWeldFeatures (@link CompoundJoinWeld List[NXOpen.Join.CompoundJoinWeld]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetOwningCompoundWelds(self) -> List[CompoundJoinWeld]:
        """
         Get a list of @link NXOpen::Join::CompoundJoinWeld NXOpen::Join::CompoundJoinWeld@endlink  from a compound join weld feature.
         @return compoundJoinWeldFeatures (@link CompoundJoinWeld List[NXOpen.Join.CompoundJoinWeld]@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a @link NXOpen::Join::CurveJoin NXOpen::Join::CurveJoin@endlink  builder.
##      <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateCurveJoinBuilder  NXOpen::Join::JoinManager::CreateCurveJoinBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class CurveJoinBuilder(JoinBuilder): 
    """
    Represents a <ja_class>NXOpen.Join.CurveJoin</ja_class> builder.
    """


    ##  the output body type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  Do not output a body. </description> </item><item><term> 
    ## Solid</term><description> 
    ##  Output solid body. </description> </item><item><term> 
    ## Sheet</term><description> 
    ##  Output sheet body. </description> </item></list>
    class BodyType(Enum):
        """
        Members Include: <NotSet> <Solid> <Sheet>
        """
        NotSet: int
        Solid: int
        Sheet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.BodyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  setting to used when creating a plug weld if two or three connected parts are used. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Two</term><description> 
    ##  Two connected parts were used to define the plug weld. </description> </item><item><term> 
    ## Three</term><description> 
    ##  Three connected parts were used to define the plug weld. </description> </item></list>
    class ConnectedPartsType(Enum):
        """
        Members Include: <Two> <Three>
        """
        Two: int
        Three: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.ConnectedPartsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the profile contour type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  straight line </description> </item><item><term> 
    ## Flush</term><description> 
    ##  straight line </description> </item><item><term> 
    ## Concave</term><description> 
    ##  concave corner shape </description> </item><item><term> 
    ## Convex</term><description> 
    ##  convex corner shape </description> </item></list>
    class ContourType(Enum):
        """
        Members Include: <NotSet> <Flush> <Concave> <Convex>
        """
        NotSet: int
        Flush: int
        Concave: int
        Convex: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.ContourType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The edge preparation method used when @link NXOpen::Join::CurveJoinBuilder::ShapeType NXOpen::Join::CurveJoinBuilder::ShapeType@endlink  is set to @link NXOpen::Join::CurveJoinBuilder::ShapeTypeSquareButt NXOpen::Join::CurveJoinBuilder::ShapeTypeSquareButt@endlink ,
    ##             @link NXOpen::Join::CurveJoinBuilder::ShapeTypeVGroove NXOpen::Join::CurveJoinBuilder::ShapeTypeVGroove@endlink , @link NXOpen::Join::CurveJoinBuilder::ShapeTypeBevelGroove NXOpen::Join::CurveJoinBuilder::ShapeTypeBevelGroove@endlink ,
    ##             @link NXOpen::Join::CurveJoinBuilder::ShapeTypeUGroove NXOpen::Join::CurveJoinBuilder::ShapeTypeUGroove@endlink , @link NXOpen::Join::CurveJoinBuilder::ShapeTypeJGroove NXOpen::Join::CurveJoinBuilder::ShapeTypeJGroove@endlink ,
    ##             @link NXOpen::Join::CurveJoinBuilder::ShapeTypeButtJoint NXOpen::Join::CurveJoinBuilder::ShapeTypeButtJoint@endlink , @link NXOpen::Join::CurveJoinBuilder::ShapeTypeTJoint NXOpen::Join::CurveJoinBuilder::ShapeTypeTJoint@endlink  or
    ##             @link NXOpen::Join::CurveJoinBuilder::ShapeTypeCornerJoint NXOpen::Join::CurveJoinBuilder::ShapeTypeCornerJoint@endlink  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## EntireLength</term><description> 
    ##  Entire length of solid will be modified. </description> </item><item><term> 
    ## Limits</term><description> 
    ##  Only portion of solid within the specified limits will be modified. </description> </item></list>
    class EdgePrepType(Enum):
        """
        Members Include: <EntireLength> <Limits>
        """
        EntireLength: int
        Limits: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.EdgePrepType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  setting to be used with Fillet Weld to specify on what face sets slots need to be filled. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  No filling of face slots is requested. </description> </item><item><term> 
    ## Set1</term><description> 
    ##  Slots should be filled only on Face Set 1 faces. </description> </item><item><term> 
    ## Set2</term><description> 
    ##  Slots should be filled only on Face Set 2 faces. </description> </item><item><term> 
    ## Both</term><description> 
    ##  Slots should be filled on both Face Sets' faces. </description> </item></list>
    class FillFaceSlotsOnSetType(Enum):
        """
        Members Include: <NotSet> <Set1> <Set2> <Both>
        """
        NotSet: int
        Set1: int
        Set2: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.FillFaceSlotsOnSetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the lap joint fillet location 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Both</term><description> 
    ##  Fillets will be created on both sides of lap solids. </description> </item><item><term> 
    ## PlacementEdge</term><description> 
    ##  Fillet will be created along the placement edges only. </description> </item></list>
    class LapFilletLocationOption(Enum):
        """
        Members Include: <Both> <PlacementEdge>
        """
        Both: int
        PlacementEdge: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.LapFilletLocationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the profile type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Sketch</term><description> 
    ##  Use sketch to define profile shape. </description> </item><item><term> 
    ## Tube</term><description> 
    ##  Create tube along the path.         </description> </item><item><term> 
    ## Ellipse</term><description> 
    ##  Create ellipse along the path.      </description> </item><item><term> 
    ## Rectangle</term><description> 
    ##  Create rectangle along the path.    </description> </item><item><term> 
    ## FillCorner</term><description> 
    ##  Fill corner between face sets.      </description> </item><item><term> 
    ## SquareButt</term><description> 
    ##  Square Butt Groove profile shape.   </description> </item><item><term> 
    ## VGroove</term><description> 
    ##  V Groove profile shape.             </description> </item><item><term> 
    ## BevelGroove</term><description> 
    ##  Bevel Groove profile shape.         </description> </item><item><term> 
    ## UGroove</term><description> 
    ##  U Groove profile shape.             </description> </item><item><term> 
    ## JGroove</term><description> 
    ##  J Groove profile shape.             </description> </item><item><term> 
    ## FlareVGroove</term><description> 
    ##  Flare V Groove profile shape.       </description> </item><item><term> 
    ## FlareBevelGroove</term><description> 
    ##  Flare Bevel Groove profile shape.   </description> </item><item><term> 
    ## ButtJoint</term><description> 
    ##  Butt joint defintion.               </description> </item><item><term> 
    ## Plug</term><description> 
    ##  Plug shape to fill a hole.          </description> </item><item><term> 
    ## TJoint</term><description> 
    ##  T-joint definition.                 </description> </item><item><term> 
    ## CornerJoint</term><description> 
    ##  Corner joint definition.            </description> </item><item><term> 
    ## LapJoint</term><description> 
    ##  Lap joint definition.               </description> </item></list>
    class ShapeType(Enum):
        """
        Members Include: <Sketch> <Tube> <Ellipse> <Rectangle> <FillCorner> <SquareButt> <VGroove> <BevelGroove> <UGroove> <JGroove> <FlareVGroove> <FlareBevelGroove> <ButtJoint> <Plug> <TJoint> <CornerJoint> <LapJoint>
        """
        Sketch: int
        Tube: int
        Ellipse: int
        Rectangle: int
        FillCorner: int
        SquareButt: int
        VGroove: int
        BevelGroove: int
        UGroove: int
        JGroove: int
        FlareVGroove: int
        FlareBevelGroove: int
        ButtJoint: int
        Plug: int
        TJoint: int
        CornerJoint: int
        LapJoint: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.ShapeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the profile type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NumberLength</term><description> 
    ## </description> </item><item><term> 
    ## PitchLength</term><description> 
    ## </description> </item></list>
    class SkipFeatureType(Enum):
        """
        Members Include: <NumberLength> <PitchLength>
        """
        NumberLength: int
        PitchLength: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.SkipFeatureType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the taper method for Groove 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FromTop</term><description> 
    ##  Taper will be measured from groove side face </description> </item><item><term> 
    ## FromEnd</term><description> 
    ##  Taper will be measured from groove end caps  </description> </item></list>
    class TaperType(Enum):
        """
        Members Include: <FromTop> <FromEnd>
        """
        FromTop: int
        FromEnd: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.TaperType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AlignFilletToPartEdge
    ##  Returns the flush creation flag for fillet.  
    ##    If true, fillet solid will be aligned with the part edge.   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def AlignFilletToPartEdge(self) -> bool:
        """
        Getter for property: (bool) AlignFilletToPartEdge
         Returns the flush creation flag for fillet.  
           If true, fillet solid will be aligned with the part edge.   
         
        """
        pass
    
    ## Setter for property: (bool) AlignFilletToPartEdge

    ##  Returns the flush creation flag for fillet.  
    ##    If true, fillet solid will be aligned with the part edge.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @AlignFilletToPartEdge.setter
    def AlignFilletToPartEdge(self, status: bool):
        """
        Setter for property: (bool) AlignFilletToPartEdge
         Returns the flush creation flag for fillet.  
           If true, fillet solid will be aligned with the part edge.   
         
        """
        pass
    
    ## Getter for property: (bool) AlignGrooveToPartEdge
    ##  Returns the flush creation flag.  
    ##    If true, groove solid will be extended to the part edge and then trimmed.   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def AlignGrooveToPartEdge(self) -> bool:
        """
        Getter for property: (bool) AlignGrooveToPartEdge
         Returns the flush creation flag.  
           If true, groove solid will be extended to the part edge and then trimmed.   
         
        """
        pass
    
    ## Setter for property: (bool) AlignGrooveToPartEdge

    ##  Returns the flush creation flag.  
    ##    If true, groove solid will be extended to the part edge and then trimmed.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @AlignGrooveToPartEdge.setter
    def AlignGrooveToPartEdge(self, status: bool):
        """
        Setter for property: (bool) AlignGrooveToPartEdge
         Returns the flush creation flag.  
           If true, groove solid will be extended to the part edge and then trimmed.   
         
        """
        pass
    
    ## Getter for property: (int) BodyColor
    ##  Returns the path body color value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def BodyColor(self) -> int:
        """
        Getter for property: (int) BodyColor
         Returns the path body color value   
            
         
        """
        pass
    
    ## Setter for property: (int) BodyColor

    ##  Returns the path body color value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @BodyColor.setter
    def BodyColor(self, bodyColor: int):
        """
        Setter for property: (int) BodyColor
         Returns the path body color value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CalculatedPitch
    ##  Returns the computed pitch when when @link NXOpen::Join::CurveJoinBuilder::SkipFeatureType NXOpen::Join::CurveJoinBuilder::SkipFeatureType@endlink  is @link  NXOpen::Join::CurveJoinBuilder::SkipFeatureTypePitchLength   NXOpen::Join::CurveJoinBuilder::SkipFeatureTypePitchLength @endlink    
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def CalculatedPitch(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CalculatedPitch
         Returns the computed pitch when when @link NXOpen::Join::CurveJoinBuilder::SkipFeatureType NXOpen::Join::CurveJoinBuilder::SkipFeatureType@endlink  is @link  NXOpen::Join::CurveJoinBuilder::SkipFeatureTypePitchLength   NXOpen::Join::CurveJoinBuilder::SkipFeatureTypePitchLength @endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link CurveJoinBuilder.ConnectedPartsType NXOpen.Join.CurveJoinBuilder.ConnectedPartsType@endlink) ConnectionType
    ##  Returns the plug weld connection value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return CurveJoinBuilder.ConnectedPartsType
    @property
    def ConnectionType(self) -> CurveJoinBuilder.ConnectedPartsType:
        """
        Getter for property: (@link CurveJoinBuilder.ConnectedPartsType NXOpen.Join.CurveJoinBuilder.ConnectedPartsType@endlink) ConnectionType
         Returns the plug weld connection value   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveJoinBuilder.ConnectedPartsType NXOpen.Join.CurveJoinBuilder.ConnectedPartsType@endlink) ConnectionType

    ##  Returns the plug weld connection value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ConnectionType.setter
    def ConnectionType(self, connectedPartsType: CurveJoinBuilder.ConnectedPartsType):
        """
        Setter for property: (@link CurveJoinBuilder.ConnectedPartsType NXOpen.Join.CurveJoinBuilder.ConnectedPartsType@endlink) ConnectionType
         Returns the plug weld connection value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ContourHeight
    ##  Returns the contour height   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ContourHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ContourHeight
         Returns the contour height   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateSkipFeatures
    ##  Returns the flag to indicate if skip features should be created.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def CreateSkipFeatures(self) -> bool:
        """
        Getter for property: (bool) CreateSkipFeatures
         Returns the flag to indicate if skip features should be created.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateSkipFeatures

    ##  Returns the flag to indicate if skip features should be created.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CreateSkipFeatures.setter
    def CreateSkipFeatures(self, createSkipFeatures: bool):
        """
        Setter for property: (bool) CreateSkipFeatures
         Returns the flag to indicate if skip features should be created.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateSolid
    ##  Returns the solid creation status.  
    ##    If true, soild should be created in connected bodies. If false, no solid would be generated.   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateSolid(self) -> bool:
        """
        Getter for property: (bool) CreateSolid
         Returns the solid creation status.  
           If true, soild should be created in connected bodies. If false, no solid would be generated.   
         
        """
        pass
    
    ## Setter for property: (bool) CreateSolid

    ##  Returns the solid creation status.  
    ##    If true, soild should be created in connected bodies. If false, no solid would be generated.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateSolid.setter
    def CreateSolid(self, status: bool):
        """
        Setter for property: (bool) CreateSolid
         Returns the solid creation status.  
           If true, soild should be created in connected bodies. If false, no solid would be generated.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) CurveSelSection
    ##  Returns the selected curve section   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def CurveSelSection(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) CurveSelSection
         Returns the selected curve section   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveJoinBuilder.EdgePrepType NXOpen.Join.CurveJoinBuilder.EdgePrepType@endlink) EdgePrepMethod
    ##  Returns the edge preparation method value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return CurveJoinBuilder.EdgePrepType
    @property
    def EdgePrepMethod(self) -> CurveJoinBuilder.EdgePrepType:
        """
        Getter for property: (@link CurveJoinBuilder.EdgePrepType NXOpen.Join.CurveJoinBuilder.EdgePrepType@endlink) EdgePrepMethod
         Returns the edge preparation method value   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveJoinBuilder.EdgePrepType NXOpen.Join.CurveJoinBuilder.EdgePrepType@endlink) EdgePrepMethod

    ##  Returns the edge preparation method value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @EdgePrepMethod.setter
    def EdgePrepMethod(self, edgePrepMethod: CurveJoinBuilder.EdgePrepType):
        """
        Setter for property: (@link CurveJoinBuilder.EdgePrepType NXOpen.Join.CurveJoinBuilder.EdgePrepType@endlink) EdgePrepMethod
         Returns the edge preparation method value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) EdgeSection1
    ##  Returns the primary selected edges   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def EdgeSection1(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) EdgeSection1
         Returns the primary selected edges   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) EdgeSection2
    ##  Returns the secondary selected edges   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def EdgeSection2(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) EdgeSection2
         Returns the secondary selected edges   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EllipseSemiMajorAxis
    ##  Returns the ellipse semi-major axis   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EllipseSemiMajorAxis(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EllipseSemiMajorAxis
         Returns the ellipse semi-major axis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EllipseSemiMinorAxis
    ##  Returns the ellipse semi-minor axis   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EllipseSemiMinorAxis(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EllipseSemiMinorAxis
         Returns the ellipse semi-minor axis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) EndDistance
    ##  Returns the end distance used to limit the length of the output curve  
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.OnPathDimensionBuilder
    @property
    def EndDistance(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) EndDistance
         Returns the end distance used to limit the length of the output curve  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndTaperAngle
    ##  Returns the groove end taper angle   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EndTaperAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndTaperAngle
         Returns the groove end taper angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExtensionDistance1
    ##  Returns the primary extension distance   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ExtensionDistance1(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExtensionDistance1
         Returns the primary extension distance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExtensionDistance2
    ##  Returns the secondary extension distance   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ExtensionDistance2(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExtensionDistance2
         Returns the secondary extension distance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector1
    ##  Returns the primary selected faces   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceCollector1(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector1
         Returns the primary selected faces   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector2
    ##  Returns the secondary selected faces   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceCollector2(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector2
         Returns the secondary selected faces   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector3
    ##  Returns the third selected faces   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceCollector3(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector3
         Returns the third selected faces   
            
         
        """
        pass
    
    ## Getter for property: (bool) FillFaceHoles
    ##  Returns the face hole fill status.  
    ##    If true, holes in faces should be filled. If false, then no hole filling will happen.   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def FillFaceHoles(self) -> bool:
        """
        Getter for property: (bool) FillFaceHoles
         Returns the face hole fill status.  
           If true, holes in faces should be filled. If false, then no hole filling will happen.   
         
        """
        pass
    
    ## Setter for property: (bool) FillFaceHoles

    ##  Returns the face hole fill status.  
    ##    If true, holes in faces should be filled. If false, then no hole filling will happen.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FillFaceHoles.setter
    def FillFaceHoles(self, status: bool):
        """
        Setter for property: (bool) FillFaceHoles
         Returns the face hole fill status.  
           If true, holes in faces should be filled. If false, then no hole filling will happen.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FillFaceSlotsGap
    ##  Returns the fillet weld fill face slot gap value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FillFaceSlotsGap(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FillFaceSlotsGap
         Returns the fillet weld fill face slot gap value   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveJoinBuilder.FillFaceSlotsOnSetType NXOpen.Join.CurveJoinBuilder.FillFaceSlotsOnSetType@endlink) FillFaceSlotsOnSet
    ##  Returns the fillet weld fill face slots value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return CurveJoinBuilder.FillFaceSlotsOnSetType
    @property
    def FillFaceSlotsOnSet(self) -> CurveJoinBuilder.FillFaceSlotsOnSetType:
        """
        Getter for property: (@link CurveJoinBuilder.FillFaceSlotsOnSetType NXOpen.Join.CurveJoinBuilder.FillFaceSlotsOnSetType@endlink) FillFaceSlotsOnSet
         Returns the fillet weld fill face slots value   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveJoinBuilder.FillFaceSlotsOnSetType NXOpen.Join.CurveJoinBuilder.FillFaceSlotsOnSetType@endlink) FillFaceSlotsOnSet

    ##  Returns the fillet weld fill face slots value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @FillFaceSlotsOnSet.setter
    def FillFaceSlotsOnSet(self, fillFaceSlotsOnSetType: CurveJoinBuilder.FillFaceSlotsOnSetType):
        """
        Setter for property: (@link CurveJoinBuilder.FillFaceSlotsOnSetType NXOpen.Join.CurveJoinBuilder.FillFaceSlotsOnSetType@endlink) FillFaceSlotsOnSet
         Returns the fillet weld fill face slots value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) GrooveAngle
    ##  Returns the angle of groove   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def GrooveAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) GrooveAngle
         Returns the angle of groove   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) GrooveDepth
    ##  Returns the depth for groove   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def GrooveDepth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) GrooveDepth
         Returns the depth for groove   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) GrooveRadius
    ##  Returns the radius of groove   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def GrooveRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) GrooveRadius
         Returns the radius of groove   
            
         
        """
        pass
    
    ## Getter for property: (bool) InferFaceInfoFromSelection
    ##  Returns the flag to indicate if face related fields should be populated based on curve selection.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def InferFaceInfoFromSelection(self) -> bool:
        """
        Getter for property: (bool) InferFaceInfoFromSelection
         Returns the flag to indicate if face related fields should be populated based on curve selection.  
             
         
        """
        pass
    
    ## Setter for property: (bool) InferFaceInfoFromSelection

    ##  Returns the flag to indicate if face related fields should be populated based on curve selection.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @InferFaceInfoFromSelection.setter
    def InferFaceInfoFromSelection(self, inferFaceInfoFromSelection: bool):
        """
        Setter for property: (bool) InferFaceInfoFromSelection
         Returns the flag to indicate if face related fields should be populated based on curve selection.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) JointMarkFace
    ##  Returns the face for joint mark placement   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def JointMarkFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) JointMarkFace
         Returns the face for joint mark placement   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) JointMarkSize
    ##  Returns the joint mark size   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def JointMarkSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) JointMarkSize
         Returns the joint mark size   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveJoinBuilder.LapFilletLocationOption NXOpen.Join.CurveJoinBuilder.LapFilletLocationOption@endlink) LapFilletLocation
    ##  Returns the lap fillet location   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return CurveJoinBuilder.LapFilletLocationOption
    @property
    def LapFilletLocation(self) -> CurveJoinBuilder.LapFilletLocationOption:
        """
        Getter for property: (@link CurveJoinBuilder.LapFilletLocationOption NXOpen.Join.CurveJoinBuilder.LapFilletLocationOption@endlink) LapFilletLocation
         Returns the lap fillet location   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveJoinBuilder.LapFilletLocationOption NXOpen.Join.CurveJoinBuilder.LapFilletLocationOption@endlink) LapFilletLocation

    ##  Returns the lap fillet location   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @LapFilletLocation.setter
    def LapFilletLocation(self, location: CurveJoinBuilder.LapFilletLocationOption):
        """
        Setter for property: (@link CurveJoinBuilder.LapFilletLocationOption NXOpen.Join.CurveJoinBuilder.LapFilletLocationOption@endlink) LapFilletLocation
         Returns the lap fillet location   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumPitch
    ##  Returns the minimum desired pitch between skip features.  
    ##    Only used when @link NXOpen::Join::CurveJoinBuilder::SkipFeatureType NXOpen::Join::CurveJoinBuilder::SkipFeatureType@endlink  is @link  NXOpen::Join::CurveJoinBuilder::SkipFeatureTypePitchLength   NXOpen::Join::CurveJoinBuilder::SkipFeatureTypePitchLength @endlink    
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinimumPitch(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumPitch
         Returns the minimum desired pitch between skip features.  
           Only used when @link NXOpen::Join::CurveJoinBuilder::SkipFeatureType NXOpen::Join::CurveJoinBuilder::SkipFeatureType@endlink  is @link  NXOpen::Join::CurveJoinBuilder::SkipFeatureTypePitchLength   NXOpen::Join::CurveJoinBuilder::SkipFeatureTypePitchLength @endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NumberOfSkips
    ##  Returns the number of skip features to create.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def NumberOfSkips(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NumberOfSkips
         Returns the number of skip features to create.  
             
         
        """
        pass
    
    ## Getter for property: (@link CurveJoinBuilder.BodyType NXOpen.Join.CurveJoinBuilder.BodyType@endlink) PathSolidBodyType
    ##  Returns the path solid body type to output   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return CurveJoinBuilder.BodyType
    @property
    def PathSolidBodyType(self) -> CurveJoinBuilder.BodyType:
        """
        Getter for property: (@link CurveJoinBuilder.BodyType NXOpen.Join.CurveJoinBuilder.BodyType@endlink) PathSolidBodyType
         Returns the path solid body type to output   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveJoinBuilder.BodyType NXOpen.Join.CurveJoinBuilder.BodyType@endlink) PathSolidBodyType

    ##  Returns the path solid body type to output   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @PathSolidBodyType.setter
    def PathSolidBodyType(self, bodyType: CurveJoinBuilder.BodyType):
        """
        Setter for property: (@link CurveJoinBuilder.BodyType NXOpen.Join.CurveJoinBuilder.BodyType@endlink) PathSolidBodyType
         Returns the path solid body type to output   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Face NXOpen.Face@endlink) PickFace1
    ##  Returns the pick face associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector1 NXOpen::Join::CurveJoinBuilder::FaceCollector1@endlink    
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Face
    @property
    def PickFace1(self) -> NXOpen.Face:
        """
        Getter for property: (@link NXOpen.Face NXOpen.Face@endlink) PickFace1
         Returns the pick face associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector1 NXOpen::Join::CurveJoinBuilder::FaceCollector1@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Face NXOpen.Face@endlink) PickFace1

    ##  Returns the pick face associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector1 NXOpen::Join::CurveJoinBuilder::FaceCollector1@endlink    
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @PickFace1.setter
    def PickFace1(self, pickFace1: NXOpen.Face):
        """
        Setter for property: (@link NXOpen.Face NXOpen.Face@endlink) PickFace1
         Returns the pick face associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector1 NXOpen::Join::CurveJoinBuilder::FaceCollector1@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Face NXOpen.Face@endlink) PickFace2
    ##  Returns the pick face associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector2 NXOpen::Join::CurveJoinBuilder::FaceCollector2@endlink    
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Face
    @property
    def PickFace2(self) -> NXOpen.Face:
        """
        Getter for property: (@link NXOpen.Face NXOpen.Face@endlink) PickFace2
         Returns the pick face associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector2 NXOpen::Join::CurveJoinBuilder::FaceCollector2@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Face NXOpen.Face@endlink) PickFace2

    ##  Returns the pick face associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector2 NXOpen::Join::CurveJoinBuilder::FaceCollector2@endlink    
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @PickFace2.setter
    def PickFace2(self, pickFace2: NXOpen.Face):
        """
        Setter for property: (@link NXOpen.Face NXOpen.Face@endlink) PickFace2
         Returns the pick face associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector2 NXOpen::Join::CurveJoinBuilder::FaceCollector2@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPoint1
    ##  Returns the pick point associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector1 NXOpen::Join::CurveJoinBuilder::FaceCollector1@endlink    
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def PickPoint1(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPoint1
         Returns the pick point associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector1 NXOpen::Join::CurveJoinBuilder::FaceCollector1@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPoint1

    ##  Returns the pick point associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector1 NXOpen::Join::CurveJoinBuilder::FaceCollector1@endlink    
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @PickPoint1.setter
    def PickPoint1(self, pickPoint1: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPoint1
         Returns the pick point associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector1 NXOpen::Join::CurveJoinBuilder::FaceCollector1@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPoint2
    ##  Returns the pick point associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector2 NXOpen::Join::CurveJoinBuilder::FaceCollector2@endlink    
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def PickPoint2(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPoint2
         Returns the pick point associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector2 NXOpen::Join::CurveJoinBuilder::FaceCollector2@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPoint2

    ##  Returns the pick point associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector2 NXOpen::Join::CurveJoinBuilder::FaceCollector2@endlink    
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @PickPoint2.setter
    def PickPoint2(self, pickPoint2: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPoint2
         Returns the pick point associated with @link NXOpen::Join::CurveJoinBuilder::FaceCollector2 NXOpen::Join::CurveJoinBuilder::FaceCollector2@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link CurveJoinBuilder.ContourType NXOpen.Join.CurveJoinBuilder.ContourType@endlink) ProfileContourType
    ##  Returns the profile contour type value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return CurveJoinBuilder.ContourType
    @property
    def ProfileContourType(self) -> CurveJoinBuilder.ContourType:
        """
        Getter for property: (@link CurveJoinBuilder.ContourType NXOpen.Join.CurveJoinBuilder.ContourType@endlink) ProfileContourType
         Returns the profile contour type value   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveJoinBuilder.ContourType NXOpen.Join.CurveJoinBuilder.ContourType@endlink) ProfileContourType

    ##  Returns the profile contour type value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ProfileContourType.setter
    def ProfileContourType(self, contourType: CurveJoinBuilder.ContourType):
        """
        Setter for property: (@link CurveJoinBuilder.ContourType NXOpen.Join.CurveJoinBuilder.ContourType@endlink) ProfileContourType
         Returns the profile contour type value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProfileDiameter
    ##  Returns the profile diameter   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ProfileDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProfileDiameter
         Returns the profile diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProfileDimension1
    ##  Returns the profile first dimension   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ProfileDimension1(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProfileDimension1
         Returns the profile first dimension   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProfileDimension2
    ##  Returns the profile second dimension   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ProfileDimension2(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProfileDimension2
         Returns the profile second dimension   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveJoinBuilder.ShapeType NXOpen.Join.CurveJoinBuilder.ShapeType@endlink) ProfileType
    ##  Returns the profile type value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return CurveJoinBuilder.ShapeType
    @property
    def ProfileType(self) -> CurveJoinBuilder.ShapeType:
        """
        Getter for property: (@link CurveJoinBuilder.ShapeType NXOpen.Join.CurveJoinBuilder.ShapeType@endlink) ProfileType
         Returns the profile type value   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveJoinBuilder.ShapeType NXOpen.Join.CurveJoinBuilder.ShapeType@endlink) ProfileType

    ##  Returns the profile type value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ProfileType.setter
    def ProfileType(self, profileType: CurveJoinBuilder.ShapeType):
        """
        Setter for property: (@link CurveJoinBuilder.ShapeType NXOpen.Join.CurveJoinBuilder.ShapeType@endlink) ProfileType
         Returns the profile type value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RectangleBase
    ##  Returns the rectangle base   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RectangleBase(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RectangleBase
         Returns the rectangle base   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RectangleHeight
    ##  Returns the rectangle height   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RectangleHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RectangleHeight
         Returns the rectangle height   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RootDepth
    ##  Returns the root depth for groove   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RootDepth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RootDepth
         Returns the root depth for groove   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RootOpening
    ##  Returns the root opening for groove   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RootOpening(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RootOpening
         Returns the root opening for groove   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SegmentLength
    ##  Returns the segment length for each skip feature.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SegmentLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SegmentLength
         Returns the segment length for each skip feature.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SketchSection
    ##  Returns the sketch profile's section   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def SketchSection(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SketchSection
         Returns the sketch profile's section   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveJoinBuilder.SkipFeatureType NXOpen.Join.CurveJoinBuilder.SkipFeatureType@endlink) SkipFeatureMethod
    ##  Returns the skip feature spacing method   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return CurveJoinBuilder.SkipFeatureType
    @property
    def SkipFeatureMethod(self) -> CurveJoinBuilder.SkipFeatureType:
        """
        Getter for property: (@link CurveJoinBuilder.SkipFeatureType NXOpen.Join.CurveJoinBuilder.SkipFeatureType@endlink) SkipFeatureMethod
         Returns the skip feature spacing method   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveJoinBuilder.SkipFeatureType NXOpen.Join.CurveJoinBuilder.SkipFeatureType@endlink) SkipFeatureMethod

    ##  Returns the skip feature spacing method   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @SkipFeatureMethod.setter
    def SkipFeatureMethod(self, skipFeatureMethod: CurveJoinBuilder.SkipFeatureType):
        """
        Setter for property: (@link CurveJoinBuilder.SkipFeatureType NXOpen.Join.CurveJoinBuilder.SkipFeatureType@endlink) SkipFeatureMethod
         Returns the skip feature spacing method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) StartDistance
    ##  Returns the start distance used to limit the length of the output curve  
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.OnPathDimensionBuilder
    @property
    def StartDistance(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) StartDistance
         Returns the start distance used to limit the length of the output curve  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartTaperAngle
    ##  Returns the groove start taper angle   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StartTaperAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartTaperAngle
         Returns the groove start taper angle   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveJoinBuilder.TaperType NXOpen.Join.CurveJoinBuilder.TaperType@endlink) TaperMethod
    ##  Returns the groove taper method value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return CurveJoinBuilder.TaperType
    @property
    def TaperMethod(self) -> CurveJoinBuilder.TaperType:
        """
        Getter for property: (@link CurveJoinBuilder.TaperType NXOpen.Join.CurveJoinBuilder.TaperType@endlink) TaperMethod
         Returns the groove taper method value   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveJoinBuilder.TaperType NXOpen.Join.CurveJoinBuilder.TaperType@endlink) TaperMethod

    ##  Returns the groove taper method value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @TaperMethod.setter
    def TaperMethod(self, taperMethod: CurveJoinBuilder.TaperType):
        """
        Setter for property: (@link CurveJoinBuilder.TaperType NXOpen.Join.CurveJoinBuilder.TaperType@endlink) TaperMethod
         Returns the groove taper method value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThroatThickness
    ##  Returns the throat thickness   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ThroatThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThroatThickness
         Returns the throat thickness   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseFaceSet1ForProjection
    ##  Returns the flag to indicate if selected curves should be projected onto face set 1.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def UseFaceSet1ForProjection(self) -> bool:
        """
        Getter for property: (bool) UseFaceSet1ForProjection
         Returns the flag to indicate if selected curves should be projected onto face set 1.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseFaceSet1ForProjection

    ##  Returns the flag to indicate if selected curves should be projected onto face set 1.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @UseFaceSet1ForProjection.setter
    def UseFaceSet1ForProjection(self, useFaceSet1ForProjection: bool):
        """
        Setter for property: (bool) UseFaceSet1ForProjection
         Returns the flag to indicate if selected curves should be projected onto face set 1.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseThroatThickness
    ##  Returns the flag to indicate whether throat thickness should be used to calculate profile dimensions.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def UseThroatThickness(self) -> bool:
        """
        Getter for property: (bool) UseThroatThickness
         Returns the flag to indicate whether throat thickness should be used to calculate profile dimensions.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseThroatThickness

    ##  Returns the flag to indicate whether throat thickness should be used to calculate profile dimensions.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @UseThroatThickness.setter
    def UseThroatThickness(self, status: bool):
        """
        Setter for property: (bool) UseThroatThickness
         Returns the flag to indicate whether throat thickness should be used to calculate profile dimensions.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) UserDefinedSolid
    ##  Returns the selected user-defined solid   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def UserDefinedSolid(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) UserDefinedSolid
         Returns the selected user-defined solid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) VisFace
    ##  Returns the face for visualization geometry placement   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def VisFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) VisFace
         Returns the face for visualization geometry placement   
            
         
        """
        pass
    
    ## Getter for property: (int) VisSolidType
    ##  Returns the visualization solid type value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def VisSolidType(self) -> int:
        """
        Getter for property: (int) VisSolidType
         Returns the visualization solid type value   
            
         
        """
        pass
    
    ## Setter for property: (int) VisSolidType

    ##  Returns the visualization solid type value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @VisSolidType.setter
    def VisSolidType(self, visSolidType: int):
        """
        Setter for property: (int) VisSolidType
         Returns the visualization solid type value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VisTubeDiameter
    ##  Returns the visualization solid tube diameter   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def VisTubeDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VisTubeDiameter
         Returns the visualization solid tube diameter   
            
         
        """
        pass
    
    ## Getter for property: (int) VisualizationColor
    ##  Returns the visualization color value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def VisualizationColor(self) -> int:
        """
        Getter for property: (int) VisualizationColor
         Returns the visualization color value   
            
         
        """
        pass
    
    ## Setter for property: (int) VisualizationColor

    ##  Returns the visualization color value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @VisualizationColor.setter
    def VisualizationColor(self, visualizationColor: int):
        """
        Setter for property: (int) VisualizationColor
         Returns the visualization color value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) WeldSize
    ##  Returns the weld size for flare groove   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def WeldSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) WeldSize
         Returns the weld size for flare groove   
            
         
        """
        pass
    
    ##  Generates extent curve 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GenerateExtentCurve(self) -> None:
        """
         Generates extent curve 
        """
        pass
    
import NXOpen.Features
##  Represents a curve based join feature  <br> To create or edit an instance of this class, use @link NXOpen::Join::CurveJoinBuilder  NXOpen::Join::CurveJoinBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class CurveJoin(NXOpen.Features.BodyFeature): 
    """ Represents a curve based join feature """
    pass


import NXOpen
##  Represents a CurveSelectBuilder class  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateCurveSelectBuilder  NXOpen::Join::JoinManager::CreateCurveSelectBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class CurveSelectBuilder(NXOpen.Builder): 
    """ Represents a CurveSelectBuilder class """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) CurveSelect
    ##  Returns the selected curve   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def CurveSelect(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) CurveSelect
         Returns the selected curve   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Features
##  A builder used to create or edit a @link NXOpen::Join::EdgePrep NXOpen::Join::EdgePrep@endlink  feature.  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateEdgePrepBuilder  NXOpen::Join::JoinManager::CreateEdgePrepBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class EdgePrepBuilder(NXOpen.Features.FeatureBuilder): 
    """ A builder used to create or edit a <ja_class>NXOpen.Join.EdgePrep</ja_class> feature. """


    ## Getter for property: (float) DistanceTolerance
    ##  Returns the distance tolerance for constructing the edge prep feature.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the edge prep feature.  
             
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##  Returns the distance tolerance for constructing the edge prep feature.  
    ##      
    ##  
    ## Setter License requirements: ugweld ("UG WELD")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the edge prep feature.  
             
         
        """
        pass
    
    ## Getter for property: (int) ErrorCode
    ##  Returns the error code for the first curve join that could not be processed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def ErrorCode(self) -> int:
        """
        Getter for property: (int) ErrorCode
         Returns the error code for the first curve join that could not be processed.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) JoinObjects
    ##  Returns the curve joins to drive edge preparation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def JoinObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) JoinObjects
         Returns the curve joins to drive edge preparation   
            
         
        """
        pass
    
    ##  Returns the curves that edge preparation was attempted on, but could not be performed. 
    ##  @return curveJoinFeatures (@link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink):  The curve join features that edge preparation failed on. .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetNoResultsInfo(self) -> List[NXOpen.Features.Feature]:
        """
         Returns the curves that edge preparation was attempted on, but could not be performed. 
         @return curveJoinFeatures (@link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink):  The curve join features that edge preparation failed on. .
        """
        pass
    
import NXOpen.Features
##  Represents a Join Edge Prep feature  <br> To create or edit an instance of this class, use @link NXOpen::Join::EdgePrepBuilder  NXOpen::Join::EdgePrepBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class EdgePrep(NXOpen.Features.BodyFeature): 
    """ Represents a Join Edge Prep feature """
    pass


import NXOpen
##  Represents a EditCurveJoinDefinitionBuilder class  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateEditCurveJoinDefinitionBuilder  NXOpen::Join::JoinManager::CreateEditCurveJoinDefinitionBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class EditCurveJoinDefinitionBuilder(NXOpen.Builder): 
    """ Represents a EditCurveJoinDefinitionBuilder class """


    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) CurveJoin
    ##  Returns the @link Join::CurveJoin Join::CurveJoin@endlink  to be edited   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def CurveJoin(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) CurveJoin
         Returns the @link Join::CurveJoin Join::CurveJoin@endlink  to be edited   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Used to view or edit the values used to define the joint and edge preparation.  <br> This sub feature is created via the main feature builder.  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## JointExitBuilder.NumberSegments </term> <description> 
##  
## 2 </description> </item> 
## 
## <item><term> 
##  
## JointExitBuilder.RootOpening </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## JointExitBuilder.SplitAngle </term> <description> 
##  
## 5.0 </description> </item> 
## 
## <item><term> 
##  
## RootOpening </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class EditCurveJoinParametersBuilder(NXOpen.Builder): 
    """ Used to view or edit the values used to define the joint and edge preparation. """


    ##  Option to indicate how the values are to be used. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Entered</term><description> 
    ##  Use the values entered as edge prep values. </description> </item><item><term> 
    ## Computed</term><description> 
    ##  Use the computed values as edge prep values. </description> </item></list>
    class Option(Enum):
        """
        Members Include: <Entered> <Computed>
        """
        Entered: int
        Computed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EditCurveJoinParametersBuilder.Option:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) EdgesPrepared
    ##  Returns the indication that the edges are prepared   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def EdgesPrepared(self) -> bool:
        """
        Getter for property: (bool) EdgesPrepared
         Returns the indication that the edges are prepared   
            
         
        """
        pass
    
    ## Setter for property: (bool) EdgesPrepared

    ##  Returns the indication that the edges are prepared   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @EdgesPrepared.setter
    def EdgesPrepared(self, prepared: bool):
        """
        Setter for property: (bool) EdgesPrepared
         Returns the indication that the edges are prepared   
            
         
        """
        pass
    
    ## Getter for property: (bool) EditingManagedAttributeGroup
    ##  Returns the indication that the modifications will be applied to a Managed Attribute Group, not the feature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def EditingManagedAttributeGroup(self) -> bool:
        """
        Getter for property: (bool) EditingManagedAttributeGroup
         Returns the indication that the modifications will be applied to a Managed Attribute Group, not the feature   
            
         
        """
        pass
    
    ## Setter for property: (bool) EditingManagedAttributeGroup

    ##  Returns the indication that the modifications will be applied to a Managed Attribute Group, not the feature   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @EditingManagedAttributeGroup.setter
    def EditingManagedAttributeGroup(self, editingManagedAttributeGroup: bool):
        """
        Setter for property: (bool) EditingManagedAttributeGroup
         Returns the indication that the modifications will be applied to a Managed Attribute Group, not the feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) Joint
    ##  Returns the joint curves.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectCurveList
    @property
    def Joint(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) Joint
         Returns the joint curves.  
             
         
        """
        pass
    
    ## Getter for property: (@link JointExitBuilder NXOpen.Weld.JointExitBuilder@endlink) JointExitBuilder
    ##  Returns the @link NXOpen::Weld::JointExitBuilder NXOpen::Weld::JointExitBuilder@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return JointExitBuilder
    @property
    def JointExitBuilder(self) -> JointExitBuilder:
        """
        Getter for property: (@link JointExitBuilder NXOpen.Weld.JointExitBuilder@endlink) JointExitBuilder
         Returns the @link NXOpen::Weld::JointExitBuilder NXOpen::Weld::JointExitBuilder@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) LeaveLooseEndValue
    ##  Returns the distance from the end of the joint to not weld (i.  
    ##   e., leave loose).   
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.OnPathDimensionBuilder
    @property
    def LeaveLooseEndValue(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) LeaveLooseEndValue
         Returns the distance from the end of the joint to not weld (i.  
          e., leave loose).   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) LeaveLooseStartValue
    ##  Returns the distance from the start of the joint to not weld (i.  
    ##   e., leave loose).   
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.OnPathDimensionBuilder
    @property
    def LeaveLooseStartValue(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) LeaveLooseStartValue
         Returns the distance from the start of the joint to not weld (i.  
          e., leave loose).   
         
        """
        pass
    
    ## Getter for property: (float) PrimaryThicknessUser
    ##  Returns the user defined value for primary thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def PrimaryThicknessUser(self) -> float:
        """
        Getter for property: (float) PrimaryThicknessUser
         Returns the user defined value for primary thickness   
            
         
        """
        pass
    
    ## Setter for property: (float) PrimaryThicknessUser

    ##  Returns the user defined value for primary thickness   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PrimaryThicknessUser.setter
    def PrimaryThicknessUser(self, thickness: float):
        """
        Setter for property: (float) PrimaryThicknessUser
         Returns the user defined value for primary thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) RootOpening
    ##  Returns the root opening   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def RootOpening(self) -> float:
        """
        Getter for property: (float) RootOpening
         Returns the root opening   
            
         
        """
        pass
    
    ## Setter for property: (float) RootOpening

    ##  Returns the root opening   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RootOpening.setter
    def RootOpening(self, rootOpening: float):
        """
        Setter for property: (float) RootOpening
         Returns the root opening   
            
         
        """
        pass
    
    ## Getter for property: (float) SecondaryThicknessUser
    ##  Returns the user defined value for secondary thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def SecondaryThicknessUser(self) -> float:
        """
        Getter for property: (float) SecondaryThicknessUser
         Returns the user defined value for secondary thickness   
            
         
        """
        pass
    
    ## Setter for property: (float) SecondaryThicknessUser

    ##  Returns the user defined value for secondary thickness   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SecondaryThicknessUser.setter
    def SecondaryThicknessUser(self, thickness: float):
        """
        Setter for property: (float) SecondaryThicknessUser
         Returns the user defined value for secondary thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) Segment2Radius
    ##  Returns the segment 2 blend radius value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def Segment2Radius(self) -> float:
        """
        Getter for property: (float) Segment2Radius
         Returns the segment 2 blend radius value   
            
         
        """
        pass
    
    ## Setter for property: (float) Segment2Radius

    ##  Returns the segment 2 blend radius value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Segment2Radius.setter
    def Segment2Radius(self, radius: float):
        """
        Setter for property: (float) Segment2Radius
         Returns the segment 2 blend radius value   
            
         
        """
        pass
    
    ## Getter for property: (float) Segment4Radius
    ##  Returns the segment 4 blend radius value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def Segment4Radius(self) -> float:
        """
        Getter for property: (float) Segment4Radius
         Returns the segment 4 blend radius value   
            
         
        """
        pass
    
    ## Setter for property: (float) Segment4Radius

    ##  Returns the segment 4 blend radius value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Segment4Radius.setter
    def Segment4Radius(self, radius: float):
        """
        Setter for property: (float) Segment4Radius
         Returns the segment 4 blend radius value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectCurve NXOpen.SelectCurve@endlink) ValueSegment
    ##  Returns the selected segment.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectCurve
    @property
    def ValueSegment(self) -> NXOpen.SelectCurve:
        """
        Getter for property: (@link NXOpen.SelectCurve NXOpen.SelectCurve@endlink) ValueSegment
         Returns the selected segment.  
             
         
        """
        pass
    
    ## Getter for property: (@link EditCurveJoinParametersBuilder.Option NXOpen.Join.EditCurveJoinParametersBuilder.Option@endlink) ValuesOption
    ##  Returns the values option which indicates whether the entered or computed values should be used.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return EditCurveJoinParametersBuilder.Option
    @property
    def ValuesOption(self) -> EditCurveJoinParametersBuilder.Option:
        """
        Getter for property: (@link EditCurveJoinParametersBuilder.Option NXOpen.Join.EditCurveJoinParametersBuilder.Option@endlink) ValuesOption
         Returns the values option which indicates whether the entered or computed values should be used.  
             
         
        """
        pass
    
    ## Setter for property: (@link EditCurveJoinParametersBuilder.Option NXOpen.Join.EditCurveJoinParametersBuilder.Option@endlink) ValuesOption

    ##  Returns the values option which indicates whether the entered or computed values should be used.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ValuesOption.setter
    def ValuesOption(self, option: EditCurveJoinParametersBuilder.Option):
        """
        Setter for property: (@link EditCurveJoinParametersBuilder.Option NXOpen.Join.EditCurveJoinParametersBuilder.Option@endlink) ValuesOption
         Returns the values option which indicates whether the entered or computed values should be used.  
             
         
        """
        pass
    
    ##  Creates the path curves to be used for @link NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseStartValue NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseStartValue@endlink  and @link NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseEndValue NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseEndValue@endlink . 
    ##  @return A tuple consisting of (path, reversedPath). 
    ##  - path is: @link NXOpen.Curve NXOpen.Curve@endlink. Path curve for @link NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseStartValue NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseStartValue@endlink . .
    ##  - reversedPath is: @link NXOpen.Curve NXOpen.Curve@endlink. Reversed Path Curve for @link NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseEndValue NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseEndValue@endlink . .

    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    def CreatePathCurvesForLeaveLoose(self) -> Tuple[NXOpen.Curve, NXOpen.Curve]:
        """
         Creates the path curves to be used for @link NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseStartValue NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseStartValue@endlink  and @link NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseEndValue NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseEndValue@endlink . 
         @return A tuple consisting of (path, reversedPath). 
         - path is: @link NXOpen.Curve NXOpen.Curve@endlink. Path curve for @link NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseStartValue NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseStartValue@endlink . .
         - reversedPath is: @link NXOpen.Curve NXOpen.Curve@endlink. Reversed Path Curve for @link NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseEndValue NXOpen::Join::EditCurveJoinParametersBuilder::LeaveLooseEndValue@endlink . .

        """
        pass
    
    ##  Deletes the @link NXOpen::Weld::JointExitBuilder NXOpen::Weld::JointExitBuilder@endlink . 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    def DeleteExitBuilder(self) -> None:
        """
         Deletes the @link NXOpen::Weld::JointExitBuilder NXOpen::Weld::JointExitBuilder@endlink . 
        """
        pass
    
    ##  Creates the path to be used for the limits. 
    ##  @return segment (@link NXOpen.Curve NXOpen.Curve@endlink):  Segment. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="value"> (int)  index of curve. </param>
    def GetSegmentFromIndex(self, value: int) -> NXOpen.Curve:
        """
         Creates the path to be used for the limits. 
         @return segment (@link NXOpen.Curve NXOpen.Curve@endlink):  Segment. .
        """
        pass
    
    ##  Reads the edge prep values from joint curve. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ## <param name="curve"> (@link NXOpen.Curve NXOpen.Curve@endlink)  Joint curve </param>
    def ReadEdgePrepValuesFromCurve(self, curve: NXOpen.Curve) -> None:
        """
         Reads the edge prep values from joint curve. 
        """
        pass
    
    ##  Recreate sketch curves for dialog preview. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    def RecreateCurves(self) -> None:
        """
         Recreate sketch curves for dialog preview. 
        """
        pass
    
import NXOpen
##  Represents a ExportJoinBuilder class  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateExportJoinBuilder  NXOpen::Join::JoinManager::CreateExportJoinBuilder @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class ExportJoinBuilder(NXOpen.Builder): 
    """ Represents a ExportJoinBuilder class """


    ##  the Output Type enum 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## IntermediateFile</term><description> 
    ## </description> </item></list>
    class OutputType(Enum):
        """
        Members Include: <IntermediateFile>
        """
        IntermediateFile: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExportJoinBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) ConnectedPartAttrToggle
    ##  Returns the connected part attribute toggle to control if read connected part attributes from join points   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def ConnectedPartAttrToggle(self) -> bool:
        """
        Getter for property: (bool) ConnectedPartAttrToggle
         Returns the connected part attribute toggle to control if read connected part attributes from join points   
            
         
        """
        pass
    
    ## Setter for property: (bool) ConnectedPartAttrToggle

    ##  Returns the connected part attribute toggle to control if read connected part attributes from join points   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @ConnectedPartAttrToggle.setter
    def ConnectedPartAttrToggle(self, connectedPartAttrToggle: bool):
        """
        Setter for property: (bool) ConnectedPartAttrToggle
         Returns the connected part attribute toggle to control if read connected part attributes from join points   
            
         
        """
        pass
    
    ## Getter for property: (str) CsvFileName
    ##  Returns the CSV file name   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return str
    @property
    def CsvFileName(self) -> str:
        """
        Getter for property: (str) CsvFileName
         Returns the CSV file name   
            
         
        """
        pass
    
    ## Setter for property: (str) CsvFileName

    ##  Returns the CSV file name   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @CsvFileName.setter
    def CsvFileName(self, csvFileName: str):
        """
        Setter for property: (str) CsvFileName
         Returns the CSV file name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) JoinPoints
    ##  Returns the join points to be exported to CSV file   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def JoinPoints(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) JoinPoints
         Returns the join points to be exported to CSV file   
            
         
        """
        pass
    
    ## Getter for property: (@link ExportJoinBuilder.OutputType NXOpen.Join.ExportJoinBuilder.OutputType@endlink) Output
    ##  Returns the option defining where to write the output data.  
    ##    Data will initally be written to a comma separated value file.  Later options will be added.   
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return ExportJoinBuilder.OutputType
    @property
    def Output(self) -> ExportJoinBuilder.OutputType:
        """
        Getter for property: (@link ExportJoinBuilder.OutputType NXOpen.Join.ExportJoinBuilder.OutputType@endlink) Output
         Returns the option defining where to write the output data.  
           Data will initally be written to a comma separated value file.  Later options will be added.   
         
        """
        pass
    
    ## Setter for property: (@link ExportJoinBuilder.OutputType NXOpen.Join.ExportJoinBuilder.OutputType@endlink) Output

    ##  Returns the option defining where to write the output data.  
    ##    Data will initally be written to a comma separated value file.  Later options will be added.   
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @Output.setter
    def Output(self, outputType: ExportJoinBuilder.OutputType):
        """
        Setter for property: (@link ExportJoinBuilder.OutputType NXOpen.Join.ExportJoinBuilder.OutputType@endlink) Output
         Returns the option defining where to write the output data.  
           Data will initally be written to a comma separated value file.  Later options will be added.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) ReferenceCsys
    ##  Returns the reference CSYS for exported data.  
    ##         
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def ReferenceCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) ReferenceCsys
         Returns the reference CSYS for exported data.  
                
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) ReferenceCsys

    ##  Returns the reference CSYS for exported data.  
    ##         
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ReferenceCsys.setter
    def ReferenceCsys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) ReferenceCsys
         Returns the reference CSYS for exported data.  
                
         
        """
        pass
    
    ## Getter for property: (str) TemplateFileName
    ##  Returns the template file name   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return str
    @property
    def TemplateFileName(self) -> str:
        """
        Getter for property: (str) TemplateFileName
         Returns the template file name   
            
         
        """
        pass
    
    ## Setter for property: (str) TemplateFileName

    ##  Returns the template file name   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @TemplateFileName.setter
    def TemplateFileName(self, templateFileName: str):
        """
        Setter for property: (str) TemplateFileName
         Returns the template file name   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseSelectedCsys
    ##  Returns the option to use the CSYS associated with @link NXOpen::Join::ExportJoinBuilder::ReferenceCsys NXOpen::Join::ExportJoinBuilder::ReferenceCsys@endlink     
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def UseSelectedCsys(self) -> bool:
        """
        Getter for property: (bool) UseSelectedCsys
         Returns the option to use the CSYS associated with @link NXOpen::Join::ExportJoinBuilder::ReferenceCsys NXOpen::Join::ExportJoinBuilder::ReferenceCsys@endlink     
            
         
        """
        pass
    
    ## Setter for property: (bool) UseSelectedCsys

    ##  Returns the option to use the CSYS associated with @link NXOpen::Join::ExportJoinBuilder::ReferenceCsys NXOpen::Join::ExportJoinBuilder::ReferenceCsys@endlink     
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @UseSelectedCsys.setter
    def UseSelectedCsys(self, csysToggle: bool):
        """
        Setter for property: (bool) UseSelectedCsys
         Returns the option to use the CSYS associated with @link NXOpen::Join::ExportJoinBuilder::ReferenceCsys NXOpen::Join::ExportJoinBuilder::ReferenceCsys@endlink     
            
         
        """
        pass
    
    ##  Get the connected part attributes of join points 
    ##  @return connectedPartAttributes (List[str]):  Connected part attributes string .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    def GetConnectedPartAttributes(self) -> List[str]:
        """
         Get the connected part attributes of join points 
         @return connectedPartAttributes (List[str]):  Connected part attributes string .
        """
        pass
    
    ##  Get the attributes of join points to be exported to CSV file 
    ##  @return exportedAttributes (List[str]):  Exported attributes string .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    def GetExportedAttributes(self) -> List[str]:
        """
         Get the attributes of join points to be exported to CSV file 
         @return exportedAttributes (List[str]):  Exported attributes string .
        """
        pass
    
    ##  Open a template file to update exported attributes. Before use it, you must set template file name. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    def OpenFromFile(self) -> None:
        """
         Open a template file to update exported attributes. Before use it, you must set template file name. 
        """
        pass
    
    ##  Read attributes from selected joins and save to exported attributes and connected part attributes 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    def ReadAttributesFromJoins(self) -> None:
        """
         Read attributes from selected joins and save to exported attributes and connected part attributes 
        """
        pass
    
    ##  Restore default template to update exported attributes. Before use it, you must set template file name. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    def RestoreDefault(self) -> None:
        """
         Restore default template to update exported attributes. Before use it, you must set template file name. 
        """
        pass
    
    ##  Save exported attributes as default template. Before use it, you must set template file name. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    def SaveAsDefault(self) -> None:
        """
         Save exported attributes as default template. Before use it, you must set template file name. 
        """
        pass
    
    ##  Save exported attributes to a template file. Before use it, you must set template file name. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    def SaveToFile(self) -> None:
        """
         Save exported attributes to a template file. Before use it, you must set template file name. 
        """
        pass
    
    ##  Set the connected part attributes of join points 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ## <param name="connectedPartAttributes"> (List[str])  Connected part attributes string </param>
    def SetConnectedPartAttributes(self, connectedPartAttributes: List[str]) -> None:
        """
         Set the connected part attributes of join points 
        """
        pass
    
    ##  Set the attributes of join points to be exported to CSV file 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ## <param name="exportedAttributes"> (List[str])  Exported attributes string </param>
    def SetExportedAttributes(self, exportedAttributes: List[str]) -> None:
        """
         Set the attributes of join points to be exported to CSV file 
        """
        pass
    
import NXOpen
##  Represents a FaceIntersectionBuilder class  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateFaceIntersectionBuilder  NXOpen::Join::JoinManager::CreateFaceIntersectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class FaceIntersectionBuilder(NXOpen.Builder): 
    """ Represents a FaceIntersectionBuilder class """


    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) EdgeSection1
    ##  Returns the primary selected edges   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def EdgeSection1(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) EdgeSection1
         Returns the primary selected edges   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) EdgeSection2
    ##  Returns the secondary selected edges   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def EdgeSection2(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) EdgeSection2
         Returns the secondary selected edges   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExtensionDistance1
    ##  Returns the primary extension distance   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ExtensionDistance1(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExtensionDistance1
         Returns the primary extension distance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExtensionDistance2
    ##  Returns the secondary extension distance   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ExtensionDistance2(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExtensionDistance2
         Returns the secondary extension distance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector1
    ##  Returns the primary selected faces   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceCollector1(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector1
         Returns the primary selected faces   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector2
    ##  Returns the secondary selected faces   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceCollector2(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector2
         Returns the secondary selected faces   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a join face intersection feature  <br> To create or edit an instance of this class, use @link NXOpen::Join::FaceIntersectionBuilder  NXOpen::Join::FaceIntersectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class FaceIntersection(NXOpen.Features.BodyFeature): 
    """ Represents a join face intersection feature """
    pass


import NXOpen
## 
##     Represents a @link NXOpen::Join::FaceJoin NXOpen::Join::FaceJoin@endlink  builder.
##      <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateFaceJoinBuilder  NXOpen::Join::JoinManager::CreateFaceJoinBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class FaceJoinBuilder(JoinBuilder): 
    """
    Represents a <ja_class>NXOpen.Join.FaceJoin</ja_class> builder.
    """


    ##  the boundary method type
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Automatic</term><description> 
    ## </description> </item><item><term> 
    ## Rectangle</term><description> 
    ## </description> </item><item><term> 
    ## Curve</term><description> 
    ## </description> </item></list>
    class BoundaryMethodType(Enum):
        """
        Members Include: <Automatic> <Rectangle> <Curve>
        """
        Automatic: int
        Rectangle: int
        Curve: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceJoinBuilder.BoundaryMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the holes coverage type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CoverTop</term><description> 
    ## </description> </item><item><term> 
    ## FillInside</term><description> 
    ## </description> </item><item><term> 
    ## DoNotCover</term><description> 
    ## </description> </item></list>
    class HolesCoverageType(Enum):
        """
        Members Include: <CoverTop> <FillInside> <DoNotCover>
        """
        CoverTop: int
        FillInside: int
        DoNotCover: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceJoinBuilder.HolesCoverageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the orientation type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NormalSelectedFace</term><description> 
    ## </description> </item><item><term> 
    ## AlongVector</term><description> 
    ## </description> </item></list>
    class OrientationTypes(Enum):
        """
        Members Include: <NormalSelectedFace> <AlongVector>
        """
        NormalSelectedFace: int
        AlongVector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceJoinBuilder.OrientationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the visualization type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## SolidBody</term><description> 
    ## </description> </item><item><term> 
    ## SheetBody</term><description> 
    ## </description> </item></list>
    class VisualizationBodyType(Enum):
        """
        Members Include: <NotSet> <SolidBody> <SheetBody>
        """
        NotSet: int
        SolidBody: int
        SheetBody: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceJoinBuilder.VisualizationBodyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the visualization location 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AboveFace</term><description> 
    ## </description> </item><item><term> 
    ## BelowFace</term><description> 
    ## </description> </item><item><term> 
    ## AboveBelowFace</term><description> 
    ## </description> </item></list>
    class VisualizationLocationType(Enum):
        """
        Members Include: <AboveFace> <BelowFace> <AboveBelowFace>
        """
        AboveFace: int
        BelowFace: int
        AboveBelowFace: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceJoinBuilder.VisualizationLocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FaceJoinBuilder.BoundaryMethodType NXOpen.Join.FaceJoinBuilder.BoundaryMethodType@endlink) BoundaryMethod
    ##  Returns the boundary method   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return FaceJoinBuilder.BoundaryMethodType
    @property
    def BoundaryMethod(self) -> FaceJoinBuilder.BoundaryMethodType:
        """
        Getter for property: (@link FaceJoinBuilder.BoundaryMethodType NXOpen.Join.FaceJoinBuilder.BoundaryMethodType@endlink) BoundaryMethod
         Returns the boundary method   
            
         
        """
        pass
    
    ## Setter for property: (@link FaceJoinBuilder.BoundaryMethodType NXOpen.Join.FaceJoinBuilder.BoundaryMethodType@endlink) BoundaryMethod

    ##  Returns the boundary method   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @BoundaryMethod.setter
    def BoundaryMethod(self, boundaryMethod: FaceJoinBuilder.BoundaryMethodType):
        """
        Setter for property: (@link FaceJoinBuilder.BoundaryMethodType NXOpen.Join.FaceJoinBuilder.BoundaryMethodType@endlink) BoundaryMethod
         Returns the boundary method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Corner1
    ##  Returns the first corner of rectangle   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Corner1(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Corner1
         Returns the first corner of rectangle   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Corner1

    ##  Returns the first corner of rectangle   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Corner1.setter
    def Corner1(self, corner1: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Corner1
         Returns the first corner of rectangle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Corner2
    ##  Returns the second corner of rectangle   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Corner2(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Corner2
         Returns the second corner of rectangle   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Corner2

    ##  Returns the second corner of rectangle   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Corner2.setter
    def Corner2(self, corner2: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Corner2
         Returns the second corner of rectangle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector
    ##  Returns the selected faces   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector
         Returns the selected faces   
            
         
        """
        pass
    
    ## Getter for property: (@link FaceJoinBuilder.HolesCoverageType NXOpen.Join.FaceJoinBuilder.HolesCoverageType@endlink) HolesCoverage
    ##  Returns the holes coverage value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceJoinBuilder.HolesCoverageType
    @property
    def HolesCoverage(self) -> FaceJoinBuilder.HolesCoverageType:
        """
        Getter for property: (@link FaceJoinBuilder.HolesCoverageType NXOpen.Join.FaceJoinBuilder.HolesCoverageType@endlink) HolesCoverage
         Returns the holes coverage value   
            
         
        """
        pass
    
    ## Setter for property: (@link FaceJoinBuilder.HolesCoverageType NXOpen.Join.FaceJoinBuilder.HolesCoverageType@endlink) HolesCoverage

    ##  Returns the holes coverage value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HolesCoverage.setter
    def HolesCoverage(self, holesCoverage: FaceJoinBuilder.HolesCoverageType):
        """
        Setter for property: (@link FaceJoinBuilder.HolesCoverageType NXOpen.Join.FaceJoinBuilder.HolesCoverageType@endlink) HolesCoverage
         Returns the holes coverage value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) InnerBoundary
    ##  Returns the section defining the inner boundary curve   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def InnerBoundary(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) InnerBoundary
         Returns the section defining the inner boundary curve   
            
         
        """
        pass
    
    ## Getter for property: (@link FaceJoinBuilder.OrientationTypes NXOpen.Join.FaceJoinBuilder.OrientationTypes@endlink) OrientationType
    ##  Returns the orientation type value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceJoinBuilder.OrientationTypes
    @property
    def OrientationType(self) -> FaceJoinBuilder.OrientationTypes:
        """
        Getter for property: (@link FaceJoinBuilder.OrientationTypes NXOpen.Join.FaceJoinBuilder.OrientationTypes@endlink) OrientationType
         Returns the orientation type value   
            
         
        """
        pass
    
    ## Setter for property: (@link FaceJoinBuilder.OrientationTypes NXOpen.Join.FaceJoinBuilder.OrientationTypes@endlink) OrientationType

    ##  Returns the orientation type value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @OrientationType.setter
    def OrientationType(self, orientationType: FaceJoinBuilder.OrientationTypes):
        """
        Setter for property: (@link FaceJoinBuilder.OrientationTypes NXOpen.Join.FaceJoinBuilder.OrientationTypes@endlink) OrientationType
         Returns the orientation type value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) OrientationVector
    ##  Returns the orientation vector   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def OrientationVector(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) OrientationVector
         Returns the orientation vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) OrientationVector

    ##  Returns the orientation vector   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @OrientationVector.setter
    def OrientationVector(self, orientationVector: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) OrientationVector
         Returns the orientation vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) OuterBoundary
    ##  Returns the section defining the outer boundary curve when boundary method is 
    ##         @link  NXOpen::Join::FaceJoinBuilder::BoundaryMethodTypeCurve   NXOpen::Join::FaceJoinBuilder::BoundaryMethodTypeCurve @endlink    
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def OuterBoundary(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) OuterBoundary
         Returns the section defining the outer boundary curve when boundary method is 
                @link  NXOpen::Join::FaceJoinBuilder::BoundaryMethodTypeCurve   NXOpen::Join::FaceJoinBuilder::BoundaryMethodTypeCurve @endlink    
            
         
        """
        pass
    
    ## Getter for property: (int) VisualizationColor
    ##  Returns the visualization color value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return int
    @property
    def VisualizationColor(self) -> int:
        """
        Getter for property: (int) VisualizationColor
         Returns the visualization color value   
            
         
        """
        pass
    
    ## Setter for property: (int) VisualizationColor

    ##  Returns the visualization color value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @VisualizationColor.setter
    def VisualizationColor(self, visualizationColor: int):
        """
        Setter for property: (int) VisualizationColor
         Returns the visualization color value   
            
         
        """
        pass
    
    ## Getter for property: (@link FaceJoinBuilder.VisualizationLocationType NXOpen.Join.FaceJoinBuilder.VisualizationLocationType@endlink) VisualizationLocation
    ##  Returns the visualization location method   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return FaceJoinBuilder.VisualizationLocationType
    @property
    def VisualizationLocation(self) -> FaceJoinBuilder.VisualizationLocationType:
        """
        Getter for property: (@link FaceJoinBuilder.VisualizationLocationType NXOpen.Join.FaceJoinBuilder.VisualizationLocationType@endlink) VisualizationLocation
         Returns the visualization location method   
            
         
        """
        pass
    
    ## Setter for property: (@link FaceJoinBuilder.VisualizationLocationType NXOpen.Join.FaceJoinBuilder.VisualizationLocationType@endlink) VisualizationLocation

    ##  Returns the visualization location method   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @VisualizationLocation.setter
    def VisualizationLocation(self, visualizationLocation: FaceJoinBuilder.VisualizationLocationType):
        """
        Setter for property: (@link FaceJoinBuilder.VisualizationLocationType NXOpen.Join.FaceJoinBuilder.VisualizationLocationType@endlink) VisualizationLocation
         Returns the visualization location method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VisualizationThickness
    ##  Returns the visualization thickness   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def VisualizationThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VisualizationThickness
         Returns the visualization thickness   
            
         
        """
        pass
    
    ## Getter for property: (@link FaceJoinBuilder.VisualizationBodyType NXOpen.Join.FaceJoinBuilder.VisualizationBodyType@endlink) VisualizationType
    ##  Returns the visualization type method   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return FaceJoinBuilder.VisualizationBodyType
    @property
    def VisualizationType(self) -> FaceJoinBuilder.VisualizationBodyType:
        """
        Getter for property: (@link FaceJoinBuilder.VisualizationBodyType NXOpen.Join.FaceJoinBuilder.VisualizationBodyType@endlink) VisualizationType
         Returns the visualization type method   
            
         
        """
        pass
    
    ## Setter for property: (@link FaceJoinBuilder.VisualizationBodyType NXOpen.Join.FaceJoinBuilder.VisualizationBodyType@endlink) VisualizationType

    ##  Returns the visualization type method   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @VisualizationType.setter
    def VisualizationType(self, visualizationType: FaceJoinBuilder.VisualizationBodyType):
        """
        Setter for property: (@link FaceJoinBuilder.VisualizationBodyType NXOpen.Join.FaceJoinBuilder.VisualizationBodyType@endlink) VisualizationType
         Returns the visualization type method   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a face based join feature  <br> To create or edit an instance of this class, use @link NXOpen::Join::FaceJoinBuilder  NXOpen::Join::FaceJoinBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class FaceJoin(NXOpen.Features.BodyFeature): 
    """ Represents a face based join feature """
    pass


import NXOpen
##  Represents a FaceSelectBuilder class  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateFaceSelectBuilder  NXOpen::Join::JoinManager::CreateFaceSelectBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class FaceSelectBuilder(NXOpen.Builder): 
    """ Represents a FaceSelectBuilder class """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceSelect
    ##  Returns the selected face   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceSelect(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceSelect
         Returns the selected face   
            
         
        """
        pass
    
import NXOpen
##  Represents a join grouping utility builder.  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateGroupJoinsBuilder  NXOpen::Join::JoinManager::CreateGroupJoinsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class GroupJoinsBuilder(NXOpen.Builder): 
    """ Represents a join grouping utility builder. """


    ##  Specifies a grouping method type to be used while grouping joins. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Standard</term><description> 
    ##  A standard one, which uses different default criterias of grouping. </description> </item><item><term> 
    ## Custom</term><description> 
    ##  A custom method type uses a pre-registered callback for join grouping. </description> </item></list>
    class GroupingMethod(Enum):
        """
        Members Include: <Standard> <Custom>
        """
        Standard: int
        Custom: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GroupJoinsBuilder.GroupingMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CustomAttributes
    ##  Returns the value of custom attributes criteria.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def CustomAttributes(self) -> bool:
        """
        Getter for property: (bool) CustomAttributes
         Returns the value of custom attributes criteria.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CustomAttributes

    ##  Returns the value of custom attributes criteria.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @CustomAttributes.setter
    def CustomAttributes(self, customAttributes: bool):
        """
        Setter for property: (bool) CustomAttributes
         Returns the value of custom attributes criteria.  
             
         
        """
        pass
    
    ## Getter for property: (@link GroupJoinsBuilder.GroupingMethod NXOpen.Join.GroupJoinsBuilder.GroupingMethod@endlink) GroupingMethodType
    ##  Returns the value of grouping type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return GroupJoinsBuilder.GroupingMethod
    @property
    def GroupingMethodType(self) -> GroupJoinsBuilder.GroupingMethod:
        """
        Getter for property: (@link GroupJoinsBuilder.GroupingMethod NXOpen.Join.GroupJoinsBuilder.GroupingMethod@endlink) GroupingMethodType
         Returns the value of grouping type.  
             
         
        """
        pass
    
    ## Setter for property: (@link GroupJoinsBuilder.GroupingMethod NXOpen.Join.GroupJoinsBuilder.GroupingMethod@endlink) GroupingMethodType

    ##  Returns the value of grouping type.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @GroupingMethodType.setter
    def GroupingMethodType(self, groupingMethod: GroupJoinsBuilder.GroupingMethod):
        """
        Setter for property: (@link GroupJoinsBuilder.GroupingMethod NXOpen.Join.GroupJoinsBuilder.GroupingMethod@endlink) GroupingMethodType
         Returns the value of grouping type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Hardware
    ##  Returns the value of hardware criteria.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def Hardware(self) -> bool:
        """
        Getter for property: (bool) Hardware
         Returns the value of hardware criteria.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Hardware

    ##  Returns the value of hardware criteria.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Hardware.setter
    def Hardware(self, hardware: bool):
        """
        Setter for property: (bool) Hardware
         Returns the value of hardware criteria.  
             
         
        """
        pass
    
    ## Getter for property: (bool) HoleRequirements
    ##  Returns the value of hole requirement criteria.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def HoleRequirements(self) -> bool:
        """
        Getter for property: (bool) HoleRequirements
         Returns the value of hole requirement criteria.  
             
         
        """
        pass
    
    ## Setter for property: (bool) HoleRequirements

    ##  Returns the value of hole requirement criteria.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @HoleRequirements.setter
    def HoleRequirements(self, holeRequirements: bool):
        """
        Setter for property: (bool) HoleRequirements
         Returns the value of hole requirement criteria.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseCustomNamingScheme
    ##  Returns the value of use custom naming scheme.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def UseCustomNamingScheme(self) -> bool:
        """
        Getter for property: (bool) UseCustomNamingScheme
         Returns the value of use custom naming scheme.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseCustomNamingScheme

    ##  Returns the value of use custom naming scheme.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @UseCustomNamingScheme.setter
    def UseCustomNamingScheme(self, useCustomNamingScheme: bool):
        """
        Setter for property: (bool) UseCustomNamingScheme
         Returns the value of use custom naming scheme.  
             
         
        """
        pass
    
import NXOpen
##  Represents a ImportJoinBuilder class  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateImportJoinBuilder  NXOpen::Join::JoinManager::CreateImportJoinBuilder @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class ImportJoinBuilder(NXOpen.Builder): 
    """ Represents a ImportJoinBuilder class """


    ##  the Output Type enum 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## IntermediateFile</term><description> 
    ## </description> </item></list>
    class OutputType(Enum):
        """
        Members Include: <IntermediateFile>
        """
        IntermediateFile: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ImportJoinBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) InputFileName
    ##  Returns the input file name   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return str
    @property
    def InputFileName(self) -> str:
        """
        Getter for property: (str) InputFileName
         Returns the input file name   
            
         
        """
        pass
    
    ## Setter for property: (str) InputFileName

    ##  Returns the input file name   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @InputFileName.setter
    def InputFileName(self, inputFileName: str):
        """
        Setter for property: (str) InputFileName
         Returns the input file name   
            
         
        """
        pass
    
    ## Getter for property: (str) TemplateFileName
    ##  Returns the template file name   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def TemplateFileName(self) -> str:
        """
        Getter for property: (str) TemplateFileName
         Returns the template file name   
            
         
        """
        pass
    
    ## Setter for property: (str) TemplateFileName

    ##  Returns the template file name   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @TemplateFileName.setter
    def TemplateFileName(self, templateFileName: str):
        """
        Setter for property: (str) TemplateFileName
         Returns the template file name   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
## 
##     Base class for all NXOpen.Join builders.
##      <br> This is an abstract class and cannot be instantiated  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class JoinBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Base class for all NXOpen.Join builders.
    """


    ##  Indicates where the new @link NXOpen::Join NXOpen::Join@endlink  will be created. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## WorkPart</term><description> 
    ##  Create new @link NXOpen::Join NXOpen::Join@endlink  in work part. </description> </item><item><term> 
    ## NewComponent</term><description> 
    ##  Create a new componenent for each @link NXOpen::Join NXOpen::Join@endlink  under the work part. </description> </item></list>
    class DestinationTypes(Enum):
        """
        Members Include: <WorkPart> <NewComponent>
        """
        WorkPart: int
        NewComponent: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> JoinBuilder.DestinationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the material assignment policy type of the join 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoneAssigned</term><description> 
    ## </description> </item><item><term> 
    ## ExternallyAssigned</term><description> 
    ## </description> </item><item><term> 
    ## JoinFeatureAssigned</term><description> 
    ## </description> </item></list>
    class MaterialAssignmentPolicyType(Enum):
        """
        Members Include: <NoneAssigned> <ExternallyAssigned> <JoinFeatureAssigned>
        """
        NoneAssigned: int
        ExternallyAssigned: int
        JoinFeatureAssigned: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> JoinBuilder.MaterialAssignmentPolicyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) Associative
    ##  Returns the associative option for join creation   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative option for join creation   
            
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##  Returns the associative option for join creation   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative option for join creation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) ConnectedBodies
    ##  Returns the Connected Bodies   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def ConnectedBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) ConnectedBodies
         Returns the Connected Bodies   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) CustomAttributesHolder
    ##  Returns a custom attribute holder object that holds the attributes temporarily.  
    ##   
    ##         The custom attributes for the @link NXOpen::Features::BodyFeature NXOpen::Features::BodyFeature@endlink  could be set on this object. 
    ##         If the attributes match the attributes' description in the join feature description, the custom attributes are created on the feature. Otherwise, ignored.
    ##         Do not delete this object, deletion results in undefined behavior.   
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def CustomAttributesHolder(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) CustomAttributesHolder
         Returns a custom attribute holder object that holds the attributes temporarily.  
          
                The custom attributes for the @link NXOpen::Features::BodyFeature NXOpen::Features::BodyFeature@endlink  could be set on this object. 
                If the attributes match the attributes' description in the join feature description, the custom attributes are created on the feature. Otherwise, ignored.
                Do not delete this object, deletion results in undefined behavior.   
         
        """
        pass
    
    ## Getter for property: (bool) DelayUpdate
    ##  Returns a delayed feature update.  
    ##    A logical true delays updating the join feature 
    ##         when the dependency geometries change. False updates the join feature normally.   
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def DelayUpdate(self) -> bool:
        """
        Getter for property: (bool) DelayUpdate
         Returns a delayed feature update.  
           A logical true delays updating the join feature 
                when the dependency geometries change. False updates the join feature normally.   
         
        """
        pass
    
    ## Setter for property: (bool) DelayUpdate

    ##  Returns a delayed feature update.  
    ##    A logical true delays updating the join feature 
    ##         when the dependency geometries change. False updates the join feature normally.   
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @DelayUpdate.setter
    def DelayUpdate(self, delayUpdate: bool):
        """
        Setter for property: (bool) DelayUpdate
         Returns a delayed feature update.  
           A logical true delays updating the join feature 
                when the dependency geometries change. False updates the join feature normally.   
         
        """
        pass
    
    ## Getter for property: (@link JoinBuilder.DestinationTypes NXOpen.Join.JoinBuilder.DestinationTypes@endlink) Destination
    ##  Returns the part destination to create new @link NXOpen::Join NXOpen::Join@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return JoinBuilder.DestinationTypes
    @property
    def Destination(self) -> JoinBuilder.DestinationTypes:
        """
        Getter for property: (@link JoinBuilder.DestinationTypes NXOpen.Join.JoinBuilder.DestinationTypes@endlink) Destination
         Returns the part destination to create new @link NXOpen::Join NXOpen::Join@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link JoinBuilder.DestinationTypes NXOpen.Join.JoinBuilder.DestinationTypes@endlink) Destination

    ##  Returns the part destination to create new @link NXOpen::Join NXOpen::Join@endlink    
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @Destination.setter
    def Destination(self, type: JoinBuilder.DestinationTypes):
        """
        Setter for property: (@link JoinBuilder.DestinationTypes NXOpen.Join.JoinBuilder.DestinationTypes@endlink) Destination
         Returns the part destination to create new @link NXOpen::Join NXOpen::Join@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceTolerance
    ##  Returns the distance tolerance   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceTolerance
         Returns the distance tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Material
    ##  Returns the material of the join   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def Material(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Material
         Returns the material of the join   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Material

    ##  Returns the material of the join   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Material
         Returns the material of the join   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaterialActualThickness
    ##  Returns the material actual thickness   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaterialActualThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaterialActualThickness
         Returns the material actual thickness   
            
         
        """
        pass
    
    ## Getter for property: (@link JoinBuilder.MaterialAssignmentPolicyType NXOpen.Join.JoinBuilder.MaterialAssignmentPolicyType@endlink) MaterialAssignmentPolicy
    ##  Returns the material assignment policy of the join   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return JoinBuilder.MaterialAssignmentPolicyType
    @property
    def MaterialAssignmentPolicy(self) -> JoinBuilder.MaterialAssignmentPolicyType:
        """
        Getter for property: (@link JoinBuilder.MaterialAssignmentPolicyType NXOpen.Join.JoinBuilder.MaterialAssignmentPolicyType@endlink) MaterialAssignmentPolicy
         Returns the material assignment policy of the join   
            
         
        """
        pass
    
    ## Setter for property: (@link JoinBuilder.MaterialAssignmentPolicyType NXOpen.Join.JoinBuilder.MaterialAssignmentPolicyType@endlink) MaterialAssignmentPolicy

    ##  Returns the material assignment policy of the join   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @MaterialAssignmentPolicy.setter
    def MaterialAssignmentPolicy(self, materialPolicy: JoinBuilder.MaterialAssignmentPolicyType):
        """
        Setter for property: (@link JoinBuilder.MaterialAssignmentPolicyType NXOpen.Join.JoinBuilder.MaterialAssignmentPolicyType@endlink) MaterialAssignmentPolicy
         Returns the material assignment policy of the join   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaterialDispensedWidth
    ##  Returns the material dispensed width   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaterialDispensedWidth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaterialDispensedWidth
         Returns the material dispensed width   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NuggetDiameter
    ##  Returns the nugget diameter   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def NuggetDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NuggetDiameter
         Returns the nugget diameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowConnectedBodies
    ##  Returns an indication of which connected bodies to include.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ShowConnectedBodies(self) -> bool:
        """
        Getter for property: (bool) ShowConnectedBodies
         Returns an indication of which connected bodies to include.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowConnectedBodies

    ##  Returns an indication of which connected bodies to include.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ShowConnectedBodies.setter
    def ShowConnectedBodies(self, showConnectedBodies: bool):
        """
        Setter for property: (bool) ShowConnectedBodies
         Returns an indication of which connected bodies to include.  
             
         
        """
        pass
    
    ## Getter for property: (str) Subtype
    ##  Returns the Subtype   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return str
    @property
    def Subtype(self) -> str:
        """
        Getter for property: (str) Subtype
         Returns the Subtype   
            
         
        """
        pass
    
    ## Setter for property: (str) Subtype

    ##  Returns the Subtype   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @Subtype.setter
    def Subtype(self, type: str):
        """
        Setter for property: (str) Subtype
         Returns the Subtype   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.FinishMethod NXOpen.Annotations.FinishMethod@endlink) WeldFinishMethod
    ##  Returns the weld finish method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Annotations.FinishMethod
    @property
    def WeldFinishMethod(self) -> NXOpen.Annotations.FinishMethod:
        """
        Getter for property: (@link NXOpen.Annotations.FinishMethod NXOpen.Annotations.FinishMethod@endlink) WeldFinishMethod
         Returns the weld finish method   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Annotations.FinishMethod NXOpen.Annotations.FinishMethod@endlink) WeldFinishMethod

    ##  Returns the weld finish method   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @WeldFinishMethod.setter
    def WeldFinishMethod(self, method: NXOpen.Annotations.FinishMethod):
        """
        Setter for property: (@link NXOpen.Annotations.FinishMethod NXOpen.Annotations.FinishMethod@endlink) WeldFinishMethod
         Returns the weld finish method   
            
         
        """
        pass
    
    ##  Used to collect newly created wave links on the fly. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ## <param name="waveLink"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def AddNewlyCreatedWaveLink(self, waveLink: NXOpen.NXObject) -> None:
        """
         Used to collect newly created wave links on the fly. 
        """
        pass
    
    ##  Gets visualization bodies created by @link NXOpen::Join NXOpen::Join@endlink  of the builder. 
    ##  @return joinBodies (@link NXOpen.Body List[NXOpen.Body]@endlink):  .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    def GetJoinBodies(self) -> List[NXOpen.Body]:
        """
         Gets visualization bodies created by @link NXOpen::Join NXOpen::Join@endlink  of the builder. 
         @return joinBodies (@link NXOpen.Body List[NXOpen.Body]@endlink):  .
        """
        pass
    
    ##  Indicates whether the output should be hidden on creation 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ## <param name="hideSolid"> (bool)  true- Hide output solid. </param>
    def SetHideSolid(self, hideSolid: bool) -> None:
        """
         Indicates whether the output should be hidden on creation 
        """
        pass
    
    ##  Indicates whether the output objects should show through on creation 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ## <param name="status"> (bool)  true- Add show through attribute to point. </param>
    def SetShowThroughState(self, status: bool) -> None:
        """
         Indicates whether the output objects should show through on creation 
        """
        pass
    
import NXOpen
##  Represents a utility for Join Check-Mate checkers.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link PointJoin PointJoin@endlink  instead.  <br> 

class JoinCheckMateUtils(NXOpen.Object): 
    """ Represents a utility for Join Check-Mate checkers. """


    ##  Check whether all of the connected parts of @link Join::PointJoin Join::PointJoin@endlink  are in fully loaded state or not.
    ##  @return fullyLoaded (bool): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link PointJoin PointJoin@endlink  instead.  <br> 

    ## License requirements: None.
    ## <param name="pointJoin"> (@link PointJoin NXOpen.Join.PointJoin@endlink) </param>
    def AreConnectedPartsFullyLoaded(pointJoin: PointJoin) -> bool:
        """
         Check whether all of the connected parts of @link Join::PointJoin Join::PointJoin@endlink  are in fully loaded state or not.
         @return fullyLoaded (bool): .
        """
        pass
    
    ##  Gets simple hole diameter of a @link Join::PointJoin Join::PointJoin@endlink .
    ##  @return holeDiameter (float): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link PointJoin PointJoin@endlink  instead.  <br> 

    ## License requirements: None.
    ## <param name="pointJoin"> (@link PointJoin NXOpen.Join.PointJoin@endlink) </param>
    def GetHoleDiameter(pointJoin: PointJoin) -> float:
        """
         Gets simple hole diameter of a @link Join::PointJoin Join::PointJoin@endlink .
         @return holeDiameter (float): .
        """
        pass
    
    ##  Gets first stackup entry point of a @link Join::PointJoin Join::PointJoin@endlink .
    ##  @return firstEntryPoint (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link PointJoin PointJoin@endlink  instead.  <br> 

    ## License requirements: None.
    ## <param name="pointJoin"> (@link PointJoin NXOpen.Join.PointJoin@endlink) </param>
    def GetPointJoinStackupFirstEntryPoint(pointJoin: PointJoin) -> NXOpen.Point3d:
        """
         Gets first stackup entry point of a @link Join::PointJoin Join::PointJoin@endlink .
         @return firstEntryPoint (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
        """
        pass
    
    ##  Gets stackup information of a @link Join::PointJoin Join::PointJoin@endlink .
    ##  @return stackupInfo (@link PointJoinStackupInfo NXOpen.Join.PointJoinStackupInfo@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link PointJoin PointJoin@endlink  instead.  <br> 

    ## License requirements: None.
    ## <param name="pointJoin"> (@link PointJoin NXOpen.Join.PointJoin@endlink) </param>
    def GetStackupInfo(pointJoin: PointJoin) -> PointJoinStackupInfo:
        """
         Gets stackup information of a @link Join::PointJoin Join::PointJoin@endlink .
         @return stackupInfo (@link PointJoinStackupInfo NXOpen.Join.PointJoinStackupInfo@endlink): .
        """
        pass
    
    ##  Load connected parts of @link Join::PointJoin Join::PointJoin@endlink .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link PointJoin PointJoin@endlink  instead.  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="pointJoin"> (@link PointJoin NXOpen.Join.PointJoin@endlink) </param>
    def LoadConnectedParts(pointJoin: PointJoin) -> None:
        """
         Load connected parts of @link Join::PointJoin Join::PointJoin@endlink .
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##     Represents a builder to run the Analyze Connections command.
##      <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateConnectedFaceFinderBuilder  NXOpen::Join::JoinManager::CreateConnectedFaceFinderBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ConnectionFinder.Filter </term> <description> 
##  
## All </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class JoinedFaceFinderBuilder(NXOpen.Builder): 
    """
    Represents a builder to run the Analyze Connections command.
    """


    ## Getter for property: (@link JoinedFinderBuilder NXOpen.Join.JoinedFinderBuilder@endlink) ConnectionFinder
    ##  Returns the connection finder object that manages the interaction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return JoinedFinderBuilder
    @property
    def ConnectionFinder(self) -> JoinedFinderBuilder:
        """
        Getter for property: (@link JoinedFinderBuilder NXOpen.Join.JoinedFinderBuilder@endlink) ConnectionFinder
         Returns the connection finder object that manages the interaction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) Features
    ##  Returns the join features used to analyze connections.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Features.SelectFeatureList
    @property
    def Features(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) Features
         Returns the join features used to analyze connections.  
             
         
        """
        pass
    
    ##  Gets all the result nodes. Each node will either be a Group entity, or feature if it cannot be grouped. 
    ##  @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): The array group objects, or features. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetResultNodes(self) -> List[NXOpen.NXObject]:
        """
         Gets all the result nodes. Each node will either be a Group entity, or feature if it cannot be grouped. 
         @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): The array group objects, or features. .
        """
        pass
    
    ##  Process the selected join features by finding the new connected parts for each feature. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def PerformAnalysis(self) -> None:
        """
         Process the selected join features by finding the new connected parts for each feature. 
        """
        pass
    
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
## 
##     Represents a builder to display, manage, delete, and allow the user to
##     edit Point Join features.
##     
## 
##   <br>  Created in NX2206.0.0  <br> 

class JoinedFinderBuilder(NXOpen.TaggedObject): 
    """
    Represents a builder to display, manage, delete, and allow the user to
    edit Point Join features.
    """


    ##  Filter value to control which nodes are shown. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## Passed</term><description> 
    ## </description> </item><item><term> 
    ## Warning</term><description> 
    ## </description> </item><item><term> 
    ## Failed</term><description> 
    ## </description> </item><item><term> 
    ## Saved</term><description> 
    ## </description> </item><item><term> 
    ## NotSaved</term><description> 
    ## </description> </item><item><term> 
    ## Deleted</term><description> 
    ## </description> </item></list>
    class FilterTypes(Enum):
        """
        Members Include: <All> <Passed> <Warning> <Failed> <Saved> <NotSaved> <Deleted>
        """
        All: int
        Passed: int
        Warning: int
        Failed: int
        Saved: int
        NotSaved: int
        Deleted: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> JoinedFinderBuilder.FilterTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link JoinedFinderBuilder.FilterTypes NXOpen.Join.JoinedFinderBuilder.FilterTypes@endlink) Filter
    ##  Returns the filter value to control which nodes are shown.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return JoinedFinderBuilder.FilterTypes
    @property
    def Filter(self) -> JoinedFinderBuilder.FilterTypes:
        """
        Getter for property: (@link JoinedFinderBuilder.FilterTypes NXOpen.Join.JoinedFinderBuilder.FilterTypes@endlink) Filter
         Returns the filter value to control which nodes are shown.  
             
         
        """
        pass
    
    ## Setter for property: (@link JoinedFinderBuilder.FilterTypes NXOpen.Join.JoinedFinderBuilder.FilterTypes@endlink) Filter

    ##  Returns the filter value to control which nodes are shown.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Filter.setter
    def Filter(self, filter: JoinedFinderBuilder.FilterTypes):
        """
        Setter for property: (@link JoinedFinderBuilder.FilterTypes NXOpen.Join.JoinedFinderBuilder.FilterTypes@endlink) Filter
         Returns the filter value to control which nodes are shown.  
             
         
        """
        pass
    
    ## Getter for property: (bool) GroupResults
    ##  Returns the option to list the results grouped by feature type, and common connected parts.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def GroupResults(self) -> bool:
        """
        Getter for property: (bool) GroupResults
         Returns the option to list the results grouped by feature type, and common connected parts.  
             
         
        """
        pass
    
    ## Setter for property: (bool) GroupResults

    ##  Returns the option to list the results grouped by feature type, and common connected parts.  
    ##      
    ##  
    ## Setter License requirements: ugweld ("UG WELD")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @GroupResults.setter
    def GroupResults(self, groupResults: bool):
        """
        Setter for property: (bool) GroupResults
         Returns the option to list the results grouped by feature type, and common connected parts.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) ReassignBody
    ##  Returns the object to use when changing a connected body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def ReassignBody(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) ReassignBody
         Returns the object to use when changing a connected body.  
             
         
        """
        pass
    
    ##  Adjusts the display of the part and fits the selected join features in the center of the graphics window. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="nodeTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Join Feature, or other NX object. </param>
    def CenterNode(self, nodeTag: NXOpen.NXObject) -> None:
        """
         Adjusts the display of the part and fits the selected join features in the center of the graphics window. 
        """
        pass
    
    ##  Clears the tree list and allows you to perform another search. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def ClearAllTree(self) -> None:
        """
         Clears the tree list and allows you to perform another search. 
        """
        pass
    
    ##  Marks the join feature to be delete. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="nodeTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Join Feature. </param>
    def DeleteNode(self, nodeTag: NXOpen.NXObject) -> None:
        """
         Marks the join feature to be delete. 
        """
        pass
    
    ##  From the feature, or group entity, get an array the SelectObject entities. This list can be used to change the body in the SelectObject entity. 
    ##  @return selectObjects (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Array of SelectObject entities for the connected bodies. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="joinFeatureTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  A Join Feature, or Group entity to get connected bodies for. </param>
    def FeatureSelectObjects(self, joinFeatureTag: NXOpen.NXObject) -> List[NXOpen.TaggedObject]:
        """
         From the feature, or group entity, get an array the SelectObject entities. This list can be used to change the body in the SelectObject entity. 
         @return selectObjects (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Array of SelectObject entities for the connected bodies. .
        """
        pass
    
    ##  Get the body collectors for the given feature.  
    ##  @return bodyCollectors (@link NXOpen.ScCollector List[NXOpen.ScCollector]@endlink):  Body Collectors. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="joinFeature"> (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink)  Specific join feature. </param>
    def GetBodies(self, joinFeature: NXOpen.Features.Feature) -> List[NXOpen.ScCollector]:
        """
         Get the body collectors for the given feature.  
         @return bodyCollectors (@link NXOpen.ScCollector List[NXOpen.ScCollector]@endlink):  Body Collectors. .
        """
        pass
    
    ##  Mark the feature or group node as modified/unmodified. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="joinFeatureTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  A Join Feature, or Group entity to get connected bodies for. </param>
    ## <param name="isModified"> (bool)  if true, the node will be marked as modified. </param>
    def MarkFeatureModified(self, joinFeatureTag: NXOpen.NXObject, isModified: bool) -> None:
        """
         Mark the feature or group node as modified/unmodified. 
        """
        pass
    
    ##  Reassign the bodies for a specified node. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="ownerTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  A Join Feature, or Group entity if editing by common connected bodies. </param>
    ## <param name="nodeTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink)  the object list to update this node with. </param>
    def ReassignBodyNode(self, ownerTag: NXOpen.NXObject, nodeTag: NXOpen.TaggedObject) -> None:
        """
         Reassign the bodies for a specified node. 
        """
        pass
    
    ##  Removes a connected body for a single feature, or multiple features if results are grouped. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="selectObjectTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink)  The SelectObject in the node to remove.  The body node will be marked for deletion, and deleted during @link Builder::Commit Builder::Commit@endlink . </param>
    def RemoveBodyNode(self, selectObjectTag: NXOpen.TaggedObject) -> None:
        """
         Removes a connected body for a single feature, or multiple features if results are grouped. 
        """
        pass
    
    ##  Identify all the connected part information as "accepted" so @link Builder::Commit Builder::Commit@endlink  will save the information. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def SaveAllTree(self) -> None:
        """
         Identify all the connected part information as "accepted" so @link Builder::Commit Builder::Commit@endlink  will save the information. 
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a @link Join::JoinHoleBuilder Join::JoinHoleBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateJoinHoleBuilder  NXOpen::Join::JoinManager::CreateJoinHoleBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class JoinHoleBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Join.JoinHoleBuilder</ja_class> builder. """


    ## Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) PointJoins
    ##  Returns the selected point joins   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Features.SelectFeatureList
    @property
    def PointJoins(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) PointJoins
         Returns the selected point joins   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a point join hole feature  <br> To create or edit an instance of this class, use @link NXOpen::Join::JoinHoleBuilder  NXOpen::Join::JoinHoleBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class JoinHole(NXOpen.Features.Feature): 
    """ Represents a point join hole feature """
    pass


import NXOpen
import NXOpen.Annotations
import NXOpen.Features
##  Represents a manager of join feature builders.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class JoinManager(NXOpen.Object): 
    """ Represents a manager of join feature builders. """


    ##  The reason for registering a callback indicates which Join commands will use
    ##             the callback.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unknown</term><description> 
    ##  Used only for validation. </description> </item><item><term> 
    ## PostCommit</term><description> 
    ##  Called in dialog apply processing after Join builder commit has been executed. Result of @link Builder::GetCommittedObjects Builder::GetCommittedObjects@endlink  is passed to @link NXOpen::Join::JoinManager::ExecuteCallback NXOpen::Join::JoinManager::ExecuteCallback@endlink . </description> </item><item><term> 
    ## GroupJoinsCustomMethod</term><description> 
    ##  Called on apply of group joins utility. </description> </item><item><term> 
    ## EasyJoinPoints</term><description> 
    ##  Called from Easy Join to override creation of Point Join features. </description> </item><item><term> 
    ## JointParameters</term><description> 
    ##  Called to set parameters on rbsw type curve joins. </description> </item><item><term> 
    ## TransformPostCommit</term><description> 
    ##  Called in transform dialog apply processing after builder commit has been executed. Result of @link Builder::GetCommittedObjects Builder::GetCommittedObjects@endlink  is passed to @link NXOpen::Join::JoinManager::ExecuteCallback NXOpen::Join::JoinManager::ExecuteCallback@endlink . </description> </item><item><term> 
    ## PreDialogLaunch</term><description> 
    ##  Called in dialog initialization processing before dialog is launched. @link NXOpen::Join::JoinBuilder NXOpen::Join::JoinBuilder@endlink  is passed to @link NXOpen::Join::JoinManager::ExecuteCallback NXOpen::Join::JoinManager::ExecuteCallback@endlink . </description> </item><item><term> 
    ## Count</term><description> 
    ##  The number of callback reasons. </description> </item></list>
    class CallbackReason(Enum):
        """
        Members Include: <Unknown> <PostCommit> <GroupJoinsCustomMethod> <EasyJoinPoints> <JointParameters> <TransformPostCommit> <PreDialogLaunch> <Count>
        """
        Unknown: int
        PostCommit: int
        GroupJoinsCustomMethod: int
        EasyJoinPoints: int
        JointParameters: int
        TransformPostCommit: int
        PreDialogLaunch: int
        Count: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> JoinManager.CallbackReason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This defines the prototype for all Join callbacks. 
    ## A callback definition with the following input arguments: 
    ##  - @link NXOpen.NXObject List[NXOpen.NXObject]@endlink
    ##  and no return type
    Callback = Callable[[List[NXOpen.NXObject]], None]
    
    
    ##  Adds the callback with the given reason.
    ##             NOTE: You can register more than one callback with the same reason. 
    ##  @return callbackMethodId (int):  A unique identifier for your callback. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="reason"> (@link JoinManager.CallbackReason NXOpen.Join.JoinManager.CallbackReason@endlink)  The reason for which you want this callback called. </param>
    ## <param name="callbackMethod"> (@link JoinManager.Callback NXOpen.Join.JoinManager.Callback@endlink)  The method you want to be called. </param>
    def AddCallback(reason: JoinManager.CallbackReason, callbackMethod: JoinManager.Callback) -> int:
        """
         Adds the callback with the given reason.
                    NOTE: You can register more than one callback with the same reason. 
         @return callbackMethodId (int):  A unique identifier for your callback. .
        """
        pass
    
    ##  Check whether all of the connected parts of @link Join::PointJoin Join::PointJoin@endlink  are in fully loaded state or not.
    ##  @return fullyLoaded (bool): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link NXOpen::Join::PointJoin::AreConnectedPartsFullyLoaded NXOpen::Join::PointJoin::AreConnectedPartsFullyLoaded@endlink  instead.  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="pointJoin"> (@link PointJoin NXOpen.Join.PointJoin@endlink) </param>
    def AreConnectedPartsFullyLoaded(pointJoin: PointJoin) -> bool:
        """
         Check whether all of the connected parts of @link Join::PointJoin Join::PointJoin@endlink  are in fully loaded state or not.
         @return fullyLoaded (bool): .
        """
        pass
    
    ##  Creates a @link Join::AttachedHardwareBuilder Join::AttachedHardwareBuilder@endlink  
    ##  @return builder (@link AttachedHardwareBuilder NXOpen.Join.AttachedHardwareBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="attachedHardware"> (@link AttachedHardware NXOpen.Join.AttachedHardware@endlink)  @link Join::AttachedHardware Join::AttachedHardware@endlink  to be edited </param>
    def CreateAttachedHardwareBuilder(part: NXOpen.Part, attachedHardware: AttachedHardware) -> AttachedHardwareBuilder:
        """
         Creates a @link Join::AttachedHardwareBuilder Join::AttachedHardwareBuilder@endlink  
         @return builder (@link AttachedHardwareBuilder NXOpen.Join.AttachedHardwareBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Join::AutoPointBuilder Join::AutoPointBuilder@endlink  
    ##  @return builder (@link AutoPointBuilder NXOpen.Join.AutoPointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateAutoPointBuilder(part: NXOpen.Part) -> AutoPointBuilder:
        """
         Creates a @link Join::AutoPointBuilder Join::AutoPointBuilder@endlink  
         @return builder (@link AutoPointBuilder NXOpen.Join.AutoPointBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Join::CompoundJoinWeldBuilder NXOpen::Join::CompoundJoinWeldBuilder@endlink  object 
    ##  @return builder (@link CompoundJoinWeldBuilder NXOpen.Join.CompoundJoinWeldBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="compoundJoinWeld"> (@link CompoundJoinWeld NXOpen.Join.CompoundJoinWeld@endlink)  @link NXOpen::Join::CompoundJoinWeld NXOpen::Join::CompoundJoinWeld@endlink  to be edited </param>
    def CreateCompoundJoinWeldBuilder(part: NXOpen.Part, compoundJoinWeld: CompoundJoinWeld) -> CompoundJoinWeldBuilder:
        """
         Creates a @link NXOpen::Join::CompoundJoinWeldBuilder NXOpen::Join::CompoundJoinWeldBuilder@endlink  object 
         @return builder (@link CompoundJoinWeldBuilder NXOpen.Join.CompoundJoinWeldBuilder@endlink):  .
        """
        pass
    
    ##  Creates a builder for running the Connected Face Finder utility. 
    ##  @return builder (@link JoinedFaceFinderBuilder NXOpen.Join.JoinedFaceFinderBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="features"> (@link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink)  MUST be an set of join features. </param>
    def CreateConnectedFaceFinderBuilder(part: NXOpen.Part, features: List[NXOpen.Features.Feature]) -> JoinedFaceFinderBuilder:
        """
         Creates a builder for running the Connected Face Finder utility. 
         @return builder (@link JoinedFaceFinderBuilder NXOpen.Join.JoinedFaceFinderBuilder@endlink):  .
        """
        pass
    
    ##  Creates a builder for running the Connected Face Finder utility. 
    ##  @return builder (@link JoinedFaceFinderBuilder NXOpen.Join.JoinedFaceFinderBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateConnectedFaceFinderOperation(part: NXOpen.Part) -> JoinedFaceFinderBuilder:
        """
         Creates a builder for running the Connected Face Finder utility. 
         @return builder (@link JoinedFaceFinderBuilder NXOpen.Join.JoinedFaceFinderBuilder@endlink):  .
        """
        pass
    
    ##  Creates a @link Join::CurveJoinBuilder Join::CurveJoinBuilder@endlink  
    ##  @return builder (@link CurveJoinBuilder NXOpen.Join.CurveJoinBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="curveJoin"> (@link CurveJoin NXOpen.Join.CurveJoin@endlink)  @link Join::CurveJoin Join::CurveJoin@endlink  to be edited </param>
    def CreateCurveJoinBuilder(part: NXOpen.Part, curveJoin: CurveJoin) -> CurveJoinBuilder:
        """
         Creates a @link Join::CurveJoinBuilder Join::CurveJoinBuilder@endlink  
         @return builder (@link CurveJoinBuilder NXOpen.Join.CurveJoinBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Join::CurveSelectBuilder NXOpen::Join::CurveSelectBuilder@endlink  object. 
    ##  @return builder (@link CurveSelectBuilder NXOpen.Join.CurveSelectBuilder@endlink):  CurveSelectBuilder builder.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateCurveSelectBuilder(part: NXOpen.Part) -> CurveSelectBuilder:
        """
         Creates a @link NXOpen::Join::CurveSelectBuilder NXOpen::Join::CurveSelectBuilder@endlink  object. 
         @return builder (@link CurveSelectBuilder NXOpen.Join.CurveSelectBuilder@endlink):  CurveSelectBuilder builder.
        """
        pass
    
    ##  Creates a @link NXOpen::Weld::EdgePrepBuilder NXOpen::Weld::EdgePrepBuilder@endlink  object. 
    ##  @return builder (@link EdgePrepBuilder NXOpen.Join.EdgePrepBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="edgePrepFeature"> (@link EdgePrep NXOpen.Join.EdgePrep@endlink)  Join Edge Prep Feature to be edited </param>
    def CreateEdgePrepBuilder(part: NXOpen.Part, edgePrepFeature: EdgePrep) -> EdgePrepBuilder:
        """
         Creates a @link NXOpen::Weld::EdgePrepBuilder NXOpen::Weld::EdgePrepBuilder@endlink  object. 
         @return builder (@link EdgePrepBuilder NXOpen.Join.EdgePrepBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Join::EditCurveJoinDefinitionBuilder NXOpen::Join::EditCurveJoinDefinitionBuilder@endlink  object. 
    ##  @return builder (@link EditCurveJoinDefinitionBuilder NXOpen.Join.EditCurveJoinDefinitionBuilder@endlink):  EditCurveJoinDefinitionBuilder builder.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join_structures (" Automated Structure Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateEditCurveJoinDefinitionBuilder(part: NXOpen.Part) -> EditCurveJoinDefinitionBuilder:
        """
         Creates a @link NXOpen::Join::EditCurveJoinDefinitionBuilder NXOpen::Join::EditCurveJoinDefinitionBuilder@endlink  object. 
         @return builder (@link EditCurveJoinDefinitionBuilder NXOpen.Join.EditCurveJoinDefinitionBuilder@endlink):  EditCurveJoinDefinitionBuilder builder.
        """
        pass
    
    ##  Creates a @link NXOpen::Join::EditCurveJoinParametersBuilder NXOpen::Join::EditCurveJoinParametersBuilder@endlink  object. 
    ##  @return builder (@link EditCurveJoinParametersBuilder NXOpen.Join.EditCurveJoinParametersBuilder@endlink):  EditCurveJoinParametersBuilder builder.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join_structures (" Automated Structure Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="parentBuilder"> (@link EditCurveJoinDefinitionBuilder NXOpen.Join.EditCurveJoinDefinitionBuilder@endlink) </param>
    def CreateEditCurveJoinParametersBuilder(part: NXOpen.Part, parentBuilder: EditCurveJoinDefinitionBuilder) -> EditCurveJoinParametersBuilder:
        """
         Creates a @link NXOpen::Join::EditCurveJoinParametersBuilder NXOpen::Join::EditCurveJoinParametersBuilder@endlink  object. 
         @return builder (@link EditCurveJoinParametersBuilder NXOpen.Join.EditCurveJoinParametersBuilder@endlink):  EditCurveJoinParametersBuilder builder.
        """
        pass
    
    ##  Creates a @link NXOpen::Join::ExportJoinBuilder NXOpen::Join::ExportJoinBuilder@endlink  object. 
    ##  @return builder (@link ExportJoinBuilder NXOpen.Join.ExportJoinBuilder@endlink):  ExportJoin builder.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateExportJoinBuilder(part: NXOpen.Part) -> ExportJoinBuilder:
        """
         Creates a @link NXOpen::Join::ExportJoinBuilder NXOpen::Join::ExportJoinBuilder@endlink  object. 
         @return builder (@link ExportJoinBuilder NXOpen.Join.ExportJoinBuilder@endlink):  ExportJoin builder.
        """
        pass
    
    ##  Creates a @link Join::FaceIntersectionBuilder Join::FaceIntersectionBuilder@endlink  
    ##  @return builder (@link FaceIntersectionBuilder NXOpen.Join.FaceIntersectionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="faceIntersection"> (@link FaceIntersection NXOpen.Join.FaceIntersection@endlink)  @link Join::FaceIntersection Join::FaceIntersection@endlink  to be edited </param>
    def CreateFaceIntersectionBuilder(part: NXOpen.Part, faceIntersection: FaceIntersection) -> FaceIntersectionBuilder:
        """
         Creates a @link Join::FaceIntersectionBuilder Join::FaceIntersectionBuilder@endlink  
         @return builder (@link FaceIntersectionBuilder NXOpen.Join.FaceIntersectionBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Join::FaceJoinBuilder Join::FaceJoinBuilder@endlink  
    ##  @return builder (@link FaceJoinBuilder NXOpen.Join.FaceJoinBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="faceJoin"> (@link FaceJoin NXOpen.Join.FaceJoin@endlink)  @link Join::FaceJoin Join::FaceJoin@endlink  to be edited </param>
    def CreateFaceJoinBuilder(part: NXOpen.Part, faceJoin: FaceJoin) -> FaceJoinBuilder:
        """
         Creates a @link Join::FaceJoinBuilder Join::FaceJoinBuilder@endlink  
         @return builder (@link FaceJoinBuilder NXOpen.Join.FaceJoinBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Join::FaceSelectBuilder NXOpen::Join::FaceSelectBuilder@endlink  object. 
    ##  @return builder (@link FaceSelectBuilder NXOpen.Join.FaceSelectBuilder@endlink):  FaceSelectBuilder builder.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateFaceSelectBuilder(part: NXOpen.Part) -> FaceSelectBuilder:
        """
         Creates a @link NXOpen::Join::FaceSelectBuilder NXOpen::Join::FaceSelectBuilder@endlink  object. 
         @return builder (@link FaceSelectBuilder NXOpen.Join.FaceSelectBuilder@endlink):  FaceSelectBuilder builder.
        """
        pass
    
    ##  Creates a @link Join::GroupJoinsBuilder Join::GroupJoinsBuilder@endlink  
    ##  @return builder (@link GroupJoinsBuilder NXOpen.Join.GroupJoinsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateGroupJoinsBuilder(part: NXOpen.Part) -> GroupJoinsBuilder:
        """
         Creates a @link Join::GroupJoinsBuilder Join::GroupJoinsBuilder@endlink  
         @return builder (@link GroupJoinsBuilder NXOpen.Join.GroupJoinsBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Join::ImportJoinBuilder NXOpen::Join::ImportJoinBuilder@endlink  object. 
    ##  @return builder (@link ImportJoinBuilder NXOpen.Join.ImportJoinBuilder@endlink):  ImportJoin builder.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateImportJoinBuilder(part: NXOpen.Part) -> ImportJoinBuilder:
        """
         Creates a @link NXOpen::Join::ImportJoinBuilder NXOpen::Join::ImportJoinBuilder@endlink  object. 
         @return builder (@link ImportJoinBuilder NXOpen.Join.ImportJoinBuilder@endlink):  ImportJoin builder.
        """
        pass
    
    ##  Creates a @link NXOpen::Join::JoinHoleBuilder NXOpen::Join::JoinHoleBuilder@endlink  
    ##  @return builder (@link JoinHoleBuilder NXOpen.Join.JoinHoleBuilder@endlink):  @link NXOpen::Join::JoinHoleBuilder NXOpen::Join::JoinHoleBuilder@endlink  to be returned .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="joinHole"> (@link JoinHole NXOpen.Join.JoinHole@endlink)  @link NXOpen::Join::JoinHole NXOpen::Join::JoinHole@endlink  to be edited </param>
    def CreateJoinHoleBuilder(part: NXOpen.Part, joinHole: JoinHole) -> JoinHoleBuilder:
        """
         Creates a @link NXOpen::Join::JoinHoleBuilder NXOpen::Join::JoinHoleBuilder@endlink  
         @return builder (@link JoinHoleBuilder NXOpen.Join.JoinHoleBuilder@endlink):  @link NXOpen::Join::JoinHoleBuilder NXOpen::Join::JoinHoleBuilder@endlink  to be returned .
        """
        pass
    
    ##  Creates a @link NXOpen::Join::JoinNoteBuilder NXOpen::Join::JoinNoteBuilder@endlink  object. 
    ##  @return builder (@link JoinNoteBuilder NXOpen.Join.JoinNoteBuilder@endlink):  Join Note builder.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="annotation"> (@link NXOpen.Annotations.Annotation NXOpen.Annotations.Annotation@endlink) </param>
    def CreateJoinNoteBuilder(part: NXOpen.Part, annotation: NXOpen.Annotations.Annotation) -> JoinNoteBuilder:
        """
         Creates a @link NXOpen::Join::JoinNoteBuilder NXOpen::Join::JoinNoteBuilder@endlink  object. 
         @return builder (@link JoinNoteBuilder NXOpen.Join.JoinNoteBuilder@endlink):  Join Note builder.
        """
        pass
    
    ##  Creates a @link NXOpen::Join::MultiEditCurveJoinParametersBuilder NXOpen::Join::MultiEditCurveJoinParametersBuilder@endlink  object. 
    ##  @return builder (@link MultiEditCurveJoinParametersBuilder NXOpen.Join.MultiEditCurveJoinParametersBuilder@endlink):  MultiEditCurveJoinParametersBuilder builder.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="parentBuilder"> (@link EditCurveJoinDefinitionBuilder NXOpen.Join.EditCurveJoinDefinitionBuilder@endlink) </param>
    def CreateMultiEditCurveJoinParametersBuilder(part: NXOpen.Part, parentBuilder: EditCurveJoinDefinitionBuilder) -> MultiEditCurveJoinParametersBuilder:
        """
         Creates a @link NXOpen::Join::MultiEditCurveJoinParametersBuilder NXOpen::Join::MultiEditCurveJoinParametersBuilder@endlink  object. 
         @return builder (@link MultiEditCurveJoinParametersBuilder NXOpen.Join.MultiEditCurveJoinParametersBuilder@endlink):  MultiEditCurveJoinParametersBuilder builder.
        """
        pass
    
    ##  Creates a @link NXOpen::Join::MultiEditPointJoinBuilder NXOpen::Join::MultiEditPointJoinBuilder@endlink  object. 
    ##  @return builder (@link MultiEditPointJoinBuilder NXOpen.Join.MultiEditPointJoinBuilder@endlink):  MultiEditPointJoinBuilder builder.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateMultiEditPointJoinBuilder(part: NXOpen.Part) -> MultiEditPointJoinBuilder:
        """
         Creates a @link NXOpen::Join::MultiEditPointJoinBuilder NXOpen::Join::MultiEditPointJoinBuilder@endlink  object. 
         @return builder (@link MultiEditPointJoinBuilder NXOpen.Join.MultiEditPointJoinBuilder@endlink):  MultiEditPointJoinBuilder builder.
        """
        pass
    
    ##  Creates a @link NXOpen::Join::MultiEditPointJoinParametersBuilder NXOpen::Join::MultiEditPointJoinParametersBuilder@endlink  object. 
    ##  @return builder (@link MultiEditPointJoinParametersBuilder NXOpen.Join.MultiEditPointJoinParametersBuilder@endlink):  MultiEditPointJoinBuilder builder.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="parentBuilder"> (@link MultiEditPointJoinBuilder NXOpen.Join.MultiEditPointJoinBuilder@endlink) </param>
    def CreateMultiEditPointJoinParametersBuilder(part: NXOpen.Part, parentBuilder: MultiEditPointJoinBuilder) -> MultiEditPointJoinParametersBuilder:
        """
         Creates a @link NXOpen::Join::MultiEditPointJoinParametersBuilder NXOpen::Join::MultiEditPointJoinParametersBuilder@endlink  object. 
         @return builder (@link MultiEditPointJoinParametersBuilder NXOpen.Join.MultiEditPointJoinParametersBuilder@endlink):  MultiEditPointJoinBuilder builder.
        """
        pass
    
    ##  Creates an @link Join::OverlapBuilder Join::OverlapBuilder@endlink  
    ##  @return builder (@link OverlapBuilder NXOpen.Join.OverlapBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="overlapFeature"> (@link Overlap NXOpen.Join.Overlap@endlink)  @link Join::Overlap Join::Overlap@endlink  to be edited </param>
    def CreateOverlapBuilder(part: NXOpen.Part, overlapFeature: Overlap) -> OverlapBuilder:
        """
         Creates an @link Join::OverlapBuilder Join::OverlapBuilder@endlink  
         @return builder (@link OverlapBuilder NXOpen.Join.OverlapBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Join::PointJoinBuilder Join::PointJoinBuilder@endlink  
    ##  @return builder (@link PointJoinBuilder NXOpen.Join.PointJoinBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="pointJoin"> (@link PointJoin NXOpen.Join.PointJoin@endlink)  @link Join::PointJoin Join::PointJoin@endlink  to be edited </param>
    def CreatePointJoinBuilder(part: NXOpen.Part, pointJoin: PointJoin) -> PointJoinBuilder:
        """
         Creates a @link Join::PointJoinBuilder Join::PointJoinBuilder@endlink  
         @return builder (@link PointJoinBuilder NXOpen.Join.PointJoinBuilder@endlink): .
        """
        pass
    
    ##  Creates an @link Join::PointLayoutBuilder Join::PointLayoutBuilder@endlink  
    ##  @return builder (@link PointLayoutBuilder NXOpen.Join.PointLayoutBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="pointLayoutFeature"> (@link PointLayout NXOpen.Join.PointLayout@endlink)  @link Join::PointLayout Join::PointLayout@endlink  to be edited </param>
    def CreatePointLayoutBuilder(part: NXOpen.Part, pointLayoutFeature: PointLayout) -> PointLayoutBuilder:
        """
         Creates an @link Join::PointLayoutBuilder Join::PointLayoutBuilder@endlink  
         @return builder (@link PointLayoutBuilder NXOpen.Join.PointLayoutBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Join::PreferencesBuilder NXOpen::Join::PreferencesBuilder@endlink  object. 
    ##  @return builder (@link PreferencesBuilder NXOpen.Join.PreferencesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="joinPrefs"> (@link JoinPreferences NXOpen.Join.JoinPreferences@endlink)  The join preferences object will be used in edit </param>
    def CreatePreferencesBuilder(part: NXOpen.Part, joinPrefs: JoinPreferences) -> PreferencesBuilder:
        """
         Creates a @link NXOpen::Join::PreferencesBuilder NXOpen::Join::PreferencesBuilder@endlink  object. 
         @return builder (@link PreferencesBuilder NXOpen.Join.PreferencesBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Join::RulesBasedJoinBulkCreateBuilder NXOpen::Join::RulesBasedJoinBulkCreateBuilder@endlink  object. 
    ##  @return builder (@link RulesBasedJoinBulkCreateBuilder NXOpen.Join.RulesBasedJoinBulkCreateBuilder@endlink):  RulesBasedJoinBulkCreateBuilder builder.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_join_structures (" Automated Structure Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateRulesBasedJoinBulkCreateBuilder(part: NXOpen.Part) -> RulesBasedJoinBulkCreateBuilder:
        """
         Creates a @link NXOpen::Join::RulesBasedJoinBulkCreateBuilder NXOpen::Join::RulesBasedJoinBulkCreateBuilder@endlink  object. 
         @return builder (@link RulesBasedJoinBulkCreateBuilder NXOpen.Join.RulesBasedJoinBulkCreateBuilder@endlink):  RulesBasedJoinBulkCreateBuilder builder.
        """
        pass
    
    ##  Creates a @link NXOpen::Weld::TransformBuilder NXOpen::Weld::TransformBuilder@endlink  object. 
    ##  @return builder (@link TransformBuilder NXOpen.Join.TransformBuilder@endlink):  TransformBuilder builder.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="feature"> (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink)  Feature to be edited </param>
    def CreateTransformBuilder(part: NXOpen.Part, feature: NXOpen.Features.Feature) -> TransformBuilder:
        """
         Creates a @link NXOpen::Weld::TransformBuilder NXOpen::Weld::TransformBuilder@endlink  object. 
         @return builder (@link TransformBuilder NXOpen.Join.TransformBuilder@endlink):  TransformBuilder builder.
        """
        pass
    
    ##  Creates a @link NXOpen::Join::WeldSymbolBuilder NXOpen::Join::WeldSymbolBuilder@endlink  object. 
    ##  @return builder (@link WeldSymbolBuilder NXOpen.Join.WeldSymbolBuilder@endlink):  weld symbol builder.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateWeldSymbolBuilder(part: NXOpen.Part) -> WeldSymbolBuilder:
        """
         Creates a @link NXOpen::Join::WeldSymbolBuilder NXOpen::Join::WeldSymbolBuilder@endlink  object. 
         @return builder (@link WeldSymbolBuilder NXOpen.Join.WeldSymbolBuilder@endlink):  weld symbol builder.
        """
        pass
    
    ##  Executes the Join callback. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="reason"> (@link JoinManager.CallbackReason NXOpen.Join.JoinManager.CallbackReason@endlink) </param>
    ## <param name="nxObjects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def ExecuteCallback(reason: JoinManager.CallbackReason, nxObjects: List[NXOpen.NXObject]) -> None:
        """
         Executes the Join callback. 
        """
        pass
    
    ##  Gets all bodies from assembly, except the visualization bodies of point joins present.
    ##  @return bodies (@link NXOpen.Body List[NXOpen.Body]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    def GetAllNonJoinBodiesInAssembly() -> List[NXOpen.Body]:
        """
         Gets all bodies from assembly, except the visualization bodies of point joins present.
         @return bodies (@link NXOpen.Body List[NXOpen.Body]@endlink): .
        """
        pass
    
    ##  Get curve of @link NXOpen::Weld::WeldJoint NXOpen::Weld::WeldJoint@endlink  from @link Join::CurveJoin Join::CurveJoin@endlink . 
    ##  @return jointCurve (@link NXOpen.Curve NXOpen.Curve@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## <param name="joinCurveFeature"> (@link CurveJoin NXOpen.Join.CurveJoin@endlink) </param>
    def GetJointCurveFromCurveJoin(joinCurveFeature: CurveJoin) -> NXOpen.Curve:
        """
         Get curve of @link NXOpen::Weld::WeldJoint NXOpen::Weld::WeldJoint@endlink  from @link Join::CurveJoin Join::CurveJoin@endlink . 
         @return jointCurve (@link NXOpen.Curve NXOpen.Curve@endlink): .
        """
        pass
    
    ##  Method to show or hide the solid body associated with a @link Join::PointJoin Join::PointJoin@endlink  feature in the work part. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="joinFeatures"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Point Join features. If empty, all feature in work part will be used. </param>
    ## <param name="hideSolids"> (bool)  true to hide solids, false to show solids. </param>
    def HideSolids(joinFeatures: List[NXOpen.NXObject], hideSolids: bool) -> None:
        """
         Method to show or hide the solid body associated with a @link Join::PointJoin Join::PointJoin@endlink  feature in the work part. 
        """
        pass
    
    ##  Load connected parts of @link Join::PointJoin Join::PointJoin@endlink .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link NXOpen::Join::PointJoin::LoadConnectedParts NXOpen::Join::PointJoin::LoadConnectedParts@endlink  instead.  <br> 

    ## License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## <param name="pointJoin"> (@link PointJoin NXOpen.Join.PointJoin@endlink) </param>
    def LoadConnectedParts(pointJoin: PointJoin) -> None:
        """
         Load connected parts of @link Join::PointJoin Join::PointJoin@endlink .
        """
        pass
    
    ##  Removes all the registered callbacks, except those configured in the Application View (APV) file. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def RemoveAllCallbacks() -> None:
        """
         Removes all the registered callbacks, except those configured in the Application View (APV) file. 
        """
        pass
    
    ##  Removes all the callbacks registered for a particular reason. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="reason"> (@link JoinManager.CallbackReason NXOpen.Join.JoinManager.CallbackReason@endlink)  The reason for which you want to remove all the callbacks. </param>
    def RemoveAllCallbacksForReason(reason: JoinManager.CallbackReason) -> None:
        """
         Removes all the callbacks registered for a particular reason. 
        """
        pass
    
    ##  Removes the registered callback. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="callbackMethodId"> (int)  The callback identifier indicating which callback to remove. </param>
    def RemoveCallback(callbackMethodId: int) -> None:
        """
         Removes the registered callback. 
        """
        pass
    
    ##  Renews all of the pre-NX2312 @link Join::PointJoin Join::PointJoin@endlink  features to NX2312 version.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def RenewAllPreNX2312PointJoins(part: NXOpen.Part) -> None:
        """
         Renews all of the pre-NX2312 @link Join::PointJoin Join::PointJoin@endlink  features to NX2312 version.
        """
        pass
    
    ##  Method to turn on or off the show through state for @link Join::PointJoin Join::PointJoin@endlink  features in the work part. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="joinFeatures"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Join features. If empty, all feature in work part will be used. </param>
    ## <param name="showThrough"> (bool)  true to turn show through state on, false to turn off. </param>
    def ShowThrough(joinFeatures: List[NXOpen.NXObject], showThrough: bool) -> None:
        """
         Method to turn on or off the show through state for @link Join::PointJoin Join::PointJoin@endlink  features in the work part. 
        """
        pass
    
    ##  Method to recompute the stackup for the Point Joint Feature. The method creates a build for each feature, commits it, and runs update for all changed features. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="joinFeatures"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Point Join features. </param>
    def UpdateStackup(joinFeatures: List[NXOpen.NXObject]) -> None:
        """
         Method to recompute the stackup for the Point Joint Feature. The method creates a build for each feature, commits it, and runs update for all changed features. 
        """
        pass
    
import NXOpen
import NXOpen.Annotations
##  Create Join Annotation for multiple Join features. This builder's Commit can produce more than one object so 
##         the GetCommittedObjects can be used to get the objects and the order of GetCommittedObject's output array is stable.  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateJoinNoteBuilder  NXOpen::Join::JoinManager::CreateJoinNoteBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## IncludeLeader </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.CustomSymbolScale </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolAspectRatio </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolHeight </term> <description> 
##  
## 25.4 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolLength </term> <description> 
##  
## 25.4 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolPreferences </term> <description> 
##  
## UseCurrent </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolScale </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolSizeMethod </term> <description> 
##  
## ScaleAndAspectRatio </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class JoinNoteBuilder(NXOpen.Builder): 
    """ Create Join Annotation for multiple Join features. This builder's Commit can produce more than one object so 
        the GetCommittedObjects can be used to get the objects and the order of GetCommittedObject's output array is stable. """


    ## Getter for property: (@link NXOpen.Annotations.AssociatedObjectsBuilder NXOpen.Annotations.AssociatedObjectsBuilder@endlink) AssociatedObjects
    ##  Returns the @link NXOpen::Annotations::AssociatedObjectsBuilder NXOpen::Annotations::AssociatedObjectsBuilder@endlink  for the annotation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Annotations.AssociatedObjectsBuilder
    @property
    def AssociatedObjects(self) -> NXOpen.Annotations.AssociatedObjectsBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.AssociatedObjectsBuilder NXOpen.Annotations.AssociatedObjectsBuilder@endlink) AssociatedObjects
         Returns the @link NXOpen::Annotations::AssociatedObjectsBuilder NXOpen::Annotations::AssociatedObjectsBuilder@endlink  for the annotation   
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludeLeader
    ##  Returns the leader option, indicates whether to create a leader   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def IncludeLeader(self) -> bool:
        """
        Getter for property: (bool) IncludeLeader
         Returns the leader option, indicates whether to create a leader   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeLeader

    ##  Returns the leader option, indicates whether to create a leader   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @IncludeLeader.setter
    def IncludeLeader(self, leader: bool):
        """
        Setter for property: (bool) IncludeLeader
         Returns the leader option, indicates whether to create a leader   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Joins
    ##  Returns the join objects to be annotated.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Joins(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Joins
         Returns the join objects to be annotated.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.LeaderBuilder NXOpen.Annotations.LeaderBuilder@endlink) Leader
    ##  Returns the @link NXOpen::Annotations::LeaderBuilder NXOpen::Annotations::LeaderBuilder@endlink  for the annotation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Annotations.LeaderBuilder
    @property
    def Leader(self) -> NXOpen.Annotations.LeaderBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.LeaderBuilder NXOpen.Annotations.LeaderBuilder@endlink) Leader
         Returns the @link NXOpen::Annotations::LeaderBuilder NXOpen::Annotations::LeaderBuilder@endlink  for the annotation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.OriginBuilder NXOpen.Annotations.OriginBuilder@endlink) Origin
    ##  Returns the origin   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Annotations.OriginBuilder
    @property
    def Origin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.OriginBuilder NXOpen.Annotations.OriginBuilder@endlink) Origin
         Returns the origin   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.PlaneBuilder NXOpen.Annotations.PlaneBuilder@endlink) Plane
    ##  Returns the plane builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Annotations.PlaneBuilder
    @property
    def Plane(self) -> NXOpen.Annotations.PlaneBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.PlaneBuilder NXOpen.Annotations.PlaneBuilder@endlink) Plane
         Returns the plane builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.StyleBuilder NXOpen.Annotations.StyleBuilder@endlink) Style
    ##  Returns the style builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Annotations.StyleBuilder
    @property
    def Style(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.StyleBuilder NXOpen.Annotations.StyleBuilder@endlink) Style
         Returns the style builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.TextWithEditControlsBuilder NXOpen.Annotations.TextWithEditControlsBuilder@endlink) Text
    ##  Returns the text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Annotations.TextWithEditControlsBuilder
    @property
    def Text(self) -> NXOpen.Annotations.TextWithEditControlsBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.TextWithEditControlsBuilder NXOpen.Annotations.TextWithEditControlsBuilder@endlink) Text
         Returns the text   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Join::JoinPreferences NXOpen::Join::JoinPreferences@endlink   <br> To create or edit an instance of this class, use @link NXOpen::Join::PreferencesBuilder  NXOpen::Join::PreferencesBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class JoinPreferences(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.Join.JoinPreferences</ja_class> """


    ## Gets a construction layer preference
    ##  @return constructionLayer (int): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def GetConstructionLayer(self) -> int:
        """
        Gets a construction layer preference
         @return constructionLayer (int): .
        """
        pass
    
    ## Gets a fix time stamp preference
    ##  @return fixTimestamp (bool): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def GetFixTimestamp(self) -> bool:
        """
        Gets a fix time stamp preference
         @return fixTimestamp (bool): .
        """
        pass
    
    ## Gets a join group ID seed value preference
    ##  @return groupIdSeedValue (str): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetGroupIdSeedValue(self) -> str:
        """
        Gets a join group ID seed value preference
         @return groupIdSeedValue (str): .
        """
        pass
    
    ## Sets a construction layer preference
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="constructionLayer"> (int) </param>
    def SetConstructionLayer(self, constructionLayer: int) -> None:
        """
        Sets a construction layer preference
        """
        pass
    
    ## Sets a fix time stamp preference
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fixTimestamp"> (bool) </param>
    def SetFixTimestamp(self, fixTimestamp: bool) -> None:
        """
        Sets a fix time stamp preference
        """
        pass
    
    ## Sets a join group ID seed value preference
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="groupIdSeedValue"> (str) </param>
    def SetGroupIdSeedValue(self, groupIdSeedValue: str) -> None:
        """
        Sets a join group ID seed value preference
        """
        pass
    
import NXOpen
##  Represents a MultiEditCurveJoinParametersBuilder class  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateMultiEditCurveJoinParametersBuilder  NXOpen::Join::JoinManager::CreateMultiEditCurveJoinParametersBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class MultiEditCurveJoinParametersBuilder(NXOpen.Builder): 
    """ Represents a MultiEditCurveJoinParametersBuilder class """


    ##  Get the @link NXOpen::Weld::JointExitBuilder NXOpen::Weld::JointExitBuilder@endlink . 
    ##  @return exitBuilder (@link JointExitBuilder NXOpen.Weld.JointExitBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    def GetJointExitBuilder(self, row: int) -> JointExitBuilder:
        """
         Get the @link NXOpen::Weld::JointExitBuilder NXOpen::Weld::JointExitBuilder@endlink . 
         @return exitBuilder (@link JointExitBuilder NXOpen.Weld.JointExitBuilder@endlink): .
        """
        pass
    
    ##  Reset the values of @link NXOpen::Weld::JointExitBuilder NXOpen::Weld::JointExitBuilder@endlink  to the callback values. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="exitBuilder"> (@link JointExitBuilder NXOpen.Weld.JointExitBuilder@endlink) </param>
    def ResetToCallbackValues(self, exitBuilder: JointExitBuilder) -> None:
        """
         Reset the values of @link NXOpen::Weld::JointExitBuilder NXOpen::Weld::JointExitBuilder@endlink  to the callback values. 
        """
        pass
    
import NXOpen
##  Represents a MultiEditPointJoinBuilder class  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateMultiEditPointJoinBuilder  NXOpen::Join::JoinManager::CreateMultiEditPointJoinBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class MultiEditPointJoinBuilder(NXOpen.Builder): 
    """ Represents a MultiEditPointJoinBuilder class """


    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) JoinPoints
    ##  Returns the join points to be edited   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def JoinPoints(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) JoinPoints
         Returns the join points to be edited   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a MultiEditPointJoinParametersBuilder class  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateMultiEditPointJoinParametersBuilder  NXOpen::Join::JoinManager::CreateMultiEditPointJoinParametersBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class MultiEditPointJoinParametersBuilder(NXOpen.Builder): 
    """ Represents a MultiEditPointJoinParametersBuilder class """


    ##  Adds object to be deleted on builder destroy 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="objectTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink)  object to delete </param>
    def AddToDeleteList(self, objectTag: NXOpen.TaggedObject) -> None:
        """
         Adds object to be deleted on builder destroy 
        """
        pass
    
    ##  Creates linked face feature in work part. Linked face feature is reorded before input feature 
    ##  @return linkedFace (@link NXOpen.Face NXOpen.Face@endlink):  newly created linked face .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="face"> (@link NXOpen.Face NXOpen.Face@endlink)  face used to create linked face feature </param>
    ## <param name="feature"> (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink)  feature used to reorder linked face feature </param>
    def CreateLinkedFace(self, face: NXOpen.Face, feature: NXOpen.Features.Feature) -> NXOpen.Face:
        """
         Creates linked face feature in work part. Linked face feature is reorded before input feature 
         @return linkedFace (@link NXOpen.Face NXOpen.Face@endlink):  newly created linked face .
        """
        pass
    
    ##  Load/update hardware for feature corresponding to table row. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of table </param>
    def LoadHardware(self, row: int) -> None:
        """
         Load/update hardware for feature corresponding to table row. 
        """
        pass
    
    ##  Set attachment hardware value for the table cell (row, colummn) 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="column"> (int)  column of cell </param>
    ## <param name="pinName"> (str) </param>
    ## <param name="pinPath"> (str) </param>
    ## <param name="pinFamilyInstanceName"> (str) </param>
    ## <param name="pinTcClassId"> (str) </param>
    ## <param name="pinTcClassInstanceId"> (str) </param>
    def SetAttachmentHardware(self, row: int, column: int, pinName: str, pinPath: str, pinFamilyInstanceName: str, pinTcClassId: str, pinTcClassInstanceId: str) -> None:
        """
         Set attachment hardware value for the table cell (row, colummn) 
        """
        pass
    
    ##  Set a boolean value for the table cell (row, colummn) 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="column"> (int)  column of cell </param>
    ## <param name="value"> (bool)  value of cell </param>
    def SetBooleanValue(self, row: int, column: int, value: bool) -> None:
        """
         Set a boolean value for the table cell (row, colummn) 
        """
        pass
    
    ##  Set a double value for the table cell (row, colummn) 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="column"> (int)  column of cell </param>
    ## <param name="value"> (float)  value of cell </param>
    def SetDoubleValue(self, row: int, column: int, value: float) -> None:
        """
         Set a double value for the table cell (row, colummn) 
        """
        pass
    
    ##  Set a expression value for the table cell (row, colummn) 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="column"> (int)  column of cell </param>
    ## <param name="expTag"> (@link NXOpen.Expression NXOpen.Expression@endlink)  value of cell </param>
    def SetExpressionValue(self, row: int, column: int, expTag: NXOpen.Expression) -> None:
        """
         Set a expression value for the table cell (row, colummn) 
        """
        pass
    
    ##  Sets collector containing curves to define alignment direction 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="collector"> (@link NXOpen.ScCollector NXOpen.ScCollector@endlink)  holds collector for curve </param>
    def SetHardwareOrientationCurve(self, row: int, collector: NXOpen.ScCollector) -> None:
        """
         Sets collector containing curves to define alignment direction 
        """
        pass
    
    ##  Set a hardware pin value for the table cell (row, colummn) 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="column"> (int)  column of cell </param>
    ## <param name="pinName"> (str) </param>
    ## <param name="pinPath"> (str) </param>
    ## <param name="pinFamilyInstanceName"> (str) </param>
    ## <param name="pinTcClassId"> (str) </param>
    ## <param name="pinTcClassInstanceId"> (str) </param>
    def SetHardwarePin(self, row: int, column: int, pinName: str, pinPath: str, pinFamilyInstanceName: str, pinTcClassId: str, pinTcClassInstanceId: str) -> None:
        """
         Set a hardware pin value for the table cell (row, colummn) 
        """
        pass
    
    ##  Set a hardware pin specification value for the table row 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of table </param>
    ## <param name="pinSpecificationName"> (str)  specification name in XML database data source. xhs path in Reuse Library data source. </param>
    ## <param name="pinSpecificationDescriptiveName"> (str)  Descriptive name in Reuse Library data source. Empty otherwise. </param>
    def SetHardwarePinSpecification(self, row: int, pinSpecificationName: str, pinSpecificationDescriptiveName: str) -> None:
        """
         Set a hardware pin specification value for the table row 
        """
        pass
    
    ##  Set a hardware head side parts value for the table cell (row, colummn) 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="column"> (int)  column of cell </param>
    ## <param name="headNames"> (List[str])  List of names </param>
    ## <param name="headPaths"> (List[str])  List of paths </param>
    ## <param name="headFamilyInstanceNames"> (List[str])  List of head family instance names </param>
    ## <param name="headTcClassIds"> (List[str])  List of Teamcenter classification class id </param>
    ## <param name="headTcClassInstanceIds"> (List[str])  List of Teamcenter classification class insatance id  </param>
    def SetHeadSideParts(self, row: int, column: int, headNames: List[str], headPaths: List[str], headFamilyInstanceNames: List[str], headTcClassIds: List[str], headTcClassInstanceIds: List[str]) -> None:
        """
         Set a hardware head side parts value for the table cell (row, colummn) 
        """
        pass
    
    ##  Set an integer value for the table cell (row, colummn) 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="column"> (int)  column of cell </param>
    ## <param name="value"> (int)  value of cell </param>
    def SetIntegerValue(self, row: int, column: int, value: int) -> None:
        """
         Set an integer value for the table cell (row, colummn) 
        """
        pass
    
    ##  Sets the material in the table cell (row, colummn) 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="column"> (int)  column of cell </param>
    ## <param name="material"> (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink)  material tag </param>
    def SetMaterial(self, row: int, column: int, material: NXOpen.PhysicalMaterial) -> None:
        """
         Sets the material in the table cell (row, colummn) 
        """
        pass
    
    ##  Sets collector containing faces for attachment hardware 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="collector"> (@link NXOpen.ScCollector NXOpen.ScCollector@endlink)  holds selection for attachment hardware face </param>
    def SetMatingFace(self, row: int, collector: NXOpen.ScCollector) -> None:
        """
         Sets collector containing faces for attachment hardware 
        """
        pass
    
    ##  Sets collector containing faces to define alignment direction 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="collector"> (@link NXOpen.ScCollector NXOpen.ScCollector@endlink)  holds selection for normal surface </param>
    def SetStackupNormalSurface(self, row: int, collector: NXOpen.ScCollector) -> None:
        """
         Sets collector containing faces to define alignment direction 
        """
        pass
    
    ##  Set a hardware tail side parts value for the table cell (row, colummn) 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="column"> (int)  column of cell </param>
    ## <param name="tailNames"> (List[str])  List of names </param>
    ## <param name="tailPaths"> (List[str])  List of paths </param>
    ## <param name="tailFamilyInstanceNames"> (List[str])  List of tail family instance names </param>
    ## <param name="tailTcClassIds"> (List[str])  List of Teamcenter classification class id </param>
    ## <param name="tailTcClassInstanceIds"> (List[str])  List of Teamcenter classification class insatance id  </param>
    def SetTailSideParts(self, row: int, column: int, tailNames: List[str], tailPaths: List[str], tailFamilyInstanceNames: List[str], tailTcClassIds: List[str], tailTcClassInstanceIds: List[str]) -> None:
        """
         Set a hardware tail side parts value for the table cell (row, colummn) 
        """
        pass
    
    ##  Makes a fixed vector copy of the input vector tag and sets in the table cell (row, colummn) 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of cell </param>
    ## <param name="column"> (int)  column of cell </param>
    ## <param name="vector"> (@link NXOpen.Direction NXOpen.Direction@endlink)  vector tag </param>
    def SetVectorTagValue(self, row: int, column: int, vector: NXOpen.Direction) -> None:
        """
         Makes a fixed vector copy of the input vector tag and sets in the table cell (row, colummn) 
        """
        pass
    
    ##  Unload hardware for feature corresponding to table row. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="row"> (int)  row of table </param>
    def UnloadHardware(self, row: int) -> None:
        """
         Unload hardware for feature corresponding to table row. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Join::OnPathDimension NXOpen::Join::OnPathDimension@endlink .
##     
## 
##   <br>  Created in NX1953.0.0  <br> 

class OnPathDimension(NXOpen.TaggedObject): 
    """ Represents a <ja_class>NXOpen.Join.OnPathDimension</ja_class>.
    """
    pass


import NXOpen
import NXOpen.Features
##  Used to create or edit a @link NXOpen::Join::Overlap NXOpen::Join::Overlap@endlink  feature.  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateOverlapBuilder  NXOpen::Join::JoinManager::CreateOverlapBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MaximumCenterlineWidth </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MinimumFlangeWidth </term> <description> 
##  
## 6.0 (millimeters part), 0.04 (inches part) </description> </item> 
## 
## <item><term> 
##  
## OffsetFromEdgeDistance </term> <description> 
##  
## 6.25 (millimeters part), 0.25 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class OverlapBuilder(NXOpen.Features.FeatureBuilder): 
    """ Used to create or edit a <ja_class>NXOpen.Join.Overlap</ja_class> feature. """


    ##  The type of connect part 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AllUniqueParts</term><description> 
    ##  All connected parts must unique. </description> </item><item><term> 
    ## OnlyOnePart</term><description> 
    ##  All connected parts must be the same.   </description> </item><item><term> 
    ## RepeatedParts</term><description> 
    ##  Connected parts do not need to be unique.  </description> </item></list>
    class ConnectPartTypes(Enum):
        """
        Members Include: <AllUniqueParts> <OnlyOnePart> <RepeatedParts>
        """
        AllUniqueParts: int
        OnlyOnePart: int
        RepeatedParts: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OverlapBuilder.ConnectPartTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The type to specify if reference sheet edges should be automatially selected. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Manual</term><description> 
    ##  User must manually specify the edges on the reference sheet. </description> </item><item><term> 
    ## Automatic</term><description> 
    ##  Automatically determine edges needed to create a centerline or offset curves on a reference sheet. </description> </item></list>
    class GuideCurveCreationTypes(Enum):
        """
        Members Include: <Manual> <Automatic>
        """
        Manual: int
        Automatic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OverlapBuilder.GuideCurveCreationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The type of sheets to create 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Faces</term><description> 
    ##  Construct the overlap sheet from faces. </description> </item><item><term> 
    ## Bodies</term><description> 
    ##  Construct the overlap sheet from bodies. </description> </item></list>
    class InputDataTypes(Enum):
        """
        Members Include: <Faces> <Bodies>
        """
        Faces: int
        Bodies: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OverlapBuilder.InputDataTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The type to specify what faces Reference Sheet should be created on. This is only used when creating a Reference Sheet from bodies. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## TopTarget</term><description> 
    ##  Join Reference Sheet feature is created on the top of the target body. </description> </item><item><term> 
    ## BetweenBodies</term><description> 
    ##  Join Reference Sheet feature is created between the target and tool bodies. </description> </item></list>
    class ReferenceSheetOptionTypes(Enum):
        """
        Members Include: <TopTarget> <BetweenBodies>
        """
        TopTarget: int
        BetweenBodies: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OverlapBuilder.ReferenceSheetOptionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The type of sheets to create 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Overlap</term><description> 
    ##  Overlap </description> </item><item><term> 
    ## Top</term><description> 
    ##  Top     </description> </item></list>
    class ReferenceSheetTypes(Enum):
        """
        Members Include: <Overlap> <Top>
        """
        Overlap: int
        Top: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OverlapBuilder.ReferenceSheetTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link OverlapBuilder.ConnectPartTypes NXOpen.Join.OverlapBuilder.ConnectPartTypes@endlink) ConnectPart
    ##  Returns the option of connecting only one part.  
    ##    If true, only one face set is required.   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return OverlapBuilder.ConnectPartTypes
    @property
    def ConnectPart(self) -> OverlapBuilder.ConnectPartTypes:
        """
        Getter for property: (@link OverlapBuilder.ConnectPartTypes NXOpen.Join.OverlapBuilder.ConnectPartTypes@endlink) ConnectPart
         Returns the option of connecting only one part.  
           If true, only one face set is required.   
         
        """
        pass
    
    ## Setter for property: (@link OverlapBuilder.ConnectPartTypes NXOpen.Join.OverlapBuilder.ConnectPartTypes@endlink) ConnectPart

    ##  Returns the option of connecting only one part.  
    ##    If true, only one face set is required.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ConnectPart.setter
    def ConnectPart(self, connectPart: OverlapBuilder.ConnectPartTypes):
        """
        Setter for property: (@link OverlapBuilder.ConnectPartTypes NXOpen.Join.OverlapBuilder.ConnectPartTypes@endlink) ConnectPart
         Returns the option of connecting only one part.  
           If true, only one face set is required.   
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##  Returns the distance tolerance for constructing the feature.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the feature.  
              
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##  Returns the distance tolerance for constructing the feature.  
    ##       
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the feature.  
              
         
        """
        pass
    
    ## Getter for property: (@link OverlapFaceSetsBuilderList NXOpen.Join.OverlapFaceSetsBuilderList@endlink) FaceSetsList
    ##  Returns the list of face sets    
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return OverlapFaceSetsBuilderList
    @property
    def FaceSetsList(self) -> OverlapFaceSetsBuilderList:
        """
        Getter for property: (@link OverlapFaceSetsBuilderList NXOpen.Join.OverlapFaceSetsBuilderList@endlink) FaceSetsList
         Returns the list of face sets    
            
         
        """
        pass
    
    ## Getter for property: (@link OverlapBuilder.GuideCurveCreationTypes NXOpen.Join.OverlapBuilder.GuideCurveCreationTypes@endlink) GuideCurveCreationType
    ##  Returns the option if sheet edges should be automatically selected.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return OverlapBuilder.GuideCurveCreationTypes
    @property
    def GuideCurveCreationType(self) -> OverlapBuilder.GuideCurveCreationTypes:
        """
        Getter for property: (@link OverlapBuilder.GuideCurveCreationTypes NXOpen.Join.OverlapBuilder.GuideCurveCreationTypes@endlink) GuideCurveCreationType
         Returns the option if sheet edges should be automatically selected.  
             
         
        """
        pass
    
    ## Setter for property: (@link OverlapBuilder.GuideCurveCreationTypes NXOpen.Join.OverlapBuilder.GuideCurveCreationTypes@endlink) GuideCurveCreationType

    ##  Returns the option if sheet edges should be automatically selected.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @GuideCurveCreationType.setter
    def GuideCurveCreationType(self, guideCurveCreationType: OverlapBuilder.GuideCurveCreationTypes):
        """
        Setter for property: (@link OverlapBuilder.GuideCurveCreationTypes NXOpen.Join.OverlapBuilder.GuideCurveCreationTypes@endlink) GuideCurveCreationType
         Returns the option if sheet edges should be automatically selected.  
             
         
        """
        pass
    
    ## Getter for property: (@link OverlapGuideBuilderList NXOpen.Join.OverlapGuideBuilderList@endlink) GuideCurvesList
    ##  Returns the list of guide curves   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return OverlapGuideBuilderList
    @property
    def GuideCurvesList(self) -> OverlapGuideBuilderList:
        """
        Getter for property: (@link OverlapGuideBuilderList NXOpen.Join.OverlapGuideBuilderList@endlink) GuideCurvesList
         Returns the list of guide curves   
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumBendRadius
    ##  Returns the radius value for which faces will be excluded from the reference sheet construction.  
    ##    Processing time will increase when smaller values are used.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def MaximumBendRadius(self) -> float:
        """
        Getter for property: (float) MaximumBendRadius
         Returns the radius value for which faces will be excluded from the reference sheet construction.  
           Processing time will increase when smaller values are used.   
         
        """
        pass
    
    ## Setter for property: (float) MaximumBendRadius

    ##  Returns the radius value for which faces will be excluded from the reference sheet construction.  
    ##    Processing time will increase when smaller values are used.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @MaximumBendRadius.setter
    def MaximumBendRadius(self, maximumBendRadius: float):
        """
        Setter for property: (float) MaximumBendRadius
         Returns the radius value for which faces will be excluded from the reference sheet construction.  
           Processing time will increase when smaller values are used.   
         
        """
        pass
    
    ## Getter for property: (float) MaximumCenterlineWidth
    ##  Returns the maximum centerline width.  
    ##    Points will be created using the centerline method
    ##         if the smallest width is less than this value. If greater, points will be
    ##         created using the offset from edge method.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def MaximumCenterlineWidth(self) -> float:
        """
        Getter for property: (float) MaximumCenterlineWidth
         Returns the maximum centerline width.  
           Points will be created using the centerline method
                if the smallest width is less than this value. If greater, points will be
                created using the offset from edge method.   
         
        """
        pass
    
    ## Setter for property: (float) MaximumCenterlineWidth

    ##  Returns the maximum centerline width.  
    ##    Points will be created using the centerline method
    ##         if the smallest width is less than this value. If greater, points will be
    ##         created using the offset from edge method.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MaximumCenterlineWidth.setter
    def MaximumCenterlineWidth(self, maximumCenterlineWidth: float):
        """
        Setter for property: (float) MaximumCenterlineWidth
         Returns the maximum centerline width.  
           Points will be created using the centerline method
                if the smallest width is less than this value. If greater, points will be
                created using the offset from edge method.   
         
        """
        pass
    
    ## Getter for property: (float) MaximumGapBetweenBodies
    ##  Returns the maximum gap expected when joining bodies.  
    ##    This value should not be bigger than expected gaps between bodies.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def MaximumGapBetweenBodies(self) -> float:
        """
        Getter for property: (float) MaximumGapBetweenBodies
         Returns the maximum gap expected when joining bodies.  
           This value should not be bigger than expected gaps between bodies.   
         
        """
        pass
    
    ## Setter for property: (float) MaximumGapBetweenBodies

    ##  Returns the maximum gap expected when joining bodies.  
    ##    This value should not be bigger than expected gaps between bodies.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @MaximumGapBetweenBodies.setter
    def MaximumGapBetweenBodies(self, maximumGapBetweenBodies: float):
        """
        Setter for property: (float) MaximumGapBetweenBodies
         Returns the maximum gap expected when joining bodies.  
           This value should not be bigger than expected gaps between bodies.   
         
        """
        pass
    
    ## Getter for property: (float) MinimumFlangeWidth
    ##  Returns the radius value for which faces will be excluded from the reference sheet construction.  
    ##    Processing time will increase when smaller values are used.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def MinimumFlangeWidth(self) -> float:
        """
        Getter for property: (float) MinimumFlangeWidth
         Returns the radius value for which faces will be excluded from the reference sheet construction.  
           Processing time will increase when smaller values are used.   
         
        """
        pass
    
    ## Setter for property: (float) MinimumFlangeWidth

    ##  Returns the radius value for which faces will be excluded from the reference sheet construction.  
    ##    Processing time will increase when smaller values are used.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MinimumFlangeWidth.setter
    def MinimumFlangeWidth(self, minimumFlangeWidth: float):
        """
        Setter for property: (float) MinimumFlangeWidth
         Returns the radius value for which faces will be excluded from the reference sheet construction.  
           Processing time will increase when smaller values are used.   
         
        """
        pass
    
    ## Getter for property: (bool) MoveReferenceSheetToConstructionLayer
    ##  Returns the value to indidate if the output sheet bodies of this feature should be moved to the construction layer.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def MoveReferenceSheetToConstructionLayer(self) -> bool:
        """
        Getter for property: (bool) MoveReferenceSheetToConstructionLayer
         Returns the value to indidate if the output sheet bodies of this feature should be moved to the construction layer.  
             
         
        """
        pass
    
    ## Setter for property: (bool) MoveReferenceSheetToConstructionLayer

    ##  Returns the value to indidate if the output sheet bodies of this feature should be moved to the construction layer.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @MoveReferenceSheetToConstructionLayer.setter
    def MoveReferenceSheetToConstructionLayer(self, moveReferenceSheetToConstructionLayer: bool):
        """
        Setter for property: (bool) MoveReferenceSheetToConstructionLayer
         Returns the value to indidate if the output sheet bodies of this feature should be moved to the construction layer.  
             
         
        """
        pass
    
    ## Getter for property: (float) OffsetFromEdgeDistance
    ##  Returns the offset distance from edge   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def OffsetFromEdgeDistance(self) -> float:
        """
        Getter for property: (float) OffsetFromEdgeDistance
         Returns the offset distance from edge   
            
         
        """
        pass
    
    ## Setter for property: (float) OffsetFromEdgeDistance

    ##  Returns the offset distance from edge   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @OffsetFromEdgeDistance.setter
    def OffsetFromEdgeDistance(self, offsetFromEdgeDistance: float):
        """
        Setter for property: (float) OffsetFromEdgeDistance
         Returns the offset distance from edge   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) OtherBodies
    ##  Returns the other bodies that are connected tot he top body.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def OtherBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) OtherBodies
         Returns the other bodies that are connected tot he top body.  
             
         
        """
        pass
    
    ## Getter for property: (@link OverlapBuilder.ReferenceSheetOptionTypes NXOpen.Join.OverlapBuilder.ReferenceSheetOptionTypes@endlink) ReferenceSheetOption
    ##  Returns the option to control where the overlap sheet will be created.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return OverlapBuilder.ReferenceSheetOptionTypes
    @property
    def ReferenceSheetOption(self) -> OverlapBuilder.ReferenceSheetOptionTypes:
        """
        Getter for property: (@link OverlapBuilder.ReferenceSheetOptionTypes NXOpen.Join.OverlapBuilder.ReferenceSheetOptionTypes@endlink) ReferenceSheetOption
         Returns the option to control where the overlap sheet will be created.  
             
         
        """
        pass
    
    ## Setter for property: (@link OverlapBuilder.ReferenceSheetOptionTypes NXOpen.Join.OverlapBuilder.ReferenceSheetOptionTypes@endlink) ReferenceSheetOption

    ##  Returns the option to control where the overlap sheet will be created.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ReferenceSheetOption.setter
    def ReferenceSheetOption(self, sheetLocation: OverlapBuilder.ReferenceSheetOptionTypes):
        """
        Setter for property: (@link OverlapBuilder.ReferenceSheetOptionTypes NXOpen.Join.OverlapBuilder.ReferenceSheetOptionTypes@endlink) ReferenceSheetOption
         Returns the option to control where the overlap sheet will be created.  
             
         
        """
        pass
    
    ## Getter for property: (@link OverlapBuilder.ReferenceSheetTypes NXOpen.Join.OverlapBuilder.ReferenceSheetTypes@endlink) ReferenceSheetType
    ##  Returns the type of reference sheet  
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return OverlapBuilder.ReferenceSheetTypes
    @property
    def ReferenceSheetType(self) -> OverlapBuilder.ReferenceSheetTypes:
        """
        Getter for property: (@link OverlapBuilder.ReferenceSheetTypes NXOpen.Join.OverlapBuilder.ReferenceSheetTypes@endlink) ReferenceSheetType
         Returns the type of reference sheet  
            
         
        """
        pass
    
    ## Setter for property: (@link OverlapBuilder.ReferenceSheetTypes NXOpen.Join.OverlapBuilder.ReferenceSheetTypes@endlink) ReferenceSheetType

    ##  Returns the type of reference sheet  
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ReferenceSheetType.setter
    def ReferenceSheetType(self, refSheet: OverlapBuilder.ReferenceSheetTypes):
        """
        Setter for property: (@link OverlapBuilder.ReferenceSheetTypes NXOpen.Join.OverlapBuilder.ReferenceSheetTypes@endlink) ReferenceSheetType
         Returns the type of reference sheet  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) TopBodies
    ##  Returns the top body that other bodies will be connected to.  
    ##     Reference sheet faces will be on the outside of this body.   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def TopBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) TopBodies
         Returns the top body that other bodies will be connected to.  
            Reference sheet faces will be on the outside of this body.   
         
        """
        pass
    
    ## Getter for property: (@link OverlapBuilder.InputDataTypes NXOpen.Join.OverlapBuilder.InputDataTypes@endlink) Type
    ##  Returns the input data type represented by @link NXOpen::Join::OverlapBuilder::InputDataTypes NXOpen::Join::OverlapBuilder::InputDataTypes@endlink  to create the reference sheet.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return OverlapBuilder.InputDataTypes
    @property
    def Type(self) -> OverlapBuilder.InputDataTypes:
        """
        Getter for property: (@link OverlapBuilder.InputDataTypes NXOpen.Join.OverlapBuilder.InputDataTypes@endlink) Type
         Returns the input data type represented by @link NXOpen::Join::OverlapBuilder::InputDataTypes NXOpen::Join::OverlapBuilder::InputDataTypes@endlink  to create the reference sheet.  
             
         
        """
        pass
    
    ## Setter for property: (@link OverlapBuilder.InputDataTypes NXOpen.Join.OverlapBuilder.InputDataTypes@endlink) Type

    ##  Returns the input data type represented by @link NXOpen::Join::OverlapBuilder::InputDataTypes NXOpen::Join::OverlapBuilder::InputDataTypes@endlink  to create the reference sheet.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Type.setter
    def Type(self, type: OverlapBuilder.InputDataTypes):
        """
        Setter for property: (@link OverlapBuilder.InputDataTypes NXOpen.Join.OverlapBuilder.InputDataTypes@endlink) Type
         Returns the input data type represented by @link NXOpen::Join::OverlapBuilder::InputDataTypes NXOpen::Join::OverlapBuilder::InputDataTypes@endlink  to create the reference sheet.  
             
         
        """
        pass
    
    ##  Move the Reference Sheet to work layer, and unlink from grouping feature. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def MoveReferenceSheet(self) -> None:
        """
         Move the Reference Sheet to work layer, and unlink from grouping feature. 
        """
        pass
    
    ##  Creates a @link NXOpen::Join::OverlapFaceSetsBuilder NXOpen::Join::OverlapFaceSetsBuilder@endlink  object. 
    ##  @return newfaceSetsBuilder (@link OverlapFaceSetsBuilder NXOpen.Join.OverlapFaceSetsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def NewFaceSets(self) -> OverlapFaceSetsBuilder:
        """
         Creates a @link NXOpen::Join::OverlapFaceSetsBuilder NXOpen::Join::OverlapFaceSetsBuilder@endlink  object. 
         @return newfaceSetsBuilder (@link OverlapFaceSetsBuilder NXOpen.Join.OverlapFaceSetsBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Join::OverlapGuideBuilder NXOpen::Join::OverlapGuideBuilder@endlink  object. 
    ##  @return newGuideBuilder (@link OverlapGuideBuilder NXOpen.Join.OverlapGuideBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def NewGuide(self) -> OverlapGuideBuilder:
        """
         Creates a @link NXOpen::Join::OverlapGuideBuilder NXOpen::Join::OverlapGuideBuilder@endlink  object. 
         @return newGuideBuilder (@link OverlapGuideBuilder NXOpen.Join.OverlapGuideBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class OverlapFaceSetsBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##  Returns the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapFaceSetsBuilderList NXOpen.Join.OverlapFaceSetsBuilderList@endlink) </param>
    ## <param name="objects"> (@link OverlapFaceSetsBuilder List[NXOpen.Join.OverlapFaceSetsBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[OverlapFaceSetsBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapFaceSetsBuilderList NXOpen.Join.OverlapFaceSetsBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link OverlapFaceSetsBuilder NXOpen.Join.OverlapFaceSetsBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: OverlapFaceSetsBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapFaceSetsBuilderList NXOpen.Join.OverlapFaceSetsBuilderList@endlink) </param>
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="delete_idx"> (int)  index of item to be deleted </param>
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapFaceSetsBuilderList NXOpen.Join.OverlapFaceSetsBuilderList@endlink) </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the objects when removing them </param>
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapFaceSetsBuilderList NXOpen.Join.OverlapFaceSetsBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapFaceSetsBuilderList NXOpen.Join.OverlapFaceSetsBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapFaceSetsBuilderList NXOpen.Join.OverlapFaceSetsBuilderList@endlink) </param>
    ## <param name="obj"> (@link OverlapFaceSetsBuilder NXOpen.Join.OverlapFaceSetsBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: OverlapFaceSetsBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapFaceSetsBuilderList NXOpen.Join.OverlapFaceSetsBuilderList@endlink) </param>
    ## <param name="obj"> (@link OverlapFaceSetsBuilder NXOpen.Join.OverlapFaceSetsBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: OverlapFaceSetsBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="obj"> (@link OverlapFaceSetsBuilder NXOpen.Join.OverlapFaceSetsBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: OverlapFaceSetsBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link OverlapFaceSetsBuilder NXOpen.Join.OverlapFaceSetsBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> OverlapFaceSetsBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link OverlapFaceSetsBuilder NXOpen.Join.OverlapFaceSetsBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link OverlapFaceSetsBuilder List[NXOpen.Join.OverlapFaceSetsBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[OverlapFaceSetsBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link OverlapFaceSetsBuilder List[NXOpen.Join.OverlapFaceSetsBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link OverlapFaceSetsBuilder NXOpen.Join.OverlapFaceSetsBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: OverlapFaceSetsBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link OverlapFaceSetsBuilder List[NXOpen.Join.OverlapFaceSetsBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[OverlapFaceSetsBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapFaceSetsBuilderList NXOpen.Join.OverlapFaceSetsBuilderList@endlink) </param>
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapFaceSetsBuilderList NXOpen.Join.OverlapFaceSetsBuilderList@endlink) </param>
    ## <param name="object1"> (@link OverlapFaceSetsBuilder NXOpen.Join.OverlapFaceSetsBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link OverlapFaceSetsBuilder NXOpen.Join.OverlapFaceSetsBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: OverlapFaceSetsBuilder, object2: OverlapFaceSetsBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Used to define the faces to create create that will be used to create a @link NXOpen::Join::Overlap NXOpen::Join::Overlap@endlink  feature.  <br> To create a new instance of this class, use @link NXOpen::Join::OverlapBuilder::NewFaceSets  NXOpen::Join::OverlapBuilder::NewFaceSets @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class OverlapFaceSetsBuilder(NXOpen.TaggedObject): 
    """ Used to define the faces to create create that will be used to create a <ja_class>NXOpen.Join.Overlap</ja_class> feature. """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceSelect
    ##  Returns the selected face collector   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceSelect(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceSelect
         Returns the selected face collector   
            
         
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class OverlapGuideBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##  Returns the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapGuideBuilderList NXOpen.Join.OverlapGuideBuilderList@endlink) </param>
    ## <param name="objects"> (@link OverlapGuideBuilder List[NXOpen.Join.OverlapGuideBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[OverlapGuideBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapGuideBuilderList NXOpen.Join.OverlapGuideBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link OverlapGuideBuilder NXOpen.Join.OverlapGuideBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: OverlapGuideBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapGuideBuilderList NXOpen.Join.OverlapGuideBuilderList@endlink) </param>
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="delete_idx"> (int)  index of item to be deleted </param>
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapGuideBuilderList NXOpen.Join.OverlapGuideBuilderList@endlink) </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the objects when removing them </param>
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapGuideBuilderList NXOpen.Join.OverlapGuideBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapGuideBuilderList NXOpen.Join.OverlapGuideBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapGuideBuilderList NXOpen.Join.OverlapGuideBuilderList@endlink) </param>
    ## <param name="obj"> (@link OverlapGuideBuilder NXOpen.Join.OverlapGuideBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: OverlapGuideBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapGuideBuilderList NXOpen.Join.OverlapGuideBuilderList@endlink) </param>
    ## <param name="obj"> (@link OverlapGuideBuilder NXOpen.Join.OverlapGuideBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: OverlapGuideBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="obj"> (@link OverlapGuideBuilder NXOpen.Join.OverlapGuideBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: OverlapGuideBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link OverlapGuideBuilder NXOpen.Join.OverlapGuideBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> OverlapGuideBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link OverlapGuideBuilder NXOpen.Join.OverlapGuideBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link OverlapGuideBuilder List[NXOpen.Join.OverlapGuideBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[OverlapGuideBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link OverlapGuideBuilder List[NXOpen.Join.OverlapGuideBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link OverlapGuideBuilder NXOpen.Join.OverlapGuideBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: OverlapGuideBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link OverlapGuideBuilder List[NXOpen.Join.OverlapGuideBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[OverlapGuideBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapGuideBuilderList NXOpen.Join.OverlapGuideBuilderList@endlink) </param>
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link OverlapGuideBuilderList NXOpen.Join.OverlapGuideBuilderList@endlink) </param>
    ## <param name="object1"> (@link OverlapGuideBuilder NXOpen.Join.OverlapGuideBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link OverlapGuideBuilder NXOpen.Join.OverlapGuideBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: OverlapGuideBuilder, object2: OverlapGuideBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Used to create or edit a guide curve in the @link NXOpen::Join::Overlap NXOpen::Join::Overlap@endlink  feature.   <br> To create a new instance of this class, use @link NXOpen::Join::OverlapBuilder::NewGuide  NXOpen::Join::OverlapBuilder::NewGuide @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class OverlapGuideBuilder(NXOpen.TaggedObject): 
    """ Used to create or edit a guide curve in the <ja_class>NXOpen.Join.Overlap</ja_class> feature.  """


    ##  The type of guide curve 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CenterLine</term><description> 
    ##  Centerline </description> </item><item><term> 
    ## OffsetFromEdge</term><description> 
    ##  Offset from Edge </description> </item><item><term> 
    ## ExistingCurve</term><description> 
    ##  Existing Curve </description> </item><item><term> 
    ## NominalDiameter</term><description> 
    ##  Nominal diameter. Uses @link Diameter Diameter@endlink , @link Multiplier Multiplier@endlink , and @link Allowance Allowance@endlink  to define the offset distance. </description> </item></list>
    class Method(Enum):
        """
        Members Include: <CenterLine> <OffsetFromEdge> <ExistingCurve> <NominalDiameter>
        """
        CenterLine: int
        OffsetFromEdge: int
        ExistingCurve: int
        NominalDiameter: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OverlapGuideBuilder.Method:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Allowance
    ##  Returns the design allowance.  
    ##    Used with @link OverlapGuideBuilder::MethodNominalDiameter OverlapGuideBuilder::MethodNominalDiameter@endlink . See @link Diameter Diameter@endlink  expression.   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Allowance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Allowance
         Returns the design allowance.  
           Used with @link OverlapGuideBuilder::MethodNominalDiameter OverlapGuideBuilder::MethodNominalDiameter@endlink . See @link Diameter Diameter@endlink  expression.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##  Returns the nominal diameter.  
    ##     Used with @link OverlapGuideBuilder::MethodNominalDiameter OverlapGuideBuilder::MethodNominalDiameter@endlink .  This value times @link Multiplier Multiplier@endlink  plus @link Allowance Allowance@endlink  defines the offset distance.   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
         Returns the nominal diameter.  
            Used with @link OverlapGuideBuilder::MethodNominalDiameter OverlapGuideBuilder::MethodNominalDiameter@endlink .  This value times @link Multiplier Multiplier@endlink  plus @link Allowance Allowance@endlink  defines the offset distance.   
         
        """
        pass
    
    ## Getter for property: (bool) ExtendOffset
    ##  Returns the flag indicating if the guide curve should be extened to the nearest face boundary.  
    ##    Used with Offset From Edge, and Nominal Diameter.   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def ExtendOffset(self) -> bool:
        """
        Getter for property: (bool) ExtendOffset
         Returns the flag indicating if the guide curve should be extened to the nearest face boundary.  
           Used with Offset From Edge, and Nominal Diameter.   
         
        """
        pass
    
    ## Setter for property: (bool) ExtendOffset

    ##  Returns the flag indicating if the guide curve should be extened to the nearest face boundary.  
    ##    Used with Offset From Edge, and Nominal Diameter.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ExtendOffset.setter
    def ExtendOffset(self, extendOffset: bool):
        """
        Setter for property: (bool) ExtendOffset
         Returns the flag indicating if the guide curve should be extened to the nearest face boundary.  
           Used with Offset From Edge, and Nominal Diameter.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) GuideCurve
    ##  Returns the guide curves created from the specified inputs.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def GuideCurve(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) GuideCurve
         Returns the guide curves created from the specified inputs.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Section NXOpen.Section@endlink) GuideCurve

    ##  Returns the guide curves created from the specified inputs.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @GuideCurve.setter
    def GuideCurve(self, guide: NXOpen.Section):
        """
        Setter for property: (@link NXOpen.Section NXOpen.Section@endlink) GuideCurve
         Returns the guide curves created from the specified inputs.  
             
         
        """
        pass
    
    ## Getter for property: (@link OverlapGuideBuilder.Method NXOpen.Join.OverlapGuideBuilder.Method@endlink) MethodOption
    ##  Returns the method option is used to define how the guide curves will be created.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return OverlapGuideBuilder.Method
    @property
    def MethodOption(self) -> OverlapGuideBuilder.Method:
        """
        Getter for property: (@link OverlapGuideBuilder.Method NXOpen.Join.OverlapGuideBuilder.Method@endlink) MethodOption
         Returns the method option is used to define how the guide curves will be created.  
             
         
        """
        pass
    
    ## Setter for property: (@link OverlapGuideBuilder.Method NXOpen.Join.OverlapGuideBuilder.Method@endlink) MethodOption

    ##  Returns the method option is used to define how the guide curves will be created.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @MethodOption.setter
    def MethodOption(self, methodOption: OverlapGuideBuilder.Method):
        """
        Setter for property: (@link OverlapGuideBuilder.Method NXOpen.Join.OverlapGuideBuilder.Method@endlink) MethodOption
         Returns the method option is used to define how the guide curves will be created.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Multiplier
    ##  Returns the diameter multiplier.  
    ##    Used with @link OverlapGuideBuilder::MethodNominalDiameter OverlapGuideBuilder::MethodNominalDiameter@endlink . See @link Diameter Diameter@endlink .   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Multiplier(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Multiplier
         Returns the diameter multiplier.  
           Used with @link OverlapGuideBuilder::MethodNominalDiameter OverlapGuideBuilder::MethodNominalDiameter@endlink . See @link Diameter Diameter@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
    ##  Returns the offset distance used with the @link OverlapGuideBuilder::MethodOffsetFromEdge OverlapGuideBuilder::MethodOffsetFromEdge@endlink     
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
         Returns the offset distance used with the @link OverlapGuideBuilder::MethodOffsetFromEdge OverlapGuideBuilder::MethodOffsetFromEdge@endlink     
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section1
    ##  Returns the first section used to create a centerline with.  
    ##    Used with @link OverlapGuideBuilder::MethodCenterLine OverlapGuideBuilder::MethodCenterLine@endlink .   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def Section1(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section1
         Returns the first section used to create a centerline with.  
           Used with @link OverlapGuideBuilder::MethodCenterLine OverlapGuideBuilder::MethodCenterLine@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section2
    ##  Returns the second section used to create a centerline with.  
    ##    Used with @link OverlapGuideBuilder::MethodCenterLine OverlapGuideBuilder::MethodCenterLine@endlink .   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def Section2(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section2
         Returns the second section used to create a centerline with.  
           Used with @link OverlapGuideBuilder::MethodCenterLine OverlapGuideBuilder::MethodCenterLine@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section3
    ##  Returns the section used specify the edges on the reference sheet to offset from.  
    ##    Used with @link OverlapGuideBuilder::MethodOffsetFromEdge OverlapGuideBuilder::MethodOffsetFromEdge@endlink  and @link OverlapGuideBuilder::MethodNominalDiameter OverlapGuideBuilder::MethodNominalDiameter@endlink .   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def Section3(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section3
         Returns the section used specify the edges on the reference sheet to offset from.  
           Used with @link OverlapGuideBuilder::MethodOffsetFromEdge OverlapGuideBuilder::MethodOffsetFromEdge@endlink  and @link OverlapGuideBuilder::MethodNominalDiameter OverlapGuideBuilder::MethodNominalDiameter@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section4
    ##  Returns the section used to specify curves to project to the reference sheet.  
    ##     Used with @link OverlapGuideBuilder::MethodExistingCurve OverlapGuideBuilder::MethodExistingCurve@endlink .    
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def Section4(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section4
         Returns the section used to specify curves to project to the reference sheet.  
            Used with @link OverlapGuideBuilder::MethodExistingCurve OverlapGuideBuilder::MethodExistingCurve@endlink .    
         
        """
        pass
    
    ##  Creates the guide curves defined by the method and sections. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def CreateGuideCurves(self) -> None:
        """
         Creates the guide curves defined by the method and sections. 
        """
        pass
    
    ##  Gets the created curves. The guide curves must exist before calling this method. 
    ##  @return A tuple consisting of (guideCurves, instanceGuideCurves). 
    ##  - guideCurves is: @link NXOpen.ICurve List[NXOpen.ICurve]@endlink.The array of curves.
    ##  - instanceGuideCurves is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink.The array of component curve instances. If there is not an assembly, then this will match the prototype curve. .

    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetGuideCurves(self) -> Tuple[List[NXOpen.ICurve], List[NXOpen.NXObject]]:
        """
         Gets the created curves. The guide curves must exist before calling this method. 
         @return A tuple consisting of (guideCurves, instanceGuideCurves). 
         - guideCurves is: @link NXOpen.ICurve List[NXOpen.ICurve]@endlink.The array of curves.
         - instanceGuideCurves is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink.The array of component curve instances. If there is not an assembly, then this will match the prototype curve. .

        """
        pass
    
    ##  Gets the mid point of the section used for creating the offset curves, and a vector indicating the offset direction. 
    ##  @return A tuple consisting of (midPoint, direction). 
    ##  - midPoint is: @link NXOpen.Point3d NXOpen.Point3d@endlink. The mid point of the section used for offsetting the curve. .
    ##  - direction is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. The vector direction that points to the interior of the reference sheet. .

    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetOffsetDirection(self) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d]:
        """
         Gets the mid point of the section used for creating the offset curves, and a vector indicating the offset direction. 
         @return A tuple consisting of (midPoint, direction). 
         - midPoint is: @link NXOpen.Point3d NXOpen.Point3d@endlink. The mid point of the section used for offsetting the curve. .
         - direction is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. The vector direction that points to the interior of the reference sheet. .

        """
        pass
    
import NXOpen.Features
##  Represents a Join.Overlap Feature.  <br> To create or edit an instance of this class, use @link NXOpen::Join::OverlapBuilder  NXOpen::Join::OverlapBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Overlap(NXOpen.Features.Feature): 
    """ Represents a Join.Overlap Feature. """


    ##  Retrieves a Reference Sheet from a Join.Overlap Feature. 
    ##  @return sheetFrec (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def GetReferenceSheet(self) -> NXOpen.Features.Feature:
        """
         Retrieves a Reference Sheet from a Join.Overlap Feature. 
         @return sheetFrec (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink): .
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Join::PointJoin NXOpen::Join::PointJoin@endlink  builder.
##      <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreatePointJoinBuilder  NXOpen::Join::JoinManager::CreatePointJoinBuilder @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class PointJoinBuilder(JoinBuilder): 
    """
    Represents a <ja_class>NXOpen.Join.PointJoin</ja_class> builder.
    """


    ##  the hole type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Simple</term><description> 
    ## </description> </item><item><term> 
    ## Counterbored</term><description> 
    ## </description> </item><item><term> 
    ## Countersunk</term><description> 
    ## </description> </item></list>
    class HoleTypes(Enum):
        """
        Members Include: <Simple> <Counterbored> <Countersunk>
        """
        Simple: int
        Counterbored: int
        Countersunk: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointJoinBuilder.HoleTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the stackup alignment type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NormalClosestFace</term><description> 
    ## </description> </item><item><term> 
    ## NormalSelectedFace</term><description> 
    ## </description> </item><item><term> 
    ## AlongVector</term><description> 
    ## </description> </item></list>
    class StackupAlignmentTypes(Enum):
        """
        Members Include: <NormalClosestFace> <NormalSelectedFace> <AlongVector>
        """
        NormalClosestFace: int
        NormalSelectedFace: int
        AlongVector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointJoinBuilder.StackupAlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the visualization geometry type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Sphere</term><description> 
    ## </description> </item><item><term> 
    ## Cylinder</term><description> 
    ## </description> </item><item><term> 
    ## Cone</term><description> 
    ## </description> </item><item><term> 
    ## Prism</term><description> 
    ## </description> </item></list>
    class VisualizationGeometryType(Enum):
        """
        Members Include: <Sphere> <Cylinder> <Cone> <Prism>
        """
        Sphere: int
        Cylinder: int
        Cone: int
        Prism: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointJoinBuilder.VisualizationGeometryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CreateCsys
    ##  Returns the indication to create a @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def CreateCsys(self) -> bool:
        """
        Getter for property: (bool) CreateCsys
         Returns the indication to create a @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink    
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateCsys

    ##  Returns the indication to create a @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink    
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @CreateCsys.setter
    def CreateCsys(self, createCsys: bool):
        """
        Setter for property: (bool) CreateCsys
         Returns the indication to create a @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) CsysYDirection
    ##  Returns  the indication to specify the y direction of the @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink     
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def CsysYDirection(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) CsysYDirection
         Returns  the indication to specify the y direction of the @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink     
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) CsysYDirection

    ##  Returns  the indication to specify the y direction of the @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink     
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @CsysYDirection.setter
    def CsysYDirection(self, csysYDirection: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) CsysYDirection
         Returns  the indication to specify the y direction of the @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink     
            
         
        """
        pass
    
    ## Getter for property: (bool) FlipCsysDirection
    ##  Returns the indication to reverse the z direction of the @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink     
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def FlipCsysDirection(self) -> bool:
        """
        Getter for property: (bool) FlipCsysDirection
         Returns the indication to reverse the z direction of the @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink     
            
         
        """
        pass
    
    ## Setter for property: (bool) FlipCsysDirection

    ##  Returns the indication to reverse the z direction of the @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink     
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @FlipCsysDirection.setter
    def FlipCsysDirection(self, flipCsysDirection: bool):
        """
        Setter for property: (bool) FlipCsysDirection
         Returns the indication to reverse the z direction of the @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink     
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HardwareAlignmentAngle
    ##  Returns the alignment angle for rotation of hardware   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HardwareAlignmentAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HardwareAlignmentAngle
         Returns the alignment angle for rotation of hardware   
            
         
        """
        pass
    
    ## Getter for property: (bool) HardwareLoad
    ##  Returns the load hardware flag.  
    ##    If true, hardware should be loaded into assembly.   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def HardwareLoad(self) -> bool:
        """
        Getter for property: (bool) HardwareLoad
         Returns the load hardware flag.  
           If true, hardware should be loaded into assembly.   
         
        """
        pass
    
    ## Setter for property: (bool) HardwareLoad

    ##  Returns the load hardware flag.  
    ##    If true, hardware should be loaded into assembly.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @HardwareLoad.setter
    def HardwareLoad(self, status: bool):
        """
        Setter for property: (bool) HardwareLoad
         Returns the load hardware flag.  
           If true, hardware should be loaded into assembly.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) HardwareOrientationCurve
    ##  Returns the orientation curves along which the hardware can be oriented   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def HardwareOrientationCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) HardwareOrientationCurve
         Returns the orientation curves along which the hardware can be oriented   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleCounterBoreDepth
    ##  Returns the Counterbore depth   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HoleCounterBoreDepth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleCounterBoreDepth
         Returns the Counterbore depth   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleCounterBoreDiameter
    ##  Returns the Counterbore diameter   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HoleCounterBoreDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleCounterBoreDiameter
         Returns the Counterbore diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleCounterSinkAngle
    ##  Returns the Countersink angle   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HoleCounterSinkAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleCounterSinkAngle
         Returns the Countersink angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleCounterSinkDiameter
    ##  Returns the Countersink diameter   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HoleCounterSinkDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleCounterSinkDiameter
         Returns the Countersink diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleCounterSinkSubflush
    ##  Returns the Countersink sub-flush depth value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HoleCounterSinkSubflush(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleCounterSinkSubflush
         Returns the Countersink sub-flush depth value   
            
         
        """
        pass
    
    ## Getter for property: (bool) HoleCreate
    ##  Returns the hole creation status.  
    ##    If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::Join::JoinManager::CreateJoinHoleBuilder NXOpen::Join::JoinManager::CreateJoinHoleBuilder@endlink  instead.  <br> 

    ## @return bool
    @property
    def HoleCreate(self) -> bool:
        """
        Getter for property: (bool) HoleCreate
         Returns the hole creation status.  
           If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies   
         
        """
        pass
    
    ## Setter for property: (bool) HoleCreate

    ##  Returns the hole creation status.  
    ##    If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::Join::JoinManager::CreateJoinHoleBuilder NXOpen::Join::JoinManager::CreateJoinHoleBuilder@endlink  instead.  <br> 

    @HoleCreate.setter
    def HoleCreate(self, status: bool):
        """
        Setter for property: (bool) HoleCreate
         Returns the hole creation status.  
           If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleDiameter
    ##  Returns the hole diameter   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HoleDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HoleDiameter
         Returns the hole diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link PointJoinBuilder.HoleTypes NXOpen.Join.PointJoinBuilder.HoleTypes@endlink) HoleType
    ##  Returns the hole type value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return PointJoinBuilder.HoleTypes
    @property
    def HoleType(self) -> PointJoinBuilder.HoleTypes:
        """
        Getter for property: (@link PointJoinBuilder.HoleTypes NXOpen.Join.PointJoinBuilder.HoleTypes@endlink) HoleType
         Returns the hole type value   
            
         
        """
        pass
    
    ## Setter for property: (@link PointJoinBuilder.HoleTypes NXOpen.Join.PointJoinBuilder.HoleTypes@endlink) HoleType

    ##  Returns the hole type value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @HoleType.setter
    def HoleType(self, holeType: PointJoinBuilder.HoleTypes):
        """
        Setter for property: (@link PointJoinBuilder.HoleTypes NXOpen.Join.PointJoinBuilder.HoleTypes@endlink) HoleType
         Returns the hole type value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) JointMarkAngle
    ##  Returns the joint mark angle   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def JointMarkAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) JointMarkAngle
         Returns the joint mark angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) JointMarkFace
    ##  Returns the face for the joint mark placement   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def JointMarkFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) JointMarkFace
         Returns the face for the joint mark placement   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) JointMarkGuideCurve
    ##  Returns the curve along which the joint mark symbol is placed   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.SelectCurveList
    @property
    def JointMarkGuideCurve(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) JointMarkGuideCurve
         Returns the curve along which the joint mark symbol is placed   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) JointMarkSize
    ##  Returns the joint mark size   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def JointMarkSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) JointMarkSize
         Returns the joint mark size   
            
         
        """
        pass
    
    ## Getter for property: (bool) MatedWithNutplate
    ##  Returns the flag when ON indicates only nutplate points from attached hardware utility are selectable    
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def MatedWithNutplate(self) -> bool:
        """
        Getter for property: (bool) MatedWithNutplate
         Returns the flag when ON indicates only nutplate points from attached hardware utility are selectable    
            
         
        """
        pass
    
    ## Setter for property: (bool) MatedWithNutplate

    ##  Returns the flag when ON indicates only nutplate points from attached hardware utility are selectable    
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @MatedWithNutplate.setter
    def MatedWithNutplate(self, matedWithNutplate: bool):
        """
        Setter for property: (bool) MatedWithNutplate
         Returns the flag when ON indicates only nutplate points from attached hardware utility are selectable    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) PointSelPoints
    ##  Returns the selected points   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.SelectPointList
    @property
    def PointSelPoints(self) -> NXOpen.SelectPointList:
        """
        Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) PointSelPoints
         Returns the selected points   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) StackupAlignment
    ##  Returns the stackup alignment   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def StackupAlignment(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) StackupAlignment
         Returns the stackup alignment   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) StackupAlignment

    ##  Returns the stackup alignment   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @StackupAlignment.setter
    def StackupAlignment(self, stackupAlignment: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) StackupAlignment
         Returns the stackup alignment   
            
         
        """
        pass
    
    ## Getter for property: (@link PointJoinBuilder.StackupAlignmentTypes NXOpen.Join.PointJoinBuilder.StackupAlignmentTypes@endlink) StackupAlignmentType
    ##  Returns the stackup alignment type value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PointJoinBuilder.StackupAlignmentTypes
    @property
    def StackupAlignmentType(self) -> PointJoinBuilder.StackupAlignmentTypes:
        """
        Getter for property: (@link PointJoinBuilder.StackupAlignmentTypes NXOpen.Join.PointJoinBuilder.StackupAlignmentTypes@endlink) StackupAlignmentType
         Returns the stackup alignment type value   
            
         
        """
        pass
    
    ## Setter for property: (@link PointJoinBuilder.StackupAlignmentTypes NXOpen.Join.PointJoinBuilder.StackupAlignmentTypes@endlink) StackupAlignmentType

    ##  Returns the stackup alignment type value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @StackupAlignmentType.setter
    def StackupAlignmentType(self, stackupAlignmentType: PointJoinBuilder.StackupAlignmentTypes):
        """
        Setter for property: (@link PointJoinBuilder.StackupAlignmentTypes NXOpen.Join.PointJoinBuilder.StackupAlignmentTypes@endlink) StackupAlignmentType
         Returns the stackup alignment type value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StackupGapLimit
    ##  Returns the gap limit   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StackupGapLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StackupGapLimit
         Returns the gap limit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StackupGapTolerance
    ##  Returns the gap tolerance   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StackupGapTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StackupGapTolerance
         Returns the gap tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StackupMaxHolePerimeter
    ##  Returns the maximum hole perimeter.  
    ##    Stackup will include bodies with holes or other openings with a loop perimeter smaller than specified here.
    ##         Bodies with larger openings will be excluded from the stackup.   
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StackupMaxHolePerimeter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StackupMaxHolePerimeter
         Returns the maximum hole perimeter.  
           Stackup will include bodies with holes or other openings with a loop perimeter smaller than specified here.
                Bodies with larger openings will be excluded from the stackup.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) StackupNormalSurface
    ##  Returns the selected normal surface   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def StackupNormalSurface(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) StackupNormalSurface
         Returns the selected normal surface   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StackupOnSurfaceTolerance
    ##  Returns the stackup on surface tolerance   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StackupOnSurfaceTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StackupOnSurfaceTolerance
         Returns the stackup on surface tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StackupOverlapTolerance
    ##  Returns the overlap tolerance   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StackupOverlapTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StackupOverlapTolerance
         Returns the overlap tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) StackupReverseDirection
    ##  Returns the reverse stackup direction flag   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def StackupReverseDirection(self) -> bool:
        """
        Getter for property: (bool) StackupReverseDirection
         Returns the reverse stackup direction flag   
            
         
        """
        pass
    
    ## Setter for property: (bool) StackupReverseDirection

    ##  Returns the reverse stackup direction flag   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @StackupReverseDirection.setter
    def StackupReverseDirection(self, isReversed: bool):
        """
        Setter for property: (bool) StackupReverseDirection
         Returns the reverse stackup direction flag   
            
         
        """
        pass
    
    ## Getter for property: (bool) SynchronizeLocation
    ##  Returns the indication of whether to update a point join's location to match its linked point.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def SynchronizeLocation(self) -> bool:
        """
        Getter for property: (bool) SynchronizeLocation
         Returns the indication of whether to update a point join's location to match its linked point.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SynchronizeLocation

    ##  Returns the indication of whether to update a point join's location to match its linked point.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SynchronizeLocation.setter
    def SynchronizeLocation(self, synchronizeLocation: bool):
        """
        Setter for property: (bool) SynchronizeLocation
         Returns the indication of whether to update a point join's location to match its linked point.  
             
         
        """
        pass
    
    ## Getter for property: (int) VisualizationColor
    ##  Returns the visualization color value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return int
    @property
    def VisualizationColor(self) -> int:
        """
        Getter for property: (int) VisualizationColor
         Returns the visualization color value   
            
         
        """
        pass
    
    ## Setter for property: (int) VisualizationColor

    ##  Returns the visualization color value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @VisualizationColor.setter
    def VisualizationColor(self, visualizationColor: int):
        """
        Setter for property: (int) VisualizationColor
         Returns the visualization color value   
            
         
        """
        pass
    
    ## Getter for property: (bool) VisualizationCreateSolid
    ##  Returns  the indication that the point join should be represented by a solid body    
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def VisualizationCreateSolid(self) -> bool:
        """
        Getter for property: (bool) VisualizationCreateSolid
         Returns  the indication that the point join should be represented by a solid body    
            
         
        """
        pass
    
    ## Setter for property: (bool) VisualizationCreateSolid

    ##  Returns  the indication that the point join should be represented by a solid body    
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @VisualizationCreateSolid.setter
    def VisualizationCreateSolid(self, visualizationCreateSolid: bool):
        """
        Setter for property: (bool) VisualizationCreateSolid
         Returns  the indication that the point join should be represented by a solid body    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VisualizationDiameter
    ##  Returns the visualization diameter   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def VisualizationDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VisualizationDiameter
         Returns the visualization diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link PointJoinBuilder.VisualizationGeometryType NXOpen.Join.PointJoinBuilder.VisualizationGeometryType@endlink) VisualizationGeometry
    ##  Returns the visualization geometry type value   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return PointJoinBuilder.VisualizationGeometryType
    @property
    def VisualizationGeometry(self) -> PointJoinBuilder.VisualizationGeometryType:
        """
        Getter for property: (@link PointJoinBuilder.VisualizationGeometryType NXOpen.Join.PointJoinBuilder.VisualizationGeometryType@endlink) VisualizationGeometry
         Returns the visualization geometry type value   
            
         
        """
        pass
    
    ## Setter for property: (@link PointJoinBuilder.VisualizationGeometryType NXOpen.Join.PointJoinBuilder.VisualizationGeometryType@endlink) VisualizationGeometry

    ##  Returns the visualization geometry type value   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @VisualizationGeometry.setter
    def VisualizationGeometry(self, visualizationGeometry: PointJoinBuilder.VisualizationGeometryType):
        """
        Setter for property: (@link PointJoinBuilder.VisualizationGeometryType NXOpen.Join.PointJoinBuilder.VisualizationGeometryType@endlink) VisualizationGeometry
         Returns the visualization geometry type value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VisualizationHeight
    ##  Returns the visualization height   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def VisualizationHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VisualizationHeight
         Returns the visualization height   
            
         
        """
        pass
    
    ## Getter for property: (int) VisualizationPointMarker
    ##  Returns the point marker   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return int
    @property
    def VisualizationPointMarker(self) -> int:
        """
        Getter for property: (int) VisualizationPointMarker
         Returns the point marker   
            
         
        """
        pass
    
    ## Setter for property: (int) VisualizationPointMarker

    ##  Returns the point marker   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @VisualizationPointMarker.setter
    def VisualizationPointMarker(self, visualizationPointMarker: int):
        """
        Setter for property: (int) VisualizationPointMarker
         Returns the point marker   
            
         
        """
        pass
    
    ##  Clears the attachment Hardware. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def ClearAttachmentHardware(self) -> None:
        """
         Clears the attachment Hardware. 
        """
        pass
    
    ##  Clears the hardware pin. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def ClearHardwarePin(self) -> None:
        """
         Clears the hardware pin. 
        """
        pass
    
    ##  Creates a new attachment Hardware. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def CreateAttachmentHardware(self) -> None:
        """
         Creates a new attachment Hardware. 
        """
        pass
    
    ##  Creates a new hardware pin. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def CreateHardwarePin(self) -> None:
        """
         Creates a new hardware pin. 
        """
        pass
    
    ##  Gets the attachment hardware. 
    ##  @return attachmentHardware (@link AttachmentHardware NXOpen.Join.AttachmentHardware@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetAttachmentHardware(self) -> AttachmentHardware:
        """
         Gets the attachment hardware. 
         @return attachmentHardware (@link AttachmentHardware NXOpen.Join.AttachmentHardware@endlink): .
        """
        pass
    
    ##  Gets the hardware pin. 
    ##  @return pin (@link PointJoinHardware NXOpen.Join.PointJoinHardware@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetHardwarePin(self) -> PointJoinHardware:
        """
         Gets the hardware pin. 
         @return pin (@link PointJoinHardware NXOpen.Join.PointJoinHardware@endlink): .
        """
        pass
    
    ##  Gets the headside hardware part by index 
    ##  @return headsidePart (@link PointJoinHardware NXOpen.Join.PointJoinHardware@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="headsidePartIndex"> (int) </param>
    def GetNthHeadSidePart(self, headsidePartIndex: int) -> PointJoinHardware:
        """
         Gets the headside hardware part by index 
         @return headsidePart (@link PointJoinHardware NXOpen.Join.PointJoinHardware@endlink): .
        """
        pass
    
    ##  Gets the tailside hardware part by index 
    ##  @return tailsidePart (@link PointJoinHardware NXOpen.Join.PointJoinHardware@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="tailsidePartIndex"> (int) </param>
    def GetNthTailSidePart(self, tailsidePartIndex: int) -> PointJoinHardware:
        """
         Gets the tailside hardware part by index 
         @return tailsidePart (@link PointJoinHardware NXOpen.Join.PointJoinHardware@endlink): .
        """
        pass
    
    ##  Gets number of headside hardware parts 
    ##  @return numberofHeadsideParts (int): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetNumberOfHeadSideParts(self) -> int:
        """
         Gets number of headside hardware parts 
         @return numberofHeadsideParts (int): .
        """
        pass
    
    ##  Gets number of tailside hardware parts 
    ##  @return numberofTailsideParts (int): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetNumberOfTailSideParts(self) -> int:
        """
         Gets number of tailside hardware parts 
         @return numberofTailsideParts (int): .
        """
        pass
    
    ##  This method adds a point that the stackup direction should be reversed for. 
    ##  @return reverseStackupDirection (bool):  Indicates if the stackup direction should be reversed for this point. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="point"> (@link NXOpen.Point NXOpen.Point@endlink)  A point was selected to reverse the stackup direction. </param>
    def GetStackupDirectionForPoint(self, point: NXOpen.Point) -> bool:
        """
         This method adds a point that the stackup direction should be reversed for. 
         @return reverseStackupDirection (bool):  Indicates if the stackup direction should be reversed for this point. .
        """
        pass
    
    ##  This method gets stackup entry point of Pointjoin 
    ##  @return entryPoint (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetStackupEntryPoint(self) -> NXOpen.Point3d:
        """
         This method gets stackup entry point of Pointjoin 
         @return entryPoint (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
        """
        pass
    
    ##  Loads hardware parts into assembly. 
    ##  @return status (bool): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_join (" NX Join")
    def LoadHardware(self) -> bool:
        """
         Loads hardware parts into assembly. 
         @return status (bool): .
        """
        pass
    
    ##  The washer information is added/updated on stackup 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def ProcessWasherInfoForStackup(self) -> None:
        """
         The washer information is added/updated on stackup 
        """
        pass
    
    ##  Set hardware pin information from name. 
    ##         If reuse library is the hardware data source, pinName is the descriptive name of the part
    ##         and pinPath is the path of the part in the reuse library.
    ##         If an XML database is used, pinName is the look up name and pinPath may be null. 
    ##         
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="pinName"> (str) </param>
    ## <param name="pinPath"> (str) </param>
    def SetHardwarePin(self, pinName: str, pinPath: str) -> None:
        """
         Set hardware pin information from name. 
                If reuse library is the hardware data source, pinName is the descriptive name of the part
                and pinPath is the path of the part in the reuse library.
                If an XML database is used, pinName is the look up name and pinPath may be null. 
                
        """
        pass
    
    ##  Set hardware for head side parts.
    ##         If reuse library is the hardware data source, headNames are the descriptive names of the parts
    ##         and headPaths are the paths of the parts in the reuse library.
    ##         If an XML database is used, headNames are the look up names and headPaths may be empty strings. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="headNames"> (List[str])  List of names </param>
    ## <param name="headPaths"> (List[str])  List of paths </param>
    def SetHeadSideParts(self, headNames: List[str], headPaths: List[str]) -> None:
        """
         Set hardware for head side parts.
                If reuse library is the hardware data source, headNames are the descriptive names of the parts
                and headPaths are the paths of the parts in the reuse library.
                If an XML database is used, headNames are the look up names and headPaths may be empty strings. 
        """
        pass
    
    ##  Sets the number of headside hardware parts.
    ##         Existing head side hardware objects are deleted and new head side hardware objects are created.
    ##         The number of newly created head side hardware objects equals numberOfHeadsideParts.
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="numberOfHeadsideParts"> (int) </param>
    def SetNumberOfHeadSideParts(self, numberOfHeadsideParts: int) -> None:
        """
         Sets the number of headside hardware parts.
                Existing head side hardware objects are deleted and new head side hardware objects are created.
                The number of newly created head side hardware objects equals numberOfHeadsideParts.
                
        """
        pass
    
    ##  Sets the number of tailside hardware parts.
    ##         Existing tail side hardware objects are deleted and new tail side hardware objects are created.
    ##         The number of newly created tail side hardware objects equals numberOfTailsideParts.
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="numberOfTailsideParts"> (int) </param>
    def SetNumberOfTailSideParts(self, numberOfTailsideParts: int) -> None:
        """
         Sets the number of tailside hardware parts.
                Existing tail side hardware objects are deleted and new tail side hardware objects are created.
                The number of newly created tail side hardware objects equals numberOfTailsideParts.
                
        """
        pass
    
    ##  This method gets the stackup direction for a specific point. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="point"> (@link NXOpen.Point NXOpen.Point@endlink)  A point was selected to reverse the stackup direction. </param>
    ## <param name="reverseStackupDirection"> (bool)  Indicates if the stackup direction should be reversed for this point. </param>
    def SetStackupDirectionForPoint(self, point: NXOpen.Point, reverseStackupDirection: bool) -> None:
        """
         This method gets the stackup direction for a specific point. 
        """
        pass
    
    ##  Set hardware for tail side parts. 
    ##         If reuse library is the hardware data source, tailNames are the descriptive names of the parts
    ##         and tailPaths are the paths of the parts in the reuse library.
    ##         If an XML database is used, tailNames are the look up names and tailPaths may be empty strings. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="tailNames"> (List[str])  List of names </param>
    ## <param name="tailPaths"> (List[str])  List of paths </param>
    def SetTailSideParts(self, tailNames: List[str], tailPaths: List[str]) -> None:
        """
         Set hardware for tail side parts. 
                If reuse library is the hardware data source, tailNames are the descriptive names of the parts
                and tailPaths are the paths of the parts in the reuse library.
                If an XML database is used, tailNames are the look up names and tailPaths may be empty strings. 
        """
        pass
    
    ##  Unloads hardware parts from assembly. 
    ##  @return status (bool): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This functionality is no longer supported.  <br> 

    ## License requirements: nx_join (" NX Join")
    def UnloadHardware(self) -> bool:
        """
         Unloads hardware parts from assembly. 
         @return status (bool): .
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Join::PointJoinHardware NXOpen::Join::PointJoinHardware@endlink .
##     
## 
##   <br>  Created in NX1926.0.0  <br> 

class PointJoinHardware(NXOpen.TaggedObject): 
    """ Represents a <ja_class>NXOpen.Join.PointJoinHardware</ja_class>.
    """


    ##  the attribute data source type
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Undefined</term><description> 
    ## </description> </item><item><term> 
    ## XmlDatabase</term><description> 
    ## </description> </item><item><term> 
    ## ReuseLibraryExcel</term><description> 
    ## </description> </item><item><term> 
    ## TeamcenterClassification</term><description> 
    ## </description> </item><item><term> 
    ## XmlDatabaseSpecification</term><description> 
    ## </description> </item><item><term> 
    ## ReuseLibrarySpecification</term><description> 
    ## </description> </item></list>
    class AttributeDataSourceType(Enum):
        """
        Members Include: <Undefined> <XmlDatabase> <ReuseLibraryExcel> <TeamcenterClassification> <XmlDatabaseSpecification> <ReuseLibrarySpecification>
        """
        Undefined: int
        XmlDatabase: int
        ReuseLibraryExcel: int
        TeamcenterClassification: int
        XmlDatabaseSpecification: int
        ReuseLibrarySpecification: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointJoinHardware.AttributeDataSourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link PointJoinHardware.AttributeDataSourceType NXOpen.Join.PointJoinHardware.AttributeDataSourceType@endlink) AttributeDataSource
    ##  Returns the attribute data source of the point join hardware part.  
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PointJoinHardware.AttributeDataSourceType
    @property
    def AttributeDataSource(self) -> PointJoinHardware.AttributeDataSourceType:
        """
        Getter for property: (@link PointJoinHardware.AttributeDataSourceType NXOpen.Join.PointJoinHardware.AttributeDataSourceType@endlink) AttributeDataSource
         Returns the attribute data source of the point join hardware part.  
            
         
        """
        pass
    
    ## Setter for property: (@link PointJoinHardware.AttributeDataSourceType NXOpen.Join.PointJoinHardware.AttributeDataSourceType@endlink) AttributeDataSource

    ##  Returns the attribute data source of the point join hardware part.  
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AttributeDataSource.setter
    def AttributeDataSource(self, attributeDataSource: PointJoinHardware.AttributeDataSourceType):
        """
        Setter for property: (@link PointJoinHardware.AttributeDataSourceType NXOpen.Join.PointJoinHardware.AttributeDataSourceType@endlink) AttributeDataSource
         Returns the attribute data source of the point join hardware part.  
            
         
        """
        pass
    
    ## Getter for property: (str) ClassificationClassId
    ##  Returns the Teamcenter Classification Object Class Id of the point join hardware part.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def ClassificationClassId(self) -> str:
        """
        Getter for property: (str) ClassificationClassId
         Returns the Teamcenter Classification Object Class Id of the point join hardware part.  
             
         
        """
        pass
    
    ## Setter for property: (str) ClassificationClassId

    ##  Returns the Teamcenter Classification Object Class Id of the point join hardware part.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ClassificationClassId.setter
    def ClassificationClassId(self, classId: str):
        """
        Setter for property: (str) ClassificationClassId
         Returns the Teamcenter Classification Object Class Id of the point join hardware part.  
             
         
        """
        pass
    
    ## Getter for property: (str) ClassificationInstanceId
    ##  Returns the Teamcenter Classification Object Instance Id of the point join hardware part.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def ClassificationInstanceId(self) -> str:
        """
        Getter for property: (str) ClassificationInstanceId
         Returns the Teamcenter Classification Object Instance Id of the point join hardware part.  
             
         
        """
        pass
    
    ## Setter for property: (str) ClassificationInstanceId

    ##  Returns the Teamcenter Classification Object Instance Id of the point join hardware part.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ClassificationInstanceId.setter
    def ClassificationInstanceId(self, instanceId: str):
        """
        Setter for property: (str) ClassificationInstanceId
         Returns the Teamcenter Classification Object Instance Id of the point join hardware part.  
             
         
        """
        pass
    
    ## Getter for property: (str) FamilyInstance
    ##  Returns the Family Instance Name of the point join hardware part in its family table.  
    ##   
    ##         It is the cell value of either the DB_PART_NO or OS_PART_NAME column of the instance's row in the part family table.
    ##         The cell value maybe prefixed with "DB_PART_NO:" or "OS_PART_NAME:" for a precise lookup for instance's values.
    ##         When not prefixed, both columns are checked for a match.
    ##           
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def FamilyInstance(self) -> str:
        """
        Getter for property: (str) FamilyInstance
         Returns the Family Instance Name of the point join hardware part in its family table.  
          
                It is the cell value of either the DB_PART_NO or OS_PART_NAME column of the instance's row in the part family table.
                The cell value maybe prefixed with "DB_PART_NO:" or "OS_PART_NAME:" for a precise lookup for instance's values.
                When not prefixed, both columns are checked for a match.
                  
         
        """
        pass
    
    ## Setter for property: (str) FamilyInstance

    ##  Returns the Family Instance Name of the point join hardware part in its family table.  
    ##   
    ##         It is the cell value of either the DB_PART_NO or OS_PART_NAME column of the instance's row in the part family table.
    ##         The cell value maybe prefixed with "DB_PART_NO:" or "OS_PART_NAME:" for a precise lookup for instance's values.
    ##         When not prefixed, both columns are checked for a match.
    ##           
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FamilyInstance.setter
    def FamilyInstance(self, familyInstance: str):
        """
        Setter for property: (str) FamilyInstance
         Returns the Family Instance Name of the point join hardware part in its family table.  
          
                It is the cell value of either the DB_PART_NO or OS_PART_NAME column of the instance's row in the part family table.
                The cell value maybe prefixed with "DB_PART_NO:" or "OS_PART_NAME:" for a precise lookup for instance's values.
                When not prefixed, both columns are checked for a match.
                  
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name of the point join hardware.  
    ##   
    ##         If the attribute data source is @link NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeXmlDatabase NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeXmlDatabase@endlink ,
    ##         name is used to look up the attributes from the XML database and the available PointJoinHardware attributes
    ##         are auto populated.
    ##           
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the point join hardware.  
          
                If the attribute data source is @link NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeXmlDatabase NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeXmlDatabase@endlink ,
                name is used to look up the attributes from the XML database and the available PointJoinHardware attributes
                are auto populated.
                  
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name of the point join hardware.  
    ##   
    ##         If the attribute data source is @link NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeXmlDatabase NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeXmlDatabase@endlink ,
    ##         name is used to look up the attributes from the XML database and the available PointJoinHardware attributes
    ##         are auto populated.
    ##           
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the point join hardware.  
          
                If the attribute data source is @link NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeXmlDatabase NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeXmlDatabase@endlink ,
                name is used to look up the attributes from the XML database and the available PointJoinHardware attributes
                are auto populated.
                  
         
        """
        pass
    
    ## Getter for property: (str) Orientation
    ##  Returns the orientation of the point join hardware part.  
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Orientation(self) -> str:
        """
        Getter for property: (str) Orientation
         Returns the orientation of the point join hardware part.  
            
         
        """
        pass
    
    ## Setter for property: (str) Orientation

    ##  Returns the orientation of the point join hardware part.  
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Orientation.setter
    def Orientation(self, orientation: str):
        """
        Setter for property: (str) Orientation
         Returns the orientation of the point join hardware part.  
            
         
        """
        pass
    
    ## Getter for property: (str) Path
    ##  Returns the path of the point join hardware part.  
    ##   
    ##         If the attribute data source is @link NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeReuseLibraryExcel NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeReuseLibraryExcel@endlink ,
    ##         path is used to look up the attributes from the EXCEL database and the available PointJoinHardware attributes
    ##         are auto populated.
    ##           
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Path(self) -> str:
        """
        Getter for property: (str) Path
         Returns the path of the point join hardware part.  
          
                If the attribute data source is @link NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeReuseLibraryExcel NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeReuseLibraryExcel@endlink ,
                path is used to look up the attributes from the EXCEL database and the available PointJoinHardware attributes
                are auto populated.
                  
         
        """
        pass
    
    ## Setter for property: (str) Path

    ##  Returns the path of the point join hardware part.  
    ##   
    ##         If the attribute data source is @link NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeReuseLibraryExcel NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeReuseLibraryExcel@endlink ,
    ##         path is used to look up the attributes from the EXCEL database and the available PointJoinHardware attributes
    ##         are auto populated.
    ##           
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Path.setter
    def Path(self, path: str):
        """
        Setter for property: (str) Path
         Returns the path of the point join hardware part.  
          
                If the attribute data source is @link NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeReuseLibraryExcel NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeReuseLibraryExcel@endlink ,
                path is used to look up the attributes from the EXCEL database and the available PointJoinHardware attributes
                are auto populated.
                  
         
        """
        pass
    
    ## Getter for property: (str) Specification
    ##  Returns the specification of the point join hardware.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Specification(self) -> str:
        """
        Getter for property: (str) Specification
         Returns the specification of the point join hardware.  
             
         
        """
        pass
    
    ## Setter for property: (str) Specification

    ##  Returns the specification of the point join hardware.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Specification.setter
    def Specification(self, spec: str):
        """
        Setter for property: (str) Specification
         Returns the specification of the point join hardware.  
             
         
        """
        pass
    
    ## Getter for property: (str) SpecificationDescriptiveName
    ##  Returns the Descriptive Name of the hardware specification in Reuse Library.  
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def SpecificationDescriptiveName(self) -> str:
        """
        Getter for property: (str) SpecificationDescriptiveName
         Returns the Descriptive Name of the hardware specification in Reuse Library.  
            
         
        """
        pass
    
    ## Setter for property: (str) SpecificationDescriptiveName

    ##  Returns the Descriptive Name of the hardware specification in Reuse Library.  
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @SpecificationDescriptiveName.setter
    def SpecificationDescriptiveName(self, specDescName: str):
        """
        Setter for property: (str) SpecificationDescriptiveName
         Returns the Descriptive Name of the hardware specification in Reuse Library.  
            
         
        """
        pass
    
    ## Getter for property: (float) Thickness
    ##  Returns the thickness of the point join hardware part.  
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def Thickness(self) -> float:
        """
        Getter for property: (float) Thickness
         Returns the thickness of the point join hardware part.  
            
         
        """
        pass
    
    ## Setter for property: (float) Thickness

    ##  Returns the thickness of the point join hardware part.  
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Thickness.setter
    def Thickness(self, thickness: float):
        """
        Setter for property: (float) Thickness
         Returns the thickness of the point join hardware part.  
            
         
        """
        pass
    
    ## Getter for property: (float) ThreadPitch
    ##  Returns the thread pitch of the point join hardware part.  
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return float
    @property
    def ThreadPitch(self) -> float:
        """
        Getter for property: (float) ThreadPitch
         Returns the thread pitch of the point join hardware part.  
            
         
        """
        pass
    
    ## Setter for property: (float) ThreadPitch

    ##  Returns the thread pitch of the point join hardware part.  
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ThreadPitch.setter
    def ThreadPitch(self, threadPitch: float):
        """
        Setter for property: (float) ThreadPitch
         Returns the thread pitch of the point join hardware part.  
            
         
        """
        pass
    
    ## Getter for property: (float) ThreadedLength
    ##  Returns the threaded length of the point join hardware part.  
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return float
    @property
    def ThreadedLength(self) -> float:
        """
        Getter for property: (float) ThreadedLength
         Returns the threaded length of the point join hardware part.  
            
         
        """
        pass
    
    ## Setter for property: (float) ThreadedLength

    ##  Returns the threaded length of the point join hardware part.  
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ThreadedLength.setter
    def ThreadedLength(self, threadedLength: float):
        """
        Setter for property: (float) ThreadedLength
         Returns the threaded length of the point join hardware part.  
            
         
        """
        pass
    
    ## Getter for property: (str) Type
    ##  Returns the type of the point join hardware part.  
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Type(self) -> str:
        """
        Getter for property: (str) Type
         Returns the type of the point join hardware part.  
            
         
        """
        pass
    
    ## Setter for property: (str) Type

    ##  Returns the type of the point join hardware part.  
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Type.setter
    def Type(self, type: str):
        """
        Setter for property: (str) Type
         Returns the type of the point join hardware part.  
            
         
        """
        pass
    
##  Indicates the required stackup info from a @link Join::PointJoin Join::PointJoin@endlink . 
class PointJoinStackupInfoOptions:
    """
     Indicates the required stackup info from a @link Join::PointJoin Join::PointJoin@endlink . 
    """
    ## Getter for property :(bool) ConnectedBodies
    ## connected bodies.
    ## @return bool
    @property
    def ConnectedBodies(self) -> bool:
        """
        Getter for property ConnectedBodies
        connected bodies.

        """
        pass
    
    ## Setter for property :(bool) ConnectedBodies
    @ConnectedBodies.setter
    def ConnectedBodies(self, value: bool):
        """
        Getter for property ConnectedBodies
        connected bodies.
        Setter for property ConnectedBodies
        connected bodies.

        """
        pass
    
    ## Getter for property :(bool) EntryExitPoints
    ## entry/exit points.
    ## @return bool
    @property
    def EntryExitPoints(self) -> bool:
        """
        Getter for property EntryExitPoints
        entry/exit points.

        """
        pass
    
    ## Setter for property :(bool) EntryExitPoints
    @EntryExitPoints.setter
    def EntryExitPoints(self, value: bool):
        """
        Getter for property EntryExitPoints
        entry/exit points.
        Setter for property EntryExitPoints
        entry/exit points.

        """
        pass
    
    ## Getter for property :(bool) EntryExitFaces
    ## entry/exit faces.
    ## @return bool
    @property
    def EntryExitFaces(self) -> bool:
        """
        Getter for property EntryExitFaces
        entry/exit faces.

        """
        pass
    
    ## Setter for property :(bool) EntryExitFaces
    @EntryExitFaces.setter
    def EntryExitFaces(self, value: bool):
        """
        Getter for property EntryExitFaces
        entry/exit faces.
        Setter for property EntryExitFaces
        entry/exit faces.

        """
        pass
    
    ## Getter for property :(bool) HoleEdges
    ## hole edges
    ## @return bool
    @property
    def HoleEdges(self) -> bool:
        """
        Getter for property HoleEdges
        hole edges

        """
        pass
    
    ## Setter for property :(bool) HoleEdges
    @HoleEdges.setter
    def HoleEdges(self, value: bool):
        """
        Getter for property HoleEdges
        hole edges
        Setter for property HoleEdges
        hole edges

        """
        pass
    


import NXOpen
##  Represents a manager of point join stackup info objects. 
## 
##   <br>  Created in NX2212.0.0  <br> 

class PointJoinStackupInfo(NXOpen.TransientObject): 
    """ Represents a manager of point join stackup info objects. """


    ##  Free resources associated with the instance. After this method
    ##         is called, it is illegal to use the object. In .NET, this method
    ##         is automatically called when the object is deleted by the garbage
    ##         collector. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object. In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    
    ##  Gets connected bodies of point join. 
    ##  @return bodies (@link NXOpen.Body List[NXOpen.Body]@endlink):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetConnectedBodies(self) -> List[NXOpen.Body]:
        """
         Gets connected bodies of point join. 
         @return bodies (@link NXOpen.Body List[NXOpen.Body]@endlink):  .
        """
        pass
    
    ##  Gets connected body of point join. 
    ##  @return body (@link NXOpen.Body NXOpen.Body@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link NXOpen::Join::PointJoinStackupInfo::GetConnectedBodies NXOpen::Join::PointJoinStackupInfo::GetConnectedBodies@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="i"> (int) </param>
    def GetConnectedBody(self, i: int) -> NXOpen.Body:
        """
         Gets connected body of point join. 
         @return body (@link NXOpen.Body NXOpen.Body@endlink): .
        """
        pass
    
    ##  Gets total number of stackup entries. 
    ##  @return stackupCount (int): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetCount(self) -> int:
        """
         Gets total number of stackup entries. 
         @return stackupCount (int): .
        """
        pass
    
    ##  Gets entry faces of point join. Maximum index can be found using @link NXOpen::Join::PointJoinStackupInfo::GetCount NXOpen::Join::PointJoinStackupInfo::GetCount@endlink . 
    ##  @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink):  .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="i"> (int) </param>
    def GetEntryFaces(self, i: int) -> List[NXOpen.Face]:
        """
         Gets entry faces of point join. Maximum index can be found using @link NXOpen::Join::PointJoinStackupInfo::GetCount NXOpen::Join::PointJoinStackupInfo::GetCount@endlink . 
         @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink):  .
        """
        pass
    
    ##  Gets entry co-ordinates of point join. 
    ##  @return coordinates (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link NXOpen::Join::PointJoinStackupInfo::GetExitPoints NXOpen::Join::PointJoinStackupInfo::GetExitPoints@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="i"> (int) </param>
    def GetEntryPoint(self, i: int) -> NXOpen.Point3d:
        """
         Gets entry co-ordinates of point join. 
         @return coordinates (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
        """
        pass
    
    ##  Gets all entry points of point join. 
    ##  @return points (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetEntryPoints(self) -> List[NXOpen.Point3d]:
        """
         Gets all entry points of point join. 
         @return points (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  .
        """
        pass
    
    ##  Gets exit faces of point join. Maximum index can be found using @link NXOpen::Join::PointJoinStackupInfo::GetCount NXOpen::Join::PointJoinStackupInfo::GetCount@endlink . 
    ##  @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink):  .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="i"> (int) </param>
    def GetExitFaces(self, i: int) -> List[NXOpen.Face]:
        """
         Gets exit faces of point join. Maximum index can be found using @link NXOpen::Join::PointJoinStackupInfo::GetCount NXOpen::Join::PointJoinStackupInfo::GetCount@endlink . 
         @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink):  .
        """
        pass
    
    ##  Gets exit co-ordinates of point join. 
    ##  @return coordinates (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link NXOpen::Join::PointJoinStackupInfo::GetExitPoints NXOpen::Join::PointJoinStackupInfo::GetExitPoints@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="i"> (int) </param>
    def GetExitPoint(self, i: int) -> NXOpen.Point3d:
        """
         Gets exit co-ordinates of point join. 
         @return coordinates (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
        """
        pass
    
    ##  Gets all exit points of point join. 
    ##  @return points (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetExitPoints(self) -> List[NXOpen.Point3d]:
        """
         Gets all exit points of point join. 
         @return points (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  .
        """
        pass
    
    ##  Gets hole edges of Point Join. 
    ##  @return edges (@link NXOpen.Edge List[NXOpen.Edge]@endlink):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetHoleEdges(self) -> List[NXOpen.Edge]:
        """
         Gets hole edges of Point Join. 
         @return edges (@link NXOpen.Edge List[NXOpen.Edge]@endlink):  .
        """
        pass
    
    ##  Gets stackup direction. 
    ##  @return stackupDirection (@link NXOpen.Vector3d NXOpen.Vector3d@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetStackupDirection(self) -> NXOpen.Vector3d:
        """
         Gets stackup direction. 
         @return stackupDirection (@link NXOpen.Vector3d NXOpen.Vector3d@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a point based join feature  <br> To create or edit an instance of this class, use @link NXOpen::Join::PointJoinBuilder  NXOpen::Join::PointJoinBuilder @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class PointJoin(NXOpen.Features.BodyFeature): 
    """ Represents a point based join feature """


    ##  Checks whether all of the connected parts of a point join are fully loaded or not.
    ##  @return fullyLoaded (bool): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def AreConnectedPartsFullyLoaded(self) -> bool:
        """
         Checks whether all of the connected parts of a point join are fully loaded or not.
         @return fullyLoaded (bool): .
        """
        pass
    
    ##  Gets simple hole diameter of a point join.
    ##  @return holeDiameter (float): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetHoleDiameter(self) -> float:
        """
         Gets simple hole diameter of a point join.
         @return holeDiameter (float): .
        """
        pass
    
    ##  Gets first stackup entry point of a point join.
    ##  @return firstEntryPoint (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def GetPointJoinStackupFirstEntryPoint(self) -> NXOpen.Point3d:
        """
         Gets first stackup entry point of a point join.
         @return firstEntryPoint (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
        """
        pass
    
    ##  Gets stackup information of a point join.
    ##  @return stackupInfo (@link PointJoinStackupInfo NXOpen.Join.PointJoinStackupInfo@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    ## 
    ## <param name="stackupInfoOptions"> (@link PointJoinStackupInfoOptions NXOpen.Join.PointJoinStackupInfoOptions@endlink) </param>
    def GetStackupInfo(self, stackupInfoOptions: PointJoinStackupInfoOptions) -> PointJoinStackupInfo:
        """
         Gets stackup information of a point join.
         @return stackupInfo (@link PointJoinStackupInfo NXOpen.Join.PointJoinStackupInfo@endlink): .
        """
        pass
    
    ##  Loads connected parts of a point join.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def LoadConnectedParts(self) -> None:
        """
         Loads connected parts of a point join.
        """
        pass
    
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
##  Used to create points on a guide curve.  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreatePointLayoutBuilder  NXOpen::Join::JoinManager::CreatePointLayoutBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DistanceFromEnds </term> <description> 
##  
## 6.25 (millimeters part), 0.04 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MaximumSpacingBetweenPoints </term> <description> 
##  
## 50 (millimeters part), 2.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MinimumNumberPoints </term> <description> 
##  
## 3 </description> </item> 
## 
## <item><term> 
##  
## MinimumSpacingBetweenPoints </term> <description> 
##  
## 25 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## NumberOfPoints.Value </term> <description> 
##  
## 3 </description> </item> 
## 
## <item><term> 
##  
## Spacing.Value </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## SpacingMethod </term> <description> 
##  
## ArcLength </description> </item> 
## 
## <item><term> 
##  
## SpacingOption </term> <description> 
##  
## Distance </description> </item> 
## 
## <item><term> 
##  
## UniformSpacingTolerance </term> <description> 
##  
## 4 (millimeters part), 0.16 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class PointLayoutBuilder(NXOpen.Features.FeatureBuilder): 
    """ Used to create points on a guide curve. """


    ##  Options for Spacing Method 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ArcLength</term><description> 
    ##  Arc Length </description> </item><item><term> 
    ## ParallelXPlane</term><description> 
    ##  Parallel X Plane </description> </item><item><term> 
    ## ParallelYPlane</term><description> 
    ##  Parallel Y Plane </description> </item><item><term> 
    ## ParallelZPlane</term><description> 
    ##  Parallel Z Plane </description> </item></list>
    class SpaceMethod(Enum):
        """
        Members Include: <ArcLength> <ParallelXPlane> <ParallelYPlane> <ParallelZPlane>
        """
        ArcLength: int
        ParallelXPlane: int
        ParallelYPlane: int
        ParallelZPlane: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointLayoutBuilder.SpaceMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Spacing Option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Distance</term><description> 
    ##  Space points by a fixed distance. Spacing at last point may not be uniform.</description> </item><item><term> 
    ## Number</term><description> 
    ##  Uniformly space a number of points. </description> </item><item><term> 
    ## MinimumDistance</term><description> 
    ##  Uniformly space points using a minimum distance value. </description> </item></list>
    class SpaceOption(Enum):
        """
        Members Include: <Distance> <Number> <MinimumDistance>
        """
        Distance: int
        Number: int
        MinimumDistance: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointLayoutBuilder.SpaceOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The type of spacing desired 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Manual</term><description> 
    ##  Fixed parameters are used to space points. </description> </item><item><term> 
    ## Automatic</term><description> 
    ##  Points are spaced using a minimum spacing distance and maximum spacing distance variables. </description> </item></list>
    class SpacingTypes(Enum):
        """
        Members Include: <Manual> <Automatic>
        """
        Manual: int
        Automatic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointLayoutBuilder.SpacingTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) DistanceFromEnds
    ##  Returns the distance from the ends to start creating weld points at   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DistanceFromEnds(self) -> float:
        """
        Getter for property: (float) DistanceFromEnds
         Returns the distance from the ends to start creating weld points at   
            
         
        """
        pass
    
    ## Setter for property: (float) DistanceFromEnds

    ##  Returns the distance from the ends to start creating weld points at   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DistanceFromEnds.setter
    def DistanceFromEnds(self, distanceFromEnds: float):
        """
        Setter for property: (float) DistanceFromEnds
         Returns the distance from the ends to start creating weld points at   
            
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##  Returns the distance tolerance for constructing the feature.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the feature.  
              
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##  Returns the distance tolerance for constructing the feature.  
    ##       
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the feature.  
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) EndDistance
    ##  Returns the end distance.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.OnPathDimensionBuilder
    @property
    def EndDistance(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) EndDistance
         Returns the end distance.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) GuidePath
    ##  Returns the selected section used to place point along.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def GuidePath(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) GuidePath
         Returns the selected section used to place point along.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaximumSpacingBetweenPoints
    ##  Returns the maximum spacing between points   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def MaximumSpacingBetweenPoints(self) -> float:
        """
        Getter for property: (float) MaximumSpacingBetweenPoints
         Returns the maximum spacing between points   
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumSpacingBetweenPoints

    ##  Returns the maximum spacing between points   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MaximumSpacingBetweenPoints.setter
    def MaximumSpacingBetweenPoints(self, maximumSpacingBetweenPoints: float):
        """
        Setter for property: (float) MaximumSpacingBetweenPoints
         Returns the maximum spacing between points   
            
         
        """
        pass
    
    ## Getter for property: (int) MinimumNumberPoints
    ##  Returns the minimum number points to create on an overlap sheet   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return int
    @property
    def MinimumNumberPoints(self) -> int:
        """
        Getter for property: (int) MinimumNumberPoints
         Returns the minimum number points to create on an overlap sheet   
            
         
        """
        pass
    
    ## Setter for property: (int) MinimumNumberPoints

    ##  Returns the minimum number points to create on an overlap sheet   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MinimumNumberPoints.setter
    def MinimumNumberPoints(self, minimumNumberPointsOnOverlap: int):
        """
        Setter for property: (int) MinimumNumberPoints
         Returns the minimum number points to create on an overlap sheet   
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumSpacingBetweenPoints
    ##  Returns the minimum spacing between points   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def MinimumSpacingBetweenPoints(self) -> float:
        """
        Getter for property: (float) MinimumSpacingBetweenPoints
         Returns the minimum spacing between points   
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumSpacingBetweenPoints

    ##  Returns the minimum spacing between points   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @MinimumSpacingBetweenPoints.setter
    def MinimumSpacingBetweenPoints(self, minimumSpacingBetweenPoints: float):
        """
        Setter for property: (float) MinimumSpacingBetweenPoints
         Returns the minimum spacing between points   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NumberOfPoints
    ##  Returns the number to determine the points along the guide curve.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def NumberOfPoints(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NumberOfPoints
         Returns the number to determine the points along the guide curve.  
             
         
        """
        pass
    
    ## Getter for property: (@link PointLayoutPointBuilderList NXOpen.Join.PointLayoutPointBuilderList@endlink) PointList
    ##  Returns the list of points  
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PointLayoutPointBuilderList
    @property
    def PointList(self) -> PointLayoutPointBuilderList:
        """
        Getter for property: (@link PointLayoutPointBuilderList NXOpen.Join.PointLayoutPointBuilderList@endlink) PointList
         Returns the list of points  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Spacing
    ##  Returns the spacing to determine the points along the guide curve.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Spacing(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Spacing
         Returns the spacing to determine the points along the guide curve.  
             
         
        """
        pass
    
    ## Getter for property: (@link PointLayoutBuilder.SpaceMethod NXOpen.Join.PointLayoutBuilder.SpaceMethod@endlink) SpacingMethod
    ##  Returns the spacing method.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PointLayoutBuilder.SpaceMethod
    @property
    def SpacingMethod(self) -> PointLayoutBuilder.SpaceMethod:
        """
        Getter for property: (@link PointLayoutBuilder.SpaceMethod NXOpen.Join.PointLayoutBuilder.SpaceMethod@endlink) SpacingMethod
         Returns the spacing method.  
             
         
        """
        pass
    
    ## Setter for property: (@link PointLayoutBuilder.SpaceMethod NXOpen.Join.PointLayoutBuilder.SpaceMethod@endlink) SpacingMethod

    ##  Returns the spacing method.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SpacingMethod.setter
    def SpacingMethod(self, spacingMethod: PointLayoutBuilder.SpaceMethod):
        """
        Setter for property: (@link PointLayoutBuilder.SpaceMethod NXOpen.Join.PointLayoutBuilder.SpaceMethod@endlink) SpacingMethod
         Returns the spacing method.  
             
         
        """
        pass
    
    ## Getter for property: (@link PointLayoutBuilder.SpaceOption NXOpen.Join.PointLayoutBuilder.SpaceOption@endlink) SpacingOption
    ##  Returns the spacing option.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PointLayoutBuilder.SpaceOption
    @property
    def SpacingOption(self) -> PointLayoutBuilder.SpaceOption:
        """
        Getter for property: (@link PointLayoutBuilder.SpaceOption NXOpen.Join.PointLayoutBuilder.SpaceOption@endlink) SpacingOption
         Returns the spacing option.  
             
         
        """
        pass
    
    ## Setter for property: (@link PointLayoutBuilder.SpaceOption NXOpen.Join.PointLayoutBuilder.SpaceOption@endlink) SpacingOption

    ##  Returns the spacing option.  
    ##      
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SpacingOption.setter
    def SpacingOption(self, spacingOption: PointLayoutBuilder.SpaceOption):
        """
        Setter for property: (@link PointLayoutBuilder.SpaceOption NXOpen.Join.PointLayoutBuilder.SpaceOption@endlink) SpacingOption
         Returns the spacing option.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) StartDistance
    ##  Returns the start distance.  
    ##      
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.OnPathDimensionBuilder
    @property
    def StartDistance(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) StartDistance
         Returns the start distance.  
             
         
        """
        pass
    
    ## Getter for property: (@link PointLayoutBuilder.SpacingTypes NXOpen.Join.PointLayoutBuilder.SpacingTypes@endlink) Type
    ##  Returns the point spacing method represented by @link NXOpen::Join::PointLayoutBuilder::SpacingTypes NXOpen::Join::PointLayoutBuilder::SpacingTypes@endlink .  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return PointLayoutBuilder.SpacingTypes
    @property
    def Type(self) -> PointLayoutBuilder.SpacingTypes:
        """
        Getter for property: (@link PointLayoutBuilder.SpacingTypes NXOpen.Join.PointLayoutBuilder.SpacingTypes@endlink) Type
         Returns the point spacing method represented by @link NXOpen::Join::PointLayoutBuilder::SpacingTypes NXOpen::Join::PointLayoutBuilder::SpacingTypes@endlink .  
            
         
        """
        pass
    
    ## Setter for property: (@link PointLayoutBuilder.SpacingTypes NXOpen.Join.PointLayoutBuilder.SpacingTypes@endlink) Type

    ##  Returns the point spacing method represented by @link NXOpen::Join::PointLayoutBuilder::SpacingTypes NXOpen::Join::PointLayoutBuilder::SpacingTypes@endlink .  
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Type.setter
    def Type(self, type: PointLayoutBuilder.SpacingTypes):
        """
        Setter for property: (@link PointLayoutBuilder.SpacingTypes NXOpen.Join.PointLayoutBuilder.SpacingTypes@endlink) Type
         Returns the point spacing method represented by @link NXOpen::Join::PointLayoutBuilder::SpacingTypes NXOpen::Join::PointLayoutBuilder::SpacingTypes@endlink .  
            
         
        """
        pass
    
    ## Getter for property: (float) UniformSpacingTolerance
    ##  Returns the distance that maximum spacing can be exceeded to achieve uniform spacing   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def UniformSpacingTolerance(self) -> float:
        """
        Getter for property: (float) UniformSpacingTolerance
         Returns the distance that maximum spacing can be exceeded to achieve uniform spacing   
            
         
        """
        pass
    
    ## Setter for property: (float) UniformSpacingTolerance

    ##  Returns the distance that maximum spacing can be exceeded to achieve uniform spacing   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @UniformSpacingTolerance.setter
    def UniformSpacingTolerance(self, uniformSpacingTolerance: float):
        """
        Setter for property: (float) UniformSpacingTolerance
         Returns the distance that maximum spacing can be exceeded to achieve uniform spacing   
            
         
        """
        pass
    
    ##  Creates a list of points on the overlap sheet. In addition, a curve selected by the user will be placed at these points. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def AppendPoints(self) -> None:
        """
         Creates a list of points on the overlap sheet. In addition, a curve selected by the user will be placed at these points. 
        """
        pass
    
    ##  Creates a @link NXOpen::Join::PointLayoutPointBuilder NXOpen::Join::PointLayoutPointBuilder@endlink  object. 
    ##  @return newPointBuilder (@link PointLayoutPointBuilder NXOpen.Join.PointLayoutPointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_join (" NX Join")
    def NewPoints(self) -> PointLayoutPointBuilder:
        """
         Creates a @link NXOpen::Join::PointLayoutPointBuilder NXOpen::Join::PointLayoutPointBuilder@endlink  object. 
         @return newPointBuilder (@link PointLayoutPointBuilder NXOpen.Join.PointLayoutPointBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class PointLayoutPointBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##  Returns the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PointLayoutPointBuilderList NXOpen.Join.PointLayoutPointBuilderList@endlink) </param>
    ## <param name="objects"> (@link PointLayoutPointBuilder List[NXOpen.Join.PointLayoutPointBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[PointLayoutPointBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PointLayoutPointBuilderList NXOpen.Join.PointLayoutPointBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link PointLayoutPointBuilder NXOpen.Join.PointLayoutPointBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: PointLayoutPointBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PointLayoutPointBuilderList NXOpen.Join.PointLayoutPointBuilderList@endlink) </param>
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="delete_idx"> (int)  index of item to be deleted </param>
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PointLayoutPointBuilderList NXOpen.Join.PointLayoutPointBuilderList@endlink) </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the objects when removing them </param>
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PointLayoutPointBuilderList NXOpen.Join.PointLayoutPointBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PointLayoutPointBuilderList NXOpen.Join.PointLayoutPointBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PointLayoutPointBuilderList NXOpen.Join.PointLayoutPointBuilderList@endlink) </param>
    ## <param name="obj"> (@link PointLayoutPointBuilder NXOpen.Join.PointLayoutPointBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: PointLayoutPointBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PointLayoutPointBuilderList NXOpen.Join.PointLayoutPointBuilderList@endlink) </param>
    ## <param name="obj"> (@link PointLayoutPointBuilder NXOpen.Join.PointLayoutPointBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: PointLayoutPointBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="obj"> (@link PointLayoutPointBuilder NXOpen.Join.PointLayoutPointBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: PointLayoutPointBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link PointLayoutPointBuilder NXOpen.Join.PointLayoutPointBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> PointLayoutPointBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link PointLayoutPointBuilder NXOpen.Join.PointLayoutPointBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link PointLayoutPointBuilder List[NXOpen.Join.PointLayoutPointBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[PointLayoutPointBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link PointLayoutPointBuilder List[NXOpen.Join.PointLayoutPointBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link PointLayoutPointBuilder NXOpen.Join.PointLayoutPointBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: PointLayoutPointBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link PointLayoutPointBuilder List[NXOpen.Join.PointLayoutPointBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[PointLayoutPointBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PointLayoutPointBuilderList NXOpen.Join.PointLayoutPointBuilderList@endlink) </param>
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PointLayoutPointBuilderList NXOpen.Join.PointLayoutPointBuilderList@endlink) </param>
    ## <param name="object1"> (@link PointLayoutPointBuilder NXOpen.Join.PointLayoutPointBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link PointLayoutPointBuilder NXOpen.Join.PointLayoutPointBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: PointLayoutPointBuilder, object2: PointLayoutPointBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Used to create or edit a point in the list of points for PointLayoutBuilder  <br> To create a new instance of this class, use @link NXOpen::Join::PointLayoutBuilder::NewPoints  NXOpen::Join::PointLayoutBuilder::NewPoints @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class PointLayoutPointBuilder(NXOpen.TaggedObject): 
    """ Used to create or edit a point in the list of points for PointLayoutBuilder """


    ##  The point classification 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None specifed. </description> </item><item><term> 
    ## MovedAlongGuide</term><description> 
    ##  User moved point from default location along the guide curve </description> </item></list>
    class PointPosition(Enum):
        """
        Members Include: <NotSet> <MovedAlongGuide>
        """
        NotSet: int
        MovedAlongGuide: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointLayoutPointBuilder.PointPosition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
    ##  Returns the point at which the feature is created   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
         Returns the point at which the feature is created   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point

    ##  Returns the point at which the feature is created   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
         Returns the point at which the feature is created   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a Join.Overlap Feature.  <br> To create or edit an instance of this class, use @link NXOpen::Join::PointLayoutBuilder  NXOpen::Join::PointLayoutBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class PointLayout(NXOpen.Features.Feature): 
    """ Represents a Join.Overlap Feature. """


    ##  Retrieves the point locations represented by the Join.PointLayout Feature. 
    ##  @return points (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def GetPoints(self) -> List[NXOpen.Point3d]:
        """
         Retrieves the point locations represented by the Join.PointLayout Feature. 
         @return points (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  .
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Join::PreferencesBuilder NXOpen::Join::PreferencesBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreatePreferencesBuilder  NXOpen::Join::JoinManager::CreatePreferencesBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class PreferencesBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Join.PreferencesBuilder</ja_class> builder """


    ## Getter for property: (int) ConstructionLayer
    ##  Returns the construction layer preference.  
    ##    This option specifies the layer on which the construction geometry should be placed.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return int
    @property
    def ConstructionLayer(self) -> int:
        """
        Getter for property: (int) ConstructionLayer
         Returns the construction layer preference.  
           This option specifies the layer on which the construction geometry should be placed.  
         
        """
        pass
    
    ## Setter for property: (int) ConstructionLayer

    ##  Returns the construction layer preference.  
    ##    This option specifies the layer on which the construction geometry should be placed.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ConstructionLayer.setter
    def ConstructionLayer(self, constructionLayer: int):
        """
        Setter for property: (int) ConstructionLayer
         Returns the construction layer preference.  
           This option specifies the layer on which the construction geometry should be placed.  
         
        """
        pass
    
    ## Getter for property: (bool) FixTimestamp
    ##  Returns the fix at timestamp preference.  
    ##    When WAVE Links are created by the Join commands including Curve utilities and Join Creation, linked geometry will be fixed at Current Timestamp allowing users to create holes where applicable.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def FixTimestamp(self) -> bool:
        """
        Getter for property: (bool) FixTimestamp
         Returns the fix at timestamp preference.  
           When WAVE Links are created by the Join commands including Curve utilities and Join Creation, linked geometry will be fixed at Current Timestamp allowing users to create holes where applicable.  
         
        """
        pass
    
    ## Setter for property: (bool) FixTimestamp

    ##  Returns the fix at timestamp preference.  
    ##    When WAVE Links are created by the Join commands including Curve utilities and Join Creation, linked geometry will be fixed at Current Timestamp allowing users to create holes where applicable.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @FixTimestamp.setter
    def FixTimestamp(self, fixTimestamp: bool):
        """
        Setter for property: (bool) FixTimestamp
         Returns the fix at timestamp preference.  
           When WAVE Links are created by the Join commands including Curve utilities and Join Creation, linked geometry will be fixed at Current Timestamp allowing users to create holes where applicable.  
         
        """
        pass
    
    ## Getter for property: (str) GroupIdSeedValue
    ##  Returns a join group ID seed value preference.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def GroupIdSeedValue(self) -> str:
        """
        Getter for property: (str) GroupIdSeedValue
         Returns a join group ID seed value preference.  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) GroupIdSeedValue

    ##  Returns a join group ID seed value preference.  
    ##   
    ##           
    ##  
    ## Setter License requirements: nx_join (" NX Join") OR nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @GroupIdSeedValue.setter
    def GroupIdSeedValue(self, groupIdSeedValue: str):
        """
        Setter for property: (str) GroupIdSeedValue
         Returns a join group ID seed value preference.  
          
                  
         
        """
        pass
    
    ## Getter for property: (int) NamingLowerLimit
    ##  Returns the naming lower limit preference.  
    ##    This option specifies the lower limit used to name the join features.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def NamingLowerLimit(self) -> int:
        """
        Getter for property: (int) NamingLowerLimit
         Returns the naming lower limit preference.  
           This option specifies the lower limit used to name the join features.  
         
        """
        pass
    
    ## Setter for property: (int) NamingLowerLimit

    ##  Returns the naming lower limit preference.  
    ##    This option specifies the lower limit used to name the join features.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NamingLowerLimit.setter
    def NamingLowerLimit(self, namingLowerLimit: int):
        """
        Setter for property: (int) NamingLowerLimit
         Returns the naming lower limit preference.  
           This option specifies the lower limit used to name the join features.  
         
        """
        pass
    
    ## Getter for property: (int) NamingUpperLimit
    ##  Returns the naming upper limit preference.  
    ##    This option specifies the upper limit used to name the join features.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def NamingUpperLimit(self) -> int:
        """
        Getter for property: (int) NamingUpperLimit
         Returns the naming upper limit preference.  
           This option specifies the upper limit used to name the join features.  
         
        """
        pass
    
    ## Setter for property: (int) NamingUpperLimit

    ##  Returns the naming upper limit preference.  
    ##    This option specifies the upper limit used to name the join features.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NamingUpperLimit.setter
    def NamingUpperLimit(self, namingUpperLimit: int):
        """
        Setter for property: (int) NamingUpperLimit
         Returns the naming upper limit preference.  
           This option specifies the upper limit used to name the join features.  
         
        """
        pass
    
import NXOpen
##  Represents a RulesBasedJoinBulkCreateBuilder class  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateRulesBasedJoinBulkCreateBuilder  NXOpen::Join::JoinManager::CreateRulesBasedJoinBulkCreateBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class RulesBasedJoinBulkCreateBuilder(CurveJoinBuilder): 
    """ Represents a RulesBasedJoinBulkCreateBuilder class """


    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) BodySelection
    ##  Returns the body selection   
    ##     
    ##  
    ## Getter License requirements: nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def BodySelection(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) BodySelection
         Returns the body selection   
            
         
        """
        pass
    
    ## Getter for property: (bool) CombineWelds
    ##  Returns the indication to combine welds if tool faces are from same body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def CombineWelds(self) -> bool:
        """
        Getter for property: (bool) CombineWelds
         Returns the indication to combine welds if tool faces are from same body.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CombineWelds

    ##  Returns the indication to combine welds if tool faces are from same body.  
    ##      
    ##  
    ## Setter License requirements: nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @CombineWelds.setter
    def CombineWelds(self, status: bool):
        """
        Setter for property: (bool) CombineWelds
         Returns the indication to combine welds if tool faces are from same body.  
             
         
        """
        pass
    
    ## Getter for property: (bool) DuplicateCheck
    ##  Returns the indication to not create features if they would overlay existing curve join features.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def DuplicateCheck(self) -> bool:
        """
        Getter for property: (bool) DuplicateCheck
         Returns the indication to not create features if they would overlay existing curve join features.  
             
         
        """
        pass
    
    ## Setter for property: (bool) DuplicateCheck

    ##  Returns the indication to not create features if they would overlay existing curve join features.  
    ##      
    ##  
    ## Setter License requirements: nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DuplicateCheck.setter
    def DuplicateCheck(self, status: bool):
        """
        Setter for property: (bool) DuplicateCheck
         Returns the indication to not create features if they would overlay existing curve join features.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaximumBodyGap
    ##  Returns the maximum distance used when determining if two bodies are coincident.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def MaximumBodyGap(self) -> float:
        """
        Getter for property: (float) MaximumBodyGap
         Returns the maximum distance used when determining if two bodies are coincident.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaximumBodyGap

    ##  Returns the maximum distance used when determining if two bodies are coincident.  
    ##      
    ##  
    ## Setter License requirements: nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @MaximumBodyGap.setter
    def MaximumBodyGap(self, gapValue: float):
        """
        Setter for property: (float) MaximumBodyGap
         Returns the maximum distance used when determining if two bodies are coincident.  
             
         
        """
        pass
    
    ## Getter for property: (str) SubtypeId
    ##  Returns the Subtype   
    ##     
    ##  
    ## Getter License requirements: nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return str
    @property
    def SubtypeId(self) -> str:
        """
        Getter for property: (str) SubtypeId
         Returns the Subtype   
            
         
        """
        pass
    
    ## Setter for property: (str) SubtypeId

    ##  Returns the Subtype   
    ##     
    ##  
    ## Setter License requirements: nx_join_structures (" Automated Structure Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SubtypeId.setter
    def SubtypeId(self, type: str):
        """
        Setter for property: (str) SubtypeId
         Returns the Subtype   
            
         
        """
        pass
    
import NXOpen
##  Represents a SubtypeAuthorAddNewAttributesBuilder class  <br> To create a new instance of this class, use @link NXOpen::Join::SubtypeAuthorBuilder::CreateSubtypeAuthorAddNewAttributesBuilder  NXOpen::Join::SubtypeAuthorBuilder::CreateSubtypeAuthorAddNewAttributesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DataType </term> <description> 
##  
## Boolean </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2406.0.0  <br> 

class SubtypeAuthorAddNewAttributesBuilder(NXOpen.Builder): 
    """ Represents a SubtypeAuthorAddNewAttributesBuilder class """


    ##  the data type enum 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Boolean</term><description> 
    ## </description> </item><item><term> 
    ## Integer</term><description> 
    ## </description> </item><item><term> 
    ## Double</term><description> 
    ## </description> </item><item><term> 
    ## String</term><description> 
    ## </description> </item></list>
    class DataTypes(Enum):
        """
        Members Include: <Boolean> <Integer> <Double> <String>
        """
        Boolean: int
        Integer: int
        Double: int
        String: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubtypeAuthorAddNewAttributesBuilder.DataTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SubtypeAuthorAddNewAttributesBuilder.DataTypes NXOpen.Join.SubtypeAuthorAddNewAttributesBuilder.DataTypes@endlink) DataType
    ##  Returns the data type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return SubtypeAuthorAddNewAttributesBuilder.DataTypes
    @property
    def DataType(self) -> SubtypeAuthorAddNewAttributesBuilder.DataTypes:
        """
        Getter for property: (@link SubtypeAuthorAddNewAttributesBuilder.DataTypes NXOpen.Join.SubtypeAuthorAddNewAttributesBuilder.DataTypes@endlink) DataType
         Returns the data type   
            
         
        """
        pass
    
    ## Setter for property: (@link SubtypeAuthorAddNewAttributesBuilder.DataTypes NXOpen.Join.SubtypeAuthorAddNewAttributesBuilder.DataTypes@endlink) DataType

    ##  Returns the data type   
    ##     
    ##  
    ## Setter License requirements: nx_join_advanced (" NX Join Advanced Functionality")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @DataType.setter
    def DataType(self, dataType: SubtypeAuthorAddNewAttributesBuilder.DataTypes):
        """
        Setter for property: (@link SubtypeAuthorAddNewAttributesBuilder.DataTypes NXOpen.Join.SubtypeAuthorAddNewAttributesBuilder.DataTypes@endlink) DataType
         Returns the data type   
            
         
        """
        pass
    
    ## Getter for property: (str) StringValue
    ##  Returns the string value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def StringValue(self) -> str:
        """
        Getter for property: (str) StringValue
         Returns the string value   
            
         
        """
        pass
    
    ## Setter for property: (str) StringValue

    ##  Returns the string value   
    ##     
    ##  
    ## Setter License requirements: nx_join_advanced (" NX Join Advanced Functionality")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @StringValue.setter
    def StringValue(self, stringValue: str):
        """
        Setter for property: (str) StringValue
         Returns the string value   
            
         
        """
        pass
    
import NXOpen
##  Represents a SubtypeAuthorValidValuesBuilder class  <br> To create a new instance of this class, use @link NXOpen::Join::SubtypeAuthorBuilder::CreateSubtypeAuthorValidValuesBuilder  NXOpen::Join::SubtypeAuthorBuilder::CreateSubtypeAuthorValidValuesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ConstraintType </term> <description> 
##  
## Equals </description> </item> 
## 
## <item><term> 
##  
## DoubleValue </term> <description> 
##  
## 0.0 </description> </item> 
## 
## <item><term> 
##  
## IntValue </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2406.0.0  <br> 

class SubtypeAuthorValidValuesBuilder(NXOpen.Builder): 
    """ Represents a SubtypeAuthorValidValuesBuilder class """


    ##  the constraint type enum 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Equals</term><description> 
    ## </description> </item><item><term> 
    ## Min</term><description> 
    ## </description> </item><item><term> 
    ## Max</term><description> 
    ## </description> </item><item><term> 
    ## MinInclusive</term><description> 
    ## </description> </item><item><term> 
    ## MaxInclusive</term><description> 
    ## </description> </item><item><term> 
    ## NotEquals</term><description> 
    ## </description> </item><item><term> 
    ## Contains</term><description> 
    ## </description> </item><item><term> 
    ## DoesNotContain</term><description> 
    ## </description> </item><item><term> 
    ## BeginsWith</term><description> 
    ## </description> </item><item><term> 
    ## EndsWith</term><description> 
    ## </description> </item></list>
    class ConstraintTypes(Enum):
        """
        Members Include: <Equals> <Min> <Max> <MinInclusive> <MaxInclusive> <NotEquals> <Contains> <DoesNotContain> <BeginsWith> <EndsWith>
        """
        Equals: int
        Min: int
        Max: int
        MinInclusive: int
        MaxInclusive: int
        NotEquals: int
        Contains: int
        DoesNotContain: int
        BeginsWith: int
        EndsWith: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubtypeAuthorValidValuesBuilder.ConstraintTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SubtypeAuthorValidValuesBuilder.ConstraintTypes NXOpen.Join.SubtypeAuthorValidValuesBuilder.ConstraintTypes@endlink) ConstraintType
    ##  Returns the constraint   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return SubtypeAuthorValidValuesBuilder.ConstraintTypes
    @property
    def ConstraintType(self) -> SubtypeAuthorValidValuesBuilder.ConstraintTypes:
        """
        Getter for property: (@link SubtypeAuthorValidValuesBuilder.ConstraintTypes NXOpen.Join.SubtypeAuthorValidValuesBuilder.ConstraintTypes@endlink) ConstraintType
         Returns the constraint   
            
         
        """
        pass
    
    ## Setter for property: (@link SubtypeAuthorValidValuesBuilder.ConstraintTypes NXOpen.Join.SubtypeAuthorValidValuesBuilder.ConstraintTypes@endlink) ConstraintType

    ##  Returns the constraint   
    ##     
    ##  
    ## Setter License requirements: nx_join_advanced (" NX Join Advanced Functionality")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ConstraintType.setter
    def ConstraintType(self, constraint: SubtypeAuthorValidValuesBuilder.ConstraintTypes):
        """
        Setter for property: (@link SubtypeAuthorValidValuesBuilder.ConstraintTypes NXOpen.Join.SubtypeAuthorValidValuesBuilder.ConstraintTypes@endlink) ConstraintType
         Returns the constraint   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleValue
    ##  Returns the double value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return float
    @property
    def DoubleValue(self) -> float:
        """
        Getter for property: (float) DoubleValue
         Returns the double value   
            
         
        """
        pass
    
    ## Setter for property: (float) DoubleValue

    ##  Returns the double value   
    ##     
    ##  
    ## Setter License requirements: nx_join_advanced (" NX Join Advanced Functionality")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @DoubleValue.setter
    def DoubleValue(self, doubleValue: float):
        """
        Setter for property: (float) DoubleValue
         Returns the double value   
            
         
        """
        pass
    
    ## Getter for property: (int) IntValue
    ##  Returns the int value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def IntValue(self) -> int:
        """
        Getter for property: (int) IntValue
         Returns the int value   
            
         
        """
        pass
    
    ## Setter for property: (int) IntValue

    ##  Returns the int value   
    ##     
    ##  
    ## Setter License requirements: nx_join_advanced (" NX Join Advanced Functionality")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @IntValue.setter
    def IntValue(self, intValue: int):
        """
        Setter for property: (int) IntValue
         Returns the int value   
            
         
        """
        pass
    
    ## Getter for property: (str) StringValue
    ##  Returns the string value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def StringValue(self) -> str:
        """
        Getter for property: (str) StringValue
         Returns the string value   
            
         
        """
        pass
    
    ## Setter for property: (str) StringValue

    ##  Returns the string value   
    ##     
    ##  
    ## Setter License requirements: nx_join_advanced (" NX Join Advanced Functionality")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @StringValue.setter
    def StringValue(self, stringValue: str):
        """
        Setter for property: (str) StringValue
         Returns the string value   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a @link NXOpen::Join::TransformBuilder NXOpen::Join::TransformBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateTransformBuilder  NXOpen::Join::JoinManager::CreateTransformBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class TransformBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a <ja_class>NXOpen.Join.TransformBuilder</ja_class> builder """


    ##  The associativity types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SourceJoin</term><description> 
    ##  Associative to source join. </description> </item><item><term> 
    ## DestinationGeometry</term><description> 
    ##  Associative to Destination geometry. </description> </item></list>
    class AssociativityTypes(Enum):
        """
        Members Include: <SourceJoin> <DestinationGeometry>
        """
        SourceJoin: int
        DestinationGeometry: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TransformBuilder.AssociativityTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The transformation types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Mirror</term><description> 
    ##  Mirror </description> </item><item><term> 
    ## Translate</term><description> 
    ##  Translate </description> </item></list>
    class TransformationTypes(Enum):
        """
        Members Include: <Mirror> <Translate>
        """
        Mirror: int
        Translate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TransformBuilder.TransformationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) Associative
    ##  Returns the indication to create associative feature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the indication to create associative feature   
            
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##  Returns the indication to create associative feature   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the indication to create associative feature   
            
         
        """
        pass
    
    ## Getter for property: (@link TransformBuilder.AssociativityTypes NXOpen.Join.TransformBuilder.AssociativityTypes@endlink) AssociativityType
    ##  Returns the associativity type   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return TransformBuilder.AssociativityTypes
    @property
    def AssociativityType(self) -> TransformBuilder.AssociativityTypes:
        """
        Getter for property: (@link TransformBuilder.AssociativityTypes NXOpen.Join.TransformBuilder.AssociativityTypes@endlink) AssociativityType
         Returns the associativity type   
            
         
        """
        pass
    
    ## Setter for property: (@link TransformBuilder.AssociativityTypes NXOpen.Join.TransformBuilder.AssociativityTypes@endlink) AssociativityType

    ##  Returns the associativity type   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @AssociativityType.setter
    def AssociativityType(self, associativityType: TransformBuilder.AssociativityTypes):
        """
        Setter for property: (@link TransformBuilder.AssociativityTypes NXOpen.Join.TransformBuilder.AssociativityTypes@endlink) AssociativityType
         Returns the associativity type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ConnectedPartTolerance
    ##  Returns the expression containing the value of the connected part tolerance.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ConnectedPartTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ConnectedPartTolerance
         Returns the expression containing the value of the connected part tolerance.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateHole
    ##  Returns the hole creation status.  
    ##    If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def CreateHole(self) -> bool:
        """
        Getter for property: (bool) CreateHole
         Returns the hole creation status.  
           If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies   
         
        """
        pass
    
    ## Setter for property: (bool) CreateHole

    ##  Returns the hole creation status.  
    ##    If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CreateHole.setter
    def CreateHole(self, status: bool):
        """
        Setter for property: (bool) CreateHole
         Returns the hole creation status.  
           If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies   
         
        """
        pass
    
    ## Getter for property: (bool) EditSettingsOnly
    ##  Returns the indication to only edit items in the settings group.  
    ##    Mainly @link NXOpen::Join::TransformBuilder::Associative NXOpen::Join::TransformBuilder::Associative@endlink , 
    ##             @link NXOpen::Join::TransformBuilder::LoadHardware NXOpen::Join::TransformBuilder::LoadHardware@endlink , and @link NXOpen::Join::TransformBuilder::CreateHole NXOpen::Join::TransformBuilder::CreateHole@endlink .
    ##             All other parameters will be left unchanged.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def EditSettingsOnly(self) -> bool:
        """
        Getter for property: (bool) EditSettingsOnly
         Returns the indication to only edit items in the settings group.  
           Mainly @link NXOpen::Join::TransformBuilder::Associative NXOpen::Join::TransformBuilder::Associative@endlink , 
                    @link NXOpen::Join::TransformBuilder::LoadHardware NXOpen::Join::TransformBuilder::LoadHardware@endlink , and @link NXOpen::Join::TransformBuilder::CreateHole NXOpen::Join::TransformBuilder::CreateHole@endlink .
                    All other parameters will be left unchanged.   
         
        """
        pass
    
    ## Setter for property: (bool) EditSettingsOnly

    ##  Returns the indication to only edit items in the settings group.  
    ##    Mainly @link NXOpen::Join::TransformBuilder::Associative NXOpen::Join::TransformBuilder::Associative@endlink , 
    ##             @link NXOpen::Join::TransformBuilder::LoadHardware NXOpen::Join::TransformBuilder::LoadHardware@endlink , and @link NXOpen::Join::TransformBuilder::CreateHole NXOpen::Join::TransformBuilder::CreateHole@endlink .
    ##             All other parameters will be left unchanged.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @EditSettingsOnly.setter
    def EditSettingsOnly(self, status: bool):
        """
        Setter for property: (bool) EditSettingsOnly
         Returns the indication to only edit items in the settings group.  
           Mainly @link NXOpen::Join::TransformBuilder::Associative NXOpen::Join::TransformBuilder::Associative@endlink , 
                    @link NXOpen::Join::TransformBuilder::LoadHardware NXOpen::Join::TransformBuilder::LoadHardware@endlink , and @link NXOpen::Join::TransformBuilder::CreateHole NXOpen::Join::TransformBuilder::CreateHole@endlink .
                    All other parameters will be left unchanged.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Features
    ##  Returns the join features to transform   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Features(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Features
         Returns the join features to transform   
            
         
        """
        pass
    
    ## Getter for property: (bool) LoadHardware
    ##  Returns the hardware load status.  
    ##    If true, loads hardware parts into assembly. If false, removes hardware parts.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def LoadHardware(self) -> bool:
        """
        Getter for property: (bool) LoadHardware
         Returns the hardware load status.  
           If true, loads hardware parts into assembly. If false, removes hardware parts.   
         
        """
        pass
    
    ## Setter for property: (bool) LoadHardware

    ##  Returns the hardware load status.  
    ##    If true, loads hardware parts into assembly. If false, removes hardware parts.   
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @LoadHardware.setter
    def LoadHardware(self, status: bool):
        """
        Setter for property: (bool) LoadHardware
         Returns the hardware load status.  
           If true, loads hardware parts into assembly. If false, removes hardware parts.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) MirrorPlane
    ##  Returns the mirror plane, used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesMirror   NXOpen::Join::TransformBuilder::TransformationTypesMirror @endlink    
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def MirrorPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) MirrorPlane
         Returns the mirror plane, used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesMirror   NXOpen::Join::TransformBuilder::TransformationTypesMirror @endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) MirrorPlane

    ##  Returns the mirror plane, used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesMirror   NXOpen::Join::TransformBuilder::TransformationTypesMirror @endlink    
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @MirrorPlane.setter
    def MirrorPlane(self, mirrorPlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) MirrorPlane
         Returns the mirror plane, used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesMirror   NXOpen::Join::TransformBuilder::TransformationTypesMirror @endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) TranslateCsys
    ##  Returns the coordinate system that defines the translate offset directions.  
    ##    If not specified the absolute coordinate system will be used.
    ##             Used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesTranslate   NXOpen::Join::TransformBuilder::TransformationTypesTranslate @endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def TranslateCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) TranslateCsys
         Returns the coordinate system that defines the translate offset directions.  
           If not specified the absolute coordinate system will be used.
                    Used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesTranslate   NXOpen::Join::TransformBuilder::TransformationTypesTranslate @endlink    
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) TranslateCsys

    ##  Returns the coordinate system that defines the translate offset directions.  
    ##    If not specified the absolute coordinate system will be used.
    ##             Used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesTranslate   NXOpen::Join::TransformBuilder::TransformationTypesTranslate @endlink    
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @TranslateCsys.setter
    def TranslateCsys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) TranslateCsys
         Returns the coordinate system that defines the translate offset directions.  
           If not specified the absolute coordinate system will be used.
                    Used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesTranslate   NXOpen::Join::TransformBuilder::TransformationTypesTranslate @endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TranslateX
    ##  Returns the expression containing the value of the x translation distance.  
    ##    
    ##             Used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesTranslate   NXOpen::Join::TransformBuilder::TransformationTypesTranslate @endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TranslateX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TranslateX
         Returns the expression containing the value of the x translation distance.  
           
                    Used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesTranslate   NXOpen::Join::TransformBuilder::TransformationTypesTranslate @endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TranslateY
    ##  Returns the expression containing the value of the y translation distance.  
    ##    
    ##             Used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesTranslate   NXOpen::Join::TransformBuilder::TransformationTypesTranslate @endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TranslateY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TranslateY
         Returns the expression containing the value of the y translation distance.  
           
                    Used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesTranslate   NXOpen::Join::TransformBuilder::TransformationTypesTranslate @endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TranslateZ
    ##  Returns the expression containing the value of the z translation distance.  
    ##    
    ##             Used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesTranslate   NXOpen::Join::TransformBuilder::TransformationTypesTranslate @endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TranslateZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TranslateZ
         Returns the expression containing the value of the z translation distance.  
           
                    Used when @link NXOpen::Join::TransformBuilder::TransformationTypes NXOpen::Join::TransformBuilder::TransformationTypes@endlink  is set to @link  NXOpen::Join::TransformBuilder::TransformationTypesTranslate   NXOpen::Join::TransformBuilder::TransformationTypesTranslate @endlink    
         
        """
        pass
    
    ## Getter for property: (@link TransformBuilder.TransformationTypes NXOpen.Join.TransformBuilder.TransformationTypes@endlink) Type
    ##  Returns the transformation type   
    ##     
    ##  
    ## Getter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return TransformBuilder.TransformationTypes
    @property
    def Type(self) -> TransformBuilder.TransformationTypes:
        """
        Getter for property: (@link TransformBuilder.TransformationTypes NXOpen.Join.TransformBuilder.TransformationTypes@endlink) Type
         Returns the transformation type   
            
         
        """
        pass
    
    ## Setter for property: (@link TransformBuilder.TransformationTypes NXOpen.Join.TransformBuilder.TransformationTypes@endlink) Type

    ##  Returns the transformation type   
    ##     
    ##  
    ## Setter License requirements: nx_join (" NX Join")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Type.setter
    def Type(self, transType: TransformBuilder.TransformationTypes):
        """
        Setter for property: (@link TransformBuilder.TransformationTypes NXOpen.Join.TransformBuilder.TransformationTypes@endlink) Type
         Returns the transformation type   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Annotations
##  the @link Builder::Commit Builder::Commit@endlink  can produce more than one object.  <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreateWeldSymbolBuilder  NXOpen::Join::JoinManager::CreateWeldSymbolBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class WeldSymbolBuilder(NXOpen.Builder): 
    """ the <ja_method>Builder.Commit</ja_method> can produce more than one object. """


    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Objects
    ##  Returns the objects (features) that are used to create Weld symbols.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Objects
         Returns the objects (features) that are used to create Weld symbols.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.PlaneBuilder NXOpen.Annotations.PlaneBuilder@endlink) Plane
    ##  Returns the @link Annotations::PlaneBuilder Annotations::PlaneBuilder@endlink  for the annotation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Annotations.PlaneBuilder
    @property
    def Plane(self) -> NXOpen.Annotations.PlaneBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.PlaneBuilder NXOpen.Annotations.PlaneBuilder@endlink) Plane
         Returns the @link Annotations::PlaneBuilder Annotations::PlaneBuilder@endlink  for the annotation.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.StyleBuilder NXOpen.Annotations.StyleBuilder@endlink) Style
    ##  Returns the @link Annotations::StyleBuilder Annotations::StyleBuilder@endlink  for the annotation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Annotations.StyleBuilder
    @property
    def Style(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.StyleBuilder NXOpen.Annotations.StyleBuilder@endlink) Style
         Returns the @link Annotations::StyleBuilder Annotations::StyleBuilder@endlink  for the annotation.  
             
         
        """
        pass
    
## @package NXOpen.Join
## Classes, Enums and Structs under NXOpen.Join namespace

##  @link AutoPointBuilderInterferenceDetails NXOpen.Join.AutoPointBuilderInterferenceDetails @endlink is an alias for @link AutoPointBuilder.InterferenceDetails NXOpen.Join.AutoPointBuilder.InterferenceDetails@endlink
AutoPointBuilderInterferenceDetails = AutoPointBuilder.InterferenceDetails


##  @link CurveJoinBuilderBodyType NXOpen.Join.CurveJoinBuilderBodyType @endlink is an alias for @link CurveJoinBuilder.BodyType NXOpen.Join.CurveJoinBuilder.BodyType@endlink
CurveJoinBuilderBodyType = CurveJoinBuilder.BodyType


##  @link CurveJoinBuilderConnectedPartsType NXOpen.Join.CurveJoinBuilderConnectedPartsType @endlink is an alias for @link CurveJoinBuilder.ConnectedPartsType NXOpen.Join.CurveJoinBuilder.ConnectedPartsType@endlink
CurveJoinBuilderConnectedPartsType = CurveJoinBuilder.ConnectedPartsType


##  @link CurveJoinBuilderContourType NXOpen.Join.CurveJoinBuilderContourType @endlink is an alias for @link CurveJoinBuilder.ContourType NXOpen.Join.CurveJoinBuilder.ContourType@endlink
CurveJoinBuilderContourType = CurveJoinBuilder.ContourType


##  @link CurveJoinBuilderEdgePrepType NXOpen.Join.CurveJoinBuilderEdgePrepType @endlink is an alias for @link CurveJoinBuilder.EdgePrepType NXOpen.Join.CurveJoinBuilder.EdgePrepType@endlink
CurveJoinBuilderEdgePrepType = CurveJoinBuilder.EdgePrepType


##  @link CurveJoinBuilderFillFaceSlotsOnSetType NXOpen.Join.CurveJoinBuilderFillFaceSlotsOnSetType @endlink is an alias for @link CurveJoinBuilder.FillFaceSlotsOnSetType NXOpen.Join.CurveJoinBuilder.FillFaceSlotsOnSetType@endlink
CurveJoinBuilderFillFaceSlotsOnSetType = CurveJoinBuilder.FillFaceSlotsOnSetType


##  @link CurveJoinBuilderLapFilletLocationOption NXOpen.Join.CurveJoinBuilderLapFilletLocationOption @endlink is an alias for @link CurveJoinBuilder.LapFilletLocationOption NXOpen.Join.CurveJoinBuilder.LapFilletLocationOption@endlink
CurveJoinBuilderLapFilletLocationOption = CurveJoinBuilder.LapFilletLocationOption


##  @link CurveJoinBuilderShapeType NXOpen.Join.CurveJoinBuilderShapeType @endlink is an alias for @link CurveJoinBuilder.ShapeType NXOpen.Join.CurveJoinBuilder.ShapeType@endlink
CurveJoinBuilderShapeType = CurveJoinBuilder.ShapeType


##  @link CurveJoinBuilderSkipFeatureType NXOpen.Join.CurveJoinBuilderSkipFeatureType @endlink is an alias for @link CurveJoinBuilder.SkipFeatureType NXOpen.Join.CurveJoinBuilder.SkipFeatureType@endlink
CurveJoinBuilderSkipFeatureType = CurveJoinBuilder.SkipFeatureType


##  @link CurveJoinBuilderTaperType NXOpen.Join.CurveJoinBuilderTaperType @endlink is an alias for @link CurveJoinBuilder.TaperType NXOpen.Join.CurveJoinBuilder.TaperType@endlink
CurveJoinBuilderTaperType = CurveJoinBuilder.TaperType


##  @link EditCurveJoinParametersBuilderOption NXOpen.Join.EditCurveJoinParametersBuilderOption @endlink is an alias for @link EditCurveJoinParametersBuilder.Option NXOpen.Join.EditCurveJoinParametersBuilder.Option@endlink
EditCurveJoinParametersBuilderOption = EditCurveJoinParametersBuilder.Option


##  @link ExportJoinBuilderOutputType NXOpen.Join.ExportJoinBuilderOutputType @endlink is an alias for @link ExportJoinBuilder.OutputType NXOpen.Join.ExportJoinBuilder.OutputType@endlink
ExportJoinBuilderOutputType = ExportJoinBuilder.OutputType


##  @link FaceJoinBuilderBoundaryMethodType NXOpen.Join.FaceJoinBuilderBoundaryMethodType @endlink is an alias for @link FaceJoinBuilder.BoundaryMethodType NXOpen.Join.FaceJoinBuilder.BoundaryMethodType@endlink
FaceJoinBuilderBoundaryMethodType = FaceJoinBuilder.BoundaryMethodType


##  @link FaceJoinBuilderHolesCoverageType NXOpen.Join.FaceJoinBuilderHolesCoverageType @endlink is an alias for @link FaceJoinBuilder.HolesCoverageType NXOpen.Join.FaceJoinBuilder.HolesCoverageType@endlink
FaceJoinBuilderHolesCoverageType = FaceJoinBuilder.HolesCoverageType


##  @link FaceJoinBuilderOrientationTypes NXOpen.Join.FaceJoinBuilderOrientationTypes @endlink is an alias for @link FaceJoinBuilder.OrientationTypes NXOpen.Join.FaceJoinBuilder.OrientationTypes@endlink
FaceJoinBuilderOrientationTypes = FaceJoinBuilder.OrientationTypes


##  @link FaceJoinBuilderVisualizationBodyType NXOpen.Join.FaceJoinBuilderVisualizationBodyType @endlink is an alias for @link FaceJoinBuilder.VisualizationBodyType NXOpen.Join.FaceJoinBuilder.VisualizationBodyType@endlink
FaceJoinBuilderVisualizationBodyType = FaceJoinBuilder.VisualizationBodyType


##  @link FaceJoinBuilderVisualizationLocationType NXOpen.Join.FaceJoinBuilderVisualizationLocationType @endlink is an alias for @link FaceJoinBuilder.VisualizationLocationType NXOpen.Join.FaceJoinBuilder.VisualizationLocationType@endlink
FaceJoinBuilderVisualizationLocationType = FaceJoinBuilder.VisualizationLocationType


##  @link GroupJoinsBuilderGroupingMethod NXOpen.Join.GroupJoinsBuilderGroupingMethod @endlink is an alias for @link GroupJoinsBuilder.GroupingMethod NXOpen.Join.GroupJoinsBuilder.GroupingMethod@endlink
GroupJoinsBuilderGroupingMethod = GroupJoinsBuilder.GroupingMethod


##  @link ImportJoinBuilderOutputType NXOpen.Join.ImportJoinBuilderOutputType @endlink is an alias for @link ImportJoinBuilder.OutputType NXOpen.Join.ImportJoinBuilder.OutputType@endlink
ImportJoinBuilderOutputType = ImportJoinBuilder.OutputType


##  @link JoinBuilderDestinationTypes NXOpen.Join.JoinBuilderDestinationTypes @endlink is an alias for @link JoinBuilder.DestinationTypes NXOpen.Join.JoinBuilder.DestinationTypes@endlink
JoinBuilderDestinationTypes = JoinBuilder.DestinationTypes


##  @link JoinBuilderMaterialAssignmentPolicyType NXOpen.Join.JoinBuilderMaterialAssignmentPolicyType @endlink is an alias for @link JoinBuilder.MaterialAssignmentPolicyType NXOpen.Join.JoinBuilder.MaterialAssignmentPolicyType@endlink
JoinBuilderMaterialAssignmentPolicyType = JoinBuilder.MaterialAssignmentPolicyType


##  @link JoinedFinderBuilderFilterTypes NXOpen.Join.JoinedFinderBuilderFilterTypes @endlink is an alias for @link JoinedFinderBuilder.FilterTypes NXOpen.Join.JoinedFinderBuilder.FilterTypes@endlink
JoinedFinderBuilderFilterTypes = JoinedFinderBuilder.FilterTypes


##  @link JoinManagerCallbackReason NXOpen.Join.JoinManagerCallbackReason @endlink is an alias for @link JoinManager.CallbackReason NXOpen.Join.JoinManager.CallbackReason@endlink
JoinManagerCallbackReason = JoinManager.CallbackReason


##  @link OverlapBuilderConnectPartTypes NXOpen.Join.OverlapBuilderConnectPartTypes @endlink is an alias for @link OverlapBuilder.ConnectPartTypes NXOpen.Join.OverlapBuilder.ConnectPartTypes@endlink
OverlapBuilderConnectPartTypes = OverlapBuilder.ConnectPartTypes


##  @link OverlapBuilderGuideCurveCreationTypes NXOpen.Join.OverlapBuilderGuideCurveCreationTypes @endlink is an alias for @link OverlapBuilder.GuideCurveCreationTypes NXOpen.Join.OverlapBuilder.GuideCurveCreationTypes@endlink
OverlapBuilderGuideCurveCreationTypes = OverlapBuilder.GuideCurveCreationTypes


##  @link OverlapBuilderInputDataTypes NXOpen.Join.OverlapBuilderInputDataTypes @endlink is an alias for @link OverlapBuilder.InputDataTypes NXOpen.Join.OverlapBuilder.InputDataTypes@endlink
OverlapBuilderInputDataTypes = OverlapBuilder.InputDataTypes


##  @link OverlapBuilderReferenceSheetOptionTypes NXOpen.Join.OverlapBuilderReferenceSheetOptionTypes @endlink is an alias for @link OverlapBuilder.ReferenceSheetOptionTypes NXOpen.Join.OverlapBuilder.ReferenceSheetOptionTypes@endlink
OverlapBuilderReferenceSheetOptionTypes = OverlapBuilder.ReferenceSheetOptionTypes


##  @link OverlapBuilderReferenceSheetTypes NXOpen.Join.OverlapBuilderReferenceSheetTypes @endlink is an alias for @link OverlapBuilder.ReferenceSheetTypes NXOpen.Join.OverlapBuilder.ReferenceSheetTypes@endlink
OverlapBuilderReferenceSheetTypes = OverlapBuilder.ReferenceSheetTypes


##  @link OverlapGuideBuilderMethod NXOpen.Join.OverlapGuideBuilderMethod @endlink is an alias for @link OverlapGuideBuilder.Method NXOpen.Join.OverlapGuideBuilder.Method@endlink
OverlapGuideBuilderMethod = OverlapGuideBuilder.Method


##  @link PointJoinBuilderHoleTypes NXOpen.Join.PointJoinBuilderHoleTypes @endlink is an alias for @link PointJoinBuilder.HoleTypes NXOpen.Join.PointJoinBuilder.HoleTypes@endlink
PointJoinBuilderHoleTypes = PointJoinBuilder.HoleTypes


##  @link PointJoinBuilderStackupAlignmentTypes NXOpen.Join.PointJoinBuilderStackupAlignmentTypes @endlink is an alias for @link PointJoinBuilder.StackupAlignmentTypes NXOpen.Join.PointJoinBuilder.StackupAlignmentTypes@endlink
PointJoinBuilderStackupAlignmentTypes = PointJoinBuilder.StackupAlignmentTypes


##  @link PointJoinBuilderVisualizationGeometryType NXOpen.Join.PointJoinBuilderVisualizationGeometryType @endlink is an alias for @link PointJoinBuilder.VisualizationGeometryType NXOpen.Join.PointJoinBuilder.VisualizationGeometryType@endlink
PointJoinBuilderVisualizationGeometryType = PointJoinBuilder.VisualizationGeometryType


##  @link PointJoinHardwareAttributeDataSourceType NXOpen.Join.PointJoinHardwareAttributeDataSourceType @endlink is an alias for @link PointJoinHardware.AttributeDataSourceType NXOpen.Join.PointJoinHardware.AttributeDataSourceType@endlink
PointJoinHardwareAttributeDataSourceType = PointJoinHardware.AttributeDataSourceType


##  @link PointLayoutBuilderSpaceMethod NXOpen.Join.PointLayoutBuilderSpaceMethod @endlink is an alias for @link PointLayoutBuilder.SpaceMethod NXOpen.Join.PointLayoutBuilder.SpaceMethod@endlink
PointLayoutBuilderSpaceMethod = PointLayoutBuilder.SpaceMethod


##  @link PointLayoutBuilderSpaceOption NXOpen.Join.PointLayoutBuilderSpaceOption @endlink is an alias for @link PointLayoutBuilder.SpaceOption NXOpen.Join.PointLayoutBuilder.SpaceOption@endlink
PointLayoutBuilderSpaceOption = PointLayoutBuilder.SpaceOption


##  @link PointLayoutBuilderSpacingTypes NXOpen.Join.PointLayoutBuilderSpacingTypes @endlink is an alias for @link PointLayoutBuilder.SpacingTypes NXOpen.Join.PointLayoutBuilder.SpacingTypes@endlink
PointLayoutBuilderSpacingTypes = PointLayoutBuilder.SpacingTypes


##  @link PointLayoutPointBuilderPointPosition NXOpen.Join.PointLayoutPointBuilderPointPosition @endlink is an alias for @link PointLayoutPointBuilder.PointPosition NXOpen.Join.PointLayoutPointBuilder.PointPosition@endlink
PointLayoutPointBuilderPointPosition = PointLayoutPointBuilder.PointPosition


##  @link SubtypeAuthorAddNewAttributesBuilderDataTypes NXOpen.Join.SubtypeAuthorAddNewAttributesBuilderDataTypes @endlink is an alias for @link SubtypeAuthorAddNewAttributesBuilder.DataTypes NXOpen.Join.SubtypeAuthorAddNewAttributesBuilder.DataTypes@endlink
SubtypeAuthorAddNewAttributesBuilderDataTypes = SubtypeAuthorAddNewAttributesBuilder.DataTypes


##  @link SubtypeAuthorValidValuesBuilderConstraintTypes NXOpen.Join.SubtypeAuthorValidValuesBuilderConstraintTypes @endlink is an alias for @link SubtypeAuthorValidValuesBuilder.ConstraintTypes NXOpen.Join.SubtypeAuthorValidValuesBuilder.ConstraintTypes@endlink
SubtypeAuthorValidValuesBuilderConstraintTypes = SubtypeAuthorValidValuesBuilder.ConstraintTypes


##  @link TransformBuilderAssociativityTypes NXOpen.Join.TransformBuilderAssociativityTypes @endlink is an alias for @link TransformBuilder.AssociativityTypes NXOpen.Join.TransformBuilder.AssociativityTypes@endlink
TransformBuilderAssociativityTypes = TransformBuilder.AssociativityTypes


##  @link TransformBuilderTransformationTypes NXOpen.Join.TransformBuilderTransformationTypes @endlink is an alias for @link TransformBuilder.TransformationTypes NXOpen.Join.TransformBuilder.TransformationTypes@endlink
TransformBuilderTransformationTypes = TransformBuilder.TransformationTypes


