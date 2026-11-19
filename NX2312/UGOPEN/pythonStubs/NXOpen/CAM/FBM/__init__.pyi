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
    ##  Direction: XM 
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
    ##  Pattern: Zig 
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
    ##  Sort order: Closet 
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
    ##   the use model depth flag   
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
          the use model depth flag   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseModelDepth

    ##   the use model depth flag   
    ##     
    ##  
    ## Setter License requirements: cam_base ("CAM BASE")
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    @UseModelDepth.setter
    def UseModelDepth(self, flag: bool):
        """
        Setter for property: (bool) UseModelDepth
          the use model depth flag   
            
         
        """
        pass
    
    ##  Creates a feature geometry set 
    ##  @return ppFeatureBuilder (@link FeatureSet NXOpen.CAM.FBM.FeatureSet@endlink):  the new in process feature set .
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the machining feature 
    def AddFeatureSet(builder: FeatureGeometry, tagMachiningFeature: NXOpen.CAM.CAMFeature, featureType: str) -> FeatureSet:
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
    def CreateFeatureSet(builder: FeatureGeometry) -> FeatureSet:
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
    ##  the geometry objects, can also be machining features 
    def CreateFeatures(builder: FeatureGeometry, objects: List[NXOpen.NXObject], featureType: str) -> List[Feature]:
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
    ##  the index of the feature set editor 
    def GetFeatureSet(builder: FeatureGeometry, nIndex: int) -> FeatureSet:
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
    @staticmethod
    def GetMachiningArea(builder: FeatureGeometry) -> str:
        """
         Returns the machining area 
         @return machiningArea (str):  the machining area .
        """
        pass
    
    ##  Reload list from parent 
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## License requirements: cam_base ("CAM BASE")
    @staticmethod
    def ReloadList(builder: FeatureGeometry) -> None:
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
    def ReorderFeatures(builder: FeatureGeometry, sortType: FeatureGeometry.SortOrder) -> None:
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
    def ReorderFeaturesByDirection(self, builder: FeatureGeometry, direction: FeatureGeometry.SequenceDirectionType, pattern: FeatureGeometry.SequencePatternType, vecValue: NXOpen.Vector3d) -> None:
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
    def ReorderFeaturesByDirection(self, builder: FeatureGeometry, direction: FeatureGeometry.SequenceDirectionType, pattern: FeatureGeometry.SequencePatternType, vecValue: NXOpen.Vector3d, bandWidth: float) -> None:
        """
         Reorders the features according to primary direction with band width 
        """
        pass
    
    ##  Reverse the features 
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## License requirements: cam_base ("CAM BASE")
    @staticmethod
    def ReverseFeatures(builder: FeatureGeometry) -> None:
        """
         Reverse the features 
        """
        pass
    
    ##  Sets a default attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def SetDefaultAttribute(self, builder: FeatureGeometry, attributeName: str, dValue: float) -> None:
        """
         Sets a default attribute value 
        """
        pass
    
    ##  Sets a default attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def SetDefaultAttribute(self, builder: FeatureGeometry, attributeName: str, strValue: str) -> None:
        """
         Sets a default attribute value 
        """
        pass
    
    ##  Sets a default attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def SetDefaultAttribute(self, builder: FeatureGeometry, attributeName: str, nValue: int) -> None:
        """
         Sets a default attribute value 
        """
        pass
    
    ##  Sets a default attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def SetDefaultAttribute(self, builder: FeatureGeometry, attributeName: str, bValue: bool) -> None:
        """
         Sets a default attribute value 
        """
        pass
    
    ##  Change machining area 
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the machining area 
    def SetMachiningArea(builder: FeatureGeometry, machiningArea: str) -> None:
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
    ##  the input entities 
    def CreateFeature(pFeatureBuilder: FeatureSet, entities: List[NXOpen.NXObject]) -> Feature:
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
    @staticmethod
    def GetFeature(pFeatureBuilder: FeatureSet) -> Feature:
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
    ##  the attribute name 
    def GetAttribute(pFeature: Feature, attributeName: str) -> NXOpen.CAM.CAMAttribute:
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
    ##  the attribute name 
    def GetAttributeDoubleValue(pFeature: Feature, attributeName: str) -> float:
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
    ##  input geometry 
    def GetMachiningArea(pSelf: Feature, tagEntit: NXOpen.DisplayableObject) -> str:
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
    ##  the attribute name 
    def IsAttributeOverridden(pFeature: Feature, attributeName: str) -> bool:
        """
         Returns true if attribute is overridden 
         @return bOverridden (bool):  the override flag  .
        """
        pass
    
    ##  Overrides the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def OverrideAttributeValue(self, pFeature: Feature, attributeName: str, dValue: float) -> None:
        """
         Overrides the attribute value 
        """
        pass
    
    ##  Overrides the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def OverrideAttributeValue(self, pFeature: Feature, attributeName: str, nValue: int) -> None:
        """
         Overrides the attribute value 
        """
        pass
    
    ##  Overrides the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def OverrideAttributeValue(self, pFeature: Feature, attributeName: str, bValue: bool) -> None:
        """
         Overrides the attribute value 
        """
        pass
    
    ##  Overrides the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def OverrideAttributeValue(self, pFeature: Feature, attributeName: str, strValue: str) -> None:
        """
         Overrides the attribute value 
        """
        pass
    
    ##  Overrides the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def OverrideAttributeValue(self, pFeature: Feature, attributeName: str, ptValue: NXOpen.Point3d) -> None:
        """
         Overrides the attribute value 
        """
        pass
    
    ##  Overrides the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def OverrideAttributeValue(self, pFeature: Feature, attributeName: str, vecValue: NXOpen.Vector3d) -> None:
        """
         Overrides the attribute value 
        """
        pass
    
    ##  Resets an attribute to its original value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    def ResetAttributeValue(pFeature: Feature, attributeName: str) -> None:
        """
         Resets an attribute to its original value 
        """
        pass
    
    ##  Resets all attributes to their original value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    @staticmethod
    def ResetAttributes(pFeature: Feature) -> None:
        """
         Resets all attributes to their original value 
        """
        pass
    
    ##  Sets the attribute value(s) to the same value(s) as another attribute 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute 
    def SetAttribute(pFeature: Feature, tagAttribute: NXOpen.CAM.CAMAttribute) -> None:
        """
         Sets the attribute value(s) to the same value(s) as another attribute 
        """
        pass
    
    ##  Sets the attribute value 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def SetAttributeValue(self, pFeature: Feature, attributeName: str, dValue: float) -> None:
        """
         Sets the attribute value 
        """
        pass
    
    ##  Sets the attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def SetAttributeValue(self, pFeature: Feature, attributeName: str, strValue: str) -> None:
        """
         Sets the attribute value 
        """
        pass
    
    ##  Sets the attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def SetAttributeValue(self, pFeature: Feature, attributeName: str, nValue: int) -> None:
        """
         Sets the attribute value 
        """
        pass
    
    ##  Sets the attribute value 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the attribute name 
    @overload
    def SetAttributeValue(self, pFeature: Feature, attributeName: str, bValue: bool) -> None:
        """
         Sets the attribute value 
        """
        pass
    
    ##  Change the feature coordinate system
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  the new feature origin 
    def SetCoordinateSystem(self, ptValue: NXOpen.Point3d, xAxis: NXOpen.Vector3d, yAxis: NXOpen.Vector3d) -> None:
        """
         Change the feature coordinate system
        """
        pass
    
    ##  Unlock Feature
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: cam_base ("CAM BASE")
    @staticmethod
    def Unlock(pFeature: Feature) -> None:
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
    ##  Form: Unified 
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
    ##  Rotation: Right-hand 
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
    ##  From Model 
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
    ##   the form standard   
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
          the form standard   
            
         
        """
        pass
    
    ## Setter for property: (@link ThreadFeatureGeometry.Form NXOpen.CAM.FBM.ThreadFeatureGeometry.Form@endlink) FormStandard

    ##   the form standard   
    ##     
    ##  
    ## Setter License requirements: cam_base ("CAM BASE")
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    @FormStandard.setter
    def FormStandard(self, standard: ThreadFeatureGeometry.Form):
        """
        Setter for property: (@link ThreadFeatureGeometry.Form NXOpen.CAM.FBM.ThreadFeatureGeometry.Form@endlink) FormStandard
          the form standard   
            
         
        """
        pass
    
    ## Getter for property: (@link ThreadFeatureGeometry.Rotation NXOpen.CAM.FBM.ThreadFeatureGeometry.Rotation@endlink) ThreadRotation
    ##   the thread rotation   
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
          the thread rotation   
            
         
        """
        pass
    
    ## Setter for property: (@link ThreadFeatureGeometry.Rotation NXOpen.CAM.FBM.ThreadFeatureGeometry.Rotation@endlink) ThreadRotation

    ##   the thread rotation   
    ##     
    ##  
    ## Setter License requirements: cam_base ("CAM BASE")
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    @ThreadRotation.setter
    def ThreadRotation(self, rotation: ThreadFeatureGeometry.Rotation):
        """
        Setter for property: (@link ThreadFeatureGeometry.Rotation NXOpen.CAM.FBM.ThreadFeatureGeometry.Rotation@endlink) ThreadRotation
          the thread rotation   
            
         
        """
        pass
    
    ##  Get the user defined form standard 
    ##  @return userDefinedForm (str): .
    ## 
    ##   <br>  Created in NX9.0.2  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFormUserDefined(builder: ThreadFeatureGeometry) -> str:
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
    @staticmethod
    def GetThreadDataSource(builder: ThreadFeatureGeometry) -> ThreadFeatureGeometry.ThreadDataSource:
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
    def SetFormUserDefined(builder: ThreadFeatureGeometry, userDefinedForm: str) -> None:
        """
         Set the user defined form standard 
        """
        pass
    
    ##  Sets the source type for retrieving thread data 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: cam_base ("CAM BASE")
    ##  thread data source type 
    def SetThreadDataSource(builder: ThreadFeatureGeometry, source: ThreadFeatureGeometry.ThreadDataSource) -> None:
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
    def UpdateThreadParameters(builder: ThreadFeatureGeometry, tagFeature: Feature) -> None:
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


