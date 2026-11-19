from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AssemblyOperationBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumDistributionFloatType(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |DirectionalBias| 
         |RotationalBias| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        DirectionalBias: int
        RotationalBias: int
        @staticmethod
        def ValueOf(value: int) -> AssemblyOperationBuilder.APIEnumDistributionFloatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DirectionDistributionI(self) -> float:
        """
        Getter for property: (float) DirectionDistributionI
         Returns the Normal distribution   
            
         
        """
        pass
    @DirectionDistributionI.setter
    def DirectionDistributionI(self, directionDistributionI: float):
        """
        Setter for property: (float) DirectionDistributionI
         Returns the Normal distribution   
            
         
        """
        pass
    @property
    def DirectionDistributionJ(self) -> float:
        """
        Getter for property: (float) DirectionDistributionJ
         Returns the  Normal distribution   
            
         
        """
        pass
    @DirectionDistributionJ.setter
    def DirectionDistributionJ(self, directionDistributionJ: float):
        """
        Setter for property: (float) DirectionDistributionJ
         Returns the  Normal distribution   
            
         
        """
        pass
    @property
    def DirectionDistributionK(self) -> float:
        """
        Getter for property: (float) DirectionDistributionK
         Returns the  Normal distribution   
            
         
        """
        pass
    @DirectionDistributionK.setter
    def DirectionDistributionK(self, directionDistributionK: float):
        """
        Setter for property: (float) DirectionDistributionK
         Returns the  Normal distribution   
            
         
        """
        pass
    @property
    def DistributionFloatType(self) -> AssemblyOperationBuilder.APIEnumDistributionFloatType:
        """
        Getter for property: ( AssemblyOperationBuilder.APIEnumDistributionFloatType NXOp) DistributionFloatType
         Returns the enum  Float Type.  
             
         
        """
        pass
    @DistributionFloatType.setter
    def DistributionFloatType(self, distributionFloatType: AssemblyOperationBuilder.APIEnumDistributionFloatType):
        """
        Setter for property: ( AssemblyOperationBuilder.APIEnumDistributionFloatType NXOp) DistributionFloatType
         Returns the enum  Float Type.  
             
         
        """
        pass
    @property
    def OverrideDefaultFloatDist(self) -> bool:
        """
        Getter for property: (bool) OverrideDefaultFloatDist
         Returns the property represents  override defualt distribution float flag.  
             
         
        """
        pass
    @OverrideDefaultFloatDist.setter
    def OverrideDefaultFloatDist(self, overrideDefaultFloatDist: bool):
        """
        Setter for property: (bool) OverrideDefaultFloatDist
         Returns the property represents  override defualt distribution float flag.  
             
         
        """
        pass
    @property
    def StrDescription(self) -> str:
        """
        Getter for property: (str) StrDescription
         Returns the str description   
            
         
        """
        pass
    @StrDescription.setter
    def StrDescription(self, strDescription: str):
        """
        Setter for property: (str) StrDescription
         Returns the str description   
            
         
        """
        pass
    @property
    def StrName(self) -> str:
        """
        Getter for property: (str) StrName
         Returns the str name   
            
         
        """
        pass
    @StrName.setter
    def StrName(self, strName: str):
        """
        Setter for property: (str) StrName
         Returns the str name   
            
         
        """
        pass
    def ButtonAdd(self) -> None:
        """
         It's a function to add constraints to the assembly operation  
        """
        pass
    def ButtonAutoOrder(self) -> None:
        """
         Function to auto order the existing constraints 
        """
        pass
    def ButtonClear(self) -> None:
        """
         It's a function to clears constraints from the dialog box 
        """
        pass
    def ButtonHideNormal(self) -> None:
        """
         Function to hide the shown normal 
        """
        pass
    def ButtonModify(self) -> None:
        """
         It's a function to modify the existing constraints
        """
        pass
    def ButtonMoveDown(self) -> None:
        """
         Function to move the existing constraint down 
        """
        pass
    def ButtonMoveUp(self) -> None:
        """
         Function to move the existing constraint up
        """
        pass
    def ButtonObjectRemove(self) -> None:
        """
         Function to remove the existing constraint 
        """
        pass
    def ButtonRemove(self) -> None:
        """
         It's a function to modify the existing constraints
        """
        pass
    def ButtonShowNormal(self) -> None:
        """
         Function to show normal of the selected constraint 
        """
        pass
    def ButtonValidate(self) -> None:
        """
         Function to modify the existing constraints
        """
        pass
    def GetConstraintObjetItem(self, index: int) -> NXOpen.NXObject:
        """
         The Constaint Object 
         Returns feature ( NXOpen.NXObject): .
        """
        pass
    def GetConstraintTargetItem(self, index: int) -> NXOpen.NXObject:
        """
         The Constaint Target 
         Returns feature ( NXOpen.NXObject): .
        """
        pass
    def GetFastenerSizeItem(self, index: int) -> float:
        """
         The Fastener Size 
         Returns fastenerSize (float): .
        """
        pass
    def GetFastenerTypeItem(self, index: int) -> bool:
        """
         The Fastner Type 
         Returns fastnerType (bool): .
        """
        pass
    def GetFloatTypeItem(self, index: int) -> bool:
        """
         The Float Type 
         Returns floatType (bool): .
        """
        pass
    def GetObjectBeingMovedItem(self, index: int) -> NXOpen.NXObject:
        """
         Gets One Object Being Moved 
         Returns part ( NXOpen.NXObject): .
        """
        pass
    def RemoveConstraint(self, index: int) -> None:
        """
         The Remove Constraint 
        """
        pass
    def SetConstraintObjetItem(self, index: int, feature: NXOpen.NXObject) -> None:
        """
         The Constaint Object 
        """
        pass
    def SetConstraintTargetItem(self, index: int, feature: NXOpen.NXObject) -> None:
        """
         The Constaint Target 
        """
        pass
    def SetFastenerSizeItem(self, index: int, fastenerSize: float) -> None:
        """
         The Fastener Size 
        """
        pass
    def SetFastenerTypeItem(self, index: int, fastnerType: bool) -> None:
        """
         The Float Type 
        """
        pass
    def SetFloatTypeItem(self, index: int, floatType: bool) -> None:
        """
         The Float Type 
        """
        pass
    def SetObjectBeingMovedItem(self, index: int, part: NXOpen.NXObject) -> None:
        """
         Sets One Object Being Moved 
        """
        pass
    def SwapConstraint(self, nIndex1: int, nIndex2: int) -> None:
        """
         The swap the existing  Constraint 
        """
        pass
import NXOpen
class AutotestValidation(NXOpen.Object): 
    """ Represents a class that is used for NX testing.  This class should not
    be made available to customers """
    def ValidateObjectDetailsPane() -> None:
        """
         Print the entire vsa object details 
        """
        pass
    def ValidateSimulationResultAll() -> None:
        """
         Print all Measurement operation simulation result 
        """
        pass
import NXOpen
class BallFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> BallFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> BallFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> BallFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
         Returns the double anchor x   
            
         
        """
        pass
    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
         Returns the double anchor x   
            
         
        """
        pass
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
         Returns the double anchor y   
            
         
        """
        pass
    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
         Returns the double anchor y   
            
         
        """
        pass
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
         Returns the double anchor z   
            
         
        """
        pass
    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
         Returns the double anchor z   
            
         
        """
        pass
    @property
    def DoubleDiameter(self) -> float:
        """
        Getter for property: (float) DoubleDiameter
         Returns the double diameter   
            
         
        """
        pass
    @DoubleDiameter.setter
    def DoubleDiameter(self, doubleDiameter: float):
        """
        Setter for property: (float) DoubleDiameter
         Returns the double diameter   
            
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def EnumForm(self) -> BallFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( BallFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: BallFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( BallFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @property
    def EnumLoc(self) -> BallFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( BallFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: BallFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( BallFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @property
    def EnumSize(self) -> BallFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( BallFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: BallFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( BallFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
import NXOpen
class BallFeature(NXOpen.NXObject): 
    """ Represents a Ball feature """
    pass
import NXOpen
class DPVInspectionRoutineBuilder(NXOpen.Builder): 
    """
    
    """
    pass
import NXOpen
class FixturePlaneFeatureBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Vsa.FixturePlaneFeatureBuilder """
    class APIFormType(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> FixturePlaneFeatureBuilder.APIFormType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APILocType(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> FixturePlaneFeatureBuilder.APILocType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APISizeType(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> FixturePlaneFeatureBuilder.APISizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the string description   
            
         
        """
        pass
    @Description.setter
    def Description(self, stringDescription: str):
        """
        Setter for property: (str) Description
         Returns the string description   
            
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def FormType(self) -> FixturePlaneFeatureBuilder.APIFormType:
        """
        Getter for property: ( FixturePlaneFeatureBuilder.APIFormType NXOp) FormType
         Returns the enum form   
            
         
        """
        pass
    @FormType.setter
    def FormType(self, formType: FixturePlaneFeatureBuilder.APIFormType):
        """
        Setter for property: ( FixturePlaneFeatureBuilder.APIFormType NXOp) FormType
         Returns the enum form   
            
         
        """
        pass
    @property
    def I(self) -> float:
        """
        Getter for property: (float) I
         Returns the i   
            
         
        """
        pass
    @I.setter
    def I(self, i: float):
        """
        Setter for property: (float) I
         Returns the i   
            
         
        """
        pass
    @property
    def ILength(self) -> float:
        """
        Getter for property: (float) ILength
         Returns the length vector I  
            
         
        """
        pass
    @ILength.setter
    def ILength(self, vectorI: float):
        """
        Setter for property: (float) ILength
         Returns the length vector I  
            
         
        """
        pass
    @property
    def J(self) -> float:
        """
        Getter for property: (float) J
         Returns the j   
            
         
        """
        pass
    @J.setter
    def J(self, j: float):
        """
        Setter for property: (float) J
         Returns the j   
            
         
        """
        pass
    @property
    def JLength(self) -> float:
        """
        Getter for property: (float) JLength
         Returns the length vector J  
            
         
        """
        pass
    @JLength.setter
    def JLength(self, vectorJ: float):
        """
        Setter for property: (float) JLength
         Returns the length vector J  
            
         
        """
        pass
    @property
    def K(self) -> float:
        """
        Getter for property: (float) K
         Returns the k   
            
         
        """
        pass
    @K.setter
    def K(self, k: float):
        """
        Setter for property: (float) K
         Returns the k   
            
         
        """
        pass
    @property
    def KLength(self) -> float:
        """
        Getter for property: (float) KLength
         Returns the length vector K  
            
         
        """
        pass
    @KLength.setter
    def KLength(self, vectorK: float):
        """
        Setter for property: (float) KLength
         Returns the length vector K  
            
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length Length  
            
         
        """
        pass
    @Length.setter
    def Length(self, length: float):
        """
        Setter for property: (float) Length
         Returns the length Length  
            
         
        """
        pass
    @property
    def LocType(self) -> FixturePlaneFeatureBuilder.APILocType:
        """
        Getter for property: ( FixturePlaneFeatureBuilder.APILocType NXOp) LocType
         Returns the enum loc   
            
         
        """
        pass
    @LocType.setter
    def LocType(self, locType: FixturePlaneFeatureBuilder.APILocType):
        """
        Setter for property: ( FixturePlaneFeatureBuilder.APILocType NXOp) LocType
         Returns the enum loc   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @property
    def SizeType(self) -> FixturePlaneFeatureBuilder.APISizeType:
        """
        Getter for property: ( FixturePlaneFeatureBuilder.APISizeType NXOp) SizeType
         Returns the enum size   
            
         
        """
        pass
    @SizeType.setter
    def SizeType(self, sizeType: FixturePlaneFeatureBuilder.APISizeType):
        """
        Setter for property: ( FixturePlaneFeatureBuilder.APISizeType NXOp) SizeType
         Returns the enum size   
            
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the length Width  
            
         
        """
        pass
    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the length Width  
            
         
        """
        pass
    @property
    def X(self) -> float:
        """
        Getter for property: (float) X
         Returns the x   
            
         
        """
        pass
    @X.setter
    def X(self, x: float):
        """
        Setter for property: (float) X
         Returns the x   
            
         
        """
        pass
    @property
    def Y(self) -> float:
        """
        Getter for property: (float) Y
         Returns the y   
            
         
        """
        pass
    @Y.setter
    def Y(self, y: float):
        """
        Setter for property: (float) Y
         Returns the y   
            
         
        """
        pass
    @property
    def Z(self) -> float:
        """
        Getter for property: (float) Z
         Returns the z   
            
         
        """
        pass
    @Z.setter
    def Z(self, z: float):
        """
        Setter for property: (float) Z
         Returns the z   
            
         
        """
        pass
import NXOpen
class FixturePlaneFeature(NXOpen.Object): 
    """ Represents a Fixture Plane Feature """
    pass
import NXOpen
class GDTMeasurementOperationBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumNameFormat(Enum):
        """
        Members Include: 
         |Short| 
         |Long| 

        """
        Short: int
        Long: int
        @staticmethod
        def ValueOf(value: int) -> GDTMeasurementOperationBuilder.APIEnumNameFormat:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIGeometricChar(Enum):
        """
        Members Include: 
         |Position| 
         |Profile| 
         |Angularity| 
         |Flatness| 

        """
        Position: int
        Profile: int
        Angularity: int
        Flatness: int
        @staticmethod
        def ValueOf(value: int) -> GDTMeasurementOperationBuilder.APIGeometricChar:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EnumNameFormat(self) -> GDTMeasurementOperationBuilder.APIEnumNameFormat:
        """
        Getter for property: ( GDTMeasurementOperationBuilder.APIEnumNameFormat NXOp) EnumNameFormat
         Returns the Name Format   
            
         
        """
        pass
    @EnumNameFormat.setter
    def EnumNameFormat(self, nameFormat: GDTMeasurementOperationBuilder.APIEnumNameFormat):
        """
        Setter for property: ( GDTMeasurementOperationBuilder.APIEnumNameFormat NXOp) EnumNameFormat
         Returns the Name Format   
            
         
        """
        pass
    @property
    def GeaomCharacteristic(self) -> GDTMeasurementOperationBuilder.APIGeometricChar:
        """
        Getter for property: ( GDTMeasurementOperationBuilder.APIGeometricChar NXOp) GeaomCharacteristic
         Returns the geom characteristic   
            
         
        """
        pass
    @GeaomCharacteristic.setter
    def GeaomCharacteristic(self, geomChar: GDTMeasurementOperationBuilder.APIGeometricChar):
        """
        Setter for property: ( GDTMeasurementOperationBuilder.APIGeometricChar NXOp) GeaomCharacteristic
         Returns the geom characteristic   
            
         
        """
        pass
    @property
    def MeasurementZoneLimit(self) -> float:
        """
        Getter for property: (float) MeasurementZoneLimit
         Returns the MeasurementZoneLimit   
            
         
        """
        pass
    @MeasurementZoneLimit.setter
    def MeasurementZoneLimit(self, measurementZoneLimit: float):
        """
        Setter for property: (float) MeasurementZoneLimit
         Returns the MeasurementZoneLimit   
            
         
        """
        pass
    @property
    def StrDescription(self) -> str:
        """
        Getter for property: (str) StrDescription
         Returns the str description   
            
         
        """
        pass
    @StrDescription.setter
    def StrDescription(self, strDescription: str):
        """
        Setter for property: (str) StrDescription
         Returns the str description   
            
         
        """
        pass
    @property
    def StrName(self) -> str:
        """
        Getter for property: (str) StrName
         Returns the str name   
            
         
        """
        pass
    @StrName.setter
    def StrName(self, strName: str):
        """
        Setter for property: (str) StrName
         Returns the str name   
            
         
        """
        pass
    def GetMeasuredFeature(self) -> NXOpen.NXObject:
        """
         The measured feature 
         Returns feature ( NXOpen.NXObject): .
        """
        pass
    def GetPrimaryDatumFeatureItem(self, index: int) -> NXOpen.NXObject:
        """
         The primary datum feature 
         Returns feature ( NXOpen.NXObject): .
        """
        pass
    def GetSecondaryDatumFeatureItem(self, index: int) -> NXOpen.NXObject:
        """
         The secondary datum feature 
         Returns feature ( NXOpen.NXObject): .
        """
        pass
    def GetTertiaryDatumFeatureItem(self, index: int) -> NXOpen.NXObject:
        """
         The tertiary datum feature 
         Returns feature ( NXOpen.NXObject): .
        """
        pass
    def RemoveDatumFeature(self, ntype: int, nIndex: int) -> None:
        """
         The Remove Datum Feature 
        """
        pass
    def SetMeasuredFeature(self, feature: NXOpen.NXObject) -> None:
        """
         The measured feature 
        """
        pass
    def SetPrimaryDatumFeatureItem(self, index: int, feature: NXOpen.NXObject) -> None:
        """
         The primary datum feature 
        """
        pass
    def SetSecondaryDatumFeatureItem(self, index: int, feature: NXOpen.NXObject) -> None:
        """
         The secondary datum feature 
        """
        pass
    def SetTertiaryDatumFeatureItem(self, index: int, feature: NXOpen.NXObject) -> None:
        """
         The tertiary datum feature 
        """
        pass
    def SwapDatumFeature(self, ntype: int, nIndex1: int, nIndex2: int) -> None:
        """
         The swap the existing  Datum Feature 
        """
        pass
import NXOpen
class GeneralSurfaceFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> GeneralSurfaceFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> GeneralSurfaceFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> GeneralSurfaceFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the string description   
            
         
        """
        pass
    @Description.setter
    def Description(self, stringDescription: str):
        """
        Setter for property: (str) Description
         Returns the string description   
            
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def EnumForm(self) -> GeneralSurfaceFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( GeneralSurfaceFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: GeneralSurfaceFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( GeneralSurfaceFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @property
    def EnumLoc(self) -> GeneralSurfaceFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( GeneralSurfaceFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: GeneralSurfaceFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( GeneralSurfaceFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @property
    def EnumSize(self) -> GeneralSurfaceFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( GeneralSurfaceFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: GeneralSurfaceFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( GeneralSurfaceFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
import NXOpen
class HoleFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> HoleFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> HoleFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> HoleFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
         Returns the double anchor x   
            
         
        """
        pass
    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
         Returns the double anchor x   
            
         
        """
        pass
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
         Returns the double anchor y   
            
         
        """
        pass
    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
         Returns the double anchor y   
            
         
        """
        pass
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
         Returns the double anchor z   
            
         
        """
        pass
    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
         Returns the double anchor z   
            
         
        """
        pass
    @property
    def DoubleDiameter1(self) -> float:
        """
        Getter for property: (float) DoubleDiameter1
         Returns the double diameter1   
            
         
        """
        pass
    @DoubleDiameter1.setter
    def DoubleDiameter1(self, doubleDiameter1: float):
        """
        Setter for property: (float) DoubleDiameter1
         Returns the double diameter1   
            
         
        """
        pass
    @property
    def DoubleDiameter2(self) -> float:
        """
        Getter for property: (float) DoubleDiameter2
         Returns the double diameter2   
            
         
        """
        pass
    @DoubleDiameter2.setter
    def DoubleDiameter2(self, doubleDiameter2: float):
        """
        Setter for property: (float) DoubleDiameter2
         Returns the double diameter2   
            
         
        """
        pass
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
         Returns the double direction i   
            
         
        """
        pass
    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
         Returns the double direction i   
            
         
        """
        pass
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
         Returns the double direction j   
            
         
        """
        pass
    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
         Returns the double direction j   
            
         
        """
        pass
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
         Returns the double direction k   
            
         
        """
        pass
    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
         Returns the double direction k   
            
         
        """
        pass
    @property
    def DoubleHeight(self) -> float:
        """
        Getter for property: (float) DoubleHeight
         Returns the double height   
            
         
        """
        pass
    @DoubleHeight.setter
    def DoubleHeight(self, doubleHeight: float):
        """
        Setter for property: (float) DoubleHeight
         Returns the double height   
            
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def EnumForm(self) -> HoleFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( HoleFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: HoleFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( HoleFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @property
    def EnumLoc(self) -> HoleFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( HoleFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: HoleFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( HoleFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @property
    def EnumSize(self) -> HoleFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( HoleFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: HoleFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( HoleFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
import NXOpen
class HoleFeature(NXOpen.NXObject): 
    """ Represents a Hole feature """
    pass
import NXOpen
class HolePatternFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> HolePatternFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> HolePatternFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> HolePatternFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def EnumForm(self) -> HolePatternFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( HolePatternFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: HolePatternFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( HolePatternFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @property
    def EnumLoc(self) -> HolePatternFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( HolePatternFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: HolePatternFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( HolePatternFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @property
    def EnumSize(self) -> HolePatternFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( HolePatternFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: HolePatternFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( HolePatternFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @property
    def NumInstanceCount(self) -> int:
        """
        Getter for property: (int) NumInstanceCount
         Returns the enum size   
            
         
        """
        pass
    @NumInstanceCount.setter
    def NumInstanceCount(self, numInstanceCount: int):
        """
        Setter for property: (int) NumInstanceCount
         Returns the enum size   
            
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
import NXOpen
class HolePatternFeature(NXOpen.NXObject): 
    """ Represents a Hole pattern feature """
    pass
import NXOpen
class MeasurementOperationBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumLimitType(Enum):
        """
        Members Include: 
         |Relative| 
         |Absolute| 

        """
        Relative: int
        Absolute: int
        @staticmethod
        def ValueOf(value: int) -> MeasurementOperationBuilder.APIEnumLimitType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumMeasurementType(Enum):
        """
        Members Include: 
         |Angle| 
         |GapFlush| 
         |PointToPoint| 
         |PointToLine| 
         |Point| 
         |MinimumVirtualClearance| 
         |MinimumFeatureClearance| 
         |VirtualHoleDiameter| 

        """
        Angle: int
        GapFlush: int
        PointToPoint: int
        PointToLine: int
        Point: int
        MinimumVirtualClearance: int
        MinimumFeatureClearance: int
        VirtualHoleDiameter: int
        @staticmethod
        def ValueOf(value: int) -> MeasurementOperationBuilder.APIEnumMeasurementType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumNameFormat(Enum):
        """
        Members Include: 
         |Short| 
         |Long| 

        """
        Short: int
        Long: int
        @staticmethod
        def ValueOf(value: int) -> MeasurementOperationBuilder.APIEnumNameFormat:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DirectionI(self) -> float:
        """
        Getter for property: (float) DirectionI
         Returns the Nominal   
            
         
        """
        pass
    @DirectionI.setter
    def DirectionI(self, directionI: float):
        """
        Setter for property: (float) DirectionI
         Returns the Nominal   
            
         
        """
        pass
    @property
    def DirectionJ(self) -> float:
        """
        Getter for property: (float) DirectionJ
         Returns the Nominal   
            
         
        """
        pass
    @DirectionJ.setter
    def DirectionJ(self, directionJ: float):
        """
        Setter for property: (float) DirectionJ
         Returns the Nominal   
            
         
        """
        pass
    @property
    def DirectionK(self) -> float:
        """
        Getter for property: (float) DirectionK
         Returns the Nominal   
            
         
        """
        pass
    @DirectionK.setter
    def DirectionK(self, directionK: float):
        """
        Setter for property: (float) DirectionK
         Returns the Nominal   
            
         
        """
        pass
    @property
    def FeatureFrom1(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) FeatureFrom1
         Returns the From Feature1   
            
         
        """
        pass
    @FeatureFrom1.setter
    def FeatureFrom1(self, featureFrom1: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) FeatureFrom1
         Returns the From Feature1   
            
         
        """
        pass
    @property
    def FeatureFrom2(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) FeatureFrom2
         Returns the From Feature2   
            
         
        """
        pass
    @FeatureFrom2.setter
    def FeatureFrom2(self, featureFrom2: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) FeatureFrom2
         Returns the From Feature2   
            
         
        """
        pass
    @property
    def FeatureFrom3(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) FeatureFrom3
         Returns the From Feature3   
            
         
        """
        pass
    @FeatureFrom3.setter
    def FeatureFrom3(self, featureFrom3: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) FeatureFrom3
         Returns the From Feature3   
            
         
        """
        pass
    @property
    def FeatureTo1(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) FeatureTo1
         Returns the From To1   
            
         
        """
        pass
    @FeatureTo1.setter
    def FeatureTo1(self, featureTo1: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) FeatureTo1
         Returns the From To1   
            
         
        """
        pass
    @property
    def FeatureTo2(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) FeatureTo2
         Returns the From To1   
            
         
        """
        pass
    @FeatureTo2.setter
    def FeatureTo2(self, featureTo2: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) FeatureTo2
         Returns the From To1   
            
         
        """
        pass
    @property
    def FeatureTo3(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) FeatureTo3
         Returns the From To1   
            
         
        """
        pass
    @FeatureTo3.setter
    def FeatureTo3(self, featureTo3: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) FeatureTo3
         Returns the From To1   
            
         
        """
        pass
    @property
    def LimitType(self) -> MeasurementOperationBuilder.APIEnumLimitType:
        """
        Getter for property: ( MeasurementOperationBuilder.APIEnumLimitType NXOp) LimitType
         Returns the Limit Type   
            
         
        """
        pass
    @LimitType.setter
    def LimitType(self, specifyType: MeasurementOperationBuilder.APIEnumLimitType):
        """
        Setter for property: ( MeasurementOperationBuilder.APIEnumLimitType NXOp) LimitType
         Returns the Limit Type   
            
         
        """
        pass
    @property
    def Lsl(self) -> float:
        """
        Getter for property: (float) Lsl
         Returns the Nominal   
            
         
        """
        pass
    @Lsl.setter
    def Lsl(self, lsl: float):
        """
        Setter for property: (float) Lsl
         Returns the Nominal   
            
         
        """
        pass
    @property
    def MeasurementType(self) -> MeasurementOperationBuilder.APIEnumMeasurementType:
        """
        Getter for property: ( MeasurementOperationBuilder.APIEnumMeasurementType NXOp) MeasurementType
         Returns the enum Measurement Type   
            
         
        """
        pass
    @MeasurementType.setter
    def MeasurementType(self, measurementType: MeasurementOperationBuilder.APIEnumMeasurementType):
        """
        Setter for property: ( MeasurementOperationBuilder.APIEnumMeasurementType NXOp) MeasurementType
         Returns the enum Measurement Type   
            
         
        """
        pass
    @property
    def NameFormat(self) -> MeasurementOperationBuilder.APIEnumNameFormat:
        """
        Getter for property: ( MeasurementOperationBuilder.APIEnumNameFormat NXOp) NameFormat
         Returns the Name Format   
            
         
        """
        pass
    @NameFormat.setter
    def NameFormat(self, nameFormat: MeasurementOperationBuilder.APIEnumNameFormat):
        """
        Setter for property: ( MeasurementOperationBuilder.APIEnumNameFormat NXOp) NameFormat
         Returns the Name Format   
            
         
        """
        pass
    @property
    def Nominal(self) -> float:
        """
        Getter for property: (float) Nominal
         Returns the Nominal   
            
         
        """
        pass
    @Nominal.setter
    def Nominal(self, nominal: float):
        """
        Setter for property: (float) Nominal
         Returns the Nominal   
            
         
        """
        pass
    @property
    def StrDescription(self) -> str:
        """
        Getter for property: (str) StrDescription
         Returns the str description   
            
         
        """
        pass
    @StrDescription.setter
    def StrDescription(self, strDescription: str):
        """
        Setter for property: (str) StrDescription
         Returns the str description   
            
         
        """
        pass
    @property
    def StrName(self) -> str:
        """
        Getter for property: (str) StrName
         Returns the str name   
            
         
        """
        pass
    @StrName.setter
    def StrName(self, strName: str):
        """
        Setter for property: (str) StrName
         Returns the str name   
            
         
        """
        pass
    @property
    def ToggleLimit(self) -> bool:
        """
        Getter for property: (bool) ToggleLimit
         Returns the toggle limit  
            
         
        """
        pass
    @ToggleLimit.setter
    def ToggleLimit(self, toggleLimit: bool):
        """
        Setter for property: (bool) ToggleLimit
         Returns the toggle limit  
            
         
        """
        pass
    @property
    def Usl(self) -> float:
        """
        Getter for property: (float) Usl
         Returns the USL   
            
         
        """
        pass
    @Usl.setter
    def Usl(self, usl: float):
        """
        Setter for property: (float) Usl
         Returns the USL   
            
         
        """
        pass
    def GetVirtualHoleDiameterFeatureObjectListItem(self, index: int) -> NXOpen.NXObject:
        """
         The Virtual Hole Diameter Features 
         Returns feature ( NXOpen.NXObject): .
        """
        pass
    def RemoveVirtualHoleDiameterFeatureObjectListItem(self, index: int) -> None:
        """
         The Remove Virtual Hole Diameter Feature 
        """
        pass
    def SetVirtualHoleDiameterFeatureObjectListItem(self, index: int, feature: NXOpen.NXObject) -> None:
        """
         The Virtual Hole Diameter Features 
        """
        pass
    def SwapVirtualHoleDiameterFeatureObjectListItem(self, nIndex1: int, nIndex2: int) -> None:
        """
         The Swap Virtual Hole Diameter Features 
        """
        pass
import NXOpen
class PartPropertyBuilder(NXOpen.Builder): 
    """
    
    """
    @property
    def ChordLength(self) -> float:
        """
        Getter for property: (float) ChordLength
         Returns the double Chord Length   
            
         
        """
        pass
    @ChordLength.setter
    def ChordLength(self, chordLength: float):
        """
        Setter for property: (float) ChordLength
         Returns the double Chord Length   
            
         
        """
        pass
    @property
    def MaximumSag(self) -> float:
        """
        Getter for property: (float) MaximumSag
         Returns the double Maximum Sag   
            
         
        """
        pass
    @MaximumSag.setter
    def MaximumSag(self, maximumSag: float):
        """
        Setter for property: (float) MaximumSag
         Returns the double Maximum Sag   
            
         
        """
        pass
    @property
    def PartName(self) -> str:
        """
        Getter for property: (str) PartName
         Returns the string name   
            
         
        """
        pass
    @PartName.setter
    def PartName(self, partName: str):
        """
        Setter for property: (str) PartName
         Returns the string name   
            
         
        """
        pass
import NXOpen
class PartProperty(NXOpen.NXObject): 
    """ Represents a Part Property """
    pass
import NXOpen
class PinFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> PinFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> PinFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> PinFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
         Returns the double anchor x   
            
         
        """
        pass
    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
         Returns the double anchor x   
            
         
        """
        pass
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
         Returns the double anchor y   
            
         
        """
        pass
    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
         Returns the double anchor y   
            
         
        """
        pass
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
         Returns the double anchor z   
            
         
        """
        pass
    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
         Returns the double anchor z   
            
         
        """
        pass
    @property
    def DoubleDiameter1(self) -> float:
        """
        Getter for property: (float) DoubleDiameter1
         Returns the double diameter1   
            
         
        """
        pass
    @DoubleDiameter1.setter
    def DoubleDiameter1(self, doubleDiameter1: float):
        """
        Setter for property: (float) DoubleDiameter1
         Returns the double diameter1   
            
         
        """
        pass
    @property
    def DoubleDiameter2(self) -> float:
        """
        Getter for property: (float) DoubleDiameter2
         Returns the double diameter2   
            
         
        """
        pass
    @DoubleDiameter2.setter
    def DoubleDiameter2(self, doubleDiameter2: float):
        """
        Setter for property: (float) DoubleDiameter2
         Returns the double diameter2   
            
         
        """
        pass
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
         Returns the double direction i   
            
         
        """
        pass
    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
         Returns the double direction i   
            
         
        """
        pass
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
         Returns the double direction j   
            
         
        """
        pass
    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
         Returns the double direction j   
            
         
        """
        pass
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
         Returns the double direction k   
            
         
        """
        pass
    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
         Returns the double direction k   
            
         
        """
        pass
    @property
    def DoubleHeight(self) -> float:
        """
        Getter for property: (float) DoubleHeight
         Returns the double height   
            
         
        """
        pass
    @DoubleHeight.setter
    def DoubleHeight(self, doubleHeight: float):
        """
        Setter for property: (float) DoubleHeight
         Returns the double height   
            
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def EnumForm(self) -> PinFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( PinFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: PinFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( PinFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @property
    def EnumLoc(self) -> PinFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( PinFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: PinFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( PinFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @property
    def EnumSize(self) -> PinFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( PinFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: PinFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( PinFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
import NXOpen
class PinFeature(NXOpen.NXObject): 
    """ Represents a Pin feature """
    pass
import NXOpen
class PinPatternFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> PinPatternFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> PinPatternFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> PinPatternFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def EnumForm(self) -> PinPatternFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( PinPatternFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: PinPatternFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( PinPatternFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @property
    def EnumLoc(self) -> PinPatternFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( PinPatternFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: PinPatternFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( PinPatternFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @property
    def EnumSize(self) -> PinPatternFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( PinPatternFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: PinPatternFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( PinPatternFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
import NXOpen
class PinPatternFeature(NXOpen.NXObject): 
    """ Represents a pin pattern feature """
    pass
import NXOpen
class PlaneFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> PlaneFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> PlaneFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> PlaneFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the string description   
            
         
        """
        pass
    @Description.setter
    def Description(self, stringDescription: str):
        """
        Setter for property: (str) Description
         Returns the string description   
            
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def EnumForm(self) -> PlaneFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( PlaneFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: PlaneFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( PlaneFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @property
    def EnumLoc(self) -> PlaneFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( PlaneFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: PlaneFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( PlaneFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @property
    def EnumSize(self) -> PlaneFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( PlaneFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: PlaneFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( PlaneFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @property
    def I(self) -> float:
        """
        Getter for property: (float) I
         Returns the i   
            
         
        """
        pass
    @I.setter
    def I(self, i: float):
        """
        Setter for property: (float) I
         Returns the i   
            
         
        """
        pass
    @property
    def J(self) -> float:
        """
        Getter for property: (float) J
         Returns the j   
            
         
        """
        pass
    @J.setter
    def J(self, j: float):
        """
        Setter for property: (float) J
         Returns the j   
            
         
        """
        pass
    @property
    def K(self) -> float:
        """
        Getter for property: (float) K
         Returns the k   
            
         
        """
        pass
    @K.setter
    def K(self, k: float):
        """
        Setter for property: (float) K
         Returns the k   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @property
    def X(self) -> float:
        """
        Getter for property: (float) X
         Returns the x   
            
         
        """
        pass
    @X.setter
    def X(self, x: float):
        """
        Setter for property: (float) X
         Returns the x   
            
         
        """
        pass
    @property
    def Y(self) -> float:
        """
        Getter for property: (float) Y
         Returns the y   
            
         
        """
        pass
    @Y.setter
    def Y(self, y: float):
        """
        Setter for property: (float) Y
         Returns the y   
            
         
        """
        pass
    @property
    def Z(self) -> float:
        """
        Getter for property: (float) Z
         Returns the z   
            
         
        """
        pass
    @Z.setter
    def Z(self, z: float):
        """
        Setter for property: (float) Z
         Returns the z   
            
         
        """
        pass
import NXOpen
class PointFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> PointFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> PointFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> PointFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
         Returns the property represents X value of anchore.  
             
         
        """
        pass
    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
         Returns the property represents X value of anchore.  
             
         
        """
        pass
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
         Returns the property represents Y value of anchore.  
             
         
        """
        pass
    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
         Returns the property represents Y value of anchore.  
             
         
        """
        pass
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
         Returns the property represents Z value of anchore.  
             
         
        """
        pass
    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
         Returns the property represents Z value of anchore.  
             
         
        """
        pass
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
         Returns the property represents X value of normal.  
             
         
        """
        pass
    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
         Returns the property represents X value of normal.  
             
         
        """
        pass
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
         Returns the property represents Y value of normal.  
             
         
        """
        pass
    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
         Returns the property represents Y value of normal.  
             
         
        """
        pass
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
         Returns the property represents Z value of normal.  
             
         
        """
        pass
    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
         Returns the property represents Z value of normal.  
             
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the property represents Form distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the property represents Form distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the property represents Loc distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the property represents Loc distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the property represents Size distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the property represents Size distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the property represents Form distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the property represents Form distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the property represents Loc distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the property represents Loc distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the property represents Size distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the property represents Size distribution Skewness.  
             
         
        """
        pass
    @property
    def EnumForm(self) -> PointFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( PointFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the property represents Form distribution type.  
             
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: PointFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( PointFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the property represents Form distribution type.  
             
         
        """
        pass
    @property
    def EnumLoc(self) -> PointFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( PointFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the property represents Loc distribution type.  
             
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: PointFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( PointFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the property represents Loc distribution type.  
             
         
        """
        pass
    @property
    def EnumSize(self) -> PointFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( PointFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the property represents Size distribution type.  
             
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: PointFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( PointFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the property represents Size distribution type.  
             
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the property represents point feature discription.  
             
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the property represents point feature discription.  
             
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the property represents Point feature name.  
             
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the property represents Point feature name.  
             
         
        """
        pass
import NXOpen
class PointFeature(NXOpen.NXObject): 
    """ Represents a Point feature """
    pass
import NXOpen
class PointSubFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumPointType(Enum):
        """
        Members Include: 
         |OnSurface| 
         |OnAnchor| 
         |OnCenter| 
         |OnTop| 

        """
        OnSurface: int
        OnAnchor: int
        OnCenter: int
        OnTop: int
        @staticmethod
        def ValueOf(value: int) -> PointSubFeatureBuilder.APIEnumPointType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssociatedPointTag(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) AssociatedPointTag
         Returns the property represents associated point tag.  
             
         
        """
        pass
    @AssociatedPointTag.setter
    def AssociatedPointTag(self, associatedPointTag: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) AssociatedPointTag
         Returns the property represents associated point tag.  
             
         
        """
        pass
    @property
    def PointSubFeatureType(self) -> PointSubFeatureBuilder.APIEnumPointType:
        """
        Getter for property: ( PointSubFeatureBuilder.APIEnumPointType NXOp) PointSubFeatureType
         Returns the property represents  point subfeature type.  
             
         
        """
        pass
    @PointSubFeatureType.setter
    def PointSubFeatureType(self, pointSubFeatureType: PointSubFeatureBuilder.APIEnumPointType):
        """
        Setter for property: ( PointSubFeatureBuilder.APIEnumPointType NXOp) PointSubFeatureType
         Returns the property represents  point subfeature type.  
             
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the property represents  point subfeature discription.  
             
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the property represents  point subfeature discription.  
             
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the property represents  point subfeature name.  
             
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the property represents  point subfeature name.  
             
         
        """
        pass
import NXOpen
class PointSubFeature(NXOpen.NXObject): 
    """ Represents a Point Sub feature """
    pass
import NXOpen
class ProjectPointsBuilder(NXOpen.Builder): 
    """
    
    """
    pass
import NXOpen
class SimulationPreferencesBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumDistributionFloatType(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        @staticmethod
        def ValueOf(value: int) -> SimulationPreferencesBuilder.APIEnumDistributionFloatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AcceptInterferenceBuild(self) -> bool:
        """
        Getter for property: (bool) AcceptInterferenceBuild
         Returns the property represents AcceptInterferenceBuild.  
             
         
        """
        pass
    @AcceptInterferenceBuild.setter
    def AcceptInterferenceBuild(self, acceptInterferenceBuild: bool):
        """
        Setter for property: (bool) AcceptInterferenceBuild
         Returns the property represents AcceptInterferenceBuild.  
             
         
        """
        pass
    @property
    def AlternativeToleranceValues(self) -> bool:
        """
        Getter for property: (bool) AlternativeToleranceValues
         Returns the property represents AlternativeToleranceValues.  
             
         
        """
        pass
    @AlternativeToleranceValues.setter
    def AlternativeToleranceValues(self, alternativeToleranceValues: bool):
        """
        Setter for property: (bool) AlternativeToleranceValues
         Returns the property represents AlternativeToleranceValues.  
             
         
        """
        pass
    @property
    def AnimateSimulation(self) -> bool:
        """
        Getter for property: (bool) AnimateSimulation
         Returns the property represents Animate Simulation flag.  
             
         
        """
        pass
    @AnimateSimulation.setter
    def AnimateSimulation(self, animateSimulation: bool):
        """
        Setter for property: (bool) AnimateSimulation
         Returns the property represents Animate Simulation flag.  
             
         
        """
        pass
    @property
    def AnimationDelay(self) -> int:
        """
        Getter for property: (int) AnimationDelay
         Returns the property represents Animation Delay.  
             
         
        """
        pass
    @AnimationDelay.setter
    def AnimationDelay(self, animateDelay: int):
        """
        Setter for property: (int) AnimationDelay
         Returns the property represents Animation Delay.  
             
         
        """
        pass
    @property
    def Cp(self) -> bool:
        """
        Getter for property: (bool) Cp
         Returns the property represents  Cp.  
             
         
        """
        pass
    @Cp.setter
    def Cp(self, cp: bool):
        """
        Setter for property: (bool) Cp
         Returns the property represents  Cp.  
             
         
        """
        pass
    @property
    def Cpk(self) -> bool:
        """
        Getter for property: (bool) Cpk
         Returns the property represents  Cpk.  
             
         
        """
        pass
    @Cpk.setter
    def Cpk(self, cpk: bool):
        """
        Setter for property: (bool) Cpk
         Returns the property represents  Cpk.  
             
         
        """
        pass
    @property
    def CutoffPercent(self) -> float:
        """
        Getter for property: (float) CutoffPercent
         Returns the property represents  CutoffPercent.  
             
         
        """
        pass
    @CutoffPercent.setter
    def CutoffPercent(self, cutoffPercent: float):
        """
        Setter for property: (float) CutoffPercent
         Returns the property represents  CutoffPercent.  
             
         
        """
        pass
    @property
    def DecimalPlaces(self) -> int:
        """
        Getter for property: (int) DecimalPlaces
         Returns the property represents  DecimalPlaces.  
             
         
        """
        pass
    @DecimalPlaces.setter
    def DecimalPlaces(self, decimalPlaces: int):
        """
        Setter for property: (int) DecimalPlaces
         Returns the property represents  DecimalPlaces.  
             
         
        """
        pass
    @property
    def DistributionFloatType(self) -> SimulationPreferencesBuilder.APIEnumDistributionFloatType:
        """
        Getter for property: ( SimulationPreferencesBuilder.APIEnumDistributionFloatType NXOp) DistributionFloatType
         Returns the enum  Float Type.  
             
         
        """
        pass
    @DistributionFloatType.setter
    def DistributionFloatType(self, distributionFloatType: SimulationPreferencesBuilder.APIEnumDistributionFloatType):
        """
        Setter for property: ( SimulationPreferencesBuilder.APIEnumDistributionFloatType NXOp) DistributionFloatType
         Returns the enum  Float Type.  
             
         
        """
        pass
    @property
    def EstimatedHigh(self) -> bool:
        """
        Getter for property: (bool) EstimatedHigh
         Returns the property represents  EstimatedHigh.  
             
         
        """
        pass
    @EstimatedHigh.setter
    def EstimatedHigh(self, estimatedHigh: bool):
        """
        Setter for property: (bool) EstimatedHigh
         Returns the property represents  EstimatedHigh.  
             
         
        """
        pass
    @property
    def EstimatedLow(self) -> bool:
        """
        Getter for property: (bool) EstimatedLow
         Returns the property represents  EstimatedLow.  
             
         
        """
        pass
    @EstimatedLow.setter
    def EstimatedLow(self, estimatedLow: bool):
        """
        Setter for property: (bool) EstimatedLow
         Returns the property represents  EstimatedLow.  
             
         
        """
        pass
    @property
    def EstimatedPercentAboveUpperSpec(self) -> bool:
        """
        Getter for property: (bool) EstimatedPercentAboveUpperSpec
         Returns the property represents  EstimatedPercentAboveUpperSpec.  
             
         
        """
        pass
    @EstimatedPercentAboveUpperSpec.setter
    def EstimatedPercentAboveUpperSpec(self, estimatedPercentAboveUpperSpec: bool):
        """
        Setter for property: (bool) EstimatedPercentAboveUpperSpec
         Returns the property represents  EstimatedPercentAboveUpperSpec.  
             
         
        """
        pass
    @property
    def EstimatedPercentBelowLowerSpec(self) -> bool:
        """
        Getter for property: (bool) EstimatedPercentBelowLowerSpec
         Returns the property represents  EstimatedPercentBelowLowerSpec.  
             
         
        """
        pass
    @EstimatedPercentBelowLowerSpec.setter
    def EstimatedPercentBelowLowerSpec(self, estimatedPercentBelowLowerSpec: bool):
        """
        Setter for property: (bool) EstimatedPercentBelowLowerSpec
         Returns the property represents  EstimatedPercentBelowLowerSpec.  
             
         
        """
        pass
    @property
    def EstimatedPercentOutOfSpec(self) -> bool:
        """
        Getter for property: (bool) EstimatedPercentOutOfSpec
         Returns the property represents  EstimatedPercentOutOfSpec.  
             
         
        """
        pass
    @EstimatedPercentOutOfSpec.setter
    def EstimatedPercentOutOfSpec(self, estimatedPercentOutOfSpec: bool):
        """
        Setter for property: (bool) EstimatedPercentOutOfSpec
         Returns the property represents  EstimatedPercentOutOfSpec.  
             
         
        """
        pass
    @property
    def EstimatedRange(self) -> bool:
        """
        Getter for property: (bool) EstimatedRange
         Returns the property represents  EstimatedRange.  
             
         
        """
        pass
    @EstimatedRange.setter
    def EstimatedRange(self, estimatedRange: bool):
        """
        Setter for property: (bool) EstimatedRange
         Returns the property represents  EstimatedRange.  
             
         
        """
        pass
    @property
    def HLMSimulation(self) -> bool:
        """
        Getter for property: (bool) HLMSimulation
         Returns the property represents  HLM Simulation flag.  
             
         
        """
        pass
    @HLMSimulation.setter
    def HLMSimulation(self, hlmSimulation: bool):
        """
        Setter for property: (bool) HLMSimulation
         Returns the property represents  HLM Simulation flag.  
             
         
        """
        pass
    @property
    def InheritFaceNames(self) -> bool:
        """
        Getter for property: (bool) InheritFaceNames
         Returns the property represents InheritFaceNames.  
             
         
        """
        pass
    @InheritFaceNames.setter
    def InheritFaceNames(self, inheritFaceNames: bool):
        """
        Setter for property: (bool) InheritFaceNames
         Returns the property represents InheritFaceNames.  
             
         
        """
        pass
    @property
    def MaxAngleTangency(self) -> int:
        """
        Getter for property: (int) MaxAngleTangency
         Returns the property represents  Max Angle Tangency.  
             
         
        """
        pass
    @MaxAngleTangency.setter
    def MaxAngleTangency(self, maxAngleTangency: int):
        """
        Setter for property: (int) MaxAngleTangency
         Returns the property represents  Max Angle Tangency.  
             
         
        """
        pass
    @property
    def MaxOffsetMating(self) -> float:
        """
        Getter for property: (float) MaxOffsetMating
         Returns the property represents  Max Offset for Mating.  
             
         
        """
        pass
    @MaxOffsetMating.setter
    def MaxOffsetMating(self, maxOffsetMating: float):
        """
        Setter for property: (float) MaxOffsetMating
         Returns the property represents  Max Offset for Mating.  
             
         
        """
        pass
    @property
    def Mean(self) -> bool:
        """
        Getter for property: (bool) Mean
         Returns the property represents  Mean.  
             
         
        """
        pass
    @Mean.setter
    def Mean(self, nominal: bool):
        """
        Setter for property: (bool) Mean
         Returns the property represents  Mean.  
             
         
        """
        pass
    @property
    def NoOfMontecarlo(self) -> int:
        """
        Getter for property: (int) NoOfMontecarlo
         Returns the property represents  No Of Montecarlo.  
             
         
        """
        pass
    @NoOfMontecarlo.setter
    def NoOfMontecarlo(self, noOfMontecarlo: int):
        """
        Setter for property: (int) NoOfMontecarlo
         Returns the property represents  No Of Montecarlo.  
             
         
        """
        pass
    @property
    def Nominal(self) -> bool:
        """
        Getter for property: (bool) Nominal
         Returns the property represents  Nominal.  
             
         
        """
        pass
    @Nominal.setter
    def Nominal(self, nominal: bool):
        """
        Setter for property: (bool) Nominal
         Returns the property represents  Nominal.  
             
         
        """
        pass
    @property
    def RunExtremeSimulation(self) -> bool:
        """
        Getter for property: (bool) RunExtremeSimulation
         Returns the property represents runExtremeSimulation.  
             
         
        """
        pass
    @RunExtremeSimulation.setter
    def RunExtremeSimulation(self, runExtremeSimulation: bool):
        """
        Setter for property: (bool) RunExtremeSimulation
         Returns the property represents runExtremeSimulation.  
             
         
        """
        pass
    @property
    def SampleHigh(self) -> bool:
        """
        Getter for property: (bool) SampleHigh
         Returns the property represents  SampleHigh.  
             
         
        """
        pass
    @SampleHigh.setter
    def SampleHigh(self, sampleHigh: bool):
        """
        Setter for property: (bool) SampleHigh
         Returns the property represents  SampleHigh.  
             
         
        """
        pass
    @property
    def SampleLow(self) -> bool:
        """
        Getter for property: (bool) SampleLow
         Returns the property represents  SampleLow.  
             
         
        """
        pass
    @SampleLow.setter
    def SampleLow(self, sampleLow: bool):
        """
        Setter for property: (bool) SampleLow
         Returns the property represents  SampleLow.  
             
         
        """
        pass
    @property
    def SampleRange(self) -> bool:
        """
        Getter for property: (bool) SampleRange
         Returns the property represents  SampleRange.  
             
         
        """
        pass
    @SampleRange.setter
    def SampleRange(self, sampleRange: bool):
        """
        Setter for property: (bool) SampleRange
         Returns the property represents  SampleRange.  
             
         
        """
        pass
    @property
    def SigmaRange(self) -> int:
        """
        Getter for property: (int) SigmaRange
         Returns the property represents  Sigma Range.  
             
         
        """
        pass
    @SigmaRange.setter
    def SigmaRange(self, sigmaRange: int):
        """
        Setter for property: (int) SigmaRange
         Returns the property represents  Sigma Range.  
             
         
        """
        pass
    @property
    def StandardDeviation(self) -> bool:
        """
        Getter for property: (bool) StandardDeviation
         Returns the property represents  StandardDeviation.  
             
         
        """
        pass
    @StandardDeviation.setter
    def StandardDeviation(self, standardDeviation: bool):
        """
        Setter for property: (bool) StandardDeviation
         Returns the property represents  StandardDeviation.  
             
         
        """
        pass
    @property
    def TolSigmaRange(self) -> int:
        """
        Getter for property: (int) TolSigmaRange
         Returns the property represents  TolSigmaRange.  
             
         
        """
        pass
    @TolSigmaRange.setter
    def TolSigmaRange(self, tolSigmaRange: int):
        """
        Setter for property: (int) TolSigmaRange
         Returns the property represents  TolSigmaRange.  
             
         
        """
        pass
    @property
    def UseVariationTails(self) -> bool:
        """
        Getter for property: (bool) UseVariationTails
         Returns the property represents UseVariationTails.  
             
         
        """
        pass
    @UseVariationTails.setter
    def UseVariationTails(self, useVariationTails: bool):
        """
        Setter for property: (bool) UseVariationTails
         Returns the property represents UseVariationTails.  
             
         
        """
        pass
import NXOpen
class SlotFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> SlotFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> SlotFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> SlotFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
         Returns the property represents  X value of anchor.  
             
         
        """
        pass
    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
         Returns the property represents  X value of anchor.  
             
         
        """
        pass
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
         Returns the property represents  Y value of anchor.  
             
         
        """
        pass
    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
         Returns the property represents  Y value of anchor.  
             
         
        """
        pass
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
         Returns the property represents  Z value of anchor.  
             
         
        """
        pass
    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
         Returns the property represents  Z value of anchor.  
             
         
        """
        pass
    @property
    def DoubleDepth(self) -> float:
        """
        Getter for property: (float) DoubleDepth
         Returns the property represents  depth of slot.  
             
         
        """
        pass
    @DoubleDepth.setter
    def DoubleDepth(self, height: float):
        """
        Setter for property: (float) DoubleDepth
         Returns the property represents  depth of slot.  
             
         
        """
        pass
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
         Returns the property represents  X value of normal.  
             
         
        """
        pass
    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
         Returns the property represents  X value of normal.  
             
         
        """
        pass
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
         Returns the property represents  Y value of normal.  
             
         
        """
        pass
    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
         Returns the property represents  Y value of normal.  
             
         
        """
        pass
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
         Returns the property represents  Z value of normal.  
             
         
        """
        pass
    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
         Returns the property represents  Z value of normal.  
             
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the property represents  Form distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the property represents  Form distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the property represents  Loc distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the property represents  Loc distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the property represents  Size distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the property represents  Size distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleLength(self) -> float:
        """
        Getter for property: (float) DoubleLength
         Returns the property represents  length of slot.  
             
         
        """
        pass
    @DoubleLength.setter
    def DoubleLength(self, distance: float):
        """
        Setter for property: (float) DoubleLength
         Returns the property represents  length of slot.  
             
         
        """
        pass
    @property
    def DoubleLengthVectorI(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorI
         Returns the property represents  X value of length vector.  
             
         
        """
        pass
    @DoubleLengthVectorI.setter
    def DoubleLengthVectorI(self, doubleLengthVectorI: float):
        """
        Setter for property: (float) DoubleLengthVectorI
         Returns the property represents  X value of length vector.  
             
         
        """
        pass
    @property
    def DoubleLengthVectorJ(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorJ
         Returns the property represents  Y value of length vector.  
             
         
        """
        pass
    @DoubleLengthVectorJ.setter
    def DoubleLengthVectorJ(self, doubleLengthVectorJ: float):
        """
        Setter for property: (float) DoubleLengthVectorJ
         Returns the property represents  Y value of length vector.  
             
         
        """
        pass
    @property
    def DoubleLengthVectorK(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorK
         Returns the property represents  Z value of length vector.  
             
         
        """
        pass
    @DoubleLengthVectorK.setter
    def DoubleLengthVectorK(self, doubleLengthVectorK: float):
        """
        Setter for property: (float) DoubleLengthVectorK
         Returns the property represents  Z value of length vector.  
             
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the property represents  Form distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the property represents  Form distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the property represents  Loc distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the property represents  Loc distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the property represents  Size distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the property represents  Size distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleWidth(self) -> float:
        """
        Getter for property: (float) DoubleWidth
         Returns the property represents  width of slot.  
             
         
        """
        pass
    @DoubleWidth.setter
    def DoubleWidth(self, width: float):
        """
        Setter for property: (float) DoubleWidth
         Returns the property represents  width of slot.  
             
         
        """
        pass
    @property
    def EnumForm(self) -> SlotFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( SlotFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the property represents  Form distribution type.  
             
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: SlotFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( SlotFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the property represents  Form distribution type.  
             
         
        """
        pass
    @property
    def EnumLoc(self) -> SlotFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( SlotFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the property represents  Loc distribution type.  
             
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: SlotFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( SlotFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the property represents  Loc distribution type.  
             
         
        """
        pass
    @property
    def EnumSize(self) -> SlotFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( SlotFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the property represents  Size distribution type.  
             
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: SlotFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( SlotFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the property represents  Size distribution type.  
             
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the property represents  slot feature discription.  
             
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the property represents  slot feature discription.  
             
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the property represents  slot feature name.  
             
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the property represents  slot feature name.  
             
         
        """
        pass
    @property
    def ToggleSwap(self) -> bool:
        """
        Getter for property: (bool) ToggleSwap
         Returns the property represents  value of swap length and depth.  
             
         
        """
        pass
    @ToggleSwap.setter
    def ToggleSwap(self, boolSwap: bool):
        """
        Setter for property: (bool) ToggleSwap
         Returns the property represents  value of swap length and depth.  
             
         
        """
        pass
import NXOpen
class SlotFeature(NXOpen.NXObject): 
    """ Represents a Slot feature """
    pass
import NXOpen
class SocketFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> SocketFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> SocketFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> SocketFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
         Returns the double anchor x   
            
         
        """
        pass
    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
         Returns the double anchor x   
            
         
        """
        pass
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
         Returns the double anchor y   
            
         
        """
        pass
    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
         Returns the double anchor y   
            
         
        """
        pass
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
         Returns the double anchor z   
            
         
        """
        pass
    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
         Returns the double anchor z   
            
         
        """
        pass
    @property
    def DoubleDiameter(self) -> float:
        """
        Getter for property: (float) DoubleDiameter
         Returns the double diameter   
            
         
        """
        pass
    @DoubleDiameter.setter
    def DoubleDiameter(self, doubleDiameter: float):
        """
        Setter for property: (float) DoubleDiameter
         Returns the double diameter   
            
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def EnumForm(self) -> SocketFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( SocketFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: SocketFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( SocketFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @property
    def EnumLoc(self) -> SocketFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( SocketFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: SocketFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( SocketFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @property
    def EnumSize(self) -> SocketFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( SocketFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: SocketFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( SocketFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
import NXOpen
class SocketFeature(NXOpen.NXObject): 
    """ Represents a Socket feature """
    pass
import NXOpen
class TabFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TabFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TabFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TabFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
         Returns the property represents X value of anchor.  
             
         
        """
        pass
    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
         Returns the property represents X value of anchor.  
             
         
        """
        pass
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
         Returns the property represents Y value of anchor.  
             
         
        """
        pass
    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
         Returns the property represents Y value of anchor.  
             
         
        """
        pass
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
         Returns the property represents Z value of anchor.  
             
         
        """
        pass
    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
         Returns the property represents Z value of anchor.  
             
         
        """
        pass
    @property
    def DoubleDepth(self) -> float:
        """
        Getter for property: (float) DoubleDepth
         Returns the property represents depth of tab.  
             
         
        """
        pass
    @DoubleDepth.setter
    def DoubleDepth(self, height: float):
        """
        Setter for property: (float) DoubleDepth
         Returns the property represents depth of tab.  
             
         
        """
        pass
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
         Returns the property represents X value of normal.  
             
         
        """
        pass
    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
         Returns the property represents X value of normal.  
             
         
        """
        pass
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
         Returns the property represents Y value of normal.  
             
         
        """
        pass
    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
         Returns the property represents Y value of normal.  
             
         
        """
        pass
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
         Returns the property represents Z value of normal.  
             
         
        """
        pass
    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
         Returns the property represents Z value of normal.  
             
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the property represents Form distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the property represents Form distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the property represents Loc distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the property represents Loc distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the property represents Size distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the property represents Size distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleLength(self) -> float:
        """
        Getter for property: (float) DoubleLength
         Returns the property represents length of tab.  
             
         
        """
        pass
    @DoubleLength.setter
    def DoubleLength(self, distance: float):
        """
        Setter for property: (float) DoubleLength
         Returns the property represents length of tab.  
             
         
        """
        pass
    @property
    def DoubleLengthVectorI(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorI
         Returns the property represents X value of length vector.  
             
         
        """
        pass
    @DoubleLengthVectorI.setter
    def DoubleLengthVectorI(self, doubleLengthVectorI: float):
        """
        Setter for property: (float) DoubleLengthVectorI
         Returns the property represents X value of length vector.  
             
         
        """
        pass
    @property
    def DoubleLengthVectorJ(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorJ
         Returns the property represents Y value of length vector.  
             
         
        """
        pass
    @DoubleLengthVectorJ.setter
    def DoubleLengthVectorJ(self, doubleLengthVectorJ: float):
        """
        Setter for property: (float) DoubleLengthVectorJ
         Returns the property represents Y value of length vector.  
             
         
        """
        pass
    @property
    def DoubleLengthVectorK(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorK
         Returns the property represents Z value of length vector.  
             
         
        """
        pass
    @DoubleLengthVectorK.setter
    def DoubleLengthVectorK(self, doubleLengthVectorK: float):
        """
        Setter for property: (float) DoubleLengthVectorK
         Returns the property represents Z value of length vector.  
             
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the property represents Form distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the property represents Form distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the property represents Loc distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the property represents Loc distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the property represents Size distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the property represents Size distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleWidth(self) -> float:
        """
        Getter for property: (float) DoubleWidth
         Returns the property represents width of tab.  
             
         
        """
        pass
    @DoubleWidth.setter
    def DoubleWidth(self, height: float):
        """
        Setter for property: (float) DoubleWidth
         Returns the property represents width of tab.  
             
         
        """
        pass
    @property
    def EnumForm(self) -> TabFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( TabFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the property represents Form distribution type.  
             
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: TabFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( TabFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the property represents Form distribution type.  
             
         
        """
        pass
    @property
    def EnumLoc(self) -> TabFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( TabFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the property represents Loc distribution type.  
             
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TabFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( TabFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the property represents Loc distribution type.  
             
         
        """
        pass
    @property
    def EnumSize(self) -> TabFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( TabFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the property represents Size distribution type.  
             
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: TabFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( TabFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the property represents Size distribution type.  
             
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the property represents tab feature discription.  
             
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the property represents tab feature discription.  
             
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the property represents tab feature name.  
             
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the property represents tab feature name.  
             
         
        """
        pass
    @property
    def ToggleSwap(self) -> bool:
        """
        Getter for property: (bool) ToggleSwap
         Returns the property represents value of swap length and depth.  
             
         
        """
        pass
    @ToggleSwap.setter
    def ToggleSwap(self, boolSwap: bool):
        """
        Setter for property: (bool) ToggleSwap
         Returns the property represents value of swap length and depth.  
             
         
        """
        pass
import NXOpen
class TabFeature(NXOpen.NXObject): 
    """ Represents a Tab feature """
    pass
import NXOpen
class TaperedHoleFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedHoleFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedHoleFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedHoleFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
         Returns the double anchor x   
            
         
        """
        pass
    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
         Returns the double anchor x   
            
         
        """
        pass
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
         Returns the double anchor y   
            
         
        """
        pass
    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
         Returns the double anchor y   
            
         
        """
        pass
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
         Returns the double anchor z   
            
         
        """
        pass
    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
         Returns the double anchor z   
            
         
        """
        pass
    @property
    def DoubleDiameter1(self) -> float:
        """
        Getter for property: (float) DoubleDiameter1
         Returns the double diameter1   
            
         
        """
        pass
    @DoubleDiameter1.setter
    def DoubleDiameter1(self, doubleDiameter1: float):
        """
        Setter for property: (float) DoubleDiameter1
         Returns the double diameter1   
            
         
        """
        pass
    @property
    def DoubleDiameter2(self) -> float:
        """
        Getter for property: (float) DoubleDiameter2
         Returns the double diameter2   
            
         
        """
        pass
    @DoubleDiameter2.setter
    def DoubleDiameter2(self, doubleDiameter2: float):
        """
        Setter for property: (float) DoubleDiameter2
         Returns the double diameter2   
            
         
        """
        pass
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
         Returns the double direction i   
            
         
        """
        pass
    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
         Returns the double direction i   
            
         
        """
        pass
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
         Returns the double direction j   
            
         
        """
        pass
    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
         Returns the double direction j   
            
         
        """
        pass
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
         Returns the double direction k   
            
         
        """
        pass
    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
         Returns the double direction k   
            
         
        """
        pass
    @property
    def DoubleHeight(self) -> float:
        """
        Getter for property: (float) DoubleHeight
         Returns the double height   
            
         
        """
        pass
    @DoubleHeight.setter
    def DoubleHeight(self, doubleHeight: float):
        """
        Setter for property: (float) DoubleHeight
         Returns the double height   
            
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def EnumForm(self) -> TaperedHoleFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( TaperedHoleFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: TaperedHoleFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( TaperedHoleFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @property
    def EnumLoc(self) -> TaperedHoleFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( TaperedHoleFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TaperedHoleFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( TaperedHoleFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @property
    def EnumSize(self) -> TaperedHoleFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( TaperedHoleFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: TaperedHoleFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( TaperedHoleFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
import NXOpen
class TaperedHoleFeature(NXOpen.NXObject): 
    """ Represents a Tapered Hole feature """
    pass
import NXOpen
class TaperedHolePatternFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedHolePatternFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedHolePatternFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedHolePatternFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def EnumForm(self) -> TaperedHolePatternFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( TaperedHolePatternFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: TaperedHolePatternFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( TaperedHolePatternFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @property
    def EnumLoc(self) -> TaperedHolePatternFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( TaperedHolePatternFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TaperedHolePatternFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( TaperedHolePatternFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @property
    def EnumSize(self) -> TaperedHolePatternFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( TaperedHolePatternFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: TaperedHolePatternFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( TaperedHolePatternFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @property
    def NumInstanceCount(self) -> int:
        """
        Getter for property: (int) NumInstanceCount
         Returns the enum size   
            
         
        """
        pass
    @NumInstanceCount.setter
    def NumInstanceCount(self, numInstanceCount: int):
        """
        Setter for property: (int) NumInstanceCount
         Returns the enum size   
            
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
import NXOpen
class TaperedHolePatternFeature(NXOpen.NXObject): 
    """ Represents a Hole pattern feature """
    pass
import NXOpen
class TaperedPinFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedPinFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedPinFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedPinFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
         Returns the double anchor x   
            
         
        """
        pass
    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
         Returns the double anchor x   
            
         
        """
        pass
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
         Returns the double anchor y   
            
         
        """
        pass
    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
         Returns the double anchor y   
            
         
        """
        pass
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
         Returns the double anchor z   
            
         
        """
        pass
    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
         Returns the double anchor z   
            
         
        """
        pass
    @property
    def DoubleDiameter1(self) -> float:
        """
        Getter for property: (float) DoubleDiameter1
         Returns the double diameter1   
            
         
        """
        pass
    @DoubleDiameter1.setter
    def DoubleDiameter1(self, doubleDiameter1: float):
        """
        Setter for property: (float) DoubleDiameter1
         Returns the double diameter1   
            
         
        """
        pass
    @property
    def DoubleDiameter2(self) -> float:
        """
        Getter for property: (float) DoubleDiameter2
         Returns the double diameter2   
            
         
        """
        pass
    @DoubleDiameter2.setter
    def DoubleDiameter2(self, doubleDiameter2: float):
        """
        Setter for property: (float) DoubleDiameter2
         Returns the double diameter2   
            
         
        """
        pass
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
         Returns the double direction i   
            
         
        """
        pass
    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
         Returns the double direction i   
            
         
        """
        pass
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
         Returns the double direction j   
            
         
        """
        pass
    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
         Returns the double direction j   
            
         
        """
        pass
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
         Returns the double direction k   
            
         
        """
        pass
    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
         Returns the double direction k   
            
         
        """
        pass
    @property
    def DoubleHeight(self) -> float:
        """
        Getter for property: (float) DoubleHeight
         Returns the double height   
            
         
        """
        pass
    @DoubleHeight.setter
    def DoubleHeight(self, doubleHeight: float):
        """
        Setter for property: (float) DoubleHeight
         Returns the double height   
            
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def EnumForm(self) -> TaperedPinFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( TaperedPinFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: TaperedPinFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( TaperedPinFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @property
    def EnumLoc(self) -> TaperedPinFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( TaperedPinFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TaperedPinFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( TaperedPinFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @property
    def EnumSize(self) -> TaperedPinFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( TaperedPinFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: TaperedPinFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( TaperedPinFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
import NXOpen
class TaperedPinFeature(NXOpen.NXObject): 
    """ Represents a Tapered Pin feature """
    pass
import NXOpen
class TaperedPinPatternFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedPinPatternFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedPinPatternFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedPinPatternFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the double kurtosis form   
            
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the double kurtosis loc   
            
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the double kurtosis size   
            
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the double skewness form   
            
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the double skewness loc   
            
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the double skewness size   
            
         
        """
        pass
    @property
    def EnumForm(self) -> TaperedPinPatternFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( TaperedPinPatternFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: TaperedPinPatternFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( TaperedPinPatternFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the enum form   
            
         
        """
        pass
    @property
    def EnumLoc(self) -> TaperedPinPatternFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( TaperedPinPatternFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TaperedPinPatternFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( TaperedPinPatternFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the enum loc   
            
         
        """
        pass
    @property
    def EnumSize(self) -> TaperedPinPatternFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( TaperedPinPatternFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: TaperedPinPatternFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( TaperedPinPatternFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the enum size   
            
         
        """
        pass
    @property
    def NumInstanceCount(self) -> int:
        """
        Getter for property: (int) NumInstanceCount
         Returns the enum size   
            
         
        """
        pass
    @NumInstanceCount.setter
    def NumInstanceCount(self, numInstanceCount: int):
        """
        Setter for property: (int) NumInstanceCount
         Returns the enum size   
            
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the string description   
            
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the string name   
            
         
        """
        pass
import NXOpen
class TaperedPinPatternFeature(NXOpen.NXObject): 
    """ Represents a Pin pattern feature """
    pass
import NXOpen
class TaperedSlotFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedSlotFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedSlotFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedSlotFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
         Returns the property represents  X value of anchor.  
             
         
        """
        pass
    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
         Returns the property represents  X value of anchor.  
             
         
        """
        pass
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
         Returns the property represents  Y value of anchor.  
             
         
        """
        pass
    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
         Returns the property represents  Y value of anchor.  
             
         
        """
        pass
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
         Returns the property represents  Z value of anchor.  
             
         
        """
        pass
    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
         Returns the property represents  Z value of anchor.  
             
         
        """
        pass
    @property
    def DoubleAngle(self) -> float:
        """
        Getter for property: (float) DoubleAngle
         Returns the property represents  Angle of slot.  
             
         
        """
        pass
    @DoubleAngle.setter
    def DoubleAngle(self, angle: float):
        """
        Setter for property: (float) DoubleAngle
         Returns the property represents  Angle of slot.  
             
         
        """
        pass
    @property
    def DoubleDepth(self) -> float:
        """
        Getter for property: (float) DoubleDepth
         Returns the property represents  depth of slot.  
             
         
        """
        pass
    @DoubleDepth.setter
    def DoubleDepth(self, height: float):
        """
        Setter for property: (float) DoubleDepth
         Returns the property represents  depth of slot.  
             
         
        """
        pass
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
         Returns the property represents  X value of normal.  
             
         
        """
        pass
    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
         Returns the property represents  X value of normal.  
             
         
        """
        pass
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
         Returns the property represents  Y value of normal.  
             
         
        """
        pass
    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
         Returns the property represents  Y value of normal.  
             
         
        """
        pass
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
         Returns the property represents  Z value of normal.  
             
         
        """
        pass
    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
         Returns the property represents  Z value of normal.  
             
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the property represents  Form distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the property represents  Form distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the property represents  Loc distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the property represents  Loc distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the property represents  Size distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the property represents  Size distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleLength(self) -> float:
        """
        Getter for property: (float) DoubleLength
         Returns the property represents  length of slot.  
             
         
        """
        pass
    @DoubleLength.setter
    def DoubleLength(self, distance: float):
        """
        Setter for property: (float) DoubleLength
         Returns the property represents  length of slot.  
             
         
        """
        pass
    @property
    def DoubleLengthVectorI(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorI
         Returns the property represents  X value of length vector.  
             
         
        """
        pass
    @DoubleLengthVectorI.setter
    def DoubleLengthVectorI(self, doubleLengthVectorI: float):
        """
        Setter for property: (float) DoubleLengthVectorI
         Returns the property represents  X value of length vector.  
             
         
        """
        pass
    @property
    def DoubleLengthVectorJ(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorJ
         Returns the property represents  Y value of length vector.  
             
         
        """
        pass
    @DoubleLengthVectorJ.setter
    def DoubleLengthVectorJ(self, doubleLengthVectorJ: float):
        """
        Setter for property: (float) DoubleLengthVectorJ
         Returns the property represents  Y value of length vector.  
             
         
        """
        pass
    @property
    def DoubleLengthVectorK(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorK
         Returns the property represents  Z value of length vector.  
             
         
        """
        pass
    @DoubleLengthVectorK.setter
    def DoubleLengthVectorK(self, doubleLengthVectorK: float):
        """
        Setter for property: (float) DoubleLengthVectorK
         Returns the property represents  Z value of length vector.  
             
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the property represents  Form distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the property represents  Form distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the property represents  Loc distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the property represents  Loc distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the property represents  Size distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the property represents  Size distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleWidth(self) -> float:
        """
        Getter for property: (float) DoubleWidth
         Returns the property represents  width of slot.  
             
         
        """
        pass
    @DoubleWidth.setter
    def DoubleWidth(self, width: float):
        """
        Setter for property: (float) DoubleWidth
         Returns the property represents  width of slot.  
             
         
        """
        pass
    @property
    def DoubleWidth2(self) -> float:
        """
        Getter for property: (float) DoubleWidth2
         Returns the property represents  width2 of slot.  
             
         
        """
        pass
    @DoubleWidth2.setter
    def DoubleWidth2(self, width2: float):
        """
        Setter for property: (float) DoubleWidth2
         Returns the property represents  width2 of slot.  
             
         
        """
        pass
    @property
    def EnumForm(self) -> TaperedSlotFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( TaperedSlotFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the property represents  Form distribution type.  
             
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: TaperedSlotFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( TaperedSlotFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the property represents  Form distribution type.  
             
         
        """
        pass
    @property
    def EnumLoc(self) -> TaperedSlotFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( TaperedSlotFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the property represents  Loc distribution type.  
             
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TaperedSlotFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( TaperedSlotFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the property represents  Loc distribution type.  
             
         
        """
        pass
    @property
    def EnumSize(self) -> TaperedSlotFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( TaperedSlotFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the property represents  Size distribution type.  
             
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: TaperedSlotFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( TaperedSlotFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the property represents  Size distribution type.  
             
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the property represents  slot feature discription.  
             
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the property represents  slot feature discription.  
             
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the property represents  slot feature name.  
             
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the property represents  slot feature name.  
             
         
        """
        pass
import NXOpen
class TaperedSlotFeature(NXOpen.NXObject): 
    """ Represents a Slot feature """
    pass
import NXOpen
class TaperedTabFeatureBuilder(NXOpen.Builder): 
    """
    
    """
    class APIEnumForm(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedTabFeatureBuilder.APIEnumForm:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumLoc(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedTabFeatureBuilder.APIEnumLoc:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class APIEnumSize(Enum):
        """
        Members Include: 
         |Normal| 
         |Uniform| 
         |Extreme| 
         |Pearson| 
         |Trapeziodal| 

        """
        Normal: int
        Uniform: int
        Extreme: int
        Pearson: int
        Trapeziodal: int
        @staticmethod
        def ValueOf(value: int) -> TaperedTabFeatureBuilder.APIEnumSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DoubleAnchorX(self) -> float:
        """
        Getter for property: (float) DoubleAnchorX
         Returns the property represents  X value of anchor.  
             
         
        """
        pass
    @DoubleAnchorX.setter
    def DoubleAnchorX(self, doubleAnchorX: float):
        """
        Setter for property: (float) DoubleAnchorX
         Returns the property represents  X value of anchor.  
             
         
        """
        pass
    @property
    def DoubleAnchorY(self) -> float:
        """
        Getter for property: (float) DoubleAnchorY
         Returns the property represents  Y value of anchor.  
             
         
        """
        pass
    @DoubleAnchorY.setter
    def DoubleAnchorY(self, doubleAnchorY: float):
        """
        Setter for property: (float) DoubleAnchorY
         Returns the property represents  Y value of anchor.  
             
         
        """
        pass
    @property
    def DoubleAnchorZ(self) -> float:
        """
        Getter for property: (float) DoubleAnchorZ
         Returns the property represents  Z value of anchor.  
             
         
        """
        pass
    @DoubleAnchorZ.setter
    def DoubleAnchorZ(self, doubleAnchorZ: float):
        """
        Setter for property: (float) DoubleAnchorZ
         Returns the property represents  Z value of anchor.  
             
         
        """
        pass
    @property
    def DoubleAngle(self) -> float:
        """
        Getter for property: (float) DoubleAngle
         Returns the property represents  Angle of tab.  
             
         
        """
        pass
    @DoubleAngle.setter
    def DoubleAngle(self, angle: float):
        """
        Setter for property: (float) DoubleAngle
         Returns the property represents  Angle of tab.  
             
         
        """
        pass
    @property
    def DoubleDepth(self) -> float:
        """
        Getter for property: (float) DoubleDepth
         Returns the property represents  depth of tab.  
             
         
        """
        pass
    @DoubleDepth.setter
    def DoubleDepth(self, height: float):
        """
        Setter for property: (float) DoubleDepth
         Returns the property represents  depth of tab.  
             
         
        """
        pass
    @property
    def DoubleDirectionI(self) -> float:
        """
        Getter for property: (float) DoubleDirectionI
         Returns the property represents  X value of normal.  
             
         
        """
        pass
    @DoubleDirectionI.setter
    def DoubleDirectionI(self, doubleDirectionI: float):
        """
        Setter for property: (float) DoubleDirectionI
         Returns the property represents  X value of normal.  
             
         
        """
        pass
    @property
    def DoubleDirectionJ(self) -> float:
        """
        Getter for property: (float) DoubleDirectionJ
         Returns the property represents  Y value of normal.  
             
         
        """
        pass
    @DoubleDirectionJ.setter
    def DoubleDirectionJ(self, doubleDirectionJ: float):
        """
        Setter for property: (float) DoubleDirectionJ
         Returns the property represents  Y value of normal.  
             
         
        """
        pass
    @property
    def DoubleDirectionK(self) -> float:
        """
        Getter for property: (float) DoubleDirectionK
         Returns the property represents  Z value of normal.  
             
         
        """
        pass
    @DoubleDirectionK.setter
    def DoubleDirectionK(self, doubleDirectionK: float):
        """
        Setter for property: (float) DoubleDirectionK
         Returns the property represents  Z value of normal.  
             
         
        """
        pass
    @property
    def DoubleKurtosisForm(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisForm
         Returns the property represents  Form distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisForm.setter
    def DoubleKurtosisForm(self, doubleKurtosisForm: float):
        """
        Setter for property: (float) DoubleKurtosisForm
         Returns the property represents  Form distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleKurtosisLoc(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisLoc
         Returns the property represents  Loc distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisLoc.setter
    def DoubleKurtosisLoc(self, doubleKurtosisLoc: float):
        """
        Setter for property: (float) DoubleKurtosisLoc
         Returns the property represents  Loc distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleKurtosisSize(self) -> float:
        """
        Getter for property: (float) DoubleKurtosisSize
         Returns the property represents  Size distribution Kurtosis.  
             
         
        """
        pass
    @DoubleKurtosisSize.setter
    def DoubleKurtosisSize(self, doubleKurtosisSize: float):
        """
        Setter for property: (float) DoubleKurtosisSize
         Returns the property represents  Size distribution Kurtosis.  
             
         
        """
        pass
    @property
    def DoubleLength(self) -> float:
        """
        Getter for property: (float) DoubleLength
         Returns the property represents  length of tab.  
             
         
        """
        pass
    @DoubleLength.setter
    def DoubleLength(self, distance: float):
        """
        Setter for property: (float) DoubleLength
         Returns the property represents  length of tab.  
             
         
        """
        pass
    @property
    def DoubleLengthVectorI(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorI
         Returns the property represents  X value of length vector.  
             
         
        """
        pass
    @DoubleLengthVectorI.setter
    def DoubleLengthVectorI(self, doubleLengthVectorI: float):
        """
        Setter for property: (float) DoubleLengthVectorI
         Returns the property represents  X value of length vector.  
             
         
        """
        pass
    @property
    def DoubleLengthVectorJ(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorJ
         Returns the property represents  Y value of length vector.  
             
         
        """
        pass
    @DoubleLengthVectorJ.setter
    def DoubleLengthVectorJ(self, doubleLengthVectorJ: float):
        """
        Setter for property: (float) DoubleLengthVectorJ
         Returns the property represents  Y value of length vector.  
             
         
        """
        pass
    @property
    def DoubleLengthVectorK(self) -> float:
        """
        Getter for property: (float) DoubleLengthVectorK
         Returns the property represents  Z value of length vector.  
             
         
        """
        pass
    @DoubleLengthVectorK.setter
    def DoubleLengthVectorK(self, doubleLengthVectorK: float):
        """
        Setter for property: (float) DoubleLengthVectorK
         Returns the property represents  Z value of length vector.  
             
         
        """
        pass
    @property
    def DoubleSkewnessForm(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessForm
         Returns the property represents  Form distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessForm.setter
    def DoubleSkewnessForm(self, doubleSkewnessForm: float):
        """
        Setter for property: (float) DoubleSkewnessForm
         Returns the property represents  Form distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleSkewnessLoc(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessLoc
         Returns the property represents  Loc distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessLoc.setter
    def DoubleSkewnessLoc(self, doubleSkewnessLoc: float):
        """
        Setter for property: (float) DoubleSkewnessLoc
         Returns the property represents  Loc distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleSkewnessSize(self) -> float:
        """
        Getter for property: (float) DoubleSkewnessSize
         Returns the property represents  Size distribution Skewness.  
             
         
        """
        pass
    @DoubleSkewnessSize.setter
    def DoubleSkewnessSize(self, doubleSkewnessSize: float):
        """
        Setter for property: (float) DoubleSkewnessSize
         Returns the property represents  Size distribution Skewness.  
             
         
        """
        pass
    @property
    def DoubleWidth(self) -> float:
        """
        Getter for property: (float) DoubleWidth
         Returns the property represents  width of tab.  
             
         
        """
        pass
    @DoubleWidth.setter
    def DoubleWidth(self, width: float):
        """
        Setter for property: (float) DoubleWidth
         Returns the property represents  width of tab.  
             
         
        """
        pass
    @property
    def DoubleWidth2(self) -> float:
        """
        Getter for property: (float) DoubleWidth2
         Returns the property represents  width2 of tab.  
             
         
        """
        pass
    @DoubleWidth2.setter
    def DoubleWidth2(self, width2: float):
        """
        Setter for property: (float) DoubleWidth2
         Returns the property represents  width2 of tab.  
             
         
        """
        pass
    @property
    def EnumForm(self) -> TaperedTabFeatureBuilder.APIEnumForm:
        """
        Getter for property: ( TaperedTabFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the property represents  Form distribution type.  
             
         
        """
        pass
    @EnumForm.setter
    def EnumForm(self, enumForm: TaperedTabFeatureBuilder.APIEnumForm):
        """
        Setter for property: ( TaperedTabFeatureBuilder.APIEnumForm NXOp) EnumForm
         Returns the property represents  Form distribution type.  
             
         
        """
        pass
    @property
    def EnumLoc(self) -> TaperedTabFeatureBuilder.APIEnumLoc:
        """
        Getter for property: ( TaperedTabFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the property represents  Loc distribution type.  
             
         
        """
        pass
    @EnumLoc.setter
    def EnumLoc(self, enumLoc: TaperedTabFeatureBuilder.APIEnumLoc):
        """
        Setter for property: ( TaperedTabFeatureBuilder.APIEnumLoc NXOp) EnumLoc
         Returns the property represents  Loc distribution type.  
             
         
        """
        pass
    @property
    def EnumSize(self) -> TaperedTabFeatureBuilder.APIEnumSize:
        """
        Getter for property: ( TaperedTabFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the property represents  Size distribution type.  
             
         
        """
        pass
    @EnumSize.setter
    def EnumSize(self, enumSize: TaperedTabFeatureBuilder.APIEnumSize):
        """
        Setter for property: ( TaperedTabFeatureBuilder.APIEnumSize NXOp) EnumSize
         Returns the property represents  Size distribution type.  
             
         
        """
        pass
    @property
    def StringDescription(self) -> str:
        """
        Getter for property: (str) StringDescription
         Returns the property represents  tab feature discription.  
             
         
        """
        pass
    @StringDescription.setter
    def StringDescription(self, stringDescription: str):
        """
        Setter for property: (str) StringDescription
         Returns the property represents  tab feature discription.  
             
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the property represents  tab feature name.  
             
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the property represents  tab feature name.  
             
         
        """
        pass
import NXOpen
class TaperedTabFeature(NXOpen.NXObject): 
    """ Represents a Tab feature """
    pass
import NXOpen
class Utils(NXOpen.Object): 
    """
    
    """
    def AddFixtureNode(assemblyTag: NXOpen.NXObject) -> None:
        """
         The routine creates a point. 
        """
        pass
    def CreateModel(rootObject: NXOpen.NXObject) -> None:
        """
         The routine creates vsa model. 
        """
        pass
    def CreatePoint() -> NXOpen.NXObject:
        """
         The routine creates a point. 
         Returns pointTag ( NXOpen.NXObject): .
        """
        pass
    def CreateindivisualpointOnFace(ptrParentFeat: NXOpen.NXObject) -> None:
        """
         The routine creates points on plane. 
        """
        pass
    def DeleteAllNodes() -> None:
        """
         The routine deletes all the nodes. 
        """
        pass
    def DeleteAssemblyOperation(assemblyOperation: NXOpen.NXObject) -> None:
        """
         The routine Deletes Assembly Operation. 
        """
        pass
    def DeleteFeature(vsaFeature: NXOpen.NXObject) -> None:
        """
         The routine Deletes Feature. 
        """
        pass
    def DeleteFixture(vsaFixtureTag: NXOpen.NXObject) -> None:
        """
         The routine Deletes Fixture.
        """
        pass
    def DeleteGDTMeasurementOperation(gdtmeasurementOperation: NXOpen.NXObject) -> None:
        """
         The routine Deletes GDTMeasurement Operation. 
        """
        pass
    def DeleteMeasurementOperation(measurementOperation: NXOpen.NXObject) -> None:
        """
         The routine Deletes Measurement Operation. 
        """
        pass
    def DeleteSubFeaturePoint(subFeaturePointTag: NXOpen.NXObject) -> None:
        """
         The routine Deletes SubFeature Point. 
        """
        pass
    def DeleteTolerance(vsaFeature: NXOpen.NXObject) -> None:
        """
         The routine Deletes Tolerance. 
        """
        pass
    def EditindivisualpointOnFace(tagPointSubFeat: NXOpen.NXObject) -> None:
        """
         The routine edit points on plane. 
        """
        pass
    def MoveAssemblyChildren(vsaPartTag: NXOpen.NXObject, sourceIndex: int, targetIndex: int) -> None:
        """
         The routine moves Assembly children. 
        """
        pass
    def MoveFixtureChildren(vsaFixtureTag: NXOpen.NXObject, sourceIndex: int, targetIndex: int) -> None:
        """
         The routine moves the fixture element at sourceIndex to targetIndex.
                If sourceIndex is 4 and the targetIndex is 1, the fixture at index 4 will be moved to index number 1.
        """
        pass
    def MovePartChildren(vsaPartTag: NXOpen.NXObject, sourceIndex: int, targetIndex: int) -> None:
        """
         The routine moves part children. 
        """
        pass
    def MoveRootProcessChildren(vsaRootProcessTag: NXOpen.NXObject, sourceIndex: int, targetIndex: int) -> None:
        """
         The routine moves root process children. 
        """
        pass
    def PopulateModelToNavigator() -> None:
        """
         The routine populates vsa model in navigator. 
        """
        pass
    def RefreshAllNavigatorViews() -> None:
        """
         The routine refreshes nevigator. 
        """
        pass
    def RenameAssemblyOperation(subFeaturePointTag: NXOpen.NXObject, pstrName: str) -> None:
        """
         The routine renames Assembly Operation. 
        """
        pass
    def RenameFeature(subFeaturePointTag: NXOpen.NXObject, pstrName: str) -> None:
        """
         The routine renames Feature. 
        """
        pass
    def RenameFixture(vsaFixture: NXOpen.NXObject, pstrName: str) -> None:
        """
         The routine supressesunpresses GDT Measurement Operation. 
        """
        pass
    def RenameMeasurementOperation(subFeaturePointTag: NXOpen.NXObject, pstrName: str) -> None:
        """
         The routine renames Measurement Operation. 
        """
        pass
    def RenameSubFeaturePoint(subFeaturePointTag: NXOpen.NXObject, pstrName: str) -> None:
        """
         The routine Rename SubFeature Point. 
        """
        pass
    def SimulateModel(rootObject: NXOpen.NXObject) -> None:
        """
         The routine validates vsa model. 
        """
        pass
    def SupressUnsupressAssemblyOperation(assemblyOperation: NXOpen.NXObject) -> None:
        """
         The routine supressesunpresses Assembly Operation. 
        """
        pass
    def SupressUnsupressGDTMeasurementOperation(gdtMeasurementOperation: NXOpen.NXObject) -> None:
        """
         The routine supressesunpresses GDT Measurement Operation. 
        """
        pass
    def SupressUnsupressMeasurementOperation(measurementOperation: NXOpen.NXObject) -> None:
        """
         The routine supressesunpresses Measurement Operation. 
        """
        pass
    def UpdatePmi() -> None:
        """
         Apply alternative values to PMIs. 
        """
        pass
    def ValidateModel(rootObject: NXOpen.NXObject) -> None:
        """
         The routine validates vsa model. 
        """
        pass
import NXOpen
class VsaExportResultBuilder(NXOpen.Builder): 
    """
    
    """
    @property
    def ContributionMatix(self) -> bool:
        """
        Getter for property: (bool) ContributionMatix
         Returns the property represents Contribution Matix.  
             
         
        """
        pass
    @ContributionMatix.setter
    def ContributionMatix(self, boolSwap: bool):
        """
        Setter for property: (bool) ContributionMatix
         Returns the property represents Contribution Matix.  
             
         
        """
        pass
    @property
    def FolderPath(self) -> str:
        """
        Getter for property: (str) FolderPath
         Returns the property represents Folder Path   
            
         
        """
        pass
    @FolderPath.setter
    def FolderPath(self, name: str):
        """
        Setter for property: (str) FolderPath
         Returns the property represents Folder Path   
            
         
        """
        pass
    @property
    def MeasurementValues(self) -> bool:
        """
        Getter for property: (bool) MeasurementValues
         Returns the property represents Measurement Values.  
             
         
        """
        pass
    @MeasurementValues.setter
    def MeasurementValues(self, boolSwap: bool):
        """
        Setter for property: (bool) MeasurementValues
         Returns the property represents Measurement Values.  
             
         
        """
        pass
    @property
    def StatisticalParamenter(self) -> bool:
        """
        Getter for property: (bool) StatisticalParamenter
         Returns the property represents Folder Statistical Paramenter   
            
         
        """
        pass
    @StatisticalParamenter.setter
    def StatisticalParamenter(self, boolSwap: bool):
        """
        Setter for property: (bool) StatisticalParamenter
         Returns the property represents Folder Statistical Paramenter   
            
         
        """
        pass
    def PrintMeasurementStatistics(self, folderpath: str) -> None:
        """
         To print measurement statistics in report
        """
        pass
    def PrintMeasurementValues(self, folderpath: str) -> None:
        """
         To print measurement values in report
        """
        pass
    def PrintTotalToleranceContribution(self, folderpath: str) -> None:
        """
         To print Total tolerance cotribution in report
        """
        pass
import NXOpen
class VsaExportResult(NXOpen.NXObject): 
    """ Represents a Export Result """
    pass
