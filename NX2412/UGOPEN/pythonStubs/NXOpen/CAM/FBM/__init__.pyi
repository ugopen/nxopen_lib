from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.CAM
class FeatureGeometry(NXOpen.CAM.Geometry): 
    """ Represents a feature geometry builder """
    class SequenceDirectionType(Enum):
        """
        Members Include: 
         |Xm|  Direction: XM 
         |Ym|  Direction: YM 
         |Zm|  Direction: ZM 
         |Vector|  Direction: Vector 

        """
        Xm: int
        Ym: int
        Zm: int
        Vector: int
        @staticmethod
        def ValueOf(value: int) -> FeatureGeometry.SequenceDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SequencePatternType(Enum):
        """
        Members Include: 
         |Zig|  Pattern: Zig 
         |ZigZag|  Pattern: Zig Zag 

        """
        Zig: int
        ZigZag: int
        @staticmethod
        def ValueOf(value: int) -> FeatureGeometry.SequencePatternType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SortOrder(Enum):
        """
        Members Include: 
         |Closest|  Sort order: Closet 
         |ShortestPath|  Sort order: Shortest Path 
         |PrimaryDirection|  Sort order: Primary Direction 

        """
        Closest: int
        ShortestPath: int
        PrimaryDirection: int
        @staticmethod
        def ValueOf(value: int) -> FeatureGeometry.SortOrder:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def UseModelDepth(self) -> bool:
        """
        Getter for property: (bool) UseModelDepth
         Returns the use model depth flag   
            
         
        """
        pass
    @UseModelDepth.setter
    def UseModelDepth(self, flag: bool):
        """
        Setter for property: (bool) UseModelDepth
         Returns the use model depth flag   
            
         
        """
        pass
    def AddFeatureSet(self, tagMachiningFeature: NXOpen.CAM.CAMFeature, featureType: str) -> FeatureSet:
        """
         Creates a feature geometry set 
         Returns ppFeatureBuilder ( FeatureSet NXOpen):  the new in process feature set .
        """
        pass
    def CreateFeatureSet(self) -> FeatureSet:
        """
         Create a new empty feature editor
         Returns ppFeatureBuilder ( FeatureSet NXOpen):  the new in process feature set .
        """
        pass
    def CreateFeatures(self, objects: List[NXOpen.NXObject], featureType: str) -> List[Feature]:
        """
         Create a series of (in process) features. Depending on the input objects feature recognition is performed. When
                        no known features can be recognized, tagged features are created of type featureType 
         Returns features ( Feature List[NXOp): .
        """
        pass
    def GetFeatureSet(self, nIndex: int) -> FeatureSet:
        """
         Get the in process feature editor at the specified index 
         Returns ppFeatureBuilder ( FeatureSet NXOpen):  the in process feature set .
        """
        pass
    def GetMachiningArea(self) -> str:
        """
         Returns the machining area 
         Returns machiningArea (str):  the machining area .
        """
        pass
    def ReloadList(self) -> None:
        """
         Reload list from parent 
        """
        pass
    def ReorderFeatures(self, sortType: FeatureGeometry.SortOrder) -> None:
        """
         Reorders the features according to a predefined algorithm 
        """
        pass
    @overload
    def ReorderFeaturesByDirection(self, direction: FeatureGeometry.SequenceDirectionType, pattern: FeatureGeometry.SequencePatternType, vecValue: NXOpen.Vector3d) -> None:
        """
         Reorders the features according to primary direction 
        """
        pass
    @overload
    def ReorderFeaturesByDirection(self, direction: FeatureGeometry.SequenceDirectionType, pattern: FeatureGeometry.SequencePatternType, vecValue: NXOpen.Vector3d, bandWidth: float) -> None:
        """
         Reorders the features according to primary direction with band width 
        """
        pass
    def ReverseFeatures(self) -> None:
        """
         Reverse the features 
        """
        pass
    @overload
    def SetDefaultAttribute(self, attributeName: str, dValue: float) -> None:
        """
         Sets a default attribute value 
        """
        pass
    @overload
    def SetDefaultAttribute(self, attributeName: str, strValue: str) -> None:
        """
         Sets a default attribute value 
        """
        pass
    @overload
    def SetDefaultAttribute(self, attributeName: str, nValue: int) -> None:
        """
         Sets a default attribute value 
        """
        pass
    @overload
    def SetDefaultAttribute(self, attributeName: str, bValue: bool) -> None:
        """
         Sets a default attribute value 
        """
        pass
    def SetMachiningArea(self, machiningArea: str) -> None:
        """
         Change machining area 
        """
        pass
import NXOpen
import NXOpen.CAM
class FeatureSet(NXOpen.CAM.GeometrySet): 
    """ Interface for feature set """
    def CreateFeature(self, entities: List[NXOpen.NXObject]) -> Feature:
        """
         Creates the feature using the specified tags
         Returns tagFeature ( Feature NXOpen): .
        """
        pass
    def GetFeature(self) -> Feature:
        """
         Returns the feature 
         Returns tagFeature ( Feature NXOpen): .
        """
        pass
import NXOpen
import NXOpen.CAM
class Feature(NXOpen.NXObject): 
    """ Interface for CAM Feature objects """
    def FlipDirection(self) -> None:
        """
         Flip feature direction
        """
        pass
    def GetAttribute(self, attributeName: str) -> NXOpen.CAM.CAMAttribute:
        """
         Gets and attribute 
         Returns tagAttribute ( NXOpen.CAM.CAMAttribute):  the attribute .
        """
        pass
    def GetAttributeDoubleValue(self, attributeName: str) -> float:
        """
         Returns the actual attribute value 
         Returns dValue (float):  the attribute value .
        """
        pass
    def GetMachiningArea(self, tagEntit: NXOpen.DisplayableObject) -> str:
        """
         Returns the machining area the input entity is part of. If the input entity is not part of the feature 
                        the return string is empty
         Returns machiningArea (str): .
        """
        pass
    def IsAttributeOverridden(self, attributeName: str) -> bool:
        """
         Returns true if attribute is overridden 
         Returns bOverridden (bool):  the override flag  .
        """
        pass
    @overload
    def OverrideAttributeValue(self, attributeName: str, dValue: float) -> None:
        """
         Overrides the attribute value 
        """
        pass
    @overload
    def OverrideAttributeValue(self, attributeName: str, nValue: int) -> None:
        """
         Overrides the attribute value 
        """
        pass
    @overload
    def OverrideAttributeValue(self, attributeName: str, bValue: bool) -> None:
        """
         Overrides the attribute value 
        """
        pass
    @overload
    def OverrideAttributeValue(self, attributeName: str, strValue: str) -> None:
        """
         Overrides the attribute value 
        """
        pass
    @overload
    def OverrideAttributeValue(self, attributeName: str, ptValue: NXOpen.Point3d) -> None:
        """
         Overrides the attribute value 
        """
        pass
    @overload
    def OverrideAttributeValue(self, attributeName: str, vecValue: NXOpen.Vector3d) -> None:
        """
         Overrides the attribute value 
        """
        pass
    def ResetAttributeValue(self, attributeName: str) -> None:
        """
         Resets an attribute to its original value 
        """
        pass
    def ResetAttributes(self) -> None:
        """
         Resets all attributes to their original value 
        """
        pass
    def SetAttribute(self, tagAttribute: NXOpen.CAM.CAMAttribute) -> None:
        """
         Sets the attribute value(s) to the same value(s) as another attribute 
        """
        pass
    @overload
    def SetAttributeValue(self, attributeName: str, dValue: float) -> None:
        """
         Sets the attribute value 
        """
        pass
    @overload
    def SetAttributeValue(self, attributeName: str, strValue: str) -> None:
        """
         Sets the attribute value 
        """
        pass
    @overload
    def SetAttributeValue(self, attributeName: str, nValue: int) -> None:
        """
         Sets the attribute value 
        """
        pass
    @overload
    def SetAttributeValue(self, attributeName: str, bValue: bool) -> None:
        """
         Sets the attribute value 
        """
        pass
    def SetCoordinateSystem(self, ptValue: NXOpen.Point3d, xAxis: NXOpen.Vector3d, yAxis: NXOpen.Vector3d) -> None:
        """
         Change the feature coordinate system
        """
        pass
    def Unlock(self) -> None:
        """
         Unlock Feature
        """
        pass
class MachiningFeatureGeometry(FeatureGeometry): 
    """ Represents a feature geometry builder """
    pass
class ThreadFeatureGeometry(FeatureGeometry): 
    """ Represents a feature geometry builder """
    class Form(Enum):
        """
        Members Include: 
         |Unified|  Form: Unified 
         |Acme|  Form: Acme 
         |StubAcme|  Form: Stub Acme 
         |Buttress|  Form: Buttress 
         |Metric|  Form: Metric 
         |Trapezoidal|  Form: Trapezoidal 
         |Lowernherz|  Form: Lowenherz 
         |SparkPlug|  Form: Spark Plug 
         |Npt|  Form: NPT 
         |HoseCoupling|  Form: Hose Coupling 
         |FireHose|  Form: Fire Hose 
         |Unj|  Form: UNJ 
         |Nps|  Form: NPS 
         |Bsp|  Form: BSP 
         |Bstp|  Form: BSTP 
         |Helicoil|  Form: Helicoil 
         |Ns|  Form: NS 
         |UserDefined|  Form: User defined 

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
        @staticmethod
        def ValueOf(value: int) -> ThreadFeatureGeometry.Form:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Rotation(Enum):
        """
        Members Include: 
         |RightHand|  Rotation: Right-hand 
         |LeftHand|  Rotation: Left-hand 

        """
        RightHand: int
        LeftHand: int
        @staticmethod
        def ValueOf(value: int) -> ThreadFeatureGeometry.Rotation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThreadDataSource(Enum):
        """
        Members Include: 
         |FromModel|  From Model 
         |FromTable|  From Table 

        """
        FromModel: int
        FromTable: int
        @staticmethod
        def ValueOf(value: int) -> ThreadFeatureGeometry.ThreadDataSource:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FormStandard(self) -> ThreadFeatureGeometry.Form:
        """
        Getter for property: ( ThreadFeatureGeometry.Form NXOpen) FormStandard
         Returns the form standard   
            
         
        """
        pass
    @FormStandard.setter
    def FormStandard(self, standard: ThreadFeatureGeometry.Form):
        """
        Setter for property: ( ThreadFeatureGeometry.Form NXOpen) FormStandard
         Returns the form standard   
            
         
        """
        pass
    @property
    def ThreadRotation(self) -> ThreadFeatureGeometry.Rotation:
        """
        Getter for property: ( ThreadFeatureGeometry.Rotation NXOpen) ThreadRotation
         Returns the thread rotation   
            
         
        """
        pass
    @ThreadRotation.setter
    def ThreadRotation(self, rotation: ThreadFeatureGeometry.Rotation):
        """
        Setter for property: ( ThreadFeatureGeometry.Rotation NXOpen) ThreadRotation
         Returns the thread rotation   
            
         
        """
        pass
    def GetFormUserDefined(self) -> str:
        """
         Get the user defined form standard 
         Returns userDefinedForm (str): .
        """
        pass
    def GetThreadDataSource(self) -> ThreadFeatureGeometry.ThreadDataSource:
        """
         Gets the source type for retrieving thread data 
         Returns source ( ThreadFeatureGeometry.ThreadDataSource NXOpen):  thread data source type .
        """
        pass
    def SetFormUserDefined(self, userDefinedForm: str) -> None:
        """
         Set the user defined form standard 
        """
        pass
    def SetThreadDataSource(self, source: ThreadFeatureGeometry.ThreadDataSource) -> None:
        """
         Sets the source type for retrieving thread data 
        """
        pass
    def UpdateThreadParameters(self, tagFeature: Feature) -> None:
        """
         Update the feature thread parameters 
        """
        pass
