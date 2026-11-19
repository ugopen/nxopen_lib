from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class Adhesive(IConnection): 
    """  Adhesive connection. Use this interface to setget properties and parameters of the spot weld connection.  """
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromStart
         Returns the line Discretization distance from start   
            
         
        """
        pass
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceToEnd
         Returns the line Discretization distance to end   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height value   
            
         
        """
        pass
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LengthStep
         Returns the line Discretization length step   
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxAngleBetweenNormals
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDistCGToElemCG
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxLengthStep
         Returns the line Discretization max length step   
            
         
        """
        pass
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxNormalDistCGToFlanges
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProjectTolerance
         Returns the projection tolerance   
            
         
        """
        pass
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width value   
            
         
        """
        pass
import NXOpen
class Bar(IConnection): 
    """ Bar connection. Use this interface to setget properties and parameters of the Bar connection.  """
    @property
    def Coefficient(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Coefficient
         Returns the coefficient for formula defined diameter   
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the connection diameter   
            
         
        """
        pass
    @property
    def DiameterType(self) -> DiameterType:
        """
        Getter for property: ( DiameterType NXOpen.CAE) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: ( DiameterType NXOpen.CAE) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchConeAngle
         Returns the search cone angle   
            
         
        """
        pass
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchRange
         Returns the search range   
            
         
        """
        pass
    @property
    def TableFile(self) -> str:
        """
        Getter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
import NXOpen
class Bearing(IConnection): 
    """ Bearing connection. Use this interface to setget properties and parameters of the Bearing connection.  """
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchConeAngle
         Returns the search cone angle   
            
         
        """
        pass
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchRange
         Returns the search range   
            
         
        """
        pass
import NXOpen
class Bolt(IConnection): 
    """ Bolt connection. Use this interface to setget properties and parameters of the spot weld connection.  """
    @property
    def Coefficient(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Coefficient
         Returns the coefficient for formula defined diameter   
            
         
        """
        pass
    @property
    def DefineNutDiameter(self) -> bool:
        """
        Getter for property: (bool) DefineNutDiameter
         Returns the define nut diameter   
            
         
        """
        pass
    @DefineNutDiameter.setter
    def DefineNutDiameter(self, param: bool):
        """
        Setter for property: (bool) DefineNutDiameter
         Returns the define nut diameter   
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the connection diameter   
            
         
        """
        pass
    @property
    def DiameterType(self) -> DiameterType:
        """
        Getter for property: ( DiameterType NXOpen.CAE) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: ( DiameterType NXOpen.CAE) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    @property
    def HeadDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HeadDiameter
         Returns the head diameter    
            
         
        """
        pass
    @property
    def HeadDiameterCoefficient(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HeadDiameterCoefficient
         Returns the head diameter coefficient   
            
         
        """
        pass
    @property
    def HeadDiameterType(self) -> HeadDiameterType:
        """
        Getter for property: ( HeadDiameterType NXOpen.CAE) HeadDiameterType
         Returns the head diameter type   
            
         
        """
        pass
    @HeadDiameterType.setter
    def HeadDiameterType(self, param: HeadDiameterType):
        """
        Setter for property: ( HeadDiameterType NXOpen.CAE) HeadDiameterType
         Returns the head diameter type   
            
         
        """
        pass
    @property
    def LimitLocationEndpointsLength(self) -> bool:
        """
        Getter for property: (bool) LimitLocationEndpointsLength
         Returns the flag indicating to limit the bolt's length to the length between the location endpoints    
            
         
        """
        pass
    @LimitLocationEndpointsLength.setter
    def LimitLocationEndpointsLength(self, param: bool):
        """
        Setter for property: (bool) LimitLocationEndpointsLength
         Returns the flag indicating to limit the bolt's length to the length between the location endpoints    
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @property
    def MaxBoltLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxBoltLength
         Returns the maximum bolt length   
            
         
        """
        pass
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @property
    def NutDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NutDiameter
         Returns the nut diameter    
            
         
        """
        pass
    @property
    def NutDiameterCoefficient(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NutDiameterCoefficient
         Returns the nut diameter coefficient   
            
         
        """
        pass
    @property
    def NutDiameterType(self) -> NutDiameterType:
        """
        Getter for property: ( NutDiameterType NXOpen.CAE) NutDiameterType
         Returns the nut diameter type   
            
         
        """
        pass
    @NutDiameterType.setter
    def NutDiameterType(self, param: NutDiameterType):
        """
        Setter for property: ( NutDiameterType NXOpen.CAE) NutDiameterType
         Returns the nut diameter type   
            
         
        """
        pass
    @property
    def ShankLengthDiscretizationType(self) -> ShankLengthDiscretizationType:
        """
        Getter for property: ( ShankLengthDiscretizationType NXOpen.CAE) ShankLengthDiscretizationType
         Returns the shank length discretization type   
            
         
        """
        pass
    @ShankLengthDiscretizationType.setter
    def ShankLengthDiscretizationType(self, param: ShankLengthDiscretizationType):
        """
        Setter for property: ( ShankLengthDiscretizationType NXOpen.CAE) ShankLengthDiscretizationType
         Returns the shank length discretization type   
            
         
        """
        pass
    @property
    def ShankLengthPercentage(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ShankLengthPercentage
         Returns the shank length percentage   
            
         
        """
        pass
    @property
    def ShankLengthUser(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ShankLengthUser
         Returns the user specified shank length   
            
         
        """
        pass
    @property
    def TableFile(self) -> str:
        """
        Getter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    @property
    def UseMasterPointAsCenter(self) -> bool:
        """
        Getter for property: (bool) UseMasterPointAsCenter
         Returns the flag to use the master point as center   
            
         
        """
        pass
    @UseMasterPointAsCenter.setter
    def UseMasterPointAsCenter(self, param: bool):
        """
        Setter for property: (bool) UseMasterPointAsCenter
         Returns the flag to use the master point as center   
            
         
        """
        pass
class BushingType(Enum):
    """
    Members Include: 
     |Rectangular|  Rectangular bushing type 
     |Cylindrical|  Cylindrical bushing type 

    """
    Rectangular: int
    Cylindrical: int
    @staticmethod
    def ValueOf(value: int) -> BushingType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Fields
class Bushing(IConnection): 
    """ Bushing connection. Use this interface to setget properties and parameters of the Bushing connection.  """
    @property
    def BushingType(self) -> BushingType:
        """
        Getter for property: ( BushingType NXOpen.CAE) BushingType
         Returns the bushing type   
            
         
        """
        pass
    @BushingType.setter
    def BushingType(self, bushingType: BushingType):
        """
        Setter for property: ( BushingType NXOpen.CAE) BushingType
         Returns the bushing type   
            
         
        """
        pass
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @property
    def IsMassOnBothTargets(self) -> bool:
        """
        Getter for property: (bool) IsMassOnBothTargets
         Returns the isMassOnBothTargets   
            
         
        """
        pass
    @IsMassOnBothTargets.setter
    def IsMassOnBothTargets(self, isMassOnBothTargets: bool):
        """
        Setter for property: (bool) IsMassOnBothTargets
         Returns the isMassOnBothTargets   
            
         
        """
        pass
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Mass
         Returns the mass value   
            
         
        """
        pass
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @property
    def RCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RCylindricalStiffnessConstant
         Returns the R cylindrical stiffness constant   
            
         
        """
        pass
    @property
    def RCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RCylindricalStiffnessDynamic
         Returns the R cylindrical stiffness dynamic   
            
         
        """
        pass
    @RCylindricalStiffnessDynamic.setter
    def RCylindricalStiffnessDynamic(self, rDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RCylindricalStiffnessDynamic
         Returns the R cylindrical stiffness dynamic   
            
         
        """
        pass
    @property
    def RCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RCylindricalStructuralDampingConstant
         Returns the R cylindrical structural damping constant   
            
         
        """
        pass
    @property
    def RCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RCylindricalStructuralDampingDynamic
         Returns the R cylindrical structural damping dynamic   
            
         
        """
        pass
    @RCylindricalStructuralDampingDynamic.setter
    def RCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RCylindricalStructuralDampingDynamic
         Returns the R cylindrical structural damping dynamic   
            
         
        """
        pass
    @property
    def RCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RCylindricalViscousDampingConstant
         Returns the R cylindrical viscous damping constant   
            
         
        """
        pass
    @property
    def RCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RCylindricalViscousDampingDynamic
         Returns the R cylindrical viscous damping dynamic   
            
         
        """
        pass
    @RCylindricalViscousDampingDynamic.setter
    def RCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RCylindricalViscousDampingDynamic
         Returns the R cylindrical viscous damping dynamic   
            
         
        """
        pass
    @property
    def RNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RNonlinearCylindricalDamping
         Returns the R nonlinear cylindrical damping   
            
         
        """
        pass
    @RNonlinearCylindricalDamping.setter
    def RNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RNonlinearCylindricalDamping
         Returns the R nonlinear cylindrical damping   
            
         
        """
        pass
    @property
    def RNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RNonlinearCylindricalStiffness
         Returns the R nonlinear cylindrical stiffness   
            
         
        """
        pass
    @RNonlinearCylindricalStiffness.setter
    def RNonlinearCylindricalStiffness(self, rDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RNonlinearCylindricalStiffness
         Returns the R nonlinear cylindrical stiffness   
            
         
        """
        pass
    @property
    def RrCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RrCylindricalStiffnessConstant
         Returns the RR cylindrical stiffness constant   
            
         
        """
        pass
    @property
    def RrCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrCylindricalStiffnessDynamic
         Returns the RR cylindrical stiffness dynamic   
            
         
        """
        pass
    @RrCylindricalStiffnessDynamic.setter
    def RrCylindricalStiffnessDynamic(self, rrDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrCylindricalStiffnessDynamic
         Returns the RR cylindrical stiffness dynamic   
            
         
        """
        pass
    @property
    def RrCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RrCylindricalStructuralDampingConstant
         Returns the RR structural damping constant   
            
         
        """
        pass
    @property
    def RrCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrCylindricalStructuralDampingDynamic
         Returns the RR cylindrical structural damping dynamic   
            
         
        """
        pass
    @RrCylindricalStructuralDampingDynamic.setter
    def RrCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrCylindricalStructuralDampingDynamic
         Returns the RR cylindrical structural damping dynamic   
            
         
        """
        pass
    @property
    def RrCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RrCylindricalViscousDampingConstant
         Returns the RR cylindrical viscous damping constant   
            
         
        """
        pass
    @property
    def RrCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrCylindricalViscousDampingDynamic
         Returns the RR cylindrical viscous damping dynamic   
            
         
        """
        pass
    @RrCylindricalViscousDampingDynamic.setter
    def RrCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrCylindricalViscousDampingDynamic
         Returns the RR cylindrical viscous damping dynamic   
            
         
        """
        pass
    @property
    def RrNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrNonlinearCylindricalDamping
         Returns the RR nonlinear cylindrical damping   
            
         
        """
        pass
    @RrNonlinearCylindricalDamping.setter
    def RrNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrNonlinearCylindricalDamping
         Returns the RR nonlinear cylindrical damping   
            
         
        """
        pass
    @property
    def RrNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrNonlinearCylindricalStiffness
         Returns the RR nonlinear cylindrical stiffness   
            
         
        """
        pass
    @RrNonlinearCylindricalStiffness.setter
    def RrNonlinearCylindricalStiffness(self, rrDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrNonlinearCylindricalStiffness
         Returns the RR nonlinear cylindrical stiffness   
            
         
        """
        pass
    @property
    def RxNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxNonlinearDamping
         Returns the RX nonlinear damping   
            
         
        """
        pass
    @RxNonlinearDamping.setter
    def RxNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxNonlinearDamping
         Returns the RX nonlinear damping   
            
         
        """
        pass
    @property
    def RxNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxNonlinearStiffness
         Returns the RX nonlinear stiffness   
            
         
        """
        pass
    @RxNonlinearStiffness.setter
    def RxNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxNonlinearStiffness
         Returns the RX nonlinear stiffness   
            
         
        """
        pass
    @property
    def RxStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RxStiffnessConstant
         Returns the RX stiffness constant   
            
         
        """
        pass
    @property
    def RxStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxStiffnessDynamic
         Returns the RX stiffness dynamic   
            
         
        """
        pass
    @RxStiffnessDynamic.setter
    def RxStiffnessDynamic(self, rxDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxStiffnessDynamic
         Returns the RX stiffness dynamic   
            
         
        """
        pass
    @property
    def RxStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RxStructuralDampingConstant
         Returns the RX structural damping constant   
            
         
        """
        pass
    @property
    def RxStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxStructuralDampingDynamic
         Returns the RX structural damping dynamic   
            
         
        """
        pass
    @RxStructuralDampingDynamic.setter
    def RxStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxStructuralDampingDynamic
         Returns the RX structural damping dynamic   
            
         
        """
        pass
    @property
    def RxViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RxViscousDampingConstant
         Returns the RX viscous damping constant   
            
         
        """
        pass
    @property
    def RxViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxViscousDampingDynamic
         Returns the RX viscous damping dynamic   
            
         
        """
        pass
    @RxViscousDampingDynamic.setter
    def RxViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxViscousDampingDynamic
         Returns the RX viscous damping dynamic   
            
         
        """
        pass
    @property
    def RyNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyNonlinearDamping
         Returns the RY nonlinear damping   
            
         
        """
        pass
    @RyNonlinearDamping.setter
    def RyNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyNonlinearDamping
         Returns the RY nonlinear damping   
            
         
        """
        pass
    @property
    def RyNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyNonlinearStiffness
         Returns the RY nonlinear stiffness   
            
         
        """
        pass
    @RyNonlinearStiffness.setter
    def RyNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyNonlinearStiffness
         Returns the RY nonlinear stiffness   
            
         
        """
        pass
    @property
    def RyStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RyStiffnessConstant
         Returns the RY stiffness constant   
            
         
        """
        pass
    @property
    def RyStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyStiffnessDynamic
         Returns the RY stiffness dynamic   
            
         
        """
        pass
    @RyStiffnessDynamic.setter
    def RyStiffnessDynamic(self, ryDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyStiffnessDynamic
         Returns the RY stiffness dynamic   
            
         
        """
        pass
    @property
    def RyStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RyStructuralDampingConstant
         Returns the RY structural damping constant   
            
         
        """
        pass
    @property
    def RyStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyStructuralDampingDynamic
         Returns the RY structural damping dynamic   
            
         
        """
        pass
    @RyStructuralDampingDynamic.setter
    def RyStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyStructuralDampingDynamic
         Returns the RY structural damping dynamic   
            
         
        """
        pass
    @property
    def RyViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RyViscousDampingConstant
         Returns the RY viscous damping constant   
            
         
        """
        pass
    @property
    def RyViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyViscousDampingDynamic
         Returns the RY viscous damping dynamic   
            
         
        """
        pass
    @RyViscousDampingDynamic.setter
    def RyViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyViscousDampingDynamic
         Returns the RY viscous damping dynamic   
            
         
        """
        pass
    @property
    def RzCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzCylindricalStiffnessConstant
         Returns the RZ cylindrical stiffness constant   
            
         
        """
        pass
    @property
    def RzCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzCylindricalStiffnessDynamic
         Returns the RZ cylindrical stiffness dynamic   
            
         
        """
        pass
    @RzCylindricalStiffnessDynamic.setter
    def RzCylindricalStiffnessDynamic(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzCylindricalStiffnessDynamic
         Returns the RZ cylindrical stiffness dynamic   
            
         
        """
        pass
    @property
    def RzCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzCylindricalStructuralDampingConstant
         Returns the RZ structural damping constant   
            
         
        """
        pass
    @property
    def RzCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzCylindricalStructuralDampingDynamic
         Returns the RZ cylindrical structural damping dynamic   
            
         
        """
        pass
    @RzCylindricalStructuralDampingDynamic.setter
    def RzCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzCylindricalStructuralDampingDynamic
         Returns the RZ cylindrical structural damping dynamic   
            
         
        """
        pass
    @property
    def RzCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzCylindricalViscousDampingConstant
         Returns the RZ cylindrical viscous damping constant   
            
         
        """
        pass
    @property
    def RzCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzCylindricalViscousDampingDynamic
         Returns the RZ cylindrical viscous damping dynamic   
            
         
        """
        pass
    @RzCylindricalViscousDampingDynamic.setter
    def RzCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzCylindricalViscousDampingDynamic
         Returns the RZ cylindrical viscous damping dynamic   
            
         
        """
        pass
    @property
    def RzNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearCylindricalDamping
         Returns the RZ nonlinear cylindrical damping   
            
         
        """
        pass
    @RzNonlinearCylindricalDamping.setter
    def RzNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearCylindricalDamping
         Returns the RZ nonlinear cylindrical damping   
            
         
        """
        pass
    @property
    def RzNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearCylindricalStiffness
         Returns the RZ nonlinear cylindrical stiffness   
            
         
        """
        pass
    @RzNonlinearCylindricalStiffness.setter
    def RzNonlinearCylindricalStiffness(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearCylindricalStiffness
         Returns the RZ nonlinear cylindrical stiffness   
            
         
        """
        pass
    @property
    def RzNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearDamping
         Returns the RZ nonlinear damping   
            
         
        """
        pass
    @RzNonlinearDamping.setter
    def RzNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearDamping
         Returns the RZ nonlinear damping   
            
         
        """
        pass
    @property
    def RzNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearStiffness
         Returns the RZ nonlinear stiffness   
            
         
        """
        pass
    @RzNonlinearStiffness.setter
    def RzNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearStiffness
         Returns the RZ nonlinear stiffness   
            
         
        """
        pass
    @property
    def RzStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzStiffnessConstant
         Returns the RZ stiffness constant   
            
         
        """
        pass
    @property
    def RzStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzStiffnessDynamic
         Returns the RZ stiffness dynamic   
            
         
        """
        pass
    @RzStiffnessDynamic.setter
    def RzStiffnessDynamic(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzStiffnessDynamic
         Returns the RZ stiffness dynamic   
            
         
        """
        pass
    @property
    def RzStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzStructuralDampingConstant
         Returns the RZ structural damping constant   
            
         
        """
        pass
    @property
    def RzStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzStructuralDampingDynamic
         Returns the RZ structural damping dynamic   
            
         
        """
        pass
    @RzStructuralDampingDynamic.setter
    def RzStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzStructuralDampingDynamic
         Returns the RZ structural damping dynamic   
            
         
        """
        pass
    @property
    def RzViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzViscousDampingConstant
         Returns the RZ viscous damping constant   
            
         
        """
        pass
    @property
    def RzViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzViscousDampingDynamic
         Returns the RZ viscous damping dynamic   
            
         
        """
        pass
    @RzViscousDampingDynamic.setter
    def RzViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzViscousDampingDynamic
         Returns the RZ viscous damping dynamic   
            
         
        """
        pass
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchConeAngle
         Returns the search cone angle   
            
         
        """
        pass
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchRange
         Returns the search range   
            
         
        """
        pass
    @property
    def StiffnessType(self) -> StiffnessType:
        """
        Getter for property: ( StiffnessType NXOpen.CAE) StiffnessType
         Returns the stiffness type   
            
         
        """
        pass
    @StiffnessType.setter
    def StiffnessType(self, oStiffnessType: StiffnessType):
        """
        Setter for property: ( StiffnessType NXOpen.CAE) StiffnessType
         Returns the stiffness type   
            
         
        """
        pass
    @property
    def XNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) XNonlinearDamping
         Returns the X nonlinear damping   
            
         
        """
        pass
    @XNonlinearDamping.setter
    def XNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) XNonlinearDamping
         Returns the X nonlinear damping   
            
         
        """
        pass
    @property
    def XNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) XNonlinearStiffness
         Returns the X nonlinear stiffness   
            
         
        """
        pass
    @XNonlinearStiffness.setter
    def XNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) XNonlinearStiffness
         Returns the X nonlinear stiffness   
            
         
        """
        pass
    @property
    def XStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XStiffnessConstant
         Returns the X stiffness constant   
            
         
        """
        pass
    @property
    def XStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) XStiffnessDynamic
         Returns the X stiffness dynamic   
            
         
        """
        pass
    @XStiffnessDynamic.setter
    def XStiffnessDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) XStiffnessDynamic
         Returns the X stiffness dynamic   
            
         
        """
        pass
    @property
    def XStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XStructuralDampingConstant
         Returns the X structural damping constant   
            
         
        """
        pass
    @property
    def XStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) XStructuralDampingDynamic
         Returns the X structural damping dynamic   
            
         
        """
        pass
    @XStructuralDampingDynamic.setter
    def XStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) XStructuralDampingDynamic
         Returns the X structural damping dynamic   
            
         
        """
        pass
    @property
    def XViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XViscousDampingConstant
         Returns the X viscous damping constant   
            
         
        """
        pass
    @property
    def XViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) XViscousDampingDynamic
         Returns the X viscous damping dynamic   
            
         
        """
        pass
    @XViscousDampingDynamic.setter
    def XViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) XViscousDampingDynamic
         Returns the X viscous damping dynamic   
            
         
        """
        pass
    @property
    def YNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) YNonlinearDamping
         Returns the Y nonlinear damping   
            
         
        """
        pass
    @YNonlinearDamping.setter
    def YNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) YNonlinearDamping
         Returns the Y nonlinear damping   
            
         
        """
        pass
    @property
    def YNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) YNonlinearStiffness
         Returns the Y nonlinear stiffness   
            
         
        """
        pass
    @YNonlinearStiffness.setter
    def YNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) YNonlinearStiffness
         Returns the Y nonlinear stiffness   
            
         
        """
        pass
    @property
    def YStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YStiffnessConstant
         Returns the Y stiffness constant   
            
         
        """
        pass
    @property
    def YStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) YStiffnessDynamic
         Returns the Y stiffness dynamic   
            
         
        """
        pass
    @YStiffnessDynamic.setter
    def YStiffnessDynamic(self, yDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) YStiffnessDynamic
         Returns the Y stiffness dynamic   
            
         
        """
        pass
    @property
    def YStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YStructuralDampingConstant
         Returns the Y structural damping constant   
            
         
        """
        pass
    @property
    def YStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) YStructuralDampingDynamic
         Returns the Y structural damping dynamic   
            
         
        """
        pass
    @YStructuralDampingDynamic.setter
    def YStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) YStructuralDampingDynamic
         Returns the Y structural damping dynamic   
            
         
        """
        pass
    @property
    def YViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YViscousDampingConstant
         Returns the Y viscous damping constant   
            
         
        """
        pass
    @property
    def YViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) YViscousDampingDynamic
         Returns the Y viscous damping dynamic   
            
         
        """
        pass
    @YViscousDampingDynamic.setter
    def YViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) YViscousDampingDynamic
         Returns the Y viscous damping dynamic   
            
         
        """
        pass
    @property
    def ZCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZCylindricalStiffnessConstant
         Returns the Z cylindrical stiffness constant   
            
         
        """
        pass
    @property
    def ZCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZCylindricalStiffnessDynamic
         Returns the Z cylindrical stiffness dynamic   
            
         
        """
        pass
    @ZCylindricalStiffnessDynamic.setter
    def ZCylindricalStiffnessDynamic(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZCylindricalStiffnessDynamic
         Returns the Z cylindrical stiffness dynamic   
            
         
        """
        pass
    @property
    def ZCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZCylindricalStructuralDampingConstant
         Returns the Z cylindrical structural damping constant   
            
         
        """
        pass
    @property
    def ZCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZCylindricalStructuralDampingDynamic
         Returns the Z cylindrical structural damping dynamic   
            
         
        """
        pass
    @ZCylindricalStructuralDampingDynamic.setter
    def ZCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZCylindricalStructuralDampingDynamic
         Returns the Z cylindrical structural damping dynamic   
            
         
        """
        pass
    @property
    def ZCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZCylindricalViscousDampingConstant
         Returns the Z cylindrical viscous damping constant   
            
         
        """
        pass
    @property
    def ZCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZCylindricalViscousDampingDynamic
         Returns the Z cylindrical viscous damping dynamic   
            
         
        """
        pass
    @ZCylindricalViscousDampingDynamic.setter
    def ZCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZCylindricalViscousDampingDynamic
         Returns the Z cylindrical viscous damping dynamic   
            
         
        """
        pass
    @property
    def ZNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearCylindricalDamping
         Returns the Z nonlinear cylindrical damping   
            
         
        """
        pass
    @ZNonlinearCylindricalDamping.setter
    def ZNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearCylindricalDamping
         Returns the Z nonlinear cylindrical damping   
            
         
        """
        pass
    @property
    def ZNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearCylindricalStiffness
         Returns the Z nonlinear cylindrical stiffness   
            
         
        """
        pass
    @ZNonlinearCylindricalStiffness.setter
    def ZNonlinearCylindricalStiffness(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearCylindricalStiffness
         Returns the Z nonlinear cylindrical stiffness   
            
         
        """
        pass
    @property
    def ZNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearDamping
         Returns the Z nonlinear damping   
            
         
        """
        pass
    @ZNonlinearDamping.setter
    def ZNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearDamping
         Returns the Z nonlinear damping   
            
         
        """
        pass
    @property
    def ZNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearStiffness
         Returns the Z nonlinear stiffness   
            
         
        """
        pass
    @ZNonlinearStiffness.setter
    def ZNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearStiffness
         Returns the Z nonlinear stiffness   
            
         
        """
        pass
    @property
    def ZStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZStiffnessConstant
         Returns the Z stiffness constant   
            
         
        """
        pass
    @property
    def ZStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZStiffnessDynamic
         Returns the Z stiffness dynamic   
            
         
        """
        pass
    @ZStiffnessDynamic.setter
    def ZStiffnessDynamic(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZStiffnessDynamic
         Returns the Z stiffness dynamic   
            
         
        """
        pass
    @property
    def ZStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZStructuralDampingConstant
         Returns the Z structural damping constant   
            
         
        """
        pass
    @property
    def ZStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZStructuralDampingDynamic
         Returns the Z structural damping dynamic   
            
         
        """
        pass
    @ZStructuralDampingDynamic.setter
    def ZStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZStructuralDampingDynamic
         Returns the Z structural damping dynamic   
            
         
        """
        pass
    @property
    def ZViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZViscousDampingConstant
         Returns the Z viscous damping constant   
            
         
        """
        pass
    @property
    def ZViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZViscousDampingDynamic
         Returns the Z viscous damping dynamic   
            
         
        """
        pass
    @ZViscousDampingDynamic.setter
    def ZViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZViscousDampingDynamic
         Returns the Z viscous damping dynamic   
            
         
        """
        pass
class CadComponentsLoadType(Enum):
    """
    Members Include: 
     |AllParts|  Full loading of all CAD components 
     |MainAssociatedPartsOnly|  Full loading of the main associated CAD components 

    """
    AllParts: int
    MainAssociatedPartsOnly: int
    @staticmethod
    def ValueOf(value: int) -> CadComponentsLoadType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class Clinch(IConnection): 
    """ Clinch connection. Use this interface to setget properties and parameters of the clinch connection.  """
    @property
    def Coefficient(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Coefficient
         Returns the coefficient for formula defined diameter   
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the connection diameter   
            
         
        """
        pass
    @property
    def DiameterType(self) -> DiameterType:
        """
        Getter for property: ( DiameterType NXOpen.CAE) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: ( DiameterType NXOpen.CAE) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromStart
         Returns the line Discretization distance from start   
            
         
        """
        pass
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceToEnd
         Returns the line Discretization distance to end   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height value   
            
         
        """
        pass
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LengthStep
         Returns the line Discretization length step   
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxAngleBetweenNormals
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDistCGToElemCG
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxLengthStep
         Returns the line Discretization max length step   
            
         
        """
        pass
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxNormalDistCGToFlanges
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProjectTolerance
         Returns the projection tolerance   
            
         
        """
        pass
    @property
    def TableFile(self) -> str:
        """
        Getter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
import NXOpen
class ComponentData(NXOpen.TaggedObject): 
    """ Composer connection. Use this interface to setget properties and parameters of the spot weld connection.  """
    @property
    def ComponentName(self) -> str:
        """
        Getter for property: (str) ComponentName
         Returns the component name    
            
         
        """
        pass
    @ComponentName.setter
    def ComponentName(self, name: str):
        """
        Setter for property: (str) ComponentName
         Returns the component name    
            
         
        """
        pass
    @property
    def ConnectionPointsPath(self) -> str:
        """
        Getter for property: (str) ConnectionPointsPath
         Returns the connection points path    
            
         
        """
        pass
    @ConnectionPointsPath.setter
    def ConnectionPointsPath(self, connectionPointsPath: str):
        """
        Setter for property: (str) ConnectionPointsPath
         Returns the connection points path    
            
         
        """
        pass
    @property
    def FilePath(self) -> str:
        """
        Getter for property: (str) FilePath
         Returns the file path    
            
         
        """
        pass
    @FilePath.setter
    def FilePath(self, path: str):
        """
        Setter for property: (str) FilePath
         Returns the file path    
            
         
        """
        pass
    @property
    def ImportedConnectionPointsPath(self) -> str:
        """
        Getter for property: (str) ImportedConnectionPointsPath
         Returns the imported connection points path    
            
         
        """
        pass
    @ImportedConnectionPointsPath.setter
    def ImportedConnectionPointsPath(self, importedConnPointsPath: str):
        """
        Setter for property: (str) ImportedConnectionPointsPath
         Returns the imported connection points path    
            
         
        """
        pass
    @property
    def MeshPath(self) -> str:
        """
        Getter for property: (str) MeshPath
         Returns the mesh path    
            
         
        """
        pass
    @MeshPath.setter
    def MeshPath(self, meshPath: str):
        """
        Setter for property: (str) MeshPath
         Returns the mesh path    
            
         
        """
        pass
    @property
    def RepresentationFilePath(self) -> str:
        """
        Getter for property: (str) RepresentationFilePath
         Returns the component representation path    
            
         
        """
        pass
    @RepresentationFilePath.setter
    def RepresentationFilePath(self, representationTypeFilePath: str):
        """
        Setter for property: (str) RepresentationFilePath
         Returns the component representation path    
            
         
        """
        pass
    @property
    def RepresentationType(self) -> str:
        """
        Getter for property: (str) RepresentationType
         Returns the component Representation Type    
            
         
        """
        pass
    @RepresentationType.setter
    def RepresentationType(self, representationType: str):
        """
        Setter for property: (str) RepresentationType
         Returns the component Representation Type    
            
         
        """
        pass
    @property
    def SolverType(self) -> str:
        """
        Getter for property: (str) SolverType
         Returns the component Solver Type    
            
         
        """
        pass
    @SolverType.setter
    def SolverType(self, solverType: str):
        """
        Setter for property: (str) SolverType
         Returns the component Solver Type    
            
         
        """
        pass
class ComposerConnectionType(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |Bolt|  Bolt 
     |Spring|  Spring 
     |Latch|  Latch 
     |Bushing|  Bushing 
     |BumpStop|  BumpStop 
     |Kinematic|  Kinematic 
     |WeatherStrip|  WeatherStrip 
     |SeamWeld|  SeamWeld 
     |Adhesive|  Adhesive 
     |SpotWeld|  SpotWeld 
     |Bar|  Bar 

    """
    NotSet: int
    Bolt: int
    Spring: int
    Latch: int
    Bushing: int
    BumpStop: int
    Kinematic: int
    WeatherStrip: int
    SeamWeld: int
    Adhesive: int
    SpotWeld: int
    Bar: int
    @staticmethod
    def ValueOf(value: int) -> ComposerConnectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class ComposerData(NXOpen.TaggedObject): 
    """ Composer connection. Use this interface to setgetcreate properties and setget parameters of the composer.  """
    @property
    def AssemblyName(self) -> str:
        """
        Getter for property: (str) AssemblyName
         Returns the assembly name    
            
         
        """
        pass
    @AssemblyName.setter
    def AssemblyName(self, assemblyName: str):
        """
        Setter for property: (str) AssemblyName
         Returns the assembly name    
            
         
        """
        pass
    @property
    def ComponentUnitSystem(self) -> str:
        """
        Getter for property: (str) ComponentUnitSystem
         Returns the component unit system    
            
         
        """
        pass
    @ComponentUnitSystem.setter
    def ComponentUnitSystem(self, componentUnitSystem: str):
        """
        Setter for property: (str) ComponentUnitSystem
         Returns the component unit system    
            
         
        """
        pass
    @property
    def InputFileDir(self) -> str:
        """
        Getter for property: (str) InputFileDir
         Returns the input file direction    
            
         
        """
        pass
    @InputFileDir.setter
    def InputFileDir(self, inputFileDir: str):
        """
        Setter for property: (str) InputFileDir
         Returns the input file direction    
            
         
        """
        pass
    @property
    def MaterialDBDir(self) -> str:
        """
        Getter for property: (str) MaterialDBDir
         Returns the material file direction    
            
         
        """
        pass
    @MaterialDBDir.setter
    def MaterialDBDir(self, materialDBDir: str):
        """
        Setter for property: (str) MaterialDBDir
         Returns the material file direction    
            
         
        """
        pass
    @property
    def OutputFileDir(self) -> str:
        """
        Getter for property: (str) OutputFileDir
         Returns the output file direction    
            
         
        """
        pass
    @OutputFileDir.setter
    def OutputFileDir(self, outputFileDir: str):
        """
        Setter for property: (str) OutputFileDir
         Returns the output file direction    
            
         
        """
        pass
    @property
    def StartNumAxisSystems(self) -> int:
        """
        Getter for property: (int) StartNumAxisSystems
         Returns the start axis number    
            
         
        """
        pass
    @StartNumAxisSystems.setter
    def StartNumAxisSystems(self, startNumAxisSystems: int):
        """
        Setter for property: (int) StartNumAxisSystems
         Returns the start axis number    
            
         
        """
        pass
    @property
    def StartNumNodeAndElement(self) -> int:
        """
        Getter for property: (int) StartNumNodeAndElement
         Returns the start node and element number    
            
         
        """
        pass
    @StartNumNodeAndElement.setter
    def StartNumNodeAndElement(self, startNumNodeAndElement: int):
        """
        Setter for property: (int) StartNumNodeAndElement
         Returns the start node and element number    
            
         
        """
        pass
    @property
    def StartNumProperties(self) -> int:
        """
        Getter for property: (int) StartNumProperties
         Returns the start properties number    
            
         
        """
        pass
    @StartNumProperties.setter
    def StartNumProperties(self, startNumProperties: int):
        """
        Setter for property: (int) StartNumProperties
         Returns the start properties number    
            
         
        """
        pass
    def CreateComponent(self) -> ComponentData:
        """
         Create component. 
         Returns component ( ComponentData NXOpen.CAE): .
        """
        pass
    def CreateConnection(self) -> ConnectionData:
        """
         Create component. 
         Returns connection ( ConnectionData NXOpen.CAE): .
        """
        pass
    def GetComponents(self) -> List[ComponentData]:
        """
         Gets components. 
         Returns components ( ComponentData List[NXOpen.C): .
        """
        pass
    def GetConnections(self) -> List[ConnectionData]:
        """
         Gets connections 
         Returns connections ( ConnectionData List[NXOpen.C): .
        """
        pass
    def SetComponents(self, components: List[ComponentData]) -> None:
        """
         Sets components. 
        """
        pass
    def SetConnections(self, connections: List[ConnectionData]) -> None:
        """
         Sets connections 
        """
        pass
import NXOpen
class ComposerTool(NXOpen.Object): 
    """ ComposerTool.  """
    def CreateComposer() -> Composer:
        """
         CreateComposer  
         Returns composer ( Composer NXOpen.CAE): .
        """
        pass
import NXOpen
import NXOpen.CAE
class Composer(NXOpen.TaggedObject): 
    """ Composer. Use this interface to setgetcreate properties and setget parameters of the composer.  """
    @property
    def ComposerData(self) -> ComposerData:
        """
        Getter for property: ( ComposerData NXOpen.CAE) ComposerData
         Returns the composer data    
            
         
        """
        pass
    @ComposerData.setter
    def ComposerData(self, composerData: ComposerData):
        """
        Setter for property: ( ComposerData NXOpen.CAE) ComposerData
         Returns the composer data    
            
         
        """
        pass
    @property
    def ConnectionDBData(self) -> ConnectionDBData:
        """
        Getter for property: ( ConnectionDBData NXOpen.CAE) ConnectionDBData
         Returns the connection db data    
            
         
        """
        pass
    @ConnectionDBData.setter
    def ConnectionDBData(self, connectionDBData: ConnectionDBData):
        """
        Setter for property: ( ConnectionDBData NXOpen.CAE) ConnectionDBData
         Returns the connection db data    
            
         
        """
        pass
    def CheckAssemblyConnections(self) -> List[str]:
        """
         CheckAssemblyConnections  
         Returns results (List[str]): .
        """
        pass
    def CheckAssemblyDocumentConnections(self, documentName: str) -> List[str]:
        """
         CheckAssemblyDocumentConnections  
         Returns results (List[str]): .
        """
        pass
    def CreateComposerData(self) -> ComposerData:
        """
         Create composer data. 
         Returns composerData ( ComposerData NXOpen.CAE): .
        """
        pass
    def Destroy(self) -> None:
        """
         Destroy the composer object 
        """
        pass
    def ExportHardPointToXml(self, tWorkPart: NXOpen.CAE.CaePart, tUnit: NXOpen.Unit, file: str) -> None:
        """
         Export HardPoint To Xml 
        """
        pass
    def GetAxisFromAlias(self, axisAlias: str) -> List[NXOpen.CoordinateSystem]:
        """
         GetAxisFromAlias  
         Returns axes ( NXOpen.CoordinateSystem Li): .
        """
        pass
    def GetLumpedMassData(self) -> List[LMIEConnection]:
        """
         Get the intermediate connection representations of lumped mass connections loaded from external file.
         Returns oConnections ( LMIEConnection List[NXOpen.C):  The intermediate connection representations .
        """
        pass
    def GetMaterialsData(self, inputBdfFilePath: str) -> List[str]:
        """
         Get MAT1 and MAT8 data from bdf file
         Returns listOfMaterialsDataResults (List[str]): .
        """
        pass
    def GetMeshPartFromPID(self, pid: int) -> List[NXOpen.TaggedObject]:
        """
         GetMeshPartFromPID  
         Returns meshParts ( NXOpen.TaggedObject Li): .
        """
        pass
    def GetMeshPartInContextFromPID(self, tWorkPart: NXOpen.CAE.CaePart, pid: int) -> List[NXOpen.TaggedObject]:
        """
         GetMeshPartInContextFromPID  
         Returns meshParts ( NXOpen.TaggedObject Li): .
        """
        pass
    def ImportAndModifyHardPointLabel(self, tWorkPart: NXOpen.CAE.CaePart, file: str) -> List[NXOpen.CAE.SelectionRecipe]:
        """
         Import HardPoint From Excel and Modify its Node Label 
         Returns selrecipes ( NXOpen.CAE.SelectionRecipe Li): .
        """
        pass
    def ImportAndUpdateHardPointFromXml(self, tWorkPart: NXOpen.CAE.CaePart, file: str, isUpdate: bool) -> Tuple[List[NXOpen.CAE.SelectionRecipe], List[NXOpen.CAE.SelectionRecipe]]:
        """
         Import HardPoint From Xml if does not exist and replaceupdate it otherwise
         Returns A tuple consisting of (selrecipes, updatedSelrecipes). 
         - selrecipes is:  NXOpen.CAE.SelectionRecipe Li. Array of created recipe tags .
         - updatedSelrecipes is:  NXOpen.CAE.SelectionRecipe Li. Array of replaced recipe tags .

        """
        pass
    def MigrateToHardPointFile(self, file: str) -> None:
        """
         Migrate old XML format  
        """
        pass
    def ReadAssemblyDefinition(self, filePath: str) -> None:
        """
         ReadAssemblyDefinition  
        """
        pass
    def ReadConnectionsDB(self, filePath: str) -> None:
        """
         ReadConnectionsDB  
        """
        pass
    def SearchBoltComponentAndPIDs(self, documentName: str) -> List[str]:
        """
         SearchBoltComponentAndPIDs  
         Returns listOfConnPIDsResults (List[str]): .
        """
        pass
    def SearchPIDs(self, documentName: str) -> Tuple[bool, List[str], List[str]]:
        """
         SearchPIDs  
         Returns A tuple consisting of (isAssemblyOpen, listOfConnPIDsResults, listOfMassPIDsResults). 
         - isAssemblyOpen is: bool.
         - listOfConnPIDsResults is: List[str].
         - listOfMassPIDsResults is: List[str].

        """
        pass
    def SetLumpedMassData(self, iConnections: List[LMIEConnection]) -> None:
        """
         Set the intermediate connection representations of lumped mass connections loaded from external file.
        """
        pass
    def WriteAssemblyDefinition(self, filePath: str) -> None:
        """
         WriteAssemblyDefinition  
        """
        pass
import NXOpen
class ConnectionData(NXOpen.TaggedObject): 
    """ Composer connection. Use this interface to setget properties and parameters of the spot weld connection.  """
    @property
    def Comp1(self) -> ComponentData:
        """
        Getter for property: ( ComponentData NXOpen.CAE) Comp1
         Returns the comp1    
            
         
        """
        pass
    @Comp1.setter
    def Comp1(self, comp1: ComponentData):
        """
        Setter for property: ( ComponentData NXOpen.CAE) Comp1
         Returns the comp1    
            
         
        """
        pass
    @property
    def Comp2(self) -> ComponentData:
        """
        Getter for property: ( ComponentData NXOpen.CAE) Comp2
         Returns the comp2    
            
         
        """
        pass
    @Comp2.setter
    def Comp2(self, comp2: ComponentData):
        """
        Setter for property: ( ComponentData NXOpen.CAE) Comp2
         Returns the comp2    
            
         
        """
        pass
    @property
    def Comp3(self) -> ComponentData:
        """
        Getter for property: ( ComponentData NXOpen.CAE) Comp3
         Returns the comp3    
            
         
        """
        pass
    @Comp3.setter
    def Comp3(self, comp3: ComponentData):
        """
        Setter for property: ( ComponentData NXOpen.CAE) Comp3
         Returns the comp3    
            
         
        """
        pass
    @property
    def ConnectionType(self) -> ComposerConnectionType:
        """
        Getter for property: ( ComposerConnectionType NXOpen.CAE) ConnectionType
         Returns the connection type    
            
         
        """
        pass
    @ConnectionType.setter
    def ConnectionType(self, type: ComposerConnectionType):
        """
        Setter for property: ( ComposerConnectionType NXOpen.CAE) ConnectionType
         Returns the connection type    
            
         
        """
        pass
    @property
    def DBItem(self) -> str:
        """
        Getter for property: (str) DBItem
         Returns the db item    
            
         
        """
        pass
    @DBItem.setter
    def DBItem(self, name: str):
        """
        Setter for property: (str) DBItem
         Returns the db item    
            
         
        """
        pass
    @property
    def Dof1(self) -> bool:
        """
        Getter for property: (bool) Dof1
         Returns the dof1   
            
         
        """
        pass
    @Dof1.setter
    def Dof1(self, name: bool):
        """
        Setter for property: (bool) Dof1
         Returns the dof1   
            
         
        """
        pass
    @property
    def Dof2(self) -> bool:
        """
        Getter for property: (bool) Dof2
         Returns the dof2   
            
         
        """
        pass
    @Dof2.setter
    def Dof2(self, name: bool):
        """
        Setter for property: (bool) Dof2
         Returns the dof2   
            
         
        """
        pass
    @property
    def Dof3(self) -> bool:
        """
        Getter for property: (bool) Dof3
         Returns the dof3   
            
         
        """
        pass
    @Dof3.setter
    def Dof3(self, name: bool):
        """
        Setter for property: (bool) Dof3
         Returns the dof3   
            
         
        """
        pass
    @property
    def Dof4(self) -> bool:
        """
        Getter for property: (bool) Dof4
         Returns the dof4   
            
         
        """
        pass
    @Dof4.setter
    def Dof4(self, name: bool):
        """
        Setter for property: (bool) Dof4
         Returns the dof4   
            
         
        """
        pass
    @property
    def Dof5(self) -> bool:
        """
        Getter for property: (bool) Dof5
         Returns the dof5   
            
         
        """
        pass
    @Dof5.setter
    def Dof5(self, name: bool):
        """
        Setter for property: (bool) Dof5
         Returns the dof5   
            
         
        """
        pass
    @property
    def Dof6(self) -> bool:
        """
        Getter for property: (bool) Dof6
         Returns the dof6   
            
         
        """
        pass
    @Dof6.setter
    def Dof6(self, name: bool):
        """
        Setter for property: (bool) Dof6
         Returns the dof6   
            
         
        """
        pass
    @property
    def ExpansionRadius1(self) -> float:
        """
        Getter for property: (float) ExpansionRadius1
         Returns the expansion radius1   
            
         
        """
        pass
    @ExpansionRadius1.setter
    def ExpansionRadius1(self, expansionRadius1: float):
        """
        Setter for property: (float) ExpansionRadius1
         Returns the expansion radius1   
            
         
        """
        pass
    @property
    def ExpansionRadius2(self) -> float:
        """
        Getter for property: (float) ExpansionRadius2
         Returns the expansion radius2   
            
         
        """
        pass
    @ExpansionRadius2.setter
    def ExpansionRadius2(self, expansionRadius2: float):
        """
        Setter for property: (float) ExpansionRadius2
         Returns the expansion radius2   
            
         
        """
        pass
    @property
    def ExpansionRadiusFactor1(self) -> float:
        """
        Getter for property: (float) ExpansionRadiusFactor1
         Returns the expansion radius factor1   
            
         
        """
        pass
    @ExpansionRadiusFactor1.setter
    def ExpansionRadiusFactor1(self, expansionRadiusFactor1: float):
        """
        Setter for property: (float) ExpansionRadiusFactor1
         Returns the expansion radius factor1   
            
         
        """
        pass
    @property
    def ExpansionRadiusFactor2(self) -> float:
        """
        Getter for property: (float) ExpansionRadiusFactor2
         Returns the expansion radius factor2   
            
         
        """
        pass
    @ExpansionRadiusFactor2.setter
    def ExpansionRadiusFactor2(self, expansionRadiusFactor2: float):
        """
        Setter for property: (float) ExpansionRadiusFactor2
         Returns the expansion radius factor2   
            
         
        """
        pass
    @property
    def FlangeSearchTolerance1(self) -> float:
        """
        Getter for property: (float) FlangeSearchTolerance1
         Returns the expansion radius factor1   
            
         
        """
        pass
    @FlangeSearchTolerance1.setter
    def FlangeSearchTolerance1(self, flangeSearchTolerance1: float):
        """
        Setter for property: (float) FlangeSearchTolerance1
         Returns the expansion radius factor1   
            
         
        """
        pass
    @property
    def FlangeSearchTolerance2(self) -> float:
        """
        Getter for property: (float) FlangeSearchTolerance2
         Returns the expansion radius factor2   
            
         
        """
        pass
    @FlangeSearchTolerance2.setter
    def FlangeSearchTolerance2(self, flangeSearchTolerance2: float):
        """
        Setter for property: (float) FlangeSearchTolerance2
         Returns the expansion radius factor2   
            
         
        """
        pass
    @property
    def FlangeType1(self) -> str:
        """
        Getter for property: (str) FlangeType1
         Returns the flange type1    
            
         
        """
        pass
    @FlangeType1.setter
    def FlangeType1(self, flangeType1: str):
        """
        Setter for property: (str) FlangeType1
         Returns the flange type1    
            
         
        """
        pass
    @property
    def FlangeType2(self) -> str:
        """
        Getter for property: (str) FlangeType2
         Returns the flange type2    
            
         
        """
        pass
    @FlangeType2.setter
    def FlangeType2(self, flangeType2: str):
        """
        Setter for property: (str) FlangeType2
         Returns the flange type2    
            
         
        """
        pass
    @property
    def HeadDiameter(self) -> float:
        """
        Getter for property: (float) HeadDiameter
         Returns the head diameter    
            
         
        """
        pass
    @HeadDiameter.setter
    def HeadDiameter(self, headDiameter: float):
        """
        Setter for property: (float) HeadDiameter
         Returns the head diameter    
            
         
        """
        pass
    @property
    def LengthStep(self) -> float:
        """
        Getter for property: (float) LengthStep
         Returns the expansion radius factor2   
            
         
        """
        pass
    @LengthStep.setter
    def LengthStep(self, lengthStep: float):
        """
        Setter for property: (float) LengthStep
         Returns the expansion radius factor2   
            
         
        """
        pass
    @property
    def LinePart1(self) -> str:
        """
        Getter for property: (str) LinePart1
         Returns the line part1    
            
         
        """
        pass
    @LinePart1.setter
    def LinePart1(self, linePart: str):
        """
        Setter for property: (str) LinePart1
         Returns the line part1    
            
         
        """
        pass
    @property
    def LinePart2(self) -> str:
        """
        Getter for property: (str) LinePart2
         Returns the line part2    
            
         
        """
        pass
    @LinePart2.setter
    def LinePart2(self, linePart: str):
        """
        Setter for property: (str) LinePart2
         Returns the line part2    
            
         
        """
        pass
    @property
    def MaximumDistanceTolerance1(self) -> float:
        """
        Getter for property: (float) MaximumDistanceTolerance1
         Returns the maximum distance tolerance1    
            
         
        """
        pass
    @MaximumDistanceTolerance1.setter
    def MaximumDistanceTolerance1(self, maximumDistanceTolerance1: float):
        """
        Setter for property: (float) MaximumDistanceTolerance1
         Returns the maximum distance tolerance1    
            
         
        """
        pass
    @property
    def MaximumDistanceTolerance2(self) -> float:
        """
        Getter for property: (float) MaximumDistanceTolerance2
         Returns the maximum distance tolerance2    
            
         
        """
        pass
    @MaximumDistanceTolerance2.setter
    def MaximumDistanceTolerance2(self, maximumDistanceTolerance2: float):
        """
        Setter for property: (float) MaximumDistanceTolerance2
         Returns the maximum distance tolerance2    
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the assembly name    
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the assembly name    
            
         
        """
        pass
    @property
    def SearchType1(self) -> str:
        """
        Getter for property: (str) SearchType1
         Returns the search type1    
            
         
        """
        pass
    @SearchType1.setter
    def SearchType1(self, searchType1: str):
        """
        Setter for property: (str) SearchType1
         Returns the search type1    
            
         
        """
        pass
    @property
    def SearchType2(self) -> str:
        """
        Getter for property: (str) SearchType2
         Returns the search type2    
            
         
        """
        pass
    @SearchType2.setter
    def SearchType2(self, searchType2: str):
        """
        Setter for property: (str) SearchType2
         Returns the search type2    
            
         
        """
        pass
    @property
    def ShankDiameter(self) -> float:
        """
        Getter for property: (float) ShankDiameter
         Returns the shank diameter    
            
         
        """
        pass
    @ShankDiameter.setter
    def ShankDiameter(self, shankDiameter: float):
        """
        Setter for property: (float) ShankDiameter
         Returns the shank diameter    
            
         
        """
        pass
    @property
    def WCDFile(self) -> str:
        """
        Getter for property: (str) WCDFile
         Returns the WCD File    
            
         
        """
        pass
    @WCDFile.setter
    def WCDFile(self, wcdFile: str):
        """
        Setter for property: (str) WCDFile
         Returns the WCD File    
            
         
        """
        pass
    def GetAxis(self) -> str:
        """
         Gets axis. 
         Returns axis (str): .
        """
        pass
    def GetComponents1(self) -> List[ComponentData]:
        """
         Get Components1  
         Returns comps ( ComponentData List[NXOpen.C): .
        """
        pass
    def GetComponents2(self) -> List[ComponentData]:
        """
         Get Components2  
         Returns comps ( ComponentData List[NXOpen.C): .
        """
        pass
    def GetInvalidDOF(self) -> List[int]:
        """
         Invalid dof 
         Returns invalidDOF (List[int]): .
        """
        pass
    def GetLineFEEdgeRecipe1(self) -> List[str]:
        """
         Get line  FE edge recipe1  
         Returns lineFEEdgeRecipe1s (List[str]): .
        """
        pass
    def GetLineFEEdgeRecipe2(self) -> List[str]:
        """
         Get line  FE edge recipe2  
         Returns lineFEEdgeRecipe2s (List[str]): .
        """
        pass
    def GetPID1s(self) -> List[int]:
        """
         Get pID1s 
         Returns pID1s (List[int]): .
        """
        pass
    def GetPID2s(self) -> List[int]:
        """
         Get pID2s 
         Returns pID2s (List[int]): .
        """
        pass
    def GetPID3s(self) -> List[int]:
        """
         Get pID3s 
         Returns pID3s (List[int]): .
        """
        pass
    def GetPointNameCoord1(self) -> List[str]:
        """
         Get point name coord1  
         Returns pointNameCoord1s (List[str]): .
        """
        pass
    def GetPointNameCoord2(self) -> List[str]:
        """
         Get point name coord2  
         Returns pointNameCoord2s (List[str]): .
        """
        pass
    def GetPointNameCoord3(self) -> List[str]:
        """
         Get point name coord3  
         Returns pointNameCoord3s (List[str]): .
        """
        pass
    def SetAxis(self, axis: str) -> None:
        """
         Sets axis. 
        """
        pass
    def SetComponents1(self, comps: List[ComponentData]) -> None:
        """
         Set Components1  
        """
        pass
    def SetComponents2(self, comps: List[ComponentData]) -> None:
        """
         Set Components2  
        """
        pass
    def SetLineFEEdgeRecipe1(self, lineFEEdgeRecipe1s: List[str]) -> None:
        """
         Set line  FE edge recipe1  
        """
        pass
    def SetLineFEEdgeRecipe2(self, lineFEEdgeRecipe2s: List[str]) -> None:
        """
         Set line  FE edge recipe1  
        """
        pass
    def SetPID1s(self, pID1s: List[int]) -> None:
        """
         Set pID1s 
        """
        pass
    def SetPID2s(self, pID2s: List[int]) -> None:
        """
         Set pID2s 
        """
        pass
    def SetPID3s(self, pID3s: List[int]) -> None:
        """
         Set pID3s 
        """
        pass
    def SetPointNameCoord1(self, pointNameCoord1s: List[str]) -> None:
        """
         Set point name coord1  
        """
        pass
    def SetPointNameCoord2(self, pointNameCoord2s: List[str]) -> None:
        """
         Set point name coord2  
        """
        pass
    def SetPointNameCoord3(self, pointNameCoord3s: List[str]) -> None:
        """
         Set point name coord3  
        """
        pass
import NXOpen
class ConnectionDBData(NXOpen.TaggedObject): 
    """ Connection DB data. Use this interface to setget properties and parameters of the connection DB data.  """
    def GetConnectionDBItemDatas(self) -> List[ConnectionDBItemData]:
        """
         Gets connection DB item datas. 
         Returns components ( ConnectionDBItemData List[NXOpen.C): .
        """
        pass
    def SetConnectionDBItemDatas(self, components: List[ConnectionDBItemData]) -> None:
        """
         Sets connection DB item datas. 
        """
        pass
import NXOpen
class ConnectionDBItemData(NXOpen.TaggedObject): 
    """ Connection DB item data. Use this interface to setget properties and parameters of the Connection DB item data.  """
    @property
    def AdhesiveWidth(self) -> float:
        """
        Getter for property: (float) AdhesiveWidth
         Returns the adhesive width    
            
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height    
            
         
        """
        pass
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the height type    
            
         
        """
        pass
    @property
    def Mass(self) -> float:
        """
        Getter for property: (float) Mass
         Returns the mass    
            
         
        """
        pass
    @Mass.setter
    def Mass(self, mass: float):
        """
        Setter for property: (float) Mass
         Returns the mass    
            
         
        """
        pass
    @property
    def MaterialID(self) -> int:
        """
        Getter for property: (int) MaterialID
         Returns the material ID    
            
         
        """
        pass
    @MaterialID.setter
    def MaterialID(self, materialID: int):
        """
        Setter for property: (int) MaterialID
         Returns the material ID    
            
         
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
    def ScrewDiameter(self) -> float:
        """
        Getter for property: (float) ScrewDiameter
         Returns the screw diameter    
            
         
        """
        pass
    @ScrewDiameter.setter
    def ScrewDiameter(self, screwDiameter: float):
        """
        Setter for property: (float) ScrewDiameter
         Returns the screw diameter    
            
         
        """
        pass
    @property
    def StiffnessR(self) -> float:
        """
        Getter for property: (float) StiffnessR
         Returns the stiffness R    
            
         
        """
        pass
    @StiffnessR.setter
    def StiffnessR(self, stiffnessR: float):
        """
        Setter for property: (float) StiffnessR
         Returns the stiffness R    
            
         
        """
        pass
    @property
    def StiffnessRR(self) -> float:
        """
        Getter for property: (float) StiffnessRR
         Returns the stiffness RR    
            
         
        """
        pass
    @StiffnessRR.setter
    def StiffnessRR(self, stiffnessRR: float):
        """
        Setter for property: (float) StiffnessRR
         Returns the stiffness RR    
            
         
        """
        pass
    @property
    def StiffnessRS(self) -> float:
        """
        Getter for property: (float) StiffnessRS
         Returns the stiffness RS    
            
         
        """
        pass
    @StiffnessRS.setter
    def StiffnessRS(self, stiffnessRS: float):
        """
        Setter for property: (float) StiffnessRS
         Returns the stiffness RS    
            
         
        """
        pass
    @property
    def StiffnessRX(self) -> float:
        """
        Getter for property: (float) StiffnessRX
         Returns the stiffness RX    
            
         
        """
        pass
    @StiffnessRX.setter
    def StiffnessRX(self, stiffnessRX: float):
        """
        Setter for property: (float) StiffnessRX
         Returns the stiffness RX    
            
         
        """
        pass
    @property
    def StiffnessRY(self) -> float:
        """
        Getter for property: (float) StiffnessRY
         Returns the stiffness RY    
            
         
        """
        pass
    @StiffnessRY.setter
    def StiffnessRY(self, stiffnessRY: float):
        """
        Setter for property: (float) StiffnessRY
         Returns the stiffness RY    
            
         
        """
        pass
    @property
    def StiffnessRZ(self) -> float:
        """
        Getter for property: (float) StiffnessRZ
         Returns the stiffness RZ    
            
         
        """
        pass
    @StiffnessRZ.setter
    def StiffnessRZ(self, stiffnessRZ: float):
        """
        Setter for property: (float) StiffnessRZ
         Returns the stiffness RZ    
            
         
        """
        pass
    @property
    def StiffnessS(self) -> float:
        """
        Getter for property: (float) StiffnessS
         Returns the stiffness RS    
            
         
        """
        pass
    @StiffnessS.setter
    def StiffnessS(self, stiffnessS: float):
        """
        Setter for property: (float) StiffnessS
         Returns the stiffness RS    
            
         
        """
        pass
    @property
    def StiffnessType(self) -> ConnectionDBItemStiffnessType:
        """
        Getter for property: ( ConnectionDBItemStiffnessType NXOpen.CAE) StiffnessType
         Returns the mass    
            
         
        """
        pass
    @StiffnessType.setter
    def StiffnessType(self, stiffnessType: ConnectionDBItemStiffnessType):
        """
        Setter for property: ( ConnectionDBItemStiffnessType NXOpen.CAE) StiffnessType
         Returns the mass    
            
         
        """
        pass
    @property
    def StiffnessX(self) -> float:
        """
        Getter for property: (float) StiffnessX
         Returns the stiffness X    
            
         
        """
        pass
    @StiffnessX.setter
    def StiffnessX(self, stiffnessX: float):
        """
        Setter for property: (float) StiffnessX
         Returns the stiffness X    
            
         
        """
        pass
    @property
    def StiffnessY(self) -> float:
        """
        Getter for property: (float) StiffnessY
         Returns the stiffness Y    
            
         
        """
        pass
    @StiffnessY.setter
    def StiffnessY(self, stiffnessY: float):
        """
        Setter for property: (float) StiffnessY
         Returns the stiffness Y    
            
         
        """
        pass
    @property
    def StiffnessZ(self) -> float:
        """
        Getter for property: (float) StiffnessZ
         Returns the stiffness Z    
            
         
        """
        pass
    @StiffnessZ.setter
    def StiffnessZ(self, stiffnessZ: float):
        """
        Setter for property: (float) StiffnessZ
         Returns the stiffness Z    
            
         
        """
        pass
    def GetDofs(self) -> List[int]:
        """
         The Dofs  
         Returns listOfDofs (List[int]): .
        """
        pass
class ConnectionDBItemStiffnessType(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |Rectangular|  Rectangular 
     |Spherical|  Spherical 
     |Cylindrical|  Cylindrical 

    """
    NotSet: int
    Rectangular: int
    Spherical: int
    Cylindrical: int
    @staticmethod
    def ValueOf(value: int) -> ConnectionDBItemStiffnessType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ConnectionType(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |SpotWeld|  SpotWeld 
     |Adhesive|  Adhesive 
     |Bolt|  Bolt 
     |Spring|  Spring 
     |Rigid|  Rigid 
     |Bushing|  Bushing 
     |Damper|  Damper 
     |Kinematic|  Kinematic 
     |SeamWeld|  Seam Weld 
     |Sealing|  Sealing 
     |Rivet|  Rivet 
     |LumpedMass|  Lumped Mass 
     |Clinch|  Clinch 
     |Crimp|  Crimp 
     |Bar|  Bar 
     |Bearing|  Bearing 

    """
    NotSet: int
    SpotWeld: int
    Adhesive: int
    Bolt: int
    Spring: int
    Rigid: int
    Bushing: int
    Damper: int
    Kinematic: int
    SeamWeld: int
    Sealing: int
    Rivet: int
    LumpedMass: int
    Clinch: int
    Crimp: int
    Bar: int
    Bearing: int
    @staticmethod
    def ValueOf(value: int) -> ConnectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class CoordinatesLocation(Location): 
    """  Location interface. This defines connection locations with common properties like coordinates.  """
    def GetCoordinates(self) -> NXOpen.Point3d:
        """
         Gets the coordinates from the specified location.
                        The location can be any type: coordinates, node or point.
                        Its coordinates will be returned. 
         Returns coordinates ( NXOpen.Point3d):  Location coordinates .
        """
        pass
    def SetCoordinates(self, coordinates: NXOpen.Point3d) -> None:
        """
         Set the coordinates. Only for coordinates type location 
        """
        pass
import NXOpen
class CoordinatesSeriesLocation(Location): 
    """  Location interface. This defines connection locations with common properties like coordinates.  """
    def GetCoordinates(self) -> List[NXOpen.Point3d]:
        """
         Gets the coordinates from the specified location.
                        The location can be any type: coordinates, node or point.
                        Its coordinates will be returned. 
         Returns coordinates ( NXOpen.Point3d Li):  Location coordinates .
        """
        pass
    def SetCoordinates(self, coordinates: List[NXOpen.Point3d]) -> None:
        """
         Set the coordinates. Only for coordinates type location 
        """
        pass
import NXOpen
class Crimp(IConnection): 
    """  Crimp connection. Use this interface to setget properties and parameters of the crimp connection.  """
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromStart
         Returns the line Discretization distance from start   
            
         
        """
        pass
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceToEnd
         Returns the line Discretization distance to end   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height value   
            
         
        """
        pass
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LengthStep
         Returns the line Discretization length step   
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxAngleBetweenNormals
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDistCGToElemCG
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxLengthStep
         Returns the line Discretization max length step   
            
         
        """
        pass
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxNormalDistCGToFlanges
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProjectTolerance
         Returns the projection tolerance   
            
         
        """
        pass
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width value   
            
         
        """
        pass
class CsysType(Enum):
    """
    Members Include: 
     |Existing|  Existing CSYS 
     |Predefined|  Predefined CSYS 
     |Absolute|  Absolute CSYS 
     |LocalCartesian|  Local Cartesian CSYS 
     |LocalCylindrical|  Local Cylindrical CSYS 
     |LocalSpherical|  Local Spherical CSYS 

    """
    Existing: int
    Predefined: int
    Absolute: int
    LocalCartesian: int
    LocalCylindrical: int
    LocalSpherical: int
    @staticmethod
    def ValueOf(value: int) -> CsysType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class CurveLocation(Location): 
    """  Location interface. This defines connection locations with common properties like coordinates.  """
    @property
    def Curve(self) -> NXOpen.IBaseCurve:
        """
        Getter for property: ( NXOpen.IBaseCurve) Curve
         Returns the CURVE used for creating the location.  
          
                        If the location type is not curve, this method will raise an error.   
         
        """
        pass
    @Curve.setter
    def Curve(self, curve: NXOpen.IBaseCurve):
        """
        Setter for property: ( NXOpen.IBaseCurve) Curve
         Returns the CURVE used for creating the location.  
          
                        If the location type is not curve, this method will raise an error.   
         
        """
        pass
import NXOpen
class Damper(IConnection): 
    """ Damper connection. Use this interface to setget properties and parameters of the Damper connection.  """
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @property
    def RxViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RxViscousDampingConstant
         Returns the RX viscous damping constant   
            
         
        """
        pass
    @property
    def RyViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RyViscousDampingConstant
         Returns the RY viscous damping constant   
            
         
        """
        pass
    @property
    def RzViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzViscousDampingConstant
         Returns the RZ viscous damping constant   
            
         
        """
        pass
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchConeAngle
         Returns the search cone angle   
            
         
        """
        pass
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchRange
         Returns the search range   
            
         
        """
        pass
    @property
    def XViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XViscousDampingConstant
         Returns the X viscous damping constant   
            
         
        """
        pass
    @property
    def YViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YViscousDampingConstant
         Returns the Y viscous damping constant   
            
         
        """
        pass
    @property
    def ZViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZViscousDampingConstant
         Returns the Z viscous damping constant   
            
         
        """
        pass
class DiameterType(Enum):
    """
    Members Include: 
     |Undefined|  Undefined diameter type 
     |User|  User defined diameter 
     |Formula|  Formula defined diameter 
     |TableFile|  Table defined diameter 
     |FlangeHoleDetection|  Flange hole defined diameter 

    """
    Undefined: int
    User: int
    Formula: int
    TableFile: int
    FlangeHoleDetection: int
    @staticmethod
    def ValueOf(value: int) -> DiameterType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiscretizationMethod(Enum):
    """
    Members Include: 
     |StepLength|  Discretize the line using step length 
     |NumberOfPoints|  Discretize the line using the total number of points 

    """
    StepLength: int
    NumberOfPoints: int
    @staticmethod
    def ValueOf(value: int) -> DiscretizationMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DofCombination(Enum):
    """
    Members Include: 
     |UserDefined|  User defined combination for all DOFs 
     |Fixed|  DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 fixed, DOF5 fixed, DOF6 fixed 
     |Spherical|  DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 free,  DOF6 free 
     |Inplane|  DOF1 fixed, DOF2 free,  DOF3 free,  DOF4 free,  DOF5 free,  DOF6 free 
     |Slider|  DOF1 free,  DOF2 fixed, DOF3 fixed, DOF4 fixed, DOF5 fixed, DOF6 fixed 
     |Revolute|  DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 fixed, DOF6 fixed 
     |Cylindrical|  DOF1 free,  DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 fixed, DOF6 fixed 
     |Universal|  DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 fixed, DOF6 free 
     |SliderUniversal|  DOF1 free,  DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 fixed, DOF6 free 
     |Inline|  DOF1 free,  DOF2 fixed, DOF3 fixed, DOF4 free,  DOF5 free, DOF6 free 

    """
    UserDefined: int
    Fixed: int
    Spherical: int
    Inplane: int
    Slider: int
    Revolute: int
    Cylindrical: int
    Universal: int
    SliderUniversal: int
    Inline: int
    @staticmethod
    def ValueOf(value: int) -> DofCombination:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DofType(Enum):
    """
    Members Include: 
     |Free|  The DOF is not constrained 
     |Fixed|  The DOF is fixed 

    """
    Free: int
    Fixed: int
    @staticmethod
    def ValueOf(value: int) -> DofType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Dof(Enum):
    """
    Members Include: 
     |X|  X Translation degree of freedom 
     |Y|  Y Translation degree of freedom 
     |Z|  Z Translation degree of freedom 
     |Rx|  X Rotation degree of freedom 
     |Ry|  Y Rotation degree of freedom 
     |Rz|  Z Rotation degree of freedom 

    """
    X: int
    Y: int
    Z: int
    Rx: int
    Ry: int
    Rz: int
    @staticmethod
    def ValueOf(value: int) -> Dof:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class ElementCollection(NXOpen.TaggedObjectCollection): 
    """  Element collection provides methods to manage CAE.Connections.Element objects  """
    @overload
    def Create(self, elementType: ElementType, name: str, connections: List[IConnection]) -> Element:
        """
         Creates a NXOpen.CAE.Connections.Element
         Returns element ( Element NXOpen.CAE): .
        """
        pass
    @overload
    def Create(self, elementType: ElementType, connectionType: ConnectionType, name: str) -> Element:
        """
         Creates a NXOpen.CAE.Connections.Element
         Returns element ( Element NXOpen.CAE): .
        """
        pass
class ElementStatusType(Enum):
    """
    Members Include: 
     |Invalid|  Invalid 
     |NotUpdated|  Not updated 
     |Updated|  Updated 

    """
    Invalid: int
    NotUpdated: int
    Updated: int
    @staticmethod
    def ValueOf(value: int) -> ElementStatusType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ElementType(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |EHex8|  Hex8 
     |EHex8Spider|  Hex8 + Spider 
     |E1d|  1D 
     |E1DSpider|  1D + Spider 
     |ESpider|  Spider 
     |EBushing|  Bushing Elm 
     |ESpring|  Spring Elm 
     |EDamper|  Damper Elm 
     |ERigid|  Rigid Elm 
     |EKinematic|  Kinematic Elm 
     |ERigidConnector|  Rigid Connector 
     |ERigidRigidConnector|  Rigid Connector - Rigid Connector 
     |EInterpolationSpider|  Interpolation + Spider 
     |EMassRigidSpider|  Concentrated Mass + Rigid Spider 
     |EMassInterpolationSpider|  Concentrated Mass + Interpolation Spider 
     |EScalarSpringRigidSpider|  Scalar Spring + Rigid Spider 
     |EScalarSpringRigidInterpolationSpider|  Scalar Spring + Rigid Spider + Interpolation Spider 
     |EJoint|  Joint Elm 
     |EJointInterpolation|  Joint Interpolation 
     |EBeamRigidSpider|  Beam + Rigid Spider 
     |EBar|  Bar + Rigid Spider 
     |EBarInterpolationSpider|  Bar + Interpolation Spider 
     |ECbear2Fou3InterpolationSpider|  CBEAR2 + FOU3 + Interpolation Spider 
     |ECbear2RigidSpider|  CBear2 + Rbe2 
     |ECbush2RigidSpider|  CBush2 + Rbe2 
     |EBeamSpider|  Beam Spider 
     |ECbush2Fou3InterpolationSpider|  CBUSH2 + FOU3 + Interpolation Spider 
     |EConstrainedJointMPCSpider|  Constrained Joint + MPC Spider 
     |EMassFou3InterpolationSpider|  Concentrated Mass + FOU3 + Interpolation Spider 
     |EFou3InterpolationSpider|  FOU3 + Interpolation Spider 
     |EBeam|  Beam 
     |ECWeld|  CWeld 
     |EClinkCbear2RigidSpider|  CLINK + CBEAR2 + RBE2 
     |EClinkCbush2RigidSpider|  Clink + CBUSH2 +RBE2 
     |EClinkBarRigidSpider|  Clink + CBAR + RBE2 
     |EClinkBeamRigidSpider|  Clink + CBEAM + RBE2 
     |EClinkFou3|  Clink + FOU3 
     |EQuad4InterpolationSpider|  Quad4 + Interpolation Spider 

    """
    NotSet: int
    EHex8: int
    EHex8Spider: int
    E1d: int
    E1DSpider: int
    ESpider: int
    EBushing: int
    ESpring: int
    EDamper: int
    ERigid: int
    EKinematic: int
    ERigidConnector: int
    ERigidRigidConnector: int
    EInterpolationSpider: int
    EMassRigidSpider: int
    EMassInterpolationSpider: int
    EScalarSpringRigidSpider: int
    EScalarSpringRigidInterpolationSpider: int
    EJoint: int
    EJointInterpolation: int
    EBeamRigidSpider: int
    EBar: int
    EBarInterpolationSpider: int
    ECbear2Fou3InterpolationSpider: int
    ECbear2RigidSpider: int
    ECbush2RigidSpider: int
    EBeamSpider: int
    ECbush2Fou3InterpolationSpider: int
    EConstrainedJointMPCSpider: int
    EMassFou3InterpolationSpider: int
    EFou3InterpolationSpider: int
    EBeam: int
    ECWeld: int
    EClinkCbear2RigidSpider: int
    EClinkCbush2RigidSpider: int
    EClinkBarRigidSpider: int
    EClinkBeamRigidSpider: int
    EClinkFou3: int
    EQuad4InterpolationSpider: int
    @staticmethod
    def ValueOf(value: int) -> ElementType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.CAE
class Element(NXOpen.NXObject): 
    """  This is the class to access a connection element  """
    @property
    def IsCompatibleType(self) -> bool:
        """
        Getter for property: (bool) IsCompatibleType
         Returns the compatibility of the element
                        (whether it accepts compatible or incompatible meshes)
                      
            
         
        """
        pass
    @property
    def Manual(self) -> bool:
        """
        Getter for property: (bool) Manual
         Returns the flag telling if the connection element is set up manually.  
          
                      
         
        """
        pass
    @Manual.setter
    def Manual(self, manual: bool):
        """
        Setter for property: (bool) Manual
         Returns the flag telling if the connection element is set up manually.  
          
                      
         
        """
        pass
    @property
    def NodeSelectionMethod(self) -> SeamWeldNodeSelectionMethod:
        """
        Getter for property: ( SeamWeldNodeSelectionMethod NXOpen.CAE) NodeSelectionMethod
         Returns the node selection method.  
           To be used when connection element has been set up manually ( NXOpen::CAE::Connections::Element::Manual  is true).
                      
         
        """
        pass
    @NodeSelectionMethod.setter
    def NodeSelectionMethod(self, method: SeamWeldNodeSelectionMethod):
        """
        Setter for property: ( SeamWeldNodeSelectionMethod NXOpen.CAE) NodeSelectionMethod
         Returns the node selection method.  
           To be used when connection element has been set up manually ( NXOpen::CAE::Connections::Element::Manual  is true).
                      
         
        """
        pass
    @property
    def PropertyTable(self) -> NXOpen.CAE.PropertyTable:
        """
        Getter for property: ( NXOpen.CAE.PropertyTable) PropertyTable
         Returns the property table.  
             
         
        """
        pass
    @property
    def Status(self) -> ElementStatusType:
        """
        Getter for property: ( ElementStatusType NXOpen.CAE) Status
         Returnsthe status of the element
                      
            
         
        """
        pass
    @property
    def Type(self) -> ElementType:
        """
        Getter for property: ( ElementType NXOpen.CAE) Type
         Returnsthe type of the element
                      
            
         
        """
        pass
    @Type.setter
    def Type(self, type: ElementType):
        """
        Setter for property: ( ElementType NXOpen.CAE) Type
         Returnsthe type of the element
                      
            
         
        """
        pass
    def AddConnections(self, connections: List[IConnection]) -> None:
        """
         Adds connections to this element
                    
        """
        pass
    def GenerateElements(self) -> None:
        """
         Mesh the Connection Element.
                    
        """
        pass
    def GetConnections(self) -> List[IConnection]:
        """
         Gets connections from this element
                    
         Returns connections ( IConnection List[NXOpen.C): .
        """
        pass
    def GetElementGroups(self) -> List[NXOpen.CAE.CaeGroup]:
        """
         Get the manual element groups. To be used when connection element has been set up manually (NXOpen.CAE.Connections.Element.Manual is true).
                    
         Returns groups ( NXOpen.CAE.CaeGroup Li): .
        """
        pass
    def GetElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Get the manual elements. To be used when connection element has been set up manually (NXOpen.CAE.Connections.Element.Manual is true).
                    
         Returns elems ( NXOpen.CAE.FEElement Li): .
        """
        pass
    def GetGeneratedElementsOfConnection(self, connection: IConnection) -> List[NXOpen.CAE.FEElement]:
        """
         Get the elements generated for a given CAE.Connections.IConnection meshed by this CAE.Connections.Element.
                    
         Returns elems ( NXOpen.CAE.FEElement Li): .
        """
        pass
    def GetGeneratedElementsOfConnectionAtLocation(self, connection: IConnection, indexOfLocation: int, indexOfDefinitionInLocation: int) -> List[NXOpen.CAE.FEElement]:
        """
         Get the elements generated at a given location of a CAE.Connections.IConnection meshed by this CAE.Connections.Element.
                        Current version does not support CAE.Connections.Bolt and nodal (CAE.Connections.Spring, CAE.Connections.Damper, 
                        CAE.Connections.Bushing, CAE.Connections.Rigid, CAE.Connections.Kinematic) connections.
                    
         Returns elems ( NXOpen.CAE.FEElement Li): .
        """
        pass
    def GetGeneratedNodesOfConnection(self, connection: IConnection) -> List[NXOpen.CAE.FENode]:
        """
         Get the nodes generated for a given CAE.Connections.IConnection meshed by this CAE.Connections.Element.
                    
         Returns nodes ( NXOpen.CAE.FENode Li): .
        """
        pass
    def GetNodeGroups(self) -> List[NXOpen.CAE.CaeGroup]:
        """
         Get the manual node groups. To be used when connection element has been set up manually (NXOpen.CAE.Connections.Element.Manual is true).
                    
         Returns groups ( NXOpen.CAE.CaeGroup Li): .
        """
        pass
    def GetNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Get the manual nodes. To be used when connection element has been set up manually (NXOpen.CAE.Connections.Element.Manual is true).
                    
         Returns nodes ( NXOpen.CAE.FENode Li): .
        """
        pass
    def MarkAsModifiedByPropertyTable(self) -> None:
        """
         Mark the Connection Element as changed. To be used when the Property Table has been modified before calling NXOpen.CAE.Connections.Element.GenerateElements.
                    
        """
        pass
    def RemoveConnections(self, connections: List[IConnection]) -> None:
        """
         Removes a connection from this element. This does not deletedestroy the connection, instead
                        this element will no longer keep a reference to the connection.
                    
        """
        pass
    def SetElementGroups(self, groups: List[NXOpen.CAE.CaeGroup]) -> None:
        """
         Set the manual element groups. To be used when connection element has been set up manually (NXOpen.CAE.Connections.Element.Manual is true).
                    
        """
        pass
    def SetElements(self, elems: List[NXOpen.CAE.FEElement]) -> None:
        """
         Set the manual elements. To be used when connection element has been set up manually (NXOpen.CAE.Connections.Element.Manual is true).
                    
        """
        pass
    def SetNodeGroups(self, groups: List[NXOpen.CAE.CaeGroup]) -> None:
        """
         Set the manual node groups. To be used when connection element has been set up manually (NXOpen.CAE.Connections.Element.Manual is true).
                    
        """
        pass
    def SetNodes(self, nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Set the manual nodes. To be used when connection element has been set up manually (NXOpen.CAE.Connections.Element.Manual is true).
                    
        """
        pass
import NXOpen.CAE
class FeEdgesLocation(Location): 
    """  Location interface. This defines connection locations with common properties like coordinates.  """
    def GetFeEdges(self) -> List[NXOpen.CAE.FEElemEdge]:
        """
         Retrieve location edges. 
         Returns edges ( NXOpen.CAE.FEElemEdge Li):  Edges used for location .
        """
        pass
    def SetFeEdges(self, edges: List[NXOpen.CAE.FEElemEdge]) -> None:
        """
         Add location edges. 
        """
        pass
import NXOpen
import NXOpen.CAE
class Folder(NXOpen.NXObject): 
    """  The Folder class offers a way to create a hierarchy of connections and sub-folders  """
    @property
    def Parent(self) -> Folder:
        """
        Getter for property: ( Folder NXOpen.CAE) Parent
         Returns the parent folder   
            
         
        """
        pass
    def AddFolder(self, subfolder: Folder) -> None:
        """
         Add a subfolder to this folder. The subfolder is moved if found in other folder. 
        """
        pass
    def CloneConnection(self, originalConnection: IConnection, newConnectionName: str) -> IConnection:
        """
         Clone a CAE.Connections.IConnection in the same folder of the specified connection 
         Returns newConnection ( IConnection NXOpen.CAE):  the created connection .
        """
        pass
    def CreateConnection(self, type: ConnectionType, name: str) -> IConnection:
        """
         Create a CAE.Connections.IConnection in this folder of the specified type with the specified name 
         Returns connection ( IConnection NXOpen.CAE):  the created connection .
        """
        pass
    def CreateFolder(self, name: str) -> Folder:
        """
         Creates a CAE.Connections.Folder in this folder with the specified name 
         Returns folder ( Folder NXOpen.CAE):  the created CAE.Connections.Folder .
        """
        pass
    def CreateSpotWeldConnectionFromWcdFile(self, file: str, matfile: str, pDbData: ConnectionDBItemData) -> List[SpotWeld]:
        """
         Create CAE.Connections.SpotWeld connections in the current CAE.Connections.Folder
                    using connection data imported from a WCD file. This method allows user to create a spotweld connection specifically for composer application 
         Returns connections ( SpotWeld List[NXOpen.C):  the created connections .
        """
        pass
    def DeleteObjects(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Delete CAE.Connections.IConnection or CAE.Connections.Folder instances. Use this to avoid performance issue in particular cases. 
        """
        pass
    def DetectConnections(self, propertyList: NXOpen.CAE.CaeDataContainer) -> List[IConnection]:
        """
         Create CAE.Connections.IConnection connections in the current CAE.Connections.Folder
                    using connection auto detect.  
         Returns connections ( IConnection List[NXOpen.C):  the created connections .
        """
        pass
    def ExportConnectionsToXMcf(self, connections: List[IConnection], propertyList: NXOpen.CAE.CaeDataContainer) -> None:
        """
         Export CAE.Connections.IConnection connections in the current CAE.Connections.Folder
                    to a xMCF file.  
        """
        pass
    def ExportSpotWeldConnectionsToWcdFile(self, filePath: str, outputLength: NXOpen.Unit, connections: List[IConnection]) -> None:
        """
         Export CAE.Connections.SpotWeld connections in the current CAE.Connections.Folder
                    to a WCD file.  
        """
        pass
    def GetAllConnections(self) -> List[IConnection]:
        """
         Get all the connections under this folder and its descendant folders 
         Returns connections ( IConnection List[NXOpen.C):  all connections under this folder and its descendants .
        """
        pass
    def GetChildFolders(self) -> List[Folder]:
        """
         Get the child folders 
         Returns children ( Folder List[NXOpen.C):  child folders.
        """
        pass
    def GetConnections(self) -> List[IConnection]:
        """
         Get the connections 
         Returns connections ( IConnection List[NXOpen.C):  connections found in folder .
        """
        pass
    def ImportConnectionsFromMcf(self, file: str, inputFileUnit: NXOpen.Unit) -> List[IConnection]:
        """
         Create CAE.Connections.IConnection connections in the current CAE.Connections.Folder 
                    using connection data imported from a MCF file.  
         Returns connections ( IConnection List[NXOpen.C):  the created connections .
        """
        pass
    def ImportConnectionsFromXMcf(self, propertyList: NXOpen.CAE.CaeDataContainer) -> List[IConnection]:
        """
         Create CAE.Connections.IConnection connections in the current CAE.Connections.Folder
                    using connection data imported from a xMCF file.  
         Returns connections ( IConnection List[NXOpen.C):  the created connections .
        """
        pass
    def ImportLumpedMassFromInterchangeData(self, lengthUnit: NXOpen.Unit, massUnit: NXOpen.Unit, reportErrors: bool, iConnections: List[LMIEConnection]) -> List[LumpedMass]:
        """
         Create CAE.Connections.LumpedMass connection in the current CAE.Connections.Folder
                    using lumped mass intermediate representation imported from an external file.  
         Returns oConnections ( LumpedMass List[NXOpen.C):  The intermediate connection representations .
        """
        pass
    def ImportSpotWeldFromWcdWithHeightAndMaterial(self, file: str, inputFileUnit: NXOpen.Unit, heightType: HeightType, heightValue: float, useInputFileMaterial: bool, userDefinedMaterialType: MaterialType, userDefinedMaterial: NXOpen.PhysicalMaterial) -> List[SpotWeld]:
        """
         Create CAE.Connections.SpotWeld connections in the current CAE.Connections.Folder
                    using connection data imported from a WCD file. This method allows user to set the height value and material for the Spot weld 
         Returns connections ( SpotWeld List[NXOpen.C):  the created connections .
        """
        pass
    def MoveConnectionsToThisFolder(self, connections: List[IConnection]) -> None:
        """
         Add an array of connections to this folder. The connections are removed from the previous parent folder. 
        """
        pass
import NXOpen.CAE
class GroupLocation(Location): 
    """  This defines Group Location used by Universal Connections.  """
    @property
    def Group(self) -> NXOpen.CAE.CaeGroup:
        """
        Getter for property: ( NXOpen.CAE.CaeGroup) Group
         Returns the Group used for creating the location.  
          
                        If the location type is not a Group, this method will raise an error.   
         
        """
        pass
    @Group.setter
    def Group(self, group: NXOpen.CAE.CaeGroup):
        """
        Setter for property: ( NXOpen.CAE.CaeGroup) Group
         Returns the Group used for creating the location.  
          
                        If the location type is not a Group, this method will raise an error.   
         
        """
        pass
class HeadDiameterType(Enum):
    """
    Members Include: 
     |User|  User defined diameter 
     |FactorOfDiameter|  User defined relationship with bolt diameter 

    """
    User: int
    FactorOfDiameter: int
    @staticmethod
    def ValueOf(value: int) -> HeadDiameterType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class HeightType(Enum):
    """
    Members Include: 
     |Undefined|  Undefined height type, used for connections that don't use this parameter 
     |User|  User defined thickness 
     |MeanOfFlangesThickness|  Mean of flanges thickness 
     |DistanceBetweenFlanges|  Distance between flanges 
     |DistanceBetweenFlangesMeanOfFlangesThickness|  Distance between flanges - Mean of flanges thickness 
     |DistanceBetweenFlangesMaxOfFlangesThickness|  Distance between flanges - Max of flanges thickness 
     |DistanceBetweenFlangesAndMeanOfFlangesThickness|  Distance between flanges + Mean of the Flange Thickness 
     |SumOfFlangesThickness|  Sum of the Flange Thickness 

    """
    Undefined: int
    User: int
    MeanOfFlangesThickness: int
    DistanceBetweenFlanges: int
    DistanceBetweenFlangesMeanOfFlangesThickness: int
    DistanceBetweenFlangesMaxOfFlangesThickness: int
    DistanceBetweenFlangesAndMeanOfFlangesThickness: int
    SumOfFlangesThickness: int
    @staticmethod
    def ValueOf(value: int) -> HeightType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class IBushingType(NXOpen.INXObject): 
    """  This class represents an Interface to the Bushing type.  """
    @property
    @abstractmethod
    def BushingType(self) -> BushingType:
        """
        Getter for property: ( BushingType NXOpen.CAE) BushingType
         Returns the bushing type   
            
         
        """
        pass
    @BushingType.setter
    def BushingType(self, bushingType: BushingType):
        """
        Setter for property: ( BushingType NXOpen.CAE) BushingType
         Returns the bushing type   
            
         
        """
        pass
import NXOpen
class IConnection(NXOpen.DisplayableObject): 
    """  This class represents an interface to a connection object.  """
    @property
    def HasConnectionElement(self) -> bool:
        """
        Getter for property: (bool) HasConnectionElement
         Returnsthe connection is part or not of a mesh object
                      
            
         
        """
        pass
    @property
    def State(self) -> UniversalConnectionState:
        """
        Getter for property: ( UniversalConnectionState NXOpen.CAE) State
         Returnsthe status of the connection
                      
            
         
        """
        pass
    @property
    def UserDescription(self) -> str:
        """
        Getter for property: (str) UserDescription
         Returns the connection user description   
            
         
        """
        pass
    @UserDescription.setter
    def UserDescription(self, description: str):
        """
        Setter for property: (str) UserDescription
         Returns the connection user description   
            
         
        """
        pass
import NXOpen
class ICsys(NXOpen.INXObject): 
    """  This class represents an Interface to the Connection Csys.  """
    @property
    @abstractmethod
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @property
    @abstractmethod
    def CsysType(self) -> CsysType:
        """
        Getter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @abstractmethod
    def GetSupportedCsysTypes(self) -> List[CsysType]:
        """
         Gets supported csys types of connection. 
         Returns types ( CsysType List[NXOpen.C):  Supported CSys Types .
        """
        pass
import NXOpen
import NXOpen.Fields
class ICylindricalStiffnessDynamic(NXOpen.INXObject): 
    """  This class represents an Interface to the Cylindrical Stiffness dynamic.  """
    @property
    @abstractmethod
    def RCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RCylindricalStiffnessDynamic
         Returns the R cylindrical stiffness dynamic   
            
         
        """
        pass
    @RCylindricalStiffnessDynamic.setter
    def RCylindricalStiffnessDynamic(self, rDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RCylindricalStiffnessDynamic
         Returns the R cylindrical stiffness dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def RrCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrCylindricalStiffnessDynamic
         Returns the RR cylindrical stiffness dynamic   
            
         
        """
        pass
    @RrCylindricalStiffnessDynamic.setter
    def RrCylindricalStiffnessDynamic(self, rrDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrCylindricalStiffnessDynamic
         Returns the RR cylindrical stiffness dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzCylindricalStiffnessDynamic
         Returns the RZ cylindrical stiffness dynamic   
            
         
        """
        pass
    @RzCylindricalStiffnessDynamic.setter
    def RzCylindricalStiffnessDynamic(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzCylindricalStiffnessDynamic
         Returns the RZ cylindrical stiffness dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZCylindricalStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZCylindricalStiffnessDynamic
         Returns the Z cylindrical stiffness dynamic   
            
         
        """
        pass
    @ZCylindricalStiffnessDynamic.setter
    def ZCylindricalStiffnessDynamic(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZCylindricalStiffnessDynamic
         Returns the Z cylindrical stiffness dynamic   
            
         
        """
        pass
import NXOpen
class ICylindricalStiffness(NXOpen.INXObject): 
    """  This class represents an Interface to the Cylindrical stiffness.  """
    @property
    @abstractmethod
    def RCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RCylindricalStiffnessConstant
         Returns the R cylindrical stiffness constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def RrCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RrCylindricalStiffnessConstant
         Returns the RR cylindrical stiffness constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzCylindricalStiffnessConstant
         Returns the RZ cylindrical stiffness constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZCylindricalStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZCylindricalStiffnessConstant
         Returns the Z cylindrical stiffness constant   
            
         
        """
        pass
import NXOpen
import NXOpen.Fields
class ICylindricalStructuralDampingDynamic(NXOpen.INXObject): 
    """  This class represents an Interface to the CylindricalStructuralDamping dynamic.  """
    @property
    @abstractmethod
    def RCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RCylindricalStructuralDampingDynamic
         Returns the R cylindrical structural damping dynamic   
            
         
        """
        pass
    @RCylindricalStructuralDampingDynamic.setter
    def RCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RCylindricalStructuralDampingDynamic
         Returns the R cylindrical structural damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def RrCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrCylindricalStructuralDampingDynamic
         Returns the RR cylindrical structural damping dynamic   
            
         
        """
        pass
    @RrCylindricalStructuralDampingDynamic.setter
    def RrCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrCylindricalStructuralDampingDynamic
         Returns the RR cylindrical structural damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzCylindricalStructuralDampingDynamic
         Returns the RZ cylindrical structural damping dynamic   
            
         
        """
        pass
    @RzCylindricalStructuralDampingDynamic.setter
    def RzCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzCylindricalStructuralDampingDynamic
         Returns the RZ cylindrical structural damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZCylindricalStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZCylindricalStructuralDampingDynamic
         Returns the Z cylindrical structural damping dynamic   
            
         
        """
        pass
    @ZCylindricalStructuralDampingDynamic.setter
    def ZCylindricalStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZCylindricalStructuralDampingDynamic
         Returns the Z cylindrical structural damping dynamic   
            
         
        """
        pass
import NXOpen
class ICylindricalStructuralDamping(NXOpen.INXObject): 
    """  This class represents an Interface to the CylindricalStructuralDamping constants.  """
    @property
    @abstractmethod
    def RCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RCylindricalStructuralDampingConstant
         Returns the R cylindrical structural damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def RrCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RrCylindricalStructuralDampingConstant
         Returns the RR structural damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzCylindricalStructuralDampingConstant
         Returns the RZ structural damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZCylindricalStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZCylindricalStructuralDampingConstant
         Returns the Z cylindrical structural damping constant   
            
         
        """
        pass
import NXOpen
import NXOpen.Fields
class ICylindricalViscousDampingDynamic(NXOpen.INXObject): 
    """  This class represents an Interface to the CylindricalViscousDamping dynamic.  """
    @property
    @abstractmethod
    def RCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RCylindricalViscousDampingDynamic
         Returns the R cylindrical viscous damping dynamic   
            
         
        """
        pass
    @RCylindricalViscousDampingDynamic.setter
    def RCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RCylindricalViscousDampingDynamic
         Returns the R cylindrical viscous damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def RrCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrCylindricalViscousDampingDynamic
         Returns the RR cylindrical viscous damping dynamic   
            
         
        """
        pass
    @RrCylindricalViscousDampingDynamic.setter
    def RrCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrCylindricalViscousDampingDynamic
         Returns the RR cylindrical viscous damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzCylindricalViscousDampingDynamic
         Returns the RZ cylindrical viscous damping dynamic   
            
         
        """
        pass
    @RzCylindricalViscousDampingDynamic.setter
    def RzCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzCylindricalViscousDampingDynamic
         Returns the RZ cylindrical viscous damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZCylindricalViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZCylindricalViscousDampingDynamic
         Returns the Z cylindrical viscous damping dynamic   
            
         
        """
        pass
    @ZCylindricalViscousDampingDynamic.setter
    def ZCylindricalViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZCylindricalViscousDampingDynamic
         Returns the Z cylindrical viscous damping dynamic   
            
         
        """
        pass
import NXOpen
class ICylindricalViscousDamping(NXOpen.INXObject): 
    """  This class represents an Interface to the CylindricalViscousDamping constants.  """
    @property
    @abstractmethod
    def RCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RCylindricalViscousDampingConstant
         Returns the R cylindrical viscous damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def RrCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RrCylindricalViscousDampingConstant
         Returns the RR cylindrical viscous damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzCylindricalViscousDampingConstant
         Returns the RZ cylindrical viscous damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZCylindricalViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZCylindricalViscousDampingConstant
         Returns the Z cylindrical viscous damping constant   
            
         
        """
        pass
import NXOpen
class IDiameter(NXOpen.INXObject): 
    """  This class represents an Interface to the Diameter parameters.  """
    @property
    @abstractmethod
    def Coefficient(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Coefficient
         Returns the coefficient for formula defined diameter   
            
         
        """
        pass
    @property
    @abstractmethod
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the connection diameter   
            
         
        """
        pass
    @property
    @abstractmethod
    def DiameterType(self) -> DiameterType:
        """
        Getter for property: ( DiameterType NXOpen.CAE) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: ( DiameterType NXOpen.CAE) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    @property
    @abstractmethod
    def TableFile(self) -> str:
        """
        Getter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    @abstractmethod
    def GetManualAdjustment(self) -> bool:
        """
         Gets manual adjustent state. 
         Returns state (bool): .
        """
        pass
    @abstractmethod
    def GetManualAdjustmentFactor(self) -> NXOpen.Expression:
        """
         Gets manual adjustent factor. 
         Returns factor ( NXOpen.Expression): .
        """
        pass
    @abstractmethod
    def GetSupportedDiameterTypes(self) -> List[DiameterType]:
        """
         Gets supported diameter types of connection. 
         Returns types ( DiameterType List[NXOpen.C):  Supported CSys Types .
        """
        pass
    @abstractmethod
    def SetManualAdjustment(self, state: bool) -> None:
        """
         Sets manual adjustent state. 
        """
        pass
import NXOpen
class IDofCombination(NXOpen.INXObject): 
    """  This class represents an interface to the connection's degrees of freedom combination.  """
    @property
    @abstractmethod
    def DofCombination(self) -> DofCombination:
        """
        Getter for property: ( DofCombination NXOpen.CAE) DofCombination
         Returns the degrees of freedom combination type   
            
         
        """
        pass
    @DofCombination.setter
    def DofCombination(self, type: DofCombination):
        """
        Setter for property: ( DofCombination NXOpen.CAE) DofCombination
         Returns the degrees of freedom combination type   
            
         
        """
        pass
import NXOpen
class IDof(NXOpen.INXObject): 
    """  This class represents an interface to the connection's degrees of freedom.  """
    @abstractmethod
    def GetDof(self, dof: Dof) -> DofType:
        """
         Get the specified degrees of freedom  
         Returns type ( DofType NXOpen.CAE): .
        """
        pass
    @abstractmethod
    def SetDof(self, dof: Dof, type: DofType) -> None:
        """
         Set the specified degrees of freedom  
        """
        pass
import NXOpen
class IFlangesContainer(NXOpen.INXObject): 
    """  This interface offers access to the flanges of a connection (SpotWeld for example).
        The flanges are used for specifying the connecting surfaces of the connection. Each flange can have one or more entities like meshes, elements etc.
          """
    @property
    @abstractmethod
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @abstractmethod
    def AddFlangeEntities(self, flangeIndex: int, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add entities to flange. Changes are not applied till an update is performed by calling Update.DoUpdate 
        """
        pass
    @abstractmethod
    def GetFlangeEntities(self, flangeIndex: int) -> List[NXOpen.TaggedObject]:
        """
         Gets entities from flange. These can be meshes, elements, groups. 
         Returns entities ( NXOpen.TaggedObject Li):  Flange entities .
        """
        pass
    @abstractmethod
    def GetMaxNumberOfFlanges(self) -> int:
        """
         Retrieve the max number of flanges supported by this connection 
         Returns number (int): .
        """
        pass
    @abstractmethod
    def GetMinNumberOfFlanges(self) -> int:
        """
         Retrieve the minimum number of flanges supported by this connection 
         Returns number (int): .
        """
        pass
    @abstractmethod
    def RemoveFlangeEntities(self, flangeIndex: int, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Remove entities from flange. Changes are not applied till an update is performed by calling Update.DoUpdate 
        """
        pass
import NXOpen
class IFriction(NXOpen.INXObject): 
    """  This class represents an Interface to the Friction constants.  """
    @property
    @abstractmethod
    def CharacteristicLengthRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CharacteristicLengthRadius
         Returns the radius characteristic length used by Revolute and Spherical Kinematic   
            
         
        """
        pass
    @property
    @abstractmethod
    def FrictionCoefficient(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FrictionCoefficient
         Returns the friction coefficient   
            
         
        """
        pass
    @property
    @abstractmethod
    def TighteningForce(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TighteningForce
         Returns the tightening force   
            
         
        """
        pass
    @property
    @abstractmethod
    def UseFriction(self) -> bool:
        """
        Getter for property: (bool) UseFriction
         Returns the flag indicating whether to use friction parameters or not   
            
         
        """
        pass
    @UseFriction.setter
    def UseFriction(self, useFriction: bool):
        """
        Setter for property: (bool) UseFriction
         Returns the flag indicating whether to use friction parameters or not   
            
         
        """
        pass
import NXOpen
class IHeight(NXOpen.INXObject): 
    """  This class represents an Interface to the Height parameters.  """
    @property
    @abstractmethod
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height value   
            
         
        """
        pass
    @property
    @abstractmethod
    def HeightType(self) -> HeightType:
        """
        Getter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @abstractmethod
    def GetSupportedHeightTypes(self) -> List[HeightType]:
        """
         Gets supported height types of connection. 
         Returns types ( HeightType List[NXOpen.C):  Supported CSys Types .
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Features
class IJoinDataContainer(NXOpen.INXObject): 
    """  This class represents an Interface to the Join Data Container.  """
    @abstractmethod
    def AddJoinData(self, feature: NXOpen.Features.Feature, component: NXOpen.Assemblies.Component) -> None:
        """
         Add a join data to the connection 
        """
        pass
    @abstractmethod
    def GetAllJoinFeatures(self) -> Tuple[List[NXOpen.Features.Feature], List[NXOpen.Assemblies.Component]]:
        """
         Get all join data features from the connection 
         Returns A tuple consisting of (features, components). 
         - features is:  NXOpen.Features.Feature Li. The join features .
         - components is:  NXOpen.Assemblies.Component Li. The CAD components of the join features .

        """
        pass
    @abstractmethod
    def GetJoinFeature(self, index: int) -> Tuple[NXOpen.Features.Feature, NXOpen.Assemblies.Component]:
        """
         Get a join data feature from the connection 
         Returns A tuple consisting of (feature, component). 
         - feature is:  NXOpen.Features.Feature. The join feature .
         - component is:  NXOpen.Assemblies.Component. The CAD component of the join feature .

        """
        pass
    @abstractmethod
    def GetNumberOfJoinData(self) -> int:
        """
         Get the number of join data from the connection 
         Returns numberOfJoinData (int):  The number of join data .
        """
        pass
    @abstractmethod
    def RemoveAllJoinData(self) -> None:
        """
         Remove all join data from the connection 
        """
        pass
    @abstractmethod
    def RemoveJoinData(self, feature: NXOpen.Features.Feature, component: NXOpen.Assemblies.Component) -> None:
        """
         Add a join data to the connection 
        """
        pass
    @abstractmethod
    def RemoveJoinDataByIndex(self, index: int) -> None:
        """
         Remove a join data from the connection 
        """
        pass
    @abstractmethod
    def SetJoinData(self, features: List[NXOpen.Features.Feature], components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Set the join data of the connection 
        """
        pass
    @abstractmethod
    def UnlinkJoinData(self) -> None:
        """
         Unlink all join data from the connection 
        """
        pass
import NXOpen
class ILineDiscretization(NXOpen.INXObject): 
    """  This class represents an Interface to the Diameter parameters.  """
    @property
    @abstractmethod
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @property
    @abstractmethod
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromStart
         Returns the line Discretization distance from start   
            
         
        """
        pass
    @property
    @abstractmethod
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceToEnd
         Returns the line Discretization distance to end   
            
         
        """
        pass
    @property
    @abstractmethod
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LengthStep
         Returns the line Discretization length step   
            
         
        """
        pass
    @property
    @abstractmethod
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxLengthStep
         Returns the line Discretization max length step   
            
         
        """
        pass
    @property
    @abstractmethod
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @property
    @abstractmethod
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @property
    @abstractmethod
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
import NXOpen
class ILineOffset(NXOpen.INXObject): 
    """  This class represents an Interface to the Diameter parameters.  """
    @abstractmethod
    def GetOffsetDistance(self, lindeDefinitionIndex: int) -> NXOpen.Expression:
        """
         Gets the line offset distance 
         Returns distance ( NXOpen.Expression): .
        """
        pass
    @abstractmethod
    def GetOffsetVector(self, lindeDefinitionIndex: int) -> NXOpen.Direction:
        """
         Gets the line offset vector 
         Returns offsetvector ( NXOpen.Direction): .
        """
        pass
    @abstractmethod
    def SetOffsetVector(self, lindeDefinitionIndex: int, offsetvector: NXOpen.Direction) -> None:
        """
         Sets the line offset vector 
        """
        pass
import NXOpen
class ILocationsContainer(NXOpen.INXObject): 
    """  This class represents an Interface to the Locations parameters.  """
    @abstractmethod
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> Location:
        """
         Convert a location to coordinates. The location is given by its index 
         Returns location ( Location NXOpen.CAE):  The created coordinates type location .
        """
        pass
    @abstractmethod
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> Location:
        """
         Get a node location to connection location list 
         Returns location ( Location NXOpen.CAE):  The location .
        """
        pass
    @abstractmethod
    def GetNumberOfDefinitions(self) -> int:
        """
         Gets the number of line offset definitions 
         Returns numberOfDefinitions (int):  The number of definitions .
        """
        pass
    @abstractmethod
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
        """
         Get a node location to connection location list 
         Returns number_of_locations (int):  The number of locations .
        """
        pass
    @abstractmethod
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        """
         Move the location by number of positions 
         Returns success (bool):  The operation result .
        """
        pass
    @abstractmethod
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
        """
         Remove a location from connection location list 
        """
        pass
import NXOpen
import NXOpen.CAE
class ILocationsMultiPointContainer(NXOpen.INXObject): 
    """  This class represents an Interface to the Multi Point Locations container.  """
    @abstractmethod
    def AddLocationSelectionRecipe(self, indexOfDefinition: int, selectionRecipe: NXOpen.CAE.SelectionRecipe) -> SelectionRecipeLocation:
        """
         Adds a Selection Recipe to connection location list 
         Returns location ( SelectionRecipeLocation NXOpen.CAE):  The created selection recipe type location .
        """
        pass
import NXOpen
import NXOpen.CAE
class ILocationsSinglePointContainer(NXOpen.INXObject): 
    """  This class represents an Interface to the Locations parameters.  """
    @abstractmethod
    def AddLocationCoordinates(self, indexOfDefinition: int, coordinates: NXOpen.Point3d) -> CoordinatesLocation:
        """
         Adds a coordinates location to connection location list 
         Returns location ( CoordinatesLocation NXOpen.CAE):  The created coordinates type location .
        """
        pass
    @abstractmethod
    def AddLocationNode(self, indexOfDefinition: int, node: NXOpen.CAE.FENode) -> NodeLocation:
        """
         Adds a node location to connection location list 
         Returns location ( NodeLocation NXOpen.CAE):  The node type location .
        """
        pass
    @abstractmethod
    def AddLocationPoint(self, indexOfDefinition: int, point: NXOpen.Point) -> PointLocation:
        """
         Adds a point location to connection location list 
         Returns location ( PointLocation NXOpen.CAE):  The created point type location .
        """
        pass
import NXOpen
import NXOpen.CAE
class ILocationsWithDirContainer(NXOpen.INXObject): 
    """  This class represents an Interface to the Locations parameters.  """
    @abstractmethod
    def AddLocationCoordinatesWithDirectionCoordinates(self, indexOfDefinition: int, point: NXOpen.Point, direction: NXOpen.Point) -> LocationWithDir:
        """
         Adds a coordinates location with direction definited by coordinates to connection location list 
         Returns location ( LocationWithDir NXOpen.CAE):  The created coordinates with direction type location .
        """
        pass
    @abstractmethod
    def AddLocationCoordinatesWithDirectionSelectionRecipes(self, indexOfDefinition: int, startSelectionRecipe: NXOpen.CAE.SelectionRecipe, endSelectionRecipe: NXOpen.CAE.SelectionRecipe) -> LocationWithDir:
        """
         Adds a coordinates location with direction definited by vector to connection location list 
         Returns location ( LocationWithDir NXOpen.CAE):  The created point with direction type location .
        """
        pass
    @abstractmethod
    def AddLocationCoordinatesWithDirectionVector(self, indexOfDefinition: int, masterPoint: NXOpen.Point, direction: NXOpen.Direction) -> LocationWithDir:
        """
         Adds a coordinates location with direction definited by vector to connection location list 
         Returns location ( LocationWithDir NXOpen.CAE):  The created point with direction type location .
        """
        pass
import NXOpen
import NXOpen.CAE
class ILocationsWithDiscretizationContainer(NXOpen.INXObject): 
    """  This class represents an Interface to the Locations With Discretization container.  """
    @abstractmethod
    def AddLocationCurve(self, indexOfDefinition: int, curve: NXOpen.IBaseCurve) -> CurveLocation:
        """
         Adds a curve location to connection location list 
         Returns location ( CurveLocation NXOpen.CAE):  The created curve type location .
        """
        pass
    @abstractmethod
    def AddLocationFeEdges(self, indexOfDefinition: int, edges: List[NXOpen.CAE.FEElemEdge]) -> FeEdgesLocation:
        """
         Adds Fe Edges to connection location list 
         Returns location ( FeEdgesLocation NXOpen.CAE):  The created edge group type location .
        """
        pass
    @abstractmethod
    def AddLocationGroup(self, indexOfDefinition: int, group: NXOpen.CAE.CaeGroup) -> GroupLocation:
        """
         Adds a group location to connection location list 
         Returns location ( GroupLocation NXOpen.CAE):  The created group type location .
        """
        pass
    @abstractmethod
    def AddLocationSeriesOfCoordinates(self, indexOfDefinition: int, coordinates: List[NXOpen.Point3d]) -> CoordinatesSeriesLocation:
        """
         Adds a series of coordinates location to connection location list 
         Returns location ( CoordinatesSeriesLocation NXOpen.CAE):  The coordinates series type location .
        """
        pass
    @abstractmethod
    def AddLocationSeriesOfNodes(self, indexOfDefinition: int, nodes: List[NXOpen.CAE.FENode]) -> NodeSeriesLocation:
        """
         Adds a series of nodes location to connection location list 
         Returns location ( NodeSeriesLocation NXOpen.CAE):  The node series type location .
        """
        pass
    @abstractmethod
    def AddLocationSeriesOfPoints(self, indexOfDefinition: int, points: List[NXOpen.Point]) -> PointSeriesLocation:
        """
         Adds a series of points location to connection location list 
         Returns location ( PointSeriesLocation NXOpen.CAE):  The point series type location .
        """
        pass
import NXOpen
class IMassBothTargets(NXOpen.INXObject): 
    """  This class represents an Interface to the Mass Both Target.  """
    @property
    @abstractmethod
    def IsMassOnBothTargets(self) -> bool:
        """
        Getter for property: (bool) IsMassOnBothTargets
         Returns the isMassOnBothTargets   
            
         
        """
        pass
    @IsMassOnBothTargets.setter
    def IsMassOnBothTargets(self, isMassOnBothTargets: bool):
        """
        Setter for property: (bool) IsMassOnBothTargets
         Returns the isMassOnBothTargets   
            
         
        """
        pass
import NXOpen
class IMassConnectivity(NXOpen.INXObject): 
    """  This class represents an Interface to the Lumped Mass panel connection parameters.  """
    @property
    @abstractmethod
    def ExpansionRadiusFactorTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExpansionRadiusFactorTolerance
         Returns the expansion radius factor   
            
         
        """
        pass
    @property
    @abstractmethod
    def ExpansionRadiusTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExpansionRadiusTolerance
         Returns the expansion radius   
            
         
        """
        pass
    @property
    @abstractmethod
    def MassConnectivityType(self) -> MassConnectivityType:
        """
        Getter for property: ( MassConnectivityType NXOpen.CAE) MassConnectivityType
         Returns the mass connection type   
            
         
        """
        pass
    @MassConnectivityType.setter
    def MassConnectivityType(self, type: MassConnectivityType):
        """
        Setter for property: ( MassConnectivityType NXOpen.CAE) MassConnectivityType
         Returns the mass connection type   
            
         
        """
        pass
    @property
    @abstractmethod
    def MaxDistanceTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDistanceTolerance
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    @property
    @abstractmethod
    def PanelSearchDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PanelSearchDistance
         Returns the panel search distance   
            
         
        """
        pass
    @property
    @abstractmethod
    def PanelSearchType(self) -> PanelSearchType:
        """
        Getter for property: ( PanelSearchType NXOpen.CAE) PanelSearchType
         Returns the panel search type  
            
         
        """
        pass
    @PanelSearchType.setter
    def PanelSearchType(self, type: PanelSearchType):
        """
        Setter for property: ( PanelSearchType NXOpen.CAE) PanelSearchType
         Returns the panel search type  
            
         
        """
        pass
    @property
    @abstractmethod
    def RingSearchType(self) -> RingSearchType:
        """
        Getter for property: ( RingSearchType NXOpen.CAE) RingSearchType
         Returns the search tolerance type  
            
         
        """
        pass
    @RingSearchType.setter
    def RingSearchType(self, type: RingSearchType):
        """
        Setter for property: ( RingSearchType NXOpen.CAE) RingSearchType
         Returns the search tolerance type  
            
         
        """
        pass
    @abstractmethod
    def AddPanels(self, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add panels 
        """
        pass
    @abstractmethod
    def GetPanels(self) -> List[NXOpen.TaggedObject]:
        """
         Gets panels 
         Returns entities ( NXOpen.TaggedObject Li):  Panels entities .
        """
        pass
    @abstractmethod
    def RemovePanels(self, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Remove panels 
        """
        pass
import NXOpen
class IMassInertia(NXOpen.INXObject): 
    """  This class represents an Interface to the Mass Inertia.  """
    @property
    @abstractmethod
    def InertiaXX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaXX
         Returns the inertia XX.  
             
         
        """
        pass
    @property
    @abstractmethod
    def InertiaYX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaYX
         Returns the inertia XY.  
             
         
        """
        pass
    @property
    @abstractmethod
    def InertiaYY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaYY
         Returns the inertia YY.  
             
         
        """
        pass
    @property
    @abstractmethod
    def InertiaZX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaZX
         Returns the inertia XZ.  
             
         
        """
        pass
    @property
    @abstractmethod
    def InertiaZY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaZY
         Returns the inertia YZ.  
             
         
        """
        pass
    @property
    @abstractmethod
    def InertiaZZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaZZ
         Returns the inertia ZZ.  
             
         
        """
        pass
import NXOpen
class IMassPhysicalParams(NXOpen.INXObject): 
    """  This class represents an Interface to the Mass Physical Params.  """
    @property
    @abstractmethod
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Mass
         Returns the mass value   
            
         
        """
        pass
import NXOpen
class IMassTarget(NXOpen.INXObject): 
    """  This class represents an Interface to the Lumped Mass target.  """
    @property
    @abstractmethod
    def Center(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) Center
         Returns the target center   
            
         
        """
        pass
    @Center.setter
    def Center(self, center: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) Center
         Returns the target center   
            
         
        """
        pass
    @property
    @abstractmethod
    def LocalSpiderCenterType(self) -> LocalSpiderCenterType:
        """
        Getter for property: ( LocalSpiderCenterType NXOpen.CAE) LocalSpiderCenterType
         Returns the local spider center type   
            
         
        """
        pass
    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, localSpiderCenterType: LocalSpiderCenterType):
        """
        Setter for property: ( LocalSpiderCenterType NXOpen.CAE) LocalSpiderCenterType
         Returns the local spider center type   
            
         
        """
        pass
    @property
    @abstractmethod
    def MassCenterType(self) -> MassCenterType:
        """
        Getter for property: ( MassCenterType NXOpen.CAE) MassCenterType
         Returns the mass center type   
            
         
        """
        pass
    @MassCenterType.setter
    def MassCenterType(self, massCenterType: MassCenterType):
        """
        Setter for property: ( MassCenterType NXOpen.CAE) MassCenterType
         Returns the mass center type   
            
         
        """
        pass
    @property
    @abstractmethod
    def MassDistributionType(self) -> MassDistributionType:
        """
        Getter for property: ( MassDistributionType NXOpen.CAE) MassDistributionType
         Returns the mass distribution type   
            
         
        """
        pass
    @MassDistributionType.setter
    def MassDistributionType(self, type: MassDistributionType):
        """
        Setter for property: ( MassDistributionType NXOpen.CAE) MassDistributionType
         Returns the mass distribution type   
            
         
        """
        pass
    @abstractmethod
    def AddSupportEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add entities to mass spider legs. 
                    Changes are not applied till an update is performed by calling Update.DoUpdate 
        """
        pass
    @abstractmethod
    def GetSupportEntities(self) -> List[NXOpen.TaggedObject]:
        """
         Gets entities from mass spider legs. 
                    These can be any combination of CAD (point, edge, face, body) or FE (node, edge, face, element and mesh) 
                    objects able to return nodes. 
         Returns entities ( NXOpen.TaggedObject Li):  Mass support entities .
        """
        pass
    @abstractmethod
    def RemoveSupportEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Remove entities from mass spider legs. 
                    Changes are not applied till an update is performed by calling Update.DoUpdate 
        """
        pass
    @abstractmethod
    def SetSupportEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add entities to mass spider legs. 
                    Changes are not applied till an update is performed by calling Update.DoUpdate 
        """
        pass
import NXOpen
class IMassType(NXOpen.INXObject): 
    """  This class represents an Interface to the Mass Type.  """
    @property
    @abstractmethod
    def MassTypeValue(self) -> MassType:
        """
        Getter for property: ( MassType NXOpen.CAE) MassTypeValue
         Returns the mass type   
            
         
        """
        pass
    @MassTypeValue.setter
    def MassTypeValue(self, type: MassType):
        """
        Setter for property: ( MassType NXOpen.CAE) MassTypeValue
         Returns the mass type   
            
         
        """
        pass
import NXOpen
class IMaterial(NXOpen.INXObject): 
    """  This class represents an Interface to the Material entity.  """
    @property
    @abstractmethod
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @abstractmethod
    def CanHaveNoMaterial(self) -> bool:
        """
         Use this function to check if the connection supports having no material 
         Returns value (bool): .
        """
        pass
    @abstractmethod
    def CanInheritMaterial(self) -> bool:
        """
         Use this function to check if the connection supports inherited material 
         Returns value (bool): .
        """
        pass
    @abstractmethod
    def IsInheritedMaterial(self) -> bool:
        """
         Use this function to check if the connection inherits material from flanges 
         Returns value (bool): .
        """
        pass
    @abstractmethod
    def SetInheritedMaterial(self) -> None:
        """
         Use this function to set inherited material to connection 
        """
        pass
import NXOpen
class INodalTargetCenterOption(NXOpen.INXObject): 
    """  This class represents an Interface to the Nodal Target Center Option.  """
    @property
    @abstractmethod
    def CenterType(self) -> NodalTargetCenterType:
        """
        Getter for property: ( NodalTargetCenterType NXOpen.CAE) CenterType
         Returns the target center type   
            
         
        """
        pass
    @CenterType.setter
    def CenterType(self, centerType: NodalTargetCenterType):
        """
        Setter for property: ( NodalTargetCenterType NXOpen.CAE) CenterType
         Returns the target center type   
            
         
        """
        pass
    @abstractmethod
    def GetAvailableTargetCenterTypes(self) -> List[NodalTargetCenterType]:
        """
         Get available center types
         Returns types ( NodalTargetCenterType List[NXOpen.C): .
        """
        pass
    @abstractmethod
    def IsCoincidentCenterTypeAllowed(self) -> bool:
        """
         Check if center type is allowed 
         Returns allowed (bool): .
        """
        pass
import NXOpen
class INodalTargetCenter(NXOpen.INXObject): 
    """  This class represents an Interface to the Connection Target.  """
    @property
    @abstractmethod
    def TargetCenter(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) TargetCenter
         Returns the target center   
            
         
        """
        pass
    @TargetCenter.setter
    def TargetCenter(self, center: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) TargetCenter
         Returns the target center   
            
         
        """
        pass
import NXOpen
class INodalTargetLegs(NXOpen.INXObject): 
    """  This class represents an Interface to the Connection Target.  """
    @abstractmethod
    def AddLegsEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add entities to target's group of points. 
                    Changes are not applied till an update is performed by calling Update.DoUpdate 
        """
        pass
    @abstractmethod
    def GetLegsEntities(self) -> List[NXOpen.TaggedObject]:
        """
         Gets entities from target's group of points. 
                    These can be any combination of CAD (point, edge, face, body) or FE (node, edge, face, element and mesh) 
                    objects able to return nodes. 
         Returns entities ( NXOpen.TaggedObject Li):  Legs entities .
        """
        pass
    @abstractmethod
    def RemoveLegsEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Remove entities from target's group of points. 
                    Changes are not applied till an update is performed by calling Update.DoUpdate 
        """
        pass
import NXOpen
import NXOpen.CAE
class INodalTargetLocalSpiderDefinition(NXOpen.INXObject): 
    """  This class represents an Interface to the Nodal Target Local Spider Definition.  """
    @property
    @abstractmethod
    def ExpansionRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExpansionRadius
         Returns the Expansion Radius   
            
         
        """
        pass
    @property
    @abstractmethod
    def ExpansionRadiusFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExpansionRadiusFactor
         Returns the Expansion Radius Factor   
            
         
        """
        pass
    @property
    @abstractmethod
    def LocalSpiderCenterType(self) -> LocalSpiderCenterType:
        """
        Getter for property: ( LocalSpiderCenterType NXOpen.CAE) LocalSpiderCenterType
         Returns the Local Spider Center type   
            
         
        """
        pass
    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, localSpiderCenterType: LocalSpiderCenterType):
        """
        Setter for property: ( LocalSpiderCenterType NXOpen.CAE) LocalSpiderCenterType
         Returns the Local Spider Center type   
            
         
        """
        pass
    @property
    @abstractmethod
    def MaxDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDistance
         Returns the Maximum Distance   
            
         
        """
        pass
    @property
    @abstractmethod
    def PanelSearchType(self) -> PanelSearchType:
        """
        Getter for property: ( PanelSearchType NXOpen.CAE) PanelSearchType
         Returns the Panel Search type   
            
         
        """
        pass
    @PanelSearchType.setter
    def PanelSearchType(self, panelSearchType: PanelSearchType):
        """
        Setter for property: ( PanelSearchType NXOpen.CAE) PanelSearchType
         Returns the Panel Search type   
            
         
        """
        pass
    @property
    @abstractmethod
    def RingSearchType(self) -> RingSearchType:
        """
        Getter for property: ( RingSearchType NXOpen.CAE) RingSearchType
         Returns the Ring Search type   
            
         
        """
        pass
    @RingSearchType.setter
    def RingSearchType(self, ringSearchType: RingSearchType):
        """
        Setter for property: ( RingSearchType NXOpen.CAE) RingSearchType
         Returns the Ring Search type   
            
         
        """
        pass
    @property
    @abstractmethod
    def SearchTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchTolerance
         Returns the Search Tolerance   
            
         
        """
        pass
    @abstractmethod
    def AddLocationMeshPoint(self, meshPoint: NXOpen.CAE.MeshPoint) -> MeshPointLocation:
        """
         Adds a mesh point location to the target locations list 
         Returns location ( MeshPointLocation NXOpen.CAE):  The created mesh point type location .
        """
        pass
    @abstractmethod
    def AddLocationNode(self, node: NXOpen.CAE.FENode) -> NodeLocation:
        """
         Adds a node location to the target locations list 
         Returns location ( NodeLocation NXOpen.CAE):  The node type location .
        """
        pass
    @abstractmethod
    def AddLocationPoint(self, point: NXOpen.Point) -> PointLocation:
        """
         Adds a point location to the target locations list 
         Returns location ( PointLocation NXOpen.CAE):  The created point type location .
        """
        pass
    @abstractmethod
    def AddLocationSelectionRecipe(self, selectionRecipe: NXOpen.CAE.SelectionRecipe) -> SelectionRecipeLocation:
        """
         Adds a Selection Recipe to the target locations list 
         Returns location ( SelectionRecipeLocation NXOpen.CAE):  The created selection recipe type location .
        """
        pass
    @abstractmethod
    def AddRegionsEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Add regions entities to the target. 
                    Changes are not applied till an update is performed by calling Update.DoUpdate 
        """
        pass
    @abstractmethod
    def GetLocation(self, indexOfLocation: int) -> Location:
        """
         Get a location from the target locations list 
         Returns location ( Location NXOpen.CAE):  The location .
        """
        pass
    @abstractmethod
    def GetNumberOfLocations(self) -> int:
        """
         Get the number of locations in the target 
         Returns number_of_locations (int):  The number of locations .
        """
        pass
    @abstractmethod
    def GetRegionsEntities(self) -> List[NXOpen.TaggedObject]:
        """
         Gets regions entities in the target. 
                    These can be any combination of CAD (point, edge, face, body) or FE (node, edge, face, element and mesh) 
                    objects able to return nodes. 
         Returns entities ( NXOpen.TaggedObject Li):  Legs entities .
        """
        pass
    @abstractmethod
    def RemoveLocation(self, indexOfLocation: int) -> None:
        """
         Remove a location from the target locations list 
        """
        pass
    @abstractmethod
    def RemoveRegionsEntities(self, entities: List[NXOpen.TaggedObject]) -> None:
        """
         Remove regions entities from the target. 
                    Changes are not applied till an update is performed by calling Update.DoUpdate 
        """
        pass
import NXOpen
class INodalTargetsContainer(NXOpen.INXObject): 
    """  This class represents an Interface to the Connection Target Container.  """
    @abstractmethod
    def GetTarget(self, index: int) -> NodalTarget:
        """
         Get target 
         Returns target ( NodalTarget NXOpen.CAE): .
        """
        pass
    @abstractmethod
    def SetTargetType(self, index: int, type: NodalTargetType) -> None:
        """
         Set the target type 
        """
        pass
    @abstractmethod
    def SwapTargets(self) -> None:
        """
         Swap targets 
        """
        pass
import NXOpen
class INodalTargetsPairing(NXOpen.INXObject): 
    """  This class represents an Interface to the nodal connections pairing algorithm parameters.  """
    @property
    @abstractmethod
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @property
    @abstractmethod
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchConeAngle
         Returns the search cone angle   
            
         
        """
        pass
    @property
    @abstractmethod
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @property
    @abstractmethod
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchRange
         Returns the search range   
            
         
        """
        pass
import NXOpen
import NXOpen.Fields
class INonlinearCylindricalDamping(NXOpen.INXObject): 
    """  This class represents an Interface to the Nonlinear Cylindrical Damping.  """
    @property
    @abstractmethod
    def RNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RNonlinearCylindricalDamping
         Returns the R nonlinear cylindrical damping   
            
         
        """
        pass
    @RNonlinearCylindricalDamping.setter
    def RNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RNonlinearCylindricalDamping
         Returns the R nonlinear cylindrical damping   
            
         
        """
        pass
    @property
    @abstractmethod
    def RrNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrNonlinearCylindricalDamping
         Returns the RR nonlinear cylindrical damping   
            
         
        """
        pass
    @RrNonlinearCylindricalDamping.setter
    def RrNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrNonlinearCylindricalDamping
         Returns the RR nonlinear cylindrical damping   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearCylindricalDamping
         Returns the RZ nonlinear cylindrical damping   
            
         
        """
        pass
    @RzNonlinearCylindricalDamping.setter
    def RzNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearCylindricalDamping
         Returns the RZ nonlinear cylindrical damping   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZNonlinearCylindricalDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearCylindricalDamping
         Returns the Z nonlinear cylindrical damping   
            
         
        """
        pass
    @ZNonlinearCylindricalDamping.setter
    def ZNonlinearCylindricalDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearCylindricalDamping
         Returns the Z nonlinear cylindrical damping   
            
         
        """
        pass
import NXOpen
import NXOpen.Fields
class INonlinearCylindricalStiffness(NXOpen.INXObject): 
    """  This class represents an Interface to the Nonlinear Cylindrical Stiffness.  """
    @property
    @abstractmethod
    def RNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RNonlinearCylindricalStiffness
         Returns the R nonlinear cylindrical stiffness   
            
         
        """
        pass
    @RNonlinearCylindricalStiffness.setter
    def RNonlinearCylindricalStiffness(self, rDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RNonlinearCylindricalStiffness
         Returns the R nonlinear cylindrical stiffness   
            
         
        """
        pass
    @property
    @abstractmethod
    def RrNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrNonlinearCylindricalStiffness
         Returns the RR nonlinear cylindrical stiffness   
            
         
        """
        pass
    @RrNonlinearCylindricalStiffness.setter
    def RrNonlinearCylindricalStiffness(self, rrDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RrNonlinearCylindricalStiffness
         Returns the RR nonlinear cylindrical stiffness   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearCylindricalStiffness
         Returns the RZ nonlinear cylindrical stiffness   
            
         
        """
        pass
    @RzNonlinearCylindricalStiffness.setter
    def RzNonlinearCylindricalStiffness(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearCylindricalStiffness
         Returns the RZ nonlinear cylindrical stiffness   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZNonlinearCylindricalStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearCylindricalStiffness
         Returns the Z nonlinear cylindrical stiffness   
            
         
        """
        pass
    @ZNonlinearCylindricalStiffness.setter
    def ZNonlinearCylindricalStiffness(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearCylindricalStiffness
         Returns the Z nonlinear cylindrical stiffness   
            
         
        """
        pass
import NXOpen
import NXOpen.Fields
class INonlinearDamping(NXOpen.INXObject): 
    """  This class represents an Interface to the nonlinear damping.  """
    @property
    @abstractmethod
    def RxNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxNonlinearDamping
         Returns the RX nonlinear damping   
            
         
        """
        pass
    @RxNonlinearDamping.setter
    def RxNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxNonlinearDamping
         Returns the RX nonlinear damping   
            
         
        """
        pass
    @property
    @abstractmethod
    def RyNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyNonlinearDamping
         Returns the RY nonlinear damping   
            
         
        """
        pass
    @RyNonlinearDamping.setter
    def RyNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyNonlinearDamping
         Returns the RY nonlinear damping   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearDamping
         Returns the RZ nonlinear damping   
            
         
        """
        pass
    @RzNonlinearDamping.setter
    def RzNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearDamping
         Returns the RZ nonlinear damping   
            
         
        """
        pass
    @property
    @abstractmethod
    def XNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) XNonlinearDamping
         Returns the X nonlinear damping   
            
         
        """
        pass
    @XNonlinearDamping.setter
    def XNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) XNonlinearDamping
         Returns the X nonlinear damping   
            
         
        """
        pass
    @property
    @abstractmethod
    def YNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) YNonlinearDamping
         Returns the Y nonlinear damping   
            
         
        """
        pass
    @YNonlinearDamping.setter
    def YNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) YNonlinearDamping
         Returns the Y nonlinear damping   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZNonlinearDamping(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearDamping
         Returns the Z nonlinear damping   
            
         
        """
        pass
    @ZNonlinearDamping.setter
    def ZNonlinearDamping(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearDamping
         Returns the Z nonlinear damping   
            
         
        """
        pass
import NXOpen
import NXOpen.Fields
class INonlinearStiffness(NXOpen.INXObject): 
    """  This class represents an Interface to the nonlinear stiffness.  """
    @property
    @abstractmethod
    def RxNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxNonlinearStiffness
         Returns the RX nonlinear stiffness   
            
         
        """
        pass
    @RxNonlinearStiffness.setter
    def RxNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxNonlinearStiffness
         Returns the RX nonlinear stiffness   
            
         
        """
        pass
    @property
    @abstractmethod
    def RyNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyNonlinearStiffness
         Returns the RY nonlinear stiffness   
            
         
        """
        pass
    @RyNonlinearStiffness.setter
    def RyNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyNonlinearStiffness
         Returns the RY nonlinear stiffness   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearStiffness
         Returns the RZ nonlinear stiffness   
            
         
        """
        pass
    @RzNonlinearStiffness.setter
    def RzNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzNonlinearStiffness
         Returns the RZ nonlinear stiffness   
            
         
        """
        pass
    @property
    @abstractmethod
    def XNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) XNonlinearStiffness
         Returns the X nonlinear stiffness   
            
         
        """
        pass
    @XNonlinearStiffness.setter
    def XNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) XNonlinearStiffness
         Returns the X nonlinear stiffness   
            
         
        """
        pass
    @property
    @abstractmethod
    def YNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) YNonlinearStiffness
         Returns the Y nonlinear stiffness   
            
         
        """
        pass
    @YNonlinearStiffness.setter
    def YNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) YNonlinearStiffness
         Returns the Y nonlinear stiffness   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZNonlinearStiffness(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearStiffness
         Returns the Z nonlinear stiffness   
            
         
        """
        pass
    @ZNonlinearStiffness.setter
    def ZNonlinearStiffness(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZNonlinearStiffness
         Returns the Z nonlinear stiffness   
            
         
        """
        pass
import NXOpen
class ISeamWeldFlangesContainer(IFlangesContainer): 
    """  This interface offers access to the flanges of a Seam Weld connection.
          """
    @abstractmethod
    def GetFlangeAngle(self, flangeIndex: int) -> NXOpen.Expression:
        """
         Get the flange angle.
         Returns angle ( NXOpen.Expression): .
        """
        pass
    @abstractmethod
    def GetFlangeGap(self, flangeIndex: int) -> NXOpen.Expression:
        """
         Get the flange gap.
         Returns gap ( NXOpen.Expression): .
        """
        pass
    @abstractmethod
    def GetFlangeThickness(self, flangeIndex: int) -> NXOpen.Expression:
        """
         Get the flange thickness.
         Returns thickness ( NXOpen.Expression): .
        """
        pass
    @abstractmethod
    def GetFlangeThicknessInherited(self, flangeIndex: int) -> bool:
        """
         Get the flange thickness inherited flag.
         Returns thicknessInherited (bool): .
        """
        pass
    @abstractmethod
    def SetFlangeThicknessInherited(self, flangeIndex: int, thicknessInherited: bool) -> None:
        """
         Set the flange thickness inherited flag.
        """
        pass
import NXOpen
import NXOpen.Fields
class IStiffnessDynamic(NXOpen.INXObject): 
    """  This class represents an Interface to the Stiffness dynamic.  """
    @property
    @abstractmethod
    def RxStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxStiffnessDynamic
         Returns the RX stiffness dynamic   
            
         
        """
        pass
    @RxStiffnessDynamic.setter
    def RxStiffnessDynamic(self, rxDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxStiffnessDynamic
         Returns the RX stiffness dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def RyStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyStiffnessDynamic
         Returns the RY stiffness dynamic   
            
         
        """
        pass
    @RyStiffnessDynamic.setter
    def RyStiffnessDynamic(self, ryDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyStiffnessDynamic
         Returns the RY stiffness dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzStiffnessDynamic
         Returns the RZ stiffness dynamic   
            
         
        """
        pass
    @RzStiffnessDynamic.setter
    def RzStiffnessDynamic(self, rzDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzStiffnessDynamic
         Returns the RZ stiffness dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def XStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) XStiffnessDynamic
         Returns the X stiffness dynamic   
            
         
        """
        pass
    @XStiffnessDynamic.setter
    def XStiffnessDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) XStiffnessDynamic
         Returns the X stiffness dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def YStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) YStiffnessDynamic
         Returns the Y stiffness dynamic   
            
         
        """
        pass
    @YStiffnessDynamic.setter
    def YStiffnessDynamic(self, yDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) YStiffnessDynamic
         Returns the Y stiffness dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZStiffnessDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZStiffnessDynamic
         Returns the Z stiffness dynamic   
            
         
        """
        pass
    @ZStiffnessDynamic.setter
    def ZStiffnessDynamic(self, zDynamic: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZStiffnessDynamic
         Returns the Z stiffness dynamic   
            
         
        """
        pass
import NXOpen
class IStiffness(NXOpen.INXObject): 
    """  This class represents an Interface to the Stiffness constants.  """
    @property
    @abstractmethod
    def RxStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RxStiffnessConstant
         Returns the RX stiffness constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def RyStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RyStiffnessConstant
         Returns the RY stiffness constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzStiffnessConstant
         Returns the RZ stiffness constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def StiffnessType(self) -> StiffnessType:
        """
        Getter for property: ( StiffnessType NXOpen.CAE) StiffnessType
         Returns the stiffness type   
            
         
        """
        pass
    @StiffnessType.setter
    def StiffnessType(self, oStiffnessType: StiffnessType):
        """
        Setter for property: ( StiffnessType NXOpen.CAE) StiffnessType
         Returns the stiffness type   
            
         
        """
        pass
    @property
    @abstractmethod
    def XStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XStiffnessConstant
         Returns the X stiffness constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def YStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YStiffnessConstant
         Returns the Y stiffness constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZStiffnessConstant
         Returns the Z stiffness constant   
            
         
        """
        pass
    @abstractmethod
    def GetSupportedStiffnessTypes(self) -> List[StiffnessType]:
        """
         Gets supported stiffness types of connection. 
         Returns types ( StiffnessType List[NXOpen.C):  Supported Stiffness Types .
        """
        pass
import NXOpen
import NXOpen.Fields
class IStructuralDampingDynamic(NXOpen.INXObject): 
    """  This class represents an Interface to the StructuralDamping dynamic.  """
    @property
    @abstractmethod
    def RxStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxStructuralDampingDynamic
         Returns the RX structural damping dynamic   
            
         
        """
        pass
    @RxStructuralDampingDynamic.setter
    def RxStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxStructuralDampingDynamic
         Returns the RX structural damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def RyStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyStructuralDampingDynamic
         Returns the RY structural damping dynamic   
            
         
        """
        pass
    @RyStructuralDampingDynamic.setter
    def RyStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyStructuralDampingDynamic
         Returns the RY structural damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzStructuralDampingDynamic
         Returns the RZ structural damping dynamic   
            
         
        """
        pass
    @RzStructuralDampingDynamic.setter
    def RzStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzStructuralDampingDynamic
         Returns the RZ structural damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def XStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) XStructuralDampingDynamic
         Returns the X structural damping dynamic   
            
         
        """
        pass
    @XStructuralDampingDynamic.setter
    def XStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) XStructuralDampingDynamic
         Returns the X structural damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def YStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) YStructuralDampingDynamic
         Returns the Y structural damping dynamic   
            
         
        """
        pass
    @YStructuralDampingDynamic.setter
    def YStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) YStructuralDampingDynamic
         Returns the Y structural damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZStructuralDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZStructuralDampingDynamic
         Returns the Z structural damping dynamic   
            
         
        """
        pass
    @ZStructuralDampingDynamic.setter
    def ZStructuralDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZStructuralDampingDynamic
         Returns the Z structural damping dynamic   
            
         
        """
        pass
import NXOpen
class IStructuralDamping(NXOpen.INXObject): 
    """  This class represents an Interface to the StructuralDamping constants.  """
    @property
    @abstractmethod
    def RxStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RxStructuralDampingConstant
         Returns the RX structural damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def RyStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RyStructuralDampingConstant
         Returns the RY structural damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzStructuralDampingConstant
         Returns the RZ structural damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def XStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XStructuralDampingConstant
         Returns the X structural damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def YStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YStructuralDampingConstant
         Returns the Y structural damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZStructuralDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZStructuralDampingConstant
         Returns the Z structural damping constant   
            
         
        """
        pass
import NXOpen
class ITolerance(NXOpen.INXObject): 
    """  This class represents an Interface to the Tolerance parameters.  """
    @property
    @abstractmethod
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxAngleBetweenNormals
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    @property
    @abstractmethod
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDistCGToElemCG
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    @property
    @abstractmethod
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxNormalDistCGToFlanges
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    @property
    @abstractmethod
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProjectTolerance
         Returns the projection tolerance   
            
         
        """
        pass
import NXOpen
import NXOpen.Fields
class IViscousDampingDynamic(NXOpen.INXObject): 
    """  This class represents an Interface to the ViscousDamping dynamic.  """
    @property
    @abstractmethod
    def RxViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxViscousDampingDynamic
         Returns the RX viscous damping dynamic   
            
         
        """
        pass
    @RxViscousDampingDynamic.setter
    def RxViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RxViscousDampingDynamic
         Returns the RX viscous damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def RyViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyViscousDampingDynamic
         Returns the RY viscous damping dynamic   
            
         
        """
        pass
    @RyViscousDampingDynamic.setter
    def RyViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RyViscousDampingDynamic
         Returns the RY viscous damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzViscousDampingDynamic
         Returns the RZ viscous damping dynamic   
            
         
        """
        pass
    @RzViscousDampingDynamic.setter
    def RzViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) RzViscousDampingDynamic
         Returns the RZ viscous damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def XViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) XViscousDampingDynamic
         Returns the X viscous damping dynamic   
            
         
        """
        pass
    @XViscousDampingDynamic.setter
    def XViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) XViscousDampingDynamic
         Returns the X viscous damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def YViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) YViscousDampingDynamic
         Returns the Y viscous damping dynamic   
            
         
        """
        pass
    @YViscousDampingDynamic.setter
    def YViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) YViscousDampingDynamic
         Returns the Y viscous damping dynamic   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZViscousDampingDynamic(self) -> NXOpen.Fields.ScalarFieldWrapper:
        """
        Getter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZViscousDampingDynamic
         Returns the Z viscous damping dynamic   
            
         
        """
        pass
    @ZViscousDampingDynamic.setter
    def ZViscousDampingDynamic(self, bridge: NXOpen.Fields.ScalarFieldWrapper):
        """
        Setter for property: ( NXOpen.Fields.ScalarFieldWrapper) ZViscousDampingDynamic
         Returns the Z viscous damping dynamic   
            
         
        """
        pass
import NXOpen
class IViscousDamping(NXOpen.INXObject): 
    """  This class represents an Interface to the ViscousDamping constants.  """
    @property
    @abstractmethod
    def RxViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RxViscousDampingConstant
         Returns the RX viscous damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def RyViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RyViscousDampingConstant
         Returns the RY viscous damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def RzViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzViscousDampingConstant
         Returns the RZ viscous damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def XViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XViscousDampingConstant
         Returns the X viscous damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def YViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YViscousDampingConstant
         Returns the Y viscous damping constant   
            
         
        """
        pass
    @property
    @abstractmethod
    def ZViscousDampingConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZViscousDampingConstant
         Returns the Z viscous damping constant   
            
         
        """
        pass
import NXOpen
class IWidth(NXOpen.INXObject): 
    """  This class represents an Interface to the Width parameters.  """
    @property
    @abstractmethod
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width value   
            
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.CAE
import NXOpen.Features
class JoinDataUtils(NXOpen.Object): 
    """ This class contains join data utility methods   """
    def CreateConnectionsFromJoinFeatures(features: List[NXOpen.Features.Feature], components: List[NXOpen.Assemblies.Component]) -> List[IConnection]:
        """
         Function that creates connections based on the feature records
         Returns connections ( IConnection List[NXOpen.C): The created connections based on the join features.
        """
        pass
    def LoadCadComponents(feModel: NXOpen.CAE.IFEModel, cadComponentsLoadType: CadComponentsLoadType) -> None:
        """
         Function that loads the required CAD components 
        """
        pass
import NXOpen
class Kinematic(IConnection): 
    """ Kinematic connection. Use this interface to setget properties and parameters of the Kinematic connection.  """
    @property
    def CharacteristicLengthRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CharacteristicLengthRadius
         Returns the radius characteristic length used by Revolute and Spherical Kinematic   
            
         
        """
        pass
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @property
    def DofCombination(self) -> DofCombination:
        """
        Getter for property: ( DofCombination NXOpen.CAE) DofCombination
         Returns the degrees of freedom combination type   
            
         
        """
        pass
    @DofCombination.setter
    def DofCombination(self, type: DofCombination):
        """
        Setter for property: ( DofCombination NXOpen.CAE) DofCombination
         Returns the degrees of freedom combination type   
            
         
        """
        pass
    @property
    def FrictionCoefficient(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FrictionCoefficient
         Returns the friction coefficient   
            
         
        """
        pass
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchConeAngle
         Returns the search cone angle   
            
         
        """
        pass
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchRange
         Returns the search range   
            
         
        """
        pass
    @property
    def TighteningForce(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TighteningForce
         Returns the tightening force   
            
         
        """
        pass
    @property
    def UseFriction(self) -> bool:
        """
        Getter for property: (bool) UseFriction
         Returns the flag indicating whether to use friction parameters or not   
            
         
        """
        pass
    @UseFriction.setter
    def UseFriction(self, useFriction: bool):
        """
        Setter for property: (bool) UseFriction
         Returns the flag indicating whether to use friction parameters or not   
            
         
        """
        pass
import NXOpen
class LMIEBody(NXOpen.TaggedObject): 
    """  LMIEBody  """
    pass
class LMIECenterDefinition(LMIEError): 
    """  Lumped Mass Center Definition. Use this interface to setget properties and parameters of the Lumped Mass Center Definition.  """
    @property
    def MassCenterType(self) -> MassCenterType:
        """
        Getter for property: ( MassCenterType NXOpen.CAE) MassCenterType
         Returns the mass center type   
            
         
        """
        pass
    @MassCenterType.setter
    def MassCenterType(self, massCenterType: MassCenterType):
        """
        Setter for property: ( MassCenterType NXOpen.CAE) MassCenterType
         Returns the mass center type   
            
         
        """
        pass
    @property
    def Node(self) -> LMIENode:
        """
        Getter for property: ( LMIENode NXOpen.CAE) Node
         Returns the node   
            
         
        """
        pass
    @Node.setter
    def Node(self, node: LMIENode):
        """
        Setter for property: ( LMIENode NXOpen.CAE) Node
         Returns the node   
            
         
        """
        pass
    @property
    def Point(self) -> LMIEPoint:
        """
        Getter for property: ( LMIEPoint NXOpen.CAE) Point
         Returns the point   
            
         
        """
        pass
    @Point.setter
    def Point(self, point: LMIEPoint):
        """
        Setter for property: ( LMIEPoint NXOpen.CAE) Point
         Returns the point   
            
         
        """
        pass
    @property
    def SelectionRecipe(self) -> LMIESelectionRecipe:
        """
        Getter for property: ( LMIESelectionRecipe NXOpen.CAE) SelectionRecipe
         Returns the selection recipe   
            
         
        """
        pass
    @SelectionRecipe.setter
    def SelectionRecipe(self, recipe: LMIESelectionRecipe):
        """
        Setter for property: ( LMIESelectionRecipe NXOpen.CAE) SelectionRecipe
         Returns the selection recipe   
            
         
        """
        pass
    def CreateNode(self) -> LMIENode:
        """
         Create a standalone node 
         Returns node ( LMIENode NXOpen.CAE):  Center Node .
        """
        pass
    def CreatePoint(self) -> LMIEPoint:
        """
         Create a standalone point 
         Returns point ( LMIEPoint NXOpen.CAE):  Center Point .
        """
        pass
    def CreateSelectionRecipe(self) -> LMIESelectionRecipe:
        """
         Create a standalone selection recipe 
         Returns recipe ( LMIESelectionRecipe NXOpen.CAE):  Center Selection Recipe .
        """
        pass
class LMIEConnection(LMIEError): 
    """  LMIEConnection  """
    @property
    def CenterDefinition(self) -> LMIECenterDefinition:
        """
        Getter for property: ( LMIECenterDefinition NXOpen.CAE) CenterDefinition
         Returns the center definition   
            
         
        """
        pass
    @CenterDefinition.setter
    def CenterDefinition(self, opt: LMIECenterDefinition):
        """
        Setter for property: ( LMIECenterDefinition NXOpen.CAE) CenterDefinition
         Returns the center definition   
            
         
        """
        pass
    @property
    def ConnectionElementType(self) -> ElementType:
        """
        Getter for property: ( ElementType NXOpen.CAE) ConnectionElementType
         Returns the connection element type   
            
         
        """
        pass
    @ConnectionElementType.setter
    def ConnectionElementType(self, connElementType: ElementType):
        """
        Setter for property: ( ElementType NXOpen.CAE) ConnectionElementType
         Returns the connection element type   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the mass description   
            
         
        """
        pass
    @Description.setter
    def Description(self, desc: str):
        """
        Setter for property: (str) Description
         Returns the mass description   
            
         
        """
        pass
    @property
    def FolderName(self) -> str:
        """
        Getter for property: (str) FolderName
         Returns the folder name   
            
         
        """
        pass
    @FolderName.setter
    def FolderName(self, folderName: str):
        """
        Setter for property: (str) FolderName
         Returns the folder name   
            
         
        """
        pass
    @property
    def Id(self) -> int:
        """
        Getter for property: (int) Id
         Returns the ID   
            
         
        """
        pass
    @Id.setter
    def Id(self, pId: int):
        """
        Setter for property: (int) Id
         Returns the ID   
            
         
        """
        pass
    @property
    def Inertia(self) -> LMIEInertia:
        """
        Getter for property: ( LMIEInertia NXOpen.CAE) Inertia
         Returns the inertia   
            
         
        """
        pass
    @Inertia.setter
    def Inertia(self, opt: LMIEInertia):
        """
        Setter for property: ( LMIEInertia NXOpen.CAE) Inertia
         Returns the inertia   
            
         
        """
        pass
    @property
    def LegConnection(self) -> LMIELegConnection:
        """
        Getter for property: ( LMIELegConnection NXOpen.CAE) LegConnection
         Returns the leg connection   
            
         
        """
        pass
    @LegConnection.setter
    def LegConnection(self, opt: LMIELegConnection):
        """
        Setter for property: ( LMIELegConnection NXOpen.CAE) LegConnection
         Returns the leg connection   
            
         
        """
        pass
    @property
    def Mass(self) -> LMIEMass:
        """
        Getter for property: ( LMIEMass NXOpen.CAE) Mass
         Returns the mass   
            
         
        """
        pass
    @Mass.setter
    def Mass(self, opt: LMIEMass):
        """
        Setter for property: ( LMIEMass NXOpen.CAE) Mass
         Returns the mass   
            
         
        """
        pass
    @property
    def Plvc(self) -> str:
        """
        Getter for property: (str) Plvc
         Returns the plvc   
            
         
        """
        pass
    @Plvc.setter
    def Plvc(self, pPlvc: str):
        """
        Setter for property: (str) Plvc
         Returns the plvc   
            
         
        """
        pass
    @property
    def UnitSystem(self) -> LMIEUnitSystem:
        """
        Getter for property: ( LMIEUnitSystem NXOpen.CAE) UnitSystem
         Returns the unit system    
            
         
        """
        pass
    @UnitSystem.setter
    def UnitSystem(self, opt: LMIEUnitSystem):
        """
        Setter for property: ( LMIEUnitSystem NXOpen.CAE) UnitSystem
         Returns the unit system    
            
         
        """
        pass
    def CreateCenterDefinition(self) -> LMIECenterDefinition:
        """
         Create a standalone center definition 
         Returns opt ( LMIECenterDefinition NXOpen.CAE):  The center definition .
        """
        pass
    def CreateInertia(self) -> LMIEInertia:
        """
         Create a standalone inertia 
         Returns opt ( LMIEInertia NXOpen.CAE):  The inertia .
        """
        pass
    def CreateLegConnection(self) -> LMIELegConnection:
        """
         Create a standalone leg connection 
         Returns opt ( LMIELegConnection NXOpen.CAE):  The leg connection .
        """
        pass
    def CreateLegDefinition(self) -> LMIELegDefinition:
        """
         Create a standalone leg definition 
         Returns opt ( LMIELegDefinition NXOpen.CAE):  The leg definition .
        """
        pass
    def CreateMass(self) -> LMIEMass:
        """
         Create a standalone mass 
         Returns opt ( LMIEMass NXOpen.CAE):  Mass Options .
        """
        pass
    def CreateUnitSystem(self) -> LMIEUnitSystem:
        """
         Create a standalone unit system  
         Returns opt ( LMIEUnitSystem NXOpen.CAE):  Unit System .
        """
        pass
    def GetLegDefinitions(self) -> List[LMIELegDefinition]:
        """
         Get the leg definitions 
         Returns opt ( LMIELegDefinition List[NXOpen.C):  The leg definitions .
        """
        pass
    def SetLegDefinitions(self, opt: List[LMIELegDefinition]) -> None:
        """
         Set the leg definitions 
        """
        pass
import NXOpen
class LMIEElementEdge(NXOpen.TaggedObject): 
    """  LMIEElementEdge object  """
    @property
    def EdgeNumber(self) -> int:
        """
        Getter for property: (int) EdgeNumber
         Returns the edge number   
            
         
        """
        pass
    @EdgeNumber.setter
    def EdgeNumber(self, edgeNumber: int):
        """
        Setter for property: (int) EdgeNumber
         Returns the edge number   
            
         
        """
        pass
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the element id   
            
         
        """
        pass
    @Id.setter
    def Id(self, elementId: str):
        """
        Setter for property: (str) Id
         Returns the element id   
            
         
        """
        pass
import NXOpen
class LMIEElementFace(NXOpen.TaggedObject): 
    """  LMIEElementFace object  """
    @property
    def FaceNumber(self) -> int:
        """
        Getter for property: (int) FaceNumber
         Returns the face number   
            
         
        """
        pass
    @FaceNumber.setter
    def FaceNumber(self, faceNumber: int):
        """
        Setter for property: (int) FaceNumber
         Returns the face number   
            
         
        """
        pass
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the element id   
            
         
        """
        pass
    @Id.setter
    def Id(self, elementId: str):
        """
        Setter for property: (str) Id
         Returns the element id   
            
         
        """
        pass
import NXOpen
class LMIEElement(NXOpen.TaggedObject): 
    """  LMIEElement object  """
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the element id   
            
         
        """
        pass
    @Id.setter
    def Id(self, unit: str):
        """
        Setter for property: (str) Id
         Returns the element id   
            
         
        """
        pass
import NXOpen
class LMIEError(NXOpen.NXObject): 
    """  LMIEError  """
    def GetErrorCodes(self) -> List[str]:
        """
         The error codes 
         Returns errorCodes (List[str]):  The error codes .
        """
        pass
    def GetErrorMessages(self) -> List[str]:
        """
         The error messages 
         Returns errorMsgs (List[str]):  The error messages .
        """
        pass
    def GetErrorValues(self, errorIndex: int) -> List[str]:
        """
         The error values for an error 
         Returns errorValues (List[str]):  The error values for an error .
        """
        pass
    def GetWarningCodes(self) -> List[str]:
        """
         The warning codes 
         Returns warningCodes (List[str]):  The warning codes .
        """
        pass
    def HasErrors(self) -> bool:
        """
         Has errors 
         Returns hasErrors (bool): .
        """
        pass
class LMIEInertia(LMIEError): 
    """  Lumped mass import export inertia object.  """
    @property
    def Ixx(self) -> float:
        """
        Getter for property: (float) Ixx
         Returns the Ixx value   
            
         
        """
        pass
    @Ixx.setter
    def Ixx(self, outputValue: float):
        """
        Setter for property: (float) Ixx
         Returns the Ixx value   
            
         
        """
        pass
    @property
    def Iyx(self) -> float:
        """
        Getter for property: (float) Iyx
         Returns the Iyx value   
            
         
        """
        pass
    @Iyx.setter
    def Iyx(self, outputValue: float):
        """
        Setter for property: (float) Iyx
         Returns the Iyx value   
            
         
        """
        pass
    @property
    def Iyy(self) -> float:
        """
        Getter for property: (float) Iyy
         Returns the Iyy value   
            
         
        """
        pass
    @Iyy.setter
    def Iyy(self, outputValue: float):
        """
        Setter for property: (float) Iyy
         Returns the Iyy value   
            
         
        """
        pass
    @property
    def Izx(self) -> float:
        """
        Getter for property: (float) Izx
         Returns the Izx value   
            
         
        """
        pass
    @Izx.setter
    def Izx(self, outputValue: float):
        """
        Setter for property: (float) Izx
         Returns the Izx value   
            
         
        """
        pass
    @property
    def Izy(self) -> float:
        """
        Getter for property: (float) Izy
         Returns the Izy value   
            
         
        """
        pass
    @Izy.setter
    def Izy(self, outputValue: float):
        """
        Setter for property: (float) Izy
         Returns the Izy value   
            
         
        """
        pass
    @property
    def Izz(self) -> float:
        """
        Getter for property: (float) Izz
         Returns the Izz value   
            
         
        """
        pass
    @Izz.setter
    def Izz(self, outputValue: float):
        """
        Setter for property: (float) Izz
         Returns the Izz value   
            
         
        """
        pass
class LMIELegConnection(LMIEError): 
    """  Mass definition.  """
    @property
    def LegConnectionType(self) -> MassConnectivityType:
        """
        Getter for property: ( MassConnectivityType NXOpen.CAE) LegConnectionType
         Returns the leg connection type   
            
         
        """
        pass
    @LegConnectionType.setter
    def LegConnectionType(self, type: MassConnectivityType):
        """
        Setter for property: ( MassConnectivityType NXOpen.CAE) LegConnectionType
         Returns the leg connection type   
            
         
        """
        pass
    @property
    def LocalSpiders(self) -> LMIELocalSpiders:
        """
        Getter for property: ( LMIELocalSpiders NXOpen.CAE) LocalSpiders
         Returns the local spiders   
            
         
        """
        pass
    @LocalSpiders.setter
    def LocalSpiders(self, opt: LMIELocalSpiders):
        """
        Setter for property: ( LMIELocalSpiders NXOpen.CAE) LocalSpiders
         Returns the local spiders   
            
         
        """
        pass
    @property
    def NearestNodes(self) -> LMIENearestNodes:
        """
        Getter for property: ( LMIENearestNodes NXOpen.CAE) NearestNodes
         Returns the nearest nodes   
            
         
        """
        pass
    @NearestNodes.setter
    def NearestNodes(self, opt: LMIENearestNodes):
        """
        Setter for property: ( LMIENearestNodes NXOpen.CAE) NearestNodes
         Returns the nearest nodes   
            
         
        """
        pass
    def CreateLocalSpiders(self) -> LMIELocalSpiders:
        """
         Create a standalone local spiders 
         Returns opt ( LMIELocalSpiders NXOpen.CAE):  Local spiders .
        """
        pass
    def CreateNearestNodes(self) -> LMIENearestNodes:
        """
         Create a standalone nearest nodes 
         Returns opt ( LMIENearestNodes NXOpen.CAE):  Nearest nodes .
        """
        pass
class LMIELegDefinition(LMIEError): 
    """  Mass definition.  """
    @property
    def Node(self) -> LMIENode:
        """
        Getter for property: ( LMIENode NXOpen.CAE) Node
         Returns the node   
            
         
        """
        pass
    @Node.setter
    def Node(self, node: LMIENode):
        """
        Setter for property: ( LMIENode NXOpen.CAE) Node
         Returns the node   
            
         
        """
        pass
    @property
    def Point(self) -> LMIEPoint:
        """
        Getter for property: ( LMIEPoint NXOpen.CAE) Point
         Returns the point   
            
         
        """
        pass
    @Point.setter
    def Point(self, point: LMIEPoint):
        """
        Setter for property: ( LMIEPoint NXOpen.CAE) Point
         Returns the point   
            
         
        """
        pass
    @property
    def SelectionRecipe(self) -> LMIESelectionRecipe:
        """
        Getter for property: ( LMIESelectionRecipe NXOpen.CAE) SelectionRecipe
         Returns the selection recipe   
            
         
        """
        pass
    @SelectionRecipe.setter
    def SelectionRecipe(self, recipe: LMIESelectionRecipe):
        """
        Setter for property: ( LMIESelectionRecipe NXOpen.CAE) SelectionRecipe
         Returns the selection recipe   
            
         
        """
        pass
    def CreateNode(self) -> LMIENode:
        """
         Create a standalone node 
         Returns node ( LMIENode NXOpen.CAE):  Leg Node .
        """
        pass
    def CreatePoint(self) -> LMIEPoint:
        """
         Create a standalone point 
         Returns point ( LMIEPoint NXOpen.CAE):  Leg Point .
        """
        pass
    def CreateSelectionRecipe(self) -> LMIESelectionRecipe:
        """
         Create a standalone selection recipe 
         Returns recipe ( LMIESelectionRecipe NXOpen.CAE):  Leg Selection Recipe .
        """
        pass
class LMIELocalSpiderCenterOptions(LMIEError): 
    """  Local Spider Center Options definition.  """
    @property
    def LocalSpiderCenterType(self) -> LocalSpiderCenterType:
        """
        Getter for property: ( LocalSpiderCenterType NXOpen.CAE) LocalSpiderCenterType
         Returns the Local Spider Center type   
            
         
        """
        pass
    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, type: LocalSpiderCenterType):
        """
        Setter for property: ( LocalSpiderCenterType NXOpen.CAE) LocalSpiderCenterType
         Returns the Local Spider Center type   
            
         
        """
        pass
class LMIELocalSpiders(LMIEError): 
    """  Mass Local Spiders definition.  """
    @property
    def LocalSpiderCenterOptions(self) -> LMIELocalSpiderCenterOptions:
        """
        Getter for property: ( LMIELocalSpiderCenterOptions NXOpen.CAE) LocalSpiderCenterOptions
         Returns the local spider center options   
            
         
        """
        pass
    @LocalSpiderCenterOptions.setter
    def LocalSpiderCenterOptions(self, opt: LMIELocalSpiderCenterOptions):
        """
        Setter for property: ( LMIELocalSpiderCenterOptions NXOpen.CAE) LocalSpiderCenterOptions
         Returns the local spider center options   
            
         
        """
        pass
    @property
    def MaxSearchDistance(self) -> float:
        """
        Getter for property: (float) MaxSearchDistance
         Returns the mass distribution type   
            
         
        """
        pass
    @MaxSearchDistance.setter
    def MaxSearchDistance(self, val: float):
        """
        Setter for property: (float) MaxSearchDistance
         Returns the mass distribution type   
            
         
        """
        pass
    @property
    def PanelOptions(self) -> LMIEPanelOptions:
        """
        Getter for property: ( LMIEPanelOptions NXOpen.CAE) PanelOptions
         Returns the panel options   
            
         
        """
        pass
    @PanelOptions.setter
    def PanelOptions(self, opt: LMIEPanelOptions):
        """
        Setter for property: ( LMIEPanelOptions NXOpen.CAE) PanelOptions
         Returns the panel options   
            
         
        """
        pass
    @property
    def RegionSelection(self) -> LMIERegionSelection:
        """
        Getter for property: ( LMIERegionSelection NXOpen.CAE) RegionSelection
         Returns the region selection   
            
         
        """
        pass
    @RegionSelection.setter
    def RegionSelection(self, opt: LMIERegionSelection):
        """
        Setter for property: ( LMIERegionSelection NXOpen.CAE) RegionSelection
         Returns the region selection   
            
         
        """
        pass
    @property
    def RingOptions(self) -> LMIERingOptions:
        """
        Getter for property: ( LMIERingOptions NXOpen.CAE) RingOptions
         Returns the ring options   
            
         
        """
        pass
    @RingOptions.setter
    def RingOptions(self, opt: LMIERingOptions):
        """
        Setter for property: ( LMIERingOptions NXOpen.CAE) RingOptions
         Returns the ring options   
            
         
        """
        pass
    def CreateLocalSpiderCenterOptions(self) -> LMIELocalSpiderCenterOptions:
        """
         Create a standalone local spider center options 
         Returns opt ( LMIELocalSpiderCenterOptions NXOpen.CAE):  Local Spider Center options .
        """
        pass
    def CreatePanelOptions(self) -> LMIEPanelOptions:
        """
         Create a standalone panel options 
         Returns opt ( LMIEPanelOptions NXOpen.CAE):  Panel options .
        """
        pass
    def CreateRegionSelection(self) -> LMIERegionSelection:
        """
         Create a standalone region selection 
         Returns opt ( LMIERegionSelection NXOpen.CAE):  Region selection .
        """
        pass
    def CreateRingOptions(self) -> LMIERingOptions:
        """
         Create a standalone ring options 
         Returns opt ( LMIERingOptions NXOpen.CAE):  Ring options .
        """
        pass
class LMIEMass(LMIEError): 
    """  Mass definition.  """
    @property
    def MassDistributionType(self) -> MassDistributionType:
        """
        Getter for property: ( MassDistributionType NXOpen.CAE) MassDistributionType
         Returns the mass distribution type   
            
         
        """
        pass
    @MassDistributionType.setter
    def MassDistributionType(self, type: MassDistributionType):
        """
        Setter for property: ( MassDistributionType NXOpen.CAE) MassDistributionType
         Returns the mass distribution type   
            
         
        """
        pass
    @property
    def MassType(self) -> MassType:
        """
        Getter for property: ( MassType NXOpen.CAE) MassType
         Returns the mass type   
            
         
        """
        pass
    @MassType.setter
    def MassType(self, type: MassType):
        """
        Setter for property: ( MassType NXOpen.CAE) MassType
         Returns the mass type   
            
         
        """
        pass
    @property
    def MassValue(self) -> float:
        """
        Getter for property: (float) MassValue
         Returns the mass distribution type   
            
         
        """
        pass
    @MassValue.setter
    def MassValue(self, val: float):
        """
        Setter for property: (float) MassValue
         Returns the mass distribution type   
            
         
        """
        pass
import NXOpen
class LMIEMesh(NXOpen.TaggedObject): 
    """  LMIEMesh object  """
    pass
class LMIENearestNodes(LMIEError): 
    """  Mass definition.  """
    @property
    def MaxSearchDistance(self) -> float:
        """
        Getter for property: (float) MaxSearchDistance
         Returns the mass distribution type   
            
         
        """
        pass
    @MaxSearchDistance.setter
    def MaxSearchDistance(self, val: float):
        """
        Setter for property: (float) MaxSearchDistance
         Returns the mass distribution type   
            
         
        """
        pass
    @property
    def RegionSelection(self) -> LMIERegionSelection:
        """
        Getter for property: ( LMIERegionSelection NXOpen.CAE) RegionSelection
         Returns the region selection   
            
         
        """
        pass
    @RegionSelection.setter
    def RegionSelection(self, opt: LMIERegionSelection):
        """
        Setter for property: ( LMIERegionSelection NXOpen.CAE) RegionSelection
         Returns the region selection   
            
         
        """
        pass
    def CreateRegionSelection(self) -> LMIERegionSelection:
        """
         Create a standalone region selection 
         Returns opt ( LMIERegionSelection NXOpen.CAE):  Region selection .
        """
        pass
class LMIENode(LMIEError): 
    """  Lumped Mass center definition node.  """
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the node id   
            
         
        """
        pass
    @Id.setter
    def Id(self, id: str):
        """
        Setter for property: (str) Id
         Returns the node id   
            
         
        """
        pass
class LMIEPanelOptions(LMIEError): 
    """  Mass definition.  """
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
         Returns the mass distribution type   
            
         
        """
        pass
    @Distance.setter
    def Distance(self, val: float):
        """
        Setter for property: (float) Distance
         Returns the mass distribution type   
            
         
        """
        pass
    @property
    def SearchPanelsType(self) -> PanelSearchType:
        """
        Getter for property: ( PanelSearchType NXOpen.CAE) SearchPanelsType
         Returns the Ring Search type   
            
         
        """
        pass
    @SearchPanelsType.setter
    def SearchPanelsType(self, type: PanelSearchType):
        """
        Setter for property: ( PanelSearchType NXOpen.CAE) SearchPanelsType
         Returns the Ring Search type   
            
         
        """
        pass
class LMIEPid(LMIEError): 
    """  Lumped Mass PID.  """
    @property
    def Label(self) -> int:
        """
        Getter for property: (int) Label
         Returns the PID label   
            
         
        """
        pass
    @Label.setter
    def Label(self, label: int):
        """
        Setter for property: (int) Label
         Returns the PID label   
            
         
        """
        pass
import NXOpen
class LMIEPoint(LMIEError): 
    """  Lumped Mass center definition point.  """
    @property
    def Coordinates(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Coordinates
         Returns the point coordinates   
            
         
        """
        pass
    @Coordinates.setter
    def Coordinates(self, point: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Coordinates
         Returns the point coordinates   
            
         
        """
        pass
class LMIERegionSelection(LMIEError): 
    """  Region selection.  """
    def CreatePid(self) -> LMIEPid:
        """
         Create a standalone PID 
         Returns opt ( LMIEPid NXOpen.CAE):  The PID .
        """
        pass
    def CreateSelectionRecipe(self) -> LMIESelectionRecipe:
        """
         Create a standalone Selection Recipe 
         Returns opt ( LMIESelectionRecipe NXOpen.CAE):  The PID .
        """
        pass
    def GetPids(self) -> List[LMIEPid]:
        """
         Get the PIDs 
         Returns opt ( LMIEPid List[NXOpen.C):  The PIDs .
        """
        pass
    def GetSelectionRecipes(self) -> List[LMIESelectionRecipe]:
        """
         Get the selection recipes 
         Returns opt ( LMIESelectionRecipe List[NXOpen.C):  The selection recipes .
        """
        pass
    def SetPids(self, opt: List[LMIEPid]) -> None:
        """
         Set the PIDs 
        """
        pass
    def SetSelectionRecipes(self, opt: List[LMIESelectionRecipe]) -> None:
        """
         Set the selection recipes 
        """
        pass
class LMIERingOptions(LMIEError): 
    """  Mass definition.  """
    @property
    def ExpansionRadius(self) -> float:
        """
        Getter for property: (float) ExpansionRadius
         Returns the mass distribution type   
            
         
        """
        pass
    @ExpansionRadius.setter
    def ExpansionRadius(self, val: float):
        """
        Setter for property: (float) ExpansionRadius
         Returns the mass distribution type   
            
         
        """
        pass
    @property
    def ExpansionRadiusFactor(self) -> float:
        """
        Getter for property: (float) ExpansionRadiusFactor
         Returns the mass distribution type   
            
         
        """
        pass
    @ExpansionRadiusFactor.setter
    def ExpansionRadiusFactor(self, val: float):
        """
        Setter for property: (float) ExpansionRadiusFactor
         Returns the mass distribution type   
            
         
        """
        pass
    @property
    def RingType(self) -> RingSearchType:
        """
        Getter for property: ( RingSearchType NXOpen.CAE) RingType
         Returns the Ring Search type   
            
         
        """
        pass
    @RingType.setter
    def RingType(self, type: RingSearchType):
        """
        Setter for property: ( RingSearchType NXOpen.CAE) RingType
         Returns the Ring Search type   
            
         
        """
        pass
class LMIESelectionRecipe(LMIEError): 
    """  Lumped Mass center definition selection recipe.  """
    @property
    def RecipeName(self) -> str:
        """
        Getter for property: (str) RecipeName
         Returns the selection recipe   
            
         
        """
        pass
    @RecipeName.setter
    def RecipeName(self, name: str):
        """
        Setter for property: (str) RecipeName
         Returns the selection recipe   
            
         
        """
        pass
class LMIEUnitSystem(LMIEError): 
    """  Seam Weld connection. Use this interface to setget properties and parameters of the spot weld connection.  """
    @property
    def LengthUnit(self) -> str:
        """
        Getter for property: (str) LengthUnit
         Returns the length unit   
            
         
        """
        pass
    @LengthUnit.setter
    def LengthUnit(self, unit: str):
        """
        Setter for property: (str) LengthUnit
         Returns the length unit   
            
         
        """
        pass
    @property
    def MassUnit(self) -> str:
        """
        Getter for property: (str) MassUnit
         Returns the mass unit   
            
         
        """
        pass
    @MassUnit.setter
    def MassUnit(self, unit: str):
        """
        Setter for property: (str) MassUnit
         Returns the mass unit   
            
         
        """
        pass
class LocalSpiderCenterType(Enum):
    """
    Members Include: 
     |MeanOfSpiderLegs|  Local spider center is computed as the mean of its legs 
     |InputLegDefinition|  Use the input leg definition coordinates as local spider center 

    """
    MeanOfSpiderLegs: int
    InputLegDefinition: int
    @staticmethod
    def ValueOf(value: int) -> LocalSpiderCenterType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class LocationDirectionType(Enum):
    """
    Members Include: 
     |Point|  Two PointsNodes 
     |Vector|  PointsNode and Vector 
     |Curve|  Curves 
     |SelectionRecipes|  Selection Recipes 

    """
    Point: int
    Vector: int
    Curve: int
    SelectionRecipes: int
    @staticmethod
    def ValueOf(value: int) -> LocationDirectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class LocationType(Enum):
    """
    Members Include: 
     |Coordinates|  Coordinates 
     |Point|  Point 
     |Node|  Node 
     |SeriesOfNodes|  Series Of Nodes 
     |SeriesOfCoordinates|  Series Of Coordinates
     |Curve|  Curve 
     |FeEdgeGroup|  Group Of Element Edges 
     |SeriesOfPoints|  Series Of Points 
     |LocationWithDirection|  Location with direction 
     |SelectionRecipe|  Selection Recipe 
     |MeshPoint|  Mesh Point 
     |Group|  Group 

    """
    Coordinates: int
    Point: int
    Node: int
    SeriesOfNodes: int
    SeriesOfCoordinates: int
    Curve: int
    FeEdgeGroup: int
    SeriesOfPoints: int
    LocationWithDirection: int
    SelectionRecipe: int
    MeshPoint: int
    Group: int
    @staticmethod
    def ValueOf(value: int) -> LocationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.CAE
class LocationWithDir(Location): 
    """  Location With Direction interface. This defines connection locations with direction.  """
    @property
    def DirectionPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) DirectionPoint
         Returns the point of the direction definition end point.  
            
         
        """
        pass
    @DirectionPoint.setter
    def DirectionPoint(self, direction: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) DirectionPoint
         Returns the point of the direction definition end point.  
            
         
        """
        pass
    @property
    def DirectionType(self) -> LocationDirectionType:
        """
        Getter for property: ( LocationDirectionType NXOpen.CAE) DirectionType
         Returns the direction type   
            
         
        """
        pass
    @property
    def DirectionValue(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) DirectionValue
         Returns the direction value  
            
         
        """
        pass
    @property
    def DirectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DirectionVector
         Returns the direction definition vector   
            
         
        """
        pass
    @DirectionVector.setter
    def DirectionVector(self, direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DirectionVector
         Returns the direction definition vector   
            
         
        """
        pass
    @property
    def EndSelectionRecipe(self) -> NXOpen.CAE.SelectionRecipe:
        """
        Getter for property: ( NXOpen.CAE.SelectionRecipe) EndSelectionRecipe
         Returns the end selection recipe  
            
         
        """
        pass
    @EndSelectionRecipe.setter
    def EndSelectionRecipe(self, selectionRecipe: NXOpen.CAE.SelectionRecipe):
        """
        Setter for property: ( NXOpen.CAE.SelectionRecipe) EndSelectionRecipe
         Returns the end selection recipe  
            
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the point of the direction definition start point.  
            
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the point of the direction definition start point.  
            
         
        """
        pass
    @property
    def StartSelectionRecipe(self) -> NXOpen.CAE.SelectionRecipe:
        """
        Getter for property: ( NXOpen.CAE.SelectionRecipe) StartSelectionRecipe
         Returns the start selection recipe  
            
         
        """
        pass
    @StartSelectionRecipe.setter
    def StartSelectionRecipe(self, selectionRecipe: NXOpen.CAE.SelectionRecipe):
        """
        Setter for property: ( NXOpen.CAE.SelectionRecipe) StartSelectionRecipe
         Returns the start selection recipe  
            
         
        """
        pass
import NXOpen
class Location(NXOpen.TaggedObject): 
    """  Location base class. This defines connection locations with common properties like coordinates.  """
    def GetDetails(self) -> str:
        """
         Gets location details. 
         Returns details (str):  Location details .
        """
        pass
    def GetInfo(self) -> str:
        """
         Gets location info. 
         Returns info (str):  Location details .
        """
        pass
    def GetXyzCoordinates(self) -> List[NXOpen.Point3d]:
        """
         Gets the coordinates from the specified location.
                        The location can be any type: coordinates, node or point.
                        Its coordinates will be returned. 
         Returns coordinates ( NXOpen.Point3d Li):  Location coordinates .
        """
        pass
import NXOpen
class LumpedMass(IConnection): 
    """ Lumped Mass. Use this interface to setget properties and parameters of the lumped mass.  """
    @property
    def Center(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) Center
         Returns the target center   
            
         
        """
        pass
    @Center.setter
    def Center(self, center: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) Center
         Returns the target center   
            
         
        """
        pass
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @property
    def ExpansionRadiusFactorTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExpansionRadiusFactorTolerance
         Returns the expansion radius factor   
            
         
        """
        pass
    @property
    def ExpansionRadiusTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExpansionRadiusTolerance
         Returns the expansion radius   
            
         
        """
        pass
    @property
    def InertiaXX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaXX
         Returns the inertia XX.  
             
         
        """
        pass
    @property
    def InertiaYX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaYX
         Returns the inertia XY.  
             
         
        """
        pass
    @property
    def InertiaYY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaYY
         Returns the inertia YY.  
             
         
        """
        pass
    @property
    def InertiaZX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaZX
         Returns the inertia XZ.  
             
         
        """
        pass
    @property
    def InertiaZY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaZY
         Returns the inertia YZ.  
             
         
        """
        pass
    @property
    def InertiaZZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaZZ
         Returns the inertia ZZ.  
             
         
        """
        pass
    @property
    def LocalSpiderCenterType(self) -> LocalSpiderCenterType:
        """
        Getter for property: ( LocalSpiderCenterType NXOpen.CAE) LocalSpiderCenterType
         Returns the local spider center type   
            
         
        """
        pass
    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, localSpiderCenterType: LocalSpiderCenterType):
        """
        Setter for property: ( LocalSpiderCenterType NXOpen.CAE) LocalSpiderCenterType
         Returns the local spider center type   
            
         
        """
        pass
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Mass
         Returns the mass value   
            
         
        """
        pass
    @property
    def MassCenterType(self) -> MassCenterType:
        """
        Getter for property: ( MassCenterType NXOpen.CAE) MassCenterType
         Returns the mass center type   
            
         
        """
        pass
    @MassCenterType.setter
    def MassCenterType(self, massCenterType: MassCenterType):
        """
        Setter for property: ( MassCenterType NXOpen.CAE) MassCenterType
         Returns the mass center type   
            
         
        """
        pass
    @property
    def MassConnectivityType(self) -> MassConnectivityType:
        """
        Getter for property: ( MassConnectivityType NXOpen.CAE) MassConnectivityType
         Returns the mass connection type   
            
         
        """
        pass
    @MassConnectivityType.setter
    def MassConnectivityType(self, type: MassConnectivityType):
        """
        Setter for property: ( MassConnectivityType NXOpen.CAE) MassConnectivityType
         Returns the mass connection type   
            
         
        """
        pass
    @property
    def MassDistributionType(self) -> MassDistributionType:
        """
        Getter for property: ( MassDistributionType NXOpen.CAE) MassDistributionType
         Returns the mass distribution type   
            
         
        """
        pass
    @MassDistributionType.setter
    def MassDistributionType(self, type: MassDistributionType):
        """
        Setter for property: ( MassDistributionType NXOpen.CAE) MassDistributionType
         Returns the mass distribution type   
            
         
        """
        pass
    @property
    def MassTypeValue(self) -> MassType:
        """
        Getter for property: ( MassType NXOpen.CAE) MassTypeValue
         Returns the mass type   
            
         
        """
        pass
    @MassTypeValue.setter
    def MassTypeValue(self, type: MassType):
        """
        Setter for property: ( MassType NXOpen.CAE) MassTypeValue
         Returns the mass type   
            
         
        """
        pass
    @property
    def MaxDistanceTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDistanceTolerance
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    @property
    def PanelSearchDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PanelSearchDistance
         Returns the panel search distance   
            
         
        """
        pass
    @property
    def PanelSearchType(self) -> PanelSearchType:
        """
        Getter for property: ( PanelSearchType NXOpen.CAE) PanelSearchType
         Returns the panel search type  
            
         
        """
        pass
    @PanelSearchType.setter
    def PanelSearchType(self, type: PanelSearchType):
        """
        Setter for property: ( PanelSearchType NXOpen.CAE) PanelSearchType
         Returns the panel search type  
            
         
        """
        pass
    @property
    def RingSearchType(self) -> RingSearchType:
        """
        Getter for property: ( RingSearchType NXOpen.CAE) RingSearchType
         Returns the search tolerance type  
            
         
        """
        pass
    @RingSearchType.setter
    def RingSearchType(self, type: RingSearchType):
        """
        Setter for property: ( RingSearchType NXOpen.CAE) RingSearchType
         Returns the search tolerance type  
            
         
        """
        pass
class MassCenterType(Enum):
    """
    Members Include: 
     |Manual|  CoG is picked by selection 
     |FromDefinedSpiderLegs|  Use the CoG from the definition legs 
     |FromComputedSpiderLegs|  Use the CoG from the computed legs 

    """
    Manual: int
    FromDefinedSpiderLegs: int
    FromComputedSpiderLegs: int
    @staticmethod
    def ValueOf(value: int) -> MassCenterType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class MassConnectivityType(Enum):
    """
    Members Include: 
     |NearestNodes|  nearest nodes on defined panels 
     |LocalSpiders|  locally created spiders 

    """
    NearestNodes: int
    LocalSpiders: int
    @staticmethod
    def ValueOf(value: int) -> MassConnectivityType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class MassDistributionType(Enum):
    """
    Members Include: 
     |Distributed|  Mass is distributed on selected nodes 
     |Repeated|  Mass is applied at the defined value on each node  

    """
    Distributed: int
    Repeated: int
    @staticmethod
    def ValueOf(value: int) -> MassDistributionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class MassType(Enum):
    """
    Members Include: 
     |OnNodes|  Mass applied on selected nodes 
     |WithSpiders|  Mass with defined spider 

    """
    OnNodes: int
    WithSpiders: int
    @staticmethod
    def ValueOf(value: int) -> MassType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class MaterialType(Enum):
    """
    Members Include: 
     |User|  User defined material 
     |FromSupport|  Material defined from support 
     |NotSet|  No material required 

    """
    User: int
    FromSupport: int
    NotSet: int
    @staticmethod
    def ValueOf(value: int) -> MaterialType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen.CAE
class MeshPointLocation(Location): 
    """  This defines Mesh Point Location used by Universal Connections.  """
    @property
    def MeshPoint(self) -> NXOpen.CAE.MeshPoint:
        """
        Getter for property: ( NXOpen.CAE.MeshPoint) MeshPoint
         Returns the Mesh Point used for creating the location.  
          
                        If the location type is not mesh point, this method will raise an error.   
         
        """
        pass
    @MeshPoint.setter
    def MeshPoint(self, point: NXOpen.CAE.MeshPoint):
        """
        Setter for property: ( NXOpen.CAE.MeshPoint) MeshPoint
         Returns the Mesh Point used for creating the location.  
          
                        If the location type is not mesh point, this method will raise an error.   
         
        """
        pass
class ModelizationPPTRefTargetType(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |Ec|  Element collector 
     |Ecc|  Element collector container 
     |Ead|  Element Associated Data 

    """
    NotSet: int
    Ec: int
    Ecc: int
    Ead: int
    @staticmethod
    def ValueOf(value: int) -> ModelizationPPTRefTargetType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ModelizationResultType(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |Material|  Material 
     |Weights|  Interpolation element weights 
     |Section|  Section 
     |Csys|  Csys 
     |Stiffness|  Stiffness 
     |ViscousDamping|  ViscousDamping 
     |StructuralDamping|  StructuralDamping 
     |Dofs|  Dofs 
     |DynamicStiffness|  Dynamic Stiffness 
     |DynamicViscousDamping|  Dynamic ViscousDamping 
     |DynamicStructuralDamping|  Dynamic StructuralDamping 
     |Friction|  Friction 
     |Contact|  Contact 
     |Mass|  Mass 
     |NonlinearStiffness|  Nonlinear Stiffness 
     |NonlinearDamping|  Nonlinear Damping 
     |Thickness|  Thickness 

    """
    NotSet: int
    Material: int
    Weights: int
    Section: int
    Csys: int
    Stiffness: int
    ViscousDamping: int
    StructuralDamping: int
    Dofs: int
    DynamicStiffness: int
    DynamicViscousDamping: int
    DynamicStructuralDamping: int
    Friction: int
    Contact: int
    Mass: int
    NonlinearStiffness: int
    NonlinearDamping: int
    Thickness: int
    @staticmethod
    def ValueOf(value: int) -> ModelizationResultType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class NodalPairingMethod(Enum):
    """
    Members Include: 
     |Proximity|  Proximity 
     |OrientatedSearch|  Oriented Search 
     |SelectionOrder|  Selection Order 

    """
    Proximity: int
    OrientatedSearch: int
    SelectionOrder: int
    @staticmethod
    def ValueOf(value: int) -> NodalPairingMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class NodalTargetCenterType(Enum):
    """
    Members Include: 
     |Manual|  CoG is picked by selection 
     |FromComputedSpiderLegs|  Use the CoG from the computed legs 
     |Coincident|  The CoG is coincident with the other target CoG 
     |FromDefinedSpiderLegs|  Use the CoG from the definition legs 

    """
    Manual: int
    FromComputedSpiderLegs: int
    Coincident: int
    FromDefinedSpiderLegs: int
    @staticmethod
    def ValueOf(value: int) -> NodalTargetCenterType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class NodalTargetLocalSpider(NodalTarget): 
    """  This is the Local Spider Nodal Target.  """
    @property
    def CenterType(self) -> NodalTargetCenterType:
        """
        Getter for property: ( NodalTargetCenterType NXOpen.CAE) CenterType
         Returns the target center type   
            
         
        """
        pass
    @CenterType.setter
    def CenterType(self, centerType: NodalTargetCenterType):
        """
        Setter for property: ( NodalTargetCenterType NXOpen.CAE) CenterType
         Returns the target center type   
            
         
        """
        pass
    @property
    def ExpansionRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExpansionRadius
         Returns the Expansion Radius   
            
         
        """
        pass
    @property
    def ExpansionRadiusFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExpansionRadiusFactor
         Returns the Expansion Radius Factor   
            
         
        """
        pass
    @property
    def LocalSpiderCenterType(self) -> LocalSpiderCenterType:
        """
        Getter for property: ( LocalSpiderCenterType NXOpen.CAE) LocalSpiderCenterType
         Returns the Local Spider Center type   
            
         
        """
        pass
    @LocalSpiderCenterType.setter
    def LocalSpiderCenterType(self, localSpiderCenterType: LocalSpiderCenterType):
        """
        Setter for property: ( LocalSpiderCenterType NXOpen.CAE) LocalSpiderCenterType
         Returns the Local Spider Center type   
            
         
        """
        pass
    @property
    def MaxDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDistance
         Returns the Maximum Distance   
            
         
        """
        pass
    @property
    def PanelSearchType(self) -> PanelSearchType:
        """
        Getter for property: ( PanelSearchType NXOpen.CAE) PanelSearchType
         Returns the Panel Search type   
            
         
        """
        pass
    @PanelSearchType.setter
    def PanelSearchType(self, panelSearchType: PanelSearchType):
        """
        Setter for property: ( PanelSearchType NXOpen.CAE) PanelSearchType
         Returns the Panel Search type   
            
         
        """
        pass
    @property
    def RingSearchType(self) -> RingSearchType:
        """
        Getter for property: ( RingSearchType NXOpen.CAE) RingSearchType
         Returns the Ring Search type   
            
         
        """
        pass
    @RingSearchType.setter
    def RingSearchType(self, ringSearchType: RingSearchType):
        """
        Setter for property: ( RingSearchType NXOpen.CAE) RingSearchType
         Returns the Ring Search type   
            
         
        """
        pass
    @property
    def SearchTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchTolerance
         Returns the Search Tolerance   
            
         
        """
        pass
    @property
    def TargetCenter(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) TargetCenter
         Returns the target center   
            
         
        """
        pass
    @TargetCenter.setter
    def TargetCenter(self, center: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) TargetCenter
         Returns the target center   
            
         
        """
        pass
class NodalTargetSetOfPoints(NodalTarget): 
    """  Set of Points Target. Use this interface to setget parameters of the Set of Points Target type.  """
    pass
import NXOpen
class NodalTargetSinglePoint(NodalTarget): 
    """  Group of Points Target. Use this interface to setget parameters of the Group of Points Target type.  """
    @property
    def TargetCenter(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) TargetCenter
         Returns the target center   
            
         
        """
        pass
    @TargetCenter.setter
    def TargetCenter(self, center: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) TargetCenter
         Returns the target center   
            
         
        """
        pass
import NXOpen
class NodalTargetSpider(NodalTarget): 
    """  Group of Points Target. Use this interface to setget parameters of the Group of Points Target type.  """
    @property
    def CenterType(self) -> NodalTargetCenterType:
        """
        Getter for property: ( NodalTargetCenterType NXOpen.CAE) CenterType
         Returns the target center type   
            
         
        """
        pass
    @CenterType.setter
    def CenterType(self, centerType: NodalTargetCenterType):
        """
        Setter for property: ( NodalTargetCenterType NXOpen.CAE) CenterType
         Returns the target center type   
            
         
        """
        pass
    @property
    def TargetCenter(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) TargetCenter
         Returns the target center   
            
         
        """
        pass
    @TargetCenter.setter
    def TargetCenter(self, center: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) TargetCenter
         Returns the target center   
            
         
        """
        pass
class NodalTargetType(Enum):
    """
    Members Include: 
     |SinglePoint|  Single Point 
     |SetOfPoints|  Set of Points 
     |Spider|  Spider 
     |NotSet|  None 
     |LocalSpider|  Local Spider 

    """
    SinglePoint: int
    SetOfPoints: int
    Spider: int
    NotSet: int
    LocalSpider: int
    @staticmethod
    def ValueOf(value: int) -> NodalTargetType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class NodalTarget(NXOpen.NXObject): 
    """  This class represents an Interface to the Connection Target.  """
    @property
    def TargetType(self) -> NodalTargetType:
        """
        Getter for property: ( NodalTargetType NXOpen.CAE) TargetType
         Returns the target type   
            
         
        """
        pass
import NXOpen.CAE
class NodeLocation(Location): 
    """  Location interface. This defines connection locations with common properties like coordinates.  """
    @property
    def Node(self) -> NXOpen.CAE.FENode:
        """
        Getter for property: ( NXOpen.CAE.FENode) Node
         Returns the FEM node used for creating the location.  
          
                        If the location type is not node, this method will raise an error.   
         
        """
        pass
    @Node.setter
    def Node(self, node: NXOpen.CAE.FENode):
        """
        Setter for property: ( NXOpen.CAE.FENode) Node
         Returns the FEM node used for creating the location.  
          
                        If the location type is not node, this method will raise an error.   
         
        """
        pass
import NXOpen.CAE
class NodeSeriesLocation(Location): 
    """  Location interface. This defines connection locations with common properties like coordinates.  """
    def AddNodes(self, nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Add location nodes. 
        """
        pass
    def GetNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Retrieve location nodes. 
         Returns nodes ( NXOpen.CAE.FENode Li):  Node used for location .
        """
        pass
    def SetNodes(self, nodes: List[NXOpen.CAE.FENode]) -> None:
        """
         Set location nodes. 
        """
        pass
class NutDiameterType(Enum):
    """
    Members Include: 
     |User|  User defined diameter 
     |FactorOfDiameter|  User defined relationship with bolt head diameter 

    """
    User: int
    FactorOfDiameter: int
    @staticmethod
    def ValueOf(value: int) -> NutDiameterType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class PanelSearchType(Enum):
    """
    Members Include: 
     |NearestSelectedPanel|  Apply on the closest panel 
     |AllSelectedPanels|  Apply on all selected panels 

    """
    NearestSelectedPanel: int
    AllSelectedPanels: int
    @staticmethod
    def ValueOf(value: int) -> PanelSearchType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class PointLocation(Location): 
    """  Location interface. This defines connection locations with common properties like coordinates.  """
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the POINT used for creating the location.  
          
                        If the location type is not point, this method will raise an error.   
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the POINT used for creating the location.  
          
                        If the location type is not point, this method will raise an error.   
         
        """
        pass
import NXOpen
class PointSeriesLocation(Location): 
    """  Location interface. This defines connection locations with common properties like coordinates.  """
    def AddPoints(self, points: List[NXOpen.Point]) -> None:
        """
         Add location nodes. 
        """
        pass
    def GetPoints(self) -> List[NXOpen.Point]:
        """
         Retrieve location points. 
         Returns points ( NXOpen.Point Li):  Points used for location .
        """
        pass
    def SetPoints(self, points: List[NXOpen.Point]) -> None:
        """
         Set location points. 
        """
        pass
import NXOpen
class Rigid(IConnection): 
    """ Rigid connection. Use this interface to setget properties and parameters of the Rigid connection.  """
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchConeAngle
         Returns the search cone angle   
            
         
        """
        pass
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchRange
         Returns the search range   
            
         
        """
        pass
class RingSearchType(Enum):
    """
    Members Include: 
     |OneRing|  One Ring 
     |TwoRings|  Two Rings 
     |ExpansionRadius|  Search by exansion radius 
     |ExpansionRadiusFactor|  Search by exansion radius factor 

    """
    OneRing: int
    TwoRings: int
    ExpansionRadius: int
    ExpansionRadiusFactor: int
    @staticmethod
    def ValueOf(value: int) -> RingSearchType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class Rivet(IConnection): 
    """ Rivet connection. Use this interface to setget properties and parameters of the rivet connection.  """
    @property
    def Coefficient(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Coefficient
         Returns the coefficient for formula defined diameter   
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the connection diameter   
            
         
        """
        pass
    @property
    def DiameterType(self) -> DiameterType:
        """
        Getter for property: ( DiameterType NXOpen.CAE) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: ( DiameterType NXOpen.CAE) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromStart
         Returns the line Discretization distance from start   
            
         
        """
        pass
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceToEnd
         Returns the line Discretization distance to end   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height value   
            
         
        """
        pass
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LengthStep
         Returns the line Discretization length step   
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxAngleBetweenNormals
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDistCGToElemCG
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxLengthStep
         Returns the line Discretization max length step   
            
         
        """
        pass
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxNormalDistCGToFlanges
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProjectTolerance
         Returns the projection tolerance   
            
         
        """
        pass
    @property
    def TableFile(self) -> str:
        """
        Getter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
import NXOpen
class Sealing(IConnection): 
    """  Sealing connection. Use this interface to setget properties and parameters of the spot weld connection.  """
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromStart
         Returns the line Discretization distance from start   
            
         
        """
        pass
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceToEnd
         Returns the line Discretization distance to end   
            
         
        """
        pass
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LengthStep
         Returns the line Discretization length step   
            
         
        """
        pass
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Mass
         Returns the mass value   
            
         
        """
        pass
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxAngleBetweenNormals
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDistCGToElemCG
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxLengthStep
         Returns the line Discretization max length step   
            
         
        """
        pass
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxNormalDistCGToFlanges
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProjectTolerance
         Returns the projection tolerance   
            
         
        """
        pass
    @property
    def RxStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RxStiffnessConstant
         Returns the RX stiffness constant   
            
         
        """
        pass
    @property
    def RyStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RyStiffnessConstant
         Returns the RY stiffness constant   
            
         
        """
        pass
    @property
    def RzStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzStiffnessConstant
         Returns the RZ stiffness constant   
            
         
        """
        pass
    @property
    def StiffnessType(self) -> StiffnessType:
        """
        Getter for property: ( StiffnessType NXOpen.CAE) StiffnessType
         Returns the stiffness type   
            
         
        """
        pass
    @StiffnessType.setter
    def StiffnessType(self, oStiffnessType: StiffnessType):
        """
        Setter for property: ( StiffnessType NXOpen.CAE) StiffnessType
         Returns the stiffness type   
            
         
        """
        pass
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    @property
    def WithOrientation(self) -> bool:
        """
        Getter for property: (bool) WithOrientation
         Returns the target type   
            
         
        """
        pass
    @WithOrientation.setter
    def WithOrientation(self, orientation: bool):
        """
        Setter for property: (bool) WithOrientation
         Returns the target type   
            
         
        """
        pass
    @property
    def XStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XStiffnessConstant
         Returns the X stiffness constant   
            
         
        """
        pass
    @property
    def YStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YStiffnessConstant
         Returns the Y stiffness constant   
            
         
        """
        pass
    @property
    def ZStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZStiffnessConstant
         Returns the Z stiffness constant   
            
         
        """
        pass
class SeamWeldLocationType(Enum):
    """
    Members Include: 
     |Vector| 
     |Flange1Side1| 
     |Flange1Side2| 
     |Flange2Side1| 
     |Flange2Side2| 

    """
    Vector: int
    Flange1Side1: int
    Flange1Side2: int
    Flange2Side1: int
    Flange2Side2: int
    @staticmethod
    def ValueOf(value: int) -> SeamWeldLocationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class SeamWeldMaterialType(Enum):
    """
    Members Include: 
     |Angle|  Seam weld angle material type 
     |Overlap|  Seam weld overlap material type 
     |Double|  Seam weld double material type 

    """
    Angle: int
    Overlap: int
    Double: int
    @staticmethod
    def ValueOf(value: int) -> SeamWeldMaterialType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class SeamWeldMcfType(Enum):
    """
    Members Include: 
     |Other|  Unspecified 
     |YJoint|  Y-Joint 
     |OverlapWeld|  Overlap Weld 
     |CornerWeld|  Corner Weld 
     |ButtJoint|  Butt Joint 
     |EdgeWeld|  Edge Weld 
     |DoubleCornerWeld|  Corner Weld (Double) 
     |CruciformJoint|  Cruciform Joint 
     |KJoint|  K-Joint 
     |IWeld|  I-Weld 
     |SplitIWeld|  Split I-Weld 

    """
    Other: int
    YJoint: int
    OverlapWeld: int
    CornerWeld: int
    ButtJoint: int
    EdgeWeld: int
    DoubleCornerWeld: int
    CruciformJoint: int
    KJoint: int
    IWeld: int
    SplitIWeld: int
    @staticmethod
    def ValueOf(value: int) -> SeamWeldMcfType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class SeamWeldNodeSelectionMethod(Enum):
    """
    Members Include: 
     |ConnectionNodes|  Use the node locations in the USWC(s) 
     |Specify|  Explicitly specify nodes or a node group 

    """
    ConnectionNodes: int
    Specify: int
    @staticmethod
    def ValueOf(value: int) -> SeamWeldNodeSelectionMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class SeamWeldSectionType(Enum):
    """
    Members Include: 
     |Undefined| 
     |I| 
     |V| 
     |U| 
     |X| 
     |Y| 
     |Hv| 
     |Hy| 
     |Fillet| 
     |Radius| 

    """
    Undefined: int
    I: int
    V: int
    U: int
    X: int
    Y: int
    Hv: int
    Hy: int
    Fillet: int
    Radius: int
    @staticmethod
    def ValueOf(value: int) -> SeamWeldSectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class SeamWeldShapeType(Enum):
    """
    Members Include: 
     |Undefined| 
     |Straight| 
     |Convex| 
     |Concave| 

    """
    Undefined: int
    Straight: int
    Convex: int
    Concave: int
    @staticmethod
    def ValueOf(value: int) -> SeamWeldShapeType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class SeamWeldSide(Enum):
    """
    Members Include: 
     |OnLargerSheetAngle|  Weld on Side of the Larger Sheet Angle 
     |OnSmallerSheetAngle|  Weld on Side of the Smaller Sheet Angle 
     |OnBothSheetSides|  Weld on Both Sides 

    """
    OnLargerSheetAngle: int
    OnSmallerSheetAngle: int
    OnBothSheetSides: int
    @staticmethod
    def ValueOf(value: int) -> SeamWeldSide:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class SeamWeldType(Enum):
    """
    Members Include: 
     |WithMaterial|  Seam weld done with material 
     |WithLaser|  Seam weld done by laser 
     |Resistance|  Seam weld done by resistance welding 
     |Friction|  Seam weld done by friction welding 
     |Brazing|  Seam weld done by braze welding 

    """
    WithMaterial: int
    WithLaser: int
    Resistance: int
    Friction: int
    Brazing: int
    @staticmethod
    def ValueOf(value: int) -> SeamWeldType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class SeamWeld(IConnection): 
    """  Seam Weld connection. Use this interface to setget properties and parameters of the seam weld connection.  """
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromStart
         Returns the line Discretization distance from start   
            
         
        """
        pass
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceToEnd
         Returns the line Discretization distance to end   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height value   
            
         
        """
        pass
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LengthStep
         Returns the line Discretization length step   
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxAngleBetweenNormals
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDistCGToElemCG
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxLengthStep
         Returns the line Discretization max length step   
            
         
        """
        pass
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxNormalDistCGToFlanges
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProjectTolerance
         Returns the projection tolerance   
            
         
        """
        pass
    @property
    def SeamWeldMcfType(self) -> SeamWeldMcfType:
        """
        Getter for property: ( SeamWeldMcfType NXOpen.CAE) SeamWeldMcfType
         Returns the seam weld MCF type   
            
         
        """
        pass
    @SeamWeldMcfType.setter
    def SeamWeldMcfType(self, seamWeldMcfType: SeamWeldMcfType):
        """
        Setter for property: ( SeamWeldMcfType NXOpen.CAE) SeamWeldMcfType
         Returns the seam weld MCF type   
            
         
        """
        pass
    @property
    def SeamWeldType(self) -> SeamWeldType:
        """
        Getter for property: ( SeamWeldType NXOpen.CAE) SeamWeldType
         Returns the seam weld type   
            
         
        """
        pass
    @SeamWeldType.setter
    def SeamWeldType(self, seamWeldType: SeamWeldType):
        """
        Setter for property: ( SeamWeldType NXOpen.CAE) SeamWeldType
         Returns the seam weld type   
            
         
        """
        pass
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width value   
            
         
        """
        pass
    def ConvertToFlangeSideLocationType(self, weldIndex: int) -> None:
        """
         Convert to Flange-Side location type.
        """
        pass
    def ConvertToVectorLocationType(self, weldIndex: int) -> None:
        """
         Convert to Vector location type.
        """
        pass
    def GetDefaultWeldAngle(self) -> NXOpen.Expression:
        """
         Get default weld angle.
         Returns defaultAngle ( NXOpen.Expression): .
        """
        pass
    def GetDefaultWeldPenetration(self) -> NXOpen.Expression:
        """
         Get default weld penetration.
         Returns defaultPenetration ( NXOpen.Expression): .
        """
        pass
    def GetDefaultWeldThickness(self) -> NXOpen.Expression:
        """
         Get default weld thickness.
         Returns defaultThickness ( NXOpen.Expression): .
        """
        pass
    def GetDefaultWeldWidth(self) -> NXOpen.Expression:
        """
         Get default weld width.
         Returns defaultWidth ( NXOpen.Expression): .
        """
        pass
    def GetMinMaxNumberOfWelds(self) -> Tuple[int, int]:
        """
         Get minimum and maximum number of welds in a Seam Weld connection 
         Returns A tuple consisting of (minNumWelds, maxNumWelds). 
         - minNumWelds is: int.
         - maxNumWelds is: int.

        """
        pass
    def GetNumberOfWelds(self) -> int:
        """
         Get the number of welds in a Seam Weld connection 
         Returns numWelds (int): .
        """
        pass
    def GetSeamWeldLocationParameter(self, weldIndex: int) -> float:
        """
         Get the seam weld Location parameter 
         Returns locationParameter (float): .
        """
        pass
    def GetSeamWeldLocationType(self, weldIndex: int) -> SeamWeldLocationType:
        """
         Get the seam weld Location type 
         Returns seamWeldLocationType ( SeamWeldLocationType NXOpen.CAE): .
        """
        pass
    def GetSeamWeldLocationVector(self, weldIndex: int) -> NXOpen.Direction:
        """
         Get the seam weld Location vector 
         Returns locationVector ( NXOpen.Direction): .
        """
        pass
    def GetSeamWeldMaterial(self, weldIndex: int) -> NXOpen.PhysicalMaterial:
        """
         Get the seam weld Material 
         Returns material ( NXOpen.PhysicalMaterial): .
        """
        pass
    def GetSeamWeldSectionType(self, weldIndex: int) -> SeamWeldSectionType:
        """
         Get the seam weld Section type 
         Returns seamWeldSectionType ( SeamWeldSectionType NXOpen.CAE): .
        """
        pass
    def GetSeamWeldShapeType(self, weldIndex: int) -> SeamWeldShapeType:
        """
         Get the seam weld Shape type 
         Returns seamWeldShapeType ( SeamWeldShapeType NXOpen.CAE): .
        """
        pass
    def GetWeldAngle(self, weldIndex: int) -> NXOpen.Expression:
        """
         Get the weld angle.
         Returns angle ( NXOpen.Expression): .
        """
        pass
    def GetWeldPenetration(self, weldIndex: int) -> NXOpen.Expression:
        """
         Get the weld penetration.
         Returns penetration ( NXOpen.Expression): .
        """
        pass
    def GetWeldThickness(self, weldIndex: int) -> NXOpen.Expression:
        """
         Get the weld thickness.
         Returns thickness ( NXOpen.Expression): .
        """
        pass
    def GetWeldWidth(self, weldIndex: int) -> NXOpen.Expression:
        """
         Get the weld width.
         Returns width ( NXOpen.Expression): .
        """
        pass
    def SetNumberOfWelds(self, numWelds: int) -> None:
        """
         Set the number of welds in a Seam Weld connection 
        """
        pass
    def SetSeamWeldLocationParameter(self, weldIndex: int, locationParameter: float) -> None:
        """
         Set the seam weld Location parameter 
        """
        pass
    def SetSeamWeldLocationType(self, weldIndex: int, seamWeldLocationType: SeamWeldLocationType) -> None:
        """
         Set the seam weld Location type 
        """
        pass
    def SetSeamWeldLocationVector(self, weldIndex: int, locationVector: NXOpen.Direction) -> None:
        """
         Set the seam weld Location vector 
        """
        pass
    def SetSeamWeldMaterial(self, weldIndex: int, material: NXOpen.PhysicalMaterial) -> None:
        """
         Set the seam weld Material 
        """
        pass
    def SetSeamWeldSectionType(self, weldIndex: int, seamWeldSectionType: SeamWeldSectionType) -> None:
        """
         Set the seam weld Section type 
        """
        pass
    def SetSeamWeldShapeType(self, weldIndex: int, seamWeldShapeType: SeamWeldShapeType) -> None:
        """
         Set the seam weld Shape type 
        """
        pass
import NXOpen.CAE
class SelectionRecipeLocation(Location): 
    """  Location interface. This defines connection locations with common properties like coordinates.  """
    @property
    def SelectionRecipe(self) -> NXOpen.CAE.SelectionRecipe:
        """
        Getter for property: ( NXOpen.CAE.SelectionRecipe) SelectionRecipe
         Returns the Selection Recipe used for creating the location.  
          
                        If the location type is not a Selection Recipe, this method will raise an error.   
         
        """
        pass
    @SelectionRecipe.setter
    def SelectionRecipe(self, selectionRecipe: NXOpen.CAE.SelectionRecipe):
        """
        Setter for property: ( NXOpen.CAE.SelectionRecipe) SelectionRecipe
         Returns the Selection Recipe used for creating the location.  
          
                        If the location type is not a Selection Recipe, this method will raise an error.   
         
        """
        pass
class ShankLengthDiscretizationType(Enum):
    """
    Members Include: 
     |NotSet|  No shank discretization for shank length 
     |UserDefined|  User defined length for shank discretization 
     |PercentLength|  Percentage of length for shank discretization 
     |PercentCurve|  Percentage of curve length for shank discretization 

    """
    NotSet: int
    UserDefined: int
    PercentLength: int
    PercentCurve: int
    @staticmethod
    def ValueOf(value: int) -> ShankLengthDiscretizationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ShankSegmentDiscretizationType(Enum):
    """
    Members Include: 
     |NotSet|  No shank discretization for shank segments 
     |SegmentLength|  Segment length for shank segment discretization 
     |NumSegments|  Number of segments for shank segment discretization 

    """
    NotSet: int
    SegmentLength: int
    NumSegments: int
    @staticmethod
    def ValueOf(value: int) -> ShankSegmentDiscretizationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class SmartTemplateBuilder(NXOpen.Object): 
    """ Contains smart template application utility methods """
    def GetSmartTemplateTool() -> SmartTemplateTool:
        """
         Create Smart template tools  
         Returns smartTemplateTool ( SmartTemplateTool NXOpen.CAE): .
        """
        pass
import NXOpen
import NXOpen.CAE
class SmartTemplateTool(NXOpen.TaggedObject): 
    """ Contains smart template application utility methods """
    def Destroy(self) -> None:
        """
         Destroy the smart template tool object 
        """
        pass
    def ExportPIDs(self, caePart: NXOpen.CAE.CaePart, iAbsoluteExportPath: str) -> None:
        """
         Export PIDs to Groups
        """
        pass
    def ExportResultDataToExcel(self, pSimSolution: NXOpen.CAE.SimSolution, iAbsoluteExportPath: str, resultName: str, drivingPoints: bool, indexFile: str) -> None:
        """
         Export the requested result data to an Excel file 
        """
        pass
    def ExportResults(self, pSimSolution: NXOpen.CAE.SimSolution, iAbsoluteExportPath: str) -> None:
        """
         Export SOL200 Design sensitivity analysis solution report
        """
        pass
    def GetGroupPhysicalPropertyTables(self, caeGroup: NXOpen.CAE.CaeGroup) -> List[NXOpen.CAE.PhysicalPropertyTable]:
        """
         Get Physical property tables associated to group
         Returns physicalPropertyTableTags ( NXOpen.CAE.PhysicalPropertyTable Li):  Group elements associated physical property tables. .
        """
        pass
    def GetHardPointNameAndType(self, iAbsoluteFilePath: str) -> Tuple[List[NXOpen.CAE.SelRecipeBaseStrategy.Type], List[str]]:
        """
         Get hard point name and associated type from the input file 
         Returns A tuple consisting of (listOfHardPointTypes, listOfHardPointNames). 
         - listOfHardPointTypes is:  NXOpen.CAE.SelRecipeBaseStrategy.Type Li.
         - listOfHardPointNames is: List[str].

        """
        pass
    @overload
    def ImportGroups(self, caePart: NXOpen.CAE.CaePart, iAbsoluteImportPath: str) -> List[NXOpen.CAE.CaeGroup]:
        """
         Import PIDs to xml file
         Returns caeGroups ( NXOpen.CAE.CaeGroup Li): .
        """
        pass
    @overload
    def ImportGroups(self, caePart: NXOpen.CAE.CaePart, iAbsoluteImportPath: str, selectedGroups: List[str]) -> List[NXOpen.CAE.CaeGroup]:
        """
         Import PIDs to xml file
         Returns caeGroups ( NXOpen.CAE.CaeGroup Li): .
        """
        pass
import NXOpen
class SpotWeld(IConnection): 
    """ Spot Weld connection. Use this interface to setget properties and parameters of the spot weld connection.  """
    @property
    def Coefficient(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Coefficient
         Returns the coefficient for formula defined diameter   
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the connection diameter   
            
         
        """
        pass
    @property
    def DiameterType(self) -> DiameterType:
        """
        Getter for property: ( DiameterType NXOpen.CAE) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    @DiameterType.setter
    def DiameterType(self, diameterType: DiameterType):
        """
        Setter for property: ( DiameterType NXOpen.CAE) DiameterType
         Returns the connection diameter type   
            
         
        """
        pass
    @property
    def DiscretizationMethod(self) -> DiscretizationMethod:
        """
        Getter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @DiscretizationMethod.setter
    def DiscretizationMethod(self, method: DiscretizationMethod):
        """
        Setter for property: ( DiscretizationMethod NXOpen.CAE) DiscretizationMethod
         Returns the discretization method   
            
         
        """
        pass
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromStart
         Returns the line Discretization distance from start   
            
         
        """
        pass
    @property
    def DistanceToEnd(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceToEnd
         Returns the line Discretization distance to end   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height value   
            
         
        """
        pass
    @property
    def HeightType(self) -> HeightType:
        """
        Getter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @HeightType.setter
    def HeightType(self, heightType: HeightType):
        """
        Setter for property: ( HeightType NXOpen.CAE) HeightType
         Returns the connection height type   
            
         
        """
        pass
    @property
    def LengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LengthStep
         Returns the line Discretization length step   
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) Material
         Returns the connection material   
            
         
        """
        pass
    @property
    def MaxAngleBetweenNormals(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxAngleBetweenNormals
         Returns the maximum angle of normals with the projection surface   
            
         
        """
        pass
    @property
    def MaxDistCGToElemCG(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDistCGToElemCG
         Returns the maximum distance from definition point to center of support element   
            
         
        """
        pass
    @property
    def MaxLengthStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxLengthStep
         Returns the line Discretization max length step   
            
         
        """
        pass
    @property
    def MaxNormalDistCGToFlanges(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxNormalDistCGToFlanges
         Returns the maximum normal distance from definition point to center of element   
            
         
        """
        pass
    @property
    def NumberOfDiscretizationPoints(self) -> int:
        """
        Getter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @NumberOfDiscretizationPoints.setter
    def NumberOfDiscretizationPoints(self, num: int):
        """
        Setter for property: (int) NumberOfDiscretizationPoints
         Returns the number of connections   
            
         
        """
        pass
    @property
    def NumberOfFlanges(self) -> int:
        """
        Getter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @NumberOfFlanges.setter
    def NumberOfFlanges(self, numberOfFlanges: int):
        """
        Setter for property: (int) NumberOfFlanges
         Returns the number of flanges.  
           When changing the number of flanges this is not applied till an update is performed by calling  Update::DoUpdate    
         
        """
        pass
    @property
    def ProjectTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProjectTolerance
         Returns the projection tolerance   
            
         
        """
        pass
    @property
    def TableFile(self) -> str:
        """
        Getter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    @TableFile.setter
    def TableFile(self, tableFile: str):
        """
        Setter for property: (str) TableFile
         Returns the table file used to compute the diameter   
            
         
        """
        pass
    @property
    def UseMaxLengthStep(self) -> bool:
        """
        Getter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @UseMaxLengthStep.setter
    def UseMaxLengthStep(self, use: bool):
        """
        Setter for property: (bool) UseMaxLengthStep
         Returns the usage of max length step   
            
         
        """
        pass
    @property
    def UseOriginalNodesOfConnection(self) -> bool:
        """
        Getter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
    @UseOriginalNodesOfConnection.setter
    def UseOriginalNodesOfConnection(self, use: bool):
        """
        Setter for property: (bool) UseOriginalNodesOfConnection
         Returns the usage of original nodes of connection   
            
         
        """
        pass
import NXOpen
class Spring(IConnection): 
    """ Spring connection. Use this interface to setget properties and parameters of the Spring connection.  """
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @property
    def CsysType(self) -> CsysType:
        """
        Getter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @CsysType.setter
    def CsysType(self, csysType: CsysType):
        """
        Setter for property: ( CsysType NXOpen.CAE) CsysType
         Returns the csys type   
            
         
        """
        pass
    @property
    def IsMassOnBothTargets(self) -> bool:
        """
        Getter for property: (bool) IsMassOnBothTargets
         Returns the isMassOnBothTargets   
            
         
        """
        pass
    @IsMassOnBothTargets.setter
    def IsMassOnBothTargets(self, isMassOnBothTargets: bool):
        """
        Setter for property: (bool) IsMassOnBothTargets
         Returns the isMassOnBothTargets   
            
         
        """
        pass
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Mass
         Returns the mass value   
            
         
        """
        pass
    @property
    def PairingMethod(self) -> NodalPairingMethod:
        """
        Getter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @PairingMethod.setter
    def PairingMethod(self, method: NodalPairingMethod):
        """
        Setter for property: ( NodalPairingMethod NXOpen.CAE) PairingMethod
         Returns the pairing method of targets   
            
         
        """
        pass
    @property
    def RxStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RxStiffnessConstant
         Returns the RX stiffness constant   
            
         
        """
        pass
    @property
    def RyStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RyStiffnessConstant
         Returns the RY stiffness constant   
            
         
        """
        pass
    @property
    def RzStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RzStiffnessConstant
         Returns the RZ stiffness constant   
            
         
        """
        pass
    @property
    def SearchConeAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchConeAngle
         Returns the search cone angle   
            
         
        """
        pass
    @property
    def SearchOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @SearchOrientation.setter
    def SearchOrientation(self, orientation: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SearchOrientation
         Returns the pairing search orientation   
            
         
        """
        pass
    @property
    def SearchRange(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchRange
         Returns the search range   
            
         
        """
        pass
    @property
    def StiffnessType(self) -> StiffnessType:
        """
        Getter for property: ( StiffnessType NXOpen.CAE) StiffnessType
         Returns the stiffness type   
            
         
        """
        pass
    @StiffnessType.setter
    def StiffnessType(self, oStiffnessType: StiffnessType):
        """
        Setter for property: ( StiffnessType NXOpen.CAE) StiffnessType
         Returns the stiffness type   
            
         
        """
        pass
    @property
    def XStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XStiffnessConstant
         Returns the X stiffness constant   
            
         
        """
        pass
    @property
    def YStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YStiffnessConstant
         Returns the Y stiffness constant   
            
         
        """
        pass
    @property
    def ZStiffnessConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZStiffnessConstant
         Returns the Z stiffness constant   
            
         
        """
        pass
class StiffnessType(Enum):
    """
    Members Include: 
     |PerElement|  Stiffness value will be specified per element 
     |PerUnitLength|  Stiffness value will be specified per unit length 

    """
    PerElement: int
    PerUnitLength: int
    @staticmethod
    def ValueOf(value: int) -> StiffnessType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class TargetDependencyType(Enum):
    """
    Members Include: 
     |NotSet|  No dependency 
     |Dependent|  Dependent target 
     |Independent|  Independent target 

    """
    NotSet: int
    Dependent: int
    Independent: int
    @staticmethod
    def ValueOf(value: int) -> TargetDependencyType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class UniversalConnectionState(Enum):
    """
    Members Include: 
     |Unknown|  Connection state cannot be determined 
     |Meshed|  The Connection is meshed 
     |NotMeshed|  The Connection is not meshed 
     |Invalid|  The Connection is not valid 

    """
    Unknown: int
    Meshed: int
    NotMeshed: int
    Invalid: int
    @staticmethod
    def ValueOf(value: int) -> UniversalConnectionState:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.CAE
import NXOpen.Features
class Utils(NXOpen.Object): 
    """ Contains universal connections utility methods """
    def CreateLmieconnection(contextPart: NXOpen.INXObject) -> LMIEConnection:
        """
         Create standalone LMIEConnection 
         Returns opt ( LMIEConnection NXOpen.CAE):  The created standalone LMIEConnection .
        """
        pass
    def ExportLumpedMassInterchangeData(iConnections: List[LMIEConnection], iAbsoluteExportPath: str, iConvertConnectionDataFromPartUnits: bool) -> None:
        """
         Exports the intermediate connection representations of lumped mass connections to external file. File type is determined by the extension. 
        """
        pass
    def FilterConnectionsByType(iConnections: List[IConnection], type: ConnectionType) -> List[IConnection]:
        """
         Filters a list of connections by type 
         Returns oConnections ( IConnection List[NXOpen.C):  all connections matching the specified connection type .
        """
        pass
    def GetBodyFromFeature(feature: NXOpen.Features.Feature) -> List[NXOpen.Body]:
        """
         Get Bodies from Given Imported Feature 
         Returns body ( NXOpen.Body Li):  list of bodies of given imported feature .
        """
        pass
    def GetBoltSupportOfLocation(iBoltConnection: IConnection, locationIndex: int, coordinateIndex: int, boltSupportIndex: int) -> NXOpen.TaggedObject:
        """
         Retrieve object at projection of a Bolt Universal Connection  
         Returns boltSupportObject ( NXOpen.TaggedObject):  The Support Object .
        """
        pass
    def GetCoordinatesFromConstraintFile(constraintFilePath: str) -> List[NXOpen.Point3d]:
        """
         Get XYZ Coordinates from Constraint File 
         Returns coordinates ( NXOpen.Point3d Li):  The array of the coordinates read from constraint file .
        """
        pass
    def GetElemLabels(feModel: NXOpen.CAE.IFEModel, fromChildren: bool) -> List[int]:
        """
         Retrieve element labels from FeModel  
         Returns labels (List[int]):  The element labels .
        """
        pass
    def GetFeatureFromBody(body: NXOpen.Body) -> NXOpen.Features.Feature:
        """
         Get Feature from Given Imported Body 
         Returns feature ( NXOpen.Features.Feature):  Feature of given imported Body .
        """
        pass
    def GetFreeEdgesFromElementCollectors(feModel: NXOpen.CAE.IFEModel, iElementCollectors: List[NXOpen.CAE.Mesh]) -> List[NXOpen.CAE.FEElement]:
        """
         Retrieve free edges from element collectors  
         Returns freeEdges ( NXOpen.CAE.FEElement Li):  The Free Edges .
        """
        pass
    def GetInterchangeDataFromLumpedMass(conversionLengthUnit: NXOpen.Unit, conversionMassUnit: NXOpen.Unit, iConnections: List[LumpedMass], iAbsoluteExportPath: str) -> List[LMIEConnection]:
        """
         Returns the intermediate connection representations of lumped mass connections 
         Returns oConnections ( LMIEConnection List[NXOpen.C):  The intermediate connection representations .
        """
        pass
    def GetNodeLabels(feModel: NXOpen.CAE.IFEModel, fromChildren: bool) -> List[int]:
        """
         Retrieve node labels from FeModel  
         Returns labels (List[int]):  The node labels .
        """
        pass
    def GetObjectAtProjectionOfLocation(iConnection: IConnection, locationIndex: int, coordinateIndex: int, flangeIndex: int) -> NXOpen.TaggedObject:
        """
         Retrieve object at projection of a Universal Connection other than Bolt  
         Returns objectAtProjection ( NXOpen.TaggedObject):  The Object at projection .
        """
        pass
    def GetProjectionPoints(iConnections: List[IConnection]) -> Tuple[List[NXOpen.INXObject], List[NXOpen.Point3d], List[int]]:
        """
         Returns the projection points of the connections per geometry flanges
         Returns A tuple consisting of (oFlanges, oProjectionPoints, oFlangeObjectIndexList). 
         - oFlanges is:  NXOpen.INXObject Li. The array of the geometry flange objects .
         - oProjectionPoints is:  NXOpen.Point3d Li. The array of the projection points .
         - oFlangeObjectIndexList is: List[int]. The array of projection point index ranges per flanges. The size of the array is number of flanges + 1. For the flange i the index range is [oFlangeObjectIndexList[i], ..., oFlangeObjectIndexList[i + 1] - 1]. .

        """
        pass
    def GetProjectionPointsOnFaces(iConnections: List[IConnection]) -> Tuple[List[NXOpen.CAE.CAEFace], List[NXOpen.Point3d], List[int]]:
        """
         Returns the projection points of the connections per geometry faces
         Returns A tuple consisting of (oFaces, oProjectionPoints, oFaceObjectIndexList). 
         - oFaces is:  NXOpen.CAE.CAEFace Li. The array of the geometry face objects .
         - oProjectionPoints is:  NXOpen.Point3d Li. The array of the projection points .
         - oFaceObjectIndexList is: List[int]. The array of projection point index ranges per faces. The size of the array is number of faces + 1. For the face i the index range is [oFaceObjectIndexList[i], ..., oFaceObjectIndexList[i + 1] - 1]. .

        """
        pass
    def ImportLumpedMassInterchangeData(contextPart: NXOpen.INXObject, iAbsoluteImportPath: str) -> List[LMIEConnection]:
        """
         Imports the intermediate connection representations of lumped mass connections from external file. File type is determined by the extension. 
         Returns oConnections ( LMIEConnection List[NXOpen.C):  The intermediate connection representations .
        """
        pass
    def MapObject(femPart: NXOpen.CAE.FemPart, cadFeature: NXOpen.TaggedObject, syncGeomData: bool) -> NXOpen.TaggedObject:
        """
         Map CAD Prt geometry in FemPart 
         Returns caeFeature ( NXOpen.TaggedObject):  Mapped cad feature in FemPart .
        """
        pass
    def PrintConnectionElementInformationFile(connectionElement: Element) -> None:
        """
         Print the connection element's information file 
        """
        pass
    def PrintConnectionInformationFile(connection: IConnection) -> None:
        """
         Print the connection's information file 
        """
        pass
    def ReimportMesh() -> None:
        """
         Reimport mesh created by external mesher. The work part should be a FEM meshed with an external mesher. 
        """
        pass
    def RelabelAFEMPhysicalProperty(assyFemPart: NXOpen.CAE.AssyFemPart) -> None:
        """
         Redo labeling of current work AFEM physical properties. The work part should be a AFEM.  
        """
        pass
    def RelabelAfem() -> None:
        """
         Redo labeling of current work AFEM. The work part should be a AFEM.  
        """
        pass
    def RelabelAfmOffsets(assyFemPart: NXOpen.CAE.AssyFemPart, node_offset: int, elem_offset: int, csys_offset: int, phys_offset: int) -> None:
        """
         Relabel assembly FEM with offset start ID 
        """
        pass
    def RemeshCompatibleConnectionComponents(connections: List[IConnection]) -> None:
        """
         Remesh Seam Weld Connection Compatible Components 
        """
        pass
    def SearchNearestFlanges(iConnections: List[IConnection]) -> Tuple[List[NXOpen.INXObject], List[int]]:
        """
         Returns the nearest polygon geometry per connections when project failed 
         Returns A tuple consisting of (oNearestFlanges, oFlangeObjectIndices). 
         - oNearestFlanges is:  NXOpen.INXObject Li. The array of the geometry flange objects .
         - oFlangeObjectIndices is: List[int]. The array of nearest flange ranges per flanges. The size of the array is number of flanges + 1. For the flange i the index range is [oFlangeObjectIndexList[i], ..., oFlangeObjectIndexList[i + 1] - 1]. .

        """
        pass
    def SplitWarpedQuads() -> None:
        """
         Splits the warped quads by invoking an external mesher. The work part should be a FEM meshed with an external mesher. 
        """
        pass
    def WriteCoordinatesToConstraintFile(constraintFilePath: str, connectionName: str, coordinates: List[NXOpen.Point3d]) -> None:
        """
         Write XYZ Coordinates to Constraint File 
        """
        pass
