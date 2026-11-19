from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.CAM
##  Represents a feature geometry builder  <br> This is an abstract class and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX9.0.1  <br> 

class FeatureGeometry(NXOpen.CAM.Geometry): 
    """ Represents a feature geometry builder """


    ##  the direction types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Xm</term><description> 
    ##  Direction: XM </description> </item><item><term> 
    ## Ym</term><description> 
    ##  Direction: YM </description> </item><item><term> 
    ## Zm</term><description> 
    ##  Direction: ZM </description> </item><item><term> 
    ## Vector</term><description> 
    ##  Direction: Vector </description> </item></list>
    class SequenceDirectionType(Enum):
        """
        Members Include: <Xm> <Ym> <Zm> <Vector>
        """
        Xm: int
        Ym: int
        Zm: int
        Vector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FeatureGeometry.SequenceDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the pattern types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Zig</term><description> 
    ##  Pattern: Zig </description> </item><item><term> 
    ## ZigZag</term><description> 
    ##  Pattern: Zig Zag </description> </item></list>
    class SequencePatternType(Enum):
        """
        Members Include: <Zig> <ZigZag>
        """
        Zig: int
        ZigZag: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FeatureGeometry.SequencePatternType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the optimization types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Closest</term><description> 
    ##  Sort order: Closet </description> </item><item><term> 
    ## ShortestPath</term><description> 
    ##  Sort order: Shortest Path </description> </item><item><term> 
    ## PrimaryDirection</term><description> 
    ##  Sort order: Primary Direction </description> </item></list>
    class SortOrder(Enum):
        """
        Members Include: <Closest> <ShortestPath> <PrimaryDirection>
        """
        Closest: int
        ShortestPath: int
        PrimaryDirection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FeatureGeometry.SortOrder:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) UseModelDepth
    ##  Returns the use model depth flag   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return bool
    @property
    def UseModelDepth(self) -> bool:
        """
        Getter for property: (bool) UseModelDepth
         Returns the use model depth flag   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseModelDepth

    ##  Returns the use model depth flag   
    ##     
    ##  
    ## Setter License requirements: cam_base ("CAM BASE")
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    @UseModelDepth.setter
    def UseModelDepth(self, flag: bool):
        """
        Setter for property: (bool) UseModelDepth
         Returns the use model depth flag   
            
         
        """
        pass
    
    ##  Creates a feature geometry set 
    ##  @return ppFeatureBuilder (@link FeatureSet NXOpen.CAM.FBM.FeatureSet@endlink):  the new in process feature set .
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## 
    ## <param name="tagMachiningFeature"> (@link NXOpen.CAM.CAMFeature NXOpen.CAM.CAMFeature@endlink)  the machining feature </param>
    ## <param name="featureType"> (str)  the in process feature type </param>
    def AddFeatureSet(self, tagMachiningFeature: NXOpen.CAM.CAMFeature, featureType: str) -> FeatureSet:
        """
         Creates a feature geometry set 
         @return ppFeatureBuilder (@link FeatureSet NXOpen.CAM.FBM.FeatureSet@endlink):  the new in process feature set .
        """
        pass
    
    ##  Create a new empty feature editor
    ##  @return ppFeatureBuilder (@link FeatureSet NXOpen.CAM.FBM.FeatureSet@endlink):  the new in process feature set .
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    def CreateFeatureSet(self) -> FeatureSet:
        """
         Create a new empty feature editor
         @return ppFeatureBuilder (@link FeatureSet NXOpen.CAM.FBM.FeatureSet@endlink):  the new in process feature set .
        """
        pass
    
    ##  Create a series of (in process) features. Depending on the input objects feature recognition is performed. When
    ##                 no known features can be recognized, tagged features are created of type featureType 
    ##  @return features (@link Feature List[NXOpen.CAM.FBM.Feature]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## 
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  the geometry objects, can also be machining features </param>
    ## <param name="featureType"> (str)  the machining feature type of the implictly created features when feature recognition fails </param>
    def CreateFeatures(self, objects: List[NXOpen.NXObject], featureType: str) -> List[Feature]:
        """
         Create a series of (in process) features. Depending on the input objects feature recognition is performed. When
                        no known features can be recognized, tagged features are created of type featureType 
         @return features (@link Feature List[NXOpen.CAM.FBM.Feature]@endlink): .
        """
        pass
    
    ##  Get the in process feature editor at the specified index 
    ##  @return ppFeatureBuilder (@link FeatureSet NXOpen.CAM.FBM.FeatureSet@endlink):  the in process feature set .
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## 
    ## <param name="nIndex"> (int)  the index of the feature set editor </param>
    def GetFeatureSet(self, nIndex: int) -> FeatureSet:
        """
         Get the in process feature editor at the specified index 
         @return ppFeatureBuilder (@link FeatureSet NXOpen.CAM.FBM.FeatureSet@endlink):  the in process feature set .
        """
        pass
    
    ##  Returns the machining area 
    ##  @return machiningArea (str):  the machining area .
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## License requirements: None.
    def GetMachiningArea(self) -> str:
        """
         Returns the machining area 
         @return machiningArea (str):  the machining area .
        """
        pass
    
    ##  Reload list from parent 
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## License requirements: cam_base ("CAM BASE")
    def ReloadList(self) -> None:
        """
         Reload list from parent 
        """
        pass
    
    ##  Reorders the features according to a predefined algorithm 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## 
    ## <param name="sortType"> (@link FeatureGeometry.SortOrder NXOpen.CAM.FBM.FeatureGeometry.SortOrder@endlink) </param>
    def ReorderFeatures(self, sortType: FeatureGeometry.SortOrder) -> None:
        """
         Reorders the features according to a predefined algorithm 
        """
        pass
    
    ##  Reorders the features according to primary direction 
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="builder"> (@link FeatureGeometry NXOpen.CAM.FBM.FeatureGeometry@endlink) </param>
    ## <param name="direction"> (@link FeatureGeometry.SequenceDirectionType NXOpen.CAM.FBM.FeatureGeometry.SequenceDirectionType@endlink) </param>
    ## <param name="pattern"> (@link FeatureGeometry.SequencePatternType NXOpen.CAM.FBM.FeatureGeometry.SequencePatternType@endlink) </param>
    ## <param name="vecValue"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    @overload
    def ReorderFeaturesByDirection(self, direction: FeatureGeometry.SequenceDirectionType, pattern: FeatureGeometry.SequencePatternType, vecValue: NXOpen.Vector3d) -> None:
        """
         Reorders the features according to primary direction 
        """
        pass
    
    ##  Reorders the features according to primary direction with band width 
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="builder"> (@link FeatureGeometry NXOpen.CAM.FBM.FeatureGeometry@endlink) </param>
    ## <param name="direction"> (@link FeatureGeometry.SequenceDirectionType NXOpen.CAM.FBM.FeatureGeometry.SequenceDirectionType@endlink) </param>
    ## <param name="pattern"> (@link FeatureGeometry.SequencePatternType NXOpen.CAM.FBM.FeatureGeometry.SequencePatternType@endlink) </param>
    ## <param name="vecValue"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    ## <param name="bandWidth"> (float) </param>
    @overload
    def ReorderFeaturesByDirection(self, direction: FeatureGeometry.SequenceDirectionType, pattern: FeatureGeometry.SequencePatternType, vecValue: NXOpen.Vector3d, bandWidth: float) -> None:
        """
         Reorders the features according to primary direction with band width 
        """
        pass
    
    ##  Reverse the features 
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## License requirements: cam_base ("CAM BASE")
    def ReverseFeatures(self) -> None:
        """
         Reverse the features 
        """
        pass
    
    ##  Sets a default attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="builder"> (@link FeatureGeometry NXOpen.CAM.FBM.FeatureGeometry@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="dValue"> (float)  the attribute value </param>
    @overload
    def SetDefaultAttribute(self, attributeName: str, dValue: float) -> None:
        """
         Sets a default attribute value 
        """
        pass
    
    ##  Sets a default attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="builder"> (@link FeatureGeometry NXOpen.CAM.FBM.FeatureGeometry@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="strValue"> (str)  the attribute value </param>
    @overload
    def SetDefaultAttribute(self, attributeName: str, strValue: str) -> None:
        """
         Sets a default attribute value 
        """
        pass
    
    ##  Sets a default attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="builder"> (@link FeatureGeometry NXOpen.CAM.FBM.FeatureGeometry@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="nValue"> (int)  the attribute value </param>
    @overload
    def SetDefaultAttribute(self, attributeName: str, nValue: int) -> None:
        """
         Sets a default attribute value 
        """
        pass
    
    ##  Sets a default attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="builder"> (@link FeatureGeometry NXOpen.CAM.FBM.FeatureGeometry@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="bValue"> (bool)  the attribute value </param>
    @overload
    def SetDefaultAttribute(self, attributeName: str, bValue: bool) -> None:
        """
         Sets a default attribute value 
        """
        pass
    
    ##  Change machining area 
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## 
    ## <param name="machiningArea"> (str)  the machining area </param>
    def SetMachiningArea(self, machiningArea: str) -> None:
        """
         Change machining area 
        """
        pass
    
import NXOpen
import NXOpen.CAM
##  Interface for feature set  <br> To create a new instance of this class, use @link NXOpen::CAM::FBM::FeatureGeometry::CreateFeatureSet  NXOpen::CAM::FBM::FeatureGeometry::CreateFeatureSet @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class FeatureSet(NXOpen.CAM.GeometrySet): 
    """ Interface for feature set """


    ##  Creates the feature using the specified tags
    ##  @return tagFeature (@link Feature NXOpen.CAM.FBM.Feature@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## 
    ## <param name="entities"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  the input entities </param>
    def CreateFeature(self, entities: List[NXOpen.NXObject]) -> Feature:
        """
         Creates the feature using the specified tags
         @return tagFeature (@link Feature NXOpen.CAM.FBM.Feature@endlink): .
        """
        pass
    
    ##  Returns the feature 
    ##  @return tagFeature (@link Feature NXOpen.CAM.FBM.Feature@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetFeature(self) -> Feature:
        """
         Returns the feature 
         @return tagFeature (@link Feature NXOpen.CAM.FBM.Feature@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.CAM
##  Interface for CAM Feature objects  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class Feature(NXOpen.NXObject): 
    """ Interface for CAM Feature objects """


    ##  Flip feature direction
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    def FlipDirection(self) -> None:
        """
         Flip feature direction
        """
        pass
    
    ##  Gets and attribute 
    ##  @return tagAttribute (@link NXOpen.CAM.CAMAttribute NXOpen.CAM.CAMAttribute@endlink):  the attribute .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attributeName"> (str)  the attribute name </param>
    def GetAttribute(self, attributeName: str) -> NXOpen.CAM.CAMAttribute:
        """
         Gets and attribute 
         @return tagAttribute (@link NXOpen.CAM.CAMAttribute NXOpen.CAM.CAMAttribute@endlink):  the attribute .
        """
        pass
    
    ##  Returns the actual attribute value 
    ##  @return dValue (float):  the attribute value .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attributeName"> (str)  the attribute name </param>
    def GetAttributeDoubleValue(self, attributeName: str) -> float:
        """
         Returns the actual attribute value 
         @return dValue (float):  the attribute value .
        """
        pass
    
    ##  Returns the machining area the input entity is part of. If the input entity is not part of the feature 
    ##                 the return string is empty
    ##  @return machiningArea (str): .
    ## 
    ##   <br>  Created in NX9.0.3  <br> 

    ## License requirements: None.
    ## 
    ## <param name="tagEntit"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  input geometry </param>
    def GetMachiningArea(self, tagEntit: NXOpen.DisplayableObject) -> str:
        """
         Returns the machining area the input entity is part of. If the input entity is not part of the feature 
                        the return string is empty
         @return machiningArea (str): .
        """
        pass
    
    ##  Returns true if attribute is overridden 
    ##  @return bOverridden (bool):  the override flag  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attributeName"> (str)  the attribute name </param>
    def IsAttributeOverridden(self, attributeName: str) -> bool:
        """
         Returns true if attribute is overridden 
         @return bOverridden (bool):  the override flag  .
        """
        pass
    
    ##  Overrides the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="pFeature"> (@link Feature NXOpen.CAM.FBM.Feature@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="dValue"> (float)  the attribute value </param>
    @overload
    def OverrideAttributeValue(self, attributeName: str, dValue: float) -> None:
        """
         Overrides the attribute value 
        """
        pass
    
    ##  Overrides the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="pFeature"> (@link Feature NXOpen.CAM.FBM.Feature@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="nValue"> (int)  the attribute value </param>
    @overload
    def OverrideAttributeValue(self, attributeName: str, nValue: int) -> None:
        """
         Overrides the attribute value 
        """
        pass
    
    ##  Overrides the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="pFeature"> (@link Feature NXOpen.CAM.FBM.Feature@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="bValue"> (bool)  the attribute value </param>
    @overload
    def OverrideAttributeValue(self, attributeName: str, bValue: bool) -> None:
        """
         Overrides the attribute value 
        """
        pass
    
    ##  Overrides the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="pFeature"> (@link Feature NXOpen.CAM.FBM.Feature@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="strValue"> (str)  the attribute value </param>
    @overload
    def OverrideAttributeValue(self, attributeName: str, strValue: str) -> None:
        """
         Overrides the attribute value 
        """
        pass
    
    ##  Overrides the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="pFeature"> (@link Feature NXOpen.CAM.FBM.Feature@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="ptValue"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  the attribute value </param>
    @overload
    def OverrideAttributeValue(self, attributeName: str, ptValue: NXOpen.Point3d) -> None:
        """
         Overrides the attribute value 
        """
        pass
    
    ##  Overrides the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="pFeature"> (@link Feature NXOpen.CAM.FBM.Feature@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="vecValue"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink)  the attribute value </param>
    @overload
    def OverrideAttributeValue(self, attributeName: str, vecValue: NXOpen.Vector3d) -> None:
        """
         Overrides the attribute value 
        """
        pass
    
    ##  Resets an attribute to its original value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## 
    ## <param name="attributeName"> (str)  the attribute name </param>
    def ResetAttributeValue(self, attributeName: str) -> None:
        """
         Resets an attribute to its original value 
        """
        pass
    
    ##  Resets all attributes to their original value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    def ResetAttributes(self) -> None:
        """
         Resets all attributes to their original value 
        """
        pass
    
    ##  Sets the attribute value(s) to the same value(s) as another attribute 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## 
    ## <param name="tagAttribute"> (@link NXOpen.CAM.CAMAttribute NXOpen.CAM.CAMAttribute@endlink)  the attribute </param>
    def SetAttribute(self, tagAttribute: NXOpen.CAM.CAMAttribute) -> None:
        """
         Sets the attribute value(s) to the same value(s) as another attribute 
        """
        pass
    
    ##  Sets the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="pFeature"> (@link Feature NXOpen.CAM.FBM.Feature@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="dValue"> (float)  the attribute value </param>
    @overload
    def SetAttributeValue(self, attributeName: str, dValue: float) -> None:
        """
         Sets the attribute value 
        """
        pass
    
    ##  Sets the attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="pFeature"> (@link Feature NXOpen.CAM.FBM.Feature@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="strValue"> (str)  the attribute value </param>
    @overload
    def SetAttributeValue(self, attributeName: str, strValue: str) -> None:
        """
         Sets the attribute value 
        """
        pass
    
    ##  Sets the attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="pFeature"> (@link Feature NXOpen.CAM.FBM.Feature@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="nValue"> (int)  the attribute value </param>
    @overload
    def SetAttributeValue(self, attributeName: str, nValue: int) -> None:
        """
         Sets the attribute value 
        """
        pass
    
    ##  Sets the attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## <param name="pFeature"> (@link Feature NXOpen.CAM.FBM.Feature@endlink) </param>
    ## <param name="attributeName"> (str)  the attribute name </param>
    ## <param name="bValue"> (bool)  the attribute value </param>
    @overload
    def SetAttributeValue(self, attributeName: str, bValue: bool) -> None:
        """
         Sets the attribute value 
        """
        pass
    
    ##  Change the feature coordinate system
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## 
    ## <param name="ptValue"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  the new feature origin </param>
    ## <param name="xAxis"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink)  the new feature x axis </param>
    ## <param name="yAxis"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink)  the new feature y axis </param>
    def SetCoordinateSystem(self, ptValue: NXOpen.Point3d, xAxis: NXOpen.Vector3d, yAxis: NXOpen.Vector3d) -> None:
        """
         Change the feature coordinate system
        """
        pass
    
    ##  Unlock Feature
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: cam_base ("CAM BASE")
    def Unlock(self) -> None:
        """
         Unlock Feature
        """
        pass
    
##  Represents a feature geometry builder  <br> An instance of this class can be obtained from @link CAM::HoleBossGeom::GetCenterHoleGeometry CAM::HoleBossGeom::GetCenterHoleGeometry@endlink  or @link CAM::HoleBossGeom::GetChamferHoleGeometry CAM::HoleBossGeom::GetChamferHoleGeometry@endlink   <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class MachiningFeatureGeometry(FeatureGeometry): 
    """ Represents a feature geometry builder """
    pass


##  Represents a feature geometry builder  <br> This is an abstract class and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX9.0.1  <br> 

class ThreadFeatureGeometry(FeatureGeometry): 
    """ Represents a feature geometry builder """


    ##  Thread form standards 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unified</term><description> 
    ##  Form: Unified </description> </item><item><term> 
    ## Acme</term><description> 
    ##  Form: Acme </description> </item><item><term> 
    ## StubAcme</term><description> 
    ##  Form: Stub Acme </description> </item><item><term> 
    ## Buttress</term><description> 
    ##  Form: Buttress </description> </item><item><term> 
    ## Metric</term><description> 
    ##  Form: Metric </description> </item><item><term> 
    ## Trapezoidal</term><description> 
    ##  Form: Trapezoidal </description> </item><item><term> 
    ## Lowernherz</term><description> 
    ##  Form: Lowenherz </description> </item><item><term> 
    ## SparkPlug</term><description> 
    ##  Form: Spark Plug </description> </item><item><term> 
    ## Npt</term><description> 
    ##  Form: NPT </description> </item><item><term> 
    ## HoseCoupling</term><description> 
    ##  Form: Hose Coupling </description> </item><item><term> 
    ## FireHose</term><description> 
    ##  Form: Fire Hose </description> </item><item><term> 
    ## Unj</term><description> 
    ##  Form: UNJ </description> </item><item><term> 
    ## Nps</term><description> 
    ##  Form: NPS </description> </item><item><term> 
    ## Bsp</term><description> 
    ##  Form: BSP </description> </item><item><term> 
    ## Bstp</term><description> 
    ##  Form: BSTP </description> </item><item><term> 
    ## Helicoil</term><description> 
    ##  Form: Helicoil </description> </item><item><term> 
    ## Ns</term><description> 
    ##  Form: NS </description> </item><item><term> 
    ## UserDefined</term><description> 
    ##  Form: User defined </description> </item></list>
    class Form(Enum):
        """
        Members Include: <Unified> <Acme> <StubAcme> <Buttress> <Metric> <Trapezoidal> <Lowernherz> <SparkPlug> <Npt> <HoseCoupling> <FireHose> <Unj> <Nps> <Bsp> <Bstp> <Helicoil> <Ns> <UserDefined>
        """
        Unified: int
        Acme: int
        StubAcme: int
        Buttress: int
        Metric: int
        Trapezoidal: int
        Lowernherz: int
        SparkPlug: int
        Npt: int
        HoseCoupling: int
        FireHose: int
        Unj: int
        Nps: int
        Bsp: int
        Bstp: int
        Helicoil: int
        Ns: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ThreadFeatureGeometry.Form:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the rotation types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## RightHand</term><description> 
    ##  Rotation: Right-hand </description> </item><item><term> 
    ## LeftHand</term><description> 
    ##  Rotation: Left-hand </description> </item></list>
    class Rotation(Enum):
        """
        Members Include: <RightHand> <LeftHand>
        """
        RightHand: int
        LeftHand: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ThreadFeatureGeometry.Rotation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  thread data source types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FromModel</term><description> 
    ##  From Model </description> </item><item><term> 
    ## FromTable</term><description> 
    ##  From Table </description> </item></list>
    class ThreadDataSource(Enum):
        """
        Members Include: <FromModel> <FromTable>
        """
        FromModel: int
        FromTable: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ThreadFeatureGeometry.ThreadDataSource:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ThreadFeatureGeometry.Form NXOpen.CAM.FBM.ThreadFeatureGeometry.Form@endlink) FormStandard
    ##  Returns the form standard   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## @return ThreadFeatureGeometry.Form
    @property
    def FormStandard(self) -> ThreadFeatureGeometry.Form:
        """
        Getter for property: (@link ThreadFeatureGeometry.Form NXOpen.CAM.FBM.ThreadFeatureGeometry.Form@endlink) FormStandard
         Returns the form standard   
            
         
        """
        pass
    
    ## Setter for property: (@link ThreadFeatureGeometry.Form NXOpen.CAM.FBM.ThreadFeatureGeometry.Form@endlink) FormStandard

    ##  Returns the form standard   
    ##     
    ##  
    ## Setter License requirements: cam_base ("CAM BASE")
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    @FormStandard.setter
    def FormStandard(self, standard: ThreadFeatureGeometry.Form):
        """
        Setter for property: (@link ThreadFeatureGeometry.Form NXOpen.CAM.FBM.ThreadFeatureGeometry.Form@endlink) FormStandard
         Returns the form standard   
            
         
        """
        pass
    
    ## Getter for property: (@link ThreadFeatureGeometry.Rotation NXOpen.CAM.FBM.ThreadFeatureGeometry.Rotation@endlink) ThreadRotation
    ##  Returns the thread rotation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## @return ThreadFeatureGeometry.Rotation
    @property
    def ThreadRotation(self) -> ThreadFeatureGeometry.Rotation:
        """
        Getter for property: (@link ThreadFeatureGeometry.Rotation NXOpen.CAM.FBM.ThreadFeatureGeometry.Rotation@endlink) ThreadRotation
         Returns the thread rotation   
            
         
        """
        pass
    
    ## Setter for property: (@link ThreadFeatureGeometry.Rotation NXOpen.CAM.FBM.ThreadFeatureGeometry.Rotation@endlink) ThreadRotation

    ##  Returns the thread rotation   
    ##     
    ##  
    ## Setter License requirements: cam_base ("CAM BASE")
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    @ThreadRotation.setter
    def ThreadRotation(self, rotation: ThreadFeatureGeometry.Rotation):
        """
        Setter for property: (@link ThreadFeatureGeometry.Rotation NXOpen.CAM.FBM.ThreadFeatureGeometry.Rotation@endlink) ThreadRotation
         Returns the thread rotation   
            
         
        """
        pass
    
    ##  Get the user defined form standard 
    ##  @return userDefinedForm (str): .
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## License requirements: None.
    def GetFormUserDefined(self) -> str:
        """
         Get the user defined form standard 
         @return userDefinedForm (str): .
        """
        pass
    
    ##  Gets the source type for retrieving thread data 
    ##  @return source (@link ThreadFeatureGeometry.ThreadDataSource NXOpen.CAM.FBM.ThreadFeatureGeometry.ThreadDataSource@endlink):  thread data source type .
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: None.
    def GetThreadDataSource(self) -> ThreadFeatureGeometry.ThreadDataSource:
        """
         Gets the source type for retrieving thread data 
         @return source (@link ThreadFeatureGeometry.ThreadDataSource NXOpen.CAM.FBM.ThreadFeatureGeometry.ThreadDataSource@endlink):  thread data source type .
        """
        pass
    
    ##  Set the user defined form standard 
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## 
    ## <param name="userDefinedForm"> (str) </param>
    def SetFormUserDefined(self, userDefinedForm: str) -> None:
        """
         Set the user defined form standard 
        """
        pass
    
    ##  Sets the source type for retrieving thread data 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## 
    ## <param name="source"> (@link ThreadFeatureGeometry.ThreadDataSource NXOpen.CAM.FBM.ThreadFeatureGeometry.ThreadDataSource@endlink)  thread data source type </param>
    def SetThreadDataSource(self, source: ThreadFeatureGeometry.ThreadDataSource) -> None:
        """
         Sets the source type for retrieving thread data 
        """
        pass
    
    ##  Update the feature thread parameters 
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ## 
    ## <param name="tagFeature"> (@link Feature NXOpen.CAM.FBM.Feature@endlink) </param>
    def UpdateThreadParameters(self, tagFeature: Feature) -> None:
        """
         Update the feature thread parameters 
        """
        pass
    
## @package NXOpen.CAM.FBM
## Classes, Enums and Structs under NXOpen.CAM.FBM namespace

##  @link FeatureGeometrySequenceDirectionType NXOpen.CAM.FBM.FeatureGeometrySequenceDirectionType @endlink is an alias for @link FeatureGeometry.SequenceDirectionType NXOpen.CAM.FBM.FeatureGeometry.SequenceDirectionType@endlink
FeatureGeometrySequenceDirectionType = FeatureGeometry.SequenceDirectionType


##  @link FeatureGeometrySequencePatternType NXOpen.CAM.FBM.FeatureGeometrySequencePatternType @endlink is an alias for @link FeatureGeometry.SequencePatternType NXOpen.CAM.FBM.FeatureGeometry.SequencePatternType@endlink
FeatureGeometrySequencePatternType = FeatureGeometry.SequencePatternType


##  @link FeatureGeometrySortOrder NXOpen.CAM.FBM.FeatureGeometrySortOrder @endlink is an alias for @link FeatureGeometry.SortOrder NXOpen.CAM.FBM.FeatureGeometry.SortOrder@endlink
FeatureGeometrySortOrder = FeatureGeometry.SortOrder


##  @link ThreadFeatureGeometryForm NXOpen.CAM.FBM.ThreadFeatureGeometryForm @endlink is an alias for @link ThreadFeatureGeometry.Form NXOpen.CAM.FBM.ThreadFeatureGeometry.Form@endlink
ThreadFeatureGeometryForm = ThreadFeatureGeometry.Form


##  @link ThreadFeatureGeometryRotation NXOpen.CAM.FBM.ThreadFeatureGeometryRotation @endlink is an alias for @link ThreadFeatureGeometry.Rotation NXOpen.CAM.FBM.ThreadFeatureGeometry.Rotation@endlink
ThreadFeatureGeometryRotation = ThreadFeatureGeometry.Rotation


##  @link ThreadFeatureGeometryThreadDataSource NXOpen.CAM.FBM.ThreadFeatureGeometryThreadDataSource @endlink is an alias for @link ThreadFeatureGeometry.ThreadDataSource NXOpen.CAM.FBM.ThreadFeatureGeometry.ThreadDataSource@endlink
ThreadFeatureGeometryThreadDataSource = ThreadFeatureGeometry.ThreadDataSource


